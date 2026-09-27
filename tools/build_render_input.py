#!/usr/bin/env python3
"""Build a chunk Render Input from validated Record Public Projection sections.

Records remain canonical. This script only copies the bounded public projection;
it does not add, delete, paraphrase, or adjudicate content.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

START = re.compile(r"^## Public Projection\s*$", re.M)

def projection(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = START.search(text)
    if not m:
        raise ValueError(f"{path}: missing ## Public Projection")
    return text[m.end():].strip() + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output", type=Path)
    ap.add_argument("records", nargs="+", type=Path)
    args = ap.parse_args()

    blocks = []
    for p in args.records:
        blocks.append(f"<!-- source-record: {p.name} -->\n" + projection(p))
    data = "\n---\n\n".join(blocks).rstrip() + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(data, encoding="utf-8")
    print(args.output)

if __name__ == "__main__":
    main()
