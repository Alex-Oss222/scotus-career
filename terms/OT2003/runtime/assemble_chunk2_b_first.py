from pathlib import Path
import re, hashlib, json

BASE = Path('terms/OT2003')
NAMES = ['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']
BLOCKS = ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']

def read(p):
    return (BASE/p).read_text(encoding='utf-8-sig')

def section(s,n):
    return re.search(r'^## '+str(n)+r'\..*?(?=^## \d+\.|\Z)',s,re.M|re.S).group().strip()

def topo(s):
    if '## Public Projection' in s:
        s=s.split('## Public Projection',1)[1]
    return re.search(r'^## Opinion Topology\n(.*?)(?=^## |\Z)',s,re.M|re.S).group(1).strip()

def recount():
    sources=[]
    prior=read(Path('runtime/OT_2003CHUNK2_PRIOR_OPINION_TABLES.md'))
    for b in re.split(r'(?m)^# ',prior):
        filename=b.splitlines()[0] if b else ''
        if not filename.endswith('.md'):continue
        sources.append((filename,topo(b)))
    for filename in CREATED:
        sources.append((filename,topo(read(Path('records')/filename))))
    counts=dict.fromkeys(NAMES,0)
    trace=[]
    for filename,t in sources:
        if 'per curiam' in t.lower():
            trace.append((filename,'per curiam; excluded'))
            continue
        m=re.search(r"^([A-Z'’\-]+), (?:C\. J\.|J\.), (?:delivered|announced)",t)
        assert m, filename
        author=next(n for n in NAMES if n.upper().replace('’',"'")==m.group(1).replace('’',"'"))
        counts[author]+=1
        trace.append((filename,author))
    return counts,trace

CREATED=[]
VALIDATION=[]

