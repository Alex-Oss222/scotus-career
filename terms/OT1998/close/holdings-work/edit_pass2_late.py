from pathlib import Path
import json,re
W=Path(__file__).resolve().parent
rows={r['file']:r for r in json.loads((W/'record_extractions.json').read_text())}
es=json.loads((W/'draft_entries_910.json').read_text())
unmarked9={
'american_airlines':{'Nonparty preclusion':'Nonparty preclusion','ADEA collective-action participation':'ADEA collective-action participation'},
'city_of_chicago':{'Meaningful standards for dispersal':'Meaningful standards for dispersal'},
'dickinson':{'APA review of PTO factual findings':'APA review of PTO factual findings'},
'lilly':{'The asserted firmly rooted exception':'The asserted firmly rooted exception','Particularized guarantees and the challenged accusations':'Particularized guarantees and the challenged accusations','Harmlessness and relief':'Harmlessness and relief'},
'cunningham':{'Complete separation from the merits':'Complete separation from the merits','Effective review after final judgment':'Effective review after final judgment'},
'greater_new_orleans':{'Direct and material advancement':'Direct and material advancement','Reasonable fit':'Reasonable fit'},
}
authors={'american_airlines':'Ginsburg','city_of_chicago':'Stone-Zsela','dickinson':'Scalia','lilly':'Breyer','cunningham':'Kennedy','greater_new_orleans':'Stone-Zsela'}
for e in es:
 if 'text' not in e:continue
 f=e['file'];r=rows[f];t=e['text']
 for key,labels in unmarked9.items():
  if f.startswith(key):
   t=t.replace('##### The question resolved by the Court\n\n','')
   for label,title in labels.items():t=t.replace('**'+label+'.**',f'##### {title}\n\n**Holding:**')
   author=authors[key]
   t=t.replace("The Court's constitutional ruling",f"{author}'s opinion of the Court on the constitutional question").replace("The Court's statutory ruling",f"{author}'s opinion of the Court on the statutory question").replace("The Court's opinion",f"{author}'s opinion of the Court")
   if key=='lilly':t=t.replace("The lead opinion's", "Breyer's opinion's")
 if r['chunk']==10 and f.startswith(('west_','schleifer_','grupo_','nasa_','strickler_','valdespino_','city_of_dallas_','jones_','maryland_v_dyson_summary')):
  dateend=re.search(r'\*\*Decided:\*\* [^\n]+\n',t).end()
  meta=t[:dateend]+'\n';source=r['sections']['Holdings']
  parts=re.split(r'^### (.+)\n',source,flags=re.M)
  intro=parts[0].strip();body=[]
  if intro:
   if f.startswith('west_'):intro='**Proposition-level authority:** '+intro
   body.append(intro)
  for i in range(1,len(parts),2):
   title,content=parts[i],parts[i+1].strip();pars=content.split('\n\n');first=pars[0]
   authority=next((p for p in pars if p.startswith('**Authority:')),None)
   if f.startswith('schleifer') and 'substantive judgment' in title:
    first='**Authority of the judgment:** '+first
    if authority:authority=authority.replace('**Authority:**','**Limits and questions not reached:**').replace('The judgment has the five votes identified above.',"The judgment has O'Connor, Scalia, Kennedy, Thomas and Breyer; no controlling rationale exists under Marks.")
   elif f.startswith('jones_') and 'aggravator' in title:
    first='**Limits and questions not reached:** '+first
    if authority:authority=authority.replace('**Authority:**','**Authority of the divided positions:**')
   else:
    first='**Holding:** '+first
    if authority:authority=authority.replace('**Authority:**','**Proposition-level authority:**')
   body.append('##### '+title+'\n\n'+first+('\n\n'+authority if authority else ''))
   if f.startswith('west_') and 'EEOC may' in title:
    body.append('**Limits and questions not reached:** '+next(p for p in pars if p.startswith('The compensation category')))
   if f.startswith('nasa_') and 'OIG examination' in title:
    body.append('**Limits and questions not reached:** The representative may assist but may not obstruct questioning, compromise protected information, direct the investigation or require bargaining at the interview; the investigator may insist on the employee\'s own account. Representation may not be reduced to silent observation where interference is otherwise established. The Court decides no universal interview protocol, outside-agency or FBI examination, wider criminal inquiry, national-security question or negotiated extension of rights.')
   if f.startswith('grupo_') and 'General equity' in title:
    body.append('**Limits and questions not reached:** The decision does not restrict injunctions protecting specific property in dispute, statutory freezes, independently authorized fraudulent-transfer remedies, bankruptcy orders, Rule 64 attachment or postjudgment enforcement. It does not decide bond recovery, create a lien, establish fraud or adjudicate the rights of absent Mexican creditors.')
   if f.startswith('valdespino_') and 'population figures' in title:
    body.append('**Limits and questions not reached:** The proposed district must remain lawful in population and geography; the 8.1% underpopulation is not approved. No mathematical crossover formula, racial floor, proportional-election right, distinct-minority-group combination or influence-only entitlement is adopted. Supplementation under ordinary procedure is neither automatically required nor forbidden; the excluded survey is not automatically admitted.')
   if f.startswith('maryland_v_dyson_summary') and 'Federal review' in title:
    body.append('**Holding:** Rules 15.1 and 16.1 make opposition optional unless ordered in this noncapital matter and permit appropriate summary merits action. The supported record and explicit settled-law error permit immediate correction here; absence of opposition and counsel\'s nonmembership in the Court\'s bar establish neither consent, waiver nor default, and no general rule dispenses with needed adversarial presentation.\n\n**Proposition-level authority:** Per curiam Part I, joined by O\'Connor, Scalia, Kennedy, Souter, Thomas and Ginsburg; six Justices. Stone-Zsela agrees with the threshold disposition without this rationale.')
  tail=t[t.index('**Treatment of earlier authority:**'):]
  t=meta+'\n\n'.join(body)+'\n\n'+tail
 # Resolve natural authority references against this Record's actual topology.
 t=t.replace('the six-Justice full-opinion coalition stated in Opinion Topology',"Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg and Breyer")
 t=t.replace('the other seven Justices in the full coalition stated in Opinion Topology',"Stone-Zsela, O'Connor, Scalia, Kennedy, Souter, Thomas and Breyer")
 t=re.sub(r'\*\*Explanation:\*\*.*?(?=\n\n\*\*Treatment)', '',t,flags=re.S) if f.startswith('osullivan') else t
 t=t.replace('**Reservation and operative limit:**','**Limits and questions not reached:**')
 # Mark the two expressly sufficient grounds rather than flattening them.
 if f.startswith(('cunningham','greater_new_orleans','city_of_dallas')):
  target={'cunningham':'Effective review after final judgment','greater_new_orleans':'Reasonable fit','city_of_dallas':'The racial/ethnic preferences also fail independent narrow fit'}
  title=next(v for k,v in target.items() if f.startswith(k));a,b=t.split('##### '+title,1)
  b=b.replace('**Holding:**','**Independent alternative holding:**',1).replace('**Proposition-level authority:**','**Proposition-level authority for alternative holding:**',1)
  t=a+'##### '+title+b
 # Remove disposition advocacy that is unnecessary to establish controlling force.
 t=re.sub(r'The dissenters would reverse the facial-vagueness disposition.*?findings\.','',t)
 t=re.sub(r'The dissenters would affirm use of clear-error review.*?question\.','',t)
 t=re.sub(r'Stevens and Breyer would reverse and remand on actual disability.*?principle\.','',t)
 t=re.sub(r'\n{3,}','\n\n',t)
 e['text']=t
(W/'entries_910.json').write_text(json.dumps(es,ensure_ascii=False,indent=2))
