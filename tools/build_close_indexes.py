#!/usr/bin/env python3
"""Generate reader and audit indexes from canonical Records.

The script extracts already-written Record text. It never decides whether a
writing is controlling, whether a departure is justified, or which future
case is affected.
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

CASE = re.compile(r"^\*\*Case and dockets:\*\*\s*(.+)$", re.M)
EVENT = re.compile(r"^\*\*Event and date:\*\*\s*(.+)$", re.M)
RESULT = re.compile(r"^\*\*Result:\*\*\s*(.+)$", re.M)
DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
DEPARTURE = re.compile(r"^\*\*Historical departure:\*\*\s*(.+)$", re.M)
CONSEQUENCE = re.compile(r"^\*\*Consequence:\*\*\s*(.+)$", re.M)

def first_body_line(text: str, heading: str):
    m = re.search(rf"^##\s+(?:\d+\.\s*)?{re.escape(heading)}\s*$", text, re.M | re.I)
    if not m:
        return ""
    tail = text[m.end():].splitlines()
    for line in tail:
        if line.startswith("## "):
            break
        clean = line.strip()
        if clean and not clean.startswith("|") and not clean.startswith("<!--"):
            return clean
    return ""

def public_section(text: str, heading: str):
    m = re.search(rf"^##\s+(?:\d+\.\s*)?{re.escape(heading)}\s*$", text, re.M | re.I)
    if not m:
        return ""
    nxt = re.search(r"^##\s+", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return text[m.end():end].strip()

def meta(path: Path):
    text = path.read_text(encoding="utf-8")
    cm, em, rm = CASE.search(text), EVENT.search(text), RESULT.search(text)
    if not (cm and em and rm):
        raise ValueError(f"{path}: missing fixed opening block")
    dm = DATE.search(em.group(1))
    if not dm:
        raise ValueError(f"{path}: missing event date")
    return {
        "path": path, "text": text, "case": cm.group(1).strip(),
        "event": em.group(1).strip(), "date": dm.group(1), "result": rm.group(1).strip(),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term", help="OT1993")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = ap.parse_args()
    root = args.root.resolve()
    term = root / "terms" / args.term
    records = [meta(p) for p in (term / "records").glob("*.md") if not p.name.startswith(".")]
    records.sort(key=lambda d: (d["date"], d["case"]))
    close = term / "close"
    close.mkdir(parents=True, exist_ok=True)

    idx = [
        f"# {args.term} Term Index", "",
        "| Date | Case and dockets | Result | Public action | Opinion topology |",
        "|---|---|---|---|---|",
    ]
    for d in records:
        action = first_body_line(d["text"], "Public Action").replace("|", "\\|")
        topo = first_body_line(d["text"], "Opinion Topology").replace("|", "\\|")
        idx.append(f"| {d['date']} | {d['case']} | {d['result']} | {action} | {topo} |")
    (term / "INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    sw = [f"# {args.term} Separate Writings Index", "", "Generated from the Public Projection blocks of canonical Records.", ""]
    for d in records:
        block = public_section(d["text"], "Separate Writings")
        if block and block.casefold() not in {"none.", "none", "no separate writings."}:
            sw += [f"## {d['date']} — {d['case']}", "", block, ""]
    if len(sw) == 4:
        sw.append("No separate writings recorded.")
    (close / "SEPARATE_WRITINGS.md").write_text("\n".join(sw).rstrip() + "\n", encoding="utf-8")

    dep = [f"# {args.term} Departures from the Historical Record", "", "One line per departure expressly recorded in a Canonical Decision Record.", ""]
    for d in records:
        for line in DEPARTURE.findall(d["text"]):
            dep.append(f"- **{d['date']} — {d['case']}:** {line.strip()}")
    if len(dep) == 4:
        dep.append("No historical departures recorded.")
    (close / "DEPARTURES.md").write_text("\n".join(dep) + "\n", encoding="utf-8")

    con = [f"# {args.term} Consequences", "", "Potential future predicates expressly identified in Canonical Decision Records. This page is an audit aid, not authority.", ""]
    for d in records:
        for line in CONSEQUENCE.findall(d["text"]):
            con.append(f"- **{d['date']} — {d['case']}:** {line.strip()}")
    if len(con) == 4:
        con.append("No future-predicate consequences recorded.")
    (close / "CONSEQUENCES.md").write_text("\n".join(con) + "\n", encoding="utf-8")
    print(f"generated indexes from {len(records)} records")

if __name__ == "__main__":
    main()