def build(d):
    # The legal form and parts in d are fixed before this fresh recount.
    counts,trace=recount()
    minimum=min(counts[n] for n in d['eligible'])
    pool=[n for n in d['eligible'] if counts[n]<=minimum+1]
    assert d['author'] in pool
    count_table='| Justice | Count before assignment | Eligible for complete lead | Balance pool |\n|---|---:|---|---|\n'+'\n'.join(f"| {n} | {counts[n]} | {'Yes' if n in d['eligible'] else 'No'} | {'Yes' if n in pool else 'No'} |" for n in NAMES)
    trace_text='\n'.join(f'- `{f}`: {a}.' for f,a in trace)
    neutral=section(read(Path('freeze/OT_2003CHUNK2_NEUTRAL.md')),d['number'])
    stone=section(read(Path('runtime/OT_2003CHUNK2_STONE.md')),d['number'])
    commitment=read(Path(f"freeze/OT_2003CHUNK2_{d['key']}_COMMITMENTS.md"))
    reconciled=read(Path(f"freeze/OT_2003CHUNK2_{d['key']}_RECONCILED.md"))
    public='\n\n'.join('## '+b+'\n\n'+d['public'].get(b,'').strip() for b in BLOCKS)+'\n'
    record=f"""**Case and dockets:** {d['case']}
**Event and date:** {d['event']}, {d['date']}; October Term 2003, chunk 2.
**Result:** {d['result']}
**Version / lineage:** Original decision.

## Event, chronology and lawful channel

{d['chronology']}

Research cutoff: {d['date']}. The approved proper-before-the-Court premise supplies the merits posture. Historical institutional dates and published recitations are distinguished from the Court's adjudication below. No invented docket or grant date is used.

## Participation, quorum and issue reach

{d['participation']}

{d['reach']}

## Issue-specific law entering the event

{d['entering']}

The actual completed Gentry, Greenville, Mitchell, Boca, Barnhart, Washoe, Ho and Valeria Public Projections were screened. Their habeas, clinic-regulation, tax, disability-administration, takings, commerce and racial-political-process holdings do not decide this case's issue. Holston's distinct commerce rule and Demore's detention rules likewise supply no contrary rule. {d.get('earlier_own','Raytheon and Banks use the same December 2 substantive baseline; their alphabetical sequence affects assignment accounting only.')}

Later-dated chunk 1 records supply authorship evidence only under the user's express all-durable assignment instruction. None enters the substantive law, facts or adjudicative rationale at this event. McConnell and later December decisions remain future law.

## Stone fixed core, final position and compatibility

The approved Section II was exposed only after the non-Stone reconciliation freeze. Its exact case portion is copied below; it is internal approval evidence.

{stone}

{d['stone_test']}

## Form, assignment and final joins

{d['form']}

The Chief Justice is in the judgment coalition and assigns. Under the user's express override, this recount includes every previously durable signed plenary lead in this term, including later-dated chunk 1 records, and each lead written earlier in this Run. Counts were freshly derived from the exact opinion topologies, not earlier assignment tallies. The full source trace is:

{trace_text}

Last previously durable source in this assembly sequence: `{trace[-1][0]}`. Latest effective event among all counted sources: West Virginia v. United States Department of Health and Human Services, June 16, 2004; that future date has an accounting role only.

{count_table}

Eligible authors: {', '.join(d['eligible'])}. Minimum eligible count: {minimum}; pool ceiling: {minimum+1}. Pool: {', '.join(pool)}. Chosen author: {d['author']}.

{d['assignment']}

{d['joins']}

Final compatibility, rather than invented draft exchanges, establishes these joins. No post-reconciliation commitment changes; no fresh circulation reconciliation is required. Differing tolerable emphases do not create a separate writing merely to repeat a join barrier.

## Controlling holdings

{d['public']['Holdings']}

## Precedent and resulting law

{d['public']['Precedent Treatment']}

{d['public']['Law After Decision']}

## Judgment, remedy and post-decision stage

{d['public']['Judgment & Remedy']}

{d['public']['Procedure After Action']}

## Continuity and noncontrolling positions

{d['continuity']}

## Sources, status and validation

Neutral framing and preservation: the frozen packet item {d['number']} and B preflight. Instrument text: frozen B source extracts and their saved primary sources. Entering law: the authorized B slice and the completed public handoffs identified above. Historical comparison: the complete primary sources listed in the copied reconciliation, verified in that separate context. {d['sources']}

The approved event posture and supported published recitations are the bounded record basis. No unexamined archive document is called unavailable and no source limitation is treated as litigant default. Exact historical passages and approved material in the audit annex are copied mechanically from their frozen source; the public account paraphrases and creates no source quotation.

Engine §15 assembly checks completed: approved fixed core and every attributed Chief join; proper channel and grant scope; event-date entering law; both participation milestones and quorum; component arithmetic and rationale joins; form-before-count assignment and all-durable source recount; complete remedy and stage; precedent scope and no later-law import; retained source limits; frozen reconciliation identity; and the §8 negative-statement check in Judgment & Remedy, Holdings, Precedent Treatment, Law After Decision and Procedure After Action. Material qualification and alternative checks passed. All ordinary explanations are below 350 words. Computational results and file hashes are recorded in `runtime/OT_2003CHUNK2_B_FIRST_ASSEMBLY_VALIDATION.md` and its freeze copy after all four are complete. Current-Term State publication and repository commitment remain the integrating operator's work; this record does not claim those later checks completed.

## Adaptive audit annex — frozen neutral packet

{neutral}

## Adaptive audit annex — independent non-Stone commitments

{commitment.strip()}

## Adaptive audit annex — historical reconciliation

{reconciled.strip()}

## Public Projection

{public}"""
    filename=d['filename']
    path=BASE/'records'/filename
    assert not path.exists(),filename
    path.write_text(record,encoding='utf-8',newline='\n')
    actual=path.read_text(encoding='utf-8').split('## Public Projection\n\n',1)[1]
    assert actual==public
    assert re.findall(r'^## (.+)$',actual,re.M)==BLOCKS
    for blocked in ['One'+'Drive','Git'+'Hub','file://','C:\\Users']:
        assert blocked not in record
    explanations=[]
    for m in re.finditer(r'\*\*Controlling explanation:\*\*\s*(.*?)(?=\n### |\n\*\*Authority:|\Z)',d['public']['Holdings'],re.S):
        wc=len(m.group(1).split());assert wc<=350,(filename,wc);explanations.append(wc)
    for suffix in ['runtime','freeze']:
        (BASE/suffix/f"OT_2003CHUNK2_{d['key']}_PUBLIC.md").write_text(actual,encoding='utf-8',newline='\n')
    assert commitment in record and reconciled in record
    CREATED.append(filename)
    VALIDATION.append({'case':d['key'],'record':filename,'author':d['author'],'counts':counts,'pool':pool,'explanation_words':explanations,'record_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'public_sha256':hashlib.sha256(actual.encode()).hexdigest(),'vote':d['result']})
    print(json.dumps(VALIDATION[-1]))

def finish():
    body='# OT2003 chunk 2 — first B assembly validation\n\nCreation order: Raytheon, Banks, Van Susteren, Virginia.\n\nThe Engine §15 assembly checks described in each Record were performed. Final Chief compatibility uses only the approved Section II and does not use the fallback for any component. All four preserve their frozen reconciled non-Stone commitments. Raytheon has seven participants and four-vote majority threshold; each other case has nine participants and five-vote threshold. Raytheon and Banks share the substantive December 2 baseline. Later-dated durable leads enter authorship accounting alone under the express user override.\n\nThe five-block §8 negative-statement review passed: surviving claim/judgment boundaries, the actual grant limitations, adopted rule qualifications and requested relief withheld have a stated legal function; no inventory of unrequested relief or hypothetical nonholdings is published. Every material statutory or instrument qualification is supplied in terms. Ordinary explanations remain under 350 words.\n\nPublic handoffs are exact copies of the bounded Public Projections. Frozen commitments and reconciliation were copied byte-for-byte as text into the internal annexes, without changing the authoritative files. No workflow material appears in the eleven public blocks. No workspace, ledger, manifest or render-input mutation was performed. Integration, term-wide deterministic validation and operator commitment remain pending.\n\n'
    for v in VALIDATION:
        body+='## '+v['case']+'\n\n'+json.dumps(v,ensure_ascii=False,indent=2)+'\n\n'
    for suffix in ['runtime','freeze']:
        (BASE/suffix/'OT_2003CHUNK2_B_FIRST_ASSEMBLY_VALIDATION.md').write_text(body,encoding='utf-8',newline='\n')
