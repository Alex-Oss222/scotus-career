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
COMMON='''All nine members—Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer—participate at submission or argument and decision. No nonparticipation is established. Six constitute the statutory quorum; all nine participate, and five votes are necessary for judgment and for a controlling proposition. No petition poll is part of this merits assembly.

The source and stage boundaries are the frozen B neutral packet, entering-law B/B_SUPPLEMENT, B reconciled commitments and scoped B Stone input, with their identified objective sources. The original independent and reconciliation freezes remain untouched. This is the disclosed cross-context fallback; it claims no pristine isolation. Historical review occurred before current Stone input. The full-reading and arithmetic receipts are `freeze/OT_1995CHUNK1_B_RECONCILIATION_FULL_READING_RECEIPT.json` and `freeze/OT_1995CHUNK1_B_RECONCILIATION_CHECK_RECEIPT.json`.

Wood (October 10), Doe (October 16) and Hodge (October 23) were read in their bounded public entering-law copies. Their Brady, school-supervision/immunity and retained-record immunity/mootness holdings do not change the grounds used here. No Tuggle adjudication is treated as effective law. Drafts of other current matters are not authority. Root preservation and the event-specific chronological refresh remain required before this draft becomes a Record.
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
 data.update({'record_filename':filename,'record':filename,'case':case,'date':date,'disposition_summary':result,'disposition':result,'participants':J,'blockers':[]})
 (OUT/filename.replace('.md','.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

LIB_H='''### Agreement permits waiver but cannot enlarge the forfeiture statute

A defendant may knowingly and voluntarily relinquish the forfeiture jury protection and admit facts supporting forfeiture. Consent does not authorize punishment beyond §853: an admission may establish a statutory predicate, but an agreement cannot replace a predicate the statute requires or transfer an interest outside the defendant's lawful power of disposition.

**Authority:** O'Connor's Part I-B, joined by all eight other Justices, controls unanimously on these common propositions; the distinct application grounds and constitutional reservation appear below.

**Controlling explanation:** Section853(a)(1) reaches property constituting or derived from proceeds obtained directly or indirectly from the violation. Paragraph(a)(2) reaches the defendant's property used or intended to be used, in any manner or part, to commit or facilitate it. For a continuing criminal enterprise, paragraph(a)(3) also reaches his interests in or claims against the enterprise and his property or contractual rights affording a source of control over it. Lawful acquisition alone therefore does not establish immunity.

Substitute property under §853(p) is different. The defendant's act or omission must have made qualifying property unavailable through inability to locate it despite due diligence; transfer, sale or deposit with a third party; placement beyond the court's jurisdiction; substantial diminution in value; or commingling that cannot be divided without difficulty. Other property may then be taken only up to the value of that qualifying property. Section853(d)'s rebuttable presumption requires the Government to prove by a preponderance both acquisition during the violation or within a reasonable time afterward and the absence of a likely source other than the covered violation. An all-assets promise alone proves neither condition.

Godinez distinguishes capacity from actual knowing and voluntary choice; Olano distinguishes intentional relinquishment from forfeiture by inaction. The limited waiver recognized in Mezzanatto does not dispense with understanding or authorize an unlawful sentence. The Court does not find every asset independently eligible, invalidate every asset, or infer private counsel's advice. The defendant's plea and agreement operate within the statute, and third-party rights retain their separate protection.

**Precedent treatment:** Godinez and Olano supply the capacity/choice and relinquishment/inaction distinctions. Mezzanatto's limited consent principle is applied without expanding its impeachment holding into unlimited sentencing authority.

### Former Rule11(f) does not require a separate forfeiture factual-basis inquiry

Former Rule11(f) requires a factual basis for the guilty plea to the substantive offense; it does not independently require a guilt-style factual-basis inquiry into the extent of criminal forfeiture imposed as part of the sentence under §§848 and853. This rule-specific conclusion does not permit a court to exceed those statutes or require acceptance of a defective agreement.

**Authority:** O'Connor's Part I-A, joined by Stevens, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer, controls by eight votes. Stone-Zsela concurs in affirmance on his separately stated statutory-record and informed-waiver grounds, without adopting an additional Rule11(f) rationale.

