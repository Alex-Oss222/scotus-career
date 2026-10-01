#!/usr/bin/env python3
"""Generate OT chunk runtime section files from an approved brief.

This exporter is deliberately mechanical. It fails if a case contains more
than one live Section I, II, or III so superseded supplements cannot silently
survive into runtime.
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

CASE_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
SECTION_RE = re.compile(r"^###\s+SECTION\s+(I|II|III)\b.*$", re.M)
SECTION_COMMENT_RE = re.compile(r"<!--\s*(BEGIN|END)_SECTION\s+(I|II|III)\s*-->")

def parse_cases(text: str):
    matches = list(CASE_RE.finditer(text))
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        yield m.group(1).strip(), text[start:end].rstrip() + "\n"

def split_case(name: str, block: str):
    ms = list(SECTION_RE.finditer(block))
    labels = [m.group(1) for m in ms]
    if labels.count("I") != 1 or labels.count("II") != 1 or labels.count("III") != 1:
        raise ValueError(f"{name}: expected exactly one live SECTION I, II, and III; found {labels}")
    by = {m.group(1): m for m in ms}
    if not (by["I"].start() < by["II"].start() < by["III"].start()):
        raise ValueError(f"{name}: sections are not ordered I, II, III")
    header = block[:by["I"].start()].rstrip() + "\n\n"

    def project(label: str, start: int, end: int):
        # The shared header may contain Section I's opening comment. Relabel
        # that marker for this output; retain only this section's body markers.
        # Strip comment tokens only, preserving all visible text and whitespace.
        section_header = SECTION_COMMENT_RE.sub(
            lambda m: f"<!-- BEGIN_SECTION {label} -->" if m.group(1) == "BEGIN" else "",
            header,
        )
        body = block[start:end].rstrip() + "\n"
        body = SECTION_COMMENT_RE.sub(
            lambda m: m.group(0) if m.group(2) == label else "", body
        )
        return section_header + body

    neutral = project("I", by["I"].start(), by["II"].start())
    stone = project("II", by["II"].start(), by["III"].start())
    comparator = project("III", by["III"].start(), len(block))
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
        n, s, c = split_case(name, block)
        neutral_parts.append(n); stone_parts.append(s); comparator_parts.append(c); count += 1
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
        bad = [str(p) for p, expected in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != expected]
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
