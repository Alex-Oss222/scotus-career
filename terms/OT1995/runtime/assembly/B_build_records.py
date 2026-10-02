from pathlib import Path
import json

BASE=Path('terms/OT1995')
OUT=BASE/'runtime/assembly'
OUT.mkdir(exist_ok=True)
J=['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']
A=J[1:]
NAMES=', '.join(J)
RECON=(BASE/'freeze/OT_1995CHUNK1_B_RECONCILED.md').read_text(encoding='utf-8')
HEADS=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
COMMON='''All nine members—Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer—participate at submission or argument and decision. No nonparticipation is established. Nine constitute a quorum; five votes are necessary for judgment and for a controlling proposition. No petition poll is part of this merits assembly.

The source and stage boundaries are the frozen B neutral packet, entering-law B/B_SUPPLEMENT, B reconciled commitments and scoped B Stone input, with their identified objective sources. The original independent and reconciliation freezes remain untouched. This is the disclosed cross-context fallback; it claims no pristine isolation. Historical review occurred before current Stone input. The full-reading and arithmetic receipts are `freeze/OT_1995CHUNK1_B_RECONCILIATION_FULL_READING_RECEIPT.json` and `freeze/OT_1995CHUNK1_B_RECONCILIATION_CHECK_RECEIPT.json`.

Wood (October10), Doe (October16) and Hodge (October23) were read in their bounded public entering-law copies. Their Brady, school-supervision/immunity and retained-record immunity/mootness holdings do not change the grounds used here. No Tuggle adjudication is treated as effective law. Drafts of other current matters are not authority. Root preservation and the event-specific chronological refresh remain required before this draft becomes a Record.
'''

def rows(case_start,case_end):
 s=RECON[RECON.index(case_start):RECON.index(case_end)]
 a=s.index('| Justice |')
 b=s.index('\n\n',a)
 return s[a:b]

