"""Reconcile navigation only after independent Standards derivation is complete."""
from pathlib import Path
import hashlib
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[4]
WORK = Path(__file__).resolve().parent
INDEPENDENT = WORK / "STANDARDS_AND_TESTS.independent.md"
HOLDINGS = WORK.parent / "HOLDINGS.candidate.md"
EXPECTED_INDEPENDENT = "76deb93dea7342fbbeadcbd5e8a954b80c6dd474e1c7bd6af7df16db6736a3b7"
EXPECTED_HOLDINGS = "33ce239af3af5affb990907733700134557559cd4fb8e7afcd958fb1912f7a52"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def normalized(text):
    text = unicodedata.normalize("NFKC", text).casefold()
    return " ".join(re.sub(r"[^\w\s]", " ", text).split())


def question_key(text):
    text = re.sub(r"^(?:Holding\s+)?(?:[IVXLCDM]+(?:-[A-Z])?|\d+)(?:[.)]|\s*[—–-])?\s+", "", text)
    text = re.sub(r"^Part\s+[IVXLCDM]+(?:-[A-Z])?\s*[—–-]\s*", "", text)
    return normalized(text)


def slug_base(text):
    text = re.sub(r"<[^>]+>", "", text).lower()
    return "".join(c for c in text if c in "-_ " or unicodedata.category(c)[0] in "LMN").replace(" ", "-")


independent_bytes = INDEPENDENT.read_bytes()
holdings_bytes = HOLDINGS.read_bytes()
assert digest(independent_bytes) == EXPECTED_INDEPENDENT
assert digest(holdings_bytes) == EXPECTED_HOLDINGS
independent = independent_bytes.decode().replace("\r\n", "\n")
holdings = holdings_bytes.decode().replace("\r\n", "\n")
receipt = json.loads((WORK / "integration-receipt.json").read_text())
changed = set(receipt["changed_titles"]) | set(receipt["new_entry_titles"])
source_map = json.loads((WORK / "holdings-navigation-map.json").read_text())

# Only headings and their identifying case/date metadata are used from Holdings.
headings = []
used = set()
case = area = date = ""
for number, line in enumerate(holdings.splitlines(), 1):
    if line.startswith("**Decided:**"):
        date = line.split("**Decided:**", 1)[1].strip()
    match = re.match(r"^(#{1,6}) (.+)$", line)
    if not match:
        continue
    level, title = len(match[1]), match[2]
    base = slug_base(title)
    slug = base
    suffix = 0
    while slug in used:
        suffix += 1
        slug = f"{base}-{suffix}"
    used.add(slug)
    if level == 2:
        area = title
    if level == 4:
        case = title
        date = ""
    headings.append({"level": level, "title": title, "case": case, "area": area,
                     "line": number, "anchor": slug, "date": date})
questions = [h for h in headings if h["level"] == 5]
mapped_question_keys = {question_key(q) for cases in source_map.values() for case in cases for q in case["questions"]}
current_questions = [h for h in questions if question_key(h["title"]) in mapped_question_keys
                     and ("1999" in h["date"] or re.search(r"(?:October|November|December|1998-(?:10|11|12))", h["date"]))]

plan = []
for match in re.finditer(r"^### ([^\n]+)\n(.*?)(?=^##(?:#)? |\Z)", independent, re.M | re.S):
    title, body = match[1], match[2]
    if title not in changed:
        continue
    authority = re.search(r"\*\*Authority by component:\*\*(.*?)(?=\n\*\*|\Z)", body, re.S)[1]
    cited_records = re.findall(r"`([^`]+\.md)`", authority)
    authority_key = normalized(authority)
    matches = []
    for heading in current_questions:
        key = question_key(heading["title"])
        if len(key) >= 20 and key in authority_key:
            matches.append(heading)
    # Retain exact question matches, including headings named after a primary citation.
    # The source map is used only to show the available navigation for manual review.
    plan.append({"title": title, "authority": authority.strip(), "record_names": cited_records,
                 "start": match.start(), "end": match.end(),
                 "matches": matches,
                 "record_heading_options": {name: source_map.get(name, []) for name in cited_records}})

(WORK / "navigation-plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"changed_entries": len(plan), "matched_entries": sum(bool(p["matches"]) for p in plan),
                  "unmatched": [{"title": p["title"], "authority": p["authority"],
                                 "options": p["record_heading_options"]} for p in plan if not p["matches"]]},
                 ensure_ascii=False, indent=2))