**Controlling explanation:** Rule11(f)'s inquiry protects the guilty plea to the offense. The separate notice and special-verdict requirements of Rules7(c)(2) and31(e) address criminal forfeiture without converting each property interest into an element of continuing-criminal-enterprise guilt. Libretti pleaded guilty to that offense, and the challenged determination fixes property included in its statutory sentence. The existence of forfeiture safeguards does not change the words or subject of Rule11(f).

That distinction answers the argument that every stipulated asset required a new plea-style factual inquiry. It does not erase the difference between procedural inquiry and lawful punishment. The sentencing court still operates under §853; a factual admission and existing evidence may supply its predicates, while consent cannot supply a power Congress withheld. Whether an independent duty apart from Rule11(f) requires a particular further inquiry is addressed only to the limited extent necessary below. No new Rule32.2 procedure or later amendment is applied.

**Precedent treatment:** The plea and waiver precedents retain their defined roles; this holding construes the then-applicable Rules11,7 and31 rather than enlarging their text through an analogy to guilt elements.

### The particular forfeiture determination is not an offense-element jury question

Under the §§848 and853 scheme at issue, the determination of the extent of forfeiture following conviction is a sentencing determination, not an element of continuing-criminal-enterprise guilt requiring a Sixth Amendment jury determination. The holding concerns this statutory determination; it does not announce that every fact affecting punishment lies outside the jury guarantee.

**Authority:** O'Connor's Part II-A, joined by Scalia, Kennedy, Thomas and Breyer, controls by five votes. Stone-Zsela, Stevens, Souter and Ginsburg leave the constitutional source of the forfeiture jury protection unresolved.

**Controlling explanation:** Gaudin requires the jury to decide each enacted criminal element, including materiality, but does not classify these property interests as elements of the substantive CCE offense. Congress separately provided a forfeiture special verdict under Rule31(e). The distinction between conviction and punishment recognized in McMillan, Cabana and Spaziano permits the particular statutory sentencing determination here without converting it into a new guilt element.

Austin's treatment of punitive civil forfeiture under the Excessive Fines Clause and Alexander's treatment of criminal forfeiture as punishment establish the bounded propositions those cases decide. Punitive character does not by itself transfer every procedural guarantee applicable to adjudication of guilt. The Court neither decides an Excessive Fines claim nor limits Gaudin's protection of actual offense elements. The four Justices reserving the constitutional issue do not vote to recognize a constitutional forfeiture jury right; their separate grounds make its source unnecessary to their dispositions.

**Precedent treatment:** Gaudin remains fully effective for enacted offense elements and is distinguished as to this sentencing determination. McMillan, Cabana and Spaziano supply the date-eligible guilt/punishment distinction. Austin and Alexander are applied only at their punitive-forfeiture scope.

### The affirmative agreement and courtroom assent waive the statutory special verdict

Libretti's represented agreement to forfeit his identified interests, signed jury waiver and express courtroom assent to ending the trial and proceeding to sentence waive the Rule31(e) special verdict on this record. Former Rule11(c) does not require an additional forfeiture-specific advisement, and Rule23(a) does not require a new forfeiture-specific written waiver for this statutory sentencing verdict.

**Authority:** O'Connor's Part II-B, joined by Scalia, Kennedy, Thomas and Breyer, controls by five votes. Stone-Zsela, Souter and Ginsburg also uphold the waiver on informed-relinquishment grounds, but do not join this part's broader sufficient-waiver formulation. Stevens does not independently resolve the waiver application because his statutory remand ground disposes of his vote.

**Controlling explanation:** Libretti did more than remain silent or enter an unexplained plea. He signed the represented agreement, expressly accepted it in court, and was told the trial would end and sentencing would follow. The agreement's actual admissions and scope matter; competence alone and a signature alone do not establish knowing surrender of every sentencing issue. Earlier trial references to the forfeiture verdict reinforce the record without requiring an assumption about private advice from counsel.

Godinez permits a competent defendant's choice but preserves the separate requirement that it be knowing and voluntary. Olano distinguishes that choice from an unpreserved objection. Mezzanatto does not make every plea a waiver of every protection. A judge may explain the special verdict expressly and must not affirmatively mislead the defendant or leave evident confusion uncorrected. Supported challenges to coercion, voluntariness, understanding or agreement scope remain distinct. The absence of a new rule-specific warning at this plea hearing therefore does not require the proposed remand; neither the right's statutory source nor practical convenience alone supplies the waiver.

