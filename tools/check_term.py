#!/usr/bin/env python3
"""Deterministic repository checks.

These checks are deliberately clerical. They never predict votes, choose
holdings, decide precedent meaning, form coalitions, or validate a historical
departure on the merits.
"""
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

CHUNK = re.compile(r"OT_(\d{4})CHUNK(\d+)\.md$")
RECORD_NAME = re.compile(r".+_(?:merits|application|order|dismissal|decree|review|motion|transition|amendment|judgment|stay|rehearing|continuity)[A-Za-z0-9_-]*_\d{4}-\d{2}-\d{2}\.md$", re.I)
FORBIDDEN_PUBLIC = [
    re.compile(r"\buser-directed\b", re.I),
    re.compile(r"\bversion\s+\d", re.I),
    re.compile(r"\bcommit\s+[0-9a-f]{7,40}\b", re.I),
    re.compile(r"\bresearch cutoff\s+[A-Za-z]+\s+\d{1,2},\s+20\d{2}\b", re.I),
    re.compile(r"\bthe simulated\s+[A-Z][A-Za-z'’.-]*\s+holding\b"),
]

def chunks(path: Path):
    return {int(m.group(2)): p for p in path.glob("OT_*CHUNK*.md") if (m := CHUNK.match(p.name))}

def git_object_exists(root: Path, sha: str) -> bool:
    return subprocess.run(["git", "-C", str(root), "cat-file", "-e", sha + "^{commit}"],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term", help="e.g. OT1993")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = ap.parse_args()
    root = args.root.resolve()
    term = root / "terms" / args.term
    errors, warnings = [], []

    if not term.exists():
        raise SystemExit(f"missing term folder: {term}")

    briefs = chunks(term / "briefs") if (term / "briefs").exists() else {}
    rin = chunks(term / "render-inputs") if (term / "render-inputs").exists() else {}
    out = chunks(term / "output") if (term / "output").exists() else {}

    for n in sorted(out):
        if n not in rin:
            errors.append(f"chunk {n}: output exists without Render Input")
    for n in sorted(rin):
        if n not in briefs:
            warnings.append(f"chunk {n}: Render Input exists without matching brief")

    for p in sorted((term / "records").glob("*.md")) if (term / "records").exists() else []:
        if p.name == ".gitkeep":
            continue
        if args.term >= "OT1993" and not RECORD_NAME.match(p.name):
            warnings.append(f"nonstandard new record filename: {p.name}")

    if (term / "output").exists():
        for p in sorted((term / "output").glob("*.md")):
            text = p.read_text(encoding="utf-8")
            for rx in FORBIDDEN_PUBLIC:
                if rx.search(text):
                    errors.append(f"{p.relative_to(root)}: public workflow/provenance leak matching {rx.pattern}")

    for p in [root / "state" / "STANDING_STATE.md"]:
        if p.exists():
            text = p.read_text(encoding="utf-8")
            own = "blob/main/state/STANDING_STATE.md#"
            if own in text:
                errors.append("state/STANDING_STATE.md contains a self-referential publication link")

    for p in term.rglob("*.md"):
        if "/close/" not in p.as_posix() and "/records/" not in p.as_posix():
            continue
        text = p.read_text(encoding="utf-8")
        for sha in set(re.findall(r"(?<![0-9a-f])([0-9a-f]{7,40})(?![0-9a-f])", text, re.I)):
            if len(sha) >= 7 and not git_object_exists(root, sha):
                warnings.append(f"{p.relative_to(root)}: referenced commit not found: {sha}")

    if errors:
        print("ERRORS")
        for x in errors: print(" -", x)
    if warnings:
        print("WARNINGS")
        for x in warnings: print(" -", x)
    if errors:
        raise SystemExit(1)
    print(f"OK: {args.term}; {len(warnings)} warning(s)")

if __name__ == "__main__":
    main()
