"""Copy objective, dated source passages for a fresh neutral validator."""
from pathlib import Path
import re
import hashlib

root=Path(__file__).resolve().parents[3]
base=root/'terms/OT2003/sources/mcconnell'
statute=(base/'BCRA-107-155.txt').read_text(encoding='utf-8')
starts=list(re.finditer(r'(?m)^SEC\. (\d+)\.',statute))
selected={101,102,103,201,202,203,204,211,212,213,214,304,305,307,311,316,318,319,401,402,403,504}
parts=['# BCRA enacted-text selections','Source: Public Law 107-155, March 27, 2002, 116 Stat. 81. Exact section copies from the saved official enacted text. These are statutory text, not findings or adjudications.']
for i,m in enumerate(starts):
 if int(m.group(1)) in selected:
  end=starts[i+1].start() if i+1<len(starts) else statute.index('    Approved March 27, 2002.')
  parts.extend(['## BCRA section '+m.group(1),'```text\n'+statute[m.start():end].rstrip()+'\n```'])
(base/'BCRA-selected-exact.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')

lower=(base/'district-251-FSupp2d-176.txt').read_text(encoding='utf-8')
groups={
 'district-overview-and-procedural-exact.md':[
  ('Per curiam: component judgments',0,12452),
  ('Per curiam: Press Clause, disclosure and coordination conclusions',144779,232637),
  ('Henderson: lowest-unit charge, raised ceilings and self-finance standing',818028,838277),
 ],
 'district-title1-competing-exact.md':[
  ('Kollar-Kotelly: national and state party fit, tax-exempt organizations, federal and state officeholders',1698972,1748874),
  ('Leon: nonfederal and mixed-purpose objection and severability',1937018,1955720),
  ('Leon: state/local activity, exempt organizations and officeholders',1955720,1993083),
 ],
 'district-title2-competing-exact.md':[
  ('Kollar-Kotelly: primary definition tailoring and disputed empirical material',1483275,1520240),
  ('Leon: primary and fallback definitions and nonprofit exception',1993774,2032899),
 ],
 'district-choice-minors-broadcast-exact.md':[
  ('Leon: party choice, minors and broadcaster records',2032899,2054330),
 ]
}
for name,ranges in groups.items():
 parts=['# Bounded District Court source passages','Source: McConnell v. FEC, 251 F. Supp. 2d 176 (D.D.C., May 2003). These are the lower judges\' respective judgments, findings, reported arguments and reasons, not controlling Supreme Court law. Prior Supreme Court descriptions inside these historical sources must be tested against the actual entering-law slice.']
 for label,start,end in ranges:
  if end<len(lower) and lower[end-1]!='\n': end=lower.rfind('\n',start,end)
  parts.extend(['## '+label,'Exact saved-source character range: '+str(start)+' to '+str(end)+'.','```text\n'+lower[start:end].rstrip()+'\n```'])
 (base/name).write_text('\n\n'.join(parts)+'\n',encoding='utf-8')

fec=(base/'19.-Appellants-Brief.txt').read_text(encoding='utf-8')
parts=['# FEC predecision brief: objective source selections','Source: Brief for the Federal Election Commission et al., August 2003, saved from the docket archive. This file reproduces party argument, not findings or law.','## Questions presented','```text\n'+fec[1300:4600]+'\n```','## Broadcaster records and minors','```text\n'+fec[287500:].rstrip()+'\n```']
(base/'FEC-questions-broadcast-minors-exact.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')

receipts=[]
for p in sorted(base.glob('*')):
 if p.is_file():receipts.append(p.name+' | '+str(p.stat().st_size)+' bytes | SHA-256 '+hashlib.sha256(p.read_bytes()).hexdigest())
(base/'SOURCE-FINGERPRINTS.txt').write_text('\n'.join(receipts)+'\n',encoding='utf-8')
print('Copied enacted text and bounded lower-court and party-source passages.')
