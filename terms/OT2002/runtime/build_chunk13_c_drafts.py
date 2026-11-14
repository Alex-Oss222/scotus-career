from pathlib import Path
import json, re

TERM = Path(__file__).resolve().parents[1]
OUT = TERM / 'runtime/chunk13-drafts'
OUT.mkdir(exist_ok=True)

def section(path, number):
    text = path.read_text(encoding='utf-8-sig')
    match = re.search(rf'(?m)^## {number}\. .*', text)
    end = re.search(r'(?m)^## (?:\d+\.|Completion controls)', text[match.end():])
    return text[match.start():match.end() + end.start() if end else len(text)].strip()

def write_record(file, case, docket, date, result, kernel, holds, blocks, number):
    annex = section(TERM/'freeze/OT_2002CHUNK13_C_RECONCILED.md', number)
    record = f'''**Case and dockets:** {case}, No. {docket}.
**Event and date:** Merits decision; {date}; October Term 2002.
**Result:** {result}
**Version / lineage:** Original decision.

{kernel.strip()}

## Controlling holdings

{holds.strip()}

## Adaptive audit annex — frozen Associate positions and reconciliation

The following bounded reconciliation is mechanically carried from the authoritative frozen handoff. Its Justice-specific grounds and refusal limits remain unchanged by assembly. The final public tables below distinguish judgment votes from opinion joins; there is no inferred join or reconstructed private circulation.

{annex}

## Sources and validation status

The legal and connected-event research cutoff is immediately before {date}. The neutral facts and source limitations are established by `freeze/OT_2002CHUNK13_C_NEUTRAL.md` and `freeze/OT_2002CHUNK13_C_CLEAN_PREFLIGHT.md`; the quoted reconciliation records the exact source review completed. The dated authorities are in `entering-law/OT_2002CHUNK13_C.md`, `entering-law/OT_2002CHUNK13_C_PRIOR_PUBLIC.md`, and `entering-law/OT_2002CHUNK13_C_CURRENT_PUBLIC.md`. The objective argument dates come from the verified syllabus metadata recorded in the frozen reconciliation. Historical sources establish the stated facts and comparator, not post-divergence Court law. No reconstruction premise or litigant default is used.

Assembly preserves all frozen Associate commitments. The draft's proposition and judgment arithmetic, partial joins, source boundaries, and eleven-block Public Projection are checked. Each ordinary controlling explanation is within 350 words. The five-block negative-statement check retains only an adopted substantive limit, a preserved lower disposition, a requested remedy withheld, or a genuine question outside the granted scope. Authorship, chronology refresh, final integration checks, publication and commitment remain pending at this draft stage. __PUBLICATION_STATUS__

## Public Projection

'''
    for name, text in blocks:
        record += f'## {name}\n\n{text.strip()}\n\n'
    (OUT/file).write_text(record.rstrip()+'\n', encoding='utf-8')

