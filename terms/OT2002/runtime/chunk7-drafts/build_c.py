from pathlib import Path
import json

OUT = Path('terms/OT2002/runtime/chunk7-drafts')
ALL = ['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']
ASSOCIATES = ALL[1:]
specs = []

def component(name, supporting, alternatives=None):
    d = {'name':name, 'supporting':supporting, 'opposing':[j for j in ALL if j not in supporting]}
    if alternatives: d['alternative_positions'] = alternatives
    return d

def write(case, date, filename, result, internal, blocks, spec):
    text = f'**Case and dockets:** {case}\n**Event and date:** {spec.pop("event")}; {date}. October Term 2002, chunk 7.\n**Result:** {result}\n**Version / lineage:** Initial assembly draft from frozen chunk 7 handoffs; supersedes no adjudication.\n\n'
    text += internal.strip() + '\n\n## Public Projection\n\n'
    for heading, body in blocks.items(): text += f'## {heading}\n\n{body.strip()}\n\n'
    (OUT / filename).write_text(text.rstrip()+'\n', encoding='utf-8')
    spec.update(case=case.split(';')[0], date=date, file=filename)
    specs.append(spec)

black_h = '''### I. An intentional threatening method may be prohibited

**Holding and operative rule.** Virginia may prohibit burning a cross on another's property, a highway, or another public place with intent to intimidate a person or group through a serious threat of unlawful violence, when the prohibition operates without regard to the speaker's viewpoint. The State must prove the threatening communication and the statutory intent beyond a reasonable doubt in the circumstances of the particular act; an intent actually to carry out the threatened violence is unnecessary.

**Authority.** Part I of the lead opinion is an opinion of the Court: Stone-Zsela, Stevens, O'Connor, Scalia and Breyer directly join its rule and explanation. Thomas agrees that the confined offense is permissible on his distinct conduct and alternative First Amendment grounds.

**Controlling explanation.** The Court holds that the State may address this distinctive method of intimidation because its threatening force, rather than disapproval of an idea, defines the prohibited harm. The history of cross burning explains why its use can convey a grave threat, but the history does not establish the meaning or intent of every burning. A political rally, religious ritual or hostile ideological message falls outside the offense unless the actual communication and intent satisfy its elements. R. A. V. supplies the substantial-overbreadth rule while leaving distinctions wholly within an unprotected category open. The present confined permission answers the question about this threatening method. American Life League sustains defined harmful conduct while preserving protected advocacy; ACLA establishes that public dissemination can communicate an attributable contextual threat. Those principles answer the contention that either the symbol's expressive uses or its public setting categorically immunize intentional threatening intimidation. Conversely, the State cannot use its interest in safety to punish political or religious disapproval alone. Virginia's express intent requirement permits resolution without choosing the minimum culpability for criminal statutes lacking that element, a question outside this grant.

### II. Black's specific instruction does not preserve the required distinction

**Holding and operative rule.** An instruction permitting the burning of a cross by itself to establish intent to intimidate cannot sustain Black's conviction where the charge leaves unresolved whether the jury evaluated the communication's context and rebuttal evidence or treated burning alone as sufficient. General directions to consider both sides' evidence and prove each element beyond a reasonable doubt do not dispel that specific constitutional ambiguity.

**Authority.** Part II is an opinion of the Court joined by Stone-Zsela, Stevens, O'Connor, Scalia and Breyer. They directly agree on the defect in Black's charge; their different positions on facial invalidity and the indictment are identified separately.

**Controlling explanation.** The Court holds that the actual charge allowed the jury to pass from an expressive act to criminal intimidation without a reliable determination of the feature separating a threat from protected advocacy. Instructions 6 and 8 required consideration of both sides' evidence and proof beyond reasonable doubt of burning and intent. Yet the additional by-itself instruction left the jury free to understand the symbol as sufficient despite evidence of a different meaning. Correct general directions do not show that the jury resolved that conflict constitutionally. ACLA requires contextual and attributable threatening meaning and separates the actual liability adjudication from findings supporting other relief; evidence concerning another respondent cannot repair Black's charge. County Court of Ulster County v. Allen distinguishes permissible evidentiary inferences from substitution for an element, and Carella v. California underscores the need to examine the instruction actually given. The State's argument that the entire charge necessarily preserved a permissible inference leaves the operative ambiguity unanswered. The ruling concerns that charge and supports leaving the conviction set aside.

### III. Black's indictment and the facial question

Black's conviction vacatur and indictment dismissal are affirmed. Seven Justices support affirmance of the indictment dismissal, but no five adopt a common rationale for that part of the judgment. Stevens, O'Connor and Breyer rely on facial invalidity of the proof provision in its present model-instruction operation; Stone-Zsela joins that proof analysis but concurs only in the judgment affirming the indictment dismissal. Kennedy, Souter and Ginsburg rely on invalidity of the selected prohibition as a whole. The four-Justice facial-proof analysis and the three-Justice offense-wide analysis are distinct grounds, not a controlling facial rule.

### IV. The different Elliott and O'Mara judgments require separate review

**Holding and operative rule.** The judgments vacating Elliott's attempted-cross-burning conviction and dismissing its indictment, and vacating O'Mara's attempted-cross-burning and conspiracy convictions and dismissing their indictments, are vacated and remanded. Virginia's courts must determine the available authoritative construction or severance of state law and apply the constitutional requirements to Elliott's own trial record and O'Mara's conditional plea, including preserved objections and applicable restrictions on further prosecution.

**Authority.** Part IV is an opinion of the Court joined by Stone-Zsela, Stevens, O'Connor, Scalia and Breyer. Their agreement on this state-law and defendant-specific remand does not require agreement on the facial analysis in Part III.

**Controlling explanation.** Elliott's jury received no Black prima facie instruction, and O'Mara preserved his constitutional challenge by conditional plea. A defect in Black's actual charge therefore does not supply their complete disposition. Because the confined intent offense is constitutionally permissible, categorical invalidation of that offense cannot by itself sustain their judgments. The state court must first determine what law validly remains and what follows on the respective records. A saving application must actually remove the unconstitutional permission to use the symbol alone as sufficient proof; a nominal disclaimer retaining that permission does not suffice. If the offense cannot operate independently under state law, an inseverable prohibition cannot sustain further proceedings. The Court supplies no state-law severability determination. Griffith v. Kentucky applies the constitutional instruction rule to nonfinal criminal cases within its scope, subject to preservation and genuine error rules; final judgments require independently applicable collateral authority. Elliott's conspiracy acquittal remains untouched. Black's affirmed indictment dismissal ends proceedings under that indictment, while these other respondents receive the distinct remand their records require.'''

black_pre = '''R. A. V. v. City of St. Paul, 505 U.S. 377, retains its substantial-overbreadth holding; this decision resolves its open content-selection question only for the defined viewpoint-independent method of intentional intimidation.

American Life League v. Reno (November 13, 1995) supplies the distinction between defined harmful conduct and protected advocacy. Its service-purpose law is distinct from the selected threatening method here.

Planned Parenthood of the Columbia/Willamette, Inc. v. American Coalition of Life Activists (December 10, 2002) supplies contextual threatening meaning, attribution and attention to the actual adjudication. Its purpose-or-knowledge rule continues to govern the civil liability it addressed; Virginia independently requires intent to intimidate.

County Court of Ulster County v. Allen, 442 U.S. 140, and Carella v. California, 491 U.S. 263, supply the distinction between permissible inference and an instruction that compromises the required determination of an element. They inform the presented First Amendment instructional question.

Griffith v. Kentucky, 479 U.S. 314, supplies application to nonfinal criminal cases. Preservation, ordinary error rules and separate collateral-review law retain their respective functions.'''

black_law = '''The State may prohibit this viewpoint-independent method of intentional threatening intimidation, with proof of an actual serious threat and the statutory intent in context. Black's particular by-itself charge is constitutionally inadequate despite its general burden instructions. The Court's direct majorities establish those rules and the Elliott/O'Mara remand. The facial question remains fractured at the level described in Part III; the affirmed dismissal of Black's indictment binds the parties. Further proceedings for Elliott and O'Mara apply the constitutional requirements to the state law that validly remains and their different adjudicative records.'''

