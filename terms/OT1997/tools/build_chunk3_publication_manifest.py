#!/usr/bin/env python3
"""Package new/changed durable Chunk 3 files, without Git or network access."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import hashlib
import json
import re

TERM = Path(__file__).resolve().parents[1]
ROOT = TERM.parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--output", default="freeze/OT_1997CHUNK3_PUBLICATION_FILES.json")
parser.add_argument("--baseline", default="freeze/OT_1997CHUNK3_STARTING_HASHES.json")
parser.add_argument("--publication-base", default="af3e18bdd8c95e99103243687e1c1fba942b4db6")
parser.add_argument("--exclude-name-contains", action="append", default=[])
args = parser.parse_args()
TARGET = (TERM / args.output).resolve()
baseline_path = (TERM / args.baseline).resolve()
if not TARGET.is_relative_to(TERM) or not baseline_path.is_relative_to(TERM):
    raise SystemExit("Manifest and baseline must stay inside the term")
BASELINE = json.loads(baseline_path.read_text())


def forbidden(path):
    return any(p.lower() == "stone" or p.upper().startswith("MASTER_JURISPRUDENCE")
               for p in Path(path).parts)


def excluded(path):
    return ("PUBLICATION_FILES" in Path(path).name
            or any(part in Path(path).name for part in args.exclude_name_contains))


if forbidden(TARGET) or forbidden(baseline_path):
    raise SystemExit("Prohibited manifest or baseline target")


def changed(path):
    old = BASELINE.get(str(path.relative_to(ROOT)))
    return not old or old["sha256"] != hashlib.sha256(path.read_bytes()).hexdigest()


selected = set()
for dirname in ("freeze", "runtime", "entering-law", "render-inputs", "output"):
    for path in (TERM / dirname).iterdir():
        if forbidden(path) or excluded(path) or path == TARGET or not path.is_file():
            continue
        if path.name.startswith("OT_1997CHUNK3"):
            selected.add(path)
order = json.loads((TERM / "freeze/OT_1997CHUNK3_RECORD_COMMIT_ORDER.json").read_text())
selected.update(TERM / "records" / row["file"] for row in order["records"])
selected.update(TERM / "workspace" / name for name in
                ("manifest.md", "ledger.md", "continuity.md", "neutral-projection.md"))
selected.add(TERM / "case-list.md")
selected.update(path for path in (TERM / "tools").iterdir()
                if path.is_file() and not forbidden(path) and changed(path))

# Source receipts can name necessary transcriptions without Markdown links.
# A controller-authored list includes only actually used support, never bulk
# retrievals or unused downloads. Link closure below adds further dependencies.
source_list = TERM / "freeze/OT_1997CHUNK3_REQUIRED_SOURCES.json"
if source_list.exists():
    for item in json.loads(source_list.read_text())["paths"]:
        path = (ROOT / item).resolve()
        if forbidden(path) or not path.is_relative_to(TERM):
            raise SystemExit("Out-of-scope source dependency: " + item)
        selected.add(path)

queue = list(selected)
seen = set()
missing = []
legacy = []
while queue:
    path = queue.pop()
    if path in seen:
        continue
    seen.add(path)
    if excluded(path):
        selected.discard(path)
        continue
    if forbidden(path):
        raise SystemExit("Prohibited publication target")
    if not path.exists():
        missing.append(str(path.relative_to(ROOT)))
        continue
    # An unchanged dependency and its source closure were already published.
    # Do not reopen old frozen handoffs or treat their copied relative links as
    # newly introduced Chunk 3 publication dependencies.
    if not changed(path):
        continue
    if path.suffix not in (".md", ".txt"):
        continue
    for match in re.finditer(r"\]\(([^)]+)\)", path.read_text()):
        target = match.group(1).strip().strip("<>")
        if not target or target.startswith("#") or urlsplit(target).scheme:
            continue
        target = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not target or forbidden(target):
            continue
        if "position_evidence" in Path(target).parts:
            legacy.append({"source": str(path.relative_to(ROOT)), "target": target,
                           "status": "Unused immutable-input reference; not opened"})
            continue
        dest = (path.parent / target).resolve()
        if forbidden(dest) or excluded(dest) or not dest.is_relative_to(TERM) or dest == TARGET:
            continue
        if dest.is_relative_to(TERM / "briefs"):
            continue
        if not dest.exists():
            if path.parent == TERM / "runtime" or path.name == "OT_1997CHUNK3_OPENING_NEUTRAL.md":
                legacy.append({"source": str(path.relative_to(ROOT)), "target": target,
                               "status": "Copied input/snapshot reference; authoritative replacement handoffs supplied"})
            else:
                missing.append(str(dest.relative_to(ROOT)))
            continue
        if dest.is_file() and dest not in selected:
            selected.add(dest)
            queue.append(dest)

unchanged = []
files = []
for path in sorted(selected):
    if not path.exists():
        continue
    rel = str(path.relative_to(ROOT))
    if not changed(path):
        unchanged.append(rel)
        continue
    body = path.read_bytes()
    files.append({"path": rel, "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()})
out = {
    "scope": "New/changed durable Chunk 3 Run/Render, current term projections/tools, and required linked sources",
    "publication_base": args.publication_base,
    "baseline_path": str(baseline_path.relative_to(ROOT)),
    "excluded_name_fragments": args.exclude_name_contains,
    "manifest_path": str(TARGET.relative_to(ROOT)),
    "publish_manifest_itself": True,
    "self_reference_note": "Publish this index separately; its own hash and size are supplied in the controller release.",
    "files": files, "file_count": len(files), "total_bytes": sum(x["bytes"] for x in files),
    "missing_linked_term_targets": sorted(set(missing)),
    "preserved_legacy_input_links": legacy,
    "already_published_unchanged_dependencies": unchanged,
    "exclusions": "Approved briefs, unchanged published dependencies, unrelated chunks, prohibited paths, and unused bulk retrievals."
}
TARGET.write_text(json.dumps(out, indent=2) + "\n")
print(str(TARGET.relative_to(ROOT)), len(files), "files", out["total_bytes"], "bytes",
      len(out["missing_linked_term_targets"]), "missing linked targets")