assert len(plan) == 123
assert all(p["matches"] for p in plan), "Resolve missing navigation before placement"
insertions = []
for item in plan:
    block = independent[item["start"]:item["end"]]
    links = []
    for h in item["matches"]:
        label = f'{h["case"]} — {h["title"]}'
        assert not any(c in label for c in "[]"), label
        links.append(f'[{label}](HOLDINGS.md#{h["anchor"]})')
    navigation = "; ".join(links) + "."
    existing = re.search(r"^\*\*Holdings navigation:\*\*[^\n]*", block, re.M)
    if existing:
        offset = item["start"] + existing.end()
        addition = " " + navigation
    else:
        offset = item["start"] + len(block.rstrip("\n"))
        addition = "\n\n**Holdings navigation:** " + navigation
    insertions.append({"offset": offset, "text": addition, "title": item["title"]})

candidate = independent
for insertion in sorted(insertions, key=lambda row: row["offset"], reverse=True):
    n = insertion["offset"]
    candidate = candidate[:n] + insertion["text"] + candidate[n:]

# Validate the exact reverse operation, not merely a normalized substantive digest.
reconstructed = candidate
for insertion in sorted(insertions, key=lambda row: row["offset"]):
    n, addition = insertion["offset"], insertion["text"]
    assert reconstructed[n:n + len(addition)] == addition
    reconstructed = reconstructed[:n] + reconstructed[n + len(addition):]
assert reconstructed == independent
assert reconstructed.replace("\n", "\r\n").encode() == independent_bytes
candidate_bytes = candidate.replace("\n", "\r\n").encode()
new_links = re.findall(r"\]\((HOLDINGS\.md#[^)]+)\)", candidate)
for link in new_links:
    path, anchor = link.split("#", 1)
    assert path == "HOLDINGS.md" and anchor in used
assert len(new_links) == sum(len(item["matches"]) for item in plan)

target = WORK.parent / "STANDARDS_AND_TESTS.candidate.md"
target.write_bytes(candidate_bytes)
final_receipt = {
    "scope": "Navigation reconciliation and candidate placement only; no legal audit or rederivation.",
    "independent_sha256": EXPECTED_INDEPENDENT,
    "holdings_candidate_sha256": EXPECTED_HOLDINGS,
    "candidate_sha256": digest(candidate_bytes),
    "candidate_bytes": len(candidate_bytes),
    "publication_context": "state/STANDARDS_AND_TESTS.md; HOLDINGS.md resolves to the coordinated state/HOLDINGS.md publication.",
    "current_term_entries_reconciled": len(plan),
    "question_level_holdings_links": len(new_links),
    "existing_navigation_preserved": True,
    "all_changes_are_navigation_insertions": True,
    "removing_recorded_insertions_recovers_independent_bytes_exactly": True,
    "independent_file_unchanged": digest(INDEPENDENT.read_bytes()) == EXPECTED_INDEPENDENT,
    "holdings_file_unchanged": digest(HOLDINGS.read_bytes()) == EXPECTED_HOLDINGS,
    "planned_publication_links_and_anchors_resolve": True,
    "existing_external_links_unchanged": True,
    "publication_headers": receipt["headers"],
    "unresolved_navigation_issues": [],
    "navigation_map": "holdings-navigation-map.json reused only for current-term question identification; final destinations use completed Holdings heading anchors.",
    "prohibited_material_accessed": False,
    "git_commands_run": False,
}
(WORK / "navigation-insertions.json").write_text(json.dumps(insertions, ensure_ascii=False, indent=2) + "\n")
(WORK / "final-receipt.json").write_text(json.dumps(final_receipt, ensure_ascii=False, indent=2) + "\n")
(WORK / "NAVIGATION_RECONCILIATION.md").write_text(
    "# OT1998 Standards navigation reconciliation\n\n"
    "The independent legal substance was complete before Holdings was consulted. This step used only identifying headings and metadata to reconcile navigation. "
    "It added current-term question-level Holdings links to 123 new or changed entries, preserving every existing navigation reference. "
    "No rule, authority statement, coalition, qualification, date, heading or other preexisting text was changed.\n\n"
    "Removing the exact recorded insertions in `navigation-insertions.json` reconstructs the independent input byte for byte, including CRLF endings. "
    "The input and final Holdings hashes remain unchanged. `final-receipt.json` records hashes, counts and verification.\n\n"
    "Links are resolved from the intended publication location `state/STANDARDS_AND_TESTS.md`, with `HOLDINGS.md` supplied by the coordinated final Holdings candidate. "
    "All added fragments resolve to actual question headings, including duplicate-heading suffixes. Existing plain-text natural-authority references and the existing external link remain unchanged. "
    "There are no unresolved navigation issues.\n\n"
    "This is candidate preparation only. No legal audit, rederivation, adjudication change, state publication or Git operation was performed. "
    "No prohibited private directory or master file was read or listed.\n"
)
print(json.dumps(final_receipt, ensure_ascii=False, indent=2))
