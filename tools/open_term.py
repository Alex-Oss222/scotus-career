#!/usr/bin/env python3
"""Create the four-file term workspace scaffold from the case-list inventory."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

ROW = re.compile(r"^\|\s*(OT_\d{4}CHUNK\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")

def read_inventory(path: Path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if m:
            chunk, case, citation, date, date_status, matter_type = m.groups()
            rows.append((date, chunk, case, citation, matter_type, date_status))
    if not rows:
        raise SystemExit(f"no inventory rows parsed from {path}")
    return sorted(rows)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term", help="OT1993")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    root = args.root.resolve()
    term = root / "terms" / args.term
    rows = read_inventory(term / "case-list.md")
    ws = term / "workspace"
    ws.mkdir(parents=True, exist_ok=True)
    manifest = ws / "manifest.md"
    if manifest.exists() and manifest.stat().st_size and not args.force:
        raise SystemExit(f"{manifest} already exists; term appears opened")

    year = args.term.removeprefix("OT")
    header = f"# {args.term} Full-Term Event Manifest\n\nGenerated from case-list.md. Open must add validated carryovers from Standing State and any expressly supplied additions before first adjudication.\n\n"
    table = "| Event date | Chunk | Case or matter | Citation | Matter type | Date status | Status |\n|---|---|---|---|---|---|---|\n"
    for date, chunk, case, citation, matter_type, date_status in rows:
        table += f"| {date} | {chunk} | {case} | {citation} | {matter_type} | {date_status} | Open |\n"
    manifest.write_text(header + table, encoding="utf-8")

    (ws / "ledger.md").write_text(
        f"# {args.term} Term Working Ledger\n\nNo current-term Record has yet been committed. Rebuild with tools/rebuild_ledger.py after each Run.\n",
        encoding="utf-8",
    )
    (ws / "continuity.md").write_text(
        f"# {args.term} Term Continuity Note\n\nOpen task must populate this projection from the validated opening state. Records control if this projection conflicts with them.\n",
        encoding="utf-8",
    )
    (ws / "neutral-projection.md").write_text(
        f"# {args.term} Current-Term Neutral Projection\n\nOpen task must populate this sanitized projection from the validated opening state. It must exclude Stone-private material, comparators, provisional commitments, reconciliation, and audit annexes.\n",
        encoding="utf-8",
    )
    print(f"Created workspace for {args.term} with {len(rows)} inventory events")

if __name__ == "__main__":
    main()
