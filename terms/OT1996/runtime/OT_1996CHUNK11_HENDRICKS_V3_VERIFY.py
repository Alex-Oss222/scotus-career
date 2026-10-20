"""Check the bounded Hendricks integration without external processes."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "terms/OT1996"
STEM = "OT_1996CHUNK11_HENDRICKS_V3"
NAME = "Kansas_v_Hendricks_merits_1997-06-23.md"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(text):
    lines = text.splitlines()
    h = next(i for i, line in enumerate(lines) if line.startswith("| Event date | Chunk | Case or matter |"))
    rows = []
    for line in lines[h + 2:]:
        if not line.startswith("|"):
            break
        rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows


def main():
    baseline = json.loads((BASE / "freeze" / (STEM + "_BASELINE.json")).read_text(encoding="utf-8"))
    invariants = json.loads((BASE / "freeze" / (STEM + "_INVARIANTS.json")).read_text(encoding="utf-8"))
    allowed = {"terms/OT1996/" + name for name in [
        "workspace/manifest.md", "workspace/ledger.md", "workspace/continuity.md",
        "workspace/neutral-projection.md", "render-inputs/OT_1996CHUNK11.md",
        "freeze/OT_1996CHUNK11_STOPPED_INDEX.json"]}
    changed, missing = [], []
    for name, digest in baseline.items():
        path = ROOT / name
        if not path.exists():
            missing.append(name)
        elif sha(path) != digest:
            changed.append(name)
    assert not missing, missing
    assert set(changed) == allowed, sorted(set(changed) ^ allowed)
    current_records = {p.name for p in (BASE / "records").glob("*.md")}
    prior_records = {Path(name).name for name in baseline if name.startswith("terms/OT1996/records/") and name.endswith(".md")}
    assert current_records - prior_records == {NAME}
    assert len(current_records) == 133 and len(prior_records) == 132

    manifest = (BASE / "workspace/manifest.md").read_text(encoding="utf-8")
    rows = inventory(manifest)
    assert len(rows) == len(invariants["inventory_rows"]) == 153
    changed_rows = []
    for old, new in zip(invariants["inventory_rows"], rows):
        assert old[:6] + old[7:] == new[:6] + new[7:], (old, new)
        if old != new:
            changed_rows.append(new)
    assert len(changed_rows) == 1
    assert changed_rows[0][2] == "Kansas v. Hendricks / Hendricks v. Kansas"
    assert changed_rows[0][6] == "Completed: " + NAME

    render_path = BASE / "render-inputs/OT_1996CHUNK11.md"
    render = render_path.read_text(encoding="utf-8")
    blocks = re.findall(r"<!-- source-record: ([^>]+) -->\n(.*?)(?=\n---\n|\Z)", render, re.S)
    names = [name.strip() for name, _body in blocks]
    assert len(names) == len(set(names)) == 12
    assert set(names) == set(invariants["prior_render_records"]) | {NAME}
    assert "**Completed events:** 12" in render
    assert "**Stopped matters:**" not in render
    assert "## Workflow Blockers" not in render
    for name, body in blocks:
        source = (BASE / "records" / name.strip()).read_text(encoding="utf-8")
        expected = source.split("\n## Public Projection\n", 1)[1].strip()
        assert body.strip() == expected, name

    record = (BASE / "records" / NAME).read_text(encoding="utf-8")
    public = record.split("\n## Public Projection\n", 1)[1]
    expected_headings = ["Event", "Participation", "Public Action", "Judgment & Remedy", "Opinion Topology", "Holdings",
                         "Precedent Treatment", "Law After Decision", "Separate Writings", "Procedure After Action", "Source Notes"]
    assert re.findall(r"^## (.+)$", public, re.M) == expected_headings
    assert not re.search(r"\b(?:Version [123]|simulated|user-directed|approval (?:history|reference)|approved by the user|commit [a-f0-9]{7,40}|research cutoff)\b", public, re.I)

    workspace_paths = [BASE / "workspace" / name for name in ["manifest.md", "ledger.md", "continuity.md", "neutral-projection.md"]]
    for path in workspace_paths:
        text = path.read_text(encoding="utf-8")
        assert NAME in text
        assert "No majority supports a complete disposition" not in text
    for name in ["continuity.md", "neutral-projection.md"]:
        text = (BASE / "workspace" / name).read_text(encoding="utf-8")
        assert "**130 Court events and 3 admitted sources**" in text
        assert "| 1997-06-23 | OT_1996CHUNK12 | Lindh v. Murphy |" in text
    neutral = (BASE / "workspace/neutral-projection.md").read_text(encoding="utf-8")
    assert "HENDRICKS_V3" not in neutral

    # New public links resolve only inside known authorized locations or externally.
    links = re.findall(r"\]\(([^)]+)\)", public)
    checked_local = []
    for link in links:
        if re.match(r"(?:https?://|mailto:|#)", link):
            continue
        local = link.split("#", 1)[0]
        path = ((BASE / "records") / local).resolve()
        relative = path.relative_to(ROOT)
        assert relative.parts[0].lower() in {"terms", "state", "foundation", "tmp"}, str(relative)
        assert path.exists(), str(relative)
        checked_local.append(relative.as_posix())

    summary = {
        "status": "passed",
        "prior_records_unchanged": len(prior_records),
        "new_record": NAME,
        "inventory_rows": len(rows),
        "inventory_status_rows_changed": len(changed_rows),
        "chunk11_projection_blocks": len(blocks),
        "stopped_chunk11_matters": 0,
        "changed_existing_files": sorted(changed),
        "briefs_case_list_outputs_and_frozen_handoffs_unchanged": True,
        "public_projection_identity": True,
        "checked_local_public_links": checked_local,
        "git_verification": "Not performed; no Git command is authorized.",
        "record_sha256": sha(BASE / "records" / NAME),
        "render_input_sha256": sha(render_path),
    }
    target = BASE / "freeze" / (STEM + "_PACKAGE_CHECKS.json")
    target.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: summary[key] for key in ["status", "prior_records_unchanged", "inventory_rows", "chunk11_projection_blocks", "stopped_chunk11_matters"]}))


if __name__ == "__main__":
    main()
