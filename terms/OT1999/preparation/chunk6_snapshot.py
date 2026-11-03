from pathlib import Path
import hashlib,json
root=Path('.'); term=root/'terms/OT1999'
files=[*Path('foundation').rglob('*.md'), *Path('state').rglob('*.md'),Path('AGENTS.md'),*Path('tools').glob('*.py'),*term.joinpath('briefs').glob('*.md'),*term.joinpath('records').glob('*.md'),*term.joinpath('output').glob('*.md'),*term.joinpath('render-inputs').glob('*.md')]
hashes={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
out=term/'freeze/OT_1999CHUNK6_BASELINE_HASHES.json'
if out.exists(): raise SystemExit('baseline already exists')
out.write_text(json.dumps(hashes,indent=2)+'\n',encoding='utf-8')
for name in ['neutral-projection','continuity','manifest','ledger']:
 (term/'freeze'/('OT_1999CHUNK6_OPENING_'+name.upper().replace('-','_')+'.md')).write_bytes((term/'workspace'/(name+'.md')).read_bytes())
print('Saved baseline hashes and four workspace snapshots; no repository-history access.')
