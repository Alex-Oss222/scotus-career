"""Mechanically total individually classified actual opinion tables, never earlier tallies."""
from pathlib import Path
import json,sys,re
sys.dont_write_bytecode=True
TERM=Path(__file__).resolve().parents[1]
evidence=Path(sys.argv[1]); rows=json.loads(evidence.read_text(encoding='utf-8'))
justices=['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']
# These classifications were made from each actual table and event, not numbers in assignment statements.
excluded={'brown_v_williams':'per curiam filing order','city_of_monroe':'per curiam summary merits','plra_section_123':'nonjudicial statutory source','jefferson_v_city':'Court jurisdictional dismissal','rogers_v_united':'dismissal as improvidently granted','lee_v_harcleroad':'Court threshold standing disposition','arteaga_v_united':'per curiam filing order','newsweek_inc':'per curiam summary merits','spencer_v_kemna':'Court threshold mootness disposition'}
counts={j:0 for j in justices}; checked=[];last=None
for r in rows:
 exclusion=next((v for k,v in excluded.items() if r['record'].startswith(k)),None)
 if exclusion:checked.append({**r,'classification':exclusion,'counted_authors':[]});continue
 t=r['opinion_topology'];authors=[]
 for line in t.splitlines():
  if line.startswith('| Opinion of the Court') or line.startswith('| Opinion announcing the judgment'):
   author=line.split('|')[2].strip()
   if author not in authors:authors.append(author)
 if not authors:
  m=re.search(r'(?:Chief Justice |Justice )?('+ '|'.join(re.escape(j) for j in justices)+r') delivers',t)
  if m:authors=[m[1]]
 assert authors and all(a in justices for a in authors),(r['record'],authors)
 for a in authors:counts[a]+=1
 checked.append({**r,'classification':'signed lead after plenary merits review; one per actual part author','counted_authors':authors});last=r['case']+'; '+r['date']+'; '+', '.join(authors)
out={'evidence':str(evidence),'counts':counts,'last_counted':last,'records':checked,'method':'fresh total from actual topologies and explicit event classifications; no prior running count used'}
dest=TERM/'freeze'/evidence.name.replace('ASSIGNMENT_EVIDENCE','COUNT_RECEIPT')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'counts':counts,'last_counted':last,'receipt':str(dest),'n':sum(counts.values())},ensure_ascii=False,indent=2))
