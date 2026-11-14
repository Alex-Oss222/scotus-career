from pathlib import Path
import json

TERM=Path(__file__).resolve().parents[1]
OUT=TERM/'runtime/chunk13-drafts'
source=(TERM/'runtime/build_chunk13_c_drafts.py').read_text(encoding='utf-8')
exec(source[:source.index('sell_holds =')])

grutter_holds='''### I. The actual Law School program satisfies the common substantial-justification standard

**Holding and operative rule:** A public university may consider race in admissions when it establishes an important lawful educational objective, a substantial evidence-supported relationship between its actual racial treatment and that objective, justified coverage and competitive burdens, and a supported response to concrete practicable alternatives comparably advancing the objective with materially less racial disadvantage. The Law School satisfies that standard on this record through its supported educational benefits, actual individual comparisons, meaningful nonracial considerations and genuine competition; academic expertise is evidence, not an exemption from the University's burden.

**Authority:** Part I of the Court's opinion; Stone, Stevens, O'Connor, Souter, Ginsburg and Breyer adopt the complete rule and application. Their six direct joins establish controlling force.

**Controlling explanation:** Adarand requires proof of the actual objective, relationship and burdens. Hopwood already recognizes supported educational diversity as important and requires genuine individual competition. Bakke supplies the competitive-consideration boundary. The evidence supports educational interaction, reduced isolation and correction of stereotyped expectations. The policy examines academic and other individual contributions throughout the applicant pool. Actual variation and meaningful nonracial considerations support the conclusion that race informs a competitive assessment rather than fixes an entitlement to a place.

The opposing evidence deserves weight: substantial admissions differentials and attention to enrollment can reveal a racial allocation concealed by flexible language. Kennedy, Scalia and Thomas find that objection decisive on their respective grounds. The Court assesses the full record, rather than treating comparisons limited to measured credentials as a complete description of applicants. Supported individual comparisons and varied outcomes answer the objection here. Neither monitoring enrollment nor the phrase critical mass by itself establishes genuine competition or a forbidden fixed share. Race does not determine an applicant's viewpoint, and the permission does not protect a hidden racial allocation.

The express racial classification triggers the inquiry without proof of exclusive hostility. Montiel preserves independent constitutional injuries and distinct statutory elements; its apportionment setting supplies no admissions safe harbor. Patrolmen's likewise requires the government's evidence-supported justification despite an operational benefit. The Court applies that same common rule independently while respecting supported trial findings. It approves the actual program because the evidence sustains its operation, rather than because individualized language or an institution's good faith shifts the burden to the challenger.

### II. Alternatives and continued operation require continuing factual justification

**Holding and operative rule:** The University must answer concrete practicable alternatives that comparably advance its supported educational objectives with materially less racial disadvantage; it need not exhaust every conceivable method or abandon legitimate educational selection for a materially different objective. Permission to continue racial consideration lasts only while the actual educational relationship, competitive burdens and response to effective alternatives remain justified.

**Authority:** Part II; the same six-Justice coalition adopts this application and continuing condition.

**Controlling explanation:** Adarand supplies the alternatives requirement, and Hopwood identifies the supported educational objective against which feasibility and comparable effect must be judged. Outreach, socioeconomic consideration, different credential weighting, percentage approaches and lottery proposals must be assessed in that setting. The Law School's national pool and legitimate individual-selection aims matter to comparability; an undergraduate percentage plan is not automatically an equivalent substitute. The actual evidence supports the conclusion that the proposed alternatives would not comparably achieve the demonstrated educational interaction while preserving legitimate selection practices. Prestige for its own sake would not justify racial treatment. The duty is to respond to supported practical alternatives, not to perform a ritual exhaustion of every imagined plan. Continuing justification supplies an endpoint: when changed conditions, effective alternatives or actual burdens defeat that showing, the permission ends.

### III. Title VI permits the justified competitive consideration established here

**Holding and operative rule:** Title VI §601's equality guarantee permits the genuinely competitive educational consideration established by this supported substantive justification. The presented intentional-treatment claim therefore fails, while §601's intent requirement and the statute's own coverage, proper-defendant and remedy predicates retain their distinct operation.

**Authority:** Part III; Stone, Stevens, O'Connor, Souter, Ginsburg and Breyer separately adopt this statutory construction and disposition.

**Controlling explanation:** The policy intentionally considers race. Hopwood prevents treating an educational purpose or good faith as absence of statutory intent. The independent statutory answer concerns whether that purposeful treatment denies the equality §601 protects. Bakke's competitive-consideration proposition, preserved and developed in Hopwood, permits genuinely competitive consideration within a substantively justified educational process rather than requiring a categorical prohibition of every racial consideration. The Law School's program satisfies that guarantee at the admitted scope. The conclusion does not arise merely by renaming the constitutional result; it rests on the statute's equality protection and the program's actual competitive operation. Sandoval preserves §601's intentional-treatment requirement.

### IV. Section 1981 protects equal educational-contract opportunity under the justified-competition construction

**Holding and operative rule:** Section 1981 permits a substantively justified educational consideration of race that preserves genuine competition and neither imposes racial ineligibility nor assigns a separate racial entitlement to the educational contract. The actual Law School program satisfies that same-right guarantee, so the presented §1981 policy challenge fails independently of the constitutional and Title VI dispositions.

**Authority:** Part IV; the same six Justices adopt this independent statutory construction and application.

**Controlling explanation:** Runyon establishes educational-contract coverage; McDonald protects applicants of every race; General Building Contractors supplies the relationship between purposeful discrimination and the constitutional equality guarantee. That relationship alone does not make every constitutionally permitted classification lawful under every statute. The Court construes §1981's same-right protection here as equal competitive access to educational contracting, informed by the preserved Bakke–Hopwood competition principle. The evidence establishes genuine competition within a substantively justified process, rather than racial exclusion or a separate contractual entitlement.

The contrary textual argument treats every purposeful racial preference as necessarily denying the same contract right. Scalia and Thomas accept that broader view; Kennedy finds the actual operation inadequate even under the justified-competition construction. The Court rejects the categorical reading in this setting because the supported competitive process supplies the equality the statute protects. Academic freedom does not excuse a statutory exclusion: Runyon's rejection of an associational defense to exclusion remains intact. Section 1983 supplies an authorized enforcement route, not a different admissions standard; source-specific defendants, causes and relief remain distinct. The requested relief resting on these resolved policy-violation theories is therefore denied.'''

