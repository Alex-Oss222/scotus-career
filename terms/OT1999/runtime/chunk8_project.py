from pathlib import Path
import re
import json
import sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
T=ROOT/'terms/OT1999'

def section(text,name):
    m=re.search(r'^## '+re.escape(name)+r'\s*\n(.*?)(?=^## |\Z)',text,re.M|re.S)
    return m[1].strip() if m else ''

def add(text,name,body):
    pat=r'(^## '+re.escape(name)+r'\s*\n)(.*?)(?=^## |\Z)'
    return re.sub(pat,lambda m:m[1]+m[2].rstrip()+'\n\n'+body.strip()+'\n\n',text,count=1,flags=re.M|re.S)

records=[]
for p in (T/'records').glob('*.md'):
    t=p.read_text(encoding='utf-8')
    em=re.search(r'^\*\*Event and date:\*\*\s*(.*)',t,re.M)
    if not em or not re.search(r'chunk 8\b',em[1],re.I):continue
    case=re.search(r'^\*\*Case and dockets:\*\*\s*(.*)',t,re.M)[1].split(';')[0].rstrip('.')
    date=re.search(r'\d{4}-\d{2}-\d{2}',em[1])[0]
    result=re.search(r'^\*\*Result:\*\*\s*(.*)',t,re.M)[1]
    pub=t.split('## Public Projection',1)[1]
    records.append((date,case,p,result,t,pub))
records.sort(key=lambda x:(x[0],x[1]))
stoppath=T/'runtime/OT_1999CHUNK8_STOPS.json'
stops=json.loads(stoppath.read_text(encoding='utf-8')) if stoppath.exists() else {}
cursor=max([r[0] for r in records]+['2000-06-12'])
count=84+len(records)
manifest=(T/'workspace/manifest.md').read_text(encoding='utf-8')
phase='after chunk 8' if len(records)+len(stops)==12 else 'during chunk 8'
manifest=re.sub(r'^\*\*Current status:\*\*.*$',f'**Current status:** Open {phase}; {count} completed Court events. Chunk 8: {len(records)} completed and {len(stops)} stopped matters.',manifest,flags=re.M)
manifest=re.sub(r'^\*\*Completed OT1999 events:\*\*.*$',f'**Completed OT1999 events:** {count} Court events and 4 admitted noncase-law sources. Fiore\'s certification is completed, but the underlying case remains open.',manifest,flags=re.M)
updated=[]
for line in manifest.splitlines():
    if line.startswith('| ') and '| OT_1999CHUNK8 |' in line:
        cells=[c.strip() for c in line.strip('|').split('|')]
        if len(cells)==11:
            for date,case,p,result,t,pub in records:
                if p.name in cells[6]:
                    cells[7]=result.replace('|','/')+' See the Record for the mandate and remaining proceedings.'
                    break
            if cells[6].startswith('Stopped:'):
                cells[7]='No Court action entered; the stated revalidation blocker remains open.'
            line='| '+' | '.join(cells)+' |'
    updated.append(line)
manifest='\n'.join(updated)+'\n'
pending_lines=[]
arizona=next((r for r in records if r[1]=='Arizona v. California'),None)
if arizona:
    pending_lines.append('Arizona v. California, No. 8, Original, remains pending after the June 19 exceptions decision. The Master must address the unresolved Fort Yuma title, boundary, acreage and water questions and provide implementing decree provisions for the two approved settlements. No final supplemental decree or objection deadline has been entered. The completed event does not close the original action. See [the Record](../records/'+arizona[2].name+').')
if stops:
    pending_lines.append('Unadjudicated chunk 8 matters: '+'; '.join(stops)+'. Their exact blockers remain in the inventory rows; no Court order, disposition or new date is inferred from the stop.')
if pending_lines:
    title='Chunk 8 pending proceedings'
    body='\n\n'.join(pending_lines)
    if re.search(r'^## '+title+r'\s*$',manifest,re.M):
        manifest=re.sub(r'(^## '+title+r'\s*\n).*?(?=^## |\Z)',lambda m:m[1]+'\n'+body+'\n\n',manifest,flags=re.M|re.S)
    else:manifest=manifest.rstrip()+'\n\n## '+title+'\n\n'+body+'\n'
(T/'workspace/manifest.md').write_text(manifest,encoding='utf-8')
pending=[]
for line in manifest.splitlines():
    if not re.match(r'^\| \d{4}-\d{2}-\d{2} \|',line):continue
    cells=[c.strip() for c in line.strip('|').split('|')]
    if len(cells)>6 and cells[6]=='Open':pending.append((cells[0],cells[2]))
