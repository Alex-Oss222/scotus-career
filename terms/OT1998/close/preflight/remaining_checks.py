#!/usr/bin/env python3
"""First-pass deterministic checks beyond check_term. No adjudication or repair."""
from collections import Counter, deque
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import sys
from urllib.parse import urlsplit, unquote

sys.dont_write_bytecode = True
ROOT = Path(__file__).absolute().parents[4]
TERM = ROOT / 'terms/OT1998'
OUT = TERM / 'close/preflight'
def forbidden(value):
    return any(p.casefold() in ('stone', '.git') or p.upper().startswith('MASTER_JURISPRUDENCE')
               for p in Path(os.path.abspath(os.fsdecode(value))).parts)
def guard(event, args):
    if event in {'subprocess.Popen', 'os.system', 'os.posix_spawn'} or event.startswith(('os.exec', 'os.spawn')):
        raise PermissionError('Subprocess blocked')
    if event in {'open', 'os.listdir', 'os.scandir'} and args and isinstance(args[0], (str, bytes, os.PathLike)) and forbidden(args[0]):
        raise PermissionError('Forbidden source blocked')
    if event == 'open':
        p, mode, flags = args
        write = (isinstance(mode, str) and any(c in mode for c in 'wax+')) or (isinstance(flags, int) and flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND))
        if write and (not isinstance(p, (str, bytes, os.PathLike)) or not Path(os.path.abspath(os.fsdecode(p))).is_relative_to(OUT)):
            raise PermissionError('Write outside preflight blocked')
    if event in {'os.remove','os.unlink','os.rmdir','os.mkdir','os.rename','os.replace','os.link','os.symlink','os.truncate','os.chmod'}:
        raise PermissionError('Mutation blocked')
sys.addaudithook(guard)
lib = runpy.run_path(str(TERM / 'audit/ot1998_chunk11_publication_manifest.py'), run_name='preflight_link_library')
read = lib['read_bytes']
decode = lambda rel: read(rel).decode('utf-8-sig')
rel = lambda p: p.relative_to(ROOT).as_posix()
records = {p.name: p for p in sorted((TERM/'records').glob('*.md')) if not p.name.startswith('.')}
report = {'phase': 'First deterministic preflight only', 'errors': [], 'record_count': len(records)}
def table(text, heading):
    lines = text.splitlines()
    start = next(i for i,line in enumerate(lines) if line.startswith(heading))
    cols = [x.strip() for x in lines[start].strip('|').split('|')]
    rows = []
    for i in range(start+2, len(lines)):
        if not lines[i].startswith('|'): break
        values = [x.strip() for x in lines[i].strip('|').split('|')]
        if len(values) != len(cols):
            raise ValueError('Unexpected table width at line '+str(i+1))
        rows.append((i+1,dict(zip(cols,values))))
    return rows
manifest = decode('terms/OT1998/workspace/manifest.md')
scheduled = table(manifest, '| Event date | Chunk | Case or matter |')
carried = table(manifest, '| Event date | Case or matter | Event type / current stage |')
admitted = table(manifest, '| Effective date | Source event |')
source_names = []
court_names = []
record_dates = {}
for name,p in records.items():
    text = p.read_text()
    event = next(line for line in text.splitlines()[:12] if line.startswith('**Event and date:**'))
    date = re.search(r'\d{4}-\d{2}-\d{2}', event)[0]
    record_dates[name] = date
    if not name.endswith(date+'.md'):
        report['errors'].append({'type':'Record date/name mismatch','path':rel(p),'date':date})
for line,row in scheduled:
    names = re.findall(r'[\w.()-]+\.md', row['Status'] if row['Status'].startswith('Completed:') else '')
    names += re.findall(r'[\w.()-]+\.md', row['Completed component Records'])
    names = list(dict.fromkeys(names))
    court_names.extend(names)
    for name in names:
        if name not in record_dates or record_dates[name] != row['Event date']:
            report['errors'].append({'type':'manifest/Record date mismatch','line':line,'record':name,'manifest_date':row['Event date'],'record_date':record_dates.get(name)})
for line,row in admitted:
    source_names += re.findall(r'[\w.()-]+\.md', row['Status'])
all_names = court_names + source_names
report['inventory'] = {'scheduled_items':len(scheduled),'undated_carryovers':len(carried),'scheduled_status_counts':dict(Counter(r['Status'].split(':')[0] for _,r in scheduled)),
    'court_records_reconciled':len(court_names),'admitted_source_records':len(source_names),
    'unrepresented_records':sorted(set(records)-set(all_names)), 'missing_records':sorted(set(all_names)-set(records)),
    'duplicate_record_assignments':[n for n,c in Counter(all_names).items() if c>1]}
for key in ('unrepresented_records','missing_records','duplicate_record_assignments'):
    if report['inventory'][key]:report['errors'].append({'type':key,'values':report['inventory'][key]})
dates = [r['Event date'] for _,r in scheduled]
report['manifest_date_order_pass'] = dates == sorted(dates)
if dates != sorted(dates): report['errors'].append({'type':'manifest is not in effective-date order'})
continuity_rows = table(decode('terms/OT1998/workspace/continuity.md'), '| Effective date | Matter | Disposition | Canonical Record |')
cont_names = [re.search(r'\.\./records/([^/#)]+)',r['Canonical Record'])[1] for _,r in continuity_rows]
cont_dates = [r['Effective date'] for _,r in continuity_rows]
report['continuity'] = {'completed_table_rows':len(cont_names),'missing_records':sorted(set(records)-set(cont_names)),
    'extra_records':sorted(set(cont_names)-set(records)), 'effective_date_order_pass':cont_dates==sorted(cont_dates)}
