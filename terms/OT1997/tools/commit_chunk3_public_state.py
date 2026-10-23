#!/usr/bin/env python3
"""Register controller-released Chunk 3 Records and copy bounded public deltas.

This is mechanical publication into the continuation projection, not legal
validation. The assembly context must validate and release each Record first.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

TERM = Path(__file__).resolve().parents[1]
ORDER = TERM / "freeze/OT_1997CHUNK3_RECORD_COMMIT_ORDER.json"
PROJECTION = TERM / "workspace/neutral-projection.md"
MARKER = "## Later completed public events during chunk 3"
data = json.loads(ORDER.read_text())
existing = {row["file"]: row for row in data["records"]}
neutral = PROJECTION.read_text()
if MARKER not in neutral:
    neutral += "\n" + MARKER + "\n\nThe following mechanically copied public projections govern from their effective dates. Same-day independent events share the prior-day baseline.\n"
for spec in sys.argv[1:]:
    key, separator, name = spec.partition("=")
    if not separator or not re.fullmatch(r"[A-Z]+", key):
        raise SystemExit("Pass KEY=Record_basename.md")
    if Path(name).name != name or not name.endswith(".md"):
        raise SystemExit("Pass a Record basename only")
    path = TERM / "records" / name
    body = path.read_text()
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if name in existing:
        if existing[name]["sha256"] != digest:
            raise SystemExit("Released Record changed: " + name)
        continue
    event = re.search(r"^\*\*Event and date:\*\*.*?(\d{4}-\d{2}-\d{2})", body, re.M)
    if not event or body.count("## Public Projection") != 1:
        raise SystemExit("Missing exact Record interface: " + name)
    public = body.split("## Public Projection", 1)[1].strip()
    headings = re.findall(r"^## (.+)$", public, re.M)
    expected = ["Event", "Participation", "Public Action", "Judgment & Remedy",
                "Opinion Topology", "Holdings", "Precedent Treatment",
                "Law After Decision", "Separate Writings", "Procedure After Action", "Source Notes"]
    if headings != expected:
        raise SystemExit("Incorrect eleven-block interface: " + name)
    delta = TERM / "freeze" / ("OT_1997CHUNK3_PUBLIC_DELTA_" + key + ".md")
    if delta.exists() and delta.read_text() != public + "\n":
        raise SystemExit("Released public delta changed: " + key)
    delta.write_text(public + "\n")
    row = {"file": name, "event_date": event.group(1), "sha256": digest,
           "key": key, "public_delta": str(delta.relative_to(TERM)),
           "status": "Assembly substantive validation and mechanical interface checks completed; public delta durably available"}
    data["records"].append(row)
    existing[name] = row
    neutral += "\n" + re.sub(r"^## ", "### ", public, flags=re.M) + "\n"
ORDER.write_text(json.dumps(data, indent=2) + "\n")
PROJECTION.write_text(neutral)
print("Registered Chunk 3 Court Records:", len(data["records"]))
