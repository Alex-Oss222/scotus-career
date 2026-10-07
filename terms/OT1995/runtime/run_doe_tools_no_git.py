"""Invoke the repository's OT1995 builders with Git operations deferred.

This task-local adapter does not change repository tooling. Existing ledger
order and first-record commit strings come from the pre-task byte snapshot;
they are not verified. A new named Record is appended as uncommitted.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / "terms" / "OT1995"
SNAPSHOT = ROOT / "tmp" / "doe-1996-06-21-before-20261007"


def load_tool(name):
    path = ROOT / "tools" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(f"doe_task_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def baseline_ledger():
    rel = "terms/OT1995/workspace/ledger.md"
    manifest = json.loads((SNAPSHOT / "manifest.json").read_text(encoding="utf-8"))
    data = (SNAPSHOT / "files" / rel).read_bytes()
    if hashlib.sha256(data).hexdigest() != manifest["files"][rel]["sha256"]:
        raise SystemExit("Pre-task ledger snapshot fails its recorded SHA-256")
    saved = {}
    for line in data.decode("utf-8").splitlines():
        m = re.search(r"\[record\]\(\.\./records/([^)]+)\)", line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 8:
            raise SystemExit(f"Unexpected pre-task ledger table shape: {m.group(1)}")
        order = int(cells[0])
        if m.group(1) in saved or order in {v[0] for v in saved.values()}:
            raise SystemExit("Duplicate pre-task ledger record or display order")
        saved[m.group(1)] = (order, cells[-2])
    if not saved:
        raise SystemExit("No pre-task ledger entries found")
    return saved


def run_ledger(new_record):
    module = load_tool("rebuild_ledger")
    saved = baseline_ledger()
    names = {p.name for p in (TERM / "records").glob("*.md") if not p.name.startswith(".")}
    if set(saved) - names:
        raise SystemExit("A pre-task ledger Record is missing; refusing to rebuild")
    if names - set(saved) != {new_record}:
        raise SystemExit(f"Expected only the named new Record {new_record!r}; found {sorted(names - set(saved))}")
    retained = dict(saved)
    saved[new_record] = (max(v[0] for v in saved.values()) + 1, "uncommitted")
    module.git_added = lambda root, path: saved[path.name]
    sys.argv = [str(ROOT / "tools/rebuild_ledger.py"), "OT1995"]
    module.main()
    ledger = TERM / "workspace/ledger.md"
    generated = ledger.read_text(encoding="utf-8").splitlines()
    generated[2] = (
        "Generated from canonical Record opening labels without Git access. "
        "Existing displayed row order and first-record commit strings are reused "
        "from the pre-task ledger snapshot and remain unverified prior metadata. "
        "The new Doe Record is appended as uncommitted; the displayed index is not "
        "a verified Git commitment order. Records control if this index conflicts with them."
    )
    generated[4] = "| Display order | Effective date | Case and dockets | Event | Result | Version / lineage | First-record commit (unverified) | Record |"
    for line in generated[6:]:
        m = re.search(r"\[record\]\(\.\./records/([^)]+)\)", line)
        if not m:
            raise SystemExit("Unexpected generated ledger row")
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if m.group(1) in retained and (int(cells[0]), cells[-2]) != retained[m.group(1)]:
            raise SystemExit(f"Pre-task order/provenance drift for {m.group(1)}")
    ledger.write_text("\n".join(generated) + "\n", encoding="utf-8")
    print(f"Git operations: NONE. Reused {len(retained)} historical display-order/commit pairs without verification; {new_record} is uncommitted.")


def run_check():
    module = load_tool("check_term")
    skipped = set()

    def deferred_exists(root, sha):
        skipped.add(sha)
        return True  # Avoid a false missing-object warning; does not verify it.

    module.git_object_exists = deferred_exists
    sys.argv = [str(ROOT / "tools/check_term.py"), "OT1995"]
    print("Running tools/check_term.py OT1995 with Git object checks explicitly deferred to the operator.")
    try:
        module.main()
    finally:
        print(f"Git operations: NONE. Commit-existence verification SKIPPED for {len(skipped)} distinct referenced hashes. All other check_term checks ran unless execution failed earlier; any OK above excludes Git verification.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("ledger", "check"))
    parser.add_argument("--new-record", help="Exact filename of the sole newly completed Doe Record; required for ledger")
    args = parser.parse_args()

    # Only check_term's two inspected, read-only Python child tools may launch.
    original_run = subprocess.run

    def guarded_run(command, *positional, **kwargs):
        if not isinstance(command, (list, tuple)) or len(command) < 3 or kwargs.get("shell"):
            raise RuntimeError("This adapter forbids unapproved subprocess invocation")
        program = Path(str(command[1])).resolve()
        allowed = (
            program == ROOT / "tools/holdings_volumes.py" and command[2] == "check"
        ) or (
            program == ROOT / "tools/split_chunk.py" and "--check" in command
        )
        if Path(str(command[0])).resolve() != Path(sys.executable).resolve() or not allowed:
            raise RuntimeError("This adapter permits only the inspected, read-only holdings and split checks; no Git command is permitted")
        return original_run(command, *positional, **kwargs)

    subprocess.run = guarded_run
    if args.action == "ledger":
        if not args.new_record or Path(args.new_record).name != args.new_record:
            parser.error("ledger requires --new-record with a filename, not a path")
        run_ledger(args.new_record)
    else:
        if args.new_record:
            parser.error("--new-record applies only to ledger")
        run_check()


if __name__ == "__main__":
    main()
