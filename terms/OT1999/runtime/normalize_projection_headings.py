from pathlib import Path
import re
from assembly_record_writer import BLOCKS
root=Path(__file__).resolve().parents[1]
changed=[]
for p in (root/'records').glob('*.md'):
    s=p.read_text(encoding='utf-8')
    before,proj=s.split('## Public Projection\n',1)
    original=proj
    for block in BLOCKS:
        proj=proj.replace('\n### '+block+'\n','\n## '+block+'\n')
    assert re.findall(r'^## (.+)$',proj,re.M)==BLOCKS,p
    assert original.replace('\n### ','\n## ')==proj,p
    if proj!=original:
        p.write_text(before+'## Public Projection\n'+proj,encoding='utf-8')
        changed.append(p.name)
note=root/'runtime'/'OT_1999CHUNK1_ASSEMBLY_VALIDATION.md'
note.write_text('# OT1999 chunk 1 — assembly validation\n\nBefore coordinated chunk validation, the eleven Public Projection block headings in the first '+str(len(changed))+' Records were mechanically normalized from level three to level two to match the native checker and builder contract. Only heading depth changed; all adjudicative text, votes, joins, authors, remedies and assignment counts remained byte-identical. This is a structural precommit validation fix, not a completed-adjudication correction. The writer now emits the required level-two headings.\n\nAffected files:\n\n'+'\n'.join('- '+x for x in changed)+'\n',encoding='utf-8')
print('Normalized headings only in',len(changed),'Records; substantive bytes unchanged.')