black_sep = '''**Part III of the lead opinion: Stevens, O'Connor and Breyer; Stone-Zsela joins its facial-proof analysis.** These Justices conclude that the proof provision in its model-instruction operation reaches substantial protected expression. Cross burning has political and ritual uses, and treating the act alone as sufficient permits conviction across a substantial identifiable range of those uses. The problem reaches beyond a single erroneous instruction because the model instruction remains undisavowed. General proof directions do not remove its specific permission. The state court has yet to supply a final construction, and construction or severance remains for the distinct Elliott and O'Mara remands. Stevens, O'Connor and Breyer affirm Black's indictment dismissal on that present facial ground. Stone-Zsela concurs in that part of the judgment without joining its indictment rationale.

**Scalia, concurring in part and dissenting in part; Thomas joins the facial-construction portion only.** Scalia accepts the confined offense, rejects present facial invalidation and would obtain an authoritative state construction. Prima facie evidence may be sufficient when unrebutted while leaving the jury obliged to weigh contrary evidence; possible misuse alone does not establish substantial overbreadth. Thomas joins that construction objection. Scalia separately concludes that Black's by-itself instruction leaves intolerable uncertainty whether the jury considered rebuttal notwithstanding Instructions 6 and 8. He would retain conviction vacatur, vacate the indictment dismissal and permit a retrial under a valid construction, subject to ordinary restrictions. Thomas does not join this instructional conclusion or retrial disposition.

**Souter, concurring in the judgment as to Black and dissenting as to Elliott and O'Mara, joined by Kennedy and Ginsburg.** They would resolve the open content-selection question against this prohibition. The combination of a symbol-specific offense and evidentiary privilege presents a realistic danger that suppressing the associated ideology partly explains the selection. A cross can convey ideology, intimidation or both. The proof provision tilts doubtful cases toward punishment, and a general intimidation law can protect safety without this selection. They would affirm every reviewed conviction vacatur and indictment dismissal. Later removal of the proof clause cannot validate prosecutions under a law constitutionally defective when the conduct occurred.

**Thomas, dissenting.** Thomas principally treats intentional cross burning as terrorizing conduct by a particular means. Alternatively, its history gives the permissive inference a rational basis under Allen, while the whole charge preserves the prosecution's burden and the jury's ability to reject the inference. He would reverse the reviewed constitutional grounds for vacatur and dismissal for each respondent and remand for remaining preserved matters, including O'Mara's plea consequences. His position requires statutory intimidating intent and does not make every political or ritual cross burning criminal.'''

black_j = '''| Judgment component | Disposition and vote | Supporting Justices | Opposing Justices | Remedy |
|---|---|---|---|---|
| Black's existing cross-burning conviction | Affirm vacatur, 8–1 | Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Ginsburg, Breyer | Thomas | Conviction remains vacated. |
| Black's indictment | Affirm dismissal, 7–2 | Stone-Zsela, Stevens, O'Connor, Kennedy, Souter, Ginsburg, Breyer | Scalia, Thomas | Dismissal remains effective; no new prosecution under that indictment. Scalia would vacate dismissal and permit lawful retrial; Thomas would reverse the reviewed constitutional grounds and remand. |
| Elliott's attempted-cross-burning conviction and indictment | Vacate and remand, 5–4 | Stone-Zsela, Stevens, O'Connor, Scalia, Breyer | Kennedy, Souter, Thomas, Ginsburg | State construction or severance and defendant-specific review. Kennedy, Souter and Ginsburg would affirm both forms of relief; Thomas would reverse the reviewed constitutional grounds and remand. |
| O'Mara's attempted-cross-burning and conspiracy convictions and indictments | Vacate and remand, 5–4 | Stone-Zsela, Stevens, O'Connor, Scalia, Breyer | Kennedy, Souter, Thomas, Ginsburg | State construction or severance and the consequences of the conditional plea for both offenses. Kennedy, Souter and Ginsburg would affirm all reviewed relief; Thomas would reverse the reviewed constitutional grounds and remand. |

Elliott's conspiracy acquittal remains effective. The constitutional instructions and state-law remand conditions appear in Holdings, Part IV.'''

black_top = '''__LEAD_AUTHOR__ delivers the opinion of the Court as to Parts I, II and IV and announces the judgment with an opinion as to Part III, joined throughout by __LEAD_JOINERS__.

| Writing or portion | Direct joins and authority | Relationship to judgment |
|---|---|---|
| Lead opinion, Parts I, II and IV | Stone-Zsela, Stevens, O'Connor, Scalia and Breyer, including the author | Court rationale for the confined offense, Black's charge and the Elliott/O'Mara remands. |
| Lead opinion, Part III's facial-proof analysis | Stone-Zsela, Stevens, O'Connor and Breyer, including the author | Four-Justice plurality. |
| Lead opinion, Part III's Black indictment rationale | Stevens, O'Connor and Breyer, including the author | Three-Justice rationale; Stone-Zsela concurs only in this judgment component. |
| Scalia separate opinion | Thomas joins only its rejection of facial invalidation and request for state construction | Scalia alone supports a lawful Black retrial after vacatur of the indictment dismissal. |
| Souter separate opinion | Kennedy and Ginsburg join in full | Affirms all reviewed vacaturs and dismissals on offense-wide invalidity. |
| Thomas dissent | Thomas | Would reverse the reviewed constitutional grounds and remand in each defendant's case; agrees in the operative permission for the confined offense. |'''

black_internal = '''## Event, chronology and source map

On review of Black v. Commonwealth, 262 Va. 764, 553 S.E.2d 738 (November 2, 2001), Supreme Court No. 01-1107; argued December 11, 2002; decided April 7, 2003. The primary syllabus header supplies the argument date, confirmed by source control before assembly completion. The challenged law is Va. Code §18.2-423. Black's rally occurred with the private landowner's permission and was observable by neighbors; Elliott and O'Mara's act occurred in a neighbor's yard. Black received the disputed prima facie instruction together with Instructions 6 and 8. Elliott received no such prima facie instruction; O'Mara pleaded conditionally. The validated Black supplement supplies all three indictment dismissals and Elliott's separate conspiracy acquittal. These are reported record facts, not independent findings of intent.

Sources: frozen C_NEUTRAL, BLACK_VALIDATED_NEUTRAL and BLACK_UNDERLYING_JUDGMENT_SOURCE_FACTS; the final C_RECONCILED section 87 is the effective Associate handoff. Its complete-opinion verification and state-opinion reading receipts resolve the prior source gaps. The original C and supplemental Black commitment files retain lineage but the final reconciliation controls. Research cutoff: April 7, 2003. No new historical fact or Associate ground is introduced in assembly.

## Participation, entering law and form before assignment

All nine participate at review and decision: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No nonparticipation is identified. Nine participants provide a quorum and five votes establish a majority. This is plenary constitutional review. Its actual mixed judgments, direct majority rules and facial fracture require one signed lead, Court portions and noncontrolling portions, plus the separate writings identified below. Form and propositions were fixed before any author count.

The entering-law slice carries R. A. V. (June 22, 1992), American Life League (November 13, 1995) and ACLA (December 10, 2002), all effective before this event. R. A. V. requires substantial protected coverage and actual permissible narrowing; its within-category content-selection theory is noncontrolling. American Life League preserves intentional harmful conduct and protected advocacy. ACLA supplies contextual attributable threats and purpose or knowledge for its civil liability, with separate adjudication of damages and injunction predicates. Allen, Carella and Griffith are date-eligible background as identified in the reconciled handoff. Unrelated same-day events supply no law here.

## Approved Stone position and final compatibility

The approved C_STONE supplement fixes validity of the viewpoint-independent threatening method, contextual beyond-reasonable-doubt proof of threat and statutory intent, rejection of symbol-alone sufficiency, affirmance of Black's conviction vacatur, and the Elliott/O'Mara remands subject to state severability, preservation and retrial law. It adopts no state-law severability finding. The lead's Parts I, II, III facial-proof analysis and IV fit those instructions. Stone's express direction permitting only otherwise lawful proceedings does not require a Black retrial or direct vacatur of his dismissed indictment.

The separate existing indictment-dismissal component is unaddressed expressly. The standing fallback supplies Stone's vote to affirm that dismissal with the six Associates who do so, and supplies no rationale. The fallback does not override the explicit conviction or remand positions. Stone therefore joins no indictment-dismissal rationale and is ineligible to author the whole lead. His ordinary Griffith transition is incorporated in the governing remand and creates no separate-writing function. No other fallback is used. No distinct Stone writing is needed: his adopted rule, limits and partial join are accurately represented.

## Complete controlling law

BLACK_H

## Judgment, precedent, current law and stage

BLACK_J

BLACK_PRE

BLACK_LAW

On remand Virginia determines authoritative construction or severance and then the permitted consequences for Elliott's trial and O'Mara's plea. Black's affirmed dismissal concludes that indictment. 

## Opinion topology and published continuity

BLACK_TOP

BLACK_SEP

Every position above is retained for continuity at its stated level. The plurality facial rule has four direct votes; the proposed offense-wide content-selection theory has three. Neither enters controlling law. The indictment result has seven judgment votes without a five-Justice rationale. No Marks synthesis is claimed: the present proof-construction route and the offense-wide anti-selection rule rest on distinct predicates, and the supporters do not adopt a common operative facial rule. Their fact-specific overlap in Black's relief is not an adopted logical-subset holding.

## Adaptive audit annex

| Justice | Frozen commitment, source basis and final join test |
|---|---|
| Stevens | Sustains core on his R. A. V. overbreadth position and American Life League/ACLA grounds; adopts model-instruction facial invalidity and Black charge defect; affirms Black dismissal; remands others. Full lead join, including remedy. The lead uses the confined harmful-method explanation without requiring adoption of a historical R. A. V. exception. |
| O'Connor | Same dispositions; her R. A. V. position, Ferber concurrence and verified Black treatment of this actual charge support facial analysis despite Instructions 6 and 8. Full lead join, with possible construction/severance reserved for the other respondents. |
| Scalia | Sustains core using his harm-based selection position; rejects facial invalidation; finds the actual charge ambiguous under Allen/Carella; preserves Black conviction vacatur but vacates indictment dismissal for lawful retrial; remands others for construction. Joins I, II and IV, not III; separate opinion preserves the exact remedy objection. |
| Kennedy | His R. A. V. and Johnson positions and ACLA attribution concerns support adopting a narrow anti-suppression selection rule here. Affirms all relief and joins Souter; no lead join is attributed. |
| Souter | His R. A. V. and Barnes positions distinguish harm from message suppression; the proof privilege undermines an exclusively harm-based selection. Affirms all relief; writes the offense-wide separate ground. |
| Thomas | Pinette, his R. A. V. position and verified Black dissent support terrorizing-conduct and rational-inference grounds. Instructions 6 and 8 confirm his approval. Supports core permission but refuses lead expressive rationale and Black charge holding. Joins only the construction critique of Scalia's separate opinion and dissents on the judgments. |
| Ginsburg | Her American Life League, ACLA and Bartnicki positions and verified agreement with Souter support the prospective anti-suppression rule. Affirms all relief; joins Souter, without claiming a controlling R. A. V. content rule. |
| Breyer | American Life League/ACLA contextual protections and Bartnicki expression/harm reasoning support the confined core; the verified facial-proof and Black-dismissal positions remain strong evidence. Full lead join with individual remands. |

Historical reconciliation: the full source contains the same Instructions 6 and 8 and the actual indictment dismissals. Their recovery supplied no changed historical premise. The final freeze accordingly corrected Scalia's intermediate approval of the charge and Stevens', O'Connor's and Breyer's intermediate Black-indictment remand. These unsupported intermediate positions are not used. The historical principal opinion had five core supporters including Rehnquist and four facial-proof supporters; Stevens wrote separately, Scalia's instruction portion lacked Thomas, Souter wrote with Kennedy/Ginsburg, and Thomas dissented. Historical authorship supplies no assignment here.

**Historical departure:** Kennedy, Souter and Ginsburg retain their historical results but materially restate their doctrinal premise: this Court's R. A. V. did not adopt the within-category content rule. Kennedy's own R. A. V./Johnson positions, Souter's R. A. V./Barnes positions and Ginsburg's verified Black agreement with the anti-suppression analysis support proposing that rule on the question left open, rather than treating it as binding prior law. The core supporters likewise justify this confined method under the actual overbreadth baseline; that changed status warrants no unsupported vote or remedial change.

The principal contrary grounds are answered in the lead: protected expressive uses require contextual proof rather than immunity for intentional threats; correct general instructions do not remove the specific by-itself ambiguity. The plurality separately answers Scalia's facial-construction objection while preserving the actual unresolved state construction. No new objection, circulated change or post-freeze Associate vote is invented.

__ASSIGNMENT_BLOCK__

Whole-lead eligible authors and complete direct joiners: Stevens, O'Connor, Breyer. Stone joins each judgment majority and therefore assigns the lead, but his fallback-only indictment vote excludes whole-opinion authorship. One of the three eligible Justices can carry every Court and plurality proposition; division of authorship is unnecessary. Final author and assignment await the root's serial recount.

## Section 15 validation status

Substantive compatibility, exact three-defendant relief, proposition-level arithmetic, source cutoff and historical reconciliation reviewed. The complete holdings below are copied from the same string as the internal law. Section 8 negative-statement review passed for Judgment & Remedy, Holdings, Precedent Treatment, Law After Decision, Procedure After Action and their internal counterparts: retained negatives concern the actual facial fracture, the surviving indictment/acquittal statuses, genuinely outside-grant criminal culpability, the Court's adopted proof/state-law limits, or the remedy sought. Unneeded disclaimers concerning guilt, damages and unrequested proceedings were excluded from those blocks. Computational draft checks and final assignment/integration checks remain for the root; this draft is not committed.'''

