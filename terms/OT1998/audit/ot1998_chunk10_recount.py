#!/usr/bin/env python3
"""Fresh clerical lead-author recount; classification is supplied by canonical Records."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
sys.dont_write_bytecode = True
ROOT = Path(__file__).absolute().parents[3]
TERM = ROOT / 'terms' / 'OT1998'
JUSTICES = ('Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer')
def normal(s): return s.replace('’', "'").replace('‘', "'")
def table_authors(lines):
    found=set()
    for line in lines:
        if not line.lstrip().startswith('|'): continue
        cells=[normal(x.strip()) for x in line.strip().strip('|').split('|')]
        if len(cells)<2 or not re.match(r'(?:Opinion of the Court|Lead opinion|Opinion announcing the judgment)\b',cells[0],re.I): continue
        for name in JUSTICES:
            if re.search(r'(?<!\w)'+re.escape(name)+r'(?!\w)',cells[1]): found.add(name)
    return found

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--date',required=True)
    ap.add_argument('--caption',required=True)
    ap.add_argument('--output',required=True,type=Path)
    args=ap.parse_args()
    output=args.output.absolute()
    if not output.is_relative_to(TERM/'freeze'): raise SystemExit('Output must be in this term freeze directory')
    if output.exists(): raise SystemExit('Preserve prior recount; supply a new output filename')
    base=json.loads((TERM/'freeze/OT_1998CHUNK10_ASSIGNMENT_BASELINE.json').read_text())
    source_map={x['source_file']:x for x in base['sources']}
    counts=Counter({j:0 for j in JUSTICES}); rows=[]
    for path in sorted((TERM/'records').glob('*.md')):
        text=path.read_text()
        cm=re.search(r'^\*\*Case and dockets:\*\*\s*(.+)$',text,re.M)
        em=re.search(r'^\*\*Event and date:\*\*\s*(.+)$',text,re.M)
        if not cm or not em: raise SystemExit('Missing identity: '+path.name)
        date=re.search(r'\d{4}-\d{2}-\d{2}',em[1])[0]
        caption=cm[1].split(';')[0].split(', No.')[0].rstrip('.')
        if (date,normal(caption).casefold()) >= (args.date,normal(args.caption).casefold()): continue
        old=source_map.get(path.name)
        if old:
            qualifying=old['qualifying']; evidence=[x['quote'] for x in old['quoted_extracts']['opinion_authorship']]
            if any(q not in text for q in evidence): raise SystemExit('Prior author evidence changed: '+path.name)
            authors=table_authors(evidence) if qualifying else set()
            if qualifying and old['author_source']!='opinion-table rows':
                authors=set(old['actual_lead_authors'])
                if any(not any(name in normal(q) for q in evidence) for name in authors): raise SystemExit('Narrative author evidence missing')
            if authors != (set(old['actual_lead_authors']) if qualifying else set()):
                raise SystemExit('Author extraction disagreement: '+path.name+' '+repr(authors))
        else:
            marker=re.search(r'^\*\*Counted lead opinion:\*\*\s*(Yes|No)\b',text,re.M|re.I)
            if not marker: raise SystemExit('New Record needs explicit human form classification: '+path.name)
            qualifying=marker[1].lower()=='yes'
            evidence=[line for line in text.splitlines() if line.lstrip().startswith('|') and re.search(r'Opinion of the Court|Lead opinion|Opinion announcing the judgment',line,re.I)]
            authors=table_authors(evidence) if qualifying else set()
            if qualifying and not authors: raise SystemExit('No actual lead author table: '+path.name)
        rows.append({'record':path.name,'date':date,'caption':caption,'qualifying':qualifying,'authors':sorted(authors,key=JUSTICES.index),'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'author_evidence':evidence})
    rows.sort(key=lambda x:(x['date'],normal(x['caption']).casefold(),x['record']))
    for row in rows:
        for name in row['authors']:counts[name]+=1
    counted=[x for x in rows if x['qualifying']]
    result={'before_date':args.date,'before_caption':args.caption,'method':'Recount from zero using exact unchanged canonical author evidence and current new Record opinion-table authors; prior tallies never used. Human supplied form classification only.','counts':dict(counts),'record_count':len(rows),'counted_opinions':len(counted),'last_counted':counted[-1]['record'] if counted else None,'sources':rows}
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'counts':dict(counts),'counted_opinions':len(counted),'last_counted':result['last_counted'],'output':str(output)},ensure_ascii=False))
if __name__=='__main__':main()
