#!/usr/bin/env python3
"""Rebuild the inventory portion of a term manifest from case-list and Records."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

ROW = re.compile(r"^\|\s*(OT_\d{4}CHUNK\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")
CASE = re.compile(r"^\*\*Case and dockets:\*\*\s*(.+)$", re.M)
EVENT = re.compile(r"^\*\*Event and date:\*\*\s*(.+)$", re.M)
DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")

def inventory(path: Path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if m:
            chunk, case, citation, date, date_status, matter_type = m.groups()
            rows.append((date, chunk, case, citation, matter_type, date_status))
    return sorted(rows)

def completed(records: Path):
    out = []
    for path in records.glob("*.md"):
        if path.name.startswith("."):
            continue
        text = path.read_text(encoding="utf-8")
        cm, em = CASE.search(text), EVENT.search(text)
        if not (cm and em):
            continue
        dm = DATE.search(em.group(1))
        if dm:
            out.append((dm.group(1), cm.group(1).casefold(), path.name))
    return out

def parse_kv(values):
    result = {}
    for value in values:
        if "=" not in value:
            raise SystemExit(f"expected CASE=TEXT, got {value!r}")
        key, text = value.split("=", 1)
        result[key.casefold()] = text
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term", help="OT1993")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--stopped", action="append", default=[], help="CASE=exact blocker")
    ap.add_argument("--carried", action="append", default=[], help="CASE=carry-forward reason")
    args = ap.parse_args()
    root = args.root.resolve()
    term = root / "terms" / args.term
    rows = inventory(term / "case-list.md")
    done = completed(term / "records")
    stopped, carried = parse_kv(args.stopped), parse_kv(args.carried)

    lines = [
        f"# {args.term} Full-Term Event Manifest", "",
        "Generated from case-list.md and canonical Records. Standing State carryovers or later authorized additions not present in case-list must be appended below the inventory table and preserved on regeneration.",
        "",
        "| Event date | Chunk | Case or matter | Citation | Matter type | Date status | Status |",
        "|---|---|---|---|---|---|---|",
    ]
    for date, chunk, case, citation, matter_type, date_status in rows:
        key = case.casefold()
        matches = [name for d, c, name in done if d == date and (key in c or c.split(", no.")[0] in key)]
        if key in stopped:
            status = "Stopped: " + stopped[key]
        elif key in carried:
            status = "Carry forward: " + carried[key]
        elif matches:
            status = "Completed: " + ", ".join(matches)
        else:
            status = "Open"
        lines.append(f"| {date} | {chunk} | {case} | {citation} | {matter_type} | {date_status} | {status} |")

    target = term / "workspace" / "manifest.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{target}: {len(rows)} inventory events")

if __name__ == "__main__":
    main()
