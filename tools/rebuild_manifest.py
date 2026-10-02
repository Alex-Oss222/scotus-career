#!/usr/bin/env python3
"""Rebuild the inventory portion of a term manifest from case-list and Records.

An existing manifest is refreshed in place: only the Status cell of an
inventory row changes, and inventory rows missing from the table are added.
Everything else in the file, including extra columns and hand-corrected cells,
is preserved. A Stopped or Carry forward status persists until a Record
completes the matter or a new flag replaces it.
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

ROW = re.compile(r"^\|\s*(OT_\d{4}CHUNK\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")
# Chronological case-index form: | No. | chunk | caption | docket(s) | date | event type | category |
INDEX_ROW = re.compile(r"^\|\s*\d+\s*\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")
# Stable-ID case-index form (OT1995+): | Seq | OTyyyy-nnn | [Chunk n](...) | caption | citation | docket(s) | date | category | event type | area of law |
STABLE_ID_ROW = re.compile(r"^\|\s*\d+\s*\|\s*OT\d{4}-\d+\s*\|\s*\[Chunk\s+(\d+)\]\([^)]*\)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")
# Any row that looks like an inventory entry; used to reject a partial parse.
CANDIDATE = re.compile(r"^\|\s*(?:\d+|OT_\d{4}CHUNK\d+)\s*\|.*\b\d{4}-\d{2}-\d{2}\b")
CASE = re.compile(r"^\*\*Case and dockets:\*\*\s*(.+)$", re.M)
EVENT = re.compile(r"^\*\*Event and date:\*\*\s*(.+)$", re.M)
DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
DOCKET = re.compile(r"\b(A-\d+|\d{1,3}-\d{1,5}|\d+,?\s*Orig(?:inal)?\b)", re.I)
HEADER = "| Event date | Chunk | Case or matter | Citation or docket | Matter type | Date status or event type | Status |"
KEPT = ("Stopped:", "Carry forward:", "Open")

def parse_row(line: str, year: str):
    m = ROW.match(line)
    if m:
        chunk, case, citation, date, date_status, matter_type = m.groups()
        return (date, chunk, case, citation, matter_type, date_status)
    m = INDEX_ROW.match(line)
    if m:
        n, case, dockets, date, event_type, category = m.groups()
        return (date, f"OT_{year}CHUNK{n}", case, dockets, category, event_type)
    m = STABLE_ID_ROW.match(line)
    if m:
        n, case, citation, dockets, date, category, event_type, _area = m.groups()
        return (date, f"OT_{year}CHUNK{n}", case, f"{citation}; {dockets}", category, event_type)
    return None

def inventory(path: Path, year: str):
    lines = path.read_text(encoding="utf-8").splitlines()
    rows = [row for line in lines if (row := parse_row(line, year))]
    unparsed = [line for line in lines if CANDIDATE.match(line) and not parse_row(line, year)]
    if not rows or unparsed:
        raise SystemExit(f"{path}: parsed {len(rows)} inventory rows; unparsed: {unparsed[:3]}")
    # Stable sort by date only: the case list's own order controls same-day ties.
    return sorted(rows, key=lambda r: r[0])

def dockets(text: str):
    return {re.sub(r"[\s,.]+", "", m.group(1)).casefold().replace("original", "orig") for m in DOCKET.finditer(text)}

def caption(text: str):
    # The "+" sim-grant marker and " / " consolidated-caption separator are case-list conventions.
    text = text.casefold().replace("+", " ").replace(" / ", "; ")
    return re.sub(r"\s+", " ", text).strip(" ;,.")

def completed(records: Path):
    out = []
    for path in sorted(records.glob("*.md")):
        if path.name.startswith("."):
            continue
        text = path.read_text(encoding="utf-8")
        cm, em = CASE.search(text), EVENT.search(text)
        if not (cm and em):
            continue
        dm = DATE.search(em.group(1))
        if dm:
            out.append((dm.group(1), caption(cm.group(1)), dockets(cm.group(1)), path.name))
    return out

def same_matter(date: str, case: str, citation: str, other_date: str, other_case: str, other_dockets) -> bool:
    """Match on date plus a shared docket, or on the normalized caption."""
    if date != other_date:
        return False
    key = caption(case)
    head = re.split(r"[;,] no\b", other_case)[0]
    return bool(dockets(citation) & other_dockets) or key in other_case or head in key

def status(row, done, stopped, carried, previous: str = ""):
    date, _chunk, case, citation = row[:4]
    key = caption(case)
    if key in stopped:
        return "Stopped: " + stopped[key]
    if key in carried:
        return "Carry forward: " + carried[key]
    found = [name for d, c, dk, name in done if same_matter(date, case, citation, d, c, dk)]
    if found:
        return "Completed: " + ", ".join(found)
    if previous.startswith(KEPT):
        return previous
    return "Open"

def cells(line: str):
    return [c.strip() for c in line.strip().strip("|").split("|")]

def refresh(text: str, rows, done, stopped, carried):
    """Return (new text, rows changed) for an existing manifest, preserving its line endings."""
    nl = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(nl)
    h = next((i for i, line in enumerate(lines) if line.startswith(HEADER)), None)
    if h is None:
        raise SystemExit("existing manifest has no inventory table to refresh")
    width = len(cells(lines[h]))
    col = cells(lines[h]).index("Status")
    end = h + 2
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    existing = [[line, cells(line), False] for line in lines[h + 2:end]]
    out, changed = [], 0
    for row in rows:
        date, chunk, case, citation, matter_type, date_status = row
        match = next((e for e in existing if not e[2] and len(e[1]) == width
                      and same_matter(date, case, citation, e[1][0], caption(e[1][2]), dockets(e[1][3]))), None)
        if match:
            match[2] = True
            new = status(row, done, stopped, carried, match[1][col])
            if new == match[1][col]:
                out.append(match[0])
                continue
            values = match[1][:col] + [new] + match[1][col + 1:]
        else:
            values = [date, chunk, case, citation, matter_type, date_status, status(row, done, stopped, carried)]
            values += [""] * (width - len(values))
        out.append("| " + " | ".join(values) + " |")
        changed += 1
    orphans = [e[0] for e in existing if not e[2]]
    if orphans:
        raise SystemExit("manifest rows match no case-list entry; reconcile before rebuilding:\n" + "\n".join(orphans))
    lines[h + 2:end] = out
    return nl.join(lines), changed

def parse_kv(values):
    result = {}
    for value in values:
        if "=" not in value:
            raise SystemExit(f"expected CASE=TEXT, got {value!r}")
        key, text = value.split("=", 1)
        result[caption(key)] = text
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term", help="OT1993")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--stopped", action="append", default=[], help="CASE=exact blocker")
    ap.add_argument("--carried", action="append", default=[], help="CASE=carry-forward reason")
    args = ap.parse_args()
    root = args.root.resolve()
    term = root / "terms" / args.term
    rows = inventory(term / "case-list.md", args.term.removeprefix("OT"))
    done = completed(term / "records")
    stopped, carried = parse_kv(args.stopped), parse_kv(args.carried)
    unknown = (set(stopped) | set(carried)) - {caption(row[2]) for row in rows}
    if unknown:
        raise SystemExit(f"--stopped/--carried name no case-list entry: {sorted(unknown)}")

    target = term / "workspace" / "manifest.md"
    if target.exists():
        text, changed = refresh(target.read_bytes().decode("utf-8"), rows, done, stopped, carried)
        target.write_bytes(text.encode("utf-8"))
        print(f"{target}: {len(rows)} inventory events; {changed} row(s) updated")
        return
    lines = [
        f"# {args.term} Full-Term Event Manifest", "",
        "Generated from case-list.md and canonical Records. Standing State carryovers or later authorized additions not present in case-list must be appended below the inventory table and preserved on regeneration.",
        "",
        HEADER,
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(list(row) + [status(row, done, stopped, carried)]) + " |")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{target}: {len(rows)} inventory events")

if __name__ == "__main__":
    main()
