"""Faithful cumulative projections from the opening snapshot and new public kernels."""
from pathlib import Path
import argparse,re,json,importlib.util,sys
sys.dont_write_bytecode=True
root=Path(__file__).resolve().parents[3];term=root/'terms/OT1999'
ap=argparse.ArgumentParser();ap.add_argument('--stopped',type=Path);args=ap.parse_args()
stopped=json.loads(args.stopped.read_text(encoding='utf-8')) if args.stopped else {}
baseline=json.loads((term/'freeze/OT_1999CHUNK6_BASELINE_HASHES.json').read_text(encoding='utf-8'))
labels=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
all_events=[];new=[]
for p in (term/'records').glob('*.md'):
 if p.name.startswith('.'):continue
 t=p.read_text(encoding='utf-8');cap=re.search(r'^\*\*Case and dockets:\*\* (.+)$',t,re.M).group(1)
 event=re.search(r'^\*\*Event and date:\*\* (.+)$',t,re.M).group(1);date=re.search(r'\d{4}-\d{2}-\d{2}',event).group()
 result=re.search(r'^\*\*Result:\*\* (.+)$',t,re.M).group(1)
 item={'path':p,'case':cap.split(';',1)[0],'date':date,'event':event,'result':result}
 all_events.append(item)
 if p.relative_to(root).as_posix() in baseline:continue
 pp=t.split('## Public Projection',1)[1];heads=list(re.finditer(r'^## (.+)$',pp,re.M));assert [m.group(1) for m in heads]==labels,p.name
 item['blocks']={m.group(1):pp[m.end():heads[i+1].start() if i+1<len(heads) else len(pp)].strip() for i,m in enumerate(heads)}
 new.append(item)
key=lambda d:(d['date'],d['case'].casefold())
all_events.sort(key=key);new.sort(key=key)
assert 0<len(new)<=12,'Expected one through twelve new chunk-six Records'
assert all('2000-05-01'<=d['date']<='2000-05-22' for d in new)
judicial=sum('admitted-source' not in d['path'].name for d in all_events);sources=len(all_events)-judicial
cursor=max(d['date'] for d in all_events)
manifest=(term/'workspace/manifest.md').read_text(encoding='utf-8')
status=f'Open during chunk 6; {judicial} completed Court events. {len(new)} of twelve chunk-six events are completed.'
if len(new)+len(stopped)==12:status=f'Open after chunk 6 processing; {judicial} completed Court events. {len(new)} of twelve chunk-six events are completed.'
if len(new)==12:status=f'Open after chunk 6; {judicial} completed Court events. All twelve chunk-six events are completed; none is stopped.'
if stopped:status+=f' {len(stopped)} chunk-six matter(s) remain stopped with exact blockers in their inventory rows.'
manifest=re.sub(r'^\*\*Current status:\*\*.*$', '**Current status:** '+status,manifest,count=1,flags=re.M)
manifest=re.sub(r'^\*\*Completed OT1999 events:\*\*.*$',f'**Completed OT1999 events:** {judicial} Court events and {sources} admitted noncase-law sources. Fiore\'s certification is completed, but the underlying case remains open.',manifest,count=1,flags=re.M)
(term/'workspace/manifest.md').write_text(manifest,encoding='utf-8')
pending=[]
for line in manifest.splitlines():
 c=[x.strip() for x in line.strip('|').split('|')]
 if len(c)>=7 and re.fullmatch(r'\d{4}-\d{2}-\d{2}',c[0]) and c[1].startswith('OT_1999CHUNK') and not c[6].startswith('Completed:'):pending.append((c[0],c[2],c[6]))
pending.sort(key=lambda r:(r[0],r[1].casefold()))
next_text=f'The next unresolved scheduled item is {pending[0][1].rstrip(" +")} on {pending[0][0]}.' if pending else 'No scheduled inventory item remains unresolved.'
def section_replace(t,title,body):
 marker='## '+title+'\n';a=t.index(marker)+len(marker);m=re.search(r'^## ',t[a:],re.M);z=a+m.start() if m else len(t)
 return t[:a]+'\n'+body.strip()+'\n\n'+t[z:]
def section_append(t,title,body):
 marker='## '+title+'\n';a=t.index(marker)+len(marker);m=re.search(r'^## ',t[a:],re.M);z=a+m.start() if m else len(t)
 return t[:z].rstrip()+'\n\n'+body.strip()+'\n\n'+t[z:]