next_event=min(pending) if pending else None
rowadd=[];laws=[];positions=[];procedures=[]
for date,case,p,result,t,pub in records:
    link=f'[{case}](../records/{p.name})'
    rowadd.append(f'| {date} | {link} | {result.replace("|","/")} |')
    head=f'### {case} — {date}\n\n{link}\n\n'
    demote=lambda s:re.sub(r'^(#{3,5}) ',lambda m:'#'+m[1]+' ',s,flags=re.M)
    laws.append(head+'\n\n'.join(demote(section(pub,h)) for h in ['Holdings','Precedent Treatment','Law After Decision'] if section(pub,h)))
    # Records expose every published position in this bounded continuity block.
    continuity=section(t,'Published noncontrolling positions')
    if not continuity:continuity=section(pub,'Separate Writings')
    if continuity and not re.match(r'^(?:None\.?$|No separate writings?(?: issues)?\.?$|No separate opinion(?: or other published noncontrolling position)?(?: issues)?\.|None issued\.?$)',continuity,re.I):positions.append(head+demote(continuity))
    procedures.append(head+section(pub,'Judgment & Remedy')+'\n\n'+section(pub,'Procedure After Action'))

for name,heads in [('continuity.md',['Completed Events and Admitted Sources','Current Law','Material Published Noncontrolling Positions','Current Procedure and Institution']),('neutral-projection.md',['Completed public events and admitted sources','Current-term law','Published noncontrolling positions','Current public procedure and institution'])]:
    s=(T/'runtime'/('OT_1999CHUNK8_OPENING_'+name)).read_text(encoding='utf-8')
    s=s.replace('84 Court events',f'{count} Court events')
    s=s.replace('72 through chunk 6 and 12 in chunk 7.',f'72 through chunk 6, 12 in chunk 7 and {len(records)} in chunk 8.')
    s=s.replace('The chronology cursor is 2000-06-12.',f'The chronology cursor is {cursor}.')
    old='The next unresolved scheduled item in effective-date and case-name order is Bradley v. Arkansas Department of Education on 2000-06-12. The uncoordinated June 12 matters share the same entering-law baseline.'
    next_text=f'The next open scheduled item is {next_event[1]} on {next_event[0]}, subject to its ordinary intake and dependency checks.' if next_event else 'No remaining open scheduled inventory item is identified.'
    new=f'Chunk 8 has {len(records)} completed events; unadjudicated matters retain their actual open status in the manifest. {next_text} Uncoordinated same-date matters share entering law and operate together only prospectively.'
    s=s.replace(old,new)
    for h,bodies in zip(heads,[rowadd,laws,positions,procedures]):
        if bodies:s=add(s,h,'\n'.join(bodies) if h==heads[0] else '\n\n'.join(bodies))
    # Sort the completion table by effective date and natural case caption.
    h=heads[0];body=section(s,h);lines=body.splitlines()
    rows=[x for x in lines if re.match(r'^\| \d{4}-',x)]
    if rows:
        sortedrows=sorted(rows,key=lambda x:(x.split('|')[1].strip(),re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',x.split('|')[2]).strip()))
        prefix=[x for x in lines if x not in rows and x.strip()]
        replacement='\n'.join(prefix+sortedrows)
        s=re.sub(r'(^## '+re.escape(h)+r'\s*\n).*?(?=^## |\Z)',lambda m:m[1]+'\n'+replacement+'\n\n',s,count=1,flags=re.M|re.S)
    if name=='continuity.md':
        msg='Chunk 8: '+( '; '.join(k+': '+v for k,v in stops.items()) if stops else 'No adjudicative blocker recorded for the completed events; unprocessed inventory items remain open.')+' Repository-history checks and commitment remain with the operator; no Git command was run.'
        s=add(s,'Blockers and Revalidation Needs',msg)
        s=add(s,'Source and Research Cutoff',f'Chunk 8 extends completed current-term law through {cursor}. Each Record preserves its event-date cutoff, actual source limits and frozen-stage lineage. No follow-on event is presumed. The generated Render Input projects only completed Records; public Render remains a separate task.')
    elif stops:
        s=add(s,'Current public procedure and institution','Unresolved chunk 8 matters: '+ '; '.join(stops)+'. No Court disposition, new procedural order or doctrinal consequence is entered for these matters.')
    (T/'workspace'/name).write_text(s.rstrip()+'\n',encoding='utf-8')
print('Projected',len(records),'chunk 8 Records; cursor',cursor)

for group,cutoff in [('B','2000-06-19'),('C','2000-06-26')]:
    parts=[f'# Chunk 8 effective earlier public decisions for {group}','', 'Mechanically copied Public Projections. These supply law only from their event dates; same-day peers do not govern one another.']
    for date,case,p,result,t,pub in records:
        if date<cutoff:parts+=['','## '+case+' — '+date,'',pub.strip()]
    (T/'entering-law'/f'OT_1999CHUNK8_{group}_EARLIER_PUBLIC.md').write_text('\n'.join(parts)+'\n',encoding='utf-8')
