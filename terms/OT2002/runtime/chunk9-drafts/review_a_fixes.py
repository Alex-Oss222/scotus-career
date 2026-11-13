from pathlib import Path
import json
import re

ROOT = Path(__file__).parent
FIXES = {
    'Massaro-v-United-States_merits_2003-04-23.md': [
        (
            'Signed lead opinion following plenary merits review. Form and substantive parts were fixed before assignment; the same eligible Associate can carry every portion where the Chief joins only part.',
            'Signed lead opinion following plenary merits review. Form and substantive parts were fixed before assignment.',
            1,
        ),
        (
            'The district court must determine deficient performance and a reasonable probability of a different lawful result under Strickland. After notice to the United States it must grant a prompt hearing unless the motion and existing files and records conclusively show that the prisoner is entitled to no relief; necessary hearing proceedings require findings and legal conclusions, and relief follows only from the established statutory and constitutional grounds.',
            'The district court must apply Strickland\'s deficient-performance and reasonable-probability prejudice requirements. Unless the motion and existing files and records conclusively show that the prisoner is entitled to no relief, it must grant a prompt hearing after notice to the United States and make findings and legal conclusions resolving the necessary issues; relief follows only from the established statutory and constitutional grounds.',
            2,
        ),
        (
            ' There is no collateral release or new-trial event to add to continuity at this stage.',
            '',
            1,
        ),
        (
            'continued custody must rest on a lawful judgment.',
            'continued custody must rest on an identified lawful basis.',
            1,
        ),
    ],
    'City-of-New-York-v-Patrolmens-Benevolent-Association_merits_2003-04-23.md': [
        (
            ' This disposition applies those limits to the actual civil trial rather than creating a universal civil plain-error formula.',
            '',
            1,
        ),
    ],
    'United-States-v-Handakas_merits_2003-04-23.md': [
        (
            'Lanier is applied to conduct-time warning without treating its section 242 holding as a definition of section 1346.',
            'Lanier is applied to conduct-time warning.',
            2,
        ),
        (
            'The pending work is adjudication of actual appellate grounds, not a general opportunity to reconstruct the prosecution.',
            'The remand requires adjudication of the actual remaining appellate grounds.',
            2,
        ),
        (
            'Olano supplies a separate discretionary reason for correcting this concrete continuing duplication; Rutledge\'s different preserved-assessment setting creates no preservation exemption here.',
            'Olano supplies a separate discretionary reason for correcting this concrete continuing duplication.',
            2,
        ),
    ],
    'Price-v-Vincent_merits_2003-05-19.md': [
        (
            'Because that requirement is unsatisfied, the Court resolves entitlement to this writ without a separate de novo ruling on the constitutional permissibility of analogous reconsideration on direct review.',
            'Failure of that statutory requirement resolves entitlement to this writ.',
            2,
        ),
        (
            ' The distinct direct-review constitutional inquiry is not reached because failure of the statutory gateway is sufficient to resolve the requested collateral relief.',
            '',
            1,
        ),
        (
            ' The full constitutional inquiry on direct review is outside the collateral question resolved by the statutory gateway.',
            ' The statutory ruling resolves this collateral claim; the draft does not list neighboring direct-review questions as reservations.',
            1,
        ),
    ],
}

results = []
expected_blocks = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes']
for filename, fixes in FIXES.items():
    path = ROOT / filename
    before = path.read_text(encoding='utf-8')
    frozen_before = before.split('## Frozen reconciliation and commitment audit\n', 1)[1].split('## Public Projection\n', 1)[0]
    text = before
    for old, new, count in fixes:
        assert text.count(old) == count, (filename, old, text.count(old), count)
        text = text.replace(old, new)
    frozen_after = text.split('## Frozen reconciliation and commitment audit\n', 1)[1].split('## Public Projection\n', 1)[0]
    assert frozen_before == frozen_after
    internal = text.split('## Controlling holdings\n', 1)[1].split('## Published noncontrolling positions\n', 1)[0].strip()
    public = text.split('## Public Projection\n', 1)[1]
    holdings = public.split('## Holdings\n', 1)[1].split('## Precedent Treatment\n', 1)[0].strip()
    assert internal == holdings
    blocks = re.findall(r'^## (.+)$', public, re.M)
    assert blocks == expected_blocks, (filename, blocks)
    explanations = re.findall(r'\*\*Controlling explanation:\*\* (.*?)(?=\n\*\*Precedent treatment:)', internal, re.S)
    counts = [len(re.findall(r'\S+', body)) for body in explanations]
    assert explanations and all(n <= 350 for n in counts), (filename, counts)
    assert text.count('__ASSIGNMENT_BLOCK__') == 1
    assert '__LEAD_AUTHOR__' in text and '__LEAD_JOINERS__' in text
    assert all(text.splitlines()[i].startswith(label) for i, label in enumerate(['**Case and dockets:**', '**Event and date:**', '**Result:**', '**Version / lineage:**']))
    path.write_text(text, encoding='utf-8')
    results.append({'file': filename, 'fixes': len(fixes), 'explanation_words': counts, 'eleven_blocks': True, 'holdings_identity': True, 'frozen_appendix_unchanged': True, 'assignment_placeholders_retained': True})
print(json.dumps(results, indent=2))
