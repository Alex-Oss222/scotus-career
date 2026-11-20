from pathlib import Path
import json,re,hashlib,collections

T=Path('terms/OT2003'); R=T/'runtime'; F=T/'freeze'
record=T/'records/mcconnell_v_federal_election_commission_merits_2003-12-10.md'
candidate=R/'OT_2003CHUNK2_MCCONNELL_CDR_DRAFT.md'
public_path=R/'OT_2003CHUNK2_MCCONNELL_PUBLIC_DRAFT.md'
data=json.loads((R/'OT_2003CHUNK2_MCCONNELL_ASSEMBLY_DATA.json').read_text(encoding='utf-8'))
accounting=json.loads((R/'OT_2003CHUNK2_MCCONNELL_ASSIGNMENT_COUNTS.json').read_text(encoding='utf-8'))
c=candidate.read_text(encoding='utf-8'); p=public_path.read_text(encoding='utf-8')
labels=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
assert re.findall(r'^## (.+)$',p,re.M)==labels
assert c.split('## Public Projection\n\n',1)[1]==p
for i,label in enumerate(['**Case and dockets:**','**Event and date:**','**Result:**','**Version / lineage:**']):
    assert c.splitlines()[i].startswith(label)
for h in data['holdings']:
    assert h['author'] in h['joins'] and len(h['joins'])==len(set(h['joins'])) and len(h['joins'])>=5
    assert len(h['explanation'].split())<=350
    for key in ['rule','explanation','precedent']: assert h[key] in p
for j in data['judgments']:
    assert len(j['support'])==len(set(j['support'])) and len(j['oppose'])==len(set(j['oppose']))
    assert not set(j['support'])&set(j['oppose'])
    if 'six supporting' not in j['decision']: assert len(j['support'])+len(j['oppose'])==9
    m=re.search(r'(\d+)\u2013(\d+)',j['decision'])
    if m: assert [len(j['support']),len(j['oppose'])]==[int(m.group(1)),int(m.group(2))]
for label in ['approved','reconciliation','simulation','counterfactual','user-directed','commit hash','private Stone','Length designation']:
    assert label.lower() not in p.lower()
assert not re.search(r'\bStone\b(?!-Zsela)',p)
for s in [c,p,Path(__file__).read_text(encoding='utf-8'),(R/'assemble_mcconnell.py').read_text(encoding='utf-8')]:
    for banned in ['one'+'drive','git'+'hub','fi'+'le://','c:'+chr(92)+'users'+chr(92),'c:'+'/'+'users/']:
        assert banned not in s.lower()
assert len(accounting['trace'])==19 and sum(accounting['counts'].values())==18
assert hashlib.sha256((F/'OT_2003CHUNK2_MCCONNELL_RECONCILED.md').read_bytes()).hexdigest()=='dd964f545f1f2f384a9f1d47296a05c38bab5748b7bc2de1067c81ceab1fce65'

