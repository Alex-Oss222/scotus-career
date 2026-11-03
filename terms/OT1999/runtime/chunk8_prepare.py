from pathlib import Path
import importlib.util
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1999'
sys.dont_write_bytecode = True
def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'tools' / (name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

areas = {
 'A': ['labor-and-employment','criminal-procedure','constitutional-structure','federal-courts','civil-rights','property-and-economic-rights'],
 'B': ['federal-courts','constitutional-structure','first-amendment','federal-indian-law','property-and-economic-rights','civil-rights'],
 'C': ['criminal-procedure','federal-courts','constitutional-structure'],
}
terms = {
 'A': r'Varity|Hughes Aircraft|Lockheed|Hicks|Hazen Paper|Simmons|\bO.Dell|Allridge|Mosley|Cedar Rapids|College Savings|Florida Prepaid|Boerne|Seminole Tribe|Coeur|Lane v. Pe.a|John Hancock|Curtiss.Wright|Mertens|Peacock|Travelers|Consolidated Coin|Brecht|O.Neal|Lindh|Alden|Almendarez|Jones v. United States',
 'B': r'Robertson|Morgan Stanley|Plaut|Agostini|Sacramento|Glucksberg|Young v. Harper|Lee v. Weisman|Pinette|Barclays|Myrick|Boston Harbor|Arizona v. California|United States v. Sioux|Rufo|Landgraf|Ingebretsen|Tanford|Bronx|Rouse|Benjamin|Plyler|Hadix|Gavin',
 'C': r'Stansbury|Davis v. United States|Thompson v. Keohane|Gaudin|Almendarez|Jones v. United States|Neder|Withrow|Brecht|Sullivan v. Louisiana|Johnson v. United States|Alvarez.Sanchez|Boerne',
}
standards = {
 'A': ['Parole ineligibility as an answer to future-danger evidence','Capital instructions on legally included lesser offenses','Commercial participation and State consent to federal suit','Article I enforcement against States in federal court','Necessary nonphysician school-health services under IDEA','ERISA sponsor design, fiduciary implementation and genuine benefit payments','Fiduciary benefit communications and deliberate disloyal deception'],
 'B': ['Prison-conditions prospective relief','Prison-conditions termination motions and automatic stays','Present legal change and prospective relief from an adjudicated injunction','Official graduation worship and independent religious pressure','Private religious viewpoints in public forums and printing benefits','Revocation of existing parole-like community liberty','Proprietary public purchases and labor preemption','Worldwide unitary-income taxation and foreign-commerce safeguards'],
 'C': ['Communicated circumstances and Miranda custody','Clarifying a possible present request for interrogation counsel','Independent Miranda custody review under the former habeas statute','Jury determination of criminal materiality','Aggravated unlawful-reentry elements and authorized maximum','Renewed proof of noncapital recidivist status'],
}
bel = module('build_entering_law')
for group in areas:
    target = TERM / 'entering-law' / f'OT_1999CHUNK8_{group}_TOOL_COPY.md'
    argv = ['build_entering_law.py',str(target)]
    for area in areas[group]: argv += ['--holdings-area',area]
    for heading in standards[group]: argv += ['--standard-heading',heading]
    argv += ['--standing-heading','1. Current Court','--standing-heading','2. Current Circuit Allotments']
    old=sys.argv;sys.argv=argv
    try: bel.main()
    finally: sys.argv=old
    raw=target.read_text(encoding='utf-8')
    selections=[]
    for m in re.finditer(r'^#### (.+)$',raw,re.M):
        if re.search(terms[group],m.group(1),re.I):
            tail=raw[m.start():]
            following=re.search(r'^#{1,4} ',tail[m.end()-m.start():],re.M)
            end=m.end()-m.start()+following.start() if following else len(tail)
            selections.append(tail[:end].strip())
    for h in standards[group]: selections.append(bel.take_heading(raw,'Standards and Tests selection: '+h))
    for h in ['1. Current Court','2. Current Circuit Allotments']:
        selections.append(bel.take_heading(raw,'Standing State selection: '+h))
    out=TERM/'entering-law'/f'OT_1999CHUNK8_{group}.md'
    out.write_text('# OT1999 chunk 8 entering-law reading selections\n\nVerbatim selections from the mechanically generated '+target.name+'. Effective current-term public law supplements this opening baseline. Uncoordinated same-date events do not supply entering law to each other.\n\n'+'\n\n'.join(selections)+'\n',encoding='utf-8')
    print(group,len(selections),'selections')

for name in ['ledger.md','manifest.md','continuity.md','neutral-projection.md']:
    p=TERM/'runtime'/('OT_1999CHUNK8_OPENING_'+name)
    if not p.exists(): p.write_bytes((TERM/'workspace'/name).read_bytes())

current={
 'A':r'kimel|weeks-v|williams-v-taylor|edwards-v|nelson-v|garner-v|carmell|weisgram|morrison',
 'B':r'geier|saenz-v|paul-p-v|fda-v|christensen|vermont-agency',
 'C':r'castillo|hubbell|ohler|johnson-v-united|smith-v-robbins',
}
for group,pattern in current.items():
    parts=['# Effective current-term public law selections','', 'Public Projection only. No audit or private material.']
    for p in sorted((TERM/'records').glob('*.md')):
        if not re.search(pattern,p.name): continue
        text=p.read_text(encoding='utf-8')
        if '## Public Projection' not in text: continue
        date=re.search(r'\d{4}-\d{2}-\d{2}',p.name).group()
        if date >= ('2000-06-12' if group=='A' else '2000-06-19' if group=='B' else '2000-06-26'): continue
        parts += ['', '## '+p.stem,'',text.split('## Public Projection',1)[1].strip()]
    (TERM/'entering-law'/f'OT_1999CHUNK8_{group}_CURRENT_PUBLIC.md').write_text('\n'.join(parts)+'\n',encoding='utf-8')
