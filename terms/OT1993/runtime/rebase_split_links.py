#!/usr/bin/env python3
"""Regenerate/check OT1993 brief splits with the F04 local-link correction.

Uses the repository splitter's parsing functions without modifying that tool or
the approved briefs. Only the relocated Stone-method link target is rebased;
external preparation references and all substantive text remain untouched.
"""
from pathlib import Path
import argparse
import runpy
import sys

sys.dont_write_bytecode = True
TERM = Path(__file__).resolve().parents[1]
ROOT = TERM.parents[1]


def expected_outputs(chunk):
    splitter = runpy.run_path(str(ROOT / "tools/split_chunk.py"))
    brief = TERM / "briefs" / f"OT_1993CHUNK{chunk}.md"
    text = brief.read_text(encoding="utf-8")
    title_end = text.find("\n## ")
    preamble = text[:title_end].rstrip() + "\n\n" if title_end >= 0 else ""
    parts = [[], [], []]
    for name, block in splitter["parse_cases"](text):
        for destination, section in zip(parts, splitter["split_case"](name, block)):
            destination.append(section)
    if not parts[0]:
        raise ValueError(f"No cases in {brief}")
    for kind, sections in zip(("NEUTRAL", "STONE", "COMPARATOR"), parts):
        content = preamble + "\n".join(sections)
        content = content.replace(
            "](OT_1993_STONE_METHOD.md)",
            "](../briefs/OT_1993_STONE_METHOD.md)",
        )
        yield TERM / "runtime" / f"OT_1993CHUNK{chunk}_{kind}.md", content


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chunk", type=int, choices=range(1, 9))
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    for path, expected in expected_outputs(args.chunk):
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                raise SystemExit(f"Stale or missing path-rebased split: {path}")
        else:
            path.write_text(expected, encoding="utf-8", newline="\n")
    print(f"OK: chunk {args.chunk}; three splits {'match' if args.check else 'regenerated from'} approved brief with the F04 link rebase")


if __name__ == "__main__":
    main()
