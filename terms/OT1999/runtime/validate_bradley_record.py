from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
draft = root/'runtime/bradley-v-arkansas-department-of-education_merits_2000-06-12.draft.md'
dest = root/'records/bradley-v-arkansas-department-of-education_merits_2000-06-12.md'
text = draft.read_text(encoding='utf-8')
expected = ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
labels = ['Case and dockets','Event and date','Result','Version / lineage']
for line, label in zip(text.splitlines()[:4], labels):
    assert line.startswith('**'+label+':**'), (label,line)
internal, public = text.split('## Public Projection\n',1)
assert re.findall(r'^## (.+)$', public, re.M) == expected
ih = internal.split('## Controlling holdings\n',1)[1].split('\n## Precedent treatment',1)[0].strip()
ph = public.split('## Holdings\n',1)[1].split('\n## Precedent Treatment',1)[0].strip()
assert ih == ph
explanation = re.search(r'\*\*Controlling explanation:\*\* (.*?)(?=\n\*\*Operative qualifications)', ph,re.S)[1]
words = len(explanation.split())
assert words <= 350, words
names = ['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']
support = re.search(r'\*\*Supporting:\*\* (.+)',public)[1]
assert all(n in support for n in names)
table = public.split('## Opinion Topology',1)[1].split('## Holdings',1)[0]
row = [x for x in table.splitlines() if x.startswith('| Opinion of the Court |')]
assert len(row)==1
cells = [x.strip() for x in row[0].strip('|').split('|')]
assert cells[1]=='Thomas'
assert all(n in cells[2] for n in names if n!='Thomas') and 'Thomas' not in cells[2]
assert not re.search(r'GitHub|OneDrive|file://',text,re.I)
assert not re.search(r'simulat|approval|workflow|commit hash|October 31, 2026',public,re.I)
assert not dest.exists(), 'Never overwrite an existing adjudication'
receipt = {'case':'Bradley v. Arkansas Department of Education','event_date':'2000-06-12','labels':'pass','public_blocks':expected,'public_holdings_identity':'pass','judgment_supporters':names,'author':'Thomas','full_joins':[n for n in names if n!='Thomas'],'controlling_explanation_words':words,'duplicate_record_prevention':'pass','source_Stone_and_frozen_compatibility':'manually reviewed; no changed commitment or fallback','not_performed':['repository commitment','workspace integration','render-input generation','term-wide validation']}
(root/'freeze/OT_1999CHUNK8_BRADLEY_ASSEMBLY_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
dest.write_text(text,encoding='utf-8')
print(json.dumps({'durable_record':dest.name,'explanation_words':words,'validation':'pass'},indent=2))
