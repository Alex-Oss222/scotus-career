from pathlib import Path
import re
import sys
import hashlib
import subprocess

sys.path.insert(0, 'tools')
from build_entering_law import take_heading

base = Path('terms/OT2003')
law = base / 'entering-law/OT_2003CHUNK2_MCCONNELL_POWER.md'
subprocess.run([
    sys.executable, '-B', 'tools/build_entering_law.py', str(law),
    '--standard-heading', 'Concrete personal interests and procedural citizen-suit standing',
    '--standard-heading', 'Compulsory state regulation or ownership of private obligations',
    '--standard-heading', 'Temporary state-executive records assistance under federal direction',
    '--standard-heading', 'Exclusive congressional qualifications and ballot restrictions',
], check=True)
parts = [law.read_text(encoding='utf-8').rstrip()]
copies = []

def append_heading(path, heading):
    text = take_heading(Path(path).read_text(encoding='utf-8'), heading)
    parts.append('\n## Exact authority selection\n\nSource: `' + path + '`; heading: ' + heading + '.\n\n' + text)
    copies.append((path, heading, text))

for heading in [
    'United States v. Lopez',
    'Printz v. United States; Mack v. United States',
    'Pierce County v. Guillen, 537 U.S. 129',
    'U.S. Term Limits, Inc. v. Thornton / Bryant v. Hill',
    "Whether Congress may require a State to regulate private waste or assume ownership, possession and liability, and whether state officials' consent cures the command",
]:
    append_heading('state/holdings/constitutional-structure.md', heading)
append_heading('state/holdings/federal-courts-justiciability.md', 'Printz v. United States; Mack v. United States')
append_heading('state/holdings/election-law.md', 'Whether congressional ballots may penalize refusal of a state-selected legislative position')

public = [
    ('terms/OT1995/output/OT_1995CHUNK4.md', 'Voting Rights Coalition', [
        'Opinion and Authority',
        'Congress may require the challenged congressional-election registration duties',
        'Presidential registration rests on a separate constitutional basis',
        'Registration procedure is distinct from substantive voter qualifications',
        'The injunction has an independent public-enforcement foundation',
    ]),
    ('terms/OT1999/output/OT_1999CHUNK2.md', 'Reno v. Condon', [
        'Opinion Topology',
        'Congress may regulate this information-distribution market',
        'Direct regulation of state disclosure is not compelled government of others',
    ]),
    ('terms/OT1996/output/OT_1996CHUNK13.md', 'Printz v.', [
        'Opinion Topology', 'Separate Positions Relevant to the Decision',
    ]),
    ('terms/OT1994/output/OT_1994CHUNK6.md', 'U.S. Term Limits', [
        'Opinion Topology', 'Separate Positions Relevant to the Decision',
    ]),
    ('terms/OT2000/output/OT_2000CHUNK3.md', 'Cook v. Gralike', [
        'Opinion Topology', 'Separate Writings',
    ]),
    ('terms/OT1994/output/OT_1994CHUNK5.md', 'United States v. Lopez', [
        'Opinion Topology', 'Separate Positions Relevant to the Decision',
    ]),
]
for path, case, headings in public:
    entry = take_heading(Path(path).read_text(encoding='utf-8'), case)
    for heading in headings:
        text = take_heading(entry, heading)
        parts.append('\n## Exact earlier public selection\n\nSource: `' + path + '`; entry: ' + case + '; heading: ' + heading + '.\n\n' + text)
        copies.append((path, case + ' / ' + heading, text))

snapshot_path = base / 'freeze/OT_2003CHUNK2_POWER_CURRENT_PUBLIC.md'
snapshot = snapshot_path.read_text(encoding='utf-8')
start = snapshot.index('# Completed public event effective 2003-10-30')
holston = snapshot[start:].strip()
parts.append('\n## Exact effective current-term public authority\n\nSource: `' + snapshot_path.as_posix() + '`.\n\n' + holston)
copies.append((snapshot_path.as_posix(), 'Holston public event', holston))
parts.insert(1, '\n## Scope and temporal boundary\n\nTargeted supplement for McConnell, December 10, 2003: Article I power, Elections Clause, federalism and the distinct private-party Tenth Amendment question. The term-opening entries are effective through June 30, 2003; Holston is effective October 30, 2003. These exact copies supplement the validated C reading slice. They do not import the historical versions of post-1991 decisions quoted by the litigants or lower judges. The earlier public selections establish the published grounds and joins actually adopted, not a vote in the pending case. The roster remains the nine Justices in the authorized current public snapshot. No commitment is made.')
law.write_text('\n\n'.join(parts).rstrip() + '\n', encoding='utf-8')

srcbase = base / 'sources/mcconnell'
source_parts = ['# McConnell power and federalism: exact predecision source selections\n\nSource quotations are copied by script from saved primary texts. Briefs remain advocacy; each lower judge speaks only for the identified scope. Historical descriptions of post-1991 Supreme Court doctrine are not current law. Source cutoff: December 10, 2003. Character offsets identify the saved extraction, not report pagination. No original-document absence is inferred.']
source_copies = []

def excerpt(name, label, a, b):
    assert 0 <= a < b, (name, label, a, b)
    text = (srcbase / name).read_text(encoding='utf-8')
    selection = text[a:b]
    source_parts.append('\n## ' + label + '\n\nSource: `' + name + '`, character offsets [' + str(a) + ', ' + str(b) + ').\n\n' + selection)
    source_copies.append((name, a, b, selection))

