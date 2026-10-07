"""Read-only final scope checks against the Doe task's pre-work byte snapshot.

Run only after assembly and derived projections are ready. Passing a filename
with --changed-record means the operator has authorized that Record's internal
entering-law/lineage note edits; this clerical checker prints those exact diffs
for review and does not claim to decide whether legal reasoning changed.
No Git command or other subprocess is invoked. No files are written.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / "terms/OT1995"
SNAPSHOT = ROOT / "tmp/doe-1996-06-21-before-20261007"
PUBLIC_MARKER = b"## Public Projection"
RECORD_LINK = re.compile(r"\[record\]\(\.\./records/([^)]+)\)")
SOURCE_BLOCK = re.compile(r"<!-- source-record: ([^>]+) -->\r?\n(.*?)(?=\r?\n---\r?\n|\Z)", re.S)
SPLITS = {
    f"terms/OT1995/runtime/OT_1995CHUNK9_{suffix}.md"
    for suffix in ("NEUTRAL", "STONE", "COMPARATOR")
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def fixed_line(data, label):
    return next((line for line in data.splitlines(keepends=True) if line.startswith(label.encode())), None)


def public_bytes(data):
    if data.count(PUBLIC_MARKER) != 1:
        raise ValueError("Record must contain exactly one Public Projection marker")
    return data[data.index(PUBLIC_MARKER):]


def projection(data):
    return public_bytes(data).decode("utf-8").split("\n", 1)[1].strip()


def manifest_rows(data):
    lines = data.decode("utf-8").splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("| Event date | Chunk | Case or matter |"))
    cols = [c.strip() for c in lines[start].strip().strip("|").split("|")]
    result = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(cols):
            raise ValueError("Manifest table shape differs from its header")
        result.append(dict(zip(cols, cells)))
    return cols, result


def ledger_rows(data):
    result = []
    for line in data.decode("utf-8").splitlines():
        m = RECORD_LINK.search(line)
        if m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 8:
                raise ValueError("Ledger table shape differs from eight columns")
            result.append((m.group(1), int(cells[0]), cells[-2], cells))
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--new-record", required=True, help="Exact filename of the one new Doe Record")
    ap.add_argument("--changed-record", action="append", default=[], help="Existing Record with authorized internal note edits; repeat as needed")
    ap.add_argument("--changed-runtime", action="append", default=[], help="Additional existing runtime filename allowed to change beyond the three generated chunk 9 splits")
    ap.add_argument("--brief-sha256", help="Optional independently captured SHA-256 for briefs/OT_1995CHUNK9.md")
    ap.add_argument("--brief-hash-stage", choices=("pre-task", "mid-task", "unspecified"), default="unspecified", help="Truthful time of the supplied brief hash capture; default: unspecified")
    ap.add_argument("--june21-sha256", help="Optional previously validated SHA-256 of the common PRE_19960621 entering-law neutral projection")
    args = ap.parse_args()
    for name in [args.new_record, *args.changed_record, *args.changed_runtime]:
        if Path(name).name != name:
            ap.error("Record/runtime arguments must be filenames, not paths")
    if len(set(args.changed_record)) != len(args.changed_record):
        ap.error("--changed-record values must be unique")
    baseline = json.loads((SNAPSHOT / "manifest.json").read_text(encoding="utf-8"))
    files = baseline["files"]
    errors, notices, successes = [], [], []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def before(rel):
        data = (SNAPSHOT / "files" / rel).read_bytes()
        require(sha(data) == files[rel]["sha256"], f"Snapshot bytes fail manifest SHA-256: {rel}")
        return data

    def current(rel):
        path = ROOT / rel
        require(path.is_file(), f"Pre-existing file missing: {rel}")
        return path.read_bytes() if path.is_file() else b""

    record_prefix = "terms/OT1995/records/"
    old_record_paths = {p for p in files if p.startswith(record_prefix)}
    old_records = {Path(p).name for p in old_record_paths if p.endswith(".md") and not Path(p).name.startswith(".")}
    authorized = set(args.changed_record)
    require(authorized <= old_records, f"Authorized changed names absent from baseline: {sorted(authorized - old_records)}")
    require(args.new_record not in old_records, "The named new Record already existed in the pre-task snapshot")
    all_current_record_files = {p.relative_to(ROOT).as_posix() for p in (TERM / "records").rglob("*") if p.is_file()}
    require(all_current_record_files == old_record_paths | {record_prefix + args.new_record}, "Record file set differs by more than the single named Doe Record")
    changed = set()
    for rel in sorted(old_record_paths):
        old, new = before(rel), current(rel)
        name = Path(rel).name
        if old == new:
            continue
        changed.add(name)
        require(name in authorized, f"Unauthorized old Record byte change: {name}")
        if name not in old_records:
            continue
        for label in ("**Case and dockets:**", "**Event and date:**", "**Result:**"):
            require(fixed_line(old, label) == fixed_line(new, label), f"Old Record {label} changed: {name}")
        try:
            require(public_bytes(old) == public_bytes(new), f"Old Record Public Projection bytes changed: {name}")
        except ValueError as e:
            errors.append(f"{name}: {e}")
        if name in authorized:
            print(f"\nAUTHORIZED INTERNAL DIFF FOR OPERATOR NOTE-SCOPE REVIEW: {name}")
            old_internal = old.split(PUBLIC_MARKER, 1)[0].decode("utf-8").splitlines()
            new_internal = new.split(PUBLIC_MARKER, 1)[0].decode("utf-8").splitlines()
            for line in difflib.unified_diff(old_internal, new_internal, fromfile="before", tofile="after", lineterm="", n=2):
                print(line)
    require(changed == authorized, f"Actual old Record changes differ from authorization list: changed={sorted(changed)}; authorized={sorted(authorized)}")
    successes.append(f"{len(old_records)} old Records: only {len(changed)} authorized internal changes; exact old Case/Event/Result/Public Projection preservation checked")

    new_path = TERM / "records" / args.new_record
    if new_path.is_file():
        new_data = new_path.read_bytes()
        event = fixed_line(new_data, "**Event and date:**") or b""
        require(b"1996-06-21" in event, "Doe event date is not 1996-06-21")
        require(b"Doe" in (fixed_line(new_data, "**Case and dockets:**") or b""), "Named new Record is not identified as Doe")
        for label in ("**Case and dockets:**", "**Event and date:**", "**Result:**", "**Version / lineage:**"):
            require(fixed_line(new_data, label) is not None, f"New Record missing {label}")

    fixed_paths = [p for p in files if p == "terms/OT1995/case-list.md" or p.startswith("terms/OT1995/output/") or p.startswith("terms/OT1995/freeze/")]
    for rel in fixed_paths:
        require(before(rel) == current(rel), f"Immutable case-list/output/pre-existing frozen artifact changed: {rel}")
    old_outputs = {p for p in files if p.startswith("terms/OT1995/output/")}
    current_outputs = {p.relative_to(ROOT).as_posix() for p in (TERM / "output").rglob("*") if p.is_file()}
    require(old_outputs == current_outputs, "Output file set changed")
    successes.append(f"Case-list, all old output files, and {sum('/freeze/' in p for p in fixed_paths)} snapshotted freeze artifacts are byte-identical; output file set unchanged")

    permitted_runtime = SPLITS | {"terms/OT1995/runtime/" + n for n in args.changed_runtime}
    runtime_changes = []
    for rel in sorted(p for p in files if p.startswith("terms/OT1995/runtime/")):
        if before(rel) != current(rel):
            runtime_changes.append(rel)
            require(rel in permitted_runtime, f"Unlisted existing runtime file changed: {rel}")
    successes.append("Existing runtime changes limited to approved filenames: " + (", ".join(Path(p).name for p in runtime_changes) or "none"))

    render_prefix = "terms/OT1995/render-inputs/"
    chunk9 = render_prefix + "OT_1995CHUNK9.md"
    for rel in sorted(p for p in files if p.startswith(render_prefix) and p != chunk9):
        require(before(rel) == current(rel), f"Other chunk Render Input bytes changed: {rel}")
    old_render_paths = {p for p in files if p.startswith(render_prefix)}
    current_render_paths = {p.relative_to(ROOT).as_posix() for p in (TERM / "render-inputs").rglob("*") if p.is_file()}
    require(current_render_paths == old_render_paths, "Render Input file set changed")
    old_ri = before(chunk9).decode("utf-8")
    new_ri = current(chunk9).decode("utf-8")
    old_blocks = [(m.group(1).strip(), m.group(2).strip()) for m in SOURCE_BLOCK.finditer(old_ri)]
    new_blocks = [(m.group(1).strip(), m.group(2).strip()) for m in SOURCE_BLOCK.finditer(new_ri)]
    require(len(old_blocks) == 11 and len({n for n, _ in old_blocks}) == 11, "Snapshot chunk 9 does not contain eleven distinct events")
    require(len(new_blocks) == 12 and len({n for n, _ in new_blocks}) == 12, "Completed chunk 9 does not contain twelve distinct events")
    require(set(dict(new_blocks)) == set(dict(old_blocks)) | {args.new_record}, "Chunk 9 event identity differs by more than the new Doe Record")
    for name, body in old_blocks:
        require(dict(new_blocks).get(name) == body, f"Prior chunk 9 event projection changed: {name}")
    for name, body in new_blocks:
        path = TERM / "records" / name
        require(path.is_file(), f"Render Input references missing Record: {name}")
        if path.is_file():
            try:
                require(projection(path.read_bytes()) == body, f"Generated Render Input/Record projection mismatch: {name}")
            except ValueError as e:
                errors.append(f"{name}: {e}")
    require(bool(re.search(r"\*\*Completed events:\*\*\s*12\b", new_ri)), "Chunk 9 metadata does not show twelve completed events")
    require("**Stopped matters:**" not in new_ri, "Chunk 9 Render Input still contains stopped matters")
    successes.append("Chunk 9 has twelve unique Record-identical projections; old eleven event projections and every other Render Input remain unchanged")

    rel_manifest = "terms/OT1995/workspace/manifest.md"
    old_cols, old_rows = manifest_rows(before(rel_manifest))
    new_cols, new_rows = manifest_rows(current(rel_manifest))
    require(old_cols == new_cols, "Manifest column structure changed")
    require(len(old_rows) == len(new_rows), "Manifest scheduled-event count changed")
    def retained_inventory_cells(row):
        permitted = {"Status"}
        if "Doe v. Kirchner" in row.get("Case or matter", ""):
            permitted.add("Current stage")
        return {k: v for k, v in row.items() if k not in permitted}

    old_fixed = [retained_inventory_cells(r) for r in old_rows]
    new_fixed = [retained_inventory_cells(r) for r in new_rows]
    require(old_fixed == new_fixed, "Manifest inventory/date/order cells changed outside Doe's authorized status/current-stage update")
    changed_statuses = [(a, b) for a, b in zip(old_rows, new_rows) if a.get("Status") != b.get("Status")]
    require(len(changed_statuses) == 1, f"Expected one manifest status change, found {len(changed_statuses)}")
    if len(changed_statuses) == 1:
        old_row, new_row = changed_statuses[0]
        require("Doe v. Kirchner" in new_row.get("Case or matter", ""), "The sole changed manifest status is not Doe")
        require(new_row.get("Event date") == "1996-06-21", "Doe manifest event date changed")
        require(new_row.get("Status") == "Completed: " + args.new_record, "Doe manifest status is not solely its new completed Record")
        require(bool(new_row.get("Current stage")) and not new_row["Current stage"].startswith(("Open", "Stopped")), "Doe manifest current-stage cell retains an open/stopped status")
    chunk9_rows = [r for r in new_rows if r.get("Chunk") == "OT_1995CHUNK9"]
    require(len(chunk9_rows) == 12, "Manifest chunk 9 no longer has exactly twelve scheduled entries")
    require(all(r.get("Status", "").startswith("Completed:") for r in chunk9_rows), "A chunk 9 manifest matter remains open/stopped")
    manifest_done = {name.strip() for r in chunk9_rows for name in r["Status"].removeprefix("Completed:").split(",")}
    require(manifest_done == set(dict(new_blocks)), "Chunk 9 manifest completed Record identity differs from Render Input")
    successes.append(f"Manifest preserves all {len(old_rows)} scheduled rows and date/order cells; only Doe completion status/current-stage cells may change")

    rel_ledger = "terms/OT1995/workspace/ledger.md"
    old_ledger, new_ledger = ledger_rows(before(rel_ledger)), ledger_rows(current(rel_ledger))
    require(len(old_ledger) == 117 and len(new_ledger) == 118, "Ledger must grow from 117 to 118 Records")
    require([r[:3] for r in new_ledger[:-1]] == [r[:3] for r in old_ledger], "Prior ledger display order or first-record commit metadata changed")
    require(bool(new_ledger) and new_ledger[-1][:3] == (args.new_record, 118, "uncommitted"), "Doe must be ledger row 118 with first-record commit uncommitted")
    for name, _, _, cells in new_ledger:
        path = TERM / "records" / name
        require(path.is_file(), f"Ledger refers to a missing Record: {name}")
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for index, label in ((2, "Case and dockets"), (3, "Event and date"), (4, "Result"), (5, "Version / lineage")):
            m = re.search(r"^\*\*" + re.escape(label) + r":\*\*\s*(.+)$", text, re.M)
            require(bool(m) and cells[index] == m.group(1).strip(), f"Ledger {label} differs from Record: {name}")
    ledger_text = current(rel_ledger).decode("utf-8")
    require("unverified" in ledger_text and "without Git access" in ledger_text, "Ledger provenance omits the unverified/no-Git limitation")
    successes.append("Ledger has 117 prior rows with preserved provenance plus Doe as uncommitted; all current opening-label projections match Records")

    brief = TERM / "briefs/OT_1995CHUNK9.md"
    if args.brief_sha256:
        require(bool(re.fullmatch(r"[0-9a-fA-F]{64}", args.brief_sha256)), "--brief-sha256 must contain 64 hexadecimal characters")
        require(brief.is_file() and sha(brief.read_bytes()).lower() == args.brief_sha256.lower(), "Approved chunk 9 brief differs from supplied SHA-256")
        successes.append(f"Approved brief matches independently supplied {args.brief_hash_stage} SHA-256")
        if args.brief_hash_stage != "pre-task":
            notices.append(f"The supplied brief hash was observed {args.brief_hash_stage}; it does not establish task-start byte identity.")
    else:
        notices.append("Briefs were not included in this agent's pre-task snapshot; brief immutability is not verified unless --brief-sha256 is supplied.")
    if args.june21_sha256:
        june21 = TERM / "entering-law/OT_1995CHUNK9_PRE_19960621_NEUTRAL_PROJECTION.md"
        require(bool(re.fullmatch(r"[0-9a-fA-F]{64}", args.june21_sha256)), "--june21-sha256 must contain 64 hexadecimal characters")
        require(june21.is_file() and sha(june21.read_bytes()).lower() == args.june21_sha256.lower(), "Shared June 21 entering baseline differs from supplied validated SHA-256")
        successes.append("Common June 21 entering baseline matches supplied validated SHA-256")
    else:
        notices.append("Entering-law files were outside this agent's pre-task snapshot; the common June 21 baseline hash was not independently compared by this script.")
    notices.append("Exact internal diffs above require operator confirmation as authorized entering-law/lineage notes. This script does not decide material legal dependence, vote arithmetic, or substantive compatibility.")
    notices.append("No Git operation or commit verification was performed. Run the no-Git check_term adapter separately for the repository's remaining deterministic checks.")
    print("\nFINAL DOE SCOPE CHECK")
    for message in successes:
        print("CHECK:", message)
    for message in notices:
        print("LIMIT:", message)
    if errors:
        for message in errors:
            print("ERROR:", message)
        raise SystemExit(1)
    print("PASS: all requested structural and byte-preservation checks passed, subject to the stated limits.")


if __name__ == "__main__":
    main()
