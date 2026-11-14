from pathlib import Path
import importlib.util
import re
import subprocess
import sys

base = Path('terms/OT2002')
spec = importlib.util.spec_from_file_location('law_copy', 'tools/build_entering_law.py')
law = importlib.util.module_from_spec(spec)
spec.loader.exec_module(law)

standards = {
    '153': ['Content-neutral permits for shared public space', 'Public-forum continuity on replacement public passageways', 'Advance permits for ordinary noncommercial canvassing'],
    '154': ['Serious risks in prison conditions and deliberate indifference', 'Legal-advice content in inmate correspondence', 'Prison-conditions prospective relief'],
    '156': ['Intermediary contribution limits and meaningful association', 'Nonprofit political spending outside a literal safe harbor', 'Candidate contribution limits and anticorruption fit'],
    '159': ['Adult access and content-based criminal network-speech restrictions', 'Cable access permissions and the invalid compulsory segregation system', 'Editorial selection in public-broadcaster candidate debates', 'Comparative standards in selective federal arts grants', 'Legal-validity arguments within funded independent welfare representation', 'Protected nonobscene depictions without actual-child exploitation'],
}
holdings = {
    '153': {
        'first-amendment': ['R. A. V. v. City of St. Paul, 505 U.S. 377 (1992)', 'Forsyth County v. Nationalist Movement, 505 U.S. 123 (1992)', 'Thomas v. Chicago Park District, 534 U.S. 316', 'Watchtower Bible & Tract Society of New York, Inc. v. Village of Stratton, 536 U.S. 150'],
    },
    '154': {
        'first-amendment': ['Shaw v. Murphy, 532 U.S. 223'],
        'civil-rights': ['Farmer v. Brennan, 511 U.S. 825', 'Deliberate deprivation of meaningful exercise in prison'],
        'criminal-procedure': ['Helling v. McKinney, 509 U.S. 25 (1993)'],
    },
    '156': {
        'first-amendment': ['Day v. Holahan'],
        'election-law': ['Kentucky Right to Life, Inc. v. Stengel', 'Russell v. Burris', 'Nixon v. Shrink Missouri Government PAC, 528 U.S. 377 (2000)', 'Mariani v. United States', 'FEC v. Colorado Republican Federal Campaign Committee', 'Missouri Republican Party v. Lamb'],
    },
    '159': {
        'first-amendment': ['Reno v. American Civil Liberties Union', 'Denver Area Educational Telecommunications Consortium, Inc. v. FCC; Alliance for Community Media v. FCC, 518 U.S. 727 (1996)', 'Arkansas Educational Television Commission v. Forbes', 'National Endowment for the Arts v. Finley', 'Rosenberger v. Rector and Visitors of the University of Virginia', 'Legal Services Corp. v. Velazquez / United States v. Velazquez, 531 U.S. 533', 'Ashcroft v. Free Speech Coalition, 535 U.S. 234', 'Ashcroft v. American Civil Liberties Union, 535 U.S. 564'],
    },
}
current = {
    '153': ('2003-06-16', ['First Unitarian Church of Salt Lake City', 'Virginia v. Black']),
    '154': ('2003-06-16', ['Gerber v. Hickman']),
    '156': ('2003-06-16', []),
    '159': ('2003-06-23', ['American Amusement Machine Association', 'Center for Reproductive Law and Policy', 'Conant v. Walters']),
}
projection = (base / 'workspace/neutral-projection.md').read_text(encoding='utf-8')
projection_parts = re.split(r'(?=^### \d{4}-)', projection, flags=re.M)
full_public = (base / 'entering-law/OT_2002CHUNK13_A_CURRENT_PUBLIC.md').read_text(encoding='utf-8')
full_parts = re.split(r'(?=^# Source )', full_public, flags=re.M)
full_selections = {'153': ['Virginia-v-Black', 'Planned-Parenthood-v-ACLA'], '154': [], '156': [], '159': ['Center-for-Reproductive-Law-and-Policy']}
for case, heads in standards.items():
    target = base / f'entering-law/OT_2002CHUNK13_{case}_LAW.md'
    args = [sys.executable, '-B', 'tools/build_entering_law.py', str(target), '--standing-heading', '1. Current Court']
    for heading in heads:
        args += ['--standard-heading', heading]
    subprocess.run(args, check=True)
    chunks = [target.read_text(encoding='utf-8')]
    for volume, titles in holdings[case].items():
        source = Path('state/holdings') / (volume + '.md')
        text = source.read_text(encoding='utf-8')
        for title in titles:
            chunks += [f'\n## Exact holding selection from `{source.as_posix()}`\n\n', law.take_heading(text, title), '\n']
    cutoff, titles = current[case]
    chunks += [f'\n## Current-term public law and published positions strictly before {cutoff}\n\n']
    matched = []
    for part in projection_parts:
        match = re.match(r'### (\d{4}-\d\d-\d\d) — (.*)', part)
        if match and match[1] < cutoff and any(title in match[2] for title in titles):
            # Bound the final dated section before any new top-level section.
            part = re.split(r'(?=^## )', part, flags=re.M)[0]
            chunks += [part.rstrip(), '\n\n']
            matched.append(match[2])
    if not matched:
        chunks += ['No additional directly governing earlier current-term holding is selected for this issue. This is a scope selection, not a claim that the term contains no related cases.\n']
    for part in full_parts:
        if not part.startswith('# Source '):
            continue
        heading = part.splitlines()[0]
        date = re.search(r'effective (\d{4}-\d\d-\d\d)', heading).group(1)
        if date < cutoff and any(key in heading for key in full_selections[case]):
            chunks += ['\n## Complete bounded public projection, mechanically supplied through control\n\n', part.rstrip(), '\n']
    target.write_text(''.join(chunks), encoding='utf-8')

