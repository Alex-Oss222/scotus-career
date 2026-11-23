from pathlib import Path
import hashlib
import re

root = Path(__file__).resolve().parents[3]
term = root / 'terms' / 'OT2004'
source = term / 'runtime' / 'OT_2004CHUNK2_NEUTRAL.md'
text = source.read_text(encoding='utf-8')
parts = re.split(r'(?=^## \d+\. )', text, flags=re.M)
selected = [p for p in parts if re.match(r'^## (14|15|16)\. ', p)]
assert len(selected) == 3
frozen = '# OT2004 chunk 2 neutral extract A\n\n' + ''.join(selected)
path = term / 'freeze' / 'OT_2004CHUNK2_NEUTRAL_A.md'
path.write_text(frozen, encoding='utf-8')
whitfield = next(p for p in selected if p.startswith('## 15.'))
(term / 'freeze' / 'OT_2004CHUNK2_NEUTRAL_WHITFIELD.md').write_text('# OT2004 chunk 2 Whitfield neutral extract\n\n' + whitfield, encoding='utf-8')

# Copy prior public decisions as date-eligible Justice-position evidence.
sources = [
    ('terms/OT2003/output/OT_2003CHUNK3.md', '### Lamie v. United States Trustee,'),
    ('terms/OT2003/output/OT_2003CHUNK6.md', '### Tennessee Student Assistance Corporation v. Hood,'),
    ('terms/OT2000/output/OT_2000CHUNK7.md', '### United States v. Mead Corp.,'),
    ('terms/OT2003/output/OT_2003CHUNK2.md', '### Barnhart v. Thomas,'),
    ('terms/OT1994/output/OT_1994CHUNK1.md', '### United States v. Shabani,'),
]
public_parts = ['# Prior public opinions relevant to chunk 2 group A', '', 'Verbatim reading copies; original public renders remain authoritative for published Justice positions.', '']
for rel, heading in sources:
    original = (root / rel).read_text(encoding='utf-8')
    start = original.index(heading)
    end_marker = original.index('**End of entry:', start)
    end = original.index('\n', end_marker) if '\n' in original[end_marker:] else len(original)
    public_parts += ['Source: ' + rel, '', original[start:end], '']
(term / 'entering-law' / 'OT_2004CHUNK2_A_PUBLIC_PRIORS.md').write_text('\n'.join(public_parts), encoding='utf-8')

# Append date-scoped current-term reading text without raw Record access.
projection = (term / 'workspace' / 'neutral-projection.md').read_text(encoding='utf-8')
chosen = []
for line in projection.splitlines():
    if line.startswith('- **') and any(name in line for name in ['[Leocal v. Ashcroft]', '[Koons Buick Pontiac GMC, Inc. v. Nigh]', '[KP Permanent Make-Up v. Lasting Impression]']):
        chosen.append(line)
assert len(chosen) == 3
slice_path = term / 'entering-law' / 'OT_2004CHUNK2_A.md'
with slice_path.open('a', encoding='utf-8') as out:
    out.write('\n## Effective current-term projection selections\n\nSource: workspace/neutral-projection.md. All three entries predate December 13, 2004, and enter each group-A event; other completed entries do not materially alter the identified questions. Uncoordinated December 13 holdings do not enter Polleys.\n\n')
    out.write('\n\n'.join(chosen) + '\n')
print('Frozen A extract SHA256:', hashlib.sha256(path.read_bytes()).hexdigest())
print('Copied prior public opinions:', len(sources))
print('Selected current-term entries:', len(chosen))