sell_holds = '''### I. Immediate appeal protects the refusal interest before medication

**Holding and operative rule:** A conclusive order authorizing involuntary antipsychotic medication over objection to restore trial competence is immediately appealable under 28 U.S.C. §1291 when it resolves the important bodily-liberty question separate from guilt and final-judgment review cannot undo the authorized intervention. The appellant must establish these category-based requirements; personal hardship alone does not suffice.

**Authority:** Part I of the Court's opinion, supported by Stone, Stevens, Kennedy, Souter, Ginsburg and Breyer; six participating Justices adopt the same rule and application.

**Controlling explanation:** The Court holds that this order falls within the narrow collateral-order category. Cohen and Coopers & Lybrand require a conclusive decision of an important, separate question that cannot effectively await final judgment. Digital Equipment applies those requirements cumulatively to categories of orders, rather than the hardship of an individual appeal. This order finally permits an intrusion into Sell's body before guilt is adjudicated. A new trial after conviction could correct a trial error but could not restore his opportunity to refuse the medication. The criminal final-judgment rule remains demanding; the decisive distinction is the final authorization of this protected bodily intervention, rather than an ordinary ruling about evidence or trial management. The possibility of an independently available civil action does not make final review of this criminal authorization effective.

### II. Prosecution alone can justify medication only on an individualized showing protecting a fair trial

**Holding and operative rule:** The Government may medicate an objecting, incompetent defendant solely to permit trial of serious nonviolent criminal charges, including serious property offenses, only if it establishes an important interest in this prosecution; a regimen substantially likely to restore competence and substantially unlikely to impair significantly effective assistance to counsel or the fairness of the defense; necessity after reasonable less intrusive treatments and methods of administration are considered; and medical appropriateness for this defendant. The court must assess defense effects before treatment and reassess actual effects before trial.

**Authority:** Part II of the Court's opinion; Stevens, Kennedy, Souter, Ginsburg and Breyer adopt the complete rule. These five direct joins establish controlling authority.

**Controlling explanation:** Riggins protects refusal by requiring overriding need, medical appropriateness and consideration of less intrusive means. Weston requires advance assessment of defense effects where restoration is an actual purpose without an independently sufficient safety justification. The Court now resolves the prosecution-only question those decisions left open. Prosecution of serious nonviolent charges can supply the necessary interest, but the court must assess its actual weight, including detention already endured and the realistic consequences of possible further civil confinement. Further confinement can reduce that interest without automatically eliminating it.

Restoration must serve a fair adjudication. A regimen that produces minimal competence while materially impairing comprehension, consultation, testimony, reactions or presentation fails that purpose. Available clinical evidence, alternatives and workable safeguards must support the advance determination; prediction need not be perfect. Reasonable less intrusive treatments must be unlikely to achieve substantially the same legitimate result, and reasonably available less intrusive administration methods must also be considered. The treatment must be in the defendant's medical interest in light of his condition. Courts retain the legal decision, informed by clinical evidence.

Ordinarily the court should determine whether the Government seeks, or has sought, treatment on an independently supported danger or medical ground and, if not, why not. Such a ground may avoid the prosecution-only inquiry, and its rejection may clarify that inquiry. Harper governs its own danger-and-treatment justification; the sequence neither assumes danger nor compels pursuit of an unavailable ground. Against the categorical objection that prosecution can never suffice, the protected refusal interest permits a demonstrated overriding need meeting every condition just stated. Diagnosis, clinical benefit and serious charges alone do not establish that showing.

### III. The asserted freedom-of-thought interest does not categorically bar justified restoration

**Holding and operative rule:** The First Amendment does not categorically prohibit medically appropriate restoration treatment satisfying all the prosecution-only protections stated above. Cognitive risks must receive their full weight in the necessity, medical-appropriateness and fair-defense inquiries; a therapeutic label does not establish constitutionality.

**Authority:** Part III of the Court's opinion; Stevens, Kennedy, Souter, Ginsburg and Breyer adopt this narrow rejection of the categorical First Amendment objection.

**Controlling explanation:** Stanley protects freedom of thought and Barnette protects against compelled orthodoxy. Restoring the capacity to think and communicate under the full protections of Part II is not, merely because treatment alters mental functioning, governmental imposition of belief. Sell's concerns about changes in cognition and expression require the concrete clinical and defense-effects assessment already demanded, rather than an irrebuttable prohibition on every qualifying restoration treatment. This answer resolves the categorical First Amendment claim presented.

### IV. The present authorization fails the required prosecution-specific inquiry

**Holding and operative rule:** A prosecution-only medication order must connect the proposed treatment to a fair prosecution through advance findings about defense effects and the actual governmental interest. The present authorization fails that requirement and is vacated; a renewed request may proceed on current circumstances under Parts II and III or on a separately established lawful treatment basis.

**Authority:** Part IV of the Court's opinion; Stevens, Kennedy, Souter, Ginsburg and Breyer adopt this ground and renewed-request direction. Stone also supports vacatur, but on the distinct categorical ground described in his separate opinion.

**Controlling explanation:** The existing clinical evidence and findings are considered at their actual scope. The defect is the inadequate connection between treatment and a fair prosecution, including an advance assessment of effects on the defense and the actual prosecutorial interest after Sell's confinement. Weston requires that inquiry before intervention; appellate reassurance and a promise of later review cannot supply it. The District Court's rejection of dangerousness leaves the present prosecution rationale to stand on its own. On remand, a renewed request must establish the applicable conditions through a current determination. The present orders authorize no involuntary administration. Lawful continued custody remains subject to its separate statutory authority and review.'''

