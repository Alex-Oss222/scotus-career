#!/usr/bin/env python3
"""Run the repository projection tools with expressly deferred Git verification.

This task-local adapter does not change the repository tools.  Run with -B.
Its only durable outputs are the requested ledger and a freeze receipt.
"""
from __future__ import annotations

import argparse
import contextlib
from datetime import datetime, timezone
import hashlib
import importlib.util
import io
import os
from pathlib import Path
import re
import subprocess
import sys

sys.dontwritebytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / "terms" / "OT1996"
TABLE = "| Commit order | Effective date | Case and dockets | Event | Result | Version / lineage | First-record commit | Record |"
RECORD_LINK = re.compile(r"\[record\]\(\.\./records/([^()]+)\)")


def load_tool(name: str):
    path = ROOT / "tools" / (name + ".py")
    spec = importlib.util.spec_from_file_location("boggs_" + name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@contextlib.contextmanager
def no_git_subprocesses():
    original = subprocess.run

    def guarded(args, *positional, **keywords):
        # All audited subprocess calls use argument lists and no shell.
        if not isinstance(args, (list, tuple)) or keywords.get("shell"):
            raise RuntimeError("Unreviewed shell/string subprocess was blocked")
        if args and Path(str(args[0])).stem.casefold() == "git":
            raise RuntimeError("A forbidden Git subprocess was blocked before launch")
        return original(args, *positional, **keywords)

    subprocess.run = guarded
    try:
        yield
    finally:
        subprocess.run = original


def call_main(module, arguments):
    output = io.StringIO()
    old_argv = sys.argv
    code = 0
    sys.argv = [module.__file__, *arguments]
    try:
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            try:
                module.main()
            except SystemExit as exc:
                code = exc.code if isinstance(exc.code, int) else (0 if exc.code is None else 1)
                if exc.code is not None and not isinstance(exc.code, int):
                    print(exc.code)
    finally:
        sys.argv = old_argv
    return code, output.getvalue()


def ledger_rows(text):
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or not cells[0].isdigit():
            continue
        match = RECORD_LINK.fullmatch(cells[-1]) if len(cells) == 8 else None
        if match is None:
            raise RuntimeError("Unrecognized existing ledger row; refusing to rebuild")
        rows.append((match.group(1), int(cells[0]), cells[6]))
    if not rows or len({row[0] for row in rows}) != len(rows):
        raise RuntimeError("Missing or duplicate existing ledger entries")
    if [row[1] for row in rows] != list(range(1, len(rows) + 1)):
        raise RuntimeError("Existing ledger order is not contiguous")
    return rows


def receipt(action, status, details, output):
    target = TERM / "freeze" / f"OT_1996CHUNK9_BOGGS_NO_GIT_{action.upper()}_VALIDATION.md"
    source = ROOT / "tools" / ("rebuild_ledger.py" if action == "ledger" else "check_term.py")
    text = (
        f"# Boggs task: {action} validation without Git\n\n"
        f"**Recorded UTC:** {datetime.now(timezone.utc).isoformat()}\n\n"
        f"**Status:** {status}\n\n"
        "**Git verification:** Not performed under the user's express no-Git instruction. "
        "No Git command was launched. Existing provenance is retained without verification; "
        "new provenance is operator-commit-pending. Git reference verification and commitment "
        "remain external operator follow-up, not a substantive stopped matter.\n\n"
        f"**Original tool:** {source.relative_to(ROOT).as_posix()}\n\n"
        f"**Tool SHA-256:** {hashlib.sha256(source.read_bytes()).hexdigest()}\n\n"
        f"{details}\n\n## Tool output\n\n```text\n{output.rstrip()}\n```\n"
    )
    target.write_text(text, encoding="utf-8")
    print(target.relative_to(ROOT).as_posix())


def rebuild_ledger(append_records):
    target = TERM / "workspace" / "ledger.md"
    original = target.read_bytes()
    text = original.decode("utf-8")
    if TABLE not in text:
        raise RuntimeError("Existing ledger header is missing")
    prefix = text[:text.index(TABLE)]
    previous = ledger_rows(text)
    cached = {name: (order, provenance) for name, order, provenance in previous}
    available = {path.name for path in (TERM / "records").glob("*.md") if not path.name.startswith(".")}
    requested = list(append_records)
    if len(set(requested)) != len(requested):
        raise RuntimeError("Duplicate --append-record argument")
    if any(Path(name).name != name for name in requested):
        raise RuntimeError("--append-record must be a filename only")
    if set(cached) - available:
        raise RuntimeError("An existing ledger Record is missing; refusing to remove its entry")
    additions = [name for name in requested if name not in cached]
    if available - set(cached) != set(additions):
        raise RuntimeError("New Records do not match explicit --append-record arguments")
    if set(requested) - available:
        raise RuntimeError("A requested append Record does not exist")
    for number, name in enumerate(additions, len(previous) + 1):
        cached[name] = (number, "operator-commit-pending")

    module = load_tool("rebuild_ledger")

    def retained_provenance(root, path):
        if root.resolve() != ROOT or path.parent.resolve() != (TERM / "records").resolve():
            raise RuntimeError("Unexpected ledger provenance path")
        return cached[path.name]

    module.git_added = retained_provenance
    output = ""
    try:
        with no_git_subprocesses():
            code, output = call_main(module, ["OT1996", "--root", str(ROOT)])
        if code:
            raise RuntimeError(f"Original ledger tool exited {code}: {output}")
        generated = target.read_text(encoding="utf-8")
        expected = previous + [(name, cached[name][0], cached[name][1]) for name in additions]
        if ledger_rows(generated) != expected:
            raise RuntimeError("Rebuild changed existing ledger order or provenance")
        table = generated[generated.index(TABLE):]
        if "\r\n" in text:
            table = table.replace("\n", "\r\n")
        target.write_bytes((prefix + table).encode("utf-8"))
    except BaseException:
        target.write_bytes(original)
        raise
    print(output, end="")
    details = (
        f"Preserved {len(previous)} existing row positions and provenance cells and the exact "
        f"existing header prefix. Appended {len(additions)} Records in explicit invocation order: "
        + (", ".join(additions) if additions else "none (idempotent rebuild)") + "."
    )
    receipt("ledger", "Projection rebuilt; Git provenance verification remains deferred.", details, output)
    return 0


def check_term():
    module = load_tool("check_term")
    deferred = []

    def unverified_reference(_root, sha):
        deferred.append(sha)
        # False preserves the original tool's warning for every unverified
        # reference.  The captured wording is corrected below: it is not a
        # finding that the referenced commit is absent.
        return False

    module.git_object_exists = unverified_reference
    with no_git_subprocesses():
        code, output = call_main(module, ["OT1996", "--root", str(ROOT)])
    output = output.replace("referenced commit not found:", "Git reference verification deferred (not checked):")
    output = output.replace("OK: OT1996;", "Non-Git deterministic checks passed: OT1996;")
    print(output, end="")
    status = (
        "Non-Git deterministic checks passed; full Git reference verification remains incomplete."
        if code == 0 else f"Non-Git deterministic checks failed (exit {code}); Git reference verification remains incomplete."
    )
    details = (
        f"Original check_term.py exit code: {code}. Deferred {len(deferred)} reference-check calls "
        f"covering {len(set(deferred))} distinct candidate hashes. No inference about their "
        "existence is made. Holdings synchronization, runtime split freshness, and all other "
        "original checks ran unchanged. Child Python processes inherited PYTHONDONTWRITEBYTECODE=1."
    )
    receipt("check", status, details, output)
    return code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    ledger = sub.add_parser("rebuild-ledger")
    ledger.add_argument("--append-record", action="append", required=True)
    sub.add_parser("check-term")
    args = parser.parse_args()
    return rebuild_ledger(args.append_record) if args.command == "rebuild-ledger" else check_term()


if __name__ == "__main__":
    raise SystemExit(main())