**Precedent treatment:** Godinez, Olano and the limited Mezzanatto holding are applied to affirmative, represented assent. Their protections against unsupported or involuntary waiver remain intact.

### This record does not require the demanded wholesale new factual-basis proceeding

The trial evidence, sentencing materials, agreement referring to §853 and the judge's response to Libretti's preserved objection provide a case-specific basis for rejecting the demanded new forfeiture factual-basis proceeding. The Court leaves the precise extent of any independent duty outside Rule11(f) open and makes no new asset-by-asset adjudication under §853(a) or(p).

**Authority:** O'Connor's Part III, joined by Kennedy, Souter, Ginsburg and Breyer, controls by five votes. Scalia and Thomas do not join this additional policy and record appraisal. Stone-Zsela concurs on his stated record-limited statutory ground; Stevens would require independent assurance of the order's lawful scope on remand.

**Controlling explanation:** The judge heard trial evidence, received sentencing materials, considered an agreement expressly tied to §853, acknowledged the statute's limits and answered Libretti's personal factual-basis objection by referring to evidence already heard. The decision therefore did not rest solely on an unexplained promise to surrender everything. The court of appeals' broad view of what agreement could authorize is not adopted as a source of statutory power.

The later April2 order contains actual adverse findings and third-party return orders. In the Wyochem/Porter discussion, it found the Government had not carried the stated substitute-property burden and left tracing or other claims for further hearing. It ordered return of the ring and the parents' funds and interest in the childhood accounts. The defendant-specific reopening was ineffective after his appeal; that jurisdictional limit did not erase the court's separate §853(n) jurisdiction or all its third-party findings.

The expressly designated $8,416.23 General Chemical distribution check in December paragraphNN is distinct from the Columbia IRA in paragraphQ and Porter's $1,333.45 claim. An express substitute-property designation is not proof of every §853(p) predicate. The appellate caveat for an employer pension or profit-sharing interest made inalienable by law, or a valid spendthrift trust created by another, is conditional; it does not establish that the distributed check or IRA had that status. These distinctions defeat neither statutory limits nor the bounded procedural affirmance. The Court orders no automatic property return, new hearing for every asset or reopening of valid third-party relief.

**Precedent treatment:** The lawful-authority limit is preserved alongside the narrow procedural holding; the Court does not adopt a consent-created forfeiture power or decide the full independent-duty question urged in dissent.'''

lib_separate='''**Stone-Zsela, concurring in the judgment and joining Part I-B.** The Chief Justice upholds Libretti's informed relinquishment of a forfeiture jury and leaves the right's constitutional source unresolved. A sentencing label alone cannot answer the constitutional question, and the actual waiver makes an answer unnecessary. Gaudin remains the rule for enacted elements; this disposition neither expands nor displaces it.

Section853 fixes the court's power to take property. Actual admissions and existing evidence can establish that basis without another hearing for every item, but a promise to forfeit cannot authorize an otherwise forbidden sentence. Lawful source alone is not immunity where the property is an instrumentality, an enterprise interest or authorized substitute property. The existing orders, admissions and evidence support rejecting a wholesale new proceeding on the reviewed claims; those claims do not establish an identified, still-operative defendant-owned portion requiring vacatur. That is not a finding that every §853(p) predicate was proved for every item or an endorsement of forfeiture by agreement alone. A demonstrated statutory defect in an identified portion would require its vacatur and lawful separation or further treatment; no prior final invalidity judgment would be necessary. The April adverse findings, effective third-party returns and defendant-specific postappeal jurisdiction limit retain their exact scope. The check, IRA and Porter claim remain distinct, and no conditional pension exclusion is applied without its predicate. Supported portions, the guilty plea and conviction are preserved.