sell_topology = '''__LEAD_AUTHOR__ delivers the opinion of the Court. __LEAD_JOINERS__ join it in full; Stone joins Part I. Kennedy files a concurring opinion. Stone files an opinion concurring in part and dissenting in part. Scalia files a dissenting opinion, joined by O'Connor and Thomas.

| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | __LEAD_AUTHOR__ | __LEAD_JOINERS__; Stone as to Part I | Immediate review; vacatur; remand permitting a sufficiently supported renewed request | Parts I–IV for the full joiners; Part I only for Stone |
| Concurrence | Kennedy | Kennedy alone | Joins the Court's opinion and judgment | Stronger ultimate assurance against significant defense impairment |
| Concurrence in part and dissent in part | Stone | Stone alone | Joins immediate review and vacatur; would prohibit prosecution-only renewal | Part I joined; distinct treatment-authority and replacement-order grounds |
| Dissent | Scalia | O'Connor and Thomas | Would vacate the appellate judgment and direct dismissal of the interlocutory appeal | Jurisdiction only; no merits adjudication |'''

sell_separates = '''**Kennedy, concurring.** Kennedy joins the complete rule but emphasizes the stronger ultimate protection he explained in Riggins and Weston: restoration requires an extraordinary showing against significant impairment of the defendant's reactions, participation and assistance to counsel. A nominal finding of competence does not establish the ability to defend fairly. His formulation concerns the assurance necessary in application; it does not prescribe a universal clear-and-convincing burden or demand perfect clinical prediction.

**Stone, concurring in part and dissenting in part.** Stone agrees that review must precede this irreversible intervention and that the present authorization must be vacated. He would hold that prosecution of the covered nonviolent charges cannot itself supply authority to medicate an objecting, nondangerous defendant. Under his reading of the substantive liberty protected by Riggins and Weston, the Government must establish an independent emergency, safety or patient-welfare basis under that authority's own substantive and procedural requirements. Trial incompetence is distinct from incapacity to refuse treatment, present danger and lawful treatment authority. Harper supplies a different source of authority; Benson's record-based denial of a new-trial writ does not resolve this prospective question.

Stone would prohibit renewal on prosecution alone. A lawful replacement order would have to identify its genuinely independent basis, provide the required process and consider reasonable less intrusive means; relabeling restoration as welfare would be insufficient. If restoration remained an actual purpose of a nonemergency replacement order, he would additionally require advance judicial assessment of foreseeable effects on comprehension, consultation, testimony, demeanor and defense presentation, supported by clinical evidence, alternatives and safeguards, and renewed assessment before trial. He proposes that protection even when an independent safety basis suffices, extending rather than restating Weston's held scope. His substantive liberty ground makes a separate First Amendment answer unnecessary. The proposal covers the nonviolent prosecution category before the Court; materially different violent-offense applications fall outside the limited grant.

**Scalia, joined by O'Connor and Thomas, dissenting.** The dissent applies the strict criminal final-judgment rule and Cohen's cumulative requirements. In its view, protection of bodily liberty does not create an additional interlocutory category in the criminal case when trial unfairness can be reviewed after conviction and a properly founded independent civil challenge remains distinct. Riggins and Weston's advance trial-court duties do not decide appellate jurisdiction. The dissent would vacate the Eighth Circuit judgment and direct dismissal of the appeal, without deciding whether this regimen satisfies the Constitution.'''

sell_precedent = '''- Cohen v. Beneficial Industrial Loan Corp., 337 U.S. 541, and Coopers & Lybrand v. Livesay, 437 U.S. 463: applied to each cumulative collateral-order requirement; the narrow method remains controlling.
- Digital Equipment Corp. v. Desktop Direct, Inc., June 6, 1994: its category-based importance and effective-unreviewability requirements govern; the bodily intervention differs from the private settlement rights there adequately protected after judgment.
- Riggins v. Nevada, May 18, 1992: its refusal, necessity, alternatives and supported defense-risk protections remain in force; the present decision answers the prosecution-only sufficiency question it left open.
- United States v. Weston, April 17, 2001: its advance and pretrial defense-effects requirements apply; its reserved prosecution-only question is resolved through the conditions in Part II.
- Washington v. Harper, 494 U.S. 210: its independent danger-and-treatment authority remains distinct and must be established on its own predicates.
- Benson v. Terhune, May 27, 2003: its collateral-review ruling leaves capacity, treatment choice and defense effects distinct and supplies no prosecution-only authorization.
- Stanley v. Georgia, 394 U.S. 557, and West Virginia State Board of Education v. Barnette, 319 U.S. 624: their protections against control of thought and compelled orthodoxy are preserved and distinguished from the fully justified restoration category.'''

