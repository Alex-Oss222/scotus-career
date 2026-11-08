from pathlib import Path
import hashlib
import json
import re

root = Path('terms/OT2000')
runtime = root/'runtime/OT_2000CHUNK2_COMMITMENTS_LATER.md'
frozen = root/'freeze/OT_2000CHUNK2_COMMITMENTS_LATER.md'
assert not frozen.exists(), 'A frozen handoff already exists; no overwrite is permitted.'
text = runtime.read_text(encoding='utf-8')
names = ['Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']
counts = {name:sum(line.startswith('| '+name+' |') for line in text.splitlines()) for name in names}
assert all(count == 4 for count in counts.values()), counts
for forbidden in ('One'+'Drive', 'Git'+'Hub'):
    assert forbidden.lower() not in text.lower()
assert not re.search(r'\]\((?:[A-Za-z]:|file:|vscode:)', text)

inputs = [Path('AGENTS.md'),Path('foundation/ENGINE.md'),root/'workspace/neutral-projection.md']
for slug in ('tricounty','brentwood','cobank','mcarthur'):
    inputs.extend([root/f'freeze/OT_2000CHUNK2_NEUTRAL_{slug}.md',root/f'entering-law/OT_2000CHUNK2_{slug}.md'])
for name in ('NEUTRAL_SUPPLEMENT','NEUTRAL_VALIDATION','CONTROL_FACTS','ROOT_FACTS','TRI_COUNTY_CONTROL_FACTS'):
    inputs.append(root/f'freeze/OT_2000CHUNK2_{name}.md')
for name in ('OT_2000CHUNK2_LATER_PUBLIC_POSITIONS.md','OT_2000CHUNK2_LATER_PUBLIC_POSITIONS_SELECTION.json','OT_2000CHUNK2_cobank_statutes.md','OT_2000CHUNK2_LATER_SOURCE_SELECTION.json'):
    inputs.append(root/'entering-law'/name)
inputs.extend([Path('terms/OT1995/output/OT_1995CHUNK9.md'),Path('terms/OT1994/output/OT_1994CHUNK2.md'),Path('terms/OT1998/output/OT_1998CHUNK5.md')])
inputs.extend(sorted((root/'sources/chunk2-later-model').glob('*.txt')))
inputs.extend(sorted((root/'sources/chunk2-later-model').glob('*.pdf')))

def entry(path):
    data=path.read_bytes()
    return {'path':str(path).replace('\\','/'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

data=runtime.read_bytes()
frozen.write_bytes(data)
assert runtime.read_bytes()==frozen.read_bytes()
receipt={
    'scope':'Independent non-Stone modeling: Tri County, Brentwood, CoBank, McArthur only',
    'mode':'isolated-context',
    'source_scope':'Only authorized neutral/source-only materials and bounded prior public writings; the three earlier output files were read only through their named case entries.',
    'preservation':'File freeze only under user command restriction; no repository commitment command used.',
    'inputs':[entry(p) for p in inputs],
    'output':entry(runtime),
    'freeze':entry(frozen),
    'byte_identity':True,
    'justice_rows_per_case':counts,
    'excluded_material_received':False,
    'new_current_chunk_law_used':False,
    'cutoffs':{'tricounty':'2001-01-17','brentwood':'2001-02-20','cobank':'2001-02-20','mcarthur':'2001-02-20'},
    'source_limits':'Statutory OCR artifacts retained in exact copies; only dated pre-event enactments used. No claim of reading withheld current-matter opinions or complete unprovided appellate submissions.'
}
receipt_path=root/'freeze/OT_2000CHUNK2_COMMITMENTS_LATER_INPUTS.json'
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'words':len(text.split()),'rows':counts,'output_sha256':receipt['output']['sha256'],'byte_identity':True,'inputs':len(inputs)},indent=2))
