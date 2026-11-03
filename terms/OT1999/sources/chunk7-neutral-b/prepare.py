from pathlib import Path
import re, subprocess, sys, hashlib

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / 'terms/OT1999/entering-law/OT_1999CHUNK7_B.md'
STANDARDS = [
 'Jury determination of criminal materiality',
 'Aggravated unlawful-reentry elements and authorized maximum',
 'Original armed carjacking and cumulative firearm punishment',
 'APA limits on exhaustion of superior-agency appeals',
 'Judicial exhaustion and damages-only federal prison medical-care claims',
 'Independent foreign prosecution and compelled testimony',
 'Voting Rights Act §5 coverage of reallocations of governing authority',
 'Section 2 challenges to governing-body size',
 'Section 2 fragmentation, state districting choice and influence claims',
 'Section 2 opportunity and remedies in judicial elections',
 'Selective racial restructuring of access to lawful remedies',
 'ERISA equitable categories and nonfiduciary compensation',
 'Fiduciary benefit communications and deliberate disloyal deception',
]
args = [sys.executable,str(ROOT/'tools/build_entering_law.py'),str(OUT),'--root',str(ROOT),'--standing-heading','1. Current Court']
for s in STANDARDS: args += ['--standard-heading',s]
subprocess.run(args,check=True)

def exact_case_sections(path, wanted):
    txt=path.read_text(encoding='utf-8')
    chunks=re.split(r'(?=^#### )',txt,flags=re.M)
    return [re.split(r'^### ',c,flags=re.M)[0].strip() for c in chunks if c.splitlines()[0] in wanted]

selections={
 'criminal-procedure': ['#### United States v. Gaudin','#### Almendarez-Torres v. United States','#### United States v. Balsys','#### Jones v. United States'],
 'civil-rights': ['#### Presley v. Etowah County Commission; Mack v. Russell County Commission, 502 U.S. 491 (1992)'],
 'election-law': ['#### Holder v. Hall','#### Valdespino v. Alamo Heights Independent School District'],
 'labor-and-employment': ['#### Mertens v. Hewitt Associates, 508 U.S. 248 (1993)','#### Varity Corp. v. Howe, 516 U.S. 489'],
 'administrative-law': ['#### Darby v. Cisneros, 509 U.S. 137 (1993)'],
}
parts=[OUT.read_text(encoding='utf-8')]
for vol,heads in selections.items():
    file=ROOT/f'state/holdings/{vol}.md'
    chunks=exact_case_sections(file,heads)
    if vol=='criminal-procedure': chunks=[c for c in chunks if not c.startswith('#### Jones') or 'No. 97-6203.' in c]
    parts += [f'\n## Canonical Holdings selections: {vol}\n\nSource: [canonical volume](../../../state/holdings/{vol}.md). Mechanically copied.\n',*chunks]
projection=(ROOT/'terms/OT1999/workspace/neutral-projection.md').read_text(encoding='utf-8')
parts += ['\n## Current-term sanitized selections\n\nSource: [Current-Term Neutral Projection](../workspace/neutral-projection.md); current law and published positions only.']
for c in re.split(r'(?=^### )',projection,flags=re.M):
    h=c.splitlines()[0]
    if any(h.startswith('### '+x) for x in ['Shalala v. Illinois Council','Rice v. Cayetano','Village of Willowbrook v. Olech','United States v. Morrison']):
        parts.append(re.split(r'^## ',c,flags=re.M)[0].strip())
OUT.write_text('\n\n'.join(parts)+'\n',encoding='utf-8')

src=ROOT/'terms/OT1999/runtime/OT_1999CHUNK7_NEUTRAL.md'
txt=src.read_text(encoding='utf-8')
selected=[]
for c in txt.split('# STONE PRE-VOTE CASE BRIEF'):
    if re.search(r'^\*(Castillo v\. United States|Sims v\. Apfel|United States v\. Hubbell|Mixon v\. Ohio|Harris Trust and Savings Bank v\. Salomon Smith Barney Inc\.)\*',c,re.M):
        selected.append('# STONE PRE-VOTE CASE BRIEF'+c)
assert len(selected)==5
base=ROOT/'terms/OT1999/freeze/OT_1999CHUNK7_NEUTRAL_B_SOURCE.md'
base.write_text('# Mechanically copied neutral source — five clean B matters\n\nSource SHA-256: '+hashlib.sha256(src.read_bytes()).hexdigest()+'\n\n'+''.join(selected),encoding='utf-8')
print('Built',OUT.relative_to(ROOT),len(OUT.read_bytes()),'bytes; copied',len(selected),'source sections.')