sell_kernel = '''## Event, participation and entering law

Sell v. United States, No. 02-5664; argued March 3, 2003; decided June 16, 2003. Certiorari to the Eighth Circuit's affirmance of the District Court's involuntary-medication order. The grant concerns prosecution-only antipsychotic medication to restore competence for trial of nonviolent charges under the First, Fifth and Sixth Amendments; §1291 appealability is a necessary antecedent. Sell seeks reversal; the United States seeks lawful restoration and prosecution. The District Court rejected the alternative dangerousness finding. Serious mental illness, incompetence, the treatment proceedings and confinement are the supported record predicates; no new clinical finding is supplied.

Stone, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participate at argument and decision. Nine participate, supplying a quorum; five votes are required for a controlling proposition. The review channel is plenary certiorari review of the interlocutory appellate judgment. The lower medication authorization is set aside and the matter returns for proceedings on a current supported request. Relevant entering law is Cohen, Coopers & Lybrand, Digital Equipment, Riggins, Harper, Weston and Benson. Weston and Riggins leave ultimate prosecution-only sufficiency open; Benson does not close that question. No post-June-16 authority enters.

## Stone fixed core and compatibility

The authorized source is `runtime/OT_2002CHUNK13_C_STONE.md`, Sell Section II. Stone's fixed core requires immediate review, invalidation of the prosecution-only order, vacatur and remand forbidding renewal solely for these nonviolent prosecutions. He requires genuine independent treatment authority and proposes advance defense-effects protection for a nonemergency replacement order pursuing restoration even where independent safety authority suffices. Custody remains separate. His liberty ground is sufficient and does not adopt the Court's First Amendment holding. No conditional branch or standing fallback is used; no substance is narrowed or supplemented.

Compatibility yields a join to Part I only. Agreement with vacatur is not a join to Parts II–IV: Stone rejects their affirmative prosecution-only authority and renewal direction. His separate writing preserves that legal disagreement, the proposed replacement-order safeguard, and the limited grant. His directions against unrequested relief are honored in the mandate without a public catalogue. His transition proposal is noncontrolling and does not backdate a new rule into Benson.

## Form, assignment and final joins

A signed opinion after argument states four genuine legal parts: immediate review; the qualified treatment-authority rule and sequence; the distinct First Amendment answer; and the present-order application and remand. This form is fixed independently of opinion counts. Every full-join Associate supports all four parts. Stone joins only Part I. Kennedy's stronger explanation performs separate legal work without withdrawing his full join. The jurisdictional dissent addresses no merits component.

__ASSIGNMENT_BLOCK__

The judgment and opinion tables in the Public Projection are the final assembly tables. Threshold support is six to three. Five approve the full conditional-authority and renewal direction; Stone supports setting aside the present authorization but rejects that renewal scope. O'Connor, Scalia and Thomas seek jurisdictional vacatur, which is not counted as a merits vacatur vote. No logical-subset construction or Marks aggregation is necessary: five direct joins support every merits proposition.

## Continuity and law change

The decision adds a narrow immediately appealable medication-order category, resolves the reserved prosecution-only question through a complete qualified rule, and rejects the presented categorical First Amendment objection. Existing refusal, alternatives and advance defense-effect protections continue. The clinical and current-interest work on renewal is factual application under settled rules. The public separate-writing summaries below are also the complete material noncontrolling continuity entries: Kennedy's stronger assurance, Stone's independent-authority limit and replacement-order extension, and the three dissenters' criminal-finality position. None changes controlling law. There is no roster, allotment or standing-practice change, and no admitted external consequence or invented follow-up event. The matter is at remand, not an uncompleted Supreme Court merits event.'''

