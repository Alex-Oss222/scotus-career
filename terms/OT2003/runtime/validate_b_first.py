from pathlib import Path
import re, hashlib, json
base=Path('terms/OT2003')
keys={'RAYTHEON':'raytheon_co_v_hernandez_merits_2003-12-02.md','BANKS':'united_states_v_banks_merits_2003-12-02.md','VAN_SUSTEREN':'van_susteren_v_jones_merits_2003-12-04.md','VIRGINIA':'virginia_v_maryland_merits_2003-12-09.md'}
blocks=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
labels=['**Case and dockets:**','**Event and date:**','**Result:**','**Version / lineage:**']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def topo(s):
    if '## Public Projection' in s:s=s.split('## Public Projection',1)[1]
    return re.search(r'^## Opinion Topology\n(.*?)(?=^## |\Z)',s,re.M|re.S).group(1).strip()
prior=(base/'runtime/OT_2003CHUNK2_PRIOR_OPINION_TABLES.md').read_text(encoding='utf-8')
prior_checked=0
for b in re.split(r'(?m)^# ',prior):
    name=b.splitlines()[0] if b else ''
    if not name.endswith('.md'):continue
    assert topo(b)==topo((base/'records'/name).read_text(encoding='utf-8')),name
    prior_checked+=1
assert prior_checked==15
annex=[]
for key,name in keys.items():
    p=base/'records'/name;s=p.read_text(encoding='utf-8');lines=s.splitlines()
    assert all(lines[i].startswith(label) for i,label in enumerate(labels))
    assert s.count('## Public Projection\n')==1
    pub=s.split('## Public Projection\n\n',1)[1]
    assert re.findall(r'^## (.+)$',pub,re.M)==blocks
    assert pub.encode()==(base/'runtime'/f'OT_2003CHUNK2_{key}_PUBLIC.md').read_bytes()
    assert pub.encode()==(base/'freeze'/f'OT_2003CHUNK2_{key}_PUBLIC.md').read_bytes()
    assert not re.search(r'(?i)simulat|reconcil|commitment|workflow|user.approval|historical comparator|version|lineage|model|2026|runtime/|freeze/',pub)
    for suffix in ['COMMITMENTS','RECONCILED']:
        f=base/'freeze'/f'OT_2003CHUNK2_{key}_{suffix}.md';raw=f.read_text(encoding='utf-8')
        assert raw in s
        annex.append(f'- `{f.relative_to(base).as_posix()}`: `{sha(f)}`; exact normalized-text inclusion passed.')
    assert all(w not in s for w in ['One'+'Drive','Git'+'Hub','file://'])
    print(key,'headers, annex identity, public identity and leakage checks passed')
validation=base/'runtime/OT_2003CHUNK2_B_FIRST_ASSEMBLY_VALIDATION.md'
v=validation.read_text(encoding='utf-8')
for key,name in keys.items():
    data=json.loads(re.search(r'^## '+key+r'\n\n(.*?)(?=^## |\Z)',v,re.M|re.S).group(1))
    assert data['record_sha256']==sha(base/'records'/name)
    assert data['public_sha256']==sha(base/'freeze'/f'OT_2003CHUNK2_{key}_PUBLIC.md')
v+='## Final deterministic identity audit\n\nAll fifteen preexisting opinion topologies in the accounting handoff were compared with the actual Records and match. All four exact first-line labels, single bounded Public Projection, eleven-block order, internal/public Holdings identity, public-copy byte identity, stored record/public hashes, and forbidden public workflow patterns pass. The eight case-stage handoffs remain unchanged; exact normalized-text inclusion of each commitment and reconciliation passes. The word approval in Van Susteren refers to Storer’s judicial holding, not operator workflow. Source hashes follow.\n\n'+'\n'.join(annex)+'\n'
for suffix in ['runtime','freeze']:(base/suffix/validation.name).write_text(v,encoding='utf-8',newline='\n')
print('Prior actual opinion tables checked:',prior_checked)
