#!/usr/bin/env python3
"""Build a verbatim entering-law reading slice from operator-selected authority."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

def take_heading(text: str, query: str):
    lines = text.splitlines()
    starts = [i for i, line in enumerate(lines) if re.match(r"^#{2,5}\s+", line)]
    q = query.casefold()
    for pos, start in enumerate(starts):
        title = re.sub(r"^#{2,5}\s+", "", lines[start]).strip()
        if q in title.casefold():
            level = len(lines[start]) - len(lines[start].lstrip("#"))
            end = len(lines)
            for nxt in starts[pos + 1:]:
                lvl = len(lines[nxt]) - len(lines[nxt].lstrip("#"))
                if lvl <= level:
                    end = nxt
                    break
            return "\n".join(lines[start:end]).strip()
    raise ValueError(f"heading not found: {query}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output", type=Path)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--holdings-area", action="append", default=[], help="doctrinal volume slug")
    ap.add_argument("--standard-heading", action="append", default=[], help="heading substring from Standards and Tests")
    ap.add_argument("--standing-heading", action="append", default=[], help="heading substring from Standing State")
    args = ap.parse_args()
    root = args.root.resolve()
    parts = [
        "# Entering-Law Reading Slice",
        "",
        "Derived reading copy only. The cited state files and effective current-term Records remain authoritative.",
        "",
    ]
    for slug in args.holdings_area:
        path = root / "state" / "holdings" / f"{slug}.md"
        parts += [f"## Holdings volume: {slug}", "", path.read_text(encoding="utf-8").strip(), ""]
    standards = (root / "state" / "STANDARDS_AND_TESTS.md").read_text(encoding="utf-8")
    for query in args.standard_heading:
        parts += [f"## Standards and Tests selection: {query}", "", take_heading(standards, query), ""]
    standing = (root / "state" / "STANDING_STATE.md").read_text(encoding="utf-8")
    for query in args.standing_heading:
        parts += [f"## Standing State selection: {query}", "", take_heading(standing, query), ""]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(args.output)

if __name__ == "__main__":
    main()
