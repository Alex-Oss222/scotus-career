#!/usr/bin/env python3
"""Build a chunk Render Input from validated Record Public Projection sections."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

START = re.compile(r"^## Public Projection\s*$", re.M)
CASE = re.compile(r"^\*\*Case and dockets:\*\*\s*(.+)$", re.M)
EVENT = re.compile(r"^\*\*Event and date:\*\*\s*(.+)$", re.M)
DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
OUT = re.compile(r"OT_(\d{4})CHUNK(\d+)\.md$")

def record_data(path: Path):
    text = path.read_text(encoding="utf-8")
    m = START.search(text)
    cm, em = CASE.search(text), EVENT.search(text)
    if not (m and cm and em):
        raise ValueError(f"{path}: missing fixed opening block or Public Projection")
    dm = DATE.search(em.group(1))
    if not dm:
        raise ValueError(f"{path}: Event and date lacks YYYY-MM-DD")
    return cm.group(1).strip(), dm.group(1), text[m.end():].strip() + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output", type=Path)
    ap.add_argument("records", nargs="+", type=Path)
    ap.add_argument("--stopped", action="append", default=[], help="natural identity: exact blocker")
    args = ap.parse_args()
    om = OUT.match(args.output.name)
    if not om:
        raise SystemExit("output filename must be OT_<year>CHUNK<n>.md")
    year, chunk = om.groups()
    rows = [record_data(p) + (p.name,) for p in args.records]
    rows.sort(key=lambda x: (x[1], x[0]))
    dates = [r[1] for r in rows]
    head = [
        f"# OT_{year}CHUNK{chunk} Render Input",
        "",
        f"**October Term:** {year}. **Completed events:** {len(rows)}. **Chronological range:** {min(dates)} through {max(dates)}.",
    ]
    if args.stopped:
        head += ["", "**Stopped matters:**"] + [f"- {x}" for x in args.stopped]
    blocks = []
    for case, date, proj, filename in rows:
        blocks.append(f"<!-- source-record: {filename} -->\n" + proj.rstrip())
    data = "\n".join(head).rstrip() + "\n\n" + "\n\n---\n\n".join(blocks).rstrip() + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(data, encoding="utf-8")
    print(args.output)

if __name__ == "__main__":
    main()
