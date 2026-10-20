#!/usr/bin/env python3
"""Run bounded OT1996 projection tools without launching external processes.

Invoke with python -B. Existing ledger order and provenance are retained.
Durable writes are limited to OT1996 projections and operational receipts.
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
CHUNK = "OT_1996CHUNK11"
TABLE_START = "| Commit order | Effective date |"
RECORD_LINK = re.compile(r"\[record\]\(\.\./records/([^()]+)\)")
APPROVED_TOOLS = {
    "rebuild_ledger", "rebuild_manifest", "build_render_input", "check_term",
    "holdings_volumes", "split_chunk",
}


def load_tool(name):
    if name not in APPROVED_TOOLS:
        raise RuntimeError("Unapproved tool")
    path = ROOT / "tools" / (name + ".py")
    spec = importlib.util.spec_from_file_location("hendricks_" + name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def deny_external_process(event, _args):
    if event in {"subprocess.Popen", "os.system", "os.posix_spawn", "os.spawn", "os.startfile", "os.startfile/2"}:
        raise RuntimeError("External process launch blocked by the task runner")


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


@contextlib.contextmanager
def no_external_processes():
    original = subprocess.run

    def guarded(args, *positional, **keywords):
        if positional or not isinstance(args, (list, tuple)) or keywords.get("shell"):
            raise RuntimeError("Unreviewed subprocess invocation blocked")
        values = [os.fspath(value) for value in args]
        if len(values) < 2 or Path(values[0]).resolve() != Path(sys.executable).resolve():
            raise RuntimeError("Only approved Python checks may run in-process")
        script, rest = Path(values[1]).resolve(), values[2:]
        if script == (ROOT / "tools" / "holdings_volumes.py").resolve():
            if rest != ["check", "--root", str(ROOT)]:
                raise RuntimeError("Unexpected Holdings check arguments")
            name = "holdings_volumes"
        elif script == (ROOT / "tools" / "split_chunk.py").resolve():
            if len(rest) != 2 or rest[1] != "--check":
                raise RuntimeError("Only split_chunk --check is permitted")
            brief = Path(rest[0]).resolve()
            if brief.parent != (TERM / "briefs").resolve() or not re.fullmatch(r"OT_1996CHUNK\d+\.md", brief.name):
                raise RuntimeError("Unexpected runtime freshness input")
            name = "split_chunk"
        else:
            raise RuntimeError("Unapproved subprocess script blocked")
        code, output = call_main(load_tool(name), rest)
        return subprocess.CompletedProcess(values, code, output, "")

    subprocess.run = guarded
    try:
        yield
    finally:
        subprocess.run = original


def receipt(action, tool_name, status, details, output):
    target = TERM / "freeze" / f"{CHUNK}_HENDRICKS_V3_NO_GIT_{action.upper()}_VALIDATION.md"
    source = ROOT / "tools" / (tool_name + ".py")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        f"# Hendricks: {action.replace('_', ' ')} validation\n\n"
        f"**Recorded UTC:** {datetime.now(timezone.utc).isoformat()}\n\n"
        f"**Status:** {status}\n\n{details}\n\n"
        "**Operational limitation:** Git object-existence checks and commitment were not performed. "
        "No external process was launched.\n\n"
        f"**Tool:** {source.relative_to(ROOT).as_posix()}\n\n"
        f"**Tool SHA-256:** {hashlib.sha256(source.read_bytes()).hexdigest()}\n\n"
        f"## Tool output\n\n```text\n{output.rstrip()}\n```\n",
        encoding="utf-8",
    )
    print(target.relative_to(ROOT).as_posix())


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
            raise RuntimeError("Unrecognized existing ledger row")
        rows.append((match.group(1), int(cells[0]), cells[6]))
    if not rows or len({row[0] for row in rows}) != len(rows):
        raise RuntimeError("Missing or duplicate existing ledger entries")
    if [row[1] for row in rows] != list(range(1, len(rows) + 1)):
        raise RuntimeError("Existing ledger order is not contiguous")
    return rows


def rebuild_ledger(append_records):
    target = TERM / "workspace" / "ledger.md"
    original = target.read_bytes()
    text = original.decode("utf-8")
    if TABLE_START not in text:
        raise RuntimeError("Existing ledger header is missing")
    prefix = text[:text.index(TABLE_START)]
    previous = ledger_rows(text)
    cached = {name: (order, provenance) for name, order, provenance in previous}
    available = {p.name for p in (TERM / "records").glob("*.md") if not p.name.startswith(".")}
    requested = list(append_records)
    if len(set(requested)) != len(requested) or any(Path(name).name != name for name in requested):
        raise RuntimeError("Append arguments must be unique filenames")
    if set(cached) - available or set(requested) - available:
        raise RuntimeError("A ledger or requested Record is missing")
    additions = [name for name in requested if name not in cached]
    if available - set(cached) != set(additions):
        raise RuntimeError("New Records do not match explicit --append-record arguments")
    for number, name in enumerate(additions, len(previous) + 1):
        cached[name] = (number, "operator-commit-pending")
    module = load_tool("rebuild_ledger")

    def retained_provenance(root, path):
        if root.resolve() != ROOT or path.parent.resolve() != (TERM / "records").resolve():
            raise RuntimeError("Unexpected ledger provenance path")
        return cached[path.name]

    module.git_added = retained_provenance
    try:
        with no_external_processes():
            code, output = call_main(module, ["OT1996", "--root", str(ROOT)])
        if code:
            raise RuntimeError(f"Ledger tool exited {code}: {output}")
        generated = target.read_text(encoding="utf-8")
        expected = previous + [(name, cached[name][0], cached[name][1]) for name in additions]
        if ledger_rows(generated) != expected:
            raise RuntimeError("Rebuild changed existing ledger order or provenance")
        table = generated[generated.index(TABLE_START):]
        if "\r\n" in text:
            table = table.replace("\n", "\r\n")
        target.write_bytes((prefix + table).encode("utf-8"))
    except BaseException:
        target.write_bytes(original)
        raise
    print(output, end="")
    receipt("ledger", "rebuild_ledger", "Projection rebuilt.",
            f"Preserved {len(previous)} existing row positions and provenance cells and the existing header prefix. "
            f"Appended {len(additions)} Records in explicit argument order.", output)
    return 0


def manifest_rows():
    text = (TERM / "workspace" / "manifest.md").read_text(encoding="utf-8")
    lines = text.splitlines()
    h = next((i for i, line in enumerate(lines) if line.startswith("| Event date | Chunk | Case or matter |")), None)
    if h is None:
        raise RuntimeError("Manifest inventory table is missing")
    columns = [c.strip() for c in lines[h].strip().strip("|").split("|")]
    rows = []
    for line in lines[h + 2:]:
        if not line.startswith("|"):
            break
        values = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(values) != len(columns):
            raise RuntimeError("Malformed manifest inventory row")
        rows.append(dict(zip(columns, values)))
    return rows


def rebuild_manifest(stopped, carried):
    arguments = ["OT1996", "--root", str(ROOT)]
    # Pass existing blockers explicitly, preserving them even if a matching
    # Record happens to be present. Explicit arguments follow and take priority.
    for row in manifest_rows():
        for prefix, flag in (("Stopped: ", "--stopped"), ("Carry forward: ", "--carried")):
            if row["Status"].startswith(prefix):
                arguments += [flag, row["Case or matter"] + "=" + row["Status"][len(prefix):]]
    for flag, values in (("--stopped", stopped), ("--carried", carried)):
        for value in values:
            arguments += [flag, value]
    with no_external_processes():
        code, output = call_main(load_tool("rebuild_manifest"), arguments)
    print(output, end="")
    receipt("manifest", "rebuild_manifest", "Projection rebuilt." if code == 0 else f"Tool failed (exit {code}).",
            "Existing inventory blockers were passed explicitly. The repository tool preserves extra columns and text outside the inventory table.", output)
    return code


def build_render_input(records, stopped):
    rows = [row for row in manifest_rows() if row["Chunk"] == CHUNK]
    expected = set()
    for row in rows:
        if row["Status"].startswith("Completed:"):
            expected.update(name.strip() for name in row["Status"][len("Completed:"):].split(","))
    selected = list(records) if records else sorted(expected)
    if not selected or len(selected) != len(set(selected)) or set(selected) != expected:
        raise RuntimeError("Render records must equal the manifest's complete chunk-11 set without duplicates")
    if any(Path(name).name != name for name in selected):
        raise RuntimeError("Render record arguments must be filenames only")
    target = TERM / "render-inputs" / (CHUNK + ".md")
    notices = list(stopped)
    if not notices:
        notices = [row["Case or matter"] + ": " + row["Status"][len("Stopped: "):]
                   for row in rows if row["Status"].startswith("Stopped: ")]
    arguments = [str(target), *[str(TERM / "records" / name) for name in selected]]
    for notice in notices:
        arguments += ["--stopped", notice]
    with no_external_processes():
        code, output = call_main(load_tool("build_render_input"), arguments)
    print(output, end="")
    receipt("render_input", "build_render_input", "Projection rebuilt." if code == 0 else f"Tool failed (exit {code}).",
            f"Selected all {len(selected)} completed chunk-11 Records from the manifest and retained {len(notices)} stopped-matter notices.", output)
    return code


def check_term():
    module = load_tool("check_term")
    deferred = []

    def unverified_reference(_root, sha):
        deferred.append(sha)
        return False

    module.git_object_exists = unverified_reference
    with no_external_processes():
        code, output = call_main(module, ["OT1996", "--root", str(ROOT)])
    # The original tool's missing-object warnings are not factual findings when
    # the lookup is skipped. Replace them with one accurate operational note.
    lines = [line for line in output.splitlines() if "referenced commit not found:" not in line and line != "WARNINGS"]
    lines = [line.replace("OK: OT1996;", "Non-Git deterministic checks passed: OT1996;")
             for line in lines if not line.startswith("OK: OT1996;")]
    if code == 0:
        lines.append("Non-Git deterministic checks passed: OT1996.")
    lines.append(f"Git object-existence checks skipped: {len(deferred)} calls; {len(set(deferred))} distinct candidate hashes.")
    output = "\n".join(lines) + "\n"
    print(output, end="")
    status = "Non-Git deterministic checks passed." if code == 0 else f"Non-Git deterministic checks failed (exit {code})."
    receipt("check", "check_term", status,
            f"Original checker exit code: {code}. Holdings synchronization, runtime split freshness and all other original checks ran. "
            "The two read-only child checks ran in-process with bytecode writes disabled.", output)
    return code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    ledger = sub.add_parser("rebuild-ledger")
    ledger.add_argument("--append-record", action="append", default=[])
    manifest = sub.add_parser("rebuild-manifest")
    manifest.add_argument("--stopped", action="append", default=[])
    manifest.add_argument("--carried", action="append", default=[])
    render = sub.add_parser("build-render-input")
    render.add_argument("records", nargs="*", help="Record filenames; default is the full manifest set")
    render.add_argument("--stopped", action="append", default=[])
    sub.add_parser("check-term")
    args = parser.parse_args()
    if args.command == "rebuild-ledger":
        return rebuild_ledger(args.append_record)
    if args.command == "rebuild-manifest":
        return rebuild_manifest(args.stopped, args.carried)
    if args.command == "build-render-input":
        return build_render_input(args.records, args.stopped)
    return check_term()


if __name__ == "__main__":
    sys.addaudithook(deny_external_process)
    raise SystemExit(main())
