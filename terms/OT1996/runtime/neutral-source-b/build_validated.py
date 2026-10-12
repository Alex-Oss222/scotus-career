from pathlib import Path
import hashlib
import html
import re

ROOT = Path(__file__).resolve().parents[4]
TERM = ROOT / 'terms/OT1996'
SRC = TERM / 'runtime/neutral-source-b'

def read(path):
    return path.read_bytes().decode('utf-8-sig')

def bounded(text, start, end=None):
    a = text.index(start)
    b = text.index(end, a + len(start)) if end else len(text)
    return text[a:b]

def section(text, title):
    a = text.index(title)
    m = re.search(r'(?m)^## ', text[a + len(title):])
    b = a + len(title) + m.start() if m else len(text)
    return text[a:b].rstrip()

def statute(name):
    raw = read(SRC / name)
    raw = bounded(raw, '<!-- field-start:statute -->', '<!-- field-end:statute -->')
    raw = re.sub(r'</p>', '\n\n', raw)
    return html.unescape(re.sub(r'<[^>]+>', '', raw)).strip()

facts = read(TERM / 'sources/chunk2-control/NEUTRAL_OBJECTIVE_FACTS_B.md')
original_b = read(TERM / 'runtime/OT_1996CHUNK2_NEUTRAL_B.md')
original_c = read(TERM / 'runtime/OT_1996CHUNK2_NEUTRAL_C.md')
walters = bounded(original_c, '# 24.', '# 25.') if '# 25.' in original_c else bounded(original_c, '# 24.')
law_b = read(TERM / 'entering-law/OT_1996CHUNK2_B.md')
law_c = read(TERM / 'entering-law/OT_1996CHUNK2_C.md')
law_current = read(TERM / 'workspace/neutral-projection.md')

def holding(source, name):
    a = source.index(name)
    m = re.search(r'(?m)^#{2,4} ', source[a+len(name):])
    return source[a:a+len(name)+m.start()].rstrip() if m else source[a:].rstrip()

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

sec921 = bounded(statute('18usc921_1994.html'), '(20)', '(21)').rstrip()
sec3661 = statute('18usc3661_1994.html')
vii = read(SRC / 'titlevii_2011_compilation.txt')
vii_b = bounded(vii, '(b) The term', '(c) The term').rstrip()
vii_f = bounded(vii, '(f) The term', '(g) The term').rstrip()
vii_history = bounded(vii, 'AMENDMENTS', 'EFFECTIVE DATE OF 1991').rstrip()
(SRC / '18usc921a20_1994.txt').write_text(sec921+'\n', encoding='utf-8')
(SRC / '18usc3661_1994.txt').write_text(sec3661+'\n', encoding='utf-8')
(SRC / '42usc2000e_b_f_source.txt').write_text(vii_b+'\n\n'+vii_f+'\n\n'+vii_history+'\n', encoding='utf-8')

common = '''## Preparation receipt and priority

This is a clean neutral-preflight handoff under Engine §§3A, 5 and 14. It contains no vote modeling. The approved neutral extraction is copied below by script, without rewriting the source brief. The express corrections and qualifications in this receipt govern over stale or categorical sentences in that copied baseline. Sanitized objective-source recitations are copied separately with their original source limits.

Preparation baseline: the current neutral projection has a completed-event cursor of December 10, 1996, covering twelve Court events and two admitted sources. The copied packets' statement that no OT1996 decision is completed is obsolete. The current projection, including Roy, Hopwood, Askin and Caterpillar at their respective scopes, governs together with the entering-law slices. No material holding decides these assigned questions automatically. Refresh the clean neutral projection for any earlier-effective chunk-2 event before modeling a later event; processing order supplies no intervening law between uncoordinated same-day peers.

Composition: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer are seated at each supplied argument and decision date. No case-specific exclusion is established in the authorized packet. Private positions, the full brief, current-matter historical outcomes, comparator, commitments and reconciliation were not supplied or opened. Original-source absence is an operator research limit, never litigant default. No factual reconstruction premise is adopted here, and preparation changes no Court order or law.
'''

