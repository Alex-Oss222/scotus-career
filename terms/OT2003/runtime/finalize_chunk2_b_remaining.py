from pathlib import Path
import re,json,hashlib

BASE=Path('terms/OT2003')
NAMES=['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']
BLOCKS=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
CREATED=[]
VALIDATION=[]

def read(p):return (BASE/p).read_text(encoding='utf-8-sig')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def section(s,n):return re.search(r'^## '+str(n)+r'\..*?(?=^## \d+\.|\Z)',s,re.M|re.S).group().strip()
def topology(s):
    if '## Public Projection' in s:s=s.split('## Public Projection',1)[1]
    return re.search(r'^## Opinion Topology\n(.*?)(?=^## |\Z)',s,re.M|re.S).group(1).strip()

def recount():
    # Inspect actual tables afresh; the refreshed handoff supplies the allowed source inventory.
    handoff=read(Path('runtime/OT_2003CHUNK2_PRIOR_OPINION_TABLES.md'))
    sources=[]
    for b in re.split(r'(?m)^# ',handoff):
        f=b.splitlines()[0] if b else ''
        if not f.endswith('.md'):continue
        actual=topology(read(Path('records')/f))
        assert actual==topology(b),f
        sources.append((f,actual))
    assert len(sources)==20
    for f in CREATED:sources.append((f,topology(read(Path('records')/f))))
    counts=dict.fromkeys(NAMES,0);trace=[]
    for f,t in sources:
        if 'per curiam' in t.lower():trace.append((f,[]));continue
        prefix=re.split(r'\b(?:delivered|announced)\b',t,maxsplit=1)[0]
        raw=re.findall(r"([A-Z'’\-]+), (?:C\. J\.|J\.)",prefix)
        authors=[]
        for token in raw:
            n=next(n for n in NAMES if n.upper().replace('’',"'")==token.replace('’',"'"))
            if n not in authors:authors.append(n)
        assert authors,f
        for n in authors:counts[n]+=1
        trace.append((f,authors))
    return counts,trace

