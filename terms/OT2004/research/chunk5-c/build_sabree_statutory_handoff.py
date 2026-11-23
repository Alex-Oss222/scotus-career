from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / 'chunk5-neutral' / 'Sabree-statutory-excerpts.md'


def read(name):
    return (ROOT / name).read_text(encoding='utf-8')


def between(text, start, end):
    a = text.index(start)
    b = text.index(end, a + len(start))
    return text[a:b].strip()


sources = {n: read('sabree_2004_' + n + '.txt')
           for n in ['1396a', '1396d', '1396c', '1320a-2', '1320a-10', '1983']}
parts = [
    '# Sabree: operative statutory text copied from official 2004 Code\n\n'
    'Internal neutral source handoff. Cutoff March 29, 2005. '
    'The excerpts below are copied by script from the saved official-source text, '
    'without retyping or substantive revision. They supply text, not an adjudication. '
    'The full source files retain the amendment and effective-date notes. '
    'The complete paragraph (a)(10) is included to preserve its qualifications; '
    'its many unrelated categories are not findings about these plaintiffs.\n'
]
selections = [
    ('1396a', 'State-plan command', between(sources['1396a'], '(a) Contents', '(1) provide')),
    ('1396a', 'Section 1396a(a)(3): fair hearing', between(sources['1396a'], '(3) provide', '(4) provide')),
    ('1396a', 'Section 1396a(a)(8): application and reasonable promptness', between(sources['1396a'], '(8) provide', '(9) provide')),
    ('1396a', 'Section 1396a(a)(10): complete paragraph, including exceptions', between(sources['1396a'], '(10) provide', '(11)(A) provide')),
    ('1396a', 'Section 1396a(a)(31): care plan and independent review', between(sources['1396a'], '(31) with respect', '(32) provide')),
    ('1396d', 'Section 1396d(a): complete payment definition, eligibility categories and covered-care list', between(sources['1396d'], '(a) Medical assistance', '(b) Federal medical')),
    ('1396d', 'Section 1396d(d): facility definition and conditions', between(sources['1396d'], '(d) Intermediate care', '(e) Physicians')),
    ('1396c', 'Section 1396c: federal funding oversight', sources['1396c'][sources['1396c'].index('§1396c.'):].strip()),
    ('1320a-2', 'Section 1320a-2: state-plan placement and preserved Suter result', sources['1320a-2'][sources['1320a-2'].index('§1320a–2.'):].strip()),
    ('1320a-10', 'Section 1320a-10: state-plan placement and preserved Suter result', sources['1320a-10'][sources['1320a-10'].index('§1320a–10.'):].strip()),
    ('1983', 'Section 1983: express civil-rights action', sources['1983'][sources['1983'].index('§1983.'):].strip()),
]
for key, heading, excerpt in selections:
    source_url = sources[key].splitlines()[0].removeprefix('Source: ')
    parts += ['\n## ' + heading + '\n\n', 'Source: ' + source_url + '\n\n', excerpt, '\n']
parts += ['\n## Source integrity\n\n']
for key in sources:
    name = 'sabree_2004_' + key + '.txt'
    parts += [name + ': SHA-256 ' + hashlib.sha256((ROOT / name).read_bytes()).hexdigest() + '\n\n']
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(''.join(parts), encoding='utf-8', newline='\n')
print(OUT.name, len(OUT.read_bytes()), 'bytes; all excerpts script-copied')
