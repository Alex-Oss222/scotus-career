"""Recount actual earlier opinion tables; never select an author or decide eligibility."""
from pathlib import Path
import argparse,importlib.util,json,sys
sys.dont_write_bytecode=True
root=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('count_source',root/'tmp/ot1999_chunk6_prior_assignments.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
ap=argparse.ArgumentParser();ap.add_argument('date');ap.add_argument('case');ap.add_argument('--output',type=Path)
a=ap.parse_args();counts={j:0 for j in module.JUSTICES};counted=[]
key=(a.date,a.case.casefold())
for p in (root/'terms/OT1999/records').glob('*.md'):
 if p.name.startswith('.'):continue
 d=module.selected_record(p);caption=d['case'].split(';',1)[0]
 if (d['date'],caption.casefold()) >= key:continue
 for author in d['authors']:counts[author]+=1
 if d['authors']:counted.append({'date':d['date'],'case':caption,'authors':sorted(d['authors']),'record':p.name})
counted.sort(key=lambda d:(d['date'],d['case'].casefold()))
result={'before_date':a.date,'before_case':a.case,'counts':counts,'total':sum(counts.values()),'last_event':counted[-1] if counted else None,'counted_events':counted,'basis':'Fresh parse of actual signed plenary lead opinion tables in earlier durable Records; no Git operation.'}
if a.output:
 target=a.output.resolve()
 if not (target.is_relative_to(root/'terms/OT1999') or target.is_relative_to(root/'tmp')):raise SystemExit('Output outside authorized roots')
 target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='counted_events'},ensure_ascii=False,indent=2))
