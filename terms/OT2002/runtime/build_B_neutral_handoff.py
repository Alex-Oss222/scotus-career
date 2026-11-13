from pathlib import Path
import re
import importlib.util

root = Path.cwd()
base = root / 'terms/OT2002'
spec = importlib.util.spec_from_file_location('entering', root / 'tools/build_entering_law.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

picks = {
    'constitutional-structure': ['United States v. Lopez', 'United States v. Harris'],
    'property-and-economic-rights': ['United States v. James Daniel Good Real Property, 510 U.S. 43'],
    'labor-and-employment': ['Barnhart v. Sigmon Coal Co., 534 U.S. 438'],
    'criminal-procedure': ['United States v. Shabani, 513 U.S. 10', 'Salinas v. United States'],
    'business-and-commercial-law': ['Campbell v. Acuff-Rose Music, Inc., 510 U.S. 569', 'Quality King Distributors, Inc. v. L’anza Research International, Inc.', 'New York Times Co. v. Tasini'],
    'first-amendment': ['Universal City Studios, Inc. v. Corley'],
}
slice_path = base / 'entering-law/OT_2002CHUNK3_B.md'
parts = [slice_path.read_text(encoding='utf-8')]
for slug, names in picks.items():
    source = root / 'state/holdings' / (slug + '.md')
    s = source.read_text(encoding='utf-8')
    for name in names:
        parts.append('## Exact Holdings selection\n\nSource: `state/holdings/' + slug + '.md`.\n\n' + module.take_heading(s, name))
projection = (base / 'workspace/neutral-projection.md').read_text(encoding='utf-8')
for x in re.split(r'(?=^### )', projection, flags=re.M):
    if x.startswith('### 2002-11-04 — INS v. Ventura') and 'summary-merits' in x or x.startswith('### 2002-12-10 — United States v. Bean'):
        parts.append('## Earlier effective current-term public law\n\n' + x.strip())
slice_path.write_text('\n\n'.join(parts).rstrip()+'\n', encoding='utf-8')

neutral = (base / 'runtime/OT_2002CHUNK3_NEUTRAL.md').read_text(encoding='utf-8')
chunks = re.split(r'(?=^## \d+\.)', neutral, flags=re.M)
selected = [x.strip() for x in chunks if re.match(r'^## (30|34|35|38)\.', x)]
assert len(selected) == 4
header = '# OT2002 chunk 3 — B neutral handoff\n\nExact derived selections of the approved neutral runtime packet. No commitments or opinion assignments are included. Research cutoffs: January 14, 2003 for Pierce County; January 15, 2003 for Barnhart and Eldred; January 21, 2003 for Jimenez Recio. Same-day decisions supply no entering law.\n\n'
(base / 'freeze/OT_2002CHUNK3_B_NEUTRAL.md').write_text(header+'\n\n'.join(selected)+'\n', encoding='utf-8')
eldred = next(x for x in selected if x.startswith('## 35.'))
corley = module.take_heading((root/'state/holdings/first-amendment.md').read_text(encoding='utf-8'), 'Universal City Studios, Inc. v. Corley')
(base/'freeze/OT_2002CHUNK3_B_ELDRED_VALIDATION_INPUT.md').write_text('# Eldred — neutral validation input\n\nThe neutral packet is copied without substantive revision. The Corley selection was identified during initial entering-law review; it is copied exactly from `state/holdings/first-amendment.md`. Validate the distinction between ordinary copyright term-setting and the distinct functional trafficking restraint addressed in Corley. No commitments are supplied.\n\n'+eldred+'\n\n## Exact entering-law selection\n\n'+corley+'\n', encoding='utf-8')
print('Created B neutral handoffs and appended exact entering-law selections.')
