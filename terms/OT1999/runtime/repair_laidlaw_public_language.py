import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
changes={
'or treating missing research copies as failed proof.':'or resting their objection on litigant default.',
'supplies no separate recovered decree.':'does not establish a separate declaratory decree in the record.'
}
p=root/'records'/'friends-of-the-earth-v-laidlaw_merits_2000-01-12.md'
s=p.read_text(encoding='utf-8')
before,proj=s.split('## Public Projection\n',1)
for old,new in changes.items():
    assert proj.count(old)==1,old
    proj=proj.replace(old,new)
p.write_text(before+'## Public Projection\n'+proj,encoding='utf-8')
p=root/'runtime'/'assembly_laidlaw.json'
d=json.loads(p.read_text())
for block in ['Holdings','Separate Writings']:
    for old,new in changes.items():d['blocks'][block]=d['blocks'][block].replace(old,new)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
with (root/'runtime'/'OT_1999CHUNK1_ASSEMBLY_VALIDATION.md').open('a',encoding='utf-8') as f:
    f.write('\nPrecommit Laidlaw public-language review: replaced retrieval-status phrasing in the dissent with its evidence-based, nondefault ground, and stated the declaratory-relief limit as absence of an established separate declaratory decree in the record. Actual source-recovery limits remain in internal provenance and Source Notes. No law, opinion join, vote, remedy or assignment changes.\n')
print('Laidlaw public workflow wording repaired; law and remedy unchanged.')
