from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys
sys.dont_write_bytecode=True

term=Path(__file__).resolve().parents[1]
root=term.parents[1]
baseline=json.loads((term/'freeze/OT_1999CHUNK9_PRESERVATION_BASELINE.json').read_text(encoding='utf-8'))
expected=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
changed=[]
for name,digest in baseline.items():
    p=root/name
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest: changed.append(name)
allowed={f'terms/OT1999/workspace/{n}.md' for n in ['manifest','ledger','continuity','neutral-projection']}
assert set(changed)<=allowed, changed
new=[]
for p in (term/'records').glob('*.md'):
    if p.relative_to(root).as_posix() not in baseline:new.append(p)
assert len(new)==9, ('Expected eight Court events and one filing source',len(new))
spec=importlib.util.spec_from_file_location('chunk9_tools',term/'runtime/chunk9_tools.py')
countmod=importlib.util.module_from_spec(spec);spec.loader.exec_module(countmod)
details=[]
for p in sorted(new):
    text=p.read_text(encoding='utf-8')
    lines=text.splitlines()
    for i,label in enumerate(['Case and dockets','Event and date','Result','Version / lineage']):
        assert lines[i].startswith('**'+label+':**'),(p.name,label)
    assert text.count('## Public Projection')==1,p.name
    pub=text.split('## Public Projection',1)[1].strip()
    assert re.findall(r'^## (.+)$',pub,re.M)==expected,p.name
    assert not re.search(r'\b(simulated|simulation|operator|reconciled|runtime|workflow|fallback|2026)\b',pub,re.I),(p.name,'public workflow')
    assert not re.search(r'github\.com|onedrive|\]\((?:file:|[A-Z]:[/\\])',text,re.I),(p.name,'forbidden link')
    parts=re.split(r'^## (.+)\n',pub,flags=re.M)
    blocks={parts[i]:parts[i+1].strip() for i in range(1,len(parts),2)}
    hold=blocks['Holdings']
    if '## Controlling holdings\n' in text:
        internal=text.split('## Controlling holdings\n',1)[1].split('\n## ',1)[0].strip()
        assert internal==hold,(p.name,'holdings mismatch')
    explanations=re.findall(r'\*\*Controlling explanation:\*\*\s*(.*?)(?=\n\n### |\Z)',hold,re.S)
    lengths=[len(e.split()) for e in explanations]
    assert all(n<=350 for n in lengths),(p.name,lengths)
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
        if re.match(r'https?://|mailto:',target):continue
        path=target.split('#')[0]
        if not path:continue
        assert (p.parent/path).exists(),(p.name,target)
    details.append({'record':p.name,'explanation_words':lengths})

for case in ['JONES','HENEREY','MOBIL','DALE','HILL','MITCHELL','STENBERG']:
    p=term/f'freeze/OT_1999CHUNK9_{case}_ASSIGNMENT_COUNTS.json'
    if not p.exists():
        raise AssertionError('Missing fresh count receipt: '+p.name)
    data=json.loads(p.read_text(encoding='utf-8'))
    actual=countmod.counts(data['before_date'],data['before_case'])
    assert data['counts']==actual['counts'],(case,data['counts'],actual['counts'])
    assert data['last_event']==actual['last_event'],(case,'last event')

for case in ['JONES','HENEREY','MOBIL','DALE','HILL','MITCHELL','STENBERG','ALASKA']:
    for stage in ['COMMITMENTS','RECONCILED']:
        f=term/f'freeze/OT_1999CHUNK9_{case}_{stage}.md'
        r=term/f'runtime/OT_1999CHUNK9_{case}_{stage}.md'
        assert f.read_bytes()==r.read_bytes(),(case,stage)

rin=term/'render-inputs/OT_1999CHUNK9.md'
inp=rin.read_text(encoding='utf-8')
entries=re.findall(r'<!-- source-record: ([^>]+) -->\n(.*?)(?=\n\n---\n\n<!-- source-record:|\Z)',inp,re.S)
assert len(entries)==8,len(entries)
for name,projection in entries:
    actual=(term/'records'/name).read_text(encoding='utf-8').split('## Public Projection',1)[1].strip()
    assert actual==projection.strip(),name
assert not (term/'output/OT_1999CHUNK9.md').exists(),'Run must not author Render'
report={'status':'PASS','prior_files_preserved':len(baseline)-len(changed),'changed_baseline_files':changed,'new_records':details,'render_input_events':len(entries),'git_verification':'Not performed; all Git commands prohibited by user.'}
(term/'freeze/OT_1999CHUNK9_DETERMINISTIC_VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