grutter_topology='''__LEAD_AUTHOR__ delivers the opinion of the Court, joined by __LEAD_JOINERS__. Kennedy files a dissenting opinion. Thomas files a dissenting opinion, Part I of which Scalia joins.

| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | __LEAD_AUTHOR__ | __LEAD_JOINERS__ | Affirm the Sixth Circuit's judgment sustaining the policy | Parts I–IV in full |
| Dissent | Kennedy | Kennedy alone | Reverse and remand for policy and surviving individual relief | Actual-operation objection under the governing standard; statutory invalidity at that scope |
| Dissent | Thomas | Scalia as to Part I | Reverse and remand | Part I: broader nonremedial-preference objection and actual-mechanism objection; Part II: Thomas's distinct selective-prestige objection |'''

grutter_separates='''**Kennedy, dissenting.** Kennedy accepts the existing availability of a supported educational-diversity objective but finds inadequate proof that the actual racial weight and numerical management preserve genuinely individual competition throughout selection. Hopwood's individual-comparison requirement and Patrolmen's evidence-supported fit rule demand more than academic assurance or flexible language. Statistics alone need not establish a quota, yet the whole operational record in his assessment fails the common justification standard. He would reverse on that narrower actual-operation ground and sustain the intentional-treatment statutory challenges at the same scope, without deciding a categorical prohibition of all supported educational consideration. On remand, policy relief and individual claims would remain distinct; Hopwood and Lesage would place the preponderance same-decision burden on the school, with claimants establishing actual loss under an available cause against a proper defendant.

**Thomas, dissenting, with Scalia joining Part I.** Part I maintains the broader personal-equality objection to nonremedial ancestry preferences, together with the conclusion that this mechanism fails genuine competitive treatment. Their earlier Adarand and Hopwood separate positions supply that objection to the governing permission; they do not treat the separate position as existing Court law. They also read §1981's same-right guarantee to prohibit the purposeful preference and would sustain the Title VI challenge. Their proposed reversal would require fitted policy relief and separate adjudication of individual causation and remedies, rather than an automatic admission or monetary award.

In Part II, Thomas separately argues that preserving selective prestige does not create a constitutionally sufficient need for unequal treatment. An institution's chosen level of selectivity cannot itself justify an ancestry preference. His supported violation-linked remedial-duty position in Hopwood remains distinct from this nonremedial policy. Both dissenters oppose the present approval; their writing supplies no assent to the Court's continuing-permission rule.'''