for a,b in [('BLACK_H',black_h),('BLACK_J',black_j),('BLACK_PRE',black_pre),('BLACK_LAW',black_law),('BLACK_TOP',black_top),('BLACK_SEP',black_sep)]: black_internal=black_internal.replace(a,b)

write('Virginia v. Black; No. 01-1107; 538 U.S. 343','2003-04-07','Virginia-v-Black_merits_2003-04-07.md','Black conviction vacatur and indictment dismissal affirmed; Elliott and O\'Mara judgments vacated and remanded.',black_internal,{
'Event':'''Virginia v. Black, No. 01-1107. Argued December 11, 2002; decided April 7, 2003. On writ of certiorari to the Supreme Court of Virginia, 262 Va. 764, 553 S.E.2d 738. The questions are whether Virginia may prohibit cross burning with intent to intimidate and whether its prima facie proof provision impermissibly reaches protected expression. Black's political rally, Elliott's jury trial and O'Mara's conditional plea present distinct records. The state court vacated Black's cross-burning conviction, Elliott's attempted-cross-burning conviction and O'Mara's attempted-cross-burning and conspiracy convictions, and dismissed their corresponding indictments.''',
'Participation':'Stone-Zsela, Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participate.',
'Public Action':'The judgment is affirmed as to Black and vacated and remanded as to Elliott and O\'Mara.',
'Judgment & Remedy':black_j,'Opinion Topology':black_top,'Holdings':black_h,'Precedent Treatment':black_pre,'Law After Decision':black_law,'Separate Writings':black_sep,
'Procedure After Action':'''Black's conviction remains vacated and his indictment dismissed. The Elliott and O'Mara matters return to the Virginia courts for the state-law and record-specific work directed in Holdings, Part IV. Any further prosecution must comply with those constitutional requirements, preserved objections and applicable retrial restrictions.''',
'Source Notes':'''Va. Code §18.2-423; Black v. Commonwealth, 262 Va. 764, 553 S.E.2d 738, 746 (2001); Black trial Instructions 6 and 8 and the separate prima facie instruction; No. 01-1107. Elliott's conspiracy acquittal is outside the convictions under review. O'Mara's conditional plea preserved his constitutional challenge.'''
},{'event':'Merits decision','form':'signed plenary','assigner':'Stone-Zsela','eligible_authors':['Stevens',"O'Connor",'Breyer'],'full_joiners':['Stevens',"O'Connor",'Breyer'],'chief_assigns_any':True,'components':[
component('Black conviction vacatur affirmed',[j for j in ALL if j!='Thomas']),
component('Black indictment dismissal affirmed',['Stone-Zsela','Stevens',"O'Connor",'Kennedy','Souter','Ginsburg','Breyer'],[{'position':'Vacate dismissal and permit lawful retrial','justices':['Scalia']},{'position':'Reverse reviewed constitutional grounds and remand','justices':['Thomas']}]),
component('Elliott attempted-cross-burning conviction and indictment judgments vacated and remanded',['Stone-Zsela','Stevens',"O'Connor",'Scalia','Breyer'],[{'position':'Affirm conviction vacatur and indictment dismissal','justices':['Kennedy','Souter','Ginsburg']},{'position':'Reverse reviewed constitutional grounds and remand','justices':['Thomas']}]),
component('OMara attempted-cross-burning and conspiracy conviction and indictment judgments vacated and remanded',['Stone-Zsela','Stevens',"O'Connor",'Scalia','Breyer'],[{'position':'Affirm all reviewed vacaturs and dismissals','justices':['Kennedy','Souter','Ginsburg']},{'position':'Reverse reviewed constitutional grounds and remand','justices':['Thomas']}]) ]})

peavy_h = '''### Settlement ends review; vacatur requires a separate equitable basis

**Holding and operative rule.** Settlement of the underlying actions removes the live controversy in this review and requires its dismissal as moot. Under 28 U.S.C. §2106, the Court retains authority to make an appropriate disposition of the judgment lawfully before it, but voluntary settlement ordinarily does not justify vacatur without a further sufficient equitable reason; none is established here.

**Authority.** The Court's unsigned order applies the controlling mootness and equitable-vacatur rules of U.S. Bancorp Mortgage Co. v. Bonner Mall Partnership. The order publishes its grounds, without a tally or individual lineup.

**Controlling explanation.** The Court holds that the settlement resolved the original Peavy and Oliver wiretap actions against WFAA and Riggs. No concrete remaining adverse claim or redressable relief within this review survives that resolution. A separate dispute about advice or settlement proceeds does not revive the original participant-publisher controversy. Bancorp distinguishes the loss of authority to decide those underlying merits from the power to dispose of the judgment already under review. It also distinguishes voluntary settlement from happenstance that frustrates review without the appellant's choice. The reported payment was consideration for resolving the actions; it supplies no exceptional equitable reason to erase the appellate judgment. Even an agreement's preference for vacatur would not itself establish that entitlement. Accordingly, review ends and the Fifth Circuit judgment remains undisturbed. The participant-publisher constitutional and statutory questions are not reached because the live controversy necessary to adjudicate them has ended.'''

