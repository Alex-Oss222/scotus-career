"""Assembly formatting and deterministic checks only; no legal inference."""
from pathlib import Path
import re
import json

TERM = Path(__file__).resolve().parents[1]
NAMES = ['Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']
BLOCKS = ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']

def recount(date, case):
    prior=[]
    counts=dict.fromkeys(NAMES,0)
    for p in (TERM/'records').glob('*.md'):
        s=p.read_text(encoding='utf-8-sig')
        d=re.search(r'^\*\*Event and date:\*\*.*?(\d{4}-\d{2}-\d{2})',s,re.M).group(1)
        c=re.search(r'^\*\*Case and dockets:\*\* (.+)',s,re.M).group(1).split(';')[0]
        if (d,c.casefold()) >= (date,case.casefold()):
            continue
        if '**Counted signed plenary lead:** Yes' not in s:
            continue
        table=s.split('## OPINION TABLE\n',1)[1].split('\n## ',1)[0]
        authors=[]
        for row in table.splitlines():
            if row.startswith('| Signed lead'):
                a=row.split('|')[2].strip()
                assert a in NAMES,(p,a)
                if a not in authors: authors.append(a)
        assert authors,p
        prior.append((d,c,p.name,authors))
    for d,c,p,aa in sorted(prior):
        for a in aa: counts[a]+=1
    return counts,sorted(prior)

def write_record(data_path, author, eligible, fit, count=True, assigner='Stone-Zsela'):
    data=json.loads(Path(data_path).read_text(encoding='utf-8-sig'))
    p=TERM/'records'/data['filename']
    assert not p.exists(),f'Will not replace existing Record: {p.name}'
    counts,prior=recount(data['date'],data['case'])
    pool=[n for n in eligible if counts[n] <= min(counts[e] for e in eligible)+1] if eligible else []
    if assigner=='Stone-Zsela' and author!='Per curiam': assert author in pool,(author,pool)
    last=f'{prior[-1][1]}, {prior[-1][0]} ({prior[-1][2]})' if prior else 'No counted event precedes this assignment.'
    count_text='; '.join(f'{n}: {counts[n]}' for n in NAMES)+'.'
    assignment=f'''## Assignment and final compatibility

**Form first:** {data['form']}

**Assignment authority:** {assigner}. {data.get('assignment_basis','The Chief is in the judgment coalition.')}

**Recount from actual earlier Record opinion tables:** {count_text}

**Last counted event:** {last}

**Eligible authors:** {', '.join(eligible) if eligible else 'No individual author; institutional per curiam disposition.'}

**Balance pool:** {', '.join(pool) if pool else 'Not applicable to this per curiam disposition.'}

**Author selected:** {author}. {fit}

**Final compatibility:** {data['compatibility']}
'''
    def fill(value):
        return value.replace('{AUTHOR}',author).replace('{FULL_JOINERS}',', '.join(n for n in data.get('lead_support',[]) if n!=author))
    topology=fill(data['blocks']['Opinion Topology'])
    internal_table=topology
    if count: internal_table=internal_table.replace('| Opinion of the Court |','| Signed lead — Opinion of the Court |').replace('| Opinion announcing the judgment |','| Signed lead — Opinion announcing the judgment |')
    projection='\n\n'.join('## '+b+'\n\n'+fill(data['blocks'][b]) for b in BLOCKS)
    annex=''
    if data.get('reconciled_start'):
        full=(TERM/'freeze'/data.get('reconciled_file','OT_1999CHUNK1_RECONCILED.md')).read_text(encoding='utf-8-sig')
        start=full.index(data['reconciled_start'])
        end=full.index(data['reconciled_end'],start) if data.get('reconciled_end') else len(full)
        annex=full[start:end].strip()
    for extra in data.get('annex_files',[]):
        annex+='\n\n'+(TERM/'freeze'/extra).read_text(encoding='utf-8-sig').strip()
    text=f'''**Case and dockets:** {data['case']}; {data['docket']}
**Event and date:** {data['event']}, {data['date']}; October Term 1999, chunk 1.
**Result:** {data['result']}
**Version / lineage:** Original decision. Durable file handoff; no repository commit is asserted.

## Event, participation, and entering law

{data['kernel']}

All nine Justices participate at submission and decision: Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, and Breyer. The nine-member Court has a quorum; five votes supply a majority. No recusal or nonparticipation is supplied.

## Stone's approved position and final action

{data['stone']}

## OPINION TABLE

{internal_table}

**Counted signed plenary lead:** {'Yes' if count else 'No'}

{assignment}
## Controlling decision kernel and continuity

The controlling holdings, proposition-level authority, exact judgment and remedy, precedent treatment, and post-action stage are the bounded Public Projection below; they are part of this canonical kernel without alteration. {data['continuity']}

## Sources, research cutoff, and validation

{data['sources']}

Research cutoff: {data['date']}. The frozen neutral packet, neutral validation, supplements and final reconciled handoff govern the identified source limits. Original-record facts, published recitations, reconstructed scheduling and this Court's legal conclusions remain distinct. No later historical action is admitted. Local validation checks the four opening labels, eleven-block order, authored topology, assignment arithmetic from actual earlier opinion tables, and durable sequence; the operator performs the coordinated workspace and term checks. Durably preserved October 31, 2026, for current-term integration. No Git command or repository-commit verification is performed by assembly.

## Adaptive audit annex

The following applicable final reconciled section is copied mechanically from the frozen handoff. It supplies each non-Stone Justice's ground, historical reconciliation, and limits. Assignment and final Stone compatibility above are assembly conclusions; no non-Stone commitment is silently changed.

{data.get('audit_extra','')}

{annex}

## Public Projection

{projection}
'''
    assert re.findall(r'^## (.+)$',text.split('## Public Projection\n',1)[1],re.M)==BLOCKS
    assert '{AUTHOR}' not in text and '{FULL_JOINERS}' not in text
    assert '\\Users\\' not in text and 'onedrive' not in text.lower() and 'github.com' not in text.lower()
    p.write_text(text,encoding='utf-8')
    order=TERM/'runtime'/'OT_1999CHUNK1_RECORD_ORDER.txt'
    with order.open('a',encoding='utf-8') as f:f.write(p.name+'\n')
    print(json.dumps({'record':p.name,'author':author,'counts_before':counts,'pool':pool,'counted':count},ensure_ascii=False))
    return p
