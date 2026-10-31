from pathlib import Path
import re,json
from assembly_record_writer import TERM,BLOCKS,NAMES,recount
order=(TERM/'runtime'/'OT_1999CHUNK1_RECORD_ORDER.txt').read_text().splitlines()
assert len(order)==9 and len(set(order))==9
rows=[]
for name in order:
    p=TERM/'records'/name
    s=p.read_text(encoding='utf-8')
    labels=['**Case and dockets:**','**Event and date:**','**Result:**','**Version / lineage:**']
    assert all(s.splitlines()[i].startswith(label+' ') for i,label in enumerate(labels)),name
    assert re.search(r'_[a-z-]+_\d{4}-\d{2}-\d{2}\.md$',name),name
    proj=s.split('## Public Projection\n',1)[1]
    assert re.findall(r'^## (.+)$',proj,re.M)==BLOCKS,name
    assert not re.search(r'\{AUTHOR\}|\{FULL_JOINERS\}|PENDING REMEDY|must be screened at release|pending clarification',s),name
    assert not re.search(r'simulat|user.directed|October 31, 2026|reconciliation|provisional|workflow|Git commit',proj,re.I),name
    case=re.search(r'^\*\*Case and dockets:\*\* (.+)',s,re.M).group(1).split(';')[0]
    date=re.search(r'^\*\*Event and date:\*\*.*?(\d{4}-\d{2}-\d{2})',s,re.M).group(1)
    counts,prior=recount(date,case)
    line=re.search(r'^\*\*Recount from actual earlier Record opinion tables:\*\* (.+)',s,re.M).group(1)
    for justice in NAMES:assert f'{justice}: {counts[justice]}' in line,(name,justice)
    topo=s.split('## OPINION TABLE\n',1)[1].split('\n## ',1)[0]
    public_topo=proj.split('## Opinion Topology\n',1)[1].split('\n## ',1)[0].strip()
    internal_topo=topo.split('\n**Counted signed plenary lead:**',1)[0].strip().replace('Signed lead — ','')
    assert internal_topo==public_topo,name
    counted='**Counted signed plenary lead:** Yes' in s
    authors=[r.split('|')[2].strip() for r in topo.splitlines() if r.startswith('| Signed lead')]
    assert bool(authors)==counted,name
    rows.append({'file':name,'date':date,'case':case,'counted':counted,'authors':authors})
assert [(x['date'],x['case'].casefold()) for x in rows]==sorted((x['date'],x['case'].casefold()) for x in rows)
counts,prior=recount('9999-12-31','ZZZ')
assert sum(counts.values())==6
with (TERM/'runtime'/'OT_1999CHUNK1_ASSEMBLY_VALIDATION.md').open('a',encoding='utf-8') as f:
    f.write('\nFinal local deterministic pass: nine unique natural-key Records; exact four opening labels; exact eleven level-two projection blocks; no unresolved draft placeholders or identified public workflow terms; chronological/alphabetical durable order; every preassignment all-nine tally recomputed from actual earlier opinion tables; internal/public topology identity; six counted signed merits leads. Fiore remains excluded as procedural despite its signed opinion. No Git operation was used. Coordinated workspace/native term validation remains the root operator’s task.\n\nFinal actual opinion counts: '+json.dumps(counts,ensure_ascii=False)+'.\n')
print(json.dumps({'records':rows,'counts':counts},ensure_ascii=False,indent=2))
