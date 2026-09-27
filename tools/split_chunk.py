#!/usr/bin/env python3
"""Regenerate NEUTRAL / STONE / COMPARATOR runtime files from an approved chunk brief.

This tool is mechanical. It never changes, summarizes, or interprets substantive text.
"""
from __future__ import annotations
import argparse, pathlib, re, sys

SECTION = re.compile(r"^###\s+SECTION\s+(I{1,3})\b", re.I)
CASE = re.compile(r"^##\s+(.+?)\s*$")

CHANNEL = {"I": "NEUTRAL", "II": "STONE", "III": "COMPARATOR"}

def split_text(text: str) -> dict[str, str]:
    lines = text.splitlines(keepends=True)
    preamble: list[str] = []
    out = {v: [] for v in CHANNEL.values()}
    current_case: str | None = None
    current_channel: str | None = None
    seen_section = False
    emitted_case = {v: None for v in CHANNEL.values()}

    for line in lines:
        cm = CASE.match(line.rstrip("\n"))
        sm = SECTION.match(line.rstrip("\n"))
        if cm and not sm:
            current_case = line.rstrip("\n")
            current_channel = None
            if not seen_section:
                preamble.append(line)
            continue
        if sm:
            seen_section = True
            key = sm.group(1).upper()
            current_channel = CHANNEL.get(key)
            if current_channel is None:
                raise ValueError(f"Unsupported section heading: {line.strip()}")
            if current_case and emitted_case[current_channel] != current_case:
                out[current_channel].append("\n" + current_case + "\n\n")
                emitted_case[current_channel] = current_case
            out[current_channel].append(line)
            continue
        if not seen_section:
            preamble.append(line)
        elif current_channel:
            out[current_channel].append(line)

    if not all(out.values()):
        missing = [k for k, v in out.items() if not v]
        raise ValueError("Missing section channel(s): " + ", ".join(missing))

    head = "".join(preamble).rstrip() + "\n\n"
    return {k: head + "".join(v).lstrip() for k, v in out.items()}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("brief", type=pathlib.Path)
    ap.add_argument("--out-dir", type=pathlib.Path)
    ap.add_argument("--check", action="store_true")
    ns = ap.parse_args()
    brief = ns.brief
    out_dir = ns.out_dir or brief.parent.parent / "runtime"
    parts = split_text(brief.read_text(encoding="utf-8"))
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = brief.stem
    failed = False
    for channel, content in parts.items():
        path = out_dir / f"{stem}_{channel}.md"
        if ns.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                print(f"STALE: {path}", file=sys.stderr)
                failed = True
        else:
            path.write_text(content, encoding="utf-8")
            print(path)
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