**Souter, concurring in part and in the judgment.** Justice Souter joins Parts I-A, I-B and III. He agrees that the right must be understood before it can be surrendered and resolves the case without deciding its constitutional source. Ordinary jury advice, understood with an indictment's forfeiture allegation, can cover the charged forfeiture question without reciting a rule number. Advice affirmatively suggesting that the jury right excludes forfeiture would present a different problem. The two earlier references to the jury's forfeiture function answer the possible misleading implication of the later guilt-focused explanation here; represented assent and the express end of trial then establish surrender. Godinez and Olano preserve that actual-choice requirement. He does not join the five's constitutional classification or broader sufficient-waiver formulation, require an automatic additional hearing, or infer private advice absent from the record.

**Ginsburg, concurring in part and in the judgment.** Justice Ginsburg joins Parts I-A, I-B and III. She requires awareness of the unusual forfeiture special-verdict right, and relies on the pretrial references to that jury function followed by Libretti's represented agreement and express assent to ending trial. A bare reading of a forfeiture allegation or broad signature need not suffice in another case. An explicit plea-hearing explanation is a readily available protection, but the omission of that additional warning does not require remand when the record otherwise establishes informed relinquishment. The limited Mezzanatto consent principle supports attention to the protection actually surrendered. She leaves the constitutional source unresolved and withholds the broader formulation in Part II; she neither finds a constitutional jury right nor equates statutory classification with knowing waiver.

**Stevens, dissenting, while joining Parts I-A and I-B.** Justice Stevens agrees that Rule11(f) does not impose the requested forfeiture inquiry and that a known jury right may be surrendered. His dissent instead requires the sentencing court independently to assure itself that its punishment stays within §853 where the record raises a concrete question about the forfeiture order's breadth. Bigelow and Ex parte Lange distinguish punishment exceeding statutory power from an arguably erroneous exercise of lawful power; Roberts illustrates why agreement alone cannot make an item forfeitable. A broad all-assets bargain cannot purchase authority Congress withheld.

The record supports portions of the order and expressly designates a substitute check. Those facts do not by themselves establish the basis for every additional interest embraced by the appellate all-assets rationale. The April court's affirmative adverse findings and its attempted defendant-specific further inquiry reinforce the distinction between assent and authority, even though the defendant's pending appeal defeated that reopening. Stevens would vacate the defendant's forfeiture disposition and remand for the statutory assurance he finds missing. He does not declare the check, IRA, Wyochem balance or every asset invalid, erase third-party orders or require automatic return. He leaves the constitutional question unresolved and does not premise remand on a finding of ignorance despite the jury notices. The remand would not automatically rescind guilt or preserve every benefit of a sentence-contingent bargain: if the court rejected an agreement governed by former Rule11(e)(1)(C), Rule11(e)(4)'s opportunity to withdraw would apply. That condition is not established merely by the existence of this forfeiture agreement.'''

lib_blocks={
'Event':'''**Libretti v. United States, No.94-7427 — November7, 1995.** Argued October3, 1995. On writ of certiorari to the Tenth Circuit, 38 F.3d523. After several days of trial, Libretti pleaded guilty to engaging in a continuing criminal enterprise and agreed to criminal forfeiture. Review concerns the factual-basis requirement, forfeiture jury protection and waiver, and the statutory bounds of the property order.''',
'Participation':NAMES+'. All nine participate.',
'Public Action':'The Court affirms the Tenth Circuit on the questions reviewed. It rejects the requested wholesale new forfeiture proceeding while preserving the statutory and third-party limits described below.',
'Judgment & Remedy':'''**Affirmed, 8–1.** Supporting: Stone-Zsela, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. Opposing: Stevens, who would vacate the defendant's forfeiture disposition and remand for independent assurance of statutory authority.

