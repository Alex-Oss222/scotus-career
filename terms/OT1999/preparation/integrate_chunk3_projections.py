"""Copy validated public chunk-3 substance into the two cumulative projections.

Default writes review drafts only. Publication requires --publish and the operator's
separate confirmation that all twelve Records are ready. No Git operation occurs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

TERM = Path(__file__).resolve().parents[1]
WORK = TERM / "workspace"
SCRATCH = TERM / "tmp" / "chunk3-projection-integration"
EXPECTED = [
    ("baral-v-united-states_merits_2000-02-22.md", "Baral v. United States"),
    ("hunt-wesson-v-franchise-tax-board_merits_2000-02-22.md", "Hunt-Wesson, Inc. v. Franchise Tax Board"),
    ("weisgram-v-marley_merits_2000-02-22.md", "Weisgram v. Marley Co."),
    ("rice-v-cayetano_merits_2000-02-23.md", "Rice v. Cayetano"),
    ("roe-v-flores-ortega_merits_2000-02-23.md", "Roe v. Flores-Ortega"),
    ("rotella-v-wood_merits_2000-02-23.md", "Rotella v. Wood"),
    ("village-of-willowbrook-v-olech_merits_2000-02-23.md", "Village of Willowbrook v. Olech"),
    ("strout-v-albanese_merits_2000-02-28.md", "Strout v. Albanese"),
    ("shalala-v-illinois-council_merits_2000-02-29.md", "Shalala v. Illinois Council on Long Term Care, Inc."),
    ("united-states-v-johnson_merits_2000-03-01.md", "United States v. Johnson"),
    ("portuondo-v-agard_merits_2000-03-06.md", "Portuondo v. Agard"),
    ("united-states-v-locke-intertanko-v-locke_merits_2000-03-06.md", "United States v. Locke / Intertanko v. Locke"),
]
BLOCKS = ["Event", "Participation", "Public Action", "Judgment & Remedy", "Opinion Topology", "Holdings", "Precedent Treatment", "Law After Decision", "Separate Writings", "Procedure After Action", "Source Notes"]
JUSTICES = ["Stone-Zsela", "Stevens", "O'Connor", "Scalia", "Kennedy", "Souter", "Thomas", "Ginsburg", "Breyer"]
CONTINUITY_BLOCKS = ["Scope and Chronology Cursor", "Completed Events and Admitted Sources", "Current Law", "Material Published Noncontrolling Positions", "Current Procedure and Institution", "Blockers and Revalidation Needs", "Source and Research Cutoff"]
NEUTRAL_BLOCKS = ["Opening law and chronology", "Completed public events and admitted sources", "Current-term law", "Published noncontrolling positions", "Current public procedure and institution"]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def section(text: str, heading: str) -> str:
    match = re.search(r"(?m)^## " + re.escape(heading) + r"[ \t]*$", text)
    if not match:
        raise ValueError(f"Missing section: {heading}")
    following = re.search(r"(?m)^## ", text[match.end():])
    end = match.end() + following.start() if following else len(text)
    return text[match.end():end].strip()


def subsection(text: str, heading: str) -> str:
    match = re.search(r"(?m)^### " + re.escape(heading) + r"[ \t]*$", text)
    if not match:
        raise ValueError(f"Missing subsection: {heading}")
    following = re.search(r"(?m)^#{2,3} ", text[match.end():])
    end = match.end() + following.start() if following else len(text)
    return text[match.start():end].strip()


def replace_section(text: str, heading: str, body: str) -> str:
    pattern = r"(?ms)(^## " + re.escape(heading) + r"[ \t]*\n).*?(?=^## |\Z)"
    replaced, count = re.subn(pattern, lambda m: m.group(1) + "\n" + body.strip() + "\n\n", text)
    if count != 1:
        raise ValueError(f"Expected one section replacement: {heading}; got {count}")
    return replaced


def nest(text: str) -> str:
    # Formatting-only: each Record's internal holding heading is nested under its case.
    return re.sub(r"(?m)^(#{3,5}) ", lambda m: "#" + m.group(1) + " ", text)


def read_record(path: Path, name: str | None = None) -> dict:
    raw = path.read_text(encoding="utf-8-sig")
    marker = "## Public Projection\n"
    if marker not in raw:
        raise ValueError(f"Public Projection missing: {path.name}")
    public = raw.split(marker, 1)[1]
    headings = re.findall(r"(?m)^## (.+)$", public)
    if headings != BLOCKS:
        raise ValueError(f"Public blocks out of order in {path.name}: {headings}")
    fields = {key: section(public, key) for key in BLOCKS}
    if re.search(r"\b(?:AUTHOR|JOINERS|MAJORITY_JOINERS|ALL_OTHER)\b", public):
        raise ValueError(f"Unresolved public placeholder: {path.name}")
    if re.search(r"\*\*(?:Historical departure|Version / lineage|Final compatibility|Stone's Controlled)", public):
        raise ValueError(f"Internal material in public projection: {path.name}")
    result_match = re.search(r"(?m)^\*\*Result:\*\*\s*(.+)$", raw)
    case_match = re.search(r"(?m)^\*\*Case and dockets:\*\*\s*(.+)$", raw)
    date = re.search(r"_(\d{4}-\d{2}-\d{2})\.md$", path.name).group(1)
    title = name or (case_match.group(1).split(";")[0] if case_match else path.stem)
    # Only this named public-continuity field is selected from the internal kernel.
    continuation = section(raw.split(marker, 1)[0], "Continuity") if re.search(r"(?m)^## Continuity\s*$", raw.split(marker, 1)[0]) else ""
    return {"path": path, "name": title, "date": date, "result": result_match.group(1) if result_match else fields["Public Action"], "public": fields, "continuity": continuation, "sha256": digest(path.read_bytes())}


def authors_from_public(record: dict) -> set[str]:
    path = record["path"]
    if "_merits_" not in path.name or "_summary-merits_" in path.name:
        return set()
    topology = record["public"]["Opinion Topology"]
    authors: set[str] = set()
    for line in topology.splitlines():
        cells = [part.strip() for part in line.strip().strip("|").split("|")]
        if line.startswith("|") and len(cells) >= 3 and cells[0].startswith(("Opinion of the Court", "Opinion announcing the judgment", "Lead,", "Lead opinion")):
            author = cells[1].replace("Chief Justice ", "").replace("Justice ", "")
            if author not in JUSTICES:
                raise ValueError(f"Unrecognized lead author in {path.name}: {author}")
            authors.add(author)
    if not authors:
        match = re.search(r"(?:Chief Justice|Justice) (Stone-Zsela|Stevens|O'Connor|Scalia|Kennedy|Souter|Thomas|Ginsburg|Breyer) delivers the [Oo]pinion of the Court", topology)
        if match:
            authors.add(match.group(1))
        elif not re.search(r"[Pp]er curiam", topology):
            raise ValueError(f"Merits opinion form not recognized: {path.name}")
    return authors


def counts_section() -> tuple[str, dict]:
    events = []
    names = dict(EXPECTED)
    for path in (TERM / "records").glob("*.md"):
        if "_merits_" not in path.name or "_summary-merits_" in path.name:
            continue
        record = read_record(path, names.get(path.name))
        authors = authors_from_public(record)
        if authors:
            events.append((record, authors))
    events.sort(key=lambda item: (item[0]["date"], item[0]["name"].casefold()))
    by_author = {justice: [] for justice in JUSTICES}
    for record, authors in events:
        for author in authors:
            by_author[author].append(record)
    text = "### Counted lead opinions through chunk 3\n\nThis recount uses actual signed lead authors in the Records' public opinion tables or authorship statements. Per curiam opinions, summary dispositions, Fiore's certification and admitted sources do not count. Each Justice who delivers part of a signed lead is counted once for that opinion. Prior assignments stand as made.\n\n| Justice | Counted signed plenary leads | Counted decisions |\n|---|---:|---|\n"
    for justice, records in by_author.items():
        links = "; ".join(f"[{r['name']}](../records/{r['path'].name})" for r in records) or "None"
        text += f"| {justice} | {len(records)} | {links} |\n"
    last = events[-1][0]
    total = sum(len(rs) for rs in by_author.values())
    text += f"\nTotal counted signed leads by author: {total}. Last counted event: {last['name']}, {last['date']}.\n"
    return text, {justice: len(records) for justice, records in by_author.items()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    SCRATCH.mkdir(parents=True, exist_ok=True)
    baselines = {}
    for name in ["continuity.md", "neutral-projection.md"]:
        baseline = SCRATCH / (name + ".baseline")
        if not baseline.exists():
            baseline.write_bytes((WORK / name).read_bytes())
        baselines[name] = baseline.read_text(encoding="utf-8-sig")
    absent = [filename for filename, _ in EXPECTED if not (TERM / "records" / filename).exists()]
    if absent:
        print(json.dumps({"status": "waiting_for_records", "missing": absent, "workspace_written": False}, indent=2))
        return

    records = [read_record(TERM / "records" / filename, name) for filename, name in EXPECTED]
    dates = [r["date"] for r in records]
    assert dates == sorted(dates)
    count_text, counts = counts_section()
    event_rows, laws, positions, procedures = [], [], [], []
    for record in records:
        p = record["public"]
        link = f"[Record](../records/{record['path'].name})"
        heading = f"### {record['name']} — {record['date']}\n\n{link}"
        event_rows.append(f"| {record['date']} | [{record['name']}](../records/{record['path'].name}) | {record['result'].replace('|', '/')} |")
        # Source holdings and their authority/explanations are preserved, without
        # importing the neutral model, Stone input, assignment or audit annex.
        legal = heading + "\n\n#### Event, question and statutory setting\n\n" + nest(p["Event"])
        legal += "\n\n" + nest(p["Holdings"])
        legal += "\n\n#### Precedent treatment\n\n" + nest(p["Precedent Treatment"])
        legal += "\n\n#### Resulting law and limits\n\n" + nest(p["Law After Decision"])
        legal += "\n\n#### Source and record limits\n\n" + nest(p["Source Notes"])
        laws.append(legal)
        continuation = record["continuity"]
        first_position = re.search(r"(?m)^\*\*(?:Chief Justice|Justice) ", continuation)
        if first_position:
            material = continuation[first_position.start():].strip()
        elif re.search(r"(?i)\b(?:concurring|dissenting|concurrence|dissent)\b", p["Separate Writings"]) and not re.search(r"(?i)^(?:no |none)", p["Separate Writings"]):
            material = p["Separate Writings"]
        else:
            material = ""
        if material:
            if re.search(r"(?i)(?:private Stone|frozen (?:commitments?|handoffs?)|historical reconcili|provisional (?:votes?|commitments?)|approval status|Stone's (?:approved|controlled)|balance pool|assignment counts|standing fallback)", material):
                raise ValueError(f"Nonpublic marker in selected continuity: {record['path'].name}")
            positions.append(heading + "\n\n" + nest(material))
        procedures.append(f"**{record['name']} — {record['date']}.** {link}\n\n{p['Judgment & Remedy']}\n\n{p['Procedure After Action']}")

    scope = "36 Court events are completed: twelve events in each of chunks 1, 2 and 3. Three nonjudicial sources are admitted with their own effective provisions. The chronology cursor is March 6, 2000, after Portuondo v. Agard and United States v. Locke / Intertanko v. Locke. Uncoordinated same-day decisions share their entering-law baseline and operate together only prospectively. No institutional change is entered."
    next_group = "The next scheduled item is Adams v. Commissioner of Internal Revenue, March 6, 2000, in chunk 4. Its same-day entering-law baseline is the baseline before the uncoordinated March 6 decisions in chunk 3; those decisions do not govern Adams merely because its processing follows them. Existing assignments stand. Strout's granted Religion Clause merits questions are complete. Fiore remains pending after certification. Weeks's bounded sentencing-response remand remains in force. All fourteen opening carryovers retain their stated stages; Alaska is already among the 104 scheduled matters and the other thirteen are additional."
    summaries = {}
    preservation = {}
    for filename, baseline in baselines.items():
        text = baseline
        if filename == "continuity.md":
            text = text.replace("## Continuing open matters", "### Continuing open matters")
            keys = CONTINUITY_BLOCKS
            scope_key, events_key, law_key, pos_key, proc_key = keys[:5]
        else:
            keys = NEUTRAL_BLOCKS
            scope_key, events_key, law_key, pos_key, proc_key = keys
        old_law = section(text, law_key)
        old_positions = section(text, pos_key)
        original_pending = subsection(text, "Opening pending matters retained")
        old_scope = section(text, scope_key)
        old_scope = re.sub(r"24 Court events are completed:.*?(?=\n\n)", scope, old_scope, count=1, flags=re.S)
        old_scope = re.sub(r"The next scheduled eligible group is chunk 3.*?(?=\n\n|\Z)", next_group, old_scope, count=1, flags=re.S)
        if filename == "neutral-projection.md":
            old_scope = old_scope.replace(" Existing assignments stand.", "")
        text = replace_section(text, scope_key, old_scope)
        event_body = section(text, events_key)
        existing_rows = list(re.finditer(r"(?m)^\| \d{4}-\d{2}-\d{2} \|[^\n]*$", event_body))
        if len(existing_rows) != 27:
            raise ValueError(f"Expected 27 baseline event/source rows in {filename}")
        insert_at = existing_rows[-1].end()
        event_body = event_body[:insert_at] + "\n" + "\n".join(event_rows) + event_body[insert_at:]
        table_blocks = [block for block in event_body.split("\n\n") if "| Effective date | Event and authority | Result / source status |" in block]
        if len(table_blocks) != 1 or len(re.findall(r"(?m)^\| \d{4}-\d{2}-\d{2} \|", table_blocks[0])) != 39:
            raise ValueError(f"The completed-event table is not one valid 39-row table in {filename}")
        text = replace_section(text, events_key, event_body)
        text = replace_section(text, law_key, old_law + "\n\n" + "\n\n".join(laws))
        text = replace_section(text, pos_key, old_positions + "\n\n" + "\n\n".join(positions))
        proc = section(text, proc_key)
        proc = proc.replace("The chunk 1 procedural dispositions remain in force.", "The prior chunks' procedural dispositions remain in force.")
        proc = proc.replace("No covered interim-relief application has been decided in chunks 1 or 2.", "No covered interim-relief application has been decided in chunks 1 through 3.")
        proc = proc.replace("Paul P., Rayphand/Torres, Steamfitters, Fraternal Order of Police and Richards have reached", "Paul P., Rayphand/Torres, Steamfitters, Fraternal Order of Police, Richards and Strout have reached")
        proc, removed = re.subn(r"(?m)^\| 32 \| Strout v\. Albanese \| 2000-02-28 \| Granted — to be heard on the merits\. \|\n?", "", proc)
        if removed != 1:
            raise ValueError(f"Strout pending row not uniquely found in {filename}")
        proc = proc.replace("### Current-chunk procedures", "### Completed-event procedures through chunk 3")
        if filename == "continuity.md":
            old_count = subsection(proc, "Counted lead opinions after this chunk")
            proc = proc.replace(old_count, "\n\n".join(procedures) + "\n\n" + count_text.strip())
        else:
            proc += "\n\n" + "\n\n".join(procedures)
        same_day_note = "The March 6 group is incomplete until Adams receives its own disposition. Adams uses the common pre-March 6 legal baseline; neither chunk 3 decision supplies its entering law."
        if filename == "continuity.md":
            same_day_note += " A later processing step does not reopen the earlier assignments."
        proc = proc.replace("### Cross-chunk same-day groups\n", "### Cross-chunk same-day groups\n\n" + same_day_note + "\n")
        text = replace_section(text, proc_key, proc)
        if filename == "continuity.md":
            block = section(text, "Blockers and Revalidation Needs")
            block = block.replace("No unresolved chunk 2 adjudication blocker remains.", "No unresolved chunk 3 adjudication blocker remains. Each future event still requires its own chronology, source and position revalidation.")
            text = replace_section(text, "Blockers and Revalidation Needs", block)
            sources = section(text, "Source and Research Cutoff").replace("through 2000-02-14", "through 2000-03-06")
            text = replace_section(text, "Source and Research Cutoff", sources)
            text = text.replace("24 Court events and 3 admitted nonjudicial sources are covered", "36 Court events and 3 admitted nonjudicial sources are covered")
        else:
            text = text.replace("after 24 Court events and 3 admitted nonjudicial sources", "after 36 Court events and 3 admitted nonjudicial sources")
        assert old_law in text, f"Prior controlling law changed in {filename}"
        assert old_positions in text, f"Prior published positions changed in {filename}"
        assert subsection(text, "Opening pending matters retained") == original_pending, f"Opening carryovers changed in {filename}"
        assert re.findall(r"(?m)^## (.+)$", text) == keys, f"Unexpected projection blocks: {filename}"
        assert "| 32 | Strout v. Albanese" not in text
        assert "**Fiore remains open in this Court.**" in text
        for record in records:
            assert text.count(f"### {record['name']} — {record['date']}") >= 1
            assert nest(record["public"]["Holdings"]) in text
            assert nest(record["public"]["Event"]) in text
            assert record["public"]["Judgment & Remedy"] in text
            assert record["public"]["Procedure After Action"] in text
        if filename == "neutral-projection.md":
            assert "### Counted lead" not in text
            assert "## Stone" not in text and "**Historical departure:**" not in text
        text = text.rstrip() + "\n"
        (SCRATCH / (filename + ".draft")).write_text(text, encoding="utf-8", newline="\n")
        preservation[filename] = {"prior_law_exact": True, "prior_positions_exact": True, "opening_pending_block_exact": True, "blocks": keys, "bytes": len(text.encode("utf-8")), "sha256": digest(text.encode("utf-8"))}
        summaries[filename] = text

    if args.publish:
        for name in summaries:
            current_hash = digest((WORK / name).read_bytes())
            baseline_hash = digest((SCRATCH / (name + ".baseline")).read_bytes())
            if current_hash != baseline_hash:
                raise ValueError(f"Workspace changed after baseline capture; inspect before publication: {name}")
        for name, text in summaries.items():
            (WORK / name).write_text(text, encoding="utf-8", newline="\n")
    report = {"status": "published" if args.publish else "drafts_ready", "workspace_written": args.publish, "records": [{"file": r["path"].name, "sha256": r["sha256"]} for r in records], "counts": counts, "preservation": preservation}
    (SCRATCH / "validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
