from pathlib import Path
import hashlib
import json
import re

root = Path('terms/OT1998')
record = root / 'records/college_savings_bank_v_florida_prepaid_merits_1999-06-23.md'
validation = root / 'freeze/OT_1998CHUNK11_COLLEGE_SAVINGS_ASSEMBLY_VALIDATION.json'
recount_path = root / 'freeze/OT_1998CHUNK11_COLLEGE_SAVINGS_RECOUNT.json'
text = record.read_text()
internal, public = text.split('## Public Projection\n', 1)
checks = {}
labels = ['**Case and dockets:**', '**Event and date:**', '**Result:**', '**Version / lineage:**']
checks['exact_four_opening_labels'] = all(line.startswith(prefix) for line, prefix in zip(text.splitlines()[:4], labels))
checks['natural_key_and_event_date'] = record.name == 'college_savings_bank_v_florida_prepaid_merits_1999-06-23.md' and '1999-06-23' in text.splitlines()[1]
blocks = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes']
checks['exact_eleven_terminal_public_blocks'] = re.findall(r'^## (.+)$', public, re.M) == blocks and text.count('## Public Projection\n') == 1
checks['internal_continuity_block'] = '## Material Published Noncontrolling Positions\n' in internal
checks['counted_marker_exact'] = text.count('**Counted lead opinion:** Yes') == 1
checks['public_private_boundary'] = not re.search(r'\b(?:approved|approval|reconciliation|recount|workflow|SHA256|2026|simulated|user-directed|delegated|freeze/|runtime/)\b', public, re.I)
checks['public_has_no_hash'] = not re.search(r'\b[0-9a-f]{64}\b', public)
checks['no_unverified_direct_quotation'] = '“' not in public and '”' not in public
for target in re.findall(r'\]\(([^)]+)\)', text):
    if '://' not in target:
        p = (record.parent / target.split('#')[0]).resolve()
        assert p == validation.resolve() or p.exists(), str(p)
checks['local_links_resolve'] = True

