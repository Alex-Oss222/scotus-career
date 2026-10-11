"""Clerical, read-only extraction of the recorded OT1991--OT1995 corpus.

This catalogue describes documents and observed references, never legal force or
stage permission. A citation is a textual mention; a URL is not verification.
Record identities are new and path-based, not recovered historical library IDs.
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from datetime import date
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


class IngestError(ValueError):
    """An input cannot safely or unambiguously be consumed."""


def strict_mapping_json(text: str) -> dict:
    """Mappings contain only string fields; reject JSON coercion and key loss."""
    def object_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise IngestError(f"Duplicate mapping JSON key: {key}")
            result[key] = value
        return result

    def reject_number(value):
        raise IngestError(f"Mapping JSON does not permit numeric values: {value[:60]}")

    try:
        data = json.loads(text, object_pairs_hook=object_pairs,
                          parse_constant=reject_number, parse_float=reject_number,
                          parse_int=reject_number)
    except (json.JSONDecodeError, RecursionError) as exc:
        raise IngestError(f"Malformed mapping JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise IngestError("Mapping JSON root must be an object")
    return data


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def record_id(path: str) -> str:
    return "record-" + digest(path.encode("utf-8"))[:20]


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).casefold()
    return re.sub(r"[^\w]+", " ", text).strip()


def valid_date(value: str) -> str | None:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return None
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError:
        return None


def cells(line: str) -> list[str]:
    """Split Markdown cells without splitting escaped or inline-code pipes."""
    result, current, fence = [], [], 0
    i = 0
    while i < len(line):
        char = line[i]
        if char == "\\" and i + 1 < len(line):
            current.extend(line[i:i + 2]); i += 2; continue
        if char == "`":
            end = i
            while end < len(line) and line[end] == "`":
                end += 1
            count = end - i
            if fence == count:
                fence = 0
            elif not fence:
                fence = count
            current.append(line[i:end]); i = end; continue
        if char == "|" and not fence:
            result.append("".join(current).strip()); current = []
        else:
            current.append(char)
        i += 1
    result.append("".join(current).strip())
    if line.lstrip().startswith("|"):
        result = result[1:]
    if line.rstrip().endswith("|"):
        result = result[:-1]
    return result


def table_rows(text: str) -> list[dict]:
    """Keep exact labels, text, line numbers, and section for every table row."""
    lines = text.splitlines()
    output, headings = [], []
    i = 0
    while i < len(lines):
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", lines[i])
        if heading:
            level, title = len(heading[1]), heading[2]
            headings = [h for h in headings if h[0] < level] + [(level, title)]
        if i + 1 < len(lines) and "|" in lines[i]:
            labels, separators = cells(lines[i]), cells(lines[i + 1])
            if (labels and len(labels) == len(separators)
                    and all(re.fullmatch(r":?-{3,}:?", s.replace(" ", "")) for s in separators)):
                if len(labels) != len(set(labels)):
                    raise IngestError(f"Duplicate table labels at line {i + 1}")
                i += 2
                while i < len(lines):
                    # The two oldest append-only ledgers contain blank lines
                    # between batches without repeating their column header.
                    if not lines[i].strip():
                        next_row = i + 1
                        while next_row < len(lines) and not lines[next_row].strip():
                            next_row += 1
                        if (next_row < len(lines) and lines[next_row].lstrip().startswith("|")
                                and len(cells(lines[next_row])) == len(labels)
                                and not (next_row + 1 < len(lines) and all(
                                    re.fullmatch(r":?-{3,}:?", s.replace(" ", ""))
                                    for s in cells(lines[next_row + 1])))):
                            i = next_row
                        else:
                            break
                    if "|" not in lines[i] or not lines[i].lstrip().startswith("|"):
                        break
                    values = cells(lines[i])
                    if len(values) != len(labels):
                        raise IngestError(f"Malformed table row at line {i + 1}: {len(values)} cells for {len(labels)} labels")
                    output.append({"line": i + 1, "columns": dict(zip(labels, values)),
                                   "raw": lines[i], "section": " / ".join(h[1] for h in headings)})
                    i += 1
                continue
        i += 1
    return output


def field(row: dict, *names: str) -> str:
    columns = {normalize(k): v for k, v in row["columns"].items()}
    for name in names:
        if normalize(name) in columns:
            return columns[normalize(name)]
    return ""


def chunk_numbers(text: str) -> list[int]:
    return sorted({int(n) for n in re.findall(r"\b(?:OT_?\d{4})?CHUNK\s*(\d+)\b", text, re.I)})


def row_chunk(row: dict) -> list[int]:
    value = field(row, "Chunk")
    if value.isdigit():
        return [int(value)]
    return chunk_numbers(value or row.get("section", ""))


def sections(text: str) -> list[dict]:
    return [{"title": m[2].strip(), "line": i, "level": len(m[1])}
            for i, line in enumerate(text.splitlines(), 1)
            if (m := re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line))]


def metadata(text: str) -> dict[str, str]:
    result = {}
    # Modern metadata is a four-line prefix. Legacy Records use an identity
    # section; retaining only labels near the beginning avoids indexing opinion
    # prose as administrative metadata.
    for line in text.splitlines()[:40]:
        matches = list(re.finditer(r"\*\*([^*]+?):\*\*\s*", line))
        for i, match in enumerate(matches):
            if match[1] not in result:
                end = matches[i + 1].start() if i + 1 < len(matches) else len(line)
                result[match[1]] = line[match.end():end].strip()
    return result


def identity_text(text: str, meta: dict[str, str]) -> str:
    if "Case and dockets" in meta:
        return meta["Case and dockets"] + "\n" + meta.get("Event and date", "")
    # Explicit administrative identity in older Record forms precedes modeling.
    head = []
    started = False
    for line in text.splitlines()[:35]:
        if line.startswith("## "):
            if started or not re.search(r"identity|event|natural|status", line, re.I):
                break
            started = True
        head.append(line)
    # Several legacy writers put the canonical Event block inside the Public
    # Projection. Its bounded text supplies identity even when the introduction
    # discusses process rather than the event.
    for match in re.finditer(r"(?m)^#{2,4}\s+(?:\d+\.\s*)?Event\s*$", text):
        tail = text[match.end():]
        head.append(re.split(r"(?m)^#{1,6}\s+", tail, maxsplit=1)[0])
    return "\n".join(head)


def docket_tokens(text: str) -> set[str]:
    values = set(re.findall(r"\b(?:\d{2}-\d{1,5}|A-\d{1,5})\b", text, re.I))
    values.update("original:" + m for m in re.findall(r"\b(?:No\.?\s*)?(\d{1,3})\s*,?\s+Original\b", text, re.I))
    return {v.upper() for v in values}


def observed_event_date(path: str, text: str, meta: dict) -> tuple[str | None, str | None]:
    match = re.search(r"(\d{4}-\d{2}-\d{2})\.md$", path)
    candidate = valid_date(match[1]) if match else None
    explicit = meta.get("Event and date", "")
    if explicit:
        dates = [x for x in re.findall(r"\b\d{4}-\d{2}-\d{2}\b", explicit) if valid_date(x)]
        if candidate in dates:
            return candidate, None
        if dates:
            return None, "Filename event date disagrees with explicit Event and date metadata."
    if candidate:
        head = identity_text(text, meta)
        parsed = date.fromisoformat(candidate)
        long_date = rf"{parsed.strftime('%B')}\s*0?{parsed.day},?\s*{parsed.year}"
        if candidate in head or re.search(long_date, head, re.I):
            return candidate, None
    return None, "Event date lacks verified identity metadata; filename is not sufficient evidence."


_CITATION = re.compile(
    r"\b\d+\s+(?:U\.\s*S\.|S\.\s*Ct\.|F\.\s*(?:2d|3d|4th)|"
    r"F\.\s*Supp\.(?:\s*(?:2d|3d))?|L\.\s*Ed\.(?:\s*2d)?|"
    r"Stat\.|Fed\.\s*Reg\.)\s*\d+\b|\b\d+\s+U\.\s*S\.\s*C\.\s*§{1,2}\s*[\w.()-]+"
)


def markdown_targets(line: str) -> list[str]:
    """Observe inline link destinations, including balanced URL parentheses."""
    output = []
    for start in re.finditer(r"\]\(", line):
        pos, depth, target = start.end(), 1, []
        angle = pos < len(line) and line[pos] == "<"
        if angle:
            end = line.find(">", pos + 1)
            if end >= 0:
                output.append(line[pos + 1:end])
            continue
        while pos < len(line):
            char = line[pos]
            if char == "\\" and pos + 1 < len(line):
                target.append(line[pos + 1]); pos += 2; continue
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if not depth:
                    break
            if char.isspace() and depth == 1:
                break
            target.append(char); pos += 1
        if target:
            output.append("".join(target))
    return output


def reference_target(root: Path, source_path: str, target: str) -> tuple[str, str, str | None]:
    """Normalize a location for navigation, without opening the target."""
    if any(ord(char) < 32 or ord(char) == 127 for char in target):
        return "missing", target, "Reference contains control characters and is not navigable."
    try:
        parsed = urlsplit(target)
        if parsed.scheme:
            decoded_url = unquote(target)
            bad_chars = (any(char.isspace() for char in target)
                         or "\\" in decoded_url
                         or any(ord(char) < 32 or ord(char) == 127 for char in decoded_url))
            _ = parsed.port  # Access validates malformed and out-of-range ports.
            if (parsed.scheme.lower() in {"https", "http"} and parsed.hostname
                    and not parsed.username and not parsed.password and not bad_chars):
                return "external", target, None
            return "missing", target, "Unsafe or unsupported reference URL is retained but not navigable."
    except ValueError:
        return "missing", target, "Malformed reference URL is retained but not navigable."
    decoded = unquote(parsed.path)
    if "\\" in decoded or "\x00" in decoded or decoded.startswith("/"):
        return "missing", target, "Reference path is not a safe repository-relative location."
    if not decoded:
        decoded = source_path
    elif not decoded.startswith(("terms/", "state/", "foundation/", "tmp/", "tools/", "development/")):
        decoded = str(PurePosixPath(source_path).parent / decoded)
    parts = []
    for part in PurePosixPath(decoded).parts:
        if part == "..":
            if not parts:
                return "missing", target, "Reference escapes the repository."
            parts.pop()
        elif part != ".":
            parts.append(part)
    normalized = "/".join(parts)
    location = root / normalized
    cursor = root
    for part in parts:
        cursor = cursor / part
        if cursor.is_symlink():
            return "missing", target, "Reference traverses a symlink and is not navigable."
    suffix = ("#" + parsed.fragment) if parsed.fragment else ""
    if parsed.query:
        return "missing", target, "Repository reference contains an unsupported query."
    if location.is_file():
        return "repository", normalized + suffix, None
    return "missing", normalized + suffix, "Referenced repository file is absent."


def extract_references(root: Path, path: str, text: str) -> tuple[list, list, list]:
    references, citations, warnings, seen = [], [], [], set()
    section = ""
    for line_number, line in enumerate(text.splitlines(), 1):
        heading = re.match(r"^#{1,6}\s+(.+)", line)
        if heading:
            section = heading[1].strip()
        for match in _CITATION.finditer(line):
            citations.append({"text": match[0], "source_path": path, "line": line_number, "section": section})
        targets = markdown_targets(line)
        for match in re.finditer(r"https?://[^\s<>`\"\]]+", line):
            if any(match[0].startswith(target) for target in targets):
                continue
            target = match[0].rstrip(".,;:")
            # Parentheses enclosing a bare URL are prose punctuation. Keep
            # balanced parentheses that are actually part of a URL path.
            while target.endswith(")") and target.count(")") > target.count("("):
                target = target[:-1]
            targets.append(target)
        for match in re.finditer(r"`((?:(?:\.{1,2}/)|(?:terms|state|foundation|tmp|records|sources|freeze|runtime|entering-law)/)[^`\n]+\.(?:md|txt|pdf|json|html)(?:#[^`\s]+)?)`", line):
            target = match[1]
            # The documented term-directory notation in code spans is not a
            # Markdown destination. `records/X.md` names that term's Record
            # folder; a Markdown `(records/X.md)` still remains file-relative.
            if re.match(r"^(?:records|sources|freeze|runtime|entering-law)/", target) and re.match(r"^terms/OT\d{4}/", path):
                target = "/".join(path.split("/")[:2]) + "/" + target
            targets.append(target)
        for target in targets:
            kind, normalized, warning = reference_target(root, path, target)
            key = (line_number, normalized)
            if key in seen:
                continue
            seen.add(key)
            references.append({"kind": kind, "target": normalized, "source_path": path,
                               "line": line_number, "section": section, "review_status": "unverified",
                               "material_kind": "mixed" if "/records/" in normalized else "unknown"})
            if warning:
                warnings.append(f"Line {line_number}: {warning} ({target})")
        if (re.search(r"source|document|petition|brief|transcript|appendix|opinion", line, re.I)
                and re.search(r"not (?:supplied|available|authenticated|retrieved)|unavailable|could not (?:retrieve|find)", line, re.I)):
            warnings.append(f"Line {line_number}: recorded source limitation; read this section in context.")
    return references, citations, warnings


class Reader:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.sources: dict[str, dict] = {}
        self.cache: dict[str, str] = {}

    def read(self, path: str) -> str:
        if path in self.cache:
            return self.cache[path]
        parsed = PurePosixPath(path)
        if parsed.is_absolute() or ".." in parsed.parts or str(parsed) != path:
            raise IngestError(f"Noncanonical source path: {path}")
        location = self.root
        for part in parsed.parts:
            location /= part
            if location.is_symlink():
                raise IngestError(f"Symlink source rejected: {path}")
        try:
            data = location.read_bytes()
            text = data.decode("utf-8")
        except (OSError, UnicodeError) as exc:
            raise IngestError(f"Cannot read source {path}: {exc}") from exc
        self.sources[path] = {"sha256": digest(data), "size": len(data)}
        self.cache[path] = text
        return text


def _filenames(text: str, names: set[str]) -> list[str]:
    # Only literal complete filenames establish a Record pointer.
    return sorted({match[0] for match in re.finditer(r"[A-Za-z0-9_.'()-]+(?:-[A-Za-z0-9_.'()-]+)*\.md", text)
                   if match[0] in names})


def build_catalogue(root: Path, terms: list[str]) -> dict:
    """Extract observed files and exact evidence; perform no writes or fetches."""
    if not terms or len(set(terms)) != len(terms) or any(not re.fullmatch(r"OT\d{4}", term) for term in terms):
        raise IngestError("Terms must be distinct OTyyyy identifiers.")
    reader = Reader(root)
    root = reader.root
    records, inventory, carryovers, warnings, summaries = [], [], [], [], []
    mapping_path = "development/case-library/inputs/record-mappings.json"
    mappings = {}
    consumed_mappings = set()
    if (root / mapping_path).exists():
        data = strict_mapping_json(reader.read(mapping_path))
        if set(data) != {"format", "mappings"} or data["format"] != "case-library-record-mappings-v1":
            raise IngestError("Unsupported explicit Record mapping format")
        if not isinstance(data["mappings"], list):
            raise IngestError("Explicit Record mappings must be an array")
        for item in data["mappings"]:
            if not isinstance(item, dict) or set(item) != {"term", "inventory_caption", "inventory_date", "inventory_dockets", "record", "evidence_quote"}:
                raise IngestError("Explicit Record mapping contains missing or unknown fields")
            if not all(isinstance(value, str) and value for value in item.values()):
                raise IngestError("Explicit Record mapping values must be nonempty strings")
            key = (item["term"], item["inventory_caption"], item["inventory_date"], item["inventory_dockets"])
            if key in mappings:
                raise IngestError(f"Duplicate explicit mapping: {key}")
            mappings[key] = item
    for term in sorted(terms):
        base = f"terms/{term}"
        paths = sorted((root / base / "records").glob("*.md"))
        if not paths:
            raise IngestError(f"No Records found for {term}")
        term_records, identities = {}, {}
        for file_path in paths:
            path = file_path.relative_to(root).as_posix()
            text = reader.read(path)
            meta = metadata(text)
            identity = identity_text(text, meta)
            first_line = text.splitlines()[0] if text.splitlines() else ""
            admitted = bool(re.search(r"^#.*Admitted Source Record|^\*\*Event and date:\*\*.*Admitted", text, re.M | re.I))
            title = meta.get("Case and dockets", re.sub(r"^#\s*(?:Canonical Decision Record\s*[—–-]\s*)?", "", first_line))
            event_date, date_warning = observed_event_date(path, text, meta)
            refs, cites, record_warnings = extract_references(root, path, text)
            if date_warning:
                record_warnings.append(date_warning)
            record = {"record_id": record_id(path), "term": term, "path": path,
                      "sha256": reader.sources[path]["sha256"],
                      "kind": "admitted_source" if admitted else "court_event",
                      "metadata": meta, "title": title, "event_date": event_date,
                      "effective_date": None, "chunks": [], "inventory_refs": [],
                      "references": refs, "citations": cites, "sections": sections(text),
                      "warnings": record_warnings}
            term_records[file_path.name] = record
            identities[file_path.name] = identity
            records.append(record)
        names = set(term_records)
        case_path = f"{base}/case-list.md"
        case_rows = []
        for row in table_rows(reader.read(case_path)):
            if field(row, "Caption", "Case or matter", "Case") and field(row, "Event date", "Date"):
                row.update({"term": term, "path": case_path, "resolved_record_ids": []})
                case_rows.append(row)
        if not case_rows:
            raise IngestError(f"No recognizable inventory rows for {term}")
        inventory.extend(case_rows)
        workspace = f"{base}/workspace.md"
        manifest_path = f"{base}/workspace/manifest.md"
        ledger_path = f"{base}/workspace/ledger.md"
        manifest_rows = table_rows(reader.read(manifest_path if (root / manifest_path).exists() else workspace))
        effective_ledger_path = ledger_path if (root / ledger_path).exists() else workspace
        ledger_rows = table_rows(reader.read(effective_ledger_path))
        for row in ledger_rows:
            effective_cell = field(row, "Effective date")
            match = re.match(r"^(\d{4}-\d{2}-\d{2})(?:$|,\s+)", effective_cell)
            effective = valid_date(match[1]) if match else None
            if not effective:
                continue
            for name in _filenames(row["raw"], names):
                record = term_records[name]
                if record["effective_date"] not in (None, effective):
                    raise IngestError(f"Conflicting explicit ledger effective dates: {record['path']}")
                record["effective_date"] = effective
                record["references"].append({"kind": "repository", "target": effective_ledger_path,
                    "source_path": effective_ledger_path, "line": row["line"],
                    "section": "Explicit ledger effective-date cell: " + effective_cell,
                    "review_status": "unverified", "material_kind": "mixed"})
                if effective_cell != effective:
                    record["warnings"].append(f"Ledger chronology qualifier preserved: {effective_cell}; date alone does not determine sequence.")
        for row in case_rows:
            caption = field(row, "Caption", "Case or matter", "Case")
            ordering_date = field(row, "Event date", "Date")
            candidates = set()
            explicit_manifest = False
            for manifest_row in manifest_rows:
                if (normalize(field(manifest_row, "Case or matter", "Caption")) == normalize(caption)
                        and field(manifest_row, "Event date", "Effective or planned date") == ordering_date):
                    linked = _filenames(manifest_row["raw"], names)
                    if linked:
                        candidates.update(linked)
                        explicit_manifest = True
            key = (term, caption, ordering_date, field(row, "Docket(s)", "Docket", "Citation or docket"))
            if key in mappings:
                item = mappings[key]
                if item["record"] not in names:
                    raise IngestError(f"Explicit mapping Record absent: {item['record']}")
                text = reader.cache[term_records[item["record"]]["path"]]
                if not item.get("evidence_quote") or text.count(item["evidence_quote"]) != 1:
                    raise IngestError(f"Explicit identity evidence changed: {item['record']}")
                if term_records[item["record"]]["event_date"] != ordering_date:
                    raise IngestError(f"Explicit mapping event date disagrees: {item['record']}")
                if candidates and candidates != {item["record"]}:
                    raise IngestError(f"Curated mapping conflicts with explicit manifest: {item['record']}")
                candidates.add(item["record"])
                consumed_mappings.add(key)
            if not candidates:
                wanted = docket_tokens(field(row, "Docket(s)", "Docket", "Citation or docket"))
                for name, record in term_records.items():
                    if record["kind"] != "court_event" or record["event_date"] != ordering_date:
                        continue
                    identity = identities[name]
                    explicit_caption = normalize(caption) in normalize(identity)
                    explicit_docket = bool(wanted) and wanted.issubset(docket_tokens(identity))
                    if explicit_caption or explicit_docket:
                        candidates.add(name)
            if len(candidates) == 1 or (candidates and explicit_manifest):
                for name in sorted(candidates):
                    record = term_records[name]
                    row["resolved_record_ids"].append(record["record_id"])
                    record["inventory_refs"].append({"path": case_path, "line": row["line"], "caption": caption,
                                                     "dockets": field(row, "Docket(s)", "Docket", "Citation or docket"),
                                                     "area_of_law": field(row, "Area of law")})
                    record["chunks"] = sorted(set(record["chunks"] + row_chunk(row)))
            else:
                warnings.append(f"{case_path}:{row['line']}: {'ambiguous' if candidates else 'unresolved'} inventory mapping: {caption}")
        # Public presentation is navigation only. Consume handoffs solely for
        # literal source-record markers; legacy handoffs have no such markers.
        for handoff in sorted((root / base / "render-inputs").glob("*.md")):
            path = handoff.relative_to(root).as_posix()
            text = reader.read(path)
            chunks = chunk_numbers(handoff.stem)
            for i, line in enumerate(text.splitlines(), 1):
                marker = re.fullmatch(r"\s*<!--\s*source-record:\s*(.*?)\s*-->\s*", line)
                if marker and marker[1] in term_records:
                    record = term_records[marker[1]]
                    record["chunks"] = sorted(set(record["chunks"] + chunks))
                    record["references"].append({"kind": "repository", "target": path,
                        "source_path": path, "line": i, "section": "source-record marker",
                        "review_status": "unverified", "material_kind": "mixed"})
        for record in term_records.values():
            if record["effective_date"] is None:
                record["warnings"].append("No explicit effective date found in the term ledger; no date was inferred.")
            if record["kind"] == "court_event" and not record["inventory_refs"]:
                record["warnings"].append("Record has no resolved inventory row; supplemental status requires reading its provenance.")
            # Old presentation files identify a chunk, not each event. Record the
            # bounded chunk navigation without asserting an event section match.
            for chunk in record["chunks"]:
                for folder in ("render-inputs", "output"):
                    path = f"{base}/{folder}/OT_{term[2:]}CHUNK{chunk}.md"
                    if (root / path).is_file() and not any(r["target"] == path for r in record["references"]):
                        record["references"].append({"kind": "repository", "target": path,
                            "source_path": case_path, "line": record["inventory_refs"][0]["line"] if record["inventory_refs"] else 1,
                            "section": "chunk navigation; not an event section locator",
                            "review_status": "unverified", "material_kind": "mixed"})
        summaries.append({"term": term, "record_count": len(term_records),
                          "court_event_count": sum(r["kind"] == "court_event" for r in term_records.values()),
                          "admitted_source_count": sum(r["kind"] == "admitted_source" for r in term_records.values()),
                          "inventory_count": len(case_rows),
                          "mapped_inventory_count": sum(bool(r["resolved_record_ids"]) for r in case_rows),
                          "chunks": sorted({n for row in case_rows for n in row_chunk(row)})})
        dossier = f"{base}/close/TERM_CLOSE_DOSSIER.md"
        if (root / dossier).exists():
            reader.read(dossier)
    unused_mappings = sorted(key for key in mappings if key[0] in terms and key not in consumed_mappings)
    if unused_mappings:
        raise IngestError(f"Unused explicit Record mapping for selected term: {unused_mappings[0]}")
    if "OT1995" in terms and (root / "state/STANDING_STATE.md").exists():
        standing_path = "state/STANDING_STATE.md"
        for row in table_rows(reader.read(standing_path)):
            if field(row, "Stage at opening") and "OT1995" in field(row, "Why on the docket"):
                carryovers.append({"term": "OT1995", "path": standing_path, "line": row["line"],
                                   "columns": row["columns"], "raw": row["raw"], "resolved_record_ids": []})
    return {"terms": summaries, "records": records, "inventory": inventory,
            "carryovers": carryovers, "warnings": warnings, "sources": dict(sorted(reader.sources.items()))}
