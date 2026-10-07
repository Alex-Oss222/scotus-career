#!/usr/bin/env python3
"""Mechanically derive scoped, Public-Projection-only entering law for three revisions.

This tool never emits Record kernels, reads private positions, or changes authority.
The event-header date gates current-term law; same-day records remain excluded.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / "terms" / "OT1995"
ENTERING = TERM / "entering-law"
CONFIG = {
    "VERA": ("1996-06-13", "OT_1995CHUNK8_A_VERA.md"),
    "EGELHOFF": ("1996-06-13", "OT_1995CHUNK8_B_OPENING.md"),
    "LEAVITT": ("1996-06-17", "OT_1995CHUNK8_C_ENTERING_LAW.md"),
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def records():
    result = []
    for path in sorted((TERM / "records").glob("*.md")):
        raw = path.read_bytes()
        # These are the only kernel bytes interpreted: the public identity header
        # and event date. All substantive reading copies start at Public Projection.
        event = re.search(rb"(?m)^\*\*Event and date:\*\*[^\r\n]*", raw)
        if event is None:
            raise ValueError(f"Missing event header: {relative(path)}")
        date = re.search(rb"\d{4}-\d{2}-\d{2}", event.group())
        if date is None:
            raise ValueError(f"Missing ISO event date: {relative(path)}")
        marker = re.search(rb"(?m)^## Public Projection[ \t]*\r?$", raw)
        if marker is None:
            raise ValueError(f"Missing Public Projection: {relative(path)}")
        projection = raw[marker.start():]
        result.append({
            "path": path,
            "date": date.group().decode("ascii"),
            "record_sha256": sha(raw),
            "projection": projection,
            "projection_sha256": sha(projection),
        })
    return sorted(result, key=lambda r: (r["date"], r["path"].name))


def build(matter: str, all_records: list, june13_ready: bool):
    cutoff, baseline_name = CONFIG[matter]
    baseline = ENTERING / baseline_name
    baseline_bytes = baseline.read_bytes()
    baseline_text = baseline_bytes.decode("utf-8")
    selected = {"holdings-area": [], "standard-heading": [], "standing-heading": []}
    labels = {
        "Holdings volume": "holdings-area",
        "Standards and Tests selection": "standard-heading",
        "Standing State selection": "standing-heading",
    }
    for match in re.finditer(r"^## (Holdings volume|Standards and Tests selection|Standing State selection): (.+)$", baseline_text, re.M):
        selected[labels[match[1]]].append(match[2].strip())
    if not any(selected.values()):
        raise ValueError(f"No authorized selections in {relative(baseline)}")

    name = f"OT_1995CHUNK8_REVISION_{matter}"
    output = ENTERING / f"{name}.md"
    copies = ENTERING / f"{name}_PUBLIC_LAW"
    copies.mkdir(parents=True, exist_ok=True)
    command = [sys.executable, str(ROOT / "tools" / "build_entering_law.py"), str(output), "--root", str(ROOT)]
    for flag, values in selected.items():
        for value in values:
            command.extend([f"--{flag}", value])
    subprocess.run(command, check=True, capture_output=True, text=True)

    earlier = [r for r in all_records if r["date"] < cutoff]
    same_day = [r for r in all_records if r["date"] == cutoff]
    later = [r for r in all_records if r["date"] > cutoff]
    expected = {r["path"].name for r in earlier}
    # Remove only obsolete generated Markdown copies in this exact generated folder.
    for old in copies.glob("*.md"):
        if old.name not in expected:
            if old.resolve().parent != copies.resolve():
                raise ValueError("Unexpected generated-copy path")
            old.unlink()
    for r in earlier:
        (copies / r["path"].name).write_bytes(r["projection"])

    inputs = {relative(baseline): sha(baseline_bytes)}
    for slug in selected["holdings-area"]:
        p = ROOT / "state" / "holdings" / f"{slug}.md"
        inputs[relative(p)] = sha(p.read_bytes())
    if selected["standard-heading"]:
        p = ROOT / "state" / "STANDARDS_AND_TESTS.md"
        inputs[relative(p)] = sha(p.read_bytes())
    if selected["standing-heading"]:
        p = ROOT / "state" / "STANDING_STATE.md"
        inputs[relative(p)] = sha(p.read_bytes())
    builder = ROOT / "tools" / "build_entering_law.py"
    inputs[relative(builder)] = sha(builder.read_bytes())

    status = "Complete as to Records presently on disk at the stated strict-before cutoff."
    if matter == "LEAVITT" and not june13_ready:
        status = ("PROVISIONAL: refresh after the June 13 Vera Record is replaced and the Egelhoff Record is assembled. "
                  "The present preceding-record set includes the existing Vera standing-only Record and has no Egelhoff Record. "
                  "Those facts describe file coverage only; they do not establish either revised outcome.")
    elif matter == "LEAVITT":
        if not any("Egelhoff" in r["path"].name for r in earlier):
            raise ValueError("Cannot mark June 13 ready: no earlier Egelhoff Record")
        status = ("Refreshed after operator confirmation that June 13 Vera and Egelhoff assembly is complete; "
                  "every presently existing Record strictly before June 17 is included.")

    text = [
        "", "## Current-term neutral authority coverage", "",
        f"**Matter:** {matter}. **Decision-date cutoff:** {cutoff}. Records dated strictly before this date are included; all same-day Records are excluded to preserve the established same-day baseline.",
        "", f"**Coverage status:** {status}", "",
        "This is a derived reading copy, not new authority. Opening-law selections reproduce the preserved baseline's selection headings through tools/build_entering_law.py. Every preceding current-term Record is available below as an exact, bounded Public Projection-only copy; its Record remains authoritative. No audit annex, comparator reconciliation, private commitment, or private Stone material is copied.",
        "", f"**Counts:** {len(earlier)} preceding Records included; {len(same_day)} same-day Records excluded; {len(later)} later Records excluded.",
        "", "### Opening selection inputs and exact hashes", "",
        "| Input | SHA-256 |", "|---|---|",
    ]
    for path, digest in inputs.items():
        text.append(f"| `{path}` | `{digest}` |")
    text += ["", "### Every preceding Record", "", "Dates below are the precise first ISO dates in the authoritative Event and date headers. Statutory application qualifications remain in the copied Public Projections.", "", "| Event date | Authoritative Record path | Record SHA-256 | Neutral public reading copy | Public Projection SHA-256 |", "|---|---|---|---|---|"]
    for r in earlier:
        path = r["path"]
        text.append(f"| {r['date']} | `{relative(path)}` | `{r['record_sha256']}` | [{path.name}]({copies.name}/{path.name}) | `{r['projection_sha256']}` |")
    text += ["", "### Same-day Records excluded from this baseline", "", "Same-day appearance does not establish an earlier intra-day legal event. The following Records, including any existing revision target, supply no entering law to this matter.", "", "| Date | Excluded Record path | Record SHA-256 |", "|---|---|---|"]
    for r in same_day:
        text.append(f"| {r['date']} | `{relative(r['path'])}` | `{r['record_sha256']}` |")
    with output.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write("\n".join(text) + "\n")

    manifest = {
        "matter": matter, "cutoff": cutoff, "coverage_status": status,
        "slice": relative(output), "slice_sha256": sha(output.read_bytes()),
        "baseline_sha256": sha(baseline_bytes), "selected": selected,
        "inputs": inputs, "preceding_count": len(earlier), "same_day_count": len(same_day),
        "later_count": len(later),
        "preceding_records": [{k: relative(v) if k == "path" else v for k, v in r.items() if k != "projection"} for r in earlier],
        "excluded_same_day": [{k: relative(v) if k == "path" else v for k, v in r.items() if k not in ("projection", "projection_sha256")} for r in same_day],
    }
    manifest_path = ENTERING / f"{name}_INPUTS.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: manifest[k] for k in ("matter", "cutoff", "slice", "slice_sha256", "preceding_count", "same_day_count", "later_count", "coverage_status")}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--matter", choices=["ALL", *CONFIG], default="ALL")
    parser.add_argument("--june13-records-ready", action="store_true", help="Operator confirms replacement Vera and new Egelhoff Records are assembled")
    args = parser.parse_args()
    all_records = records()
    for matter in CONFIG if args.matter == "ALL" else [args.matter]:
        build(matter, all_records, args.june13_records_ready)


if __name__ == "__main__":
    main()
