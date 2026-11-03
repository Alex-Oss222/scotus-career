from pathlib import Path
import re, hashlib

ROOT=Path(__file__).resolve().parents[4]
TERM=ROOT/'terms/OT1999'
raw=(TERM/'runtime/OT_1999CHUNK7_NEUTRAL.md').read_text(encoding='utf-8')
tool=(TERM/'entering-law/OT_1999CHUNK7_A_TOOL_COPY.md').read_text(encoding='utf-8')
selected={
 'federal-courts':['Stewart v. Martinez-Villareal','Lujan v. Defenders','Citizens for a Better Environment v. Steel','Felker v. Turpin','Triestman v. United States','In re Dorsainvil','Bousley v. United States','Schlup v. Delo','College Savings Bank v. Florida','Florida Prepaid Postsecondary','Adarand Constructors'],
 'bankruptcy':['Patterson v. Shumate','Taylor v. Freeland','Dewsnup v. Timm','United States v. Noland','United States v. Reorganized','Pension Benefit Guaranty Corporation v. CF&I','United States v. Ron Pair'],
 'civil-rights':['Adarand Constructors','Hopwood v. Texas'],
 'criminal-procedure':['Bailey v. United States','Carlisle v. United States','Stewart v. Martinez'],
 'labor-and-employment':['Mertens v. Hewitt'],
 'administrative-law':['Director, Office of Workers’ Compensation Programs v. Greenwich'],
}
parts=['# OT1999 chunk 7 — entering law A','',
'Derived verbatim reading copy, selected from build_entering_law.py output. This slice changes no law. The generated full tool copy is retained as [copy receipt](OT_1999CHUNK7_A_TOOL_COPY.md). Canonical holdings and standards control; relevant effective current-term public law is copied below from the sanitized neutral projection.','',
'**Chronology:** Vermont Agency and Barrett use the law effective before May 22, 2000. Uncoordinated Geier, Jones and Playboy decisions of May 22 supply none of their entering law. Eisenberg and Hartford use law effective before May 30, including earlier effective law; no same-day chunk 7 decision supplies another May 30 decision’s law. Raleigh factual material is routed for fresh validation. No Ohler framing is supplied here.','']
for slug,qs in selected.items():
 marker='## Holdings volume: '+slug
 a=tool.index(marker);b=tool.find('\n## Holdings volume:',a+len(marker));c=tool.find('\n## Standards and Tests selection:',a+len(marker))
 ends=[x for x in [b,c] if x>=0];block=tool[a:min(ends) if ends else len(tool)]
 lines=block.splitlines();starts=[i for i,l in enumerate(lines) if l.startswith('#### ')]
 for i in starts:
  if not any(q in lines[i] for q in qs):continue
  end=next((j for j in range(i+1,len(lines)) if re.match(r'^#{1,4} ',lines[j])),len(lines))
  txt='\n'.join(lines[i:end]).strip()
  parts+=['## '+lines[i][5:],f'Source: [canonical {slug} volume](../../../state/holdings/{slug}.md).','',txt,'']
a=tool.index('## Standards and Tests selection:')
parts+=['## Exact reusable standards and institutional setting','',tool[a:].strip(),'']
proj=(TERM/'workspace/neutral-projection.md').read_text(encoding='utf-8')
paras=proj.split('\n\n')
keys=['- **Texas v. Lesage','- **Kimel /','- **Friends of the Earth v. Laidlaw','**Adarand Constructors, Inc. v. Slater','- **O\'Connor, joined by Scalia, Kennedy and Thomas, Kimel','- **Thomas, joined by Kennedy, Kimel','- **Stevens, Laidlaw concurrence','- **Scalia, joined by Thomas, Laidlaw dissent']
parts+=['## Effective current-term law and published positions','', 'Source: [Current-Term Neutral Projection](../workspace/neutral-projection.md). Public positions only; these are not new commitment instructions.','']
for p in paras:
 if any(p.startswith(k) for k in keys):parts +=[p,'']
lines=proj.splitlines()
for key in ['### Slack v. McDaniel — 2000-04-26','### Christensen v. Harris County — 2000-05-01']:
 for i,l in enumerate(lines):
  if l==key:
   end=next((j for j in range(i+1,len(lines)) if re.match(r'^#{1,3} ',lines[j])),len(lines))
   parts += ['\n'.join(lines[i:end]).strip(),'']
(TERM/'entering-law/OT_1999CHUNK7_A.md').write_text('\n'.join(parts).rstrip()+'\n',encoding='utf-8')
chunks=raw.split('# STONE PRE-VOTE CASE BRIEF')
copies=[]
for i in [1,3,4,6]: copies.append('# STONE PRE-VOTE CASE BRIEF'+chunks[i])
(TERM/'freeze/OT_1999CHUNK7_NEUTRAL_A_SOURCE_COPY.md').write_text('# Mechanically copied neutral source sections — A\n\n'+''.join(copies),encoding='utf-8')
print('Built bounded entering-law copy and four neutral source sections; source SHA256',hashlib.sha256(raw.encode()).hexdigest())