peavy_pre = '''U.S. Bancorp Mortgage Co. v. Bonner Mall Partnership, 513 U.S. 18, applies: subsequent mootness ends merits review but preserves §2106 dispositional authority; a voluntary settlement requires a further sufficient equitable reason for vacatur. United States v. Munsingwear, Inc., 340 U.S. 36, retains its different setting of review frustrated by happenstance and does not supply automatic vacatur after voluntary settlement.'''
peavy_law = '''Existing mootness and equitable-vacatur rules govern the settled review. The Fifth Circuit judgment remains in place without a Supreme Court adjudication of its underlying wiretap or First Amendment grounds. The participant-publisher question remains outside this disposition because the parties' controversy has ended.'''
peavy_internal = '''## Event, chronology, source map and entering law

This is the accepted scheduled review of Peavy v. WFAA-TV, Inc., 221 F.3d 158, Fifth Circuit No. 99-10272, decided July 31, 2000. The assigned Court event is April 7, 2003. No historical Supreme Court docket, grant or argument date is asserted. The question concerned participation in unlawful interception followed by use or disclosure on a public-concern subject. The lower judgment was mixed, requiring further proceedings on some statutory claims; its entire set of claims is not treated as uniformly revived.

The judicial factual account in Jenkens & Gilchrist v. Riggs, 87 S.W.3d 198, 200 (Tex. App. 2002), dated September 17, 2002, reports global resolution of the Peavy and Oliver actions against WFAA and Riggs, with aggregate payment of $5 million by WFAA and Jenkens & Gilchrist. The validated SUPPLEMENT_NEUTRAL accepts that historical proposition under Engine §14. Exact allocation, release text and dismissal instruments are not asserted. Missing original instruments do not establish a surviving claim or litigant default. The accepted scheduled arrival remains a procedural premise distinct from continuing adversity.

Frozen C_NEUTRAL, PEAVY_SOURCE_FACTS, SUPPLEMENT_VALIDATED_NEUTRAL and final C_RECONCILED supply the sources and support. The settlement source, corroboration and source-reading limits are preserved there. No complete reading of the 82-page merits opinion is claimed or required for the settled threshold path. Research cutoff: April 7, 2003. Entering Bancorp (November 8, 1994) was read in the selected slice: subsequent mootness leaves §2106 dispositional authority, and voluntary settlement ordinarily requires a further sufficient equitable reason for vacatur. Munsingwear's happenstance setting remains distinct. Bartnicki's nonparticipant holding supplies no jurisdiction to reach the conditional participant question.

## Participation and form fixed before counting

All nine participate at consideration and decision: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No nonparticipation is identified; quorum is satisfied, five votes suffice. The live-dispute and judgment-treatment grounds call for an unsigned procedural dismissal, not a plenary lead opinion. Form is fixed on those grounds before any count. No public tally or lineup is disclosed.

## Stone and final compatibility

Stone's approved supplement expressly prioritizes settlement mootness and separate Bancorp vacatur analysis. The supported global-resolution record satisfies his conditional termination branch. His core requires termination where no concrete remaining claim exists and preservation of the judgment absent a further equitable reason; he directly joins both grounds. The older source caveat about missing settlement instruments is resolved by the approved bounded-source method, not by fictional terms. No fallback is used. His conditional participant-liability theory never becomes operative and supplies neither holding nor published dictum.

## Complete controlling law

PEAVY_H

## Judgment, precedent, current law and stage

Internal component votes: all nine dismiss this review as moot; all nine deny vacatur and leave the existing Fifth Circuit judgment intact. These votes remain internal. There is no new litigation remand or settlement-enforcement proceeding. The review concludes on the stated threshold and equitable grounds.

PEAVY_PRE

PEAVY_LAW

## Adaptive audit annex and continuity

| Justice | Frozen commitment and individual source basis |
|---|---|
| Stevens | Dismiss as moot without vacatur. His Bancorp join separates termination from judgment treatment; his Bartnicki join supplies no continuing adversity. |
| O'Connor | Same; her Bancorp join distinguishes voluntary settlement from happenstance. |
| Scalia | Same; his Bancorp opinion supplies the controlling jurisdiction/equity distinction. |
| Kennedy | Same; Bancorp controls even though his Bartnicki nonparticipant rule leaves a distinct participant question. |
| Souter | Same; his Bancorp join preserves the voluntarily abandoned judgment without adopting its merits. |
| Thomas | Same; his Bancorp join controls despite his different publication position. |
| Ginsburg | Same; her Bancorp join separates original actions from collateral settlement litigation. |
| Breyer | Same; his Bancorp join precludes continuing a settled dispute merely to clarify constitutional law. |

All eight commitments are unchanged after historical reconciliation. There was no historical Supreme Court decision or Justice lineup on these merits. The official panel's mixed judgment is accurately distinguished from the later global settlement. No historical Supreme Court departure is asserted. The alternative path requires a supported live claim; the validated resolution supplies none. Automatic Munsingwear vacatur fails because the cause is voluntary settlement and the required further equitable reason is absent. No separate writing performs legal work. The only continuity change is termination of this review with the lower judgment undisturbed; no participant-publisher merits rule is created.

__ASSIGNMENT_BLOCK__

Unsigned procedural action; no countable lead, author pool or merits assignment. The internal unanimous grounds do not authorize public poll disclosure.

## Section 15 validation status

Settlement scope, mootness, separate vacatur ground, Stone's applicable branch, dates, sources, internal voting and public disclosure checked. The full holding is identically copied to Public Projection. Section 8 negative-statement review passed for the five governed blocks and their internal counterparts: remaining negatives state the unresolved merits question outside jurisdiction or the surviving judgment and denied vacatur. Conditional merits analysis is excluded from the public account. Final computational/integration checks remain for the root; this draft is not committed.'''
for a,b in [('PEAVY_H',peavy_h),('PEAVY_PRE',peavy_pre),('PEAVY_LAW',peavy_law)]:peavy_internal=peavy_internal.replace(a,b)
write('Peavy v. WFAA-TV, Inc.; 221 F.3d 158; Fifth Circuit No. 99-10272','2003-04-07','Peavy-v-WFAA-TV_procedural-dismissal_2003-04-07.md','Review dismissed as moot; vacatur denied; Fifth Circuit judgment remains undisturbed.',peavy_internal,{
'Event':'''Peavy v. WFAA-TV, Inc., 221 F.3d 158. Dismissal, April 7, 2003. Review of the Fifth Circuit's July 31, 2000 judgment concerned whether a publisher's participation in unlawful interception defeats a First Amendment defense to resulting use or disclosure on matters of public concern. The original Peavy and Oliver actions against WFAA and Riggs were subsequently resolved by settlement.''',
'Participation':'The full Court participates.',
'Public Action':'The review is dismissed as moot. Vacatur is denied. No tally or individual lineup is announced.',
'Judgment & Remedy':'The Fifth Circuit judgment remains undisturbed. The settlement has ended the controversy in this review, which is concluded.',
'Opinion Topology':'The Court issues an unsigned order stating the threshold and equitable grounds for dismissal without vacatur.',
'Holdings':peavy_h,'Precedent Treatment':peavy_pre,'Law After Decision':peavy_law,'Separate Writings':'',
'Procedure After Action':'This review is concluded by dismissal. The existing appellate judgment remains effective.',
'Source Notes':'Peavy v. WFAA-TV, Inc., 221 F.3d 158 (5th Cir. 2000); Jenkens & Gilchrist v. Riggs, 87 S.W.3d 198, 200 (Tex. App. 2002); 28 U.S.C. §2106. The reported aggregate $5 million payment is settlement consideration.'
},{'event':'Procedural dismissal','form':'procedural','countable':False,'assigner':'Stone-Zsela','eligible_authors':[],'full_joiners':ALL,'chief_assigns_any':False,'components':[component('Dismiss review as moot',ALL),component('Deny vacatur and preserve Fifth Circuit judgment',ALL)]})