grutter_precedent='''- Adarand Constructors, Inc. v. Peña, June 12, 1995: applies the unchanged common substantial-justification standard and government-borne evidentiary burden.
- Hopwood v. Texas, November 25, 1996: applies the already established educational-diversity permission, genuine-competition requirement, intentional-treatment rule and distinction between process injury and lost admission.
- Regents of the University of California v. Bakke, 438 U.S. 265: applies the preserved competitive-consideration boundary.
- City of New York v. Patrolmen's Benevolent Association, April 23, 2003: applies actual objective, relationship, burdens and alternatives despite a useful operational purpose.
- Montiel v. Davis, January 13, 2003: preserves distinct constitutional and statutory inquiries without replacing the admissions-classification standard.
- Runyon v. McCrary, 427 U.S. 160: applies educational-contract coverage and preserves rejection of an associational defense to racial exclusion.
- McDonald v. Santa Fe Trail Transportation Co., 427 U.S. 273: applies §1981's protection of applicants of every race.
- General Building Contractors Association v. Pennsylvania, 458 U.S. 375: applies the intentional-discrimination relationship without making all constitutional permissions statutory defenses.
- Alexander v. Sandoval, April 24, 2001: preserves §601's intentional-treatment protection.
- Texas v. Lesage, November 29, 1999: preserves the distinction between competitive-process injury and consequential admission relief.'''

grutter_kernel='''## Event, participation and entering law

Grutter v. Bollinger, No. 02-241; argued April 1, 2003; decided June 23, 2003. Plenary certiorari review of the Sixth Circuit's reversal of the District Court's invalidation of the Law School admissions program. The preserved question includes equal protection, Title VI and §1981; the actual intentional-treatment claims are each reached and resolved. Grutter seeks invalidation and individual relief based on the policy; the Law School seeks affirmance. The record includes its 1992 policy, individual-review testimony, variation in outcomes, educational and alternative evidence, and the contested significance of enrollment monitoring. The judgment rests on the supported record at its actual scope, not a new historical finding or an inference of perfect individual treatment.

All nine participate at argument and decision: Stone, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. Quorum is satisfied; five joins are required for controlling force. The operative substantial-justification and educational-competition rules come from Adarand and Hopwood; Montiel and Patrolmen's preserve their actual classification and distinct statutory operation. Sandoval and the earlier §1981 authorities supply the separate statutory inquiry. Gratz supplies no entering holding: the cases share the June 23 baseline without substantive same-day sequencing. No later June 26 decision enters. Final integration remains subject to the intervening June 16 public-law refresh.

## Stone fixed core and final compatibility

The approved source is `runtime/OT_2002CHUNK13_C_STONE.md`, Grutter Section II. Stone affirms the actual program under the existing common standard, demanding supported educational function, justified burdens, genuine competition and a response to concrete practical alternatives. He rejects a format-based safe harbor, racial viewpoint assumptions, indefinite unsupported operation and an invented fixed sunset. His distinct statutory positions reject the presented Title VI and §1981 policy theories while preserving their enacted predicates and remedies. The approved remedy denies relief based on these theories and preserves the policy within its justified design.

Each Part I–IV proposition is within that fixed core. Stone joins the full opinion. No conditional branch, fallback, new ground, substantive narrowing or clerical correction is used. His safeguards against unrequested relief are satisfied by the affirmance without a public remedial catalogue. No distinct Stone writing is necessary: the Court's full reasoning carries his approved ground, qualifications and remedy.

## Form, assignment and join test

A signed opinion following plenary argument addresses the constitutional record application, concrete alternatives and continuing justification, and each of the two statutes separately. The form and legal parts are fixed without reference to author counts. Stone, Stevens, O'Connor, Souter, Ginsburg and Breyer support all four parts. The genuine-comparison finding and concrete alternatives analysis answer the objection to academic deference without changing any frozen commitment. Continuing justification, rather than a forecast of a particular year, is the shared actual standard.

__ASSIGNMENT_BLOCK__

Kennedy refuses the actual-operation conclusion and supports statutory invalidity at that narrower scope; he joins none of the lead. Scalia and Thomas maintain their broader objection and actual-mechanism ground, also joining none of the lead. Thomas's dissent Part I states their shared position; Scalia's join stops before Thomas's distinct selective-prestige ground in Part II. This scope follows the frozen grounds rather than historical authorship or partial joins. No separate Ginsburg or Breyer writing is needed merely to exclude a fixed sunset absent from the Court's own rule. Six direct full joins control every announced proposition; no Marks construction or artificial circulation is used.

## Continuity, disposition and law change

The Sixth Circuit judgment sustaining the program is affirmed, 6–3. The constitutional common rule remains unchanged and is applied to the developed operational record. Continuing justification supplies the permission's duration; no fixed calendar sunset is created. Title VI and §1981 receive independent justified-competition constructions and dispositions, rather than being silently assimilated to equal protection. The presented policy-violation claims are resolved and the requested relief based on them is denied. The District Court injunction, vacated below, is not reinstated. Materially changed future operation is ordinary application of the governing rule, not a law question reserved by this decision.

The complete material published noncontrolling continuity is in the separate-writing summaries below: Kennedy's supported-objective but insufficient-operation objection; Scalia and Thomas's broader nonremedial-preference and actual-mechanism objections; Thomas's distinct selective-prestige ground; and their bounded individual-remedy positions. None changes current law. No roster, allotment, standing practice or admitted external follow-up changes. The reviewed merits controversy is resolved; no separate new proceeding is invented.'''

