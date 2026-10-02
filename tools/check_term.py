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
import sys
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
# Chronological case-index form: | No. | chunk | caption | docket(s) | date | ...
INDEX_CASE_ROW = re.compile(r"^\|\s*\d+\s*\|\s*\d+\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", re.M)
STABLE_ID_CASE_ROW = re.compile(r"^\|\s*\d+\s*\|\s*OT\d{4}-\d+\s*\|\s*\[Chunk\s+\d+\]\([^)]*\)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", re.M)

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

def completed_by_chunk(manifest_text: str):
    """Map each chunk label to the Records its manifest rows mark Completed."""
    lines = manifest_text.splitlines()
    h = next((i for i, line in enumerate(lines) if line.startswith("| Event date | Chunk | Case or matter |")), None)
    out: dict[str, set[str]] = {}
    if h is None:
        return out
    cols = [c.strip() for c in lines[h].strip().strip("|").split("|")]
    ci, si = cols.index("Chunk"), cols.index("Status")
    for line in lines[h + 2:]:
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == len(cols) and cells[si].startswith("Completed:"):
            out.setdefault(cells[ci], set()).update(x.strip() for x in cells[si][len("Completed:"):].split(","))
    return out

def render_input_coverage(rel: str, text: str, expected: set[str]):
    """Errors when a Render Input drops, duplicates or adds events relative to the manifest."""
    errors = []
    names = [x.strip() for x in re.findall(r"<!-- source-record: ([^>]+) -->", text)]
    dupes = sorted({x for x in names if names.count(x) > 1})
    if dupes:
        errors.append(f"{rel}: duplicate source-record blocks: {dupes}")
    m = re.search(r"\*\*Completed events:\*\*\s*(\d+)", text)
    if m and int(m.group(1)) != len(names):
        errors.append(f"{rel}: header says {m.group(1)} completed events but carries {len(names)} blocks")
    missing, extra = sorted(expected - set(names)), sorted(set(names) - expected)
    if missing:
        errors.append(f"{rel}: omits Records the manifest marks Completed for this chunk: {missing[:5]}")
    if extra:
        errors.append(f"{rel}: carries Records the manifest does not mark Completed for this chunk: {extra[:5]}")
    return errors

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
        p = subprocess.run([sys.executable, str(root / "tools" / "holdings_volumes.py"), "check", "--root", str(root)],
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
            p = subprocess.run([sys.executable, str(root / "tools" / "split_chunk.py"), str(brief), "--check"],
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
        listed = {m.group(1).strip() for rx in (CASE_ROW, INDEX_CASE_ROW, STABLE_ID_CASE_ROW) for m in rx.finditer(case_list)}
        mtext = manifest.read_text(encoding="utf-8")
        missing = sorted(case for case in listed if case not in mtext)
        if missing:
            errors.append(f"manifest omits {len(missing)} case-list matters; first: {missing[:5]}")
        # Each chunk's Render Input carries exactly the events its manifest rows mark Completed.
        done = completed_by_chunk(mtext)
        for n in sorted(rin):
            errors += render_input_coverage(str(rin[n].relative_to(root)), rin[n].read_text(encoding="utf-8"),
                                            done.get(f"OT_{args.term.removeprefix('OT')}CHUNK{n}", set()))

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