hason_h = '''### I. Dismissal and the request to retain review

**Holding and operative rule.** The Board's motion to dismiss its writ under Rule 46 is granted, and Hason's request to retain review with an appointed amicus is denied. Dismissal ends this writ and leaves the Ninth Circuit judgment in force; monetary incidents require a separate demonstrated legal and factual basis.

**Authority.** The Court's unsigned order states these procedural grounds. Its tally and individual joins are not disclosed.

**Controlling explanation.** The Court holds that Rule 46 supplies the procedure for ending this review. Under Rule 46.2, an adverse party's objection is confined to damages and costs in this Court or the movant's representation of the petitioners; an unresolved permissible objection comes before the Court for determination. Hason nevertheless asks the Court to retain the live underlying controversy because briefing is complete, a significant split is asserted and the Board has declined settlement. Those circumstances give him no entitlement to compel continued review. His proposal to appoint an amicus, drawing on Dickerson, addresses representation of a legal position; it does not establish a judicial need to refuse this proper dismissal request. The asserted timing and strategy establish no abuse warranting that course. The Court determines the actual monetary demands below, then completes dismissal. The limited immunity question is not reached after withdrawal; the separate substantive licensing question was outside the grant. The disposition rests on voluntary dismissal, not a finding that the underlying controversy is moot.

### II. Rule 46 and ordinary costs

**Holding and operative rule.** Rule 46's provision for damages and costs resolves amounts payable under an applicable legal source; it creates no independent entitlement to reimbursement of all counsel work caused by review. The requested $85,020 in counsel fees and reimbursement of the Court's unquantified brief-printing expense are denied under the asserted Rule 46 and ordinary-costs grounds.

**Authority.** The Court's unsigned order supplies this controlling procedural determination.

**Controlling explanation.** Hason requests $58,400 for 146 hours at $400 and $26,620 for 48.4 hours at $550. Those amounts total $85,020, but expenditure and asserted rates do not themselves establish an obligation of the Board. Rule 46 provides a way to resolve a monetary objection, not a substantive fee entitlement. Rule 43.3 allows Clerk's fees and joint-appendix printing costs but excludes printing expenses for briefs. The request that the Board repay the Court for printing Hason's brief therefore fails as an ordinary taxable cost.

### III. Attorney-specific excess expenses under §1927

**Holding and operative rule.** Section 1927 permits an award against an admitted attorney or other admitted representative who personally and unreasonably and vexatiously multiplies proceedings, limited to the excess costs, expenses and fees reasonably incurred because of that conduct. Seeking review and later withdrawing it on the circumstances shown here establishes neither that misconduct nor the claimed causal excess expense; the request under §1927 is denied.

**Authority.** The Court's unsigned order adopts this source-specific ground.

**Controlling explanation.** The Court holds that the statute's actor, conduct and causation requirements must each be satisfied. It does not automatically place counsel's personal statutory liability on the Board. The timing of withdrawal after opposition and briefing does not by itself show unreasonable and vexatious multiplication, nor establish that all work preparing the opposition, the brief and the objection was excess expense caused by such multiplication. The statute cannot serve as a general respondent-compensation provision merely because a petitioner abandons review. The requested award thus lacks the predicates this asserted source requires.

### IV. Inherent sanction authority

**Holding and operative rule.** A fee sanction under the Court's inherent authority requires bad-faith abuse of the judicial process and the restraint and procedural fairness described in Chambers v. NASCO, Inc. The facts asserted here do not establish that predicate; both counsel-fee compensation and printing reimbursement are denied on this alternative ground.

**Authority.** The Court's unsigned order adopts this distinct sanctions determination.

**Controlling explanation.** Chambers recognizes power to remedy proven abuse; it does not convert an available dismissal procedure into automatic responsibility for an opponent's expenses. Hason points to an unexplained one-sentence withdrawal after briefing, the absence of an announced change of circumstances and possible strategic selection of a better vehicle. Those circumstances do not establish bad faith. Ordinary expense in litigating a properly presented case is not made sanctionable merely because review ends before argument. Because entitlement fails, findings fixing reasonable hours, rates or the amount of printing expense are unnecessary to resolve the requested sanctions.'''

hason_pre = '''U.S. Bancorp Mortgage Co. v. Bonner Mall Partnership, 513 U.S. 18, supplies the distinction between termination of review and disposition of the lower judgment. Its settlement-vacatur holding does not turn this withdrawal into a settlement or an automatic right to vacatur.

Chambers v. NASCO, Inc., 501 U.S. 32, supplies the bad-faith requirement, restraint and procedural fairness for the asserted inherent-authority fee sanction. It remains available for proven abuse; the present showing does not establish that predicate.

Dickerson v. United States, 530 U.S. 428, is distinguished in answering the retention request: representing an unadvanced position with an amicus in a case the Court is deciding does not establish a right or need to continue this withdrawn review.'''
hason_law = '''Rule 46 dismissal, monetary entitlement and treatment of the lower judgment retain their distinct requirements. The dismissal adds no Title II immunity or licensing holding because those questions are not reached. The Ninth Circuit judgment remains operative, and Hason's action may continue in the position that judgment created.'''
hason_internal = '''## Event, chronology, source map and source status

Medical Board of California v. Hason, No. 02-479; judgment below Hason v. Medical Board of California, 279 F.3d 1167, Ninth Circuit No. 00-55784. The circuit judgment of February 12, 2002 reversed sovereign-immunity dismissal; rehearing was denied June 26. The November 18, 2002 grant covered Question 1, immunity, not Question 2, substantive licensing restrictions. The Board moved to dismiss March 3, 2003; federal consent arrived March 4; Hason objected March 6; the scheduled March 25 argument was removed March 7. The present event is April 7, 2003. All participants take part at motion consideration and decision; no argument participation is invented after cancellation.

The frozen C_NEUTRAL and validated Hason source/footnote supplements establish the actual objection. Its ten-page scan was read completely by source control; the page-8 footnote supplies the retention/amicus request omitted from the earlier transcription. It requests counsel compensation of $58,400 plus $26,620, totaling $85,020, and unquantified reimbursement to the Court for printing the respondent's brief. Rule 46, §1927 and inherent power are distinct asserted sources. Hason's description of timing, strategic abuse and lack of changed circumstances is advocacy, not a bad-faith finding. His underlying disability-discrimination allegations remain allegations. The full source search and reading limits are preserved in HASON_SOURCE_FACTS and HASON_FOOTNOTE_SOURCE_FACTS, accepted by SUPPLEMENT_VALIDATED_NEUTRAL. Final C_RECONCILED section 89 controls the eight Associate commitments. Research cutoff: April 7, 2003.

## Participation, entering law and form before assignment

Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participate; no case-specific recusal is identified, quorum is satisfied and five votes suffice. The case calls for an unsigned reasoned procedural dismissal resolving actual incidents, not a signed plenary lead. Form follows the withdrawal posture and asserted remedies, before any count. The public order discloses grounds, not the internal tally or individual joins. This is filing administration under Rule 46, not a covered emergency application requiring separate signed statements.

The applicable Rules 46 and 43.3 are the versions preceding May 2003. Rule 46.2 limits an adverse objection and brings an unresolved permitted objection to the Court; Rule 46.3 permits no mandate or other process absent a Court order. Rule 43.3 excludes brief-printing expense while allowing Clerk's fees and joint-appendix printing. Section 1927 supplies personal admitted-representative liability for unreasonable/vexatious multiplication and caused excess expense. Chambers supplies the inherent-fee bad-faith standard. Bancorp (November 8, 1994) separates ending review from erasure of the judgment. Entering Garrett and Popovich are confined to their actual Title I and bounded Title II access/retaliation holdings; they create no need to reach this withdrawn immunity question. Unrelated April 7 decisions supply no entering rule.

## Approved Stone position, fallback and compatibility

Stone expressly directs Rule 46 dismissal, resolution of an actually supported permissible monetary objection, preservation of the Ninth Circuit judgment and rejection of treating dismissal as a substantive disability or licensing victory. He joins the ordinary withdrawal/judgment distinction and the requirement of a demonstrated monetary legal and factual basis. His core is honored by resolving the actual requested incidents rather than leaving an undefined costs issue open.

His supplement does not expressly choose the independent §1927 or inherent-power grounds, the separate printing-cost theory, or the actual retention-with-amicus request subsequently supplied in full. The standing fallback therefore supplies his votes to deny those otherwise-silent components with the majority and adds no ground. It does not supply a join in those eight-Associate source-specific explanations. His general requirement of demonstrated monetary entitlement does not authorize attributing Chambers' culpability analysis or §1927's actor/causation analysis to him. As to the overall $85,020 fee demand under Rule 46, he joins the source-and-proof requirement and disposition, not an unstated alternative sanction rationale. The affirmative dismissal instruction remains controlling; denying retention is consistent with it. There is no required individual signed statement for this ordinary procedural action and no unsupported Stone separate theory.

## Complete controlling law

HASON_H

## Internal votes, judgment and current law

All nine grant Rule 46 dismissal and preserve the Ninth Circuit judgment. All nine deny the retention/amicus request, the $85,020 fees under Rule 46, the ordinary printing-cost request, the §1927 award and the inherent-power fees/printing sanction. The eight Associates directly join every source-specific ground. Stone's exact direct and fallback-only scope is stated above. These are internal positions; no public tally or join roster is authorized. The Court orders dismissal without damages and costs. No separate mandate or other process is ordered under Rule 46.3. The underlying action continues under the circuit judgment.

HASON_PRE

HASON_LAW

## Adaptive audit annex and continuity

| Justice | Frozen commitment and individual ground |
|---|---|
| Stevens | Grants dismissal and rejects all requested incidents. His Chambers majority join supports power over proven abuse, not automatic compensation; Bancorp preserves the judgment. |
| O'Connor | Same; her Chambers join requires sufficient bad-faith findings and her Bancorp join separates abandonment from judgment erasure. |
| Scalia | Same; his Chambers dissent distinguishes management authority from the bad-faith prerequisite and respects prescribed procedures. His Bancorp opinion supplies the judgment-treatment rule. |
| Kennedy | Same; his Chambers dissent requires a legitimate source, attention to the exact conduct and restraint. Bancorp defeats presumed vacatur. |
| Souter | Same; his Chambers dissent join supports source-specific analysis; Rule 46 and Bancorp permit ending review while litigation continues below. |
| Thomas | Same; Bancorp, §1927's actor/causation text and the existing Chambers rule suffice without choosing immunity merits. |
| Ginsburg | Same; Bancorp separates review from judgment treatment; Rule 46 allows adjudication of an objection but the separate sanction predicates fail. |
| Breyer | Same; Bancorp, orderly withdrawal under Rule 46 and Chambers' abuse requirement reject compelled review and automatic financing of briefing. |

The historical April 7 order dismissed without damages and costs and did not vacate the circuit judgment; it published neither division nor reasons. The final reconciliation preserves that public result without inventing historical votes. Every independent Associate ground remains unchanged. The changed in-world Title II law creates no reason to force withdrawn review. No historical departure is asserted. The retention alternative is rejected on this actual record, not on a universal prohibition of retaining a case. The Rule 46, §1927 and inherent-authority alternatives each fail on their own supported predicates, not on a supposed failure to furnish an unrecovered document. No amount-fixing findings or new hearing are needed once entitlement fails. No separate-writing function remains. Continuity records the procedural termination, unresolved immunity merits and surviving circuit judgment, not a new Title II holding.

__ASSIGNMENT_BLOCK__

Unsigned procedural action; no countable lead or authorship assignment. Grounds receive eight direct Associate joins, with Stone's limited direct agreement and component fallback preserved internally. No public poll is disclosed.

## Section 15 validation status

Chronology, actual requests, controlling pre-May Rules, source-specific monetary grounds, separate retention request, unchanged lower judgment and Stone's vote/rationale distinction reviewed. All requested incidents receive a disposition. Holdings are mechanically identical internally and publicly. Section 8 negative-statement review passed in the five governed blocks and internal counterparts: retained negatives deny actual relief sought, identify genuine nonreach after withdrawal/outside the grant, distinguish surviving judgment status and state the adopted limitations necessary to the monetary rules. Source gaps and research-status caveats remain internal. Final computational/integration checks remain for the root; this draft is not committed.'''
for a,b in [('HASON_H',hason_h),('HASON_PRE',hason_pre),('HASON_LAW',hason_law)]:hason_internal=hason_internal.replace(a,b)
write('Medical Board of California v. Hason; No. 02-479; 279 F.3d 1167 below','2003-04-07','Medical-Board-of-California-v-Hason_procedural-dismissal_2003-04-07.md','Writ dismissed under Rule 46 without damages and costs; retention/amicus and each monetary request denied; Ninth Circuit judgment remains operative.',hason_internal,{
'Event':'''Medical Board of California v. Hason, No. 02-479. Voluntary dismissal, April 7, 2003. On writ of certiorari to the Ninth Circuit, 279 F.3d 1167. The November 18, 2002 grant was limited to sovereign immunity from Hason's Title II licensing suit. The Board moved to dismiss on March 3, the United States consented March 4 and Hason objected March 6. The scheduled March 25 argument was removed from the calendar on March 7. Hason requests retention of review with an amicus, $85,020 in counsel fees and reimbursement of the Court's brief-printing expense.''',
'Participation':'The full Court participates in the motion and its disposition.',
'Public Action':'The motion is granted and the writ dismissed under Rule 46 without damages and costs. The retention/amicus request and each asserted monetary remedy are denied. No tally or individual lineup is announced.',
'Judgment & Remedy':'The Ninth Circuit judgment remains in force. The writ is dismissed without affirmance, reversal or vacatur of that judgment. Hason\'s counsel-fee request and separate printing-reimbursement request are denied on the grounds stated below.',
'Opinion Topology':'The Court issues an unsigned order explaining dismissal and the disposition of the asserted retention and monetary incidents; individual joins are not announced.',
'Holdings':hason_h,'Precedent Treatment':hason_pre,'Law After Decision':hason_law,'Separate Writings':'',
'Procedure After Action':'The writ is terminated. Hason\'s underlying action continues in the posture established by the Ninth Circuit judgment. Under Rule 46.3, no mandate or other process issues absent an order of the Court; this dismissal orders none.',
'Source Notes':'Supreme Court Rules 43.3 and 46 as in force on April 7, 2003; 28 U.S.C. §§1927, 2106; No. 02-479; Hason v. Medical Board of California, 279 F.3d 1167. Hason\'s Objection to Motion to Dismiss (March 6, 2003), including page 8 footnote 1, presents the monetary and retention requests.'
},{'event':'Voluntary dismissal and disposition of objections','form':'procedural','countable':False,'assigner':'Stone-Zsela','eligible_authors':[],'full_joiners':ASSOCIATES,'chief_assigns_any':False,'components':[
component('Grant Rule46 dismissal and preserve circuit judgment',ALL),component('Deny retention and appointed amicus',ALL),component('Deny 85020 counsel fees under Rule46',ALL),component('Deny ordinary brief-printing reimbursement',ALL),component('Deny section1927 award',ALL),component('Deny inherent-power fees and printing sanction',ALL)]})

