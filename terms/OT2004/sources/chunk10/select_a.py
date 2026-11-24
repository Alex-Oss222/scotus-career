import os, sys, re, subprocess
from pathlib import Path
os.environ['PYTHONDONTWRITEBYTECODE']='1'
sys.dont_write_bytecode=True
root=Path.cwd()
sys.path.insert(0,str(root/'tools'))
from build_entering_law import take_heading
out=root/'terms/OT2004/entering-law/OT_2004CHUNK10_A.md'
standards=['Lemon test','Equal religious eligibility for controlled secular educational services','Devotional study conditions on individual scholarships','Procedural correction and successive habeas applications','One-year state-custody habeas filing period','Second or successive state-custody habeas applications','Recall reopening completed state-prisoner habeas merits','Supplemental jurisdiction over related state administrative review','Diversity cured before trial after erroneous removal','Acquisition for Amtrak service and the presumption of need','Delegated Customs interpretation and independent tariff review']
cmd=[sys.executable,'tools/build_entering_law.py',str(out)]
for s in standards: cmd += ['--standard-heading',s]
subprocess.run(cmd,check=True)
parts=[out.read_text(encoding='utf-8')]
selected={
'administrative-law':['Yellow Transportation, Inc. v. Michigan, 537 U.S. 36'],
'first-amendment':['Strout v. Albanese','Zelman v. Simmons-Harris, 536 U.S. 639','Locke v. Davey, 540 U.S. 712','Freedom From Religion Foundation, Inc. v. McCallum (judgment below: 324 F.3d 880) — First Amendment, OT2003'],
'property-and-economic-rights':['National Railroad Passenger Corp. v. Boston & Maine Corp., 503 U.S. 407 (1992)'],
'federal-courts-habeas':["Abdur'Rahman v. Bell, 537 U.S. 88"],
'criminal-procedure':['Artuz v. Bennett, 531 U.S. 4'],
'federal-courts':['City of Chicago v. International College of Surgeons','Grupo Dataflux v. Atlas Global Group, L.P., 541 U.S. 567 (2004)']}
for volume,titles in selected.items():
    src=(root/'state/holdings'/f'{volume}.md').read_text(encoding='utf-8')
    for title in titles:
        parts+=['\n## Selected opening holding — '+volume+'\n',take_heading(src,title)]
src=(root/'terms/OT2004/workspace/neutral-projection.md').read_text(encoding='utf-8')
lines=src.splitlines()
names=['Kowalski v. Tesmer','Rhines v. Weber','Pace v. DiGuglielmo','Lingle v. Chevron','Grable & Sons','San Remo Hotel']
starts=[i for i,l in enumerate(lines) if re.match(r'^### ',l)]
for p,i in enumerate(starts):
    if any(name in lines[i] for name in names):
        end=next((j for j in range(i+1,len(lines)) if re.match(r'^#{1,3} ',lines[j])),len(lines))
        section='\n'.join(lines[i:end])
        if '**Judgment & Remedy.**' not in section:
            parts+=['\n## Current-term public law or published positions\n',section]
for line in lines:
    if line.startswith('- **') and 'Kowalski v. Tesmer' in line:
        parts+=['\n## Current-term Kowalski rule\n',line]
public=[('OT2002','OT_2002CHUNK2.md',['Yellow Transportation, Inc. v. Michigan, No. 01-270',"Abdur'Rahman v. Bell, No. 01-9094"]),('OT2003','OT_2003CHUNK4.md',['Locke v. Davey, No. 02-1315','Freedom From Religion Foundation, Inc. v. McCallum']),('OT2003','OT_2003CHUNK6.md',['Grupo Dataflux v. Atlas Global Group, L.P., No. 02-1689'])]
for term,filename,titles in public:
    src=(root/'terms'/term/'output'/filename).read_text(encoding='utf-8')
    for title in titles:
        entry=take_heading(src,title)
        selected_parts=[p for p in re.split(r'(?m)(?=^#### )',entry) if p.startswith('#### Opinion') or p.startswith('#### Separate')]
        parts+=['\n## Published prior-term position source: '+term+' '+filename+'; '+title+'\n','\n'.join(selected_parts)]
extra=[('OT2000','OT_2000CHUNK8.md','Palazzolo v. Rhode Island, No. 99-2047'),('OT2001','OT_2001CHUNK4.md','Tahoe-Sierra Preservation Council, Inc. v. Tahoe Regional Planning Agency, No. 00-1167'),('OT1997','OT_1997CHUNK2.md','City of Chicago v. International College of Surgeons, No. 96-910')]
for term,filename,title in extra:
    entry=take_heading((root/'terms'/term/'output'/filename).read_text(encoding='utf-8'),title)
    selected_parts=[p for p in re.split(r'(?m)(?=^#### )',entry) if p.startswith('#### Opinion') or p.startswith('#### Separate')]
    parts+=['\n## Additional published positions: '+term+' '+filename+'; '+title+'\n','\n'.join(selected_parts)]
for name in ['uscode2000-28-sec1367.txt','uscode2000-49-sec14504.txt','uscode2000-28-sec2244.txt']:
    source=(root/'terms/OT2004/sources/chunk10'/name).read_text(encoding='utf-8')
    # Exact source quotation; historical notes excluded after the current operative text.
    source=source.split('Historical and Revision Notes')[0].split('Prior Provisions')[0]
    parts+=['\n## Enacted text: '+name+'\n',source]
text='\n\n'.join(parts)
text=re.sub(r'\[([^\]]+)\]\((?!https?://)[^)]+\)',r'\1',text)
for forbidden in ['One'+'Drive','Git'+'Hub']:
    if forbidden.casefold() in text.casefold(): raise RuntimeError('Disallowed source text')
out.write_text(text,encoding='utf-8')
print('Wrote',out.name,'words',len(text.split()))
