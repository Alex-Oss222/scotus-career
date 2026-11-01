from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'sources/chunk4-neutral'
OUT = ROOT / 'entering-law/OT_1999CHUNK4_FDA_STATUTORY_CORRECTION.md'

def source(name):
    text = (SRC / f'FDA-statute-{name}.txt').read_text(encoding='utf-8')
    assert 'United States Code, 1998 Edition' in text and 'Page Not Found' not in text
    return text

def between(text, start, end):
    begin = text.index(start)
    return text[begin:text.index(end, begin)].strip()

def replace_once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new, 1)

blocks = []
def block(title, status, text):
    blocks.append(f'## {title}\n\n{status}\n\n```text\n{text.strip()}\n```\n')

clean_act = (ROOT / 'preparation/OT_1999CHUNK4_FDA_1997_SOURCE_TEXT.md').read_text(encoding='utf-8')
blocks.append('## Enacted mission, tobacco reservation, and effective-date text\n\n' + clean_act)

same = 'Script-copied from the saved official 1998 Code. Relevant paragraph unchanged by Pub. L. 105-115; the source amendment notes identify no intervening alteration of this selected paragraph. This is the operative earlier text, not an application of a new 1997 amendment.'
derived = 'DERIVED EARLIER READING COPY, not a retrieved historical Code edition: script-copied from the official 1998 Code and mechanically reversed only the identified exact 1997 amendments. The enacted amendment instructions and unchanged surrounding text establish the reconstruction; no words are supplied from memory.'

t = source('definitions')
block('21 U.S.C. 321(g) and (h)', same, between(t, '\n(g)(1)', '\n(i)'))
block('21 U.S.C. 321(p): new drug', same, between(t, '\n(p)', '\n(q)'))
t = source('331')
block('21 U.S.C. 331(a) and (d)', same, 'The following acts and the causing thereof are prohibited:\n' + between(t, '\n(a)', '\n(b)') + '\n' + between(t, '\n(d)', '\n(e)'))
t = source('352')
block('21 U.S.C. 352(f), (j), (q), and (r)', same, 'A drug or device shall be deemed to be misbranded—\n' + '\n'.join([between(t, '\n(f)', '\n(g)'), between(t, '\n(j)', '\n(k)'), between(t, '\n(q)', '\n(s)')]))
t = source('353')
g = between(t, '\n(g) Regulation', '\n(June')
g = replace_once(g, 'section 262(i) of title 42', 'section 262(a) of title 42')
g = replace_once(g, 'biologics license application under subsection (a)', 'product or establishment license under subsection (a) or (d)')
g = replace_once(g, '357,1', '357,')
block('21 U.S.C. 353(g): combination products', derived + ' Section 123(e) reversed in paragraph (4); paragraphs (1)–(3) unchanged. The 1998 editorial footnote marker after section 357 is removed because the underlying reference remains in the earlier text.', g)
t = source('355')
block('21 U.S.C. 355(a)', same, between(t, '\n(a)', '\n(b)'))
d = between(t, '\n(d) Grounds', '\n(e) Withdrawal')
begin = d.index(' If the Secretary determines, based on relevant science,')
added = d[begin:].strip()
act = (SRC / 'FDA-PL105-115.txt').read_text(encoding='utf-8')
assert ' '.join(added.split()) in ' '.join(act.split())
d = d[:begin]
block('21 U.S.C. 355(d): earlier complete subsection', derived + ' Section 115(a) reversed by deleting precisely the final sentence it added. The notice, hearing, seven refusal grounds, approval sentence, and original substantial-evidence definition remain intact.', d)
t = source('360c')
a = between(t, '\n(a) Classes', '\n(b) Classification')
a = a[:a.index('\n(C) In making a determination of a reasonable assurance')]
a = replace_once(a, '1 or more clinical investigations', 'clinical investigations')
block('21 U.S.C. 360c(a): earlier complete subsection', derived + ' Sections 205(a) and 217 reversed: remove new (3)(C)–(D), restore “clinical investigations” in (3)(A). Paragraphs (1), (2), and (3)(B) remain unchanged, including the alternative valid-scientific-evidence route.', a)
f = between(t, '\n(f) Initial', '\n(g) Information')
f = f[:f.index('\n(5) The Secretary may not withhold')]
new_start = f.index('\n(2)(A) Any person who submits')
old_start = f.index('\n(3)(A) The Secretary may initiate')
f = f[:new_start] + f[old_start:]
f = replace_once(f, 'petition submitted under paragraph (3)', 'petition submitted under paragraph (2)')
f = replace_once(f, 'under paragraph (2) or (3) classifying', 'under paragraph (2) classifying')
f = replace_once(f, '\n(3)(A) The Secretary may initiate', '\n(2)(A) The Secretary may initiate')
f = replace_once(f, '\n(4) If a manufacturer reports', '\n(3) If a manufacturer reports')
block('21 U.S.C. 360c(f): earlier complete subsection', derived + ' Sections 206(b) and 207 reversed: remove new (5) and new (2), restore former numbering and cross-references. The preexisting reclassification-petition process remains; the new 30-day de novo request is not supplied as a tobacco route.', f)
i = between(t, '\n(i) Substantial', '\n(June')
start = i.index('\n(C) To facilitate reviews')
end = i.index('\n(2) A device may not be found')
i = i[:start] + i[end:]
i = replace_once(i, 'appropriate clinical or scientific data', 'clinical data')
i = replace_once(i, ' or a person accredited under section 360m of this title', '')
i = replace_once(i, 'different questions of safety and effectiveness', 'different questions of safety and efficacy')
block('21 U.S.C. 360c(i): earlier complete subsection', derived + ' Sections 205(b) and 206(c) reversed: remove new (1)(C)–(F), restore clinical-data and efficacy wording, and remove accreditation addition. No new labeling-based intended-use constraint is imported into the coverage question.', i)
for name in ['360f', '360h', '360k']:
    t = source(name)
    block(f'21 U.S.C. {name}: complete operative section', same, between(t, '\n(a)', '\n(June'))