stout_h = '''### I. Attendance practices remain subject to the enacted impact rule

**Holding and operative rule.** Uniform administration of an attendance practice does not defeat a disparate-impact claim under Title VII concerning pregnancy, childbirth or related medical conditions. A plaintiff must identify the particular practice and prove by a preponderance that it causes disproportionate exclusion of a protected group; the employer then must prove by a preponderance that the practice is job related for the position and consistent with business necessity, and liability may also follow from a proved available less discriminatory alternative serving the employer's legitimate needs that the employer refuses to adopt.

**Authority.** Part I is an opinion of the Court joined by all nine Justices.

**Controlling explanation.** The Court holds that the Pregnancy Discrimination Act's equal-treatment clause operates alongside §703(k), not as an exemption from its impact requirements. Griggs distinguishes a neutral practice from one justified despite its discriminatory effect. Guerra explains why the PDA's comparison language is not an absolute-neutrality ceiling. Watson requires identification of a practice and substantial causal disparity while rejecting a rigid mathematical formula; the enacted §703(k), rather than an earlier formulation of the defense burden, governs the present sequence. Thus regular attendance may be a legitimate employment need without establishing the necessity of this precise three-day total cutoff during ninety days of probation. The claimant must prove comparative causal effect; pregnancy or medical hardship alone supplies no unconditional leave entitlement. Those requirements answer Baxter's concern that impact review necessarily commands preferential leave. Necessity and alternatives determine whether a proved disparity is legally justified.

### II. The medical evidence permits the impact claim to proceed

**Holding and operative rule.** Reliable medical and operational evidence may support a causal comparison without workplace statistics when a particular practice predictably excludes an independently defined protected group. Here the expert evidence that childbirth prevents work for at least two weeks, combined with the automatic three-day cutoff during probation and the supported individual related-condition injury, permits a reasonable inference sufficient to defeat Baxter's existing impact summary judgment.

**Authority.** Part II is an opinion of the Court joined by Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg and Breyer.

**Controlling explanation.** The Court holds that the initial group is employees undergoing childbirth during probation, a condition Congress expressly identifies, rather than everyone selected by failure of the attendance rule. The medical evidence predicts essentially complete exclusion of that group. Otherwise relevant probationary employees not affected by childbirth do not face the same status-linked inevitable absence. That difference permits a comparative inference; it remains open to contrary proof concerning the actual groups and the rule's operation. Reeves requires reasonable inferences for Stout on Baxter's motion, without judicial credibility choices. The lower court accepted the predicted exclusion but rejected the nonstatistical route because it treated equal administration as sufficient for this attendance rule.

The contrary position demands more evidence of actual comparative absence patterns and stresses that Stout experienced miscarriage rather than childbirth. The comparison already rests on an independently defined statutory condition and medically necessary exclusion, not a circular group invented from the rule's failures. Stout's own early-labor and miscarriage absence of more than two weeks is independently documented, rather than inferred solely from the childbirth testimony. Her individual nexus to the proved impact theory and any proposed class's scope still require adjudication. The Court's sufficiency ruling removes the existing summary judgment; it does not resolve the ultimate statutory defenses or expand the childbirth medical proposition to every related condition.

### III. Intentional discrimination and the competing liability motion

**Holding and operative rule.** Baxter's summary judgment on disparate treatment and the denial of Stout's liability cross-motion are affirmed. Each motion must be considered separately with reasonable inferences for its opponent: the record supplies no reasonable inference of intentional discrimination, and the impact evidence does not establish Stout's entitlement to a liability judgment on all required predicates and defenses.

**Authority.** Part III is an opinion of the Court joined by all nine Justices.

**Controlling explanation.** The Court holds that evidence of miscarriage-related absence does not itself establish that sex motivated discharge. The policy's terms and administration treat the reasons for absence alike; there is no supported unequal enforcement, preferential treatment of other absentees or sham physical requirement. Positive performance reviews and perfect attendance during the first two months do not contradict the actual absence-based explanation for the later discharge. Reeves permits a reasonable inference from supported pretext, not an inference from the protected condition alone. Swierkiewicz separates pleading from proof and leaves the Rule 56 evidentiary obligation intact.

The impact claim presents a different question, but defeating Baxter's motion does not satisfy Stout's own motion. Viewing each motion from the required perspective preserves the employer's opportunity to contest the comparison and the remaining statutory predicates and defenses. Denial of her requested liability judgment therefore stands while her impact claim returns for further adjudication.

### IV. The governing remand

**Holding and operative rule.** The Fifth Circuit judgment is vacated only as to Baxter's disparate-impact summary judgment and is otherwise affirmed. On remand the court must apply §703(k)'s causal-impact, job-relatedness, business-necessity and refused-alternative sequence, determine Stout's individual nexus and any class predicates under ordinary procedure, and determine relief if liability is established.

**Authority.** Part IV is an opinion of the Court joined by Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg and Breyer.

**Controlling explanation.** The Court's evidence ruling governs the existing impact motion; the remand is not permission to restore that same judgment solely because the attendance rule was uniformly administered or the supported medical evidence lacked workplace statistics. The parties may contest the inference and the relationship between the defined group, Stout's documented condition and any class properly proposed. Once impact is proved, Baxter must establish the need for this particular practice. A probation extension can be considered if supported as an available, equally effective less discriminatory alternative, rather than assumed to be an established accommodation. Certification, representative adequacy and eventual remedies follow their independent requirements. These are factual, liability and remedial tasks under the settled statutory framework, not reservations about whether pregnancy-related impact claims are legally cognizable.'''