The guilty plea and conviction remain intact. The Court neither enlarges §853 nor independently declares every asset forfeitable. Effective third-party relief is not undone. No Excessive Fines claim, automatic return, new asset-by-asset hearing or independent reopening of the defendant's order is decided or directed.''',
'Opinion Topology':'''| Writing / portion | Author | Joined by | Scope and status |
|---|---|---|---|
| Opinion of the Court, Part I-A | O'Connor | Stevens, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | Eight votes: Rule11(f)'s limited subject. Stone-Zsela concurs in judgment without adding this rationale. |
| Opinion of the Court, Part I-B | O'Connor | Stone-Zsela, Stevens, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | Nine votes: informed waivability and consent bounded by statutory authority. |
| Opinion of the Court, Parts II-A and II-B | O'Connor | Scalia, Kennedy, Thomas, Breyer | Five votes: this forfeiture's constitutional classification and affirmative-agreement waiver application. |
| Opinion of the Court, Part III | O'Connor | Kennedy, Souter, Ginsburg, Breyer | Five votes: bounded appraisal rejecting a wholesale new factual-basis proceeding; precise independent-duty scope reserved. |
| Concurrence in judgment, joining Part I-B | Stone-Zsela | — | Informed waiver without constitutional classification; record-limited statutory authority and conditional remedy for an identified unsupported portion. |
| Concurrence in part and judgment | Souter | — | Joins I-A, I-B and III; actual understanding, ordinary advice and prior notices; constitutional question reserved. |
| Concurrence in part and judgment | Ginsburg | — | Joins I-A, I-B and III; awareness supplied by prior notices and later assent; constitutional question reserved. |
| Dissent, joining I-A and I-B | Stevens | — | Statutory-assurance remand; no independent waiver-defect holding or identified-asset invalidity finding. |

Each controlling part has an actual majority. The distinct concurrence grounds need not be combined into a new controlling rationale. Agreement in judgment does not add a join to Part II or III.''',
'Holdings':LIB_H,
'Precedent Treatment':'''- **Godinez v. Moran:** Applied to distinguish competence from actual knowing and voluntary waiver; no automatic hearing is added.
- **United States v. Olano:** Applied to intentional relinquishment, distinct from failure to preserve; Libretti's factual-basis objection is not erased.
- **United States v. Mezzanatto:** Its limited consent principle informs actual waiver; its impeachment holding is not expanded into unlimited sentencing authority.
- **United States v. Gaudin:** Remains controlling for enacted offense elements; the five-Justice Part II-A distinguishes the particular statutory forfeiture determination.
- **McMillan v. Pennsylvania; Cabana v. Bullock; Spaziano v. Florida:** Supply Part II-A's date-eligible distinction between adjudication of guilt and punishment, without a universal rule for every sentence-affecting fact.
- **Austin v. United States; Alexander v. United States:** Retain their bounded punitive-forfeiture holdings; punitive character alone does not import every guilt-trial safeguard.
- **Bigelow v. Forrest; Ex parte Lange; United States v. Roberts:** Stevens invokes their lawful-punishment limits to require additional statutory assurance. His demanded remand is not the Court's holding.''',
'Law After Decision':'''Former Rule11(f) imposes no independent factual-basis inquiry into this criminal forfeiture sentence. Five Justices classify the particular property-extent determination as sentencing rather than a Sixth Amendment offense-element question and uphold the statutory special-verdict waiver on the affirmative agreement and courtroom assent. The constitutional reservation of four Justices does not displace that majority holding. A separate five-Justice ground rejects a wholesale new proceeding on the existing record while reserving the precise independent-duty question. Knowing waiver remains distinct from competence or silence, and consent cannot enlarge §853. No general asset eligibility, pension-plan status or displacement of third-party relief is established.''',
'Separate Writings':lib_separate,
'Procedure After Action':'''The affirmed judgment returns through the ordinary appellate process. This mandate orders no new hearing or property return. Section853(n) remains the separate avenue for a person other than the defendant asserting a qualifying legal interest: a petition must be filed within thirty days of final publication or receipt of notice, whichever is earlier; relief requires the statutory superior or vested interest, or bona fide purchase for value without reasonable cause to believe the property subject to forfeiture. It is not a postjudgment reconsideration route for the defendant. The existing April third-party dispositions and their lawful further proceedings are not vacated by this decision.''',
'Source Notes':'''The [record and briefs, No.94-7427](https://archive.org/details/micro_IA40385013_0616), particularly the plea agreement, December order at JA155–164, April order at JA298–312 and appellate opinion at JA313–329, supply the property, objection and jurisdictional facts. The Columbia IRA is paragraphQ at JA158; the General Chemical distribution check is paragraphNN at JA162. The appellate pension/spendthrift caveat at JA326 n.8 is conditional, not a finding about those assets. The [primary judicial report](https://www.govinfo.gov/content/pkg/USREPORTS-516/pdf/USREPORTS-516-29.pdf) reports the pretrial exchange at 1 Tr.8 and the voir-dire notice at 1 Tr.188. Those underlying transcript pages are not separately reproduced here; the decision does not infer private advice or additional transcript findings. The then-applicable rules and statute govern, without later forfeiture-rule amendments.'''}