t = source('360j')
block('21 U.S.C. 360j(e): complete restricted-device subsection', same, between(t, '\n(e) Restricted', '\n(f) Good'))

for name in ['1331', '1334', '4406']:
    t = (SRC / f'FDA-statute-{name}.txt').read_text(encoding='utf-8')
    assert 'United States Code, 1998 Edition' in t and 'Page Not Found' not in t
    block(f'Title 15, section {name}: original official source copy', 'Section 422 concerns the FDCA, not a repeal or amendment of these separate tobacco enactments. This source is retained from the original annex with its original editorial notes.', t)

# Complete numbered sections, including any internal new sections, bounded by
# the next numbered top-level section rather than the next generic SEC marker.
for n in [115, 123, 205, 206, 207, 217, 416]:
    start = act.index(f'SEC. {n}.')
    next_n = 301 if n == 217 else n + 1
    end = act.index(f'SEC. {next_n}.', start)
    block(f'Pub. L. 105-115 section {n}: exact amendment instructions', 'Mechanically copied from the saved official Act. Used to audit the earlier reading copies or identify new provisions excluded by section 422; not substituted for the earlier tobacco regime.', act[start:end])

header = '''# FDA statutory source correction: November 20, 1997 tobacco baseline

This supplemental annex controls over the original FDA_STATUTORY_TEXT annex for FDA modeling. The original annex is preserved for provenance, but its 1998 Code as a whole is not an operative tobacco-law compilation. Its FDA-statute-393 block is an error-navigation page and supplies no law. That defect and the omitted section 422 are expressly corrected here.

The exact 1997 session law is official source text. Selected unchanged paragraphs below are copied from official 1998 Code sources after amendment review. Changed material subsections are expressly labeled DERIVED EARLIER READING COPY and mechanically reconstructed by reversing the exact enacted amendments; they are not represented as an independently retrieved 1994 or 1996 Code. A later Code's editorial cross-references remain Code cross-references. No omitted subsection of the original annex is certified for operative tobacco use. If a decisional path requires one, obtain and validate its November 20, 1997 form before use.

Primary Act source: https://www.govinfo.gov/content/pkg/PLAW-105publ115/html/PLAW-105publ115.htm . Original saved Code sources are identified by section in sources/chunk4-neutral/FDA-statute-*.html and .txt; no generic current-case source was consulted. Build script: preparation/build_fda_1997_repair.py.

'''
OUT.write_text(header + '\n'.join(blocks), encoding='utf-8')
print(OUT.as_posix(), OUT.stat().st_size)
