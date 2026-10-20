"""Project the validated Hendricks Record; never author a Render Input."""
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parents[1]
NAME = "Kansas_v_Hendricks_merits_1997-06-23.md"
RECORD = BASE / "records" / NAME


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise RuntimeError(f"Expected one integration target: {old[:100]!r}")
    return text.replace(old, new, 1)


def read(path):
    return path.read_bytes().decode("utf-8")


def write_preserving_newlines(path, text, original):
    newline = "\r\n" if "\r\n" in original else "\n"
    path.write_bytes(text.replace("\r\n", "\n").replace("\n", newline).encode("utf-8"))


def main():
    record = RECORD.read_text(encoding="utf-8")
    public = record.split("\n## Public Projection\n", 1)[1].strip()
    headings = list(re.finditer(r"^## (.+)$", public, re.M))
    blocks = {m.group(1): public[m.end():headings[i + 1].start() if i + 1 < len(headings) else len(public)].strip()
              for i, m in enumerate(headings)}
    expected = ["Event", "Participation", "Public Action", "Judgment & Remedy", "Opinion Topology", "Holdings",
                "Precedent Treatment", "Law After Decision", "Separate Writings", "Procedure After Action", "Source Notes"]
    if list(blocks) != expected:
        raise RuntimeError("Unexpected Public Projection structure")
    result = re.search(r"^\*\*Result:\*\* (.+)$", record, re.M).group(1)
    caption = "Kansas v. Hendricks; Hendricks v. Kansas, Nos. 95-1649 and 95-9075"
    entry = f"### 1997-06-23 — {caption}\n\nAuthority: [Record](../records/{NAME}).\n\n"

    def nest(content):
        return re.sub(r"^(#{3,}) ", r"##\1 ", content, flags=re.M)

    law = entry + "\n\n".join("#### " + key + "\n\n" + nest(blocks[key])
                                for key in ["Holdings", "Precedent Treatment", "Law After Decision"]) + "\n\n"
    separate = entry + nest(blocks["Separate Writings"]) + "\n\n"
    procedure = entry + nest(blocks["Procedure After Action"]) + "\n\n"

    manifest_path = BASE / "workspace/manifest.md"
    manifest_original = read(manifest_path)
    manifest = manifest_original.replace("\r\n", "\n")
    lines = manifest.splitlines()
    matches = [i for i, line in enumerate(lines) if line.startswith("| 1997-06-23 | OT_1996CHUNK11 | Kansas v. Hendricks /")]
    if len(matches) != 1:
        raise RuntimeError("Hendricks inventory row missing or duplicated")
    row_index = matches[0]
    row = lines[row_index]
    cells = [cell.strip() for cell in row.strip("|").split("|")]
    if not cells[6].startswith("Stopped:"):
        raise RuntimeError("Expected the preserved Hendricks stopped status")
    # Clear only this resolved blocker so the original manifest tool can match its new Record.
    cells[6] = "Open"
    lines[row_index] = "| " + " | ".join(cells) + " |"
    manifest = "\n".join(lines) + ("\n" if manifest.endswith("\n") else "")
    manifest = replace_once(manifest, "129 current-term Court events", "130 current-term Court events")
    manifest = replace_once(manifest,
        "Chunk 11 has eleven completed events and one stopped matter: Kansas v. Hendricks / Hendricks v. Kansas, whose exact blocker is in its inventory row. It remains open without a Court disposition.",
        "All twelve chunk 11 events are complete, with no stopped matter.")
    manifest = replace_once(manifest,
        "The next unresolved inventory entry is Hendricks; the next not-yet-taken-up entry is Lindh v. Murphy in chunk 12.",
        "The next unresolved inventory entry is Lindh v. Murphy in chunk 12.")
    next_row = next(line for line in lines if line.startswith("| 1997-06-23 | OT_1996CHUNK12 | Lindh v. Murphy |"))

    updates = []
    for filename in ["continuity.md", "neutral-projection.md"]:
        path = BASE / "workspace" / filename
        original = read(path)
        text = original.replace("\r\n", "\n")
        text = replace_once(text, "**129 Court events and 3 admitted sources**", "**130 Court events and 3 admitted sources**")
        old_row = next(line for line in text.splitlines() if line.startswith("| 1997-06-23 | OT_1996CHUNK11 | Kansas v. Hendricks /"))
        text = replace_once(text, old_row, next_row)
        if filename == "continuity.md":
            event_row = f"| 1997-06-23 | {caption}. | {result} | [Record](../records/{NAME}) |\n\n"
            text = replace_once(text, "\n\n## 3. Current Law", "\n" + event_row + "## 3. Current Law")
            text = replace_once(text, "## 4. Material Published Noncontrolling Positions", law + "## 4. Material Published Noncontrolling Positions")
            text = replace_once(text, "## 5. Current Procedure and Institution", separate + "## 5. Current Procedure and Institution")
            text = replace_once(text, "## 6. Blockers and Revalidation Needs", procedure + "## 6. Blockers and Revalidation Needs")
            start = text.index("Chunk 11 has 11 completed Court events and 1 stopped matter.")
            end = text.index("The separate Gaydos certiorari submission", start)
            text = text[:start] + "Chunk 11 has 12 completed Court events and no stopped matter.\n\n" + text[end:]
        else:
            text = replace_once(text, "## Material published noncontrolling positions", law + "## Material published noncontrolling positions")
            text = replace_once(text, "## Public procedure after completed actions", separate + "## Public procedure after completed actions")
            text = replace_once(text, "## Scope and cutoff", procedure + "## Scope and cutoff")
            text = replace_once(text, "Coverage is 129 Court events", "Coverage is 130 Court events")
        updates.append((path, text, original))

    ledger_path = BASE / "workspace/ledger.md"
    ledger_original = read(ledger_path)
    ledger = replace_once(ledger_original,
        "Newly written Records are appended by filesystem creation order, with effective date and case name resolving ties;",
        "Newly written Records are appended in the explicit order supplied to the no-Git rebuild runner;")
    # Validate every target above before beginning the coordinated projection writes.
    write_preserving_newlines(manifest_path, manifest, manifest_original)
    for path, text, original in updates:
        write_preserving_newlines(path, text, original)
    write_preserving_newlines(ledger_path, ledger, ledger_original)
    stopped = BASE / "freeze/OT_1996CHUNK11_STOPPED_INDEX.json"
    stopped.write_text(json.dumps({
        "stopped_matters": [],
        "resolved_matter": "Kansas v. Hendricks / Hendricks v. Kansas",
        "record": NAME,
        "court_action": "Affirmed on the as-applied Ex Post Facto ground, 5-4; 1997-06-23.",
        "assembly_receipt": "OT_1996CHUNK11_HENDRICKS_V3_ASSEMBLY.md"
    }, indent=2) + "\n", encoding="utf-8")
    print("Projected the validated Hendricks Record into continuity and neutral state; cleared only its obsolete blocker. Run original rebuild tools next.")


if __name__ == "__main__":
    main()