validation='''# McConnell assembly validation

**Status:** Local assembly complete. Engine section 15 review passed at the Record/Public Projection boundary. Coordinated workspace, ledger, manifest, generated Render Input and whole-chunk validation remain root's next integration work and are not certified as already performed here. The public render remains a separate task.

## Stage and source integrity

The complete reconciled freeze was explicitly authorized before the assembly context read the current McConnell private supplement. Its SHA-256 is `dd964f545f1f2f384a9f1d47296a05c38bab5748b7bc2de1067c81ceab1fce65`; the hash matches. Section 12 is the operative final map, and superseded section 11B is not used as a current commitment. The source-only argument-date check read the saved primary syllabus lines 60-61 and establishes September 8, 2003 without importing historical lineup or disposition.

The exact enacted text was checked for the clarified party/entity/agent classes, four federal-election-activity exclusions, Levin conditions, the literal payroll trigger (activities in connection with a federal election), section 323(d)'s separate recipient branches, section 323(e)(2)'s own scope and office-sought wording, pre-election windows, President/Vice President geographic exception and public inspection of broadcaster files. These correct shorthand descriptions without changing a Justice's operative conclusion or adding a challenged provision. The material statutory qualifications, separate grounds, burdens and remedies are carried in the holdings themselves. Long saved-source passages were incorporated programmatically.

The substantive source boundary remains the validated neutral and power preflights, actual entering-law slices, complete frozen reconciliation and earlier effective public law. No unavailable source establishes litigant default; no new concession, precise advertising statistic, claimant-negative fact, nonprofit status or reprisal event is presumed. Source sufficiency does not claim a fresh full reading of every brief or appendix. No material source gap remains for the bounded presented decisions.

## Conditional authoring and assignment

The signed lead's legal form and separable questions were fixed before the recount. Nineteen actual prior topology blocks yield eighteen signed leads. Gentry's per curiam and all separate writings are excluded. The five later-dated chunk 1 leads count only under the current express accounting direction. No current McConnell part increments a count until this one Record is written.

| Justice | Count before all assignments here |
|---|---:|
'''
validation+='\n'.join(f'| {j} | {n} |' for j,n in accounting['counts'].items())
validation+='''

Last earlier effective event: Virginia v. Maryland, December 9, 2003. Latest accounting-only date: West Virginia v. HHS, June 16, 2004. The source-to-author trace is retained in the Record and `runtime/OT_2003CHUNK2_MCCONNELL_ASSIGNMENT_COUNTS.json`.

The Chief's conditional rule applies only where five or more including him directly join his approved reasoning. Nineteen holding blocks carry his adopted substantive grounds, with exact narrower or broader joins separately identified. The eleven uncovered holding blocks are delivered by O'Connor. The common fully eligible authors for that complete group are O'Connor (two) and Souter (three); both are in the balance pool (minimum two, ceiling three). O'Connor's source-specific election, actual fit and statutory-channel work, and lower count, support the selection. She independently assigns the payroll part as the most senior Associate in its majority; the Chief assigns the uncovered portions whose judgment he joins. The conditional instruction, not balance, requires his authorship of adopted portions. Each lead deliverer counts once after this Record: Stone-Zsela and O'Connor each gain one; no separate writing counts.

The Chief's approved sustaining vote on payroll is preserved as a dissent joined there by Stevens, Ginsburg and Breyer. His additional affirmative effective-timely-review instruction appears only in his separate writing, with no other join; ordinary application-review reservations are not used to create a remedial majority. The exact fallback activations and disposition-only relationships are listed in the Record and identified by component in the public topology. Fallback supplies no reasoning or author eligibility. His expressed sections 201/212, 311, 504 and threshold positions are not replaced by an alternative ground or changed remedy.

## Votes, joins, remedies and explanation ceilings

There are 33 judgment component rows: eighteen unanimous disposition rows, eleven 6-3 rows, one 5-4 payroll-remand row, one 8-1 attribution row, one 7-2 broadcaster-application row, and one six-supporter equality row where the other three obtain their requested relief on speech grounds without a separate equality vote. That last row is deliberately not converted into a fictitious 6-3 reasoning division. All names are unique within each coalition and supporting/opposing sets are disjoint. Actual remedy differences are retained even where counts coincide.

All 30 holding blocks name a direct controlling coalition. Mixed-scope holdings explicitly identify unanimous narrower propositions, Thomas's narrower broadcaster join, the five-Associate classification rationale and the eight-Associate racial-impact ground. The five payroll votes directly adopt the same fit/remand rule; no Marks aggregation is used. Every proposed author belongs to the actual full-proposition coalition for the portion delivered. Separate-writing joins and withheld grounds match the final frozen boundaries.

All 30 explanation bodies are within the ordinary 350-word ceiling; the maximum is 203 words. Full rules and their material qualifications are retained separately from the explanation, with no relocation of reasoning to evade the ceiling. The 90 rule/explanation/precedent data fields match their public projection text. Each selected separate writing explains its substantive ground, component scope, joins and proposed remedy. No extended-length designation was supplied or printed.

## Section 8 negative-statement review

**Result: passed.** Judgment & Remedy, Holdings, Precedent Treatment, Law After Decision and Procedure After Action were reviewed individually. Internal join-accounting comments, hypothetical different-relief intervenor examples, universal scope disclaimers and the private negative catalogue of unawarded remedies were removed. Retained qualifications state actual legal questions left on identified threshold/inactive grounds, relief sought or ordered below, surviving injunction/statutory status, or an adopted operative limit not entailed by the disposition. The reporting-versus-prohibition, source-versus-speech-fit and independent-versus-coordinated distinctions do substantive work; they are not lists of unrequested relief. The public account states the affirmative rule before its necessary limits. The Chief's unjoined additional timing direction appears only as his published separate remedial position.

## Section 15 result and deterministic verification

**Section 15 result: passed for local assembly.** Term/event/argument chronology, nine-person participation, quorum, proper supplied channel, actual issue scope, latest approved Chief core and revalidation, fixed-core comparisons, exact final Associate commitments, assignment bases, direct joins, judgment/remedy coherence, complete-resolution grounds, ordinary explanation ceilings, precedent force and source cutoff were reviewed. Final compatibility introduces no material Associate change, so a new sanitized circulation-reconciliation stage is not required. No fictional circulation history is asserted.

The exact four opening labels and natural-key filename were checked. The bounded Public Projection has exactly eleven level-two blocks in Contract order; its bytes match the frozen/runtime public handoffs. No private position, workflow label, modern research date or historical-authorship claim enters the public projection. The Chief's public name is Stone-Zsela. The prescribed file-scope and content restrictions were checked. No repository command was executed. Deterministic checks validate consistency, not legal substance.

## Completed later-record screen

After fixing all present holdings, the assembly context read only the public Event, Law After Decision and Procedure After Action blocks of Rancho Viejo, Lomont, Environmental Defense Center, ACLU of New Jersey v. County of Hudson and West Virginia v. HHS. Their actual necessary-inclusion affirmance, voluntary certification, operational stormwater information, custodial confidentiality and conditional-funding premises remain distinct from the present election sources, private-finance structure, electoral information and supported request-file functions. The Record supplies the case-by-case comparison. No concrete displaced predicate was found; no prior adjudication is altered and no later law enters the present holding.

## Durable artifacts

- `records/mcconnell_v_federal_election_commission_merits_2003-12-10.md`
- `runtime/OT_2003CHUNK2_MCCONNELL_PUBLIC.md` and identical `freeze/OT_2003CHUNK2_MCCONNELL_PUBLIC.md`
- `runtime/OT_2003CHUNK2_MCCONNELL_ASSEMBLY_VALIDATION.md` and identical `freeze/OT_2003CHUNK2_MCCONNELL_ASSEMBLY_VALIDATION.md`

Record and handoff hashes follow. Source and assignment data remain in their named internal artifacts. Root may now perform coordinated projections and the remaining chunk checks.
'''

