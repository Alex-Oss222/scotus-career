from pathlib import Path
import re
import sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
TERM=ROOT/'terms/OT1999'
parts=['# Current-term opinion and assignment reading copy','', 'Only event identity, opinion topology and assignment statements are copied. Records remain authoritative. Recount before each new assignment; this export is not a running tally.','']
events=[]
for p in (TERM/'records').glob('*.md'):
    t=p.read_text(encoding='utf-8')
    cm=re.search(r'^\*\*Case and dockets:\*\*.*$',t,re.M)
    em=re.search(r'^\*\*Event and date:\*\*.*$',t,re.M)
    if not cm or not em:continue
    date=re.search(r'\d{4}-\d{2}-\d{2}',em[0])[0]
    entries=[cm[0],em[0]]
    pub=t.split('## Public Projection',1)[-1]
    m=re.search(r'^## (?:\d+\. )?Opinion Topology\s*\n(.*?)(?=^## |\Z)',pub,re.M|re.S)
    if m:entries+=['### Opinion topology',m[1].strip()]
    internal=t.split('## Public Projection',1)[0]
    for m in re.finditer(r'^## ([^\n]*assignment[^\n]*)\n(.*?)(?=^## |\Z)',internal,re.M|re.S|re.I):
        entries+=['### '+m[1],m[2].strip()]
    tables=re.finditer(r'^\| Writing \|[^\n]*\n(?:\|[^\n]*\n)+',internal,re.M)
    for m in tables:entries+=['### Record opinion table',m[0].strip()]
    events.append((date,cm[0],p.name,entries))
for _,_,name,entries in sorted(events):parts+=['## '+name,'']+entries+['']
(TERM/'runtime/OT_1999CHUNK8_PRIOR_OPINIONS.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
print(len(events),'Record opinion/assignment entries exported')