def shift(t):return re.sub(r'^(#{1,4}) ',r'##\1 ',t,flags=re.M)
table=['| Effective date | Event and authority | Result / source status |','|---|---|---|']
for d in all_events:table.append(f'| {d["date"]} | [{d["case"]}](../records/{d["path"].name}) | {d["result"].replace("|","/")} |')
law=[];separates=[];procedures=[]
for d in new:
 b=d['blocks'];ref=f'[Record](../records/{d["path"].name})'
 pieces=[f'### {d["case"]} — {d["date"]}',ref]
 for title in ['Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Source Notes']:pieces += ['#### '+title,shift(b[title])]
 law.append('\n\n'.join(pieces))
 if b['Separate Writings'].strip().lower() not in ['none.','none','no separate writing.','no separate writing issues.']:separates.append(f'### {d["case"]} — {d["date"]}\n\n'+shift(b['Separate Writings'])+'\n\n'+ref)
 procedures.append(f'**{d["case"]} — {d["date"]}.** '+b['Procedure After Action']+' '+ref)
for name,completed,lawhead,separatehead,procedurehead in [
 ('CONTINUITY','Completed Events and Admitted Sources','Current Law','Material Published Noncontrolling Positions','Current Procedure and Institution'),
 ('NEUTRAL_PROJECTION','Completed public events and admitted sources','Current-term law','Published noncontrolling positions','Current public procedure and institution')]:
 t=(term/'freeze'/f'OT_1999CHUNK6_OPENING_{name}.md').read_text(encoding='utf-8')
 t=t.replace('60 Court events and 4 admitted nonjudicial sources',f'{judicial} Court events and {sources} admitted nonjudicial sources',1)
 t=re.sub(r'60 Court events are completed:.*?No institutional change is entered\.',f'{judicial} Court events are completed: 60 through chunk 5 and {len(new)} in chunk 6. Four nonjudicial sources retain their own effective provisions. The chronology cursor is {cursor}. Uncoordinated same-day decisions share entering law and operate together only prospectively. No institutional change is entered.',t,count=1)
 t=re.sub(r'The next scheduled chunk is chunk 6,.*?(?=\n\n)',next_text+' Fiore, the fourteen opening carryovers, and the existing bounded remands retain their recorded stages. The completed chunk-six events retain each mandate and scope limit stated below.',t,count=1,flags=re.S)
 t=section_replace(t,completed,'\n'.join(table))
 t=section_append(t,lawhead,'\n\n'.join(law))
 if separates:t=section_append(t,separatehead,'\n\n'.join(separates))
 t=section_append(t,procedurehead,'### Chunk 6 procedures\n\n'+'\n\n'.join(procedures))
 if name=='CONTINUITY':
  spec=importlib.util.spec_from_file_location('counter',root/'tmp/ot1999_chunk6_prior_assignments.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
  counts={j:0 for j in mod.JUSTICES};counted=[]
  for d in all_events:
   data=mod.selected_record(d['path'])
   for author in data['authors']:counts[author]+=1
   if data['authors']:counted.append(d)
  count_text='### Counted lead opinions through current chunk 6 work\n\nRecounted from actual signed plenary lead authors in Record opinion tables. Per curiam, summary, procedural and separate writings do not count. No Git query was made.\n\n| Justice | Counted leads |\n|---|---:|\n'+'\n'.join(f'| {j} | {n} |' for j,n in counts.items())+f'\n\nLast counted event: {counted[-1]["case"]}, {counted[-1]["date"]}. Existing assignments stand.\n\n'
  t=re.sub(r'### Counted lead opinions through chunk 5\n.*?(?=### Continuing open matters)',lambda m:count_text,t,count=1,flags=re.S)
  block='\n\n'.join(f'**{c}:** {b}' for c,b in stopped.items()) if stopped else ('No chunk-six matter is stopped. All twelve supplied matters are completed.' if len(new)==12 else f'{len(new)} chunk-six events are completed. Remaining chunk-six matters await their separated Run stages; no outcome or terminal action is inferred.')
  t=section_replace(t,'Blockers and Revalidation Needs',block+'\n\nPrior open-matter stages and carryovers remain as specified above. Repository-history verification and commit remain with the operator under the no-Git instruction.')
  t=section_append(t,'Source and Research Cutoff',f'Chunk 6 public law and procedure are projected through {cursor}. Each new Record supplies its event-specific research cutoff, neutral/reconciliation provenance and source limits. The Run does not commission public Render. No new external follow-up event is inferred.')
  (term/'freeze/OT_1999CHUNK6_CURRENT_COUNTS.json').write_text(json.dumps(counts,indent=2)+'\n',encoding='utf-8')
 target=term/'workspace'/('continuity.md' if name=='CONTINUITY' else 'neutral-projection.md')
 target.write_text(t.rstrip()+'\n',encoding='utf-8')
print(f'Projected {len(new)} new Records; {judicial} Court events and {sources} sources; cursor {cursor}.')