# The candidate has passed the checks above and the recorded legal/qualification
# review. The single durable event is written only now.
assert not record.exists(), 'Refusing to replace an existing adjudication.'
record.write_text(c,encoding='utf-8')
for directory in [R,F]:
    (directory/'OT_2003CHUNK2_MCCONNELL_PUBLIC.md').write_text(p,encoding='utf-8')
record_sha=hashlib.sha256(record.read_bytes()).hexdigest()
public_sha=hashlib.sha256((F/'OT_2003CHUNK2_MCCONNELL_PUBLIC.md').read_bytes()).hexdigest()
validation+=f'\n**Record SHA-256:** `{record_sha}`\n\n**Public handoff SHA-256:** `{public_sha}`\n'
for directory in [R,F]:
    (directory/'OT_2003CHUNK2_MCCONNELL_ASSEMBLY_VALIDATION.md').write_text(validation,encoding='utf-8')
assert (R/'OT_2003CHUNK2_MCCONNELL_PUBLIC.md').read_bytes()==(F/'OT_2003CHUNK2_MCCONNELL_PUBLIC.md').read_bytes()
assert (R/'OT_2003CHUNK2_MCCONNELL_ASSEMBLY_VALIDATION.md').read_bytes()==(F/'OT_2003CHUNK2_MCCONNELL_ASSEMBLY_VALIDATION.md').read_bytes()
assert record.read_text(encoding='utf-8').split('## Public Projection\n\n',1)[1]==(F/'OT_2003CHUNK2_MCCONNELL_PUBLIC.md').read_text(encoding='utf-8')
print('McConnell Record, public twins and validation twins written and verified.')
print('Record SHA-256:',record_sha)
print('Public SHA-256:',public_sha)
