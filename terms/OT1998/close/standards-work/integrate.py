from pathlib import Path
import re,json,hashlib
W=Path('terms/OT1998/close/standards-work'); source=Path('state/STANDARDS_AND_TESTS.md')
raw=source.read_bytes(); baseline=raw.decode().replace('\r\n','\n'); text=baseline
rows=json.loads((W/'records-index.json').read_text())
early=json.loads((W/'early-edits.json').read_text()); late=json.loads((W/'late-edits.json').read_text())
# Integration correction: direct candidate contribution rules belong under their own recipient trigger.
for e in late:
 if e['title']=='Intermediary contribution limits and meaningful association':
  e['current_append']='Annual duration, actual recipient function, per-recipient versus aggregate operation, amount and demonstrated effect on collective advocacy must be considered together. Other available committees and aggregate political success do not alone cure a burden on the chosen association.'
  e['authority_append']=[e['authority_append'][0].split(' Part III supplies')[0]+' Part III supplies the actual-channel and operational considerations.']
  e['effective']=None
  e['fields']['Current wording authority']='Russell, April 28, 1999, applies Day’s meaningful-pooling and actual-fit rule to a demonstrated per-recipient candidate-conduit setting without adopting a general dollar safe harbor.'
  e['fields']['Related current rules']='Candidate contribution limits and anticorruption fit states the distinct direct-candidate and exact dispersed-donor classification rules.'
late.append({'mode':'add','title':'Candidate contribution limits and anticorruption fit','area':'Speech, association, and elections','text':'''### Candidate contribution limits and anticorruption fit

**Governing question:** What justifies direct candidate-contribution limits and differentiated source allowances.

**Current rule:** Candidate contribution limits must be closely drawn to a sufficiently important interest in preventing corruption or its appearance while preserving meaningful political association. No completed bribe is necessary, and equality of political influence is not an independent justification. Amount and inflation comparisons establish no permanent constitutional boundary; actual campaign scale, fundraising burden and cumulative restrictions matter. Under the adjudicated Arkansas classification, a registered committee receiving contributions exclusively from individuals and no more than $25 cumulatively from any individual during a calendar year may receive a $2,500 per-candidate, per-election contribution allowance while ordinary sources face lower ceilings. The actual dispersed-donor structure and its anticorruption fit, rather than a small-donor label, support the distinction.

**Authority by component:**

- Direct-candidate interest and close fit: Russell v. Burris — Canonical Decision Record, Holdings, “Contribution limits require actual anticorruption fit; two candidate categories fail here”, April 28, 1999; O’Connor Part I, all nine Justices.
- Exact dispersed-donor classification: Russell — Holdings, “The exact small-donor qualification supports a different candidate allowance”, April 28, 1999; O’Connor Part IV with Stevens, Souter, Ginsburg and Breyer.

**Present operation effective:** Russell, April 28, 1999.

**Exceptions and limits:** Office-specific dollar applications establish no general floor or safe harbor. Every small-donor qualification remains necessary to the adjudicated distinction; no unlimited candidate-giving right, immunity for sham structures or automatic validity of materially different classifications follows. A failed categorical challenge does not resolve a genuinely different office-specific application.

**Related current rules:** Intermediary contribution limits and meaningful association separately governs committee receipt restrictions and actual candidate-conduit fit.
'''})

def bounds(title):
 m=re.search(r'^### '+re.escape(title)+r'\n',text,re.M)
 if not m:raise ValueError('missing title '+title)
 n=re.search(r'^#{2,3} ',text[m.end():],re.M)
 return m.start(), m.end()+n.start() if n else len(text)
def field_replace(entry,name,value,append=False):
 pattern=r'^\*\*'+re.escape(name)+r':\*\*[^\n]*(?:\n(?!\*\*|#{2,3} ).*)*'
 m=re.search(pattern,entry,re.M)
 if m:
  old=m.group().rstrip(); value=old+' '+value if append else '**'+name+':** '+value
  return entry[:m.start()]+value+'\n\n'+entry[m.end():].lstrip('\n')
 return entry.rstrip()+'\n\n**'+name+':** '+value+'\n\n'
