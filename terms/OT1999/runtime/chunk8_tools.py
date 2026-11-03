from pathlib import Path
import argparse
import importlib.util
import json
import re
import sys

sys.dont_write_bytecode = True
ROOT=Path(__file__).resolve().parents[3]
TERM=ROOT/'terms/OT1999'
NAMES=['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']

def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'tools'/(name+'.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def counts(date,case):
    counts={n:0 for n in NAMES};events=[]
    case_key=case.strip().rstrip('.')
    for p in (TERM/'records').glob('*.md'):
        t=p.read_text(encoding='utf-8')
        cm=re.search(r'^\*\*Case and dockets:\*\*\s*(.*)',t,re.M)
        em=re.search(r'^\*\*Event and date:\*\*\s*(.*)',t,re.M)
        if not cm or not em: continue
        when=re.search(r'\d{4}-\d{2}-\d{2}',em[1])[0]
        caption=cm[1].split(';')[0].strip().rstrip('.')
        if (when,caption)>=(date,case_key) or not re.search(r'plenary|merits',em[1],re.I) or re.search(r'summary',em[1],re.I): continue
        pub=t.split('## Public Projection',1)[-1]
        m=re.search(r'^## (?:\d+\. )?Opinion Topology\s*\n(.*?)(?=^## |\Z)',pub,re.M|re.S)
        if not m: raise RuntimeError('No opinion topology: '+p.name)
        authors=[]
        for row in (t.split('## Public Projection',1)[0]+'\n'+m[1]).splitlines():
            cells=[c.strip() for c in row.strip().strip('|').split('|')]
            if len(cells)<3 or not row.startswith('|'): continue
            if re.search(r'opinion of the Court|Court opinion|opinion.*announc|\blead\b',cells[0],re.I) and not re.search('per curiam',cells[0]+' '+cells[1],re.I):
                for n in NAMES:
                    if n in cells[1] and n not in authors: authors.append(n)
        if not authors and not re.search(r'per curiam',m[1],re.I):
            prose=re.search(r'(?:Chief Justice|Justice)\s+([A-Za-z\x27\u2019-]+)\s+(?:delivers|delivered|writes|wrote)\s+(?:the\s+)?(?:opinion of the Court|opinion announcing)',m[1],re.I)
            if prose and prose[1].replace('\u2019',"'") in NAMES: authors.append(prose[1].replace('\u2019',"'"))
            else: raise RuntimeError('Unparsed counted topology: '+p.name+'\n'+m[1])
        if authors: events.append({'date':when,'case':caption,'record':p.name,'authors':authors})
    events.sort(key=lambda e:(e['date'],e['case']))
    for e in events:
        for n in e['authors']:counts[n]+=1
    return {'before_date':date,'before_case':case,'counts':counts,'total':sum(counts.values()),'last_event':events[-1] if events else None,'counted_events':events}

def check():
    mod=load('check_term');skipped=[]
    # Preserve the supplied nine-column index and annotated date cells.
    mod.INDEX_CASE_ROW=re.compile(r'^\|\s*\d+\s*\|\s*\d+\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})',re.M)
    def no_git(root,sha):
        skipped.append(sha)
        return True
    mod.git_object_exists=no_git
    sys.argv=['check_term.py','OT1999']
    try: mod.main()
    finally: print('NOT PERFORMED: Git commit-reference existence; user prohibits all Git commands. References bypassed:',len(set(skipped)))

def ledger():
    mod=load('rebuild_ledger')
    old=(TERM/'runtime/OT_1999CHUNK8_OPENING_ledger.md').read_text(encoding='utf-8')
    indexed={}
    for row in old.splitlines():
        m=re.search(r'\[record\]\(../records/([^)]*)\)',row)
        if m:
            cells=[c.strip() for c in row.strip('|').split('|')]
            indexed[m[1]]=(int(cells[0]),cells[-2])
    new=[]
    for p in (TERM/'records').glob('*.md'):
        if p.name not in indexed:
            d=mod.parse(p);new.append((d['date'],d['case'],p.name))
    for n,(_,_,filename) in enumerate(sorted(new),len(indexed)+1):indexed[filename]=(n,'Not queried: Git prohibited')
    mod.git_added=lambda root,path:indexed[path.name]
    sys.argv=['rebuild_ledger.py','OT1999'];mod.main()
    p=TERM/'workspace/ledger.md';s=p.read_text(encoding='utf-8')
    s=s.replace('Generated from canonical Records in Git commitment order. Records control if this index conflicts with them.','Generated from canonical Records without Git access. Records control if this index conflicts with them. Existing index order and first-record references are preserved without independent verification. Newly indexed Records are appended in effective-date and case-name order; the displayed order does not establish Git commitment order. No new commit reference is asserted.')
    s=s.replace('| Commit order |','| Recorded order |').replace('| First-record commit |','| Recorded first-record commit |')
    p.write_text(s,encoding='utf-8')

def manifest():
    mod=load('rebuild_manifest')
    def inventory(path,year):
        rows=[]
        for line in path.read_text(encoding='utf-8').splitlines():
            if not re.match(r'^\|\s*\d+\s*\|',line):continue
            c=[x.strip() for x in line.strip().strip('|').split('|')]
            if len(c)!=9 or not c[1].isdigit():raise ValueError('Unexpected case-index row')
            dm=re.match(r'(\d{4}-\d{2}-\d{2})(.*)',c[4])
            if not dm:raise ValueError('Missing inventory date')
            rows.append((dm[1],f'OT_{year}CHUNK{c[1]}',c[2],c[3],c[6],dm[2].strip(' -\u2014')+'; '+c[5]))
        if len(rows)!=104:raise ValueError(f'Expected 104 supplied inventory rows, found {len(rows)}')
        return sorted(rows,key=lambda r:r[0])
    mod.inventory=inventory
    sys.argv=['rebuild_manifest.py','OT1999']
    path=TERM/'runtime/OT_1999CHUNK8_STOPS.json'
    stops=json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    for case,reason in stops.items():sys.argv+=['--stopped',case+'='+reason]
    mod.main()

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('operation',choices=['counts','check','ledger','manifest']);ap.add_argument('--date');ap.add_argument('--case');ap.add_argument('--out');a=ap.parse_args()
    if a.operation=='counts':
        result=counts(a.date,a.case)
        if a.out:Path(a.out).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({k:v for k,v in result.items() if k!='counted_events'},indent=2))
    elif a.operation=='check':check()
    elif a.operation=='ledger':ledger()
    else:manifest()
