#!/usr/bin/env python3
"""Deterministic structural checks for an October Term.

This checker validates repository structure and synchronization only. It never predicts
votes, forms coalitions, interprets precedent, decides historical departures, applies
Marks, chooses remedies, or generates holdings.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

from split_chunk import split_text

PUBLIC_FORBIDDEN = (
    "Simulation Workflow Blockers",
    "research cutoff",
    "user-directed",
    "approved Stone",
    "approved by the user",
    "the simulated ",
    "simulation inference",
    "true blindness",
)
RECORD_HEADERS = (
    "**Case and dockets:**",
    "**Event and date:**",
    "**Result:**",
    "**Record version and supersession:**",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int)
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path("."))
    args = parser.parse_args()

    root = args.root.resolve()
    term = root / "terms" / f"OT{args.year}"
    errors: list[str] = []
    warnings: list[str] = []

    if not term.exists():
        errors.append(f"missing term directory: {term}")
    elif args.year >= 1993:
        for name in (
            "runtime", "entering-law", "freeze", "validation", "workspace",
            "records", "render-inputs", "output", "close",
        ):
            if not (term / name).exists():
                errors.append(f"missing OT{args.year} directory: {name}")

    output_dir = term / "output"
    if output_dir.exists():
        for path in sorted(output_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            for token in PUBLIC_FORBIDDEN:
                if token.lower() in text.lower():
                    errors.append(f"{path}: public workflow/provenance token: {token}")

    records_dir = term / "records"
    if args.year >= 1993 and records_dir.exists():
        for path in sorted(records_dir.glob("*.md")):
            if path.name == ".gitkeep":
                continue
            text = path.read_text(encoding="utf-8")
            opening = "\n".join(text.splitlines()[:18])
            for header in RECORD_HEADERS:
                if header not in opening:
                    errors.append(f"{path}: missing opening field {header}")
            if "## Public projection" not in text:
                errors.append(f"{path}: missing bounded Public projection")
            if not re.search(r"_\d{4}-\d{2}-\d{2}\.md$", path.name):
                warnings.append(f"{path}: filename lacks natural-key date suffix")

    render_input_dir = term / "render-inputs"
    inputs = {p.name for p in render_input_dir.glob("OT_*CHUNK*.md")} if render_input_dir.exists() else set()
    outputs = {p.name for p in output_dir.glob("OT_*CHUNK*.md")} if output_dir.exists() else set()
    for name in sorted(outputs - inputs):
        errors.append(f"public chunk lacks Render Input: {name}")

    briefs_dir = term / "briefs"
    runtime_dir = term / "runtime"
    if args.year >= 1993 and briefs_dir.exists() and runtime_dir.exists():
        for brief in sorted(briefs_dir.glob("OT_*CHUNK*.md")):
            try:
                expected = split_text(brief.read_text(encoding="utf-8"))
            except ValueError as exc:
                errors.append(f"{brief}: {exc}")
                continue
            for channel, content in expected.items():
                path = runtime_dir / f"{brief.stem}_{channel}.md"
                if not path.exists():
                    errors.append(f"{brief}: missing runtime split {path.name}")
                elif path.read_text(encoding="utf-8") != content:
                    errors.append(f"{brief}: stale runtime split {path.name}")

    standing = root / "state" / "STANDING_STATE.md"
    if standing.exists():
        text = standing.read_text(encoding="utf-8")
        if "state/STANDING_STATE.md#3-standing-practices" in text:
            errors.append("STANDING_STATE.md contains a self-referential standing-practice source link")

    close_dir = term / "close"
    if close_dir.exists() and (close_dir / "AUDIT.md").exists():
        candidates = list(close_dir.glob("*.candidate.md"))
        if candidates:
            warnings.append("close/AUDIT.md exists while candidate tracker files remain")

    for warning in warnings:
        print("WARN:", warning)
    for error in errors:
        print("ERROR:", error, file=sys.stderr)

    print(f"checked OT{args.year}: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
