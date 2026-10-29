from pathlib import Path
import json,re
W=Path(__file__).resolve().parent
es=json.loads((W/'draft_entries_11.json').read_text())
for e in es:
 t=e['text'];f=e['file']
 t=t.replace('**Operative proposition:**','**Holding:**').replace('**Rule and scope limit:**','**Limits and questions not reached:**').replace('**Reserved questions.**','**Limits and questions not reached:**')
 if f.startswith('albertsons_'):
  t=re.sub(r'##### Disability-method discussion and its limited authority.*?(?=\*\*Treatment of earlier authority:)', '',t,flags=re.S)
  t=t.replace('The unnecessary disability-method discussion creates no new binding rule on natural compensation; Bragdon’s individual inquiry and general mitigation reservation remain governing.','The unnecessary disability-method discussion creates no new binding rule on natural compensation. For the separate same-day original-ADA mitigation holdings, see Sutton v. United Air Lines, Inc., No. 97-1943, and Murphy v. United Parcel Service, Inc., No. 97-1992, decided June 22, 1999, in Civil Rights.')
  t=t.replace('its reservation of general mitigating measures is not resolved by a nonessential discussion here.','its reservation of general mitigating measures is not resolved by the nonessential discussion in this decision.')
 if f.startswith('olmstead_'):
  t=t.replace('Part I, joined by',"Part I of Ginsburg's opinion of the Court, joined by").replace('Part II, joined by',"Part II of Ginsburg's opinion of the Court, joined by")
  t=t.replace('Kennedy expressly adopts only the narrower non-isolated-cost proposition identified in Opinion Topology.',"Kennedy additionally adopts only the narrower proposition that the inquiry cannot be confined to the two claimants' isolated additional expense and must permit institutional and program overhead and relevant administrative responsibilities; he does not join the full Part II rule.")
 if f.startswith('college_savings_'):
  t=t.replace('**Proposition-level authority:** Part I,',"**Proposition-level authority:** Part I of Stone-Zsela's opinion of the Court,").replace('**Proposition-level authority:** Part II,',"**Proposition-level authority:** Part II of Stone-Zsela's opinion of the Court,").replace('**Proposition-level authority:** Part III,',"**Proposition-level authority:** Part III of Stone-Zsela's opinion of the Court,")
  t=t.replace('**Judgment without controlling affirmative rationale:**','**Authority of the judgment:**').replace('**Authority and limit:**','**Limits of the judgment:**')
 if f.startswith('florida_prepaid_'):
  t=t.replace('The immunity-denial judgment is affirmed. Stevens,', '**Authority of the judgment:** The immunity-denial judgment is affirmed, 5–4. Stevens,',1)
  t=t.replace('There is no controlling general Article I abrogation holding, no controlling §5 fit ruling for the Patent Remedy Act, and no controlling commercial-consent rule.', 'This decision supplies no controlling general Article I abrogation holding, §5 fit ruling for the Patent Remedy Act, or commercial-consent rationale.')
  t+='\nFor the separate controlling rejection of consent inferred from ordinary commercial participation, see College Savings Bank v. Florida Prepaid Postsecondary Education Expense Board, No. 98-149, June 23, 1999, in Federal Courts. The distinct judgments and affirmative rationales are not merged.\n'
  t=re.sub(r'The four dissenters would vacate the immunity-denial judgment.*?patent proceedings\.','',t,flags=re.S)
 if f.startswith('ortiz_'):
  a,b=t.split('##### 4. The undivided representation independently fails Rule 23(a)(4)',1)
  b=b.replace('**Holding:**','**Independent alternative holding:**',1).replace('**Proposition-level authority:**','**Proposition-level authority for alternative holding:**',1)
  t=a+'##### 4. The undivided representation independently fails Rule 23(a)(4)'+b
  t=t.replace('Stevens and Breyer would sustain the challenged certification determinations, while reserving definitive resolution of the additional objections the Court does not reach.','')
 e['text']=re.sub(r'\n{3,}','\n\n',t)
# Place the separately usable statutory and patent-property questions in their
# own doctrinal areas. Each question retains one complete primary location.
out=[]
for e in es:
 mp={'alden_':{1:'Labor and Employment'},'florida_prepaid_':{1:'Business and Commercial Law'}}
 mapping=next((v for k,v in mp.items() if e['file'].startswith(k)),None)
 if not mapping:out.append(e);continue
 prefix,tail=e['text'].split('**Treatment of earlier authority:**',1)
 hs=list(re.finditer(r'^##### ',prefix,re.M));head=prefix[:hs[0].start()]
 qs=[prefix[h.start():hs[i+1].start() if i+1<len(hs) else len(prefix)] for i,h in enumerate(hs)]
 groups={}
 for i,q in enumerate(qs):groups.setdefault(mapping.get(i,e['area']),[]).append(q)
 for area,questions in groups.items():
  text=head+''.join(questions)
  if area==e['area']:text+='**Treatment of earlier authority:**'+tail
  name=head.splitlines()[0][5:];date=re.search(r'\*\*Decided:\*\* (.*?)\.',head).group(1)
  text+='\n\nFor the other questions in '+name+', decided '+date+', at the dockets stated above, see '+', '.join(a for a in groups if a!=area)+'.'
  if area!=e['area']:text+=' The complete event-wide precedent treatment and operative mandate appear with this case in '+e['area']+'.'
  out.append(dict(file=e['file'],area=area,text=text+'\n'))
(W/'entries_11.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