def write_record(filename,case,date,result,internal,blocks,data):
 assert list(blocks)==HEADS
 text=f'''**Case and dockets:** {case}
**Event and date:** {'Original-jurisdiction exceptions' if 'original_exceptions' in filename else 'Merits adjudication'}, {date}; October Term 1995.
**Result:** {result}
**Version / lineage:** Initial adjudication draft; no prior Record superseded; operator Git commitment pending.

{internal.rstrip()}

## Controlling law of the decision

{blocks['Holdings']}

## Precedent, resulting law and published continuity

{blocks['Precedent Treatment']}

{blocks['Law After Decision']}

{blocks['Separate Writings']}

## Validation status and preservation

This is an assembly draft, not a committed Record. Final compatibility and the stated proposition-level counts have been checked against the frozen commitments and fixed Stone input. Source-reading extent is stated in the linked receipts; no unperformed direct-transcript or asset-specific check is reported as passed. Public Projection/holding identity and JSON arithmetic are checked by the companion assembly check. Root must complete chronology, actual-current-assignment review, preservation and term tooling before commitment. No public render is written here.

## Public Projection
'''
 for h,v in blocks.items():text+=f'\n## {h}\n\n{v.rstrip()}\n'
 (OUT/filename).write_text(text,encoding='utf-8')
 data.update({'record_filename':filename,'case':case,'date':date,'disposition_summary':result,'participants':J,'blockers':[]})
 (OUT/filename.replace('.md','.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

STR_H='''### Temporary preservation of a claimed setoff

A creditor's genuinely temporary refusal to pay a deposit debt while promptly seeking judicial relief to exercise a claimed setoff is not itself a setoff forbidden by §362(a)(7) when the creditor has not intended permanently to settle the mutual accounts or finally applied one obligation against the other. The act's legal character controls; a label or the absence of a bookkeeping entry alone does not establish that character.

**Authority:** Scalia's Part I, joined by all eight other Justices, controls unanimously.

**Controlling explanation:** Studley describes setoff as applying mutual debts against each other. The ordinary decision, implementing act and recordation sequence reflects the intention permanently to settle those accounts. Federal law determines whether a setoff has occurred under the Bankruptcy Code even if state law employs a different definition. Section553 preserves qualifying nonbankruptcy setoff rights but creates none and leaves their exercise subject to the automatic stay. Section542(b) excepts payment to the extent the debt may be offset under §553. Requiring immediate payment while treating every temporary preservation step as the completed offset would defeat that enacted relationship.

The bank imposed its hold October2 and sought relief October7; its application asked the bankruptcy court to authorize the later setoff. It did not purport finally to reduce the account by the loan balance. Five days is the record's interval, not a universal safe harbor. The rule permits neither an indefinite freeze nor a secret completed debit, and good faith creates no general stay exception. Whether the amount withheld exceeded the available offset is not decided. No fixed deadline, independent promptness cause of action, or new setoff entitlement is created.

**Precedent treatment:** Studley supplies the mutual-debt function. The Code's particular preservation and stay provisions control their own federal meaning; no general equitable exception is adopted.

### The temporary refusal also does not violate the presented control and collection provisions

On this record, temporarily declining to perform the bank's deposit-payment promise while seeking setoff relief is neither prohibited possession or control under §362(a)(3) nor collection, assessment or recovery under §362(a)(6). This debt-payment holding does not exclude the estate's contractual claim from property of the estate or authorize retention of every kind of estate property.

**Authority:** Scalia's Part II, joined by all eight other Justices, controls unanimously.

**Controlling explanation:** Bank of Marin supplies the debtor-creditor character of an ordinary bank deposit: the depositor has a payment claim, not title to particular currency held in trust. Section542(b)'s payment exception must operate coherently with §§362 and553. The temporary refusal here preserves judicial determination of an asserted offset; it does not finally appropriate the deposit claim or demand payment through coercive collection. Construing the general control or collection provisions to forbid this particular preservation would erase the specific payment exception.

Whiting Pools addresses turnover of property under §542(a), including the protections attending that process; it does not eliminate §542(b)'s distinct debt-payment qualification. Celotex concerns an operative judicial restraint and its authorized review, not a new creditor power to adjudicate its own claim. The Court authorizes no indefinite restraint, refusal after adverse judicial direction or amount beyond legally available offset. Confirmation's effect under §1327 is not reached because that contention was not raised below. The later stay-relief/setoff order is not adjudicated anew.

**Precedent treatment:** Bank of Marin is applied to the deposit relationship. Whiting Pools and Celotex are distinguished at their statutory and procedural scopes.

### The rejected theory cannot sustain the sanctions judgment

The Fourth Circuit's judgment restoring sanctions on the ground that this temporary administrative hold itself violated the automatic stay is reversed. The case is remanded for proceedings consistent with this opinion. The mandate identifies no issue as procedurally open, directs no new evidentiary inquiry, and reopens no unappealed contempt or later setoff order, unpreserved confirmation contention, or other final matter; any otherwise properly remaining question may proceed only through its ordinary lawful channel.

**Authority:** Scalia's Part III, joined by all eight other Justices, controls unanimously.

**Controlling explanation:** The sanctions depended on the stay theory rejected in Parts I and II. Their legal foundation therefore fails without a new decision on willfulness, injury or punitive damages. Then-§362(h) separately requires a willful violation injuring an individual for actual damages, costs and fees, and permits punitive damages in appropriate circumstances; this decision changes none of those requirements. It does not reinstate an unappealed contempt determination, undo the later setoff authorization, decide an excessive hold or determine a taking. Granfinanciera supports declining the unpreserved confirmation contention. Reservations do not themselves require a new evidentiary proceeding in this appeal.

**Precedent treatment:** Granfinanciera's preservation principle is applied; no general priority between a confirmed plan and setoff is established.'''

str_blocks={
'Event':'''**Citizens Bank of Maryland v. Strumpf, No.94-1340 — October31, 1995.** Argued October3, 1995. On writ of certiorari to the Fourth Circuit, 37 F.3d155, reviewing restoration of sanctions for a temporary administrative hold on a Chapter13 debtor's checking account. The questions concern §§362(a)(7), (a)(3) and (a)(6), and the consequence for the sanctions judgment.''',
'Participation':NAMES+'. All nine participate.',
'Public Action':'The Court reverses the Fourth Circuit and remands for proceedings consistent with its opinion.',
'Judgment & Remedy':'''**Reversed and remanded, 9–0.** Supporting: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. Opposing: none.

The temporary-hold theory cannot sustain the restored sanctions. The mandate identifies no issue as still open, directs no new evidentiary inquiry and reopens no unappealed contempt or later setoff order, unpreserved confirmation contention, or other final matter. Any otherwise properly remaining setoff or Code question may proceed only through its ordinary lawful channel.''',
'Opinion Topology':'Scalia delivers the opinion of a unanimous Court. All eight other Justices join Parts I–III.',
'Holdings':STR_H,
'Precedent Treatment':'''- **Studley v. Boylston National Bank:** Applied to setoff's permanent application of mutual obligations.
- **Bank of Marin v. England:** Applied to the bank's deposit-payment promise.
- **Whiting Pools:** Its property-turnover rule does not erase the separate §542(b) payment exception.
- **Celotex Corp. v. Edwards:** Its actual-injunction and orderly-review holding remains distinct from the creditor's temporary preservation here.
- **Granfinanciera:** Applied to nonreach of the unpreserved §1327 argument; confirmation priority remains undecided.''',
'Law After Decision':'''A genuinely temporary payment refusal preserving a claimed offset for prompt judicial consideration is distinct from a completed setoff and, in this deposit-debt setting, does not violate the presented control or collection provisions. Section553 creates no offset right, actual offset remains stayed without relief, and no general immunity for bank holds results. The sanctions judgment loses its stated foundation; separate statutory elements and unpresented claims remain unchanged.''',
'Separate Writings':'No separate opinion is filed.',
'Procedure After Action':'The case returns to the Fourth Circuit for proceedings consistent with reversal. No new damages trial, turnover award, constitutional remedy or reconsideration of a final or unappealed order is directed. Any otherwise properly remaining question is governed by ordinary preservation, jurisdiction and procedural requirements.',
'Source Notes':'''The [record and briefs, No.94-1340](https://archive.org/details/micro_IA40385013_0580), including the lower opinions and bankruptcy orders, support the hold, filing interval and sanctions posture. The bank's later setoff authorization and the separate contempt issue are outside this review. The Court uses the Bankruptcy Code provisions applicable to the 1991 bankruptcy; the later amendments do not govern merely because review occurs in 1995.'''}

str_internal='''## Event, channel and entering law

Research cutoff: 1995-10-31. October3 argument/October31 event are verified by the primary report and supplied inventory. Review is appellate certiorari jurisdiction, not a new setoff action. The district court reversed the bankruptcy award of $500 fees, $375 punitive damages and $25 nominal damages under then-§362(h); the Fourth Circuit restored the decision except the unappealed contempt component. The bank later obtained stay relief and setoff authorization, after the account had been emptied. The Court reviews the sanctions judgment, not entitlement to recreate depleted funds.

'''+COMMON+'''
The entering statutory text is the 1991-bankruptcy version of §§362,542,553 and1327. Standards and Tests **Interim restraint and orderly review in related bankruptcy proceedings**, present operation Celotex, April19,1995, concerns actual relatedness, judicial restraint and authorized review; it supplies no general equitable exception here. Patterson/Nobelman and BFP remain at their bounded statutory holdings; independent federal construction is preserved. Then-§362(h)'s distinct injury/willfulness and punitive conditions are not displaced. The two October31 B matters share the same entering baseline.

## Stone compatibility and final joins

The October2-approved Stone core requires reversal, actual temporary preservation tied to prompt judicial process, no good-faith exception, reservation of excess and a limited remand on setoff validity/remaining Code requirements. Parts I–III adopt his statutory reasoning, express ordinary-channel remand and limits without expanding them. The clean mandate clarification confirms that all eight Associates accept this ordinary conditional remand: it supplies no new evidentiary inquiry, finding that a question remains open, or reopening of any resolved matter. Stone joins the whole opinion. His remand is given effect within his express preservation and ordinary-channel threshold. No standing fallback is needed for the expressly controlled reversal and remedial component. An unspecified preserved claim is neither invented nor extinguished.

## Assignment and compatibility audit

The Chief is in the unanimous reversal coalition and assigns the Court opinion to Scalia. This is a fit assignment: Scalia's Patterson concurrence, Dewsnup dissent and the frozen federal-text ground specifically equip him to explain the interlocking Code provisions. Stone is the strongest alternative on the separation between preservation and actual setoff. Scalia's date-eligible Code writings particularly fit the federal-text distinction and precise relationship among three provisions; the Chief delegates that explanation while joining its complete rule and ordinary remand. The choice rests on that work fit, not a fictitious remedial disagreement. No historical authorship supplies this choice. The preceding-term review identifies no consecutive-term concentration restriction. Current effective Chief assignments before this event are Wood/O'Connor, Doe/Ginsburg and Hodge/O'Connor; no draft is counted as a committed assignment.

The Associates' former directed-remand positions were reconciled before Stone entered. The same five-day interval, express excess reservation and unpreserved confirmation issue supplied no materially changed premise from their historical reversal. Their exact grounds and retained limits are below; no assembly commitment changes.

'''+rows('## Citizens Bank','## Louisiana')+'''

No material non-Stone historical departure remains. The later clean clarification in `freeze/OT_1995CHUNK1_B_STRUMPF_MANDATE_CLARIFICATION.md` and its receipt states every Associate's acceptance of this ordinary conditional reverse-and-remand wording without changing a vote, ground or reserved issue. No substantive new inquiry is inferred from the word remand, and no remedial disagreement is invented. No opinion-assignment or circulation dialogue is fabricated.

## Source map and remaining limits

`sources/B_STRUMPF_OBJECTIVE_SOURCE_ADDENDUM.md` maps the IA joint appendix, orders, briefs and then-effective statutes; it identifies exactly which portions were read. The complete historical opinion and sole merits footnote were read and cross-checked against the entire official report. No absence of evidence is inferred from unread portions of the full record. The amount of any excess and the merits of confirmation remain unadjudicated, not operator findings. There is no present blocker to the bounded disposition.
'''

write_record('Citizens_Bank_of_Maryland_v_Strumpf_merits_1995-10-31.md','Citizens Bank of Maryland v. Strumpf, No.94-1340','1995-10-31','Reverse and remand for proceedings consistent with the opinion, 9–0.',str_internal,str_blocks,{
 'judgments':[{'component':'automatic-stay and sanctions judgment','disposition':'reverse and remand for proceedings consistent with the opinion','support':J,'oppose':[],'printed_tally':'9–0'}],
 'writings':[{'author':'Scalia','joiners':[x for x in J if x!='Scalia'],'scope':'Parts I–III','controlling':True}],
 'law_summary':str_blocks['Law After Decision'],
 'published_positions':[],
 'next_stage':str_blocks['Procedure After Action'],
 'assignment':{'assigner':'Stone-Zsela','author':'Scalia','chief_assignment':True}})

LOU_H='''### A navigation-channel shift does not transfer a continuing island between States

When a river divides around a continuing island, an established interstate boundary remains on the island's original side even if the principal downstream navigation channel shifts to its other side. Gradual erosion and accretion may move the still-running boundary channel on that original side; once it ceases running and becomes stagnant, later filling does not continue moving that fixed boundary.

**Authority:** Souter's Part I, joined by all eight other Justices, controls unanimously.

**Controlling explanation:** The ordinary thalweg rule locates a river boundary in the main downstream navigational channel and accommodates gradual erosion and accretion. Missouri v. Kentucky supplies the island exception that prevents a navigation shift alone from transferring an established island. Indiana v. Kentucky confirms that altered flow or filling does not alone transfer sovereignty, while its distinct cession basis remains intact. Arkansas v. Tennessee supplies the distinction between gradual movement of the active old channel and its eventual cessation. These rules do not make the boundary geographically immobile at the earlier navigation shift or classify every divided-channel change as an avulsion.

The Master found that the disputed area derives from Stack Island, previously on Mississippi's side, and that erosion on its east and accretion on its west moved the island toward the Louisiana bank. The inherited exception preserves Mississippi sovereignty on that supported continuity premise. Louisiana's exception A incorrectly treats the navigation channel and the continuing boundary channel as necessarily identical. The Court overrules it without deciding a general rule for newly formed islands or avulsive severance of mainland.

**Precedent treatment:** Missouri, Indiana and the two Arkansas decisions retain their distinct island, channel and cessation functions; no universal island-stability maxim replaces them.

### The record supports continuity without a new definition of an island

Louisiana's disappearance and definition exceptions are overruled because the Master's cumulative evidence supports the relevant island's continuity even under Louisiana's proposed mean-high-water test. The Court need not prescribe a universal minimum elevation, acreage or duration for an island or find uninterrupted survival of a pre-statehood landmass.

**Authority:** Souter's Part I, joined by all eight other Justices, controls unanimously.

**Controlling explanation:** The early-history alternative does not alter the relevant Mississippi-side origin of the island existing in 1881, identified in the Master's report and the expert recognition it describes. For 1883, Louisiana relies on an overlay showing a navigation line crossing the earlier map's island. Even assuming the disputed map's authenticity, the line does not prove total disappearance. Independent contemporaneous mapping, the navigation light, the 1885 affidavits describing residence and cultivation since 1882, and the Commission's 1883 works report contradict that inference.

Later vegetation, overlapping mapped landmasses, elevation evidence and the sequence of surveys support continued identity. The Court does not equate the report's 1949 elevation reference with the response's 1948 description or independently measure an unexamined exhibit. The evidence is assessed cumulatively, not by requiring every map to show all land at every river stage. Because the Master tested the island under Louisiana's demanding proposed description, exception C supplies no occasion to define all islands. Exceptions B and C are overruled. Complete destruction followed by unrelated land formation is not decided merely by retaining the same place name.

**Precedent treatment:** The inherited island exception is applied on proved continuity, not extended to every recurring shoal or similarly named formation.

### The former-channel line is accepted at the merits stage; a consistent decree must follow

The Court adopts the report's former-channel boundary recommendation and overrules the Smith-line, southern-formation and technical-treatment exceptions after independent review. Original jurisdiction is retained for a decree embodying a verified, internally consistent boundary description; no inconsistent coordinate is made operative by this decision.

**Authority:** Souter's Part I, joined by all eight other Justices, controls unanimously.

**Controlling explanation:** The report distinguishes the surveyor's earlier borrowed line from his later boundary determination and explains why the southern formations lay on Mississippi's side of the relevant channel before merger and cessation. Those findings answer exception D without a new parcel measurement or a rule awarding every downstream deposit to the island. The Court independently examines the legal and technical objections under exception E. The Master's reasoned treatment of the particular evidence is persuasive; his office does not make it binding, and Rule52 appellate deference does not control this original action.

The report's AppendixA gives Point3 as 32°48′47″N, while AppendixE gives 32°49′47″N; both give 91°09′37″W. A consistent description must be authenticated from the cited surveys or corrected before the precise implementing decree. This discrete discrepancy does not defeat the resolved legal boundary and exceptions. No costs, private-parcel injunction or unverified coordinate is ordered. Prescription and acquiescence are not reached because the island/channel ground suffices.

**Precedent treatment:** Kansas v. Colorado supplies independent original-action review with appropriate weight for supported technical work; Nebraska v. Wyoming preserves the distinction between established entitlement and the proof needed for precise relief.

### The sovereign boundary does not decide every private title

Louisiana's unexcepted rejection of its request to cancel the Houston Group's private title remains undisturbed at its stranger-to-title scope. Determining sovereignty does not itself authorize Louisiana to assert unspecified private owners' superior titles or adjudicate the rights of absent owners.

**Authority:** Souter's Part I, joined by all eight other Justices, controls unanimously.

**Controlling explanation:** Mississippi v. Louisiana places an actual controversy between States within this Court's exclusive original jurisdiction while preserving otherwise lawful private-title litigation. The boundary determination resolves sovereignty, not every competing deed. Louisiana did not except to the Master's rejection of its private-title cancellation request. The Court does not reopen it, adopt alternative patent, deed-description or laches grounds, or enter a quiet-title judgment against absent owners. An earlier district-court interstate determination made without jurisdiction has no binding force here.

**Precedent treatment:** Mississippi v. Louisiana's original-forum and private-claim distinctions are applied without enlarging the sovereign action into a universal title adjudication.

### Disagreement with the resolved evidence does not require a new supplemental hearing

The separate petition for a new supplemental hearing is denied because the incorporated record, extensive supplemental testimony and exhibits, cross-examination, argument and two site views supplied a full opportunity to present the objections, and Louisiana identifies no material defect requiring another hearing. This does not foreclose a new hearing when a genuine denial of opportunity or material evidentiary defect is established.

**Authority:** Souter's Part II, joined by Stevens, O'Connor, Scalia, Kennedy, Thomas, Ginsburg and Breyer, controls by eight votes. Stone-Zsela concurs in this component's judgment without adding a ground.

**Controlling explanation:** Independent review requires consideration of the actual objections, not repetition of proceedings whenever the Master resolves competing evidence against a party. The report describes the original and supplemental proceedings and answers the disputed continuity and location theories. Louisiana's disagreement with those answers supplies no sound reason to reopen the completed supplemental hearing. The denial neither excludes technical evidence nor presumes the Master incapable of error.

**Precedent treatment:** The independent-review principle applied in Kansas is retained; no categorical rule against further evidence is announced.'''

lou_blocks={
'Event':'''**Louisiana v. Mississippi et al., No.121, Original — October31, 1995.** Argued October3, 1995, on exceptions to the Special Master's report and a petition for a new supplemental hearing. The action concerns the interstate boundary near Stack Island and Louisiana's request to cancel the Houston Group's title. It follows the jurisdictional disposition in Mississippi v. Louisiana.''',
'Participation':NAMES+'. All nine participate.',
'Public Action':'Louisiana\'s exceptions are overruled, the report is adopted at the stated boundary and private-title scope, and the petition for a new supplemental hearing is denied. The Court directs preparation of a verified boundary decree and retains original jurisdiction.',
'Judgment & Remedy':'''| Component | Disposition and vote | Supporting Justices | Opposing Justices | Remedy |
|---|---|---|---|---|
| Exceptions A–E | Overruled, 9–0 | Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | — | Adopt the former-channel recommendation at the resolved merits scope. |
| New supplemental hearing | Denied, 9–0 in judgment | All nine participating Justices | — | Eight adopt the Court's reasons; Stone-Zsela joins the denial without an additional ground. |
| Unexcepted private-title rejection | Left undisturbed, 9–0 | All nine participating Justices | — | No cancellation or general adjudication of private deeds. |
| Implementing decree | Preparation directed; jurisdiction retained, 9–0 | All nine participating Justices | — | Authenticate a consistent boundary schedule before entry. |

No prescription or acquiescence ground is decided, and no disputed coordinate becomes operative today.''',
'Opinion Topology':'''| Writing | Author | Joined by | Scope |
|---|---|---|---|
| Opinion of the Court, Part I | Souter | Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Thomas, Ginsburg, Breyer | Boundary, exceptions, private-title scope and later decree. |
| Opinion of the Court, Part II | Souter | Stevens, O'Connor, Scalia, Kennedy, Thomas, Ginsburg, Breyer | Reasons for denying the new supplemental hearing. Stone-Zsela concurs in that judgment only. |''',
'Holdings':LOU_H,
'Precedent Treatment':'''- **Missouri v. Kentucky, 78 U.S.395,401:** Supplies the established-island exception to a change in the main navigation channel.
- **Indiana v. Kentucky, 136 U.S.479,508–509:** Confirms the limited significance of altered flow or filling; its separate cession basis is not generalized away.
- **Arkansas v. Tennessee, 246 U.S.158; 397 U.S.88:** Supply the active-old-channel and cessation distinction.
- **Louisiana v. Mississippi, 202 U.S.1; 282 U.S.458; 384 U.S.24; 466 U.S.96:** Their thalweg rules remain subject to the established island exception.
- **Mississippi v. Louisiana:** Exclusive interstate jurisdiction and distinct private-title litigation remain intact.
- **Kansas v. Colorado; Nebraska v. Wyoming:** Their independent review, proof and remedial limits are applied to the original proceeding.''',
'Law After Decision':'''The island exception preserves the established side of a continuing island despite a navigation-channel shift, while permitting ordinary movement of the active boundary channel until cessation fixes it. The report's continuity and former-channel determinations control this sovereign dispute. No universal island definition, prescription holding, private-title judgment against absent owners or numerical boundary decree is added. The precise implementing decree remains to be entered from a consistent description.''',
'Separate Writings':'No separate opinion is filed. Stone-Zsela concurs only in the judgment denying a new supplemental hearing and adopts no additional reason on that component.',
'Procedure After Action':'''Original jurisdiction is retained. A proposed decree must embody the report's verified former-channel boundary and resolve the inconsistent Point3 latitude before entry. The Court issues no new supplemental-hearing order, private-title cancellation or cost allocation at this stage.''',
'Source Notes':'''The [Master's final report](https://www.supremecourt.gov/pdfs/recordsandbriefs/1000370934/1000370934_008.pdf) and [Louisiana's exceptions and new-hearing petition](https://www.supremecourt.gov/pdfs/recordsandbriefs/1000370934/1000370934_009.pdf) supply the survey history, competing continuity accounts and objections. AppendicesA andE give different latitudes for Point3; the precise decree awaits authentication of the underlying surveys or a corrected description. The decision does not resolve map authenticity or the report/response's 1948–1949 elevation-date discrepancy.'''}

lou_internal='''## Event, channel and entering law

Research cutoff: 1995-10-31. Argument and exception-decision dates are verified in the primary report and inventory. This is §1251(a) original jurisdiction, not appellate review of the jurisdictionally defective interstate district judgment. The prior Mississippi v. Louisiana decision left private claims distinct. All exceptions A–E, the separate new-hearing request, the unexcepted title recommendation and later decree implementation are identified separately; prescription is an alternative not reached.

'''+COMMON+'''
Standards and Tests **Exclusive interstate jurisdiction and private boundary-related claims**, present operation Mississippi v. Louisiana, December14,1992, governs the forum/title distinction. Kansas v. Colorado (May15,1995) and Nebraska v. Wyoming (May30,1995) supply current original-review and remedial principles. Missouri v. Kentucky, Indiana v. Kentucky, both Arkansas v. Tennessee decisions and the earlier Louisiana/Mississippi thalweg decisions remain available at their actual conditions. The new Wood/Doe/Hodge holdings do not alter this original jurisdiction, independent review or title separation. Strumpf and this event share the common October31 baseline.

## Stone compatibility and fixed-core application

Stone's October2-approved core overrules every exception, adopts the supported continuity/report recommendation, leaves unexcepted private-title rejection undisturbed, retains jurisdiction and directs a verified decree without invented coordinates. Part I follows those instructions. Applying the inherited old-channel rule answers exception A without inventing a new island definition; the technical and southern-line answers implement the same inherited rule and report adoption. The conflicting schedule is reserved for the expressly required verification rather than selected by inference.

**Standing fallback applied:** the separately requested new supplemental hearing is not expressly addressed by SectionII. Stone joins the majority's denial of that component and adds no ground. He therefore does not join Part II. This is a vote-only use, not authority to attribute the Associates' procedural reasoning to him. The Public Projection names that judgment-only scope.

## Assignment and final compatibility

The Chief belongs to the unanimous judgment coalition and assigns Souter. His Nebraska original-action opinion offers particular fit in separating sovereign scope, private claims and proof necessary for a later decree. O'Connor's Kansas opinion supplies strong technical-review capability; Souter's combined jurisdiction/remedy fit is at least as good for this particular original boundary disposition. Stone is a capable alternative on continuity and scope, but his core requires no new doctrinal formulation that his own authorship alone would preserve, and Souter carries the eight-Justice new-hearing explanation without attributing it to Stone. This is a fit assignment, not importation of historical authorship. No preceding-term concentration ceiling applies; current actual assignments must be counted at preservation, with draft assignments excluded.

Every Associate retains the frozen result and limits. No circulation revision changes a non-Stone commitment, and no historical merits departure is claimed. The coordinate condition is a later implementation source limit, not a new reason for a changed vote.

'''+rows('## Louisiana','## Libretti')+'''

## Source map and precise remaining condition

`sources/B_LOUISIANA_OBJECTIVE_SOURCE_ADDENDUM.md` records full readings of the report and exceptions/response and visual checks of the two printed schedules. The older island authorities were separately authenticated in `sources/B_MODEL_PREDIVERGENCE_BOUNDARY_SOURCE_RECEIPT.md`. The historical single opinion was read in full and all seven official pages cross-checked. The exact later-decree condition is Point3: AppendixA 32°48′47″N versus AppendixE 32°49′47″N, both91°09′37″W. Obtain cited P-32D, LA-1A, P-32E, counterclaim¶5 or authenticated correction before a numerical decree. No such decree is drafted here. This does not block the present exception event.
'''

write_record('Louisiana_v_Mississippi_original_exceptions_1995-10-31.md','Louisiana v. Mississippi et al., No.121, Original','1995-10-31','Exceptions overruled; report adopted at the stated scope; new hearing denied; verified decree directed; original jurisdiction retained, all 9–0 in judgment.',lou_internal,lou_blocks,{
'judgments':[{'component':c,'disposition':d,'support':J,'oppose':[],'printed_tally':'9–0'} for c,d in [('exceptions A-E','overrule'),('new supplemental hearing','deny'),('unexcepted private-title rejection','leave undisturbed'),('later decree','direct verified preparation; retain jurisdiction')]],
'writings':[{'author':'Souter','joiners':[x for x in J if x!='Souter'],'scope':'Part I','controlling':True},{'author':'Souter','joiners':[x for x in A if x!='Souter'],'scope':'Part II; Stone-Zsela judgment only','controlling':True}],
'law_summary':lou_blocks['Law After Decision'],'published_positions':[], 'next_stage':lou_blocks['Procedure After Action'],
'assignment':{'assigner':'Stone-Zsela','author':'Souter','chief_assignment':True},'later_event_blocker':'Authenticate Point3 latitude from cited survey or correction before precise implementing decree.'})