grutter_blocks=[
('Event','Grutter v. Bollinger, No. 02-241. Argued April 1, 2003; decided June 23, 2003. On writ of certiorari to the United States Court of Appeals for the Sixth Circuit. The Sixth Circuit reversed the District Court\'s invalidation of the Law School\'s admissions policy and sustained its consideration of race. The Court decides whether that policy violates equal protection, Title VI or 42 U.S.C. §1981 on the developed record of individual review, educational effects, actual outcomes, enrollment monitoring and alternatives.'),
('Participation','Stone, Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated at argument and decision.'),
('Public Action','The Court affirms the judgment sustaining the Law School\'s actual admissions program and rejects the presented constitutional, Title VI and §1981 policy challenges.'),
('Judgment & Remedy','''**Affirmed, 6–3.**

**Supporting:** Stone, Stevens, O'Connor, Souter, Ginsburg and Breyer.
**Opposing:** Scalia, Kennedy and Thomas.

The requested invalidation and individual relief resting on the resolved policy-violation theories are denied. The District Court's injunction, vacated by the Sixth Circuit, is not reinstated.'''),
('Opinion Topology',grutter_topology),('Holdings',grutter_holds),('Precedent Treatment',grutter_precedent),
('Law After Decision','The existing common standard permits the Law School\'s supported program of genuine competitive consideration. Actual educational function, burdens and practical alternatives govern both present permission and its continuation; individualized language or academic expertise supplies no exemption. Title VI and §1981 independently permit the justified competitive treatment established here at the stated statutory scope. The factual basis must continue to support operation, and changed circumstances are assessed under the same rule.'),
('Separate Writings',grutter_separates),
('Procedure After Action','The Sixth Circuit judgment is affirmed. The policy may continue within its justified design and applicable statutory requirements. The presented policy-violation claims and the requested relief based on them are resolved. Future operation remains subject to the continuing-justification condition through ordinary challenge procedures.'),
('Source Notes','U.S. Const., Amend. XIV; 42 U.S.C. §§1981, 1983, 2000d. Grutter v. Bollinger, No. 02-241; 137 F. Supp. 2d 821; 288 F.3d 732. The record includes the Law School\'s 1992 policy, admissions testimony, individual variation, educational-effect evidence and disputed statistical assessments of actual racial weight and proposed alternatives.')]

grutter_file='Grutter-v-Bollinger_merits_2003-06-23.md'
write_record(grutter_file,'Grutter v. Bollinger','02-241','2003-06-23','Affirmed, 6–3; the constitutional, Title VI and §1981 policy challenges are separately rejected.',grutter_kernel,grutter_holds,grutter_blocks,162)
specs=json.loads((OUT/'C_specs.json').read_text(encoding='utf-8'))
specs=[s for s in specs if s['case']!='Grutter v. Bollinger']
specs.append({'file':grutter_file,'case':'Grutter v. Bollinger','date':'2003-06-23','countable':True,'assigner':'Stone-Zsela','chief_assigns_any':True,'eligible_authors':['Stone-Zsela','Stevens',"O'Connor",'Souter','Ginsburg','Breyer'],'full_joiners':['Stone-Zsela','Stevens',"O'Connor",'Souter','Ginsburg','Breyer']})
(OUT/'C_specs.json').write_text(json.dumps(specs,indent=2)+'\n',encoding='utf-8')
print('Grutter draft and complete C_specs.json written.')
