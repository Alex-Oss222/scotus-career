#!/usr/bin/env python3
"""List completed chunks 1–2 durable files and their linked term-local support.

No Git or network access; excludes unrelated chunks and prohibited paths.
This is publication packaging, not a substantive audit.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

TERM = Path(__file__).resolve().parents[1]
ROOT = TERM.parents[1]
TARGET = TERM / "freeze/OT_1997CHUNK2_PUBLICATION_FILES.json"
CHUNK = re.compile(r"^OT_1997CHUNK(?:1|2)(?:_|\.)")

def forbidden(path):
    return any(p.lower() == "stone" or p.upper().startswith("MASTER_JURISPRUDENCE")
               for p in Path(path).parts)

selected = set()
for dirname in ("freeze", "entering-law", "runtime", "render-inputs"):
    for path in (TERM / dirname).iterdir():
        if forbidden(path) or not CHUNK.match(path.name) or path == TARGET:
            continue
        if path.is_file():
            selected.add(path)
for chunk in (1, 2):
    order = json.loads((TERM / f"freeze/OT_1997CHUNK{chunk}_RECORD_COMMIT_ORDER.json").read_text())
    selected.update(TERM / "records" / row["file"] for row in order["records"])
selected.update(TERM / "workspace" / name for name in
                ("manifest.md", "ledger.md", "continuity.md", "neutral-projection.md"))
selected.add(TERM / "case-list.md")
selected.add(TERM / "output/OT_1997CHUNK2.md")
selected.update(TERM / "tools" / name for name in
                ("run_tool.py", "commit_public_state.py", "build_publication_manifest.py"))

# Compact official opinion transcriptions and corroboration receipts preserve
# the validated source content without bulk PDFs or unfiltered website copies.
source = TERM / "freeze/sources/chunk2_control"
for pattern in ("USREPORTS-522-*.txt", "*_lower_opinion_only.txt", "*_cap_opinion.txt",
                "*selected.txt", "*_source_receipt.json", "CHUNK2_OFFICIAL_SOURCE_RECEIPT.json",
                "LOWER_REPORTER_COMPARISON.json", "_control_*notes.md", "_neutral_*facts.md"):
    selected.update(source.glob(pattern))

queue = list(selected)
seen = set()
missing = []
legacy_links = []
while queue:
    path = queue.pop()
    if path in seen:
        continue
    seen.add(path)
    if forbidden(path):
        raise SystemExit("Prohibited publication target")
    if not path.exists():
        missing.append(str(path.relative_to(ROOT)))
        continue
    if path.suffix not in (".md", ".txt"):
        continue
    text = path.read_text()
    for match in re.finditer(r"\]\(([^)]+)\)", text):
        target = match.group(1).strip().strip("<>")
        if not target or target.startswith("#") or urlsplit(target).scheme:
            continue
        target = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not target or forbidden(target):
            continue
        legacy = path.parent == TERM / "runtime" or path.name in (
            "OT_1997CHUNK2_NEUTRAL_ROGERS_SEED.md", "OT_1997CHUNK1_OPENING_NEUTRAL.md",
            "OT_1997CHUNK2_OPENING_NEUTRAL.md")
        if "position_evidence" in Path(target).parts:
            legacy_links.append({"source": str(path.relative_to(ROOT)), "target": target,
                                 "status": "unused preparation reference preserved in derived input; not opened"})
            continue
        dest = (path.parent / target).resolve()
        if forbidden(dest) or not dest.is_relative_to(TERM):
            continue
        if dest == TARGET:
            continue
        # Approved input briefs already exist on main and remain immutable.
        if dest.is_relative_to(TERM / "briefs"):
            continue
        if not dest.exists():
            if legacy:
                legacy_links.append({"source": str(path.relative_to(ROOT)), "target": target,
                                     "status": "unused preparation reference or copied snapshot-relative link; authoritative replacement inputs are included"})
            else:
                missing.append(str(dest.relative_to(ROOT)))
            continue
        if dest.is_file() and dest not in selected:
            selected.add(dest)
            queue.append(dest)

files = []
for path in sorted(selected):
    if not path.exists():
        continue
    body = path.read_bytes()
    files.append({"path": str(path.relative_to(ROOT)), "bytes": len(body),
                  "sha256": hashlib.sha256(body).hexdigest()})
out = {"scope": "Required durable Chunk1 support and completed Chunk2 state/render; approved briefs unchanged",
       "manifest_path": str(TARGET.relative_to(ROOT)),
       "publish_manifest_itself": True,
       "self_reference_note": "Publish this index alongside the files below; its own size/hash are supplied separately to avoid a circular digest.",
       "files": files, "file_count": len(files), "total_bytes": sum(x["bytes"] for x in files),
       "missing_linked_term_targets": sorted(set(missing)),
       "preserved_legacy_input_links": legacy_links,
       "exclusions": "Unrelated chunks, prohibited sources, unused bulk/raw retrievals, and failed downloads. Already-published unchanged Chunk1 output is included only if a durable selected file links it."}
TARGET.write_text(json.dumps(out, indent=2) + "\n")
print(str(TARGET.relative_to(ROOT)), out["file_count"], "files", out["total_bytes"], "bytes",
      len(out["missing_linked_term_targets"]), "missing linked targets")
