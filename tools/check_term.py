#!/usr/bin/env python3
"""Deterministic repository checks.

These checks are clerical only. They do not predict votes, choose holdings,
decide precedent meaning, form coalitions, apply Marks, or decide whether a
historical departure is substantively justified.
"""
from __future__ import annotations
import argparse
import re
import subprocess
from pathlib import Path

CHUNK = re.compile(r"OT_(\d{4})CHUNK(\d+)\.md$")
RECORD_NAME = re.compile(r".+_[A-Za-z0-9_-]+_\d{4}-\d{2}-\d{2}\.md$", re.I)
RECORD_LABELS = (
    "**Case and dockets:**",
    "**Event and date:**",
    "**Result:**",
    "**Version / lineage:**",
)
PUBLIC_HEADINGS = (
    "Event", "Participation", "Public Action", "Judgment & Remedy",
    "Opinion Topology", "Holdings", "Precedent Treatment",
    "Law After Decision", "Separate Writings", "Procedure After Action",
    "Source Notes",
)
FORBIDDEN_PUBLIC = [
    re.compile(r"\buser-directed\b", re.I),
    re.compile(r"\bversion\s+\d", re.I),
    re.compile(r"\bcommit\s+[0-9a-f]{7,40}\b", re.I),
    re.compile(r"\bresearch cutoff\b", re.I),
    re.compile(r"\bthe simulated\s+[A-Z][A-Za-z'’.-]*\s+holding\b"),
    re.compile(r"^##\s+Simulation Workflow Blockers\s*$", re.M | re.I),
]
CASE_ROW = re.compile(r"^\|\s*OT_\d{4}CHUNK\d+\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", re.M)

def chunks(path: Path):
    return {int(m.group(2)): p for p in path.glob("OT_*CHUNK*.md") if (m := CHUNK.match(p.name))}

