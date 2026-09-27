#!/usr/bin/env python3
"""Rebuild the current-term ledger index from canonical Records and Git history."""
from __future__ import annotations
import argparse
import re
import subprocess
from pathlib import Path

LABELS = {
    "case": re.compile(r"^\*\*Case and dockets:\*\*\s*(.+)$", re.M),
    "event": re.compile(r"^\*\*Event and date:\*\*\s*(.+)$", re.M),
    "result": re.compile(r"^\*\*Result:\*\*\s*(.+)$", re.M),
    "version": re.compile(r"^\*\*Version / lineage:\*\*\s*(.+)$", re.M),
}
DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")

def git_added(root: Path, path: Path):
    rel = path.relative_to(root).as_posix()
    p = subprocess.run(
        ["git", "-C", str(root), "log", "--diff-filter=A", "--follow", "--format=%ct|%H", "--", rel],
        capture_output=True, text=True,
    )
    rows = [x for x in p.stdout.splitlines() if "|" in x]
    if not rows:
        return (2**63 - 1, "uncommitted")
    ts, sha = rows[-1].split("|", 1)
    return int(ts), sha[:12]

def parse(path: Path):
    text = path.read_text(encoding="utf-8")
    data = {}
    for name, rx in LABELS.items():
        m = rx.search(text)
        if not m:
            raise ValueError(f"{path}: missing {name} opening label")
        data[name] = m.group(1).strip()
    dm = DATE.search(data["event"])
    if not dm:
        raise ValueError(f"{path}: Event and date lacks YYYY-MM-DD")
    data["date"] = dm.group(1)
    return data

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term", help="OT1993")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = ap.parse_args()
    root = args.root.resolve()
    term = root / "terms" / args.term
    rows = []
    for path in sorted((term / "records").glob("*.md")):
        if path.name.startswith("."):
            continue
        data = parse(path)
        ts, sha = git_added(root, path)
        rows.append((ts, path.name, sha, data))
    rows.sort(key=lambda x: (x[0], x[1]))
    out = [
        f"# {args.term} Term Working Ledger",
        "",
        "Generated from canonical Records in Git commitment order. Records control if this index conflicts with them.",
        "",
        "| Commit order | Effective date | Case and dockets | Event | Result | Version / lineage | First-record commit | Record |",
        "|---:|---|---|---|---|---|---|---|",
    ]
    for n, (_, filename, sha, d) in enumerate(rows, 1):
        out.append(f"| {n} | {d['date']} | {d['case']} | {d['event']} | {d['result']} | {d['version']} | {sha} | [record](../records/{filename}) |")
    target = term / "workspace" / "ledger.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{target}: {len(rows)} records")

if __name__ == "__main__":
    main()
