from pathlib import Path
import hashlib,json,re
base=Path('terms/OT2003')
old='Its distinct fisheries provisions do not erase that preservation. Article VIII bars unilateral alteration, and the congressional consent retains federal rights, jurisdiction and commerce power.'
new='Article VII §2 continues the specified Maryland fisheries laws as of December 1, 1958, subject to authorized Commission change; §3 continued existing fishing licenses for six months before abrogation. Neither alters §1. Article IX replaced the former Compact sixty days after the final legally necessary act. Article VIII bars unilateral alteration. Congress retains federal rights, jurisdiction and commerce power and reserves authority to alter, amend or repeal its consent.'
virnote=' Article VII §2 separately continues the specified Maryland fisheries laws as of December 1, 1958, subject to authorized Commission change; §3 continued existing fishing licenses for six months before abrogation. Article IX replaced the former Compact sixty days after the final legally necessary act. Congress expressly reserved its authority to alter, amend or repeal the consent resolution.'
vannote=' The record supplies no formal party resolution or finding that an alternative candidacy route offered equivalent electoral prospects.'
vp=base/'records/virginia_v_maryland_merits_2003-12-09.md'
s=vp.read_text(encoding='utf-8')
assert s.count(old)==2 and s.count(virnote)==1
s=s.replace(old,new).replace('The supported account places official awareness in 1973 and protests from 1976','The record places official awareness in 1973 and protests from 1976').replace(virnote,'')
vp.write_text(s,encoding='utf-8',newline='\n')
p=base/'records/van_susteren_v_jones_merits_2003-12-04.md'
s=p.read_text(encoding='utf-8');assert s.count(vannote)==1
p.write_text(s.replace(vannote,''),encoding='utf-8',newline='\n')
keys={'RAYTHEON':'raytheon_co_v_hernandez_merits_2003-12-02.md','BANKS':'united_states_v_banks_merits_2003-12-02.md','VAN_SUSTEREN':'van_susteren_v_jones_merits_2003-12-04.md','VIRGINIA':'virginia_v_maryland_merits_2003-12-09.md'}
v=base/'runtime/OT_2003CHUNK2_B_FIRST_ASSEMBLY_VALIDATION.md'
val=v.read_text(encoding='utf-8')
for key,f in keys.items():
    p=base/'records'/f;s=p.read_text(encoding='utf-8');pub=s.split('## Public Projection\n\n',1)[1]
    for suffix in ['runtime','freeze']:(base/suffix/f'OT_2003CHUNK2_{key}_PUBLIC.md').write_text(pub,encoding='utf-8',newline='\n')
    assert len(re.findall(r'^## (.+)$',pub,re.M))==11
    h=re.search(r'^## Holdings\n(.*?)(?=^## Precedent Treatment)',pub,re.M|re.S).group(1).strip()
    assert h in s.split('## Adaptive audit annex',1)[0]
    wc=[len(m.group(1).split()) for m in re.finditer(r'\*\*Controlling explanation:\*\*\s*(.*?)(?=\n### |\n\*\*Authority:|\Z)',h,re.S)]
    assert all(n<=350 for n in wc)
    m=re.search(r'^## '+key+r'\n\n(.*?)(?=^## |\Z)',val,re.M|re.S)
    data=json.loads(m.group(1));data['record_sha256']=hashlib.sha256(p.read_bytes()).hexdigest();data['public_sha256']=hashlib.sha256(pub.encode()).hexdigest();data['explanation_words']=wc
    val=val[:m.start(1)]+json.dumps(data,ensure_ascii=False,indent=2)+'\n\n'+val[m.end(1):]
    print(key,wc,data['public_sha256'])
for suffix in ['runtime','freeze']:(base/suffix/v.name).write_text(val,encoding='utf-8',newline='\n')
p=base/'runtime/chunk2_b_first_decisions.py';s=p.read_text(encoding='utf-8')
s=s.replace(old,new).replace('The supported account places official awareness in 1973 and protests from 1976','The record places official awareness in 1973 and protests from 1976').replace(virnote,'').replace(vannote,'')
p.write_text(s,encoding='utf-8',newline='\n')