stout_pre = '''Griggs v. Duke Power Co., 401 U.S. 424, applies its distinction between facial neutrality and justified practices with discriminatory impact within the enacted §703(k) sequence.

Watson v. Fort Worth Bank & Trust, 487 U.S. 977, supplies identification of a particular practice, substantial causal comparison and flexibility in the evidentiary form; §703(k) controls the present burden of proving the employer's defense.

California Federal Savings & Loan Association v. Guerra, 479 U.S. 272, supplies the interpretation of the PDA's equal-treatment language as part of Title VII's equal-opportunity protection rather than an absolute-neutrality ceiling.

Reeves v. Sanderson Plumbing Products, Inc., 530 U.S. 133, supplies whole-record evidentiary review, reasonable inferences and the prohibition on credibility choices. Its pretext rule requires an evidentiary basis and does not infer discrimination solely from protected status.

Swierkiewicz v. Sorema N.A., 534 U.S. 506, retains its pleading rule; Rule 56 still requires evidence. Its rejection of an added complaint checklist does not replace the actual proof inquiry here.'''
stout_law = '''Title VII's impact sequence applies to attendance practices affecting pregnancy, childbirth and related medical conditions. Uniform treatment after employees violate a cutoff does not answer the challenge to the cutoff's comparative effects. Medical and operational evidence may establish the necessary comparison without a mandatory statistical format; the particular evidence here permits the claim to continue. The claimant's causal proof, the employer's necessity defense, an available refused alternative, class requirements and relief retain their separate burdens and stages.'''
stout_j = '''| Judgment component | Disposition and vote | Supporting Justices | Opposing Justices | Remedy |
|---|---|---|---|---|
| Baxter's disparate-treatment summary judgment | Affirmed, 9–0 | Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | | Judgment for Baxter stands on intentional discrimination. |
| Baxter's disparate-impact summary judgment | Vacated and remanded, 6–3 | Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg, Breyer | Scalia, Kennedy, Thomas | Impact proceedings under §703(k) and the evidence ruling stated in Holdings. |
| Denial of Stout's liability cross-motion | Affirmed, 9–0 | Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | | The requested liability judgment remains denied. |'''
stout_top = '''__LEAD_AUTHOR__ delivers the opinion of the Court, joined throughout by __LEAD_JOINERS__. Scalia, Kennedy and Thomas join Parts I and III. Stone-Zsela files a concurring opinion. Scalia files an opinion concurring in part and dissenting in part, joined by Kennedy and Thomas.

| Portion | Direct coalition | Scope |
|---|---|---|
| Lead opinion, Parts I and III | All nine Justices | Statutory framework, intentional-discrimination judgment and denial of the liability cross-motion. |
| Lead opinion, Parts II and IV | Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg and Breyer, including the author | Evidence sufficiency and impact vacatur/remand. |
| Stone-Zsela concurrence | Stone-Zsela | Conditional remedial approach following an independently established violation. |
| Scalia separate opinion | Scalia, Kennedy and Thomas | Agrees on common framework and affirmed components; would affirm the impact judgment for insufficient comparative proof. |'''
stout_sep = '''**Scalia, concurring in part and dissenting in part, joined by Kennedy and Thomas.** They accept that §703(k) reaches a properly proved pregnancy-related impact claim, with its enacted necessity and alternative burdens. They would nevertheless affirm Baxter's impact judgment because this record establishes Stout's individual injury and predictable exclusion of childbirth during probation without adequately proving the relevant comparative effect. The lack of an inevitable childbirth absence among other employees does not establish their actual relative ability to meet the total-absence limit, and the broader related-condition claim requires a supported relationship to the childbirth subgroup. They do not demand statistics in every case: reliable medical, operational or statistical evidence could supply the missing comparison. Their ground is proof insufficiency before the employer's defense is triggered, rather than immunity for uniformly enforced attendance policies.

**Stone-Zsela, concurring.** Stone-Zsela joins the Court's evidence and statutory rulings. If a common unlawful cutoff is proved within a properly supported remedial claim, he would presume correction for the persons governed unless Baxter proves a narrower complete cure. That proposed remedial presumption would operate only after certification, individual nexus and liability requirements are independently met. Relief would address causally supported injury, including lawful reinstatement or backpay, and prevent continued use of the proved unlawful cutoff within the appropriate scope. Baxter would first have an opportunity to propose a lawful attendance rule preserving proven job needs. A fitted decree would set a feasible implementation date and require the revised rule, employee notice and actual employment decisions to demonstrate compliance; failure to cure would permit enforcement. He treats a probation extension as a possible evidenced alternative and would permit judgment for Baxter if ordinary procedure ultimately leaves no genuine impact dispute or lawful further development. This conditional remedial approach is his separate position, not an additional holding of the Court.'''

