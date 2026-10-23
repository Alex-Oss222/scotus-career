#!/usr/bin/env python3
"""Register already-validated chunk-2 Records and copy their public deltas.

Clerical only: the calling assembly context must first validate and release
each Record. Does not decide law, votes, assignments, or source sufficiency.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

TERM = Path(__file__).resolve().parents[1]
ORDER = TERM / "freeze/OT_1997CHUNK2_RECORD_COMMIT_ORDER.json"
PROJECTION = TERM / "workspace/neutral-projection.md"
MARKER = "## Later completed public events during chunk 2"

data = json.loads(ORDER.read_text())
existing = {row["file"]: row for row in data["records"]}
neutral = PROJECTION.read_text()
if MARKER not in neutral:
    raise SystemExit("Expected current chunk-2 public-delta section")
for name in sys.argv[1:]:
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
    if len(headings) != 11:
        raise SystemExit("Expected eleven public blocks: " + name)
    row = {"file": name, "event_date": event.group(1), "sha256": digest,
           "status": "assembly substantive validation and mechanical interface checks completed; public delta durably available"}
    data["records"].append(row)
    existing[name] = row
    neutral += "\n" + re.sub(r"^## ", "### ", public, flags=re.M) + "\n"
ORDER.write_text(json.dumps(data, indent=2) + "\n")
PROJECTION.write_text(neutral)
print("Registered Court Records:", len(data["records"]) - 1)