def git_object_exists(root: Path, sha: str) -> bool:
    return subprocess.run(["git", "-C", str(root), "cat-file", "-e", sha + "^{commit}"],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

def projection(text: str):
    marker = "## Public Projection"
    i = text.find(marker)
    return text[i + len(marker):].strip() if i >= 0 else None

def check_render_input(root: Path, term: Path, path: Path, errors: list[str]):
    text = path.read_text(encoding="utf-8")
    blocks = list(re.finditer(r"<!-- source-record: ([^>]+) -->\n(.*?)(?=\n---\n|\Z)", text, re.S))
    if not blocks:
        errors.append(f"{path.relative_to(root)}: no generated source-record blocks")
        return
    for m in blocks:
        name, body = m.group(1).strip(), m.group(2).strip()
        record = term / "records" / name
        if not record.exists():
            errors.append(f"{path.relative_to(root)}: missing source Record {name}")
            continue
        expected = projection(record.read_text(encoding="utf-8"))
        if expected is None:
            errors.append(f"{record.relative_to(root)}: missing Public Projection")
        elif body != expected:
            errors.append(f"{path.relative_to(root)}: projection drift from {name}")

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

    modern = int(args.term.removeprefix("OT")) >= 1993

    # Global Holdings volume synchronization.
    if modern:
        p = subprocess.run([str(root / "tools" / "holdings_volumes.py"), "check", "--root", str(root)],
                           capture_output=True, text=True)
        if p.returncode:
            errors.append("Holdings doctrinal volumes are stale or unsynchronized: " + (p.stderr.strip() or p.stdout.strip()))

    briefs = chunks(term / "briefs") if (term / "briefs").exists() else {}
    rin = chunks(term / "render-inputs") if (term / "render-inputs").exists() else {}
    out = chunks(term / "output") if (term / "output").exists() else {}

    for n in sorted(out):
        if n not in rin:
            errors.append(f"chunk {n}: output exists without Render Input")
    for n in sorted(rin):
        if n not in briefs:
            errors.append(f"chunk {n}: Render Input exists without matching brief")
        check_render_input(root, term, rin[n], errors)

    # Runtime split freshness is required once a chunk has a Render Input or output.
    if modern:
        for n in sorted(set(rin) | set(out)):
            brief = briefs.get(n)
            if not brief:
                continue
            p = subprocess.run([str(root / "tools" / "split_chunk.py"), str(brief), "--check"],
                               capture_output=True, text=True)
            if p.returncode:
                errors.append(f"chunk {n}: stale runtime split: " + (p.stderr.strip() or p.stdout.strip()))

    # Four-file workspace and manifest coverage after Open.
    ws = term / "workspace"
    manifest = ws / "manifest.md"
    if modern and manifest.exists():
        required = ["manifest.md", "ledger.md", "continuity.md", "neutral-projection.md"]
        for name in required:
            if not (ws / name).exists():
                errors.append(f"workspace missing {name}")
        case_list = (term / "case-list.md").read_text(encoding="utf-8")
        listed = {m.group(1).strip() for m in CASE_ROW.finditer(case_list)}
        mtext = manifest.read_text(encoding="utf-8")
        missing = sorted(case for case in listed if case not in mtext)
        if missing:
            errors.append(f"manifest omits {len(missing)} case-list matters; first: {missing[:5]}")

    # Record naming and fixed interface.
    for p in sorted((term / "records").glob("*.md")) if (term / "records").exists() else []:
        if p.name.startswith("."):
            continue
        text = p.read_text(encoding="utf-8")
        if modern and not RECORD_NAME.match(p.name):
            errors.append(f"nonstandard new Record filename: {p.name}")
        if modern:
            first = "\n".join(text.splitlines()[:12])
            for label in RECORD_LABELS:
                if label not in first:
                    errors.append(f"{p.relative_to(root)}: missing opening label {label}")
            proj = projection(text)
            if proj is None:
                errors.append(f"{p.relative_to(root)}: missing Public Projection")
            else:
                positions = []
                for heading in PUBLIC_HEADINGS:
                    m = re.search(rf"^##\s+(?:\d+\.\s*)?{re.escape(heading)}\s*$", proj, re.M | re.I)
                    if not m:
                        errors.append(f"{p.relative_to(root)}: Public Projection missing {heading}")
                    else:
                        positions.append(m.start())
                if positions and positions != sorted(positions):
                    errors.append(f"{p.relative_to(root)}: Public Projection blocks out of order")

    # Public voice checks.
    if (term / "output").exists():
        for p in sorted((term / "output").glob("*.md")):
            text = p.read_text(encoding="utf-8")
            for rx in FORBIDDEN_PUBLIC:
                if rx.search(text):
                    errors.append(f"{p.relative_to(root)}: public workflow/provenance leak matching {rx.pattern}")

    standing = root / "state" / "STANDING_STATE.md"
    if standing.exists() and "blob/main/state/STANDING_STATE.md#" in standing.read_text(encoding="utf-8"):
        errors.append("state/STANDING_STATE.md contains a self-referential publication link")

    # Commit references in internal history must resolve.
    for p in term.rglob("*.md"):
        if "/close/" not in p.as_posix() and "/records/" not in p.as_posix():
            continue
        text = p.read_text(encoding="utf-8")
        for sha in set(re.findall(r"(?<![0-9a-f])([0-9a-f]{7,40})(?![0-9a-f])", text, re.I)):
            if not git_object_exists(root, sha):
                warnings.append(f"{p.relative_to(root)}: referenced commit not found: {sha}")

    # Candidates should not survive a completed close.
    audit = term / "close" / "AUDIT.md"
    if audit.exists() and re.search(r"no unresolved", audit.read_text(encoding="utf-8"), re.I):
        candidates = list((term / "close").glob("*.candidate.md"))
        if candidates:
            errors.append("completed close still contains candidate files: " + ", ".join(p.name for p in candidates))

    if errors:
        print("ERRORS")
        for x in errors:
            print(" -", x)
    if warnings:
        print("WARNINGS")
        for x in warnings:
            print(" -", x)
    if errors:
        raise SystemExit(1)
    print(f"OK: {args.term}; {len(warnings)} warning(s)")

if __name__ == "__main__":
    main()
