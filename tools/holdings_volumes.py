#!/usr/bin/env python3
"""Maintain doctrinal Holdings volumes and the continuous compatibility view."""
from __future__ import annotations
import argparse
from pathlib import Path

AREAS = [
    ("Constitutional Structure", "constitutional-structure"),
    ("Federal Courts", "federal-courts"),
    ("Criminal Procedure", "criminal-procedure"),
    ("Civil Rights", "civil-rights"),
    ("First Amendment", "first-amendment"),
    ("Election Law", "election-law"),
    ("Administrative Law", "administrative-law"),
    ("Immigration", "immigration"),
    ("Federal Indian Law", "federal-indian-law"),
    ("Labor and Employment", "labor-and-employment"),
    ("Maritime Law", "maritime-law"),
    ("Bankruptcy", "bankruptcy"),
    ("Federal Taxation", "federal-taxation"),
    ("Tort Law", "tort-law"),
    ("Environmental Law", "environmental-law"),
    ("Business and Commercial Law", "business-and-commercial-law"),
    ("Property and Economic Rights", "property-and-economic-rights"),
    ("Antitrust", "antitrust"),
]

def header_and_sections(text: str):
    lines = text.splitlines()
    starts = [(i, line[3:].strip()) for i, line in enumerate(lines) if line.startswith("## ")]
    if not starts:
        raise ValueError("no doctrinal headings found")
    header = "\n".join(lines[:starts[0][0]]).rstrip()
    sections = {}
    for n, (start, name) in enumerate(starts):
        end = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
        sections[name] = "\n".join(lines[start:end]).strip()
    return header, sections

def split(root: Path):
    source = root / "state" / "HOLDINGS.md"
    header, sections = header_and_sections(source.read_text(encoding="utf-8"))
    out = root / "state" / "holdings"
    out.mkdir(parents=True, exist_ok=True)
    expected = {name for name, _ in AREAS}
    if set(sections) != expected:
        missing = expected - set(sections)
        extra = set(sections) - expected
        raise SystemExit(f"area mismatch; missing={sorted(missing)} extra={sorted(extra)}")
    for name, slug in AREAS:
        (out / f"{slug}.md").write_text(header + "\n\n" + sections[name] + "\n", encoding="utf-8")

def build(root: Path, check: bool):
    vol = root / "state" / "holdings"
    headers, sections = [], []
    for name, slug in AREAS:
        path = vol / f"{slug}.md"
        header, parsed = header_and_sections(path.read_text(encoding="utf-8"))
        if list(parsed) != [name]:
            raise SystemExit(f"{path}: expected only area {name!r}")
        headers.append(header)
        sections.append(parsed[name])
    if len(set(headers)) != 1:
        raise SystemExit("volume publication headers are not synchronized")
    generated = headers[0] + "\n\n" + "\n\n".join(sections) + "\n"
    target = root / "state" / "HOLDINGS.md"
    if check:
        if target.read_text(encoding="utf-8") != generated:
            raise SystemExit("state/HOLDINGS.md is stale relative to doctrinal volumes")
        print("OK: Holdings volumes and compatibility view are synchronized")
    else:
        target.write_text(generated, encoding="utf-8")
        print(target)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=("split", "build", "check"))
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = ap.parse_args()
    if args.command == "split":
        split(args.root)
    else:
        build(args.root, args.command == "check")

if __name__ == "__main__":
    main()
