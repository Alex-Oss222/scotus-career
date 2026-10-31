import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
old="Benefit-plan alternatives require at least equal payment or cost for older workers under the specified regulation, or a voluntary early-retirement incentive consistent with the Act's purposes;"
new="For each benefit or benefit package under a bona fide employee benefit plan, the actual payment made or cost incurred for an older worker must be no less than that for a younger worker, as permissible under 29 C.F.R. §1625.10 as in effect on June 22, 1989; the separate alternative is a voluntary early-retirement incentive plan consistent with the Act's purposes;"
old2='They neither infer constitutional validity from state-law permission nor treat unrecovered legislative sources as proof that Congress heard nothing.'
new2='They do not infer constitutional validity from state-law permission. The identified recitations are not an exhaustive congressional record, and the dissent does not conclude that Congress heard no evidence.'
p=root/'records'/'kimel-v-florida-board-of-regents_merits_2000-01-11.md'
s=p.read_text(encoding='utf-8')
before,proj=s.split('## Public Projection\n',1)
assert proj.count(old)==1 and proj.count(old2)==1
proj=proj.replace(old,new).replace(old2,new2)
p.write_text(before+'## Public Projection\n'+proj,encoding='utf-8')
p=root/'runtime'/'assembly_kimel.json'
d=json.loads(p.read_text())
d['blocks']['Separate Writings']=d['blocks']['Separate Writings'].replace(old,new).replace(old2,new2)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
note=root/'runtime'/'OT_1999CHUNK1_ASSEMBLY_VALIDATION.md'
with note.open('a',encoding='utf-8') as f:
    f.write('\nPrecommit Kimel completeness review: expanded the existing benefit-plan qualification to identify the bona fide plan, each benefit/package, actual older/younger payment or cost comparison, and 29 C.F.R. §1625.10 as in effect June 22, 1989. The separate voluntary-incentive route and all hiring, retirement and burden limits remain. Replaced public research-status wording with the legal limitation that the identified legislative recitations are not exhaustive and the dissent does not infer absence of evidence. These corrections project the already frozen statutory and evidentiary basis; no vote, joined rule, rationale, disposition, assignment or remedy changes.\n')
print('Kimel public completeness repaired from existing frozen basis; internal kernel and votes unchanged.')
