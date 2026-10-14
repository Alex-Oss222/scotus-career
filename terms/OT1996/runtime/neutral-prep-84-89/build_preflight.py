from pathlib import Path
import re, hashlib, json, shutil
import importlib.util

ROOT=Path(__file__).resolve().parents[4]
TERM=ROOT/'terms/OT1996'
OUT=TERM/'runtime/neutral-prep-84-89'
neutral=TERM/'runtime/OT_1996CHUNK8_NEUTRAL.md'
projection=TERM/'workspace/neutral-projection.md'
spec=importlib.util.spec_from_file_location('slice_builder',ROOT/'tools/build_entering_law.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)

def write(name,text):
    (OUT/name).write_text(text.rstrip()+'\n',encoding='utf-8')

def section(text,start,end):
    i=text.index(start); j=text.index(end,i+len(start));return text[i:j].rstrip()

p=neutral.read_text(encoding='utf-8')
cases=[]
for n in range(84,90):
    cases.append(re.search(r'^# '+str(n)+r'\..*?(?=^# \d+\. |\Z)',p,re.M|re.S).group(0).rstrip())
write('APPROVED_NEUTRAL_84_89.md','# Approved neutral passages — verbatim mechanical extraction\n\n'+'\n\n'.join(cases))

selections={
 'election-law':['Johnson v. De Grandy, 512 U.S. 997','Morse v. Republican Party of Virginia, 517 U.S. 186','Shaw v. Reno, 509 U.S. 630 (1993)'],
 'constitutional-structure':['West Lynn Creamery, Inc. v. Healy, 512 U.S. 186','Oregon Waste Systems, Inc. v. Department of Environmental Quality and Columbia Resource Co. v. Environmental Quality Commission, 511 U.S. 93','C & A Carbone, Inc. v. Town of Clarkstown, 511 U.S. 383','Fulton Corp. v. Faulkner, 516 U.S. 325','Weiss v. United States, 510 U.S. 163','Ryder v. United States'],
 'criminal-procedure':['United States v. Wellons','United States v. Pinson','Stinson v. United States, 508 U.S. 36 (1993)','Koon v. United States; Powell v. United States, 518 U.S. 81'],
 'federal-courts':['Landgraf v. USI Film Products, 511 U.S. 244','Felker v. Turpin, 518 U.S. 651 (1996)'],
 'civil-rights':['Heck v. Humphrey, 512 U.S. 477','Sandin v. Conner'],
 'immigration':['INS v. Doherty, 502 U.S. 314 (1992)','Reno v. Flores, 507 U.S. 292 (1993)']
}
parts=['# Focused opening-law reading copy','Mechanically copied selected headings. The full operator-built slice and cited state authorities control.']
for area,titles in selections.items():
    text=(ROOT/'state/holdings'/f'{area}.md').read_text(encoding='utf-8')
    for title in titles:
        parts += [f'## Source: state/holdings/{area}.md',builder.take_heading(text,title)]
full=(TERM/'entering-law/OT_1996CHUNK8_84_89.md').read_text(encoding='utf-8')
parts.append(full[full.index('## Standards and Tests selection:'):])
write('FOCUSED_OPENING_LAW.md','\n\n'.join(parts))

p=projection.read_text(encoding='utf-8')
parts=['# Current-term neutral law selected for matters 84–89','Verbatim projection extracts, not raw Records. Same-day May 12 peer decisions are not entering law for matters 84–86.']
parts.append(p[:p.index('## Current-term controlling law')] if '## Current-term controlling law' in p else p[:p.index('### 1996-')])
for part in re.split(r'(?=^### )',p,flags=re.M):
    if part.startswith('### ') and any(k in part.splitlines()[0] for k in ['Yueh-Shaio Yang','Young v. Fordice','Chandler v.','Richards v.','Young v. Harper','Blessing v.']):
        parts.append(part.rstrip())
write('CURRENT_TERM_LAW.md','\n\n'.join(parts))

p=(OUT/'USCODE_1994_title49.raw.txt').read_text(encoding='utf-8')
parts=['# Official statutory text — Edmond','Source: https://www.govinfo.gov/content/pkg/USCODE-1994-title49/html/USCODE-1994-title49.htm',section(p,'§323. Personnel','§324. Members')]
p=(OUT/'USCODE_1994_title10.raw.txt').read_text(encoding='utf-8')
parts.append('Source: https://www.govinfo.gov/content/pkg/USCODE-1994-title10/html/USCODE-1994-title10.htm')
for a,b in [('§866. Art. 66.','§867. Art. 67.'),('§867. Art. 67.','§867a.')]:
    s=section(p,a,b)
    # Statute and enactment citation through the first history heading, not the unrelated revision notes.
    parts.append(s.split('Historical and Revision Notes')[0].rstrip())
write('EDMOND_STATUTES.md','\n\n'.join(parts))
p=(OUT/'AEDPA.raw.txt').read_text(encoding='utf-8')
write('AEDPA_440_TEXT.md','# AEDPA §440 — official enacted text\n\nSource: https://www.govinfo.gov/content/pkg/PLAW-104publ132/html/PLAW-104publ132.htm\n\n'+section(p,'SEC. 440. CRIMINAL ALIEN REMOVAL.','SEC. 441.'))

receipt={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest() for path in [neutral,projection,ROOT/'foundation/ENGINE.md',ROOT/'foundation/COURT_COMPOSITION.md',TERM/'entering-law/OT_1996CHUNK8_84_89.md']}
write('INPUT_SHA256.json',json.dumps(receipt,indent=2))
print('Mechanical neutral passages and law/statute extracts written.')