sell_blocks = [
('Event','Sell v. United States, No. 02-5664. Argued March 3, 2003; decided June 16, 2003. On writ of certiorari to the United States Court of Appeals for the Eighth Circuit. The Court reviews compulsory antipsychotic medication solely to restore competence for trial of nonviolent offenses under the First, Fifth and Sixth Amendments, and the antecedent question of immediate appellate jurisdiction. The Eighth Circuit sustained the treatment authorization after the District Court rejected dangerousness as an alternative basis.'),
('Participation','Stone, Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated at argument and decision.'),
('Public Action','The Court accepts immediate review, vacates the judgment sustaining the present medication authorization, and remands for further proceedings under the requirements stated in its opinion.'),
('Judgment & Remedy','''| Judgment component | Disposition and vote | Supporting Justices | Opposing Justices | Remedy or remand |
|---|---|---|---|---|
| Immediate appellate review | Jurisdiction sustained, 6–3 | Stone, Stevens, Kennedy, Souter, Ginsburg, Breyer | O'Connor, Scalia, Thomas | Reach the preserved constitutional questions |
| Present treatment authorization | Vacatur and merits remand, six supporting vacatur on different grounds | Stone, Stevens, Kennedy, Souter, Ginsburg, Breyer | O'Connor, Scalia, Thomas oppose the merits adjudication | The present orders provide no authority for involuntary medication |
| Scope of merits remand | Renewed prosecution-only request permitted upon the complete required showing, five votes | Stevens, Kennedy, Souter, Ginsburg, Breyer | Stone would prohibit prosecution-only renewal; O'Connor, Scalia and Thomas do not reach the merits | Return through the Eighth Circuit for proceedings under Parts II–IV |

The jurisdictional dissenters would instead vacate the appellate judgment and direct dismissal of the interlocutory appeal. Their proposed vacatur does not join the Court's merits remedy.'''),
('Opinion Topology',sell_topology),('Holdings',sell_holds),('Precedent Treatment',sell_precedent),
('Law After Decision','Conclusive orders authorizing the covered forced medication receive immediate collateral-order review. Prosecution of serious nonviolent charges may justify restoration medication only through the complete individualized interest, efficacy, fair-defense, necessity and medical-appropriateness showing. Advance assessment and pretrial reassessment remain operative requirements. The categorical First Amendment objection fails within that fully protected category. These rules govern the present order and subsequent covered requests from this decision; the clinical findings needed on renewal are applications of settled law.'),
('Separate Writings',sell_separates),
('Procedure After Action','The judgment is vacated and the case remanded through the Eighth Circuit. Officials may not administer involuntary medication under the vacated authorization. A renewed request must establish the complete prosecution-only showing on current circumstances or a genuinely supported independent treatment basis under its own law. The court must ordinarily address any asserted alternative basis first, assess anticipated defense effects where the stated restoration rule applies, and reassess actual effects before trial. Continued custody requires its separate statutory authority and review.'),
('Source Notes','28 U.S.C. §1291; 18 U.S.C. §§4241–4246; U.S. Const., Amends. I, V, VI. Sell v. United States, No. 02-5664; United States v. Sell, 282 F.3d 560. Petitioner\'s merits brief, pp. 24–25, 28–32, and United States merits brief, pp. 36–38, present the competing freedom-of-thought arguments. The dangerousness finding was rejected below; a replacement finding must rest on a lawful current determination.')]

sell_file='Sell-v-United-States_merits_2003-06-16.md'
write_record(sell_file,'Sell v. United States','02-5664','2003-06-16','Immediate review sustained, 6–3; present medication authorization vacated; five Justices permit a supported renewed prosecution-only request, while Stone would bar that ground.',sell_kernel,sell_holds,sell_blocks,158)

specs=[{'file':sell_file,'case':'Sell v. United States','date':'2003-06-16','countable':True,'assigner':'Stone','eligible_authors':['Stevens','Kennedy','Souter','Ginsburg','Breyer'],'full_joiners':['Stevens','Kennedy','Souter','Ginsburg','Breyer'],'assignment_authority_text':'The Chief joins the six-Justice judgment setting aside the present authorization and remanding, and assigns the lead opinion. His disagreement with the five-Justice renewed-request instruction excludes him from whole-opinion authorship and is preserved in the exact partial joins.'}]
(OUT/'C_specs.json').write_text(json.dumps(specs,indent=2)+'\n',encoding='utf-8')
print('Sell draft and initial C_specs.json written.')
