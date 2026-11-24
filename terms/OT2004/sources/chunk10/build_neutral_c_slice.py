from pathlib import Path
import sys,subprocess,re
sys.dont_write_bytecode=True
sys.path.insert(0,'tools')
from build_entering_law import take_heading
sel={'civil-rights':['Sandin v. Conner','Connecticut Department of Public Safety v. Doe, 538 U.S. 1','Doe v. District of Columbia'], 'federal-courts-habeas':['Calderon v. Thompson'], 'criminal-procedure':['Carlisle v. United States, 517 U.S. 416'], 'criminal-procedure-sentencing-and-capital':['Neal v. United States, 516 U.S. 284'], 'first-amendment':['Agostini v. Felton; Chancellor, Board of Education of the City of New York v. Felton','Freedom From Religion Foundation, Inc. v. City of Marshfield'], 'business-and-commercial-law':['A&M Records, Inc. v. Napster, Inc.'], 'administrative-law':['United States v. Mead Corp., 533 U.S. 218','National Cable & Telecommunications Assn., Inc. v. Gulf Power Co., 534 U.S. 327','Barnhart v. Walton, 535 U.S. 212','Yellow Transportation, Inc. v. Michigan, 537 U.S. 36','AT&T Corp. v. Iowa Utilities Board','Smiley v. Citibank (South Dakota), N.A., 517 U.S. 735']}
std=['Municipal responsibility and the underlying federal deprivation','Mandatory investigative procedures and substantive entitlements','Hearings for risk-based and conviction-based notification','Recall reopening completed state-prisoner habeas merits','Timely postverdict acquittal and limits on substitute authority','Lemon test','Municipal divestiture and continuing presentation of a religious display','Delegated Customs interpretation and independent tariff review','Persuasive weight of a nonbinding agency advisory interpretation','FCC implementation of local-competition duties','Telecommunications network elements and bounded access','Knowing material assistance and beneficial supervision of infringement','Function-specific copyright protections and injunction limits','Duration and trial-work conditions in initial disability entitlement','Federal interest classification and national-bank home-state charges','Separate statutory and Guidelines LSD quantities']
out=Path('terms/OT2004/entering-law/OT_2004CHUNK10_C.md')
args=[sys.executable,'tools/build_entering_law.py',str(out)]
for slug in sel: args += ['--holdings-area',slug]
for h in std: args += ['--standard-heading',h]
subprocess.run(args,check=True)
parts=['# Entering law — OT2004 chunk 10, matters 101–105','Derived reading copy only. Authority remains the selected Holdings and Standards entries and effective current-term decisions. Cutoff: before the uncoordinated June 27, 2005 events. Selection generated with build_entering_law.py and reduced mechanically by exact authority headings.','## Selected opening holdings']
for slug,qs in sel.items():
 t=Path('state/holdings/'+slug+'.md').read_text(encoding='utf-8')
 for q in qs:
  b=take_heading(t,q)
  narrower={
   'Agostini v. Felton; Chancellor, Board of Education of the City of New York v. Felton':['I. Lemon governs through one inquiry into governmental religious authority and function'],
   'AT&T Corp. v. Iowa Utilities Board':['I. National implementing rules coexist with state determinations','IV. Necessity and impairment must perform independent limiting work'],
   'Smiley v. Citibank (South Dakota), N.A., 517 U.S. 735':["Does interpretive change or a rule's development during litigation categorically defeat deference?"],
   'Barnhart v. Walton, 535 U.S. 212':['The agency may require twelve months of disabling inability'],
   'A&M Records, Inc. v. Napster, Inc.':['Substantial lawful capability does not immunize specific ongoing assistance','Financial benefit and actual supervision independently support preliminary vicarious liability']}
  if q in narrower:
   b=b.split('##### ')[0].rstrip()+'\n\n'+'\n\n'.join(take_heading(b,h) for h in narrower[q])
  parts += ['Source: state/holdings/'+slug+'.md',b]
parts += ['## Selected operative Standards and Tests']
t=Path('state/STANDARDS_AND_TESTS.md').read_text(encoding='utf-8')
for q in std:
 if q not in ['FCC implementation of local-competition duties','Telecommunications network elements and bounded access','Duration and trial-work conditions in initial disability entitlement','Federal interest classification and national-bank home-state charges']: parts += [take_heading(t,q)]
t=Path('terms/OT2004/workspace/neutral-projection.md').read_text(encoding='utf-8')
parts += ['## Effective current-term public law and published positions']
qs=['Rhines v. Weber','Consumers Energy','Doe v. Porter','Johanns v.','Cutter v.','Wilkinson v. Austin','Rompilla v. Beard']
for b in re.split(r'(?=^### )',t,flags=re.M)[1:]:
 if any(q in b.splitlines()[0] for q in qs):
  limits={'Doe v. Porter':'2. A public school cannot outsource its own devotional instruction','Cutter v.':'Neutral accommodation of private religious exercise in custody','Consumers Energy':'Part I ? Comparable access turns on actual operation','Johanns v.':'Actual governmental control identifies the speaker'}
  h=next((v for k,v in limits.items() if k in b.splitlines()[0]),None)
  if h and h in b:
   b=b.splitlines()[0]+'\n\n'+take_heading(b,h)
  elif h and not ('Opinion Topology' in b or 'Separate Writings' in b or 'Published opinion relationship' in b): continue
  parts += [b.rstrip()]
parts += ['## Court and participation',take_heading(t,'Court and seniority')]
s='\n\n'.join(parts)+'\n'
for forbidden in ['One'+'Drive','Git'+'Hub']: s=s.replace(forbidden,'[source host omitted]')
out.write_text(s,encoding='utf-8')
print('Bounded slice:',len(s),'characters;',len(s.splitlines()),'lines')