def build(d,receipt_paths,additive_paths=()):
    assert receipt_paths,'Clean public-law receipt required'
    for rel in receipt_paths:assert (BASE/rel).exists(),rel
    counts,trace=recount()
    minimum=min(counts[n] for n in d['eligible']);pool=[n for n in d['eligible'] if counts[n]<=minimum+1]
    assert d['author'] in pool
    public='\n\n'.join('## '+b+'\n\n'+d['public'].get(b,'').strip() for b in BLOCKS)+'\n'
    assert not re.search(r'(?i)reserved for final|unassigned|authorship|approved|workflow|reconcil|simulat|2026|runtime/|freeze/',public)
    assert re.findall(r'^## (.+)$',public,re.M)==BLOCKS
    holds=d['public']['Holdings']
    words=[len(m.group(1).split()) for m in re.finditer(r'\*\*Controlling explanation:\*\*\s*(.*?)(?=\n### |\n\*\*Authority:|\Z)',holds,re.S)]
    assert all(w<=350 for w in words),(d['key'],words)
    full_words=[len(x.split()) for x in re.split(r'\n### ',holds)]
    assert all(w<=350 for w in full_words),(d['key'],full_words)
    table='| Justice | Count before assignment | Eligible for complete lead | Balance pool |\n|---|---:|---|---|\n'+'\n'.join(f"| {n} | {counts[n]} | {'Yes' if n in d['eligible'] else 'No'} | {'Yes' if n in pool else 'No'} |" for n in NAMES)
    trace_text='\n'.join(f"- `{f}`: {', '.join(a) if a else 'per curiam; excluded'}." for f,a in trace)
    neutral=section(read(Path('freeze/OT_2003CHUNK2_NEUTRAL.md')),d['number'])
    stone=section(read(Path('runtime/OT_2003CHUNK2_STONE.md')),d['number'])
    primary_paths=[Path(f"freeze/OT_2003CHUNK2_{d['key']}_COMMITMENTS.md"),Path(f"freeze/OT_2003CHUNK2_{d['key']}_RECONCILED.md")]
    audit_paths=primary_paths+list(map(Path,additive_paths))+list(map(Path,receipt_paths))
    audits='\n\n'.join('## Frozen audit source — '+p.name+'\n\n'+read(p).strip() for p in audit_paths)
    status='The original frozen provisional and reconciliation sources are preserved below as stage artifacts. '+d.get('stage_status','No post-reconciliation substantive commitment changed in assembly.')
    record=f"""**Case and dockets:** {d['case']}
**Event and date:** {d['event']}, {d['date']}; October Term 2003, chunk 2.
**Result:** {d['result']}
**Version / lineage:** Original decision.

## Event, chronology and lawful channel

{d['chronology']}

Research cutoff: {d['date']}. The approved proper-before-the-Court posture supplies the merits stage; no additional grant date or historical docket event is invented. Public dates distinguish the underlying proceedings from this decision.

## Participation, quorum and reach

{d['participation']}

{d['reach']}

## Issue-specific entering law and completed public-law screen

{d['entering']}

{d['law_screen']}

All previously durable signed plenary leads count for assignment under the user's express override, including later-dated chunk 1 decisions. Their future holdings, facts and rationale do not enter this case's substantive law. Castro and Pringle share the December 15 pre-date law; alphabetical creation order supplies assignment accounting only.

## Chief fixed core and final compatibility

{d['stone_test']}

The exact approved case-specific Section II follows as internal evidence; it was exposed only after the original non-Stone reconciliation freeze.

{stone}

## Form, assignment and final joins

{d['form']}

The Chief is in the judgment coalition and assigns. The foregoing legal form, propositions and part boundaries were fixed before this recount. Each author below comes from the actual opinion topology, freshly inspected and compared with the exact refreshed handoff; earlier assignment tallies are not sources. Count each signed plenary lead once per delivering author, including both McConnell lead authors but excluding separate writings and the Gentry per curiam.

{trace_text}

Last durable event in this assignment sequence: `{trace[-1][0]}`. Latest effective date among all counted sources: June 16, 2004, West Virginia v. United States Department of Health and Human Services; that future date has an accounting role only.

{table}

Eligible authors: {', '.join(d['eligible'])}. Minimum eligible count: {minimum}; pool ceiling: {minimum+1}. Pool: {', '.join(pool)}. Chosen author: {d['author']}.

{d['assignment']}

{d['joins']}

{status} Final compatibility establishes the published joins without invented drafts or persuasion. A recorded silence is not an affirmative objection or reason to manufacture a separate writing.

## Controlling holdings

{holds}

## Precedent treatment and resulting law

{d['public']['Precedent Treatment']}

{d['public']['Law After Decision']}

## Judgment, remedy and post-decision stage

{d['public']['Judgment & Remedy']}

{d['public']['Procedure After Action']}

## Continuity and noncontrolling published positions

{d['continuity']}

{d.get('departure','')}

## Affected later-public-law screen after the present holdings were fixed

{d['affected_later']}

## Sources and completed assembly validation

{d['sources']}

Engine §15 checks completed: approved fixed core, every Chief proposition and limited join, named fallback use if any; lawful channel, actual grant and preservation; both participation milestones and quorum; complete judgment/rationale arithmetic; date-effective law and source limitations; final frozen commitment compatibility; form-before-count sequential assignment from actual tables; complete operative qualifications; remedy and stage; and no later-law import. The §8 review of Judgment & Remedy, Holdings, Precedent Treatment, Law After Decision and Procedure After Action retains only actual grant/preservation limits, adopted operative qualifications, relief sought or ordered that is withheld, and surviving judgment status. Neighboring nonholdings and hypothetical-remand catalogues are removed. Ordinary explanation counts: {', '.join(map(str,words))}, each within 350 words. Exact handoff inclusion and Public Projection identity are verified by the assembly script and recorded in the remaining-B validation. Current-term workspace publication, generated Render Inputs, term-wide deterministic checks and operator commitment remain integration work and are not claimed completed here.

## Frozen neutral input

{neutral}

{audits}

## Public Projection

{public}"""
    for p in audit_paths:assert read(p) in record,p
    for bad in ['One'+'Drive','Git'+'Hub','file://','C:\\Users']:assert bad not in record
    p=BASE/'records'/d['filename'];assert not p.exists(),p
    p.write_text(record,encoding='utf-8',newline='\n')
    exact=p.read_text(encoding='utf-8').split('## Public Projection\n\n',1)[1]
    assert exact==public
    for directory in ['runtime','freeze']:
        q=BASE/directory/f"OT_2003CHUNK2_{d['key']}_PUBLIC.md";q.write_text(exact,encoding='utf-8',newline='\n');assert q.read_bytes()==exact.encode()
    CREATED.append(d['filename'])
    VALIDATION.append({'case':d['key'],'record':d['filename'],'author':d['author'],'counts_before':counts,'eligible':d['eligible'],'pool':pool,'result':d['result'],'explanation_words':words,'complete_holding_words':full_words,'record_sha256':sha(p),'public_sha256':hashlib.sha256(public.encode()).hexdigest(),'audit_inputs':{x.as_posix():sha(BASE/x) for x in audit_paths}})
    print(json.dumps(VALIDATION[-1],ensure_ascii=False))
    save_progress()

