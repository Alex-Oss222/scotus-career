from pathlib import Path
import re

TERM=Path('terms/OT2003')
JUSTICES=['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']
BLOCKS=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
BASELINE={'aclu_of_new_jersey_v_county_of_hudson_merits_2004-04-13.md','demore_v_kim_merits_2003-10-14.md','environmental_defense_center_v_epa_merits_2004-03-25.md','lomont_v_oneill_merits_2004-03-11.md','rancho_viejo_llc_v_norton_merits_2004-02-05.md','united_states_v_holston_merits_2003-10-30.md','west_virginia_v_us_department_of_health_and_human_services_merits_2004-06-16.md'}
ASSEMBLED={'greenville_womens_clinic_v_commissioner_merits_2003-10-27.md','mitchell_v_esparza_merits_2003-11-03.md','boca_investerings_partnership_v_united_states_merits_2003-11-06.md','barnhart_v_thomas_merits_2003-11-12.md','washoe_county_v_united_states_merits_2003-11-17.md','united_states_v_ho_merits_2003-11-20.md','valeria_v_davis_merits_2003-11-25.md'}

def recount(date):
    counts=dict.fromkeys(JUSTICES,0); sources=[]
    for p in sorted((TERM/'records').glob('*.md')):
        t=p.read_text(encoding='utf-8-sig')
        m=re.search(r'^\*\*Event and date:\*\*.*?(\d{4}-\d{2}-\d{2})',t,re.M)
        if not m or not (p.name in BASELINE or (p.name in ASSEMBLED and m[1]<date)): continue
        pub=t.split('## Public Projection',1)[1]
        topology=pub.split('## Opinion Topology',1)[1].split('## Holdings',1)[0]
        lead=re.search(r"\b([A-Z][A-Z'’ -]+), (?:J\.|C\. J\.), delivered",topology)
        if not lead: continue
        raw=lead[1].strip().title().replace('’',"'")
        author=next((j for j in JUSTICES if j.lower()==raw.lower()),None)
        if author is None: raise ValueError((p,raw))
        counts[author]+=1; sources.append((m[1],p.name,author))
    return counts, sorted(sources)

def assignment(date,eligible,author,explanation,authority='The Chief Justice assigns from the judgment coalition.'):
    counts,sources=recount(date)
    minimum=min(counts[j] for j in eligible)
    pool=[j for j in eligible if counts[j]<=minimum+1]
    assert author in pool
    rows='\n'.join(f'| {j} | {counts[j]} | {"Yes" if j in eligible else "No"} | {"Yes" if j in pool else "No"} |' for j in JUSTICES)
    trace='\n'.join(f'- {d}: `{f}`, actual public opinion topology: {a}, one signed lead.' for d,f,a in sources)
    return f'''{authority}

Recount performed afresh from the actual opinion tables of all seven already durable chunk-one Records, plus earlier-created chunk-two Records. The user's task-specific durable-Record counting instruction includes later-dated baseline Records for assignment counts only; their substantive law remains excluded until its effective date. Separate writings and the Gentry per curiam count zero. Later-created chunk-two Records are excluded. Last counted event in the displayed event-date inventory: {sources[-1][0]+' '+sources[-1][1] if sources else 'none'}.

{trace}

| Justice | Count before assignment | Eligible for the complete opinion | Balance pool |
|---|---:|---|---|
{rows}

Eligible authors: {', '.join(eligible)}. Minimum eligible count: {minimum}; pool ceiling: {minimum+1}. Pool: {', '.join(pool)}. Chosen author: {author}. {explanation}
'''

def save(name,case,date,result,kernel,assign,annex,blocks):
    assert list(blocks)==BLOCKS
    p=TERM/'records'/name
    assert not p.exists(), p
    text=f'''**Case and dockets:** {case}
**Event and date:** Merits decision, {date}; October Term 2003, chunk 2.
**Result:** {result}
**Version / lineage:** Original decision record; supersedes no completed adjudication.

## Decision kernel

{kernel}

The bounded Public Projection below supplies the component judgments, exact opinion joins, controlling holdings, precedent treatment, resulting law, selected separate positions and procedure, and is incorporated into this kernel without substantive variation. The historical or lower-court source is evidence of the record and posture, not authority over the entering simulated law.

## Form, assignment and final compatibility

{assign}

## Adaptive audit annex

{annex}

## Sources, chronology and validation status

Research cutoff: {date}. The frozen neutral packet, A preflight and source extracts, applicable A entering-law selections, final case-specific reconciliation and approved Section II supply the authorized inputs. Published lower judicial recitations support the material historical facts; no claim is made that original petitions, briefs, the complete appendix or transcripts were independently inspected. Research limits establish no litigant default or missing Court filing. The inventory supplies proper merits submission and the event date; no argument date is invented. All nine seated Justices participate at submission and decision; quorum and five-vote threshold are satisfied.

Validation actually performed during initial assembly before final handoff: final judgment and proposition coalitions were compared with every frozen Associate scope and Stone's fixed core; counts were recomputed from actual earlier durable Record opinion tables under the user's committed-Record override; natural-key filename, exact four opening labels, eleven ordered public blocks, absence of public workflow metadata, and component arithmetic were checked. The Section 8 negative-statement review covered the five specified blocks and this kernel: retained negatives state an operative qualification, a genuine open legal question, relief sought or surviving judgment status. No unsupported reservation or inventory of unrequested relief is retained. No Associate commitment changes occur in assembly; reconciled changes remain those documented in the frozen handoff. No fictional draft exchanges are asserted. There is no unresolved event-level blocker. Term-level projection and deterministic integration checks remain the integrating operator's responsibility; this record does not claim that those later steps have occurred. Durable creation occurs in the instructed event order and is recorded in the A assembly validation receipt; coordinated Current Term State publication follows integration.

## Public Projection

'''
    text+='\n\n'.join('## '+k+'\n\n'+v.strip() for k,v in blocks.items())+'\n'
    p.write_text(text,encoding='utf-8')
    assert [x for x in re.findall(r'^## (.+)$',text.split('## Public Projection\n',1)[1],re.M)]==BLOCKS
    return p

def frozen_audit(key,heading=None):
    t=(TERM/'freeze'/f'OT_2003CHUNK2_{key}_RECONCILED.md').read_text(encoding='utf-8-sig')
    if heading: t=t.split(heading,1)[1]
    return 'The following frozen reconciliation is copied without alteration as the audit support; its stage language describes the earlier handoff. The final decision and joins are stated above and in the Public Projection.\n\n'+t

if __name__=='__main__':
    print('Assembly helpers loaded; individual event scripts perform one durable creation at a time.')