lib_internal='''## Event, channel and entering law

Research cutoff: 1995-11-07. Argument on October 3 and decision on November 7 are verified by the official report and inventory. Certiorari reviews the Tenth Circuit's judgment at 38 F.3d 523. After several days of his multicount trial, Libretti entered the represented October 5, 1992 agreement and pleaded guilty under §848. His personal factual-basis objection was raised at sentencing; the Court does not turn it into an unpreserved claim. The December order and the April 2, 1993 third-party/reconsideration order must be distinguished. The appellate review did not decide an unpressed Excessive Fines claim.

'''+COMMON+'''
The exact entering Standards are **Jury determination of criminal materiality** (Gaudin, June 19, 1995); **Capacity to plead or waive counsel and independent valid waiver** (Godinez, June 24, 1993); **Punitive forfeiture and Excessive Fines review** (Austin/Alexander, June 28, 1993); and **Advance plea-statement waivers for impeachment** (Mezzanatto, January 18, 1995). Olano retains its waiver/forfeiture distinction. These authorities do not decide that every punishment-related fact is a guilt element, that every competent choice is informed, or that assent can enlarge §853. Wood, Doe and Hodge supply no changed predicate. Root must refresh actual effective October 31 decisions before canonical preservation; no pending B or C draft is treated as law.

## Fixed Stone core and assembly compatibility

Stone rejects the challenge to informed forfeiture-jury waiver, reserves its constitutional source and preserves guilt. He affirms supported forfeiture and requires vacatur of any identified unsupported portion, without a blanket new asset hearing. His statutory limit applies even to lawfully acquired property: an instrumentality, enterprise interest or statutory substitute may still qualify, but the actual predicate must be present. This core is fixed.

The independently reviewed assembly memorandum `freeze/OT_1995CHUNK1_LIBRETTI_STONE_PROPERTY_COMPATIBILITY.md` supports bounded affirmance. It does not establish a specified still-operative defendant-owned portion to which Stone's conditional vacatur must now apply. A prior final invalidity judgment is not a prerequisite; a demonstrated appellate statutory defect could trigger his remedy. None is established for an identified remaining own interest on the questions reviewed. That conclusion is source- and claim-limited, not universal proof of eligibility, absence of adverse findings, or an invented future collateral remedy.

He joins Part I-B's common informed-waiver and statutory-authority propositions. His expressed affirmance is sufficient to resolve the Rule11(f) challenge in judgment without a new categorical Rule11(f) reason attributed to him; no standing fallback is used to invent a rationale or override his conditional remedy. He withholds Parts II-A and II-B because constitutional nonreach and actual informed relinquishment, rather than the five's classification and broader formulation, are his grounds. He does not join Part III's reserved independent-duty analysis, stating his actual supported-order and conditional-vacatur ground separately. These are proposition-specific joins, not an inferred nine-Justice opinion from eight votes to affirm.

## Objective property and jurisdiction controls

The validated fuller-record supplement, its independent no-change effect review, the validated notice supplement and its independently refreshed commitments are cumulative with the original B freeze. Their exact paths are `freeze/OT_1995CHUNK1_LIBRETTI_NEUTRAL_SUPPLEMENT.md`, `freeze/OT_1995CHUNK1_LIBRETTI_INDEPENDENT_SUPPLEMENT_EFFECT.md`, `freeze/OT_1995CHUNK1_LIBRETTI_NOTICE_NEUTRAL_SUPPLEMENT.md` and `freeze/OT_1995CHUNK1_LIBRETTI_NOTICE_REFRESH_COMMITMENTS.md`. They preserve original bytes, accept the positive April findings and both reported jury notices, and precede historical reconciliation. No absence-of-findings or whole-record no-notice premise survives.

| Source / item | Positive evidence and precise legal limit |
|---|---|
| April order, JA303 n.1 and surrounding Wyochem/Porter discussion | Government failed the stated substitute-property showing; the source/tracing questions were reserved. This adverse finding is retained. It does not expressly amend every other item or paragraphNN. |
| Porter's $1,333.45 interest | Separate third-party claim with unresolved tracing/proportion; not the General Chemical retirement distribution check. |
| Ring and childhood bank accounts, JA306,308,310 | Actual return orders followed legitimate-source/ownership findings. The ring finding used innocent-owner terminology; that wording does not replace §853(n)'s statutory criteria. The parents' funds and interest were ordered returned. Execution of those orders is not independently proved here. |
| Defendant-specific reopening, JA309–312; appellate JA318–319 | Pending appeal deprived the district court of jurisdiction over defendant reconsideration. The then-Rule35(c) timing/scope did not authorize it. Distinct §853(n) third-party jurisdiction remained; the whole April order is not nullified. |
| December paragraphNN, JA162 | $8,416.23 General Chemical distribution check expressly designated substitute for dissipated/expended assets. Designation supplies the stated route, not independent proof of every §853(p) condition. No identified operative defect in this item is established by the reviewed claims. |
| December paragraphQ, JA158 | Columbia IRA is a separate item; neither its name nor a general pension caveat establishes statutory inalienability. |
| Appellate JA326 n.8 | Conditional exclusion for an employer pension/profit-sharing interest made inalienable by law, or a valid spendthrift trust created by another; not an applied holding that this check or IRA qualifies. |
| Star Valley and father's securities | Reserved tracing/claim questions and denied claims keep their separate dispositions; no blanket asset order is inferred from either. |

The complete joint appendix was read across the source phases; it is not the complete trial transcript. The merits petitioner/government briefs and reply were read in full; the certiorari opposition/reply were independently read for notice authentication. The notice source is the official judicial report, not direct reading of 1 Tr.8/188. Source receipts state these different levels. Party theories about drug proceeds, values and agreements are not converted into asset findings. The statutory predicate list in the public holding is complete at the relied-on scope; its recital does not announce new findings for all property.

## Non-Stone reconciliation, join test and assignment

The frozen reconciliation supplies the eight individual grounds and the reason each surviving historical premise remains persuasive. The independent Steele-free model was not repaired after comparator access. The source handoffs and clean refreshes preceded the reconciliation; assembly adds no Associate theory or changed asset finding.

'''+rows('## Libretti v.','## American Life League')+'''

| Portion | Actual joins after Stone enters | Withheld assent and resolution |
|---|---|---|
| I-A: Rule11(f) | O'Connor, Stevens, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | Stone's judgment agrees; no unsupported categorical rule rationale attributed. |
| I-B: common informed waivability and statutory limits | All nine | No objection displaced; application and constitutional disagreements remain explicit. |
| II-A/II-B: classification and broader waiver application | O'Connor, Scalia, Kennedy, Thomas, Breyer | Stone, Souter and Ginsburg require nonreach/actual-awareness grounds; Stevens resolves disposition on statutory assurance. No revision purports to gain their joins. |
| III: policy and aggregate record appraisal | O'Connor, Kennedy, Souter, Ginsburg, Breyer | Scalia/Thomas retain their refusal of the additional discussion without invented explanation. Stone uses his distinct statutory conditional remedy. Stevens requires further assurance. |
| Judgment | Stone, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer affirm; Stevens vacates/remands | Eight to one, with no independent asset-invalidity finding or new waiver inquiry imposed. |

No material non-Stone historical departure remains. Souter's original inquiry/remand becomes informed-waiver affirmance after comparison with his treatment of the same notices; Ginsburg's independent constitutional classification becomes nonreach in light of her same-record actual-awareness rationale. Stevens's vacatur rests on the statutory-authority ground that survives full source review, not a no-notice premise. These changes were made and frozen before Stone exposure; the assembly does not reopen them. No Marks combination is asserted because each controlling part has five or more actual joins.

The Chief is in the eight-Justice affirmance majority and assigns the Court opinion to O'Connor. Her date-eligible Godinez/Olano and limited Mezzanatto positions fit the distinction between capacity, represented actual assent, statutory procedure and preserved legal limits. Stone is the strongest alternative on bounded statutory authority and informed waiver, but his express constitutional reservation prevents him from carrying the five-Justice Part II-A rationale as his own. O'Connor can state both actual majorities and their distinct joins. The prior-term review has no concentration trigger; the actual previously acknowledged assignments are Wood/O'Connor, Doe/Ginsburg and Hodge/O'Connor. Root will add actual intervening assignments when preserving this later event. Historical authorship supplies no reason for assignment. Separate writings are selected for their substantive grounds, with no unsupported joins or fictional circulation dialogue.

## Source map and remaining limits

Primary source addenda: `sources/B_LIBRETTI_FULLER_RECORD_ADDENDUM.md`, `sources/B_LIBRETTI_FULLER_READ_RECEIPT.json`, `sources/B_LIBRETTI_PRETRIAL_NOTICE_OBJECTIVE_EXTRACT.md` and `sources/B_LIBRETTI_REMEDIAL_REQUESTS.md`, together with the B factual/source handoff and both clean supplements. The entire official reported decision and all separate writings/footnotes were read in reconciliation; incomplete Cornell opening paragraphs were cured from the official report and visual checks. That review did not supply an unvalidated asset finding. The October 31 actual-law refresh is a preservation step for root; no present source or fixed-Stone conflict blocks this bounded draft.
'''