if set(cont_names)!=set(records):report['errors'].append({'type':'continuity Record coverage','details':report['continuity']})
if cont_dates != sorted(cont_dates): report['errors'].append({'type':'continuity is not in effective-date order'})
ledger_rows=table(decode('terms/OT1998/workspace/ledger.md'),'| Local entry order | Effective date |')
ledger_names=[re.search(r'\.\./records/([^/#)]+)',r['Record'])[1] for _,r in ledger_rows]
report['ledger']={'rows':len(ledger_names),'coverage_pass':len(ledger_names)==len(set(ledger_names)) and set(ledger_names)==set(records),
    'order_scope':'Local entry order intentionally differs from effective chronology; not an adjudication chronology defect'}
if not report['ledger']['coverage_pass']:report['errors'].append({'type':'ledger coverage'})
report['open_matters']=[{'line':line,'matter':row['Case or matter'],'status':row['Status'],'stage':row['Current stage']} for line,row in scheduled if row['Status'].startswith('Open')]
report['open_matters'] += [{'line':line,'matter':row['Case or matter'],'status':row['Status'],'stage':row['Event type / current stage']} for line,row in carried]
report['candidate_dependent_checks']='Pending complete synchronized Holdings, Standards and Tests, and Standing State candidates; explicit next-term carry-forward of 14 unresolved matters; cutoff/edition synchronization, controlling-authority coverage, anchors, and candidate cleanup at completed close.'

# Core active artifacts plus directly linked same-term dependencies. Prior-term
# targets are checked for existence/anchors without recursively reopening them.
primary = {'terms/OT1998/case-list.md'}
for dirname in ('records','workspace','render-inputs','output','entering-law','briefs'):
    primary.update(rel(p) for p in (TERM/dirname).glob('*.md') if not forbidden(p))
primary.update('state/'+name for name in ('HOLDINGS.md','STANDARDS_AND_TESTS.md','STANDING_STATE.md'))
primary.update(rel(p) for p in (ROOT/'state/holdings').glob('*.md'))
contexts={}
prior_checks=json.loads(read('terms/OT1998/audit/OT_1998CHUNK11_PUBLICATION_CHECKS.json'))
for item in prior_checks['snapshot_context_links']:
    contexts[(item['source'],item['link'])]=item['baseline_source']
for chunk in (10,11):
    for label,name in (('MANIFEST','manifest'),('LEDGER','ledger'),('CONTINUITY','continuity'),('NEUTRAL_PROJECTION','neutral-projection')):
        contexts[('terms/OT1998/freeze/OT_1998CHUNK'+str(chunk)+'_OPENING_'+label+'.md',None)]='terms/OT1998/workspace/'+name+'.md'
pending=deque(sorted(primary));seen=set();anchor_cache={};link_issues=[];context_links=[];forbidden_skipped=[];external=0;local=0
while pending:
    source=pending.popleft()
    if source in seen:continue
    seen.add(source)
    raw=read(source)
    for target,line in lib['destinations'](raw):
        source_context=contexts.get((source,target),contexts.get((source,None),source))
        original_target=target
        parsed=urlsplit(target)
        if parsed.scheme or target.startswith('//'):
            prefix='/Alex-Oss222/scotus-career/blob/main/'
            if parsed.netloc.lower()=='github.com' and parsed.path.startswith(prefix):
                target='/'+parsed.path[len(prefix):]+('#'+parsed.fragment if parsed.fragment else '')
            else:
                external+=1
                continue
        try:
            result=lib['resolve_target'](source_context,target)
            if result is None:continue
            dest,anchor=result
            local+=1
            if source_context!=source:context_links.append({'source':source,'line':line,'link':original_target,'original_context':source_context,'target':dest})
            path=lib['safe_path'](dest)
            if not path.exists():
                link_issues.append({'source':source,'line':line,'link':original_target,'target':dest,'issue':'missing file','scope':'core' if source in primary else 'linked dependency'})
                continue
            if anchor and dest.lower().endswith('.md'):
                if dest not in anchor_cache:anchor_cache[dest]=lib['anchors'](read(dest))
                if anchor not in anchor_cache[dest]:link_issues.append({'source':source,'line':line,'link':original_target,'target':dest,'anchor':anchor,'issue':'missing anchor','scope':'core' if source in primary else 'linked dependency'})
            if dest.startswith('terms/OT1998/') and dest.endswith('.md') and '/close/' not in dest and path.is_file():pending.append(dest)
        except lib['UnsafePath'] as exc:
            forbidden_skipped.append({'source':source,'line':line,'link':original_target,'reason':str(exc)})
report['links']={'primary_files':len(primary),'markdown_files_inspected':len(seen),'local_links_checked':local,'external_links_not_network_rechecked':external,
    'unresolved':link_issues,'relocated_context_links':context_links,'forbidden_or_unsafe_targets_not_accessed':forbidden_skipped,
    'scope':'Active term corpus and directly linked same-term dependency closure, plus opening trackers; prior-term targets existence and anchors only. External authority sites were not recrawled.'}
report['read_identities']=[{'path':p,'sha256':hashlib.sha256(read(p)).hexdigest()} for p in sorted(seen)]
(OUT/'remaining_checks.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('read_identities','links')},indent=2,ensure_ascii=False))
print(json.dumps({k:(len(v) if isinstance(v,list) else v) for k,v in report['links'].items()},indent=2))