b_note = read(SRC / 'supplement_b.md')
w_note = read(SRC / 'supplement_walters.md')
b = '# OT1996 chunk 2 — validated neutral handoff B\n\n'+common+'\n'+b_note+'\n\n## Approved neutral source extraction — verbatim copy\n\n'+original_b
b += '\n\n## Sanitized published objective recitations — verbatim copy\n\n'+section(facts,'## Watts and Putra')+'\n\n'+section(facts,'## Old Chief')
b += '\n\n## Walmer stipulated conduct and exception posture — verbatim lower-opinion recitation\n\n'+bounded(read(TERM/'sources/chunk2-neutral/Walmer_lower_opinion.txt'),'Plaintiff expressly acknowledged the truth', 'Plaintiff also asserted').rstrip().removesuffix('2').rstrip()
b += '\n\n## Bounded statutory reading copies\n\n### 18 U.S.C. §3661 (1994 official edition)\n\n'+sec3661+'\n\n### 18 U.S.C. §921(a)(20) (1994 official edition)\n\n'+sec921
b += '\n\n## Material governing-law clarifications — copied from entering law\n\n'
for name in ['#### Harris v. Forklift Systems, Inc., 510 U.S. 17','#### R. A. V. v. City of St. Paul, 505 U.S. 377 (1992)','#### Wisconsin v. Mitchell, 508 U.S. 476 (1993)','#### Hurley v. Irish-American Gay, Lesbian and Bisexual Group of Boston','#### Romer v. Evans, 517 U.S. 620']:
    b += holding(law_b,name)+'\n\n'
b += '\n## Copy validation\n\nApproved neutral B source SHA-256: `'+digest(TERM/'runtime/OT_1996CHUNK2_NEUTRAL_B.md')+'`. The source extraction above is mechanically identical to that decoded source; the original brief is untouched. Objective facts source SHA-256: `'+digest(TERM/'sources/chunk2-control/NEUTRAL_OBJECTIVE_FACTS_B.md')+'`.\n'

w = '# OT1996 chunk 2 — validated neutral handoff, Walters\n\n'+common+'\n'+w_note+'\n\n## Approved neutral source extraction — verbatim #24 only\n\n'+walters
w += '\n\n## Sanitized published objective recitations — verbatim copy\n\n'+section(facts,'## Walters')
w += '\n\n## Operative statutory text — mechanically extracted\n\n'+vii_b+'\n\n'+vii_f+'\n\n### Temporal verification from official amendment history\n\n'+vii_history
w += '\n\n## Date-eligible classification analogies — copied from entering law\n\n'+holding(law_c,'#### Nationwide Mutual Insurance Co. v. Darden, 503 U.S. 318 (1992)')+'\n\n'+holding(law_c,'#### NLRB v. Town & Country Electric, Inc., 516 U.S. 85')
w += '\n\n## Copy validation\n\nWalters source block SHA-256 (UTF-8 encoded decoded block): `'+hashlib.sha256(walters.encode()).hexdigest()+'`. No other case block from neutral C is copied. Objective facts source SHA-256: `'+digest(TERM/'sources/chunk2-control/NEUTRAL_OBJECTIVE_FACTS_B.md')+'`.\n'

targets = [(TERM/'freeze/OT_1996CHUNK2_NEUTRAL_B_VALIDATED.md',b,original_b),(TERM/'freeze/OT_1996CHUNK2_NEUTRAL_WALTERS_VALIDATED.md',w,walters)]
for path, content, original in targets:
    path.write_bytes(content.encode('utf-8'))
    assert original in read(path)
    assert '## Public Projection' not in content
    print(path.relative_to(ROOT),len(content.encode('utf-8')),'bytes; verbatim baseline verified')
