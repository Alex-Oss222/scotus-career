#!/usr/bin/env python3
"""Rebuild the inventory portion of a term manifest from case-list and Records."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

ROW = re.compile(r"^\|\s*(OT_\d{4}CHUNK\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")
# Chronological case-index form: | No. | chunk | caption | docket(s) | date | event type | category |
INDEX_ROW = re.compile(r"^\|\s*\d+\s*\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")
CASE = re.compile(r"^\*\*Case and dockets:\*\*\s*(.+)$", re.M)
EVENT = re.compile(r"^\*\*Event and date:\*\*\s*(.+)$", re.M)
DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")

def parse_row(line: str, year: str):
    m = ROW.match(line)
    if m:
        chunk, case, citation, date, date_status, matter_type = m.groups()
        return (date, chunk, case, citation, matter_type, date_status)
    m = INDEX_ROW.match(line)
    if m:
        n, case, dockets, date, event_type, category = m.groups()
        return (date, f"OT_{year}CHUNK{n}", case, dockets, category, event_type)
    return None

def inventory(path: Path, year: str):
    rows = [row for line in path.read_text(encoding="utf-8").splitlines() if (row := parse_row(line, year))]
    # Stable sort by date only: the case list's own order controls same-day ties.
    return sorted(rows, key=lambda r: r[0])

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
    rows = inventory(term / "case-list.md", args.term.removeprefix("OT"))
    done = completed(term / "records")
    stopped, carried = parse_kv(args.stopped), parse_kv(args.carried)

    lines = [
        f"# {args.term} Full-Term Event Manifest", "",
        "Generated from case-list.md and canonical Records. Standing State carryovers or later authorized additions not present in case-list must be appended below the inventory table and preserved on regeneration.",
        "",
        "| Event date | Chunk | Case or matter | Citation or docket | Matter type | Date status or event type | Status |",
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
    # Preserve every section appended below the inventory table (carryovers,
    # institutional calendar, controls): from the first "## " heading onward.
    preserved = ""
    if target.exists():
        m = re.search(r"^## ", target.read_text(encoding="utf-8"), re.M)
        if m:
            preserved = "\n" + target.read_text(encoding="utf-8")[m.start():].rstrip() + "\n"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines) + "\n" + preserved, encoding="utf-8")
    print(f"{target}: {len(rows)} inventory events")

if __name__ == "__main__":
    main()