# Store exact public writing excerpts separately to keep the principal law slices readable.
public_sources = [
    ('terms/OT1999/output/OT_1999CHUNK2.md', 'Nixon v. Shrink'),
    ('terms/OT2000/output/OT_2000CHUNK1.md', 'Mariani v.'),
    ('terms/OT1995/output/OT_1995CHUNK10.md', 'Denver Area'),
    ('terms/OT1996/output/OT_1996CHUNK13.md', 'Reno v. American'),
    ('terms/OT1997/output/OT_1997CHUNK12.md', 'National Endowment'),
    ('terms/OT2000/output/OT_2000CHUNK3.md', 'Legal Services Corp.'),
    ('terms/OT1993/output/OT_1993CHUNK6.md', 'Farmer v. Brennan'),
]
out = ['# Date-eligible public separate-writing excerpts\n\nMechanically copied public text only. These writings supply individual jurisprudential evidence; noncontrolling views are not governing law.\n\n']
for path, query in public_sources:
    text = Path(path).read_text(encoding='utf-8')
    case = next(part for part in re.split(r'(?=^### )', text, flags=re.M) if part.startswith('### ') and query in part.splitlines()[0])
    out += [f'## Source: `{path}`\n\n', case.splitlines()[0], '\n\n']
    for part in re.split(r'(?=^#### )', case, flags=re.M):
        if 'Separate' in part.splitlines()[0]:
            out += [part.rstrip(), '\n\n']
(base / 'entering-law/OT_2002CHUNK13_A_PUBLIC_WRITINGS.md').write_text(''.join(out), encoding='utf-8')

source_dir = base / 'sources/chunk13-a'
statutes = ['# Exact statutory reading excerpts\n\nDerived from the saved official 2002 Code text. The entire source sections remain in the source directory. The corpus is evidence of enacted text, not an adjudication of unrelated statutory branches.\n\n']
for filename, start, end, title in [
    ('usc20-9134-2002.txt', '(f) Internet safety', '(Pub. L.', '20 U.S.C. 9134(f)'),
    ('usc47-254-2002.txt', '(6) Requirements for certain libraries', '(i) Consumer protection', '47 U.S.C. 254(h)(6)-(7)'),
    ('usc2-441b-2002.txt', '(a) In general', '(c) Rules relating to electioneering communications', '2 U.S.C. 441b(a)-(b)'),
]:
    text = (source_dir / filename).read_text(encoding='utf-8')
    beginning = text.index(start)
    finish = text.index(end, beginning)
    statutes += [f'## {title}\n\n', text.splitlines()[0], '\n\n', text[beginning:finish], '\n']
(base / 'entering-law/OT_2002CHUNK13_A_STATUTES.md').write_text(''.join(statutes), encoding='utf-8')

# The neutral input copy contains only the four assigned cases, with no withheld sections.
neutral = (base / 'runtime/OT_2002CHUNK13_NEUTRAL.md').read_text(encoding='utf-8')
parts = [part for part in re.split(r'(?=^## \d+\.)', neutral, flags=re.M) if re.match(r'## (153|154|156|159)\.', part)]
assert len(parts) == 4
packet = '# OT2002 chunk 13 neutral packet A\n\nExact Section I copy for cases 153, 154, 156 and 159. Preflight only; no vote commitments. The supplements and law selections below are part of the neutral handoff.\n\n' + ''.join(parts)
packet += '\n## Neutral supplement and exact entering law\n\n'
packet += (base / 'runtime/OT_2002CHUNK13_PREFLIGHT_A.md').read_text(encoding='utf-8')
packet += '\n\n## Validated objective Overton rule excerpt\n\n'
packet += (base / 'entering-law/OT_2002CHUNK13_OVERTON_RULES_NEUTRAL.md').read_text(encoding='utf-8')
(base / 'freeze').mkdir(exist_ok=True)
(base / 'freeze/OT_2002CHUNK13_A_NEUTRAL.md').write_text(packet, encoding='utf-8')
print('Created four law slices, public-writing excerpts, statutory excerpts, and frozen neutral packet A.')