modified=set();added=[]
for e in early+late:
 mode=e['mode'];title=e['title']
 if mode=='add':
  if re.search(r'^### '+re.escape(title)+r'$',text,re.M):raise ValueError('duplicate '+title)
  area=e['area'];m=re.search(r'^## '+re.escape(area)+r'\n',text,re.M)
  if not m:raise ValueError('missing area '+area)
  end=re.search(r'^## ',text[m.end():],re.M); pos=m.end()+end.start() if end else len(text)
  text=text[:pos].rstrip()+'\n\n'+e['text'].strip()+'\n\n'+text[pos:];added.append(title)
 else:
  a,b=bounds(title); entry=text[a:b]
  if mode=='replace': entry=e['text'].strip()+'\n\n'
  elif mode=='extend':
   for old,new in e['replace'].items():
    if old not in entry:raise ValueError('missing replacement '+title+': '+old)
    entry=entry.replace(old,new)
   entry=field_replace(entry,'Current rule',e['current_append'],True)
   am=re.search(r'^\*\*Authority by component:\*\*',entry,re.M)
   pm=re.search(r'^\*\*Present operation effective:\*\*',entry,re.M)
   if not am or not pm or pm.start()<am.start():raise ValueError('field ordering '+title)
   entry=entry[:pm.start()].rstrip()+'\n\n'+'\n'.join('- '+s for s in e['authority_append'])+'\n\n'+entry[pm.start():]
   if e['effective']:entry=field_replace(entry,'Present operation effective',e['effective'])
   for k,v in e['fields'].items():entry=field_replace(entry,k,v)
  text=text[:a]+entry+text[b:];modified.add(title)
headers={'Last completed October Term':'1998','Processed through':'June 23, 1999, after all 130 completed OT1998 Court events and one admitted source event.','Edition':'October 29, 2026'}
for k,v in headers.items():text=re.sub(r'^\*\*'+re.escape(k)+r':\*\*.*$',f'**{k}:** {v}',text,flags=re.M)
# Preserve byte-level line endings of the opening register.
out=text.replace('\n','\r\n').encode(); (W/'STANDARDS_AND_TESTS.independent.md').write_bytes(out)

def sections(s):
 out={}
 for m in re.finditer(r'^### (.+)\n',s,re.M):
  n=re.search(r'^#{2,3} ',s[m.end():],re.M);end=m.end()+n.start() if n else len(s)
  if m.group(1) in out:raise ValueError('duplicate heading '+m.group(1))
  out[m.group(1)]=s[m.start():end].rstrip()
 return out
before=sections(baseline);after=sections(text)
missing=set(before)-set(after);unexpected=[k for k,v in before.items() if k not in modified and v!=after.get(k)]
required=['Governing question','Current rule','Authority by component','Present operation effective']
field_fail=[(k,f) for k in added|set() for f in []] if False else []
for k in set(added)|modified:
 for f in required:
  if '**'+f+':**' not in after[k]:field_fail.append((k,f))
assert not missing and not unexpected and not field_fail,(missing,unexpected,field_fail)
cov=[]
for x in json.loads((W/'early-coverage.json').read_text()):
 n=next(i+1 for i,r in enumerate(rows) if r['file']==x['file']);cov.append({'event':n,'file':x['file'],'date':rows[n-1]['date'],'status':x['decision'],'titles':x['titles'],'explanation':x['explanation']})
for x in json.loads((W/'late-coverage.json').read_text()):
 r=rows[x['event']-1];cov.append({**x,'file':r['file'],'date':r['date']})
next(x for x in cov if x['event']==81)['titles'].append('Candidate contribution limits and anticorruption fit')
cov.sort(key=lambda x:x['event']);assert [x['event'] for x in cov]==list(range(1,132))
for x in cov:
 for k in x['titles']:assert k in after,(x['event'],k)
(W/'coverage.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2))
lines=['# OT1998 Standards and Tests event coverage','', 'The status concerns admission of reusable rules, not the validity or importance of a decision. Records control.','', '| Event | Date | Record | Admission | Rules / reason |','|---:|---|---|---|---|']
for x in cov:lines.append(f'| {x["event"]} | {x["date"]} | `{x["file"]}` | {x["status"]} | '+('; '.join(x['titles'])+'. ' if x['titles'] else '')+x['explanation'].replace('|','/')+' |')
(W/'COVERAGE.md').write_text('\n'.join(lines)+'\n')
receipt={'opening_sha256':hashlib.sha256(raw).hexdigest(),'draft_sha256':hashlib.sha256(out).hexdigest(),'opening_bytes':len(raw),'draft_bytes':len(out),'opening_entries':len(before),'candidate_entries':len(after),'new_entries':len(added),'modified_opening_entries':len(set(before)&modified),'unchanged_opening_entries':len(set(before)-modified),'all_opening_entries_preserved':not missing,'unrelated_entries_exact_after_newline_normalization':not unexpected,'required_fields_complete_for_changes':not field_fail,'events_covered':len(cov),'headers':headers,'holdings_candidate_read':False,'new_entry_titles':added,'changed_titles':sorted(modified)}
(W/'integration-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in receipt.items() if k not in ['new_entry_titles','changed_titles']},indent=2))