# Prose spacing is clerical only; do not touch the first two B drafts owned by root.
import re
def space_prose(t):
 t=re.sub(r'\b(Rule|Rules|Part|Parts|paragraph|JA|October|November|April|December|Section)(?=[0-9A-Z])',r'\1 ',t)
 t=re.sub(r'§(?=\d)','§ ',t)
 t=re.sub(r'\b(No\.)(?=\d)',r'\1 ',t)
 t=t.replace('and853','and 853').replace('and31','and 31').replace('or(p)','or (p)').replace('Paragraph(a)','Paragraph (a)').replace('paragraph(a)','paragraph (a)')
 return t
lib_blocks={k:space_prose(v) for k,v in lib_blocks.items()}
lib_internal=space_prose(lib_internal).replace('Steele-free model','Stone-free model')
lib_blocks['Holdings']=space_prose(LIB_H)
affirm=[x for x in J if x!='Stevens']
rule_names=A
five_class=["O'Connor",'Scalia','Kennedy','Thomas','Breyer']
five_record=["O'Connor",'Kennedy','Souter','Ginsburg','Breyer']
write_record('Libretti_v_United_States_merits_1995-11-07.md','Libretti v. United States, No. 94-7427','1995-11-07','Affirm the Tenth Circuit on the questions reviewed, 8–1; no new forfeiture proceeding ordered.',lib_internal,lib_blocks,{
 'judgments':[{'component':'reviewed forfeiture judgment','disposition':'affirm','support':affirm,'oppose':['Stevens'],'printed_tally':'8–1','other_positions':[]}],
 'writings':[{'author':"O'Connor",'joiners':[x for x in rule_names if x!="O'Connor"],'scope':'Part I-A','controlling':True},
 {'author':"O'Connor",'joiners':[x for x in J if x!="O'Connor"],'scope':'Part I-B','controlling':True},
 {'author':"O'Connor",'joiners':[x for x in five_class if x!="O'Connor"],'scope':'Parts II-A and II-B','controlling':True},
 {'author':"O'Connor",'joiners':[x for x in five_record if x!="O'Connor"],'scope':'Part III','controlling':True},
 {'author':'Stone-Zsela','joiners':[],'scope':'concurrence in judgment; joins I-B','controlling':False},
 {'author':'Souter','joiners':[],'scope':'concurrence in part and judgment; joins I-A, I-B, III','controlling':False},
 {'author':'Ginsburg','joiners':[],'scope':'concurrence in part and judgment; joins I-A, I-B, III','controlling':False},
 {'author':'Stevens','joiners':[],'scope':'dissent; joins I-A and I-B','controlling':False}],
 'law_summary':lib_blocks['Law After Decision'],
 'published_positions':[s.strip() for s in lib_blocks['Separate Writings'].split('\n\n**') if s.strip()],
 'next_stage':lib_blocks['Procedure After Action'],
 'assignment':{'assigner':'Stone-Zsela','author':"O'Connor",'chief_assignment':True}})