s = (srcbase / '10.-Appellants-Brief.txt').read_text(encoding='utf-8')
excerpt('10.-Appellants-Brief.txt', 'McConnell Question 1', s.index('1. Whether'), s.index('2. Whether'))
a = s.rfind('\nB.', 0, 75989)
b = s.index('\nC.', a + 3)
excerpt('10.-Appellants-Brief.txt', 'McConnell merits Part I.B, pages 26-35', a, b)
a = s.index('Section 318 also violates')
b = s.index('district', a)
b = s.index('affirmed.', b) + len('affirmed.')
excerpt('10.-Appellants-Brief.txt', 'McConnell minor-contribution federalism alternative', a, b)

s = (srcbase / '14.-Appellants-Brief.txt').read_text(encoding='utf-8')
a = s.index('QUESTIONS PRESENTED'); b = s.index('2.', a)
excerpt('14.-Appellants-Brief.txt', 'Political-party Question 1', a, b)
a = s.index('Il. NEW SECTION 323')
b = s.index('fll. NEW SECTION 323', 190000)
excerpt('14.-Appellants-Brief.txt', 'Political-party power and federalism argument, pages 78-90', a, b)

s = (srcbase / '19.-Appellants-Brief.txt').read_text(encoding='utf-8')
a = s.rfind('\nC.', 0, 155166); b = s.index('\nD.', a + 3)
excerpt('19.-Appellants-Brief.txt', 'United States/FEC power and federalism response, pages 65-69', a, b)

s = (srcbase / 'district-251-FSupp2d-176.txt').read_text(encoding='utf-8')
a = s.rfind('\nD. ', 0, 1759888); b = s.index('\nE. Conclusion', a)
excerpt('district-251-FSupp2d-176.txt', 'Kollar-Kotelly Part II.D, 251 F. Supp. 2d 712-716', a, b)
a = s.rfind('\n.', 0, 2586584)
b = s.index('\n. This reason necessarily', a)
excerpt('district-251-FSupp2d-176.txt', 'Kollar-Kotelly associated footnotes: prudential standing and State representation', a, b)
a = s.rfind('\n.', 0, 2475247); b = s.index('\n.', 2475247)
excerpt('district-251-FSupp2d-176.txt', 'Henderson Part IV.D.4 footnote: Section 323(e) power ruling', a, b)
a = s.rfind('\n.', 0, 2642874); b = s.index('\n.', 2642874)
excerpt('district-251-FSupp2d-176.txt', 'Leon Part I.B.2 footnote: Section 301(20)(A)(iii) power ruling', a, b)
a = s.rfind('\n1. ', 0, 1958662); b = s.index('\nThe Supreme Court', a)
excerpt('district-251-FSupp2d-176.txt', 'Leon reserves power objections to other activity categories while resolving First Amendment', a, b)

s = (srcbase / 'tennessee-electric-306-118.txt').read_text(encoding='utf-8')
footer = s.find('\nCC')
if footer != -1:
    s = s[:footer].rstrip() + '\n'
    (srcbase / 'tennessee-electric-306-118.txt').write_text(s, encoding='utf-8')
source_parts.append('\n## Tennessee Electric primary-source provenance\n\nTennessee Electric Power Co. v. Tennessee Valley Authority, 306 U.S. 118 (1939), full opinion and footnotes saved as `tennessee-electric-306-118.txt` from https://www.law.cornell.edu/supremecourt/text/306/118. The text reproduces the Court opinion and Butler dissent. Counsel argument is expressly omitted by that source. The passage below preserves the majority\'s actual competition and state-rights context; it does not turn its phrasing into a new categorical holding for directly regulated parties.')
a = s.index('A distinct ground upon which standing'); b = s.index('Finally, it is asserted', a)
excerpt('tennessee-electric-306-118.txt', 'Tennessee Electric majority paragraph 15 in context', a, b)

out = srcbase / 'power-federalism-selected-exact.md'
out.write_text('\n\n'.join(source_parts) + '\n', encoding='utf-8')
for path, heading, selection in copies:
    original = Path(path).read_text(encoding='utf-8')
    assert selection in original, (path, heading)
    assert selection in law.read_text(encoding='utf-8')
for name, a, b, selection in source_copies:
    original = (srcbase / name).read_text(encoding='utf-8')
    assert original[a:b] == selection, name
    assert selection in out.read_text(encoding='utf-8')
receipt = ['# Power supplement exact-copy validation', '', 'Exact heading selections and bounded source selections were compared with their saved authorities. No content substitution was performed.', '']
for path in [law, out, srcbase / 'tennessee-electric-306-118.txt']:
    raw = path.read_bytes()
    receipt.append(path.as_posix() + ': ' + str(len(raw)) + ' bytes; SHA-256 ' + hashlib.sha256(raw).hexdigest())
receipt.append('\nAuthority selections: ' + str(len(copies)) + '; source selections: ' + str(len(source_copies)) + '. All exact-copy assertions passed.')
(base / 'runtime/OT_2003CHUNK2_MCCONNELL_POWER_COPY_CHECK.md').write_text('\n'.join(receipt) + '\n', encoding='utf-8')
print('Created bounded law and predecision source selections; exact-copy assertions passed.')
