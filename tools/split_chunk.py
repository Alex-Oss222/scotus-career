#!/usr/bin/env python3
"""Generate OT chunk runtime section files from an approved brief.

This is a mechanical exporter. It does not interpret law, select sources,
model votes, reconcile history, or modify Stone's position.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

CASE_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
SECTION_RE = re.compile(r"^###\s+SECTION\s+(I|II|III)\b.*$", re.M)

def parse_cases(text: str):
    matches = list(CASE_RE.finditer(text))
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].rstrip() + "\n"
        yield m.group(1).strip(), block

def split_case(block: str):
    ms = list(SECTION_RE.finditer(block))
    if len(ms) < 3:
        raise ValueError("case block does not contain SECTION I, II, and III")
    by = {m.group(1): m for m in ms}
    if not all(k in by for k in ("I", "II", "III")):
        raise ValueError("missing required section")
    header = block[:by["I"].start()].rstrip() + "\n\n"
    neutral = header + block[by["I"].start():by["II"].start()].rstrip() + "\n"
    stone = header + block[by["II"].start():by["III"].start()].rstrip() + "\n"
    comparator = header + block[by["III"].start():].rstrip() + "\n"
    return neutral, stone, comparator

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("brief", type=Path)
    ap.add_argument("--outdir", type=Path)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    text = args.brief.read_text(encoding="utf-8")
    title_end = text.find("\n## ")
    preamble = text[:title_end].rstrip() + "\n\n" if title_end >= 0 else ""

    neutral_parts, stone_parts, comparator_parts = [], [], []
    count = 0
    for name, block in parse_cases(text):
        n, s, c = split_case(block)
        neutral_parts.append(n)
        stone_parts.append(s)
        comparator_parts.append(c)
        count += 1
    if not count:
        raise SystemExit("no case blocks found")

    base = args.brief.stem
    outdir = args.outdir or args.brief.parent.parent / "runtime"
    outputs = {
        outdir / f"{base}_NEUTRAL.md": preamble + "\n".join(neutral_parts),
        outdir / f"{base}_STONE.md": preamble + "\n".join(stone_parts),
        outdir / f"{base}_COMPARATOR.md": preamble + "\n".join(comparator_parts),
    }

    if args.check:
        bad = []
        for path, expected in outputs.items():
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                bad.append(str(path))
        if bad:
            raise SystemExit("stale or missing runtime split: " + ", ".join(bad))
        print(f"OK: {count} matters; runtime split is current")
        return

    outdir.mkdir(parents=True, exist_ok=True)
    for path, data in outputs.items():
        path.write_text(data, encoding="utf-8")
        print(path)

if __name__ == "__main__":
    main()
