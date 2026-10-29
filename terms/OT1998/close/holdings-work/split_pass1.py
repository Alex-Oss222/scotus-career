from pathlib import Path
import re,json
W=Path(__file__).resolve().parent
es=json.loads((W/'entries_345.json').read_text())
maps={
 'marcus_v_iowa':{0:'Federal Courts'},
 'citizens_for_a':{0:'Federal Courts',2:'First Amendment'},
 'department_of_commerce':{0:'Federal Courts',1:'Federal Courts'},
 'reform_party':{2:'Federal Courts',3:'Federal Courts'},
 'peguero':{0:'Federal Courts'},
 'cedar_rapids':{1:'Constitutional Structure'},
 'att_corp':{11:'Federal Courts'},
}
out=[]
for e in es:
 if 'text' not in e:out.append(e);continue
 mapping=next((v for k,v in maps.items() if e['file'].startswith(k)),None)
 if not mapping:out.append(e);continue
 t=e['text'];prefix,tail=t.split('**Treatment of earlier authority:**',1)
 m=list(re.finditer(r'^##### ',prefix,re.M));head=prefix[:m[0].start()]
 questions=[prefix[x.start():m[i+1].start() if i+1<len(m) else len(prefix)] for i,x in enumerate(m)]
 groups={}
 for i,q in enumerate(questions):groups.setdefault(mapping.get(i,e['area']),[]).append(q)
 for area,qs in groups.items():
  others=', '.join(a for a in groups if a!=area)
  title=head.splitlines()[0][5:]
  date=re.search(r'\*\*Decided:\*\* (.*?)\.',head).group(1)
  text=head+''.join(qs)
  if area==e['area']:text+='**Treatment of earlier authority:**'+tail
  text+=f'\n\nFor the other questions in {title}, decided {date}, at the dockets stated above, see {others}.'
  if area!=e['area']:text+=f' The complete event-wide precedent treatment and operative mandate appear with this case in {e["area"]}.'
  out.append(dict(file=e['file'],area=area,text=text+'\n'))
(W/'entries_345.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
