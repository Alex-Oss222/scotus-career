from pathlib import Path
import json,re
p=Path('terms/OT2002/runtime/chunk13-drafts')
specs=json.loads((p/'B_specs.json').read_text(encoding='utf-8'))
names={
'Bechhoefer_v_United_States_Department_of_Justice_DEA_dismissal_2003-06-16.md':'Bechhoefer-v-United-States-Department-of-Justice-DEA_dismissal_2003-06-16.md',
'Heimmermann_v_First_Union_Mortgage_Corp_merits_2003-06-16.md':'Heimmermann-v-First-Union-Mortgage-Corp_merits_2003-06-16.md',
'Fairley_v_Luman_merits_2003-06-23.md':'Fairley-v-Luman_merits_2003-06-23.md',
'Krimstock_v_Kelly_merits_2003-06-23.md':'Krimstock-v-Kelly_merits_2003-06-23.md'}
keys=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
for s in specs:
    f=p/s['file']
    text=f.read_text(encoding='utf-8')
    internal,pub=text.split('## Public Projection\n',1)
    for key in keys:
        pub=pub.replace('### '+key+'\n','## '+key+'\n')
    pub=pub.replace('Decided on the merits submissions; no separate oral-argument date is stated.','Decided on the merits submissions.')
    pub=pub.replace(' The §8(b) issue is outside the granted yield-spread-premium questions.','')
    pub=pub.replace(' The separate municipal Fourth Amendment theory is unnecessary to the judgment because this procedural-due-process ground fully supports the verdict.','')
    for prefix in ['B','H','F','K']:
        for n,roman in [(4,'IV'),(3,'III'),(2,'II'),(1,'I')]:
            pub=re.sub(r'\b'+prefix+str(n)+r'\b','Part '+roman,pub)
    new=names.get(s['file'],s['file'])
    (p/new).write_text(internal+'## Public Projection\n'+pub,encoding='utf-8')
    if new!=s['file']:
        f.unlink()
    s['file']=new
(p/'B_specs.json').write_text(json.dumps(specs,indent=2),encoding='utf-8')
for s in specs:
    text=(p/s['file']).read_text(encoding='utf-8')
    pub=text.split('## Public Projection\n',1)[1]
    hs=re.findall(r'^## (.+)$',pub,re.M)
    assert hs==keys,(s['file'],hs)
    assert not re.search(r'\b[BHFK][1-4](?:\b|-)',pub),s['file']
    assert text.count('__ASSIGNMENT_BLOCK__')==(1 if s['countable'] else 0)
    assert text.count('__PUBLICATION_STATUS__')==1
    assert 'no separate oral-argument date is stated' not in pub
    print(s['file'],len(text.split()),'words; projection and placeholder checks passed')
