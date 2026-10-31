import json
from pathlib import Path
root=Path(__file__).parent
p=root/'assembly_steamfitters.json'
d=json.loads(p.read_text())
d['blocks']['Source Notes']=d['blocks']['Source Notes'].replace(', and no Supreme Court docket number is supplied.','.')
d['blocks']['Source Notes']=d['blocks']['Source Notes'].replace('Its separate no-property-injury concern is not the ground affirmed here.', "The District Court's no-property-injury rationale, questioned by the Third Circuit, is not adopted.")
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
p=root/'assembly_kimel.json'
d=json.loads(p.read_text())
d['blocks']['Holdings']=d['blocks']['Holdings'].replace('the prohibition on retaliation for protected FLSA complaints, proceedings or testimony','the prohibition on retaliation')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print('Removed nonmaterial operator wording and kept statutory cross-reference precise.')
