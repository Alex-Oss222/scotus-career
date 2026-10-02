"""Insert root-reviewed C chronology/count/status text without changing public bytes."""
from pathlib import Path
import json
import re
import sys

term = Path(__file__).resolve().parents[1]
name = sys.argv[1]
cases = {
    'A_St_P_C_v_B_C_merits_1995-11-20.md': ('Stone-Zsela', 7),
    'Field_v_Mans_merits_1995-11-28.md': ('Souter', 8),
    'NLRB_v_Town_and_Country_Electric_Inc_merits_1995-11-28.md': ('Ginsburg', 8),
    'Thompson_v_Keohane_merits_1995-11-29.md': ("O'Connor", 10),
}
assert name in cases
author, prior_total = cases[name]
receipts = ['C_FINAL_B_ACTUAL_LAW_REFRESH.md']
counts = {"O'Connor": 3, 'Ginsburg': 1, 'Scalia': 1, 'Souter': 1, 'Kennedy': 1}
if prior_total >= 8:
    assert (term / 'records/A_St_P_C_v_B_C_merits_1995-11-20.md').exists()
    receipts.append('C_NOV20_ACTUAL_LAW_REFRESH.md')
    counts['Stone-Zsela'] = 1
if prior_total >= 10:
    for earlier in ['Field_v_Mans_merits_1995-11-28.md', 'NLRB_v_Town_and_Country_Electric_Inc_merits_1995-11-28.md']:
        assert (term / 'records' / earlier).exists()
    receipts.append('C_NOV28_ACTUAL_LAW_REFRESH.md')
    counts['Ginsburg'] = 2
    counts['Souter'] = 2
assert sum(counts.values()) == prior_total
for receipt in receipts:
    assert (term / 'freeze' / receipt).is_file(), receipt
assert (term / 'records/American_Life_League_v_Reno_merits_1995-11-13.md').is_file()

path = term / 'runtime/assembly' / name
private, public = path.read_text(encoding='utf-8').split('## Public Projection', 1)
public_copy = path.with_name('PUBLIC_DRAFT_' + name).read_text(encoding='utf-8').strip() + '\n'
assert public.strip() + '\n' == public_copy
private = re.sub(
    r'(?m)^The baseline is the coordinated OT1994 closing law.*$',
    'The coordinated OT1994 closing law through June 29, 1995 is supplemented by the actual earlier effective Records. '
    'Each later event has been checked against its actual date-specific public law before preservation. '
    'The two November 28 matters share a common entering-law baseline; file order does not create a dependency. '
    'A material changed legal premise would require a scoped refresh rather than an assembly vote inference.', private)
private = private.replace(
    "Later-preserved B law still requires the root's final effective-date check; no substantive non-Stone refresh is triggered by the three reviewed A decisions.",
    'The completed B-law and applicable earlier C-law checks below are cumulative with this A-law review.')
count_text = '; '.join(f'{justice} {count}' for justice, count in counts.items())
assignment = (
    'The preceding-term review records 94 named Chief assignments, with no author above one half; the consecutive-term ceiling is inactive. '
    f'The actual Records on strictly earlier dates establish {prior_total} Chief assignments: {count_text}. '
    f'This opinion is assigned to {author}. The separate American Life League RFRA opinion was assigned by O\'Connor and is excluded from that Chief count. '
    'The November 28 cohort adds Field/Souter and Town/Ginsburg as separate opinions without making either same-day decision entering law for the other. '
    'These counts confirm the recorded assignment baseline; they do not replace the case-specific fit analysis.')
private = re.sub(r'(?m)^The preceding-term assignment review reports.*$', lambda _: assignment, private)

refs = ', '.join('freeze/' + r for r in receipts)
law = (
    '**Final actual-law refresh:** ' + refs + ' record the completed prospective checks. '
    'Strumpf supplies only the specified bankruptcy-payment/stay and ordinary-remand rules; Louisiana supplies the original boundary and bounded implementation rules. '
    'Libretti distinguishes criminal forfeiture, actual waiver and statutory authority without a universal proof, classification or no-remand rule. '
    'American Life League preserves its distinct commerce, conduct-speech, damages-attribution and RFRA applications; its exclusive-own-minor exception creates no constitutional parental veto or general proof standard. '
    'These actual holdings change no frozen C ground or join. '
)
if prior_total >= 8:
    law += 'The actual A. St. P. C. heightened-proof rule concerns the severe statutory all-contact trigger, not ordinary fraud reliance, NLRA employee status or Miranda-custody review; its protective and restoration limits remain intact. '
if prior_total >= 10:
    law += 'Actual Field distinguishes the reliance rule from its disputed application and debt nexus; actual Town permits compatible dual service within the NLRA. Neither alters Thompson\'s pre-AEDPA classification, historical-fact treatment or reserved remedy. '
private = re.sub(r'(?m)^\*\*Status:\*\*.*$', lambda _: (
    law + '\n\n**Status:** Initial Canonical Decision Record authorized for durable preservation after root Stone-compatibility, actual-law and assignment review. '
    'C_PUBLIC_DRAFT_COMPATIBILITY_AUDIT.md and its final checks, the C assembly clerical audit and the dated refresh receipts identify the reviewed public bytes. '
    'Only private completion text and navigation metadata were finalized after that public review; the Public Projection remains unchanged. '
    'Git verification and commitment remain with the operator; repository projection checks are reported in the chunk validation. No public render is produced.'), private)
path.write_text(private + '## Public Projection' + public, encoding='utf-8')
assert path.read_text(encoding='utf-8').split('## Public Projection', 1)[1].strip() + '\n' == public_copy
meta_path = path.with_suffix('.json')
meta = json.loads(meta_path.read_text(encoding='utf-8'))
meta['status'] = 'reviewed for initial preservation; canonical copy gate required'
meta['assignment']['count_pending_root'] = False
meta['assignment']['chief_assignment'] = True
meta['assignment']['current_prior_chief_counts'] = counts
meta['final_root_refresh_reference'] = refs
meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(name + ': private completion finalized; audited public text unchanged.')