stout_internal = '''## Event, chronology and source map

Stout v. Baxter Healthcare Corp., 282 F.3d 856; Fifth Circuit No. 00-60542, February 19, 2002. The accepted scheduled plenary review on full merits briefing has an assigned decision date of May 19, 2003; no historical Supreme Court docket or argument date is asserted. The Fifth Circuit affirmed Baxter's summary judgments on intentional discrimination and impact and denial of Stout's liability cross-motion. The questions concern the PDA, a uniformly administered attendance cutoff, the actual evidentiary showing and the separate motions.

The lower opinion reports employment beginning May 1998 as a material handler, positive reviews and perfect attendance for two months. Beginning August 14, early labor and miscarriage made Stout unable to work for more than two weeks. She promptly notified her supervisor and furnished a medical excuse one week later. Baxter terminated her August 21 under its maximum three days absent in ninety days of probation, with no medical leave for probationers. The expert testified that childbirth prevents work for at least two weeks; the circuit accepted predicted exclusion of all or substantially all employees giving birth during probation, but rejected its Garcia nonstatistical route for this policy on its PDA/equal-treatment reasoning. It did not find the testimony incredible. Stout's own medical absence is independently supported and does not require extrapolation from the childbirth testimony.

Frozen C_NEUTRAL, STOUT_SOURCE_FACTS, MILLER_STOUT_VALIDATED_NEUTRAL and final C_RECONCILED section 90 supply the source map. The full ten-page official circuit opinion was read by source control and historical reconciliation. The record supplies no workplace comparative statistics, adjudicated class certification or liability findings. These limits are distinguished from the legal sufficiency of a permissible inference. Research cutoff: May 19, 2003. No new facts or Associate commitments enter assembly.

## Participation, entering law and form before counting

All nine participate in plenary consideration and decision: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No nonparticipation is identified. Nine supply quorum; five establish a majority. The actual statutory question, evidentiary disagreement and three judgment components warrant one signed Court lead and the separate writings described below. Form, parts and full-join eligibility were fixed before assignment counts. A single eligible member can carry every Court proposition, so divided authorship is unnecessary.

The entering slice supplies Reeves (June 12, 2000), including the whole-record and actual-pretext rules, and Swierkiewicz (February 26, 2002), preserving Rule 56 evidence despite fair-notice pleading. Title VII §§701(k), 703(a) and 703(k) govern the defined statutory categories, discrimination theories and enacted impact sequence. Griggs, Watson and Guerra are date-eligible background with the exact roles stated below. No later pregnancy-accommodation law enters the decision. The relevant standards are the ordinary summary-judgment reasonable-inference rule and plaintiff's causal preponderance burden, followed by the employer's preponderance defense burden and the available refused-alternative route. The parties' competing motions retain separate perspectives. No FMLA claim is presented.

## Approved Stone position and final compatibility

The approved C_STONE position affirmatively chooses the treatment affirmance, impact vacatur/remand and denial of the liability cross-motion. It rejects an attendance-policy exemption while preserving actual causal proof, necessity, alternatives, individual nexus, certification and remedy predicates. The direct six-Justice sufficiency ruling is consistent with his leading position: the record permits further adjudication under a reliable-medical-evidence rule and does not establish a plaintiff liability judgment. His conditional fallback for a genuinely inadequate comparison is not selected merely because three Associates reject the inference. The independent evidence of his documented miscarriage-related absence strengthens the factual accuracy of the approved inquiry without changing its legal ground. No standing fallback is used.

Stone directly joins all Court portions, including the sufficiency of the actual evidence to defeat the existing defense impact judgment. His additional remedial presumption, employer opportunity, feasible timetable, notice/compliance and enforcement program has no frozen Associate support and remains in a concurrence. Its conditional character, class and causal predicates, and allowance for a lawful narrower complete cure are preserved; it does not govern remand as Court law. His direction not to award immediate policy-wide relief is implemented by the actual remand, not repetitive public disclaimers.

## Complete controlling law

STOUT_H

## Judgment, precedent, current law and next stage

STOUT_J

STOUT_PRE

STOUT_LAW

The impact theory returns to the lower courts for the work stated in Part IV. The intentional-discrimination judgment and denial of the liability cross-motion remain effective. Actual certification, nexus, statutory defenses and relief are ordinary adjudicative tasks under the rule, not unresolved law or already adjudicated liability.

## Opinion topology and published noncontrolling continuity

STOUT_TOP

STOUT_SEP

The Scalia/Kennedy/Thomas comparison objection and Stone's conditional remedial proposal remain noncontrolling published positions for later modeling. The Court adopts direct majorities without a Marks inquiry. Six direct rationale supporters join the whole lead; all nine join Parts I and III.

## Adaptive audit annex

| Justice | Frozen result, individual source basis and join test |
|---|---|
| Stevens | Vacates impact judgment; affirms treatment and denial of Stout's motion. Guerra concurrence, Watson concurrence and Reeves support equal opportunity and reliable nonstatistical inference. Full lead join; no medical-fact-only liability or compulsory statistical formula. |
| O'Connor | Same; her Watson opinion requires a practice and causal comparison without a rigid mathematical formula, and her Guerra/Reeves joins support this predictable exclusion. Full lead join with identified statutory group and real causal comparison, not presumed unlawfulness of every absence limit. |
| Scalia | Affirms all lower results on insufficient comparative proof for impact. Watson, Guerra, Reeves and Swierkiewicz support proof before a triggered statutory defense. Joins I/III and writes the evidence dissent; no categorical attendance immunity or superseded defense allocation. |
| Kennedy | Same bounded impact affirmance; his Wards Cove position informs proper comparisons while enacted §703(k) controls the defense. Reeves/Swierkiewicz preserve proof distinct from inference. Joins I/III and Scalia's separate opinion. |
| Souter | Vacates impact judgment; affirms other components. Reeves/Swierkiewicz, Griggs and enacted §703(k) support inference from predictable exclusion of an independently defined group. Full lead join with separate individual and class nexus work. |
| Thomas | Affirms impact on comparative insufficiency; common statutory allocation accepted. Reeves/Swierkiewicz and Watson preserve actual proof. Joins I/III and Scalia, without an attendance exemption. |
| Ginsburg | Vacates impact; childbirth is an independently specified statutory category, with an inevitable absence absent in unaffected comparators. Reeves/Swierkiewicz and Guerra support its evidentiary significance. Full lead join; individual/class relationship remains for adjudication, without generalizing childbirth recovery to every miscarriage. |
| Breyer | Vacates impact; reliable medical comparison supplies a rebuttable reasonable inference, and statutory defenses avoid automatic leave. Reeves/Swierkiewicz, Griggs, Watson and Guerra supply the grounds. Full lead join while permitting challenge and actual necessity proof. |

Historical reconciliation: there was no historical Supreme Court merits vote. Garwood's circuit opinion for Jolly and DeMoss, read in full, affirmed on the legal treatment of the accepted evidence. Five Associates reject that assessment; three affirm on a different bounded comparative-proof ground rather than endorsing an exemption. No historical Supreme Court departure is asserted. The supporting majority answers the strongest objection by identifying childbirth independently of the policy and explaining its predicted exclusion, while preserving Stout's distinct injury and nexus. The dissent answers the strongest counterargument by distinguishing predicted subgroup exclusion from a sufficient relevant comparison. These are frozen legal choices, not new facts or revised votes. The same approved proof rule does not become a guaranteed accommodation or mandatory discovery program.

__ASSIGNMENT_BLOCK__

Stone is in every judgment majority and assigns. Eligible full-lead authors and full direct joiners: Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg and Breyer. The Court's opinion does not include Stone's separate conditional remedial program. Authorship awaits the root's serial recount. Scalia's separate opinion functions as the precise comparative-proof dissent, joined by Kennedy and Thomas; that author choice does not count as a lead assignment.

## Section 15 validation status

All three motion dispositions, exact causal comparison, individual miscarriage evidence, statutory burden sequence, class/remedy stages, Stone compatibility, Associate joins and source cutoffs reviewed. The complete internal holdings are copied unchanged into Public Projection. Section 8 negative-statement review passed in the five governed blocks and counterparts: retained negatives answer the attendance-immunity and automatic-leave arguments, deny the actual liability request, preserve the affirmed judgments and state adopted limits needed to distinguish the evidence ruling from conclusive proof. Bare disclaimers about unrequested remedies and hypothetical unpresented applications are omitted. No liability or class certification is inferred. Final computational and assignment/integration checks remain for the root; this draft is not committed.'''
for a,b in [('STOUT_H',stout_h),('STOUT_J',stout_j),('STOUT_PRE',stout_pre),('STOUT_LAW',stout_law),('STOUT_TOP',stout_top),('STOUT_SEP',stout_sep)]:stout_internal=stout_internal.replace(a,b)
write('Stout v. Baxter Healthcare Corp.; 282 F.3d 856; Fifth Circuit No. 00-60542','2003-05-19','Stout-v-Baxter-Healthcare-Corp_merits_2003-05-19.md','Treatment summary judgment and denial of plaintiff liability motion affirmed; employer impact summary judgment vacated and remanded.',stout_internal,{
'Event':'''Stout v. Baxter Healthcare Corp., 282 F.3d 856. Decision on plenary review, May 19, 2003. Review of the Fifth Circuit's February 19, 2002 judgment concerns whether the Pregnancy Discrimination Act permits disparate-impact review of a uniformly administered probationary attendance rule and whether this evidence permits the claim to proceed. The circuit affirmed Baxter's summary judgments on disparate treatment and impact and denial of Stout's liability cross-motion. Baxter discharged Stout after documented early-labor and miscarriage-related absence exceeded its three-day limit during ninety days of probation. The record includes expert evidence that childbirth prevents work for at least two weeks.''',
'Participation':'Stone-Zsela, Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participate.',
'Public Action':'The judgment is affirmed in part, vacated in part and remanded.',
'Judgment & Remedy':stout_j,'Opinion Topology':stout_top,'Holdings':stout_h,'Precedent Treatment':stout_pre,'Law After Decision':stout_law,'Separate Writings':stout_sep,
'Procedure After Action':'The disparate-impact claim returns for proceedings under Holdings, Part IV. The intentional-discrimination judgment for Baxter and denial of Stout\'s liability cross-motion remain effective. Ordinary certification, individual nexus, liability and relief determinations proceed at their respective stages.',
'Source Notes':'Title VII §§701(k), 703(a), 703(k), 42 U.S.C. §§2000e(k), 2000e-2(a), 2000e-2(k); Federal Rule of Civil Procedure 56; Stout v. Baxter Healthcare Corp., 282 F.3d 856 (5th Cir. 2002), No. 00-60542. The summary-judgment record independently documents Stout\'s medical inability to work for more than two weeks; the expert\'s separate proposition concerns childbirth.'
},{'event':'Merits decision','form':'signed plenary','assigner':'Stone-Zsela','eligible_authors':['Stone-Zsela','Stevens',"O'Connor",'Souter','Ginsburg','Breyer'],'full_joiners':['Stone-Zsela','Stevens',"O'Connor",'Souter','Ginsburg','Breyer'],'chief_assigns_any':True,'components':[component('Affirm Baxter treatment summary judgment',ALL),component('Vacate Baxter impact summary judgment and remand',['Stone-Zsela','Stevens',"O'Connor",'Souter','Ginsburg','Breyer']),component('Affirm denial of Stout liability crossmotion',ALL)]})

(OUT/'C_specs.json').write_text(json.dumps(specs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Created four group C drafts and C_specs.json.')


