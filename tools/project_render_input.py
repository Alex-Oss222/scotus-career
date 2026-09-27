#!/usr/bin/env python3
"""Copy bounded Public projection sections from Records into one Render Input.

This tool copies approved public blocks. It does not adjudicate or rewrite them.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

MARKER = "## Public projection"
PRIVATE_MARKERS = (
    "## Adaptive audit annex",
    "## Internal audit",
    "## Historical reconciliation",
    "Provisional commitment",
)


def extract(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8")
    pos = text.find(MARKER)
    if pos < 0:
        raise ValueError(f"{path}: missing {MARKER!r}")
    public = text[pos + len(MARKER):].lstrip("\n")
    for token in PRIVATE_MARKERS:
        if token in public:
            raise ValueError(f"{path}: private material inside Public projection: {token}")
    return public.rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=pathlib.Path)
    parser.add_argument("records", nargs="+", type=pathlib.Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    body = "\n---\n\n".join(extract(path).rstrip() for path in args.records) + "\n"

    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != body:
            print(f"STALE: {args.output}", file=sys.stderr)
            return 1
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(body, encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
