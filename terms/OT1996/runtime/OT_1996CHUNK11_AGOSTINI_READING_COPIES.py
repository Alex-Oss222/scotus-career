"""Copy bounded public-law sections from current Records into reading slices."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys

sys.dontwritebytecode = True
ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / "terms" / "OT1996"
TARGETS = {
    "OT_1996CHUNK12_B.md": ("Agostini_v_Felton_merits_1997-06-23.md",),
    "OT_1996CHUNK12_LAWYER_FOCUSED.md": ("Agostini_v_Felton_merits_1997-06-23.md",),
    "OT_1996CHUNK13_A.md": ("City_of_Boerne_v_Flores_merits_1997-06-25.md",),
    "OT_1996CHUNK13_B.md": (
        "City_of_Boerne_v_Flores_merits_1997-06-25.md",
        "Lawyer_v_Department_of_Justice_merits_1997-06-25.md",
    ),
}
PARTS = {
    "Current Court law in effective order": ("Holdings", "Precedent Treatment", "Law After Decision"),
    "Material published noncontrolling positions": ("Separate Writings",),
    "Public procedure after completed actions": ("Procedure After Action",),
}


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def record_sections(name):
    path = TERM / "records" / name
    text = path.read_text(encoding="utf-8")
    projection = text.split("## Public Projection\n", 1)[1]
    if name.startswith("Agostini_"):
        result = re.search(r"^\*\*Result:\*\* (.+)$", text, re.M)
        if result is None or not re.search(r"vacat", result.group(1), re.I):
            raise RuntimeError("Agostini's current judgment does not match the expected operative source")
        if not re.search(r"Stone(?:-Zsela)?.{0,150}Opinion of the Court|Opinion of the Court.{0,150}Stone", projection, re.I):
            raise RuntimeError("Agostini's public authorship source is not ready")
    headings = list(re.finditer(r"^## ([^\n]+)\n", projection, re.M))
    sections = {}
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(projection)
        sections[match.group(1)] = projection[match.end():end].strip()
    return sections, hashlib.sha256(path.read_bytes()).hexdigest()


def selection_spans(text, record_name):
    pattern = re.compile(r"^### [^\n]+\n\nAuthority: \[Record\]\(\.\./records/" + re.escape(record_name) + r"\)\.\n\n", re.M)
    found = []
    for index, match in enumerate(pattern.finditer(text)):
        if index >= len(PARTS):
            raise RuntimeError("Too many case reading-copy sections")
        enclosing = list(re.finditer(r"^## Current-term reading copy: ([^\n]+)$", text[:match.start()], re.M))
        category = tuple(PARTS)[index]
        if enclosing and enclosing[-1].group(1) != category:
            raise RuntimeError("Reading-copy section order does not match its category")
        next_heading = re.search(r"^#{1,3} ", text[match.end():], re.M)
        end = match.end() + next_heading.start() if next_heading else len(text)
        raw = text[match.end():end]
        body = raw.rstrip("\n")
        if index == 0 and not body.startswith("#### Holdings\n"):
            raise RuntimeError("First case reading copy is not the expected law section")
        found.append((match.end(), match.end() + len(body), category))
    if len(found) != 3 or {item[2] for item in found} != set(PARTS):
        raise RuntimeError(f"Expected exactly three reading sections for {record_name}")
    return found


def section_text(sections, category):
    names = PARTS[category]
    if len(names) == 1:
        return re.sub(r"^(#{2,}) ", lambda match: "##" + match.group(1) + " ", sections[names[0]], flags=re.M)
    source = "\n\n".join("## " + name + "\n\n" + sections[name] for name in names)
    return re.sub(r"^(#{2,}) ", lambda match: "##" + match.group(1) + " ", source, flags=re.M)


def main():
    pending = []
    receipt = {"sources": {}, "copies": []}
    for filename, records in TARGETS.items():
        target = TERM / "entering-law" / filename
        original = target.read_bytes()
        raw = original.decode("utf-8")
        newline = "\r\n" if "\r\n" in raw else "\n"
        text = raw.replace("\r\n", "\n")
        operations = []
        for record_name in records:
            sections, sha = record_sections(record_name)
            receipt["sources"][record_name] = sha
            for start, end, category in selection_spans(text, record_name):
                replacement = section_text(sections, category)
                operations.append((start, end, replacement))
                receipt["copies"].append({
                    "file": filename,
                    "record": record_name,
                    "section": category,
                    "copied_text_sha256": digest(replacement),
                })
        operations.sort()
        if any(left[1] > right[0] for left, right in zip(operations, operations[1:])):
            raise RuntimeError("Selected copy boundaries overlap")
        result, outside, position = [], [], 0
        for start, end, replacement in operations:
            unchanged = text[position:start]
            result.extend((unchanged, replacement))
            outside.append(unchanged)
            position = end
        result.append(text[position:])
        outside.append(text[position:])
        output = "".join(result)
        for record_name in records:
            sections, _ = record_sections(record_name)
            for start, end, category in selection_spans(output, record_name):
                if output[start:end] != section_text(sections, category):
                    raise RuntimeError("Reading-copy source identity check failed")
        pending.append((target, output.replace("\n", newline).encode("utf-8")))
        receipt.setdefault("unselected_text_sha256", {})[filename] = digest("".join(outside))
    for target, data in pending:
        target.write_bytes(data)
        print(target.relative_to(ROOT).as_posix())
    receipt["status"] = "All selected sections copied directly from current public sources; unselected text and section order preserved."
    target = TERM / "freeze" / "OT_1996CHUNK11_AGOSTINI_READING_COPY_VALIDATION.json"
    target.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(target.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