roster = ['Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']
votes = {
    'reverse_remand': ['Stone-Zsela', 'Stevens', 'Souter', 'Ginsburg', 'Breyer'],
    'affirm': ["O'Connor", 'Scalia', 'Kennedy', 'Thomas'],
    'statutory_authorization': roster,
    'reject_presented_section_5': ['Stone-Zsela', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer'],
    'reject_constructive_commercial_consent': ['Stone-Zsela', "O'Connor", 'Scalia', 'Kennedy', 'Thomas'],
    'article_i_and_fair_inclusion': ['Stone-Zsela'],
    'prospective_commercial_condition': ['Stevens', 'Souter', 'Ginsburg', 'Breyer'],
    'affirmative_section_5': ['Stevens'],
}
for names in votes.values():
    assert len(names) == len(set(names)) and set(names) <= set(roster)
for a, b in [('reverse_remand', 'affirm'), ('reject_presented_section_5', 'affirmative_section_5'), ('reject_constructive_commercial_consent', 'prospective_commercial_condition')]:
    assert set(votes[a]) | set(votes[b]) == set(roster)
    assert not set(votes[a]) & set(votes[b])
checks['all_nine_component_arithmetic'] = True
joins = {
    'lead_part_i': roster,
    'lead_part_ii': votes['reject_presented_section_5'],
    'lead_part_iii': votes['reject_constructive_commercial_consent'],
    'lead_part_iv': votes['article_i_and_fair_inclusion'],
    'lead_part_v_judgment_only': votes['reverse_remand'],
    'breyer_concurrence': ['Breyer', 'Stevens', 'Souter', 'Ginsburg'],
    'stevens_further_concurrence': ['Stevens'],
    'oconnor_dissent': ["O'Connor", 'Scalia', 'Kennedy', 'Thomas'],
}
expected = [
    ('Opinion of the Court, Part I', 'Stone-Zsela', 'lead_part_i'),
    ('Opinion of the Court, Part II', 'Stone-Zsela', 'lead_part_ii'),
    ('Opinion of the Court, Part III', 'Stone-Zsela', 'lead_part_iii'),
    ('Opinion announcing the judgment, Part IV', 'Stone-Zsela', 'lead_part_iv'),
    ('Opinion announcing the judgment, Part V', 'Stone-Zsela', 'lead_part_v_judgment_only'),
    ('Concurrence in part and in the judgment', 'Breyer', 'breyer_concurrence'),
    ('Further concurrence in part and in the judgment', 'Stevens', 'stevens_further_concurrence'),
    ('Dissent', "O'Connor", 'oconnor_dissent'),
]
for section in [internal, public]:
    for title, author, key in expected:
        row = next([c.strip() for c in line.split('|')[1:-1]] for line in section.splitlines() if line.startswith('| ' + title + ' |'))
        assert row[1] == author
        actual = {author} | {j for j in roster if j in row[2]}
        assert actual == set(joins[key]), (title, actual, joins[key])
checks['internal_and_public_exact_opinion_joins'] = True
lead_authors = set()
for line in text.splitlines():
    if line.startswith('|'):
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if len(cells) > 1 and re.match(r'(?:Opinion of the Court|Lead opinion|Opinion announcing the judgment)\b', cells[0], re.I):
            lead_authors.add(cells[1])
checks['recognized_lead_rows_one_counted_author'] = lead_authors == {'Stone-Zsela'}

recount = json.loads(recount_path.read_text())
counts = {'Stone-Zsela': 12, 'Stevens': 12, "O'Connor": 14, 'Scalia': 12, 'Kennedy': 14, 'Souter': 13, 'Thomas': 12, 'Ginsburg': 13, 'Breyer': 13}
checks['fresh_recount_identity_and_arithmetic'] = (recount['before_date'] == '1999-06-23' and recount['before_caption'] == 'College Savings Bank v. Florida Prepaid Postsecondary Education Expense Board' and recount['counts'] == counts and sum(counts.values()) == recount['counted_opinions'] == 115 and recount['last_counted'] == 'alden_v_maine_merits_1999-06-23.md')
last = recount['sources'][-1]
checks['preceding_alden_author_evidence_identity'] = last['source_sha256'] == '4c1ba430478debc5dbed6db5fffff78196f1bc4f5e016e51e350138bea5bb939' and last['authors'] == ['Souter']
checks['all_nine_assignment_counts_in_record'] = all(f'| {j} | {c} |' in internal for j, c in counts.items())
checks['assignment_authority_eligibility_pool_and_choice_explicit'] = all(s in internal for s in ['**Assigning Justice:** Chief Justice Stone-Zsela.', '**Eligible authors for the entire lead:** Stone-Zsela only.', '**Balance pool:** Stone-Zsela only', '**Chosen author:** Stone-Zsela.'])
holdings = public.split('## Holdings\n', 1)[1].split('## Precedent Treatment\n', 1)[0]
explanation_words = [len(re.findall(r'\S+', p.split('\n### ', 1)[0])) for p in re.split(r'\*\*Controlling explanation:\*\*', holdings)[1:]]
checks['controlling_explanations_within_350_words'] = len(explanation_words) == 3 and max(explanation_words) <= 350

reconciled_path = root / 'freeze/OT_1998CHUNK11_COLLEGE_SAVINGS_RECONCILED.md'
assert hashlib.sha256(reconciled_path.read_bytes()).hexdigest() == 'a7f439d21755c2b2a89f77a8beea6d99d249a645b9be2e38fa31c7cf97748225'
prep_path = root / 'freeze/OT_1998CHUNK11_COLLEGE_SAVINGS_ASSEMBLY_LEGAL_PREPARATION.md'
assert hashlib.sha256(prep_path.read_bytes()).hexdigest() == '4fe621cbbd81d958f3d6a7e608e3ec6e471095a87013a7bd1b3af0add0705e7f'
source_hashes = {}
for relative, expected_hash in re.findall(r'\| `([^`]+)` \| `([0-9a-f]{64})` \|', reconciled_path.read_text()):
    if relative.startswith('entering-law/') or relative in {'freeze/OT_1998CHUNK11_COLLEGE_SAVINGS_NEUTRAL.md', 'freeze/OT_1998CHUNK11_COLLEGE_SAVINGS_COMMITMENTS.md', 'freeze/OT_1998CHUNK11_IP_UNION_GAS_WELCH_HILTON_ADDENDUM.md', 'freeze/OT_1998CHUNK11_JUNE23_FINAL_NEUTRAL_SCREEN.md'}:
        p = root / relative
        actual = hashlib.sha256(p.read_bytes()).hexdigest()
        assert actual == expected_hash, (relative, actual)
        source_hashes[str(p)] = actual
for p in [reconciled_path, prep_path, root / 'runtime/chunk11-scoped/COLLEGE_SAVINGS_STONE.md', recount_path, Path('AGENTS.md'), Path('foundation/ENGINE.md'), Path('foundation/RENDER_CONTRACT.md'), Path('foundation/COURT_COMPOSITION.md')]:
    source_hashes[str(p)] = hashlib.sha256(p.read_bytes()).hexdigest()
checks['immutable_authorized_source_hashes_match'] = True
checks['category_prevention_and_existing_property_preserved'] = all(s in public for s in ['conduct that is not independently unconstitutional', 'absence of a completed violation in each plaintiff', 'established business assets, goodwill and legal claims'])
checks['hilton_and_actual_consent_preserved'] = "Hilton's independently retained FELA coverage" in public and 'Genuine voluntary waiver' in public
checks['no_invented_majority_amenability'] = 'No Associate joins Part IV' in public and 'participating majority expressly rejects' in public
checks['stone_revalidation_and_eight_departures_present'] = all(s in internal for s in ['## Stone fixed core, revalidation and delegated choices', 'No standing fallback is used.', 'delegated, not as propositions personally and specifically approved', '## Frozen-commitment compatibility and historical reconciliation']) and internal.count('**Historical departure:**') == 8
assert all(checks.values()), [k for k, value in checks.items() if not value]

data = {
    'status': 'passed',
    'record': str(record),
    'record_sha256': hashlib.sha256(record.read_bytes()).hexdigest(),
    'event_date': '1999-06-23',
    'caption': 'College Savings Bank v. Florida Prepaid Postsecondary Education Expense Board',
    'scope': 'College Savings final assembly only. No broad audit, workspace update or Render Input generation.',
    'stage_order': {'legal_preparation_before_counts': True, 'alden_final_signal_received': True, 'fresh_recount_after_signal': True, 'no_june23_peer_substantive_law_used': True},
    'component_votes': {key: {'count': len(names), 'justices': names} for key, names in votes.items()},
    'opinion_joins': joins,
    'opinion_authors': {'lead_parts_i_through_v': 'Stone-Zsela', 'commercial_consent_concurrence': 'Breyer', 'further_section_5_concurrence': 'Stevens', 'dissent': "O'Connor"},
    'assignment': {'assigning_justice': 'Stone-Zsela', 'counts_before_assignment': counts, 'last_event_counted': 'Alden v. Maine, merits, 1999-06-23', 'last_record_counted': recount['last_counted'], 'eligible_authors': ['Stone-Zsela'], 'balance_pool': ['Stone-Zsela'], 'chosen_author': 'Stone-Zsela', 'counted_authors': ['Stone-Zsela'], 'reason': 'Only reversal-coalition member supporting every actual lead proposition, including adverse majority portions and affirmative Article I route. Mandatory sole-pool assignment; one author can carry every part, so no division merely for balance.'},
    'stone_revalidation': {'fixed_core_preserved': True, 'standing_fallback_used': False, 'delegated_choices': ['Fair inclusion of Article I argument supporting preserved federal immunity/abrogation claim', 'Federal-question/diversity account for interstate plaintiff'], 'delegation_status': 'Prospective user delegation, not personally and specifically approved propositions in the original supplement.', 'non_stone_commitments_changed': False},
    'legal_review': {'section_5': 'Eight negative joins; Stevens alone preserves affirmative category prevention. No individual-violation or formal-findings prerequisite.', 'consent': 'Five reject commercial consent; four preserve prospective-condition concurrence; Hilton state-court FELA coverage remains.', 'marks': 'No controlling affirmative rationale; commercial-consent rule expressly rejected by five, sole Article I and affirmative section 5 grounds noncontrolling.', 'scope': 'Stone alone adopts fair inclusion under delegated completion; four dissenters retain nonreach and four consent proponents do not activate constitutional alternatives.', 'remedy': 'Ordinary federal Lanham merits remand only; no award, evidence proceeding, revived common-law claim, counterclaim or patent disposition.'},
    'checks': checks,
    'controlling_explanation_word_counts': explanation_words,
    'source_hashes': source_hashes,
    'unresolved_material_discrepancies': [],
    'integration_boundary': 'Final canonical Record is available for parent sequencing. Parent owns workspace, projection integration and later render generation. No further assembly audit pending.',
}
validation.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'status': 'passed', 'checks': len(checks), 'record': str(record), 'record_sha256': data['record_sha256'], 'validation': str(validation), 'validation_sha256': hashlib.sha256(validation.read_bytes()).hexdigest(), 'lead_author': 'Stone-Zsela', 'explanation_words': explanation_words}, ensure_ascii=False))