def save_progress():
    (BASE/'runtime/OT_2003CHUNK2_B_REMAINING_STATE.json').write_text(json.dumps({'created':CREATED,'validation':VALIDATION},ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
    v='# OT2003 chunk 2 — remaining B final assembly validation\n\nCreated sequentially in the order listed below, after the actual McConnell public-law screen and clean receipts. Every assignment freshly recounts all20 prior actual opinion tables plus each new preceding Record. McConnell counts once for each of Stone-Zsela and O’Connor. Future-dated chunk1 decisions enter accounting only.\n\nThe explicit Engine §15 and five-block §8 checks described in each Record have been performed at assembly scope. Exact frozen text inclusion, eleven-block order, internal/Public Projection holding identity, public-copy byte identity, operative qualification completeness, final vote/join arithmetic and explanation ceilings pass. Workspace, generated Render Input and term-wide integration remain pending with the operator.\n\n'+json.dumps(VALIDATION,ensure_ascii=False,indent=2)+'\n'
    for directory in ['runtime','freeze']:(BASE/directory/'OT_2003CHUNK2_B_REMAINING_ASSEMBLY_VALIDATION.md').write_text(v,encoding='utf-8',newline='\n')

def restore():
    p=BASE/'runtime/OT_2003CHUNK2_B_REMAINING_STATE.json'
    if p.exists():
        state=json.loads(p.read_text(encoding='utf-8'));CREATED.extend(state['created']);VALIDATION.extend(state['validation'])

def load_data(key):return json.loads(read(Path(f'runtime/OT_2003CHUNK2_{key}_ASSEMBLY_DATA.json')))

def scope_polish(d):
    if d['key']=='DEATON':
        d['public']['Holdings']=d['public']['Holdings'].replace(' Holston’s necessary-inclusion mechanism and Ho’s demonstrated abatement-service market remain distinct; hiring a contractor does not import their factual predicates into this water case.','')
        d['public']['Precedent Treatment']='\n'.join(x for x in d['public']['Precedent Treatment'].splitlines() if not x.startswith('- United States v. Holston') and not x.startswith('- Virginia v. Maryland'))
    if d['key']=='PRINGLE':
        d['public']['Judgment & Remedy']=d['public']['Judgment & Remedy'].replace('any independently preserved admissibility or trial issue','any independently preserved issue')
        d['public']['Procedure After Action']='The case returns to the Maryland courts for proceedings consistent with the Court’s resolution of the arrest-based suppression ground and any independently preserved issue remaining in its proper posture.'
    return d
