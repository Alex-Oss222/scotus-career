from pathlib import Path
import json,re,hashlib
b=Path(__file__).parent
manifest={'scope':'Control-only mechanical source filtering; no legal framing. Original newline layout and unaffected columns retained.','files':{}}
for name in ['petition','ja','petitioners','respondent','reply']:
 p=b/f'meghrig_{name}.txt';s=p.read_text();a=s.split('\n');orig=list(a);edits=[]
 def erase(line,old):
  assert old in a[line-1],(name,line,old)
  a[line-1]=a[line-1].replace(old,' '*len(old),1)
 if name=='ja':
  for i,l in enumerate(a):
   if 'Certiorari Granted September 27, 1995' in l:a[i]=''
   if 'Order of the United States Supreme Court Granting' in l:a[i]='';a[i+1]=''
  idx=next(i for i,l in enumerate(a) if 'ORDER ALLOWING CERTIORARI.' in l)
  start=idx
  while start and '\f' not in a[start]:start-=1
  end=idx+1
  while end<len(a) and '\f' not in a[end]:end+=1
  for i in range(start,end):a[i]=a[i][:66].rstrip()
 elif name=='petitioners':
  erase(288,', and was granted on');erase(289,'September 27, 1995.')
 elif name=='respondent':
  erase(250,', and was granted on September 27,');erase(251,'1995.')
 elif name=='reply':
  erase(165,'granted by this Court')
  erase(649,'This Court granted certiorari as');erase(650,'to both issues.')
  erase(654,'Both were accepted for review by the Court, and the')
 for i,(before,after) in enumerate(zip(orig,a)):
  if before!=after:edits.append({'original_line':i+1,'before':before,'after':after})
 out='\n'.join(a);op=b/f'meghrig_{name}_neutral_read.txt';op.write_text(out)
 manifest['files'][p.name]={'original_sha256':hashlib.sha256(s.encode()).hexdigest(),'derivative':op.name,'derivative_sha256':hashlib.sha256(out.encode()).hexdigest(),'changed_lines':edits}
(b/'MEGHRIG_REDACTION_CONTROL.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps({k:len(v['changed_lines']) for k,v in manifest['files'].items()}))
