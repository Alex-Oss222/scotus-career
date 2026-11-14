from pathlib import Path
import hashlib
import re

root = Path(__file__).resolve().parents[1]
src = root / 'sources/chunk10-comparators/01-188_ZO.txt'
dst = root / 'freeze/OT_2002CHUNK10_WALSH_SOURCE_FACTS.md'
raw = src.read_text(encoding='utf-8')
lines = raw.splitlines()

def one(prefix):
    found = [(i + 1, s.strip()) for i, s in enumerate(lines) if s.strip().startswith(prefix)]
    assert len(found) == 1, (prefix, len(found))
    return found[0]

selected = [
    ('Motion and supporting submissions', 'Several months before January 1, 2001'),
    ('Manufacturers: affidavit descriptions and opinions', 'Four of the affidavits describe'),
    ('State: opposing affidavit descriptions and proposed safeguards', 'Respondents’ opposition to the motion'),
    ('District-court assumptions and stated grounds', 'Without resolving any factual issues, the District Court granted'),
]
body = []
for title, prefix in selected:
    num, passage = one(prefix)
    body += [f'## {title}', '', f'Source-copy line: {num}. The following paragraph is copied mechanically, without alteration.', '', passage, '']

num, paragraph = one('The centerpiece of petitioner’s attack')
marker = 'It appears that Maine had argued before the District Court'
assert paragraph.count(marker) == 1
sentence = paragraph[paragraph.index(marker):]
assert sentence.endswith('what it has done.')
body += [
    '## Characterization of the State’s district-court argument', '',
    'This is a qualified published characterization of the position advanced below, not a recovered transcript, a factual concession or a finding that no Medicaid benefit is possible. Its opening qualification is retained. Only the record-characterization sentence is copied; no reviewing Court legal conclusion accompanies it.', '',
    f'Source-copy line: {num}, final sentence, copied mechanically.', '', sentence, '',
]

body += ['## Source notes accompanying the copied record paragraphs', '', 'The following numbered notes are copied mechanically from the same source. They identify the cited underlying materials; possession of those underlying materials is not claimed here.', '']
note_numbers = []
for i, line in enumerate(lines):
    match = re.match(r'^(\d+)\.\s', line.strip())
    if match and 18 <= int(match.group(1)) <= 29:
        note_numbers.append(int(match.group(1)))
        body += [f'Source-copy line {i + 1}:', '', line.strip(), '']
assert note_numbers == list(range(18, 30))

header = '''# Walsh — bounded source facts for fresh neutral validation

**Event and cutoff:** Pharmaceutical Research and Manufacturers of America v. Walsh, No. 01-188; May 19, 2003. This supplement concerns the already identified preliminary-injunction review and creates no new filing, agency action, assumption or Court event.

**Purpose and status:** The existing validated packet describes disputed operational effects but does not reproduce the detailed submission and affidavit posture below. These source excerpts permit fresh neutral validation of that posture. They contain objective submission descriptions, attributed affidavit assertions, a qualified characterization of a litigating position, and the district court’s own stated assumptions and grounds. None is a final finding that Maine Rx caused or prevented a particular access injury, saving or eligibility change.

**Primary source map:** `terms/OT2002/sources/chunk10-comparators/01-188_ZO.txt`, the saved text of Pharmaceutical Research and Manufacturers of America v. Walsh, 538 U.S. 644, record narrative in Part III at 655–659, associated notes 18–29, and the final record-characterization sentence in the first paragraph of Part V at 662. The official report counterpart is `terms/OT2002/sources/chunk10-comparators/walsh-reporter.txt`. The source-copy line numbers below identify the exact saved-text passage, independent of page extraction. Only the specified record passages are exposed here; this handoff supplies no reviewing Court disposition, lineup, opinion assignment or legal analysis.

**Underlying source limits:** The excerpts identify complaint and appendix citations, sworn submissions and the October 26, 2000 district-court ruling. The original affidavits and full trial-court file are not newly represented as recovered or read. The narrow source mechanism is a supported published recitation under Engine §14. A fresh validator should retain the distinction between the fact that an affidavit was submitted, its asserted prediction or opinion, the district court’s express assumption, and any disputed inference from that material.

**Existing qualifications remain:** The program had not been implemented; generic prior-authorization effects do not establish actual effects of this program. Maine’s statute includes its as-permitted-by-law qualification, and its offered clinical procedures and proposed rules are not established implementation. No concession that the program could serve no Medicaid purpose is established merely because the State asserted that it need not demonstrate one. The actual CMS letter and the preserved scope of the approval issue remain in the previously validated handoff. Ordinary preliminary-relief criteria and the proper review of legal conclusions and discretionary decisions remain questions for independent adjudication, not conclusions supplied by this extract.

'''
digest = hashlib.sha256(src.read_bytes()).hexdigest()
text = header + f'**Saved source SHA-256:** `{digest}`.\n\n' + '\n'.join(body)
assert not dst.exists(), 'Preserve any existing source-facts freeze'
dst.write_text(text, encoding='utf-8', newline='\n')
print(f'Created {dst.name}: {len(text)} characters, {len(selected)} full record paragraphs, one qualified sentence, twelve source notes.')
