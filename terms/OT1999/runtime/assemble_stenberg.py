from pathlib import Path
import re

term=Path(__file__).resolve().parents[1]
path=term/'records/stenberg-v-carhart_merits_2000-06-28.md'
assert not path.exists(), 'Initial assembly must not overwrite an existing Stenberg Record.'
neutral=(term/'freeze/OT_1999CHUNK9_STENBERG_NEUTRAL.md').read_text(encoding='utf-8')
reconciled=(term/'freeze/OT_1999CHUNK9_STENBERG_RECONCILED.md').read_text(encoding='utf-8')
standard=neutral.split('### Protected choice and the six-step standard for previability regulation\n',1)[1]
framework=standard.split('**Current rule:** ',1)[1].split('\n\n**Authority by component:**',1)[0].strip()
assert all(f'{n}. **' in framework for n in range(1,7))
judgment_source=neutral.split('## Stenberg - exact district-court judgment directions\n',1)[1].split('\n\n---',1)[0].strip()
departure_lines='\n\n'.join(re.findall(r'^\*\*Historical departure:\*\* .+$',reconciled,re.M))
assert departure_lines.count('**Historical departure:**')==2

holding_open='''### 1. The complete Casey standard governs the enacted duty and proved applications

**Holding and operative rule:** The complete six-step Casey standard, as applied in Fargo and Voinovich, governs Nebraska's method prohibition; an established substantial obstacle and denial of timely necessary life-and-health care are independently invalid, and the absence of an obstacle does not end review of remaining severe or meaningful interference. The Court applies that existing rule without substituting a numerical facial threshold, a no-valid-applications barrier, a physician-preference exemption or a new bodily-autonomy framework.

**Authority:** Souter's Opinion of the Court, joined by Stone-Zsela, Stevens, O'Connor, Ginsburg and Breyer, controls all four holdings by six direct votes. Kennedy's agreement with the necessary-care baseline does not add a join in this complete framework or the Court's completed applications.

**Governing rule retained from Casey:**

'''

holding_rest='''

**Controlling explanation:** Casey preserves the patient's previability decision and necessary care while replacing the former trimester timetable with the complete ordered inquiry above. Fargo applies that framework without confusing notice, culpability and substantive access. Voinovich requires examination of the actual prohibited acts, clinically usable alternatives, statutory defenses and matching relief; it does not make overlap between medical and statutory labels enough to decide every issue. Here the enacted substantial-portion language and developed clinical findings permit substantive application. The Court identifies the affected nonviable procedures and patients, the prohibition's added interference and the actual safeguards before reaching the independent obstacle and necessary-care bars. Neither bar can be overcome by balancing after the violation is established. No separate obstructive-purpose finding or new residual-interference application is needed to sustain this judgment. The remaining steps and their proof allocation remain governing law, not abandoned requirements.

### 2. The enacted definition reaches ordinary D&E and creates a substantial obstacle

**Holding and operative rule:** Nebraska's definition reaches the supported ordinary dilation-and-evacuation sequence when the physician deliberately and intentionally brings a living fetus or a substantial portion into the vagina to perform a procedure the physician knows will cause death and that does cause death before delivery is completed. Prohibiting those ordinary D&E applications removes practical access to the predominant second-trimester method for the affected previability patients and creates a substantial obstacle, independently sustaining the existing bounded declaration and injunction.

**Controlling explanation:** The statutory elaboration includes a substantial portion, not only intact delivery. The described ordinary procedure can deliberately bring a living fetus's limb through the cervix before dismemberment; the act, intent, knowledge, life and sequence elements can therefore be satisfied in ordinary D&E. The Court does not hold that every D&E is prohibited, that a label establishes all elements, or that removal after fetal death satisfies the living-fetus condition.

Nebraska's strongest answer invokes the entire delivery-and-death sequence, the enactment's purpose and constitutional avoidance to confine the prohibition to the intact method. Those considerations cannot erase the enacted substantial-portion alternative or insert an exclusion the text does not contain. The Attorney General's nonenforcement position is not an authoritative Nebraska Supreme Court construction or established control over every county prosecutor. Constitutional avoidance permits a legally available construction; it does not authorize rewriting this statute.

Casey requires concrete interference rather than a presumption against all method regulation. The operative comparison is care with and without this prohibition, with other circumstances held constant, for patients whose timely clinically appropriate nonviable care uses the ordinary D&E acts described. Penal and dependent licensing exposure constrains that usable provider capacity. The availability of other procedures in some circumstances does not establish adequate care for that affected population. Voinovich's rejection of categorical notice reasoning does not cure a demonstrated substantive obstacle; Ohio's distinct alternative-method defenses are absent here. The law's absence of a viability limit does not enlarge the present injunction beyond its nonviable scope, and no categorical vagueness holding is necessary.

### 3. The supported necessary-health applications independently require protection

**Holding and operative rule:** Even if the prohibition could lawfully be confined to an intact procedure, it cannot be enforced in supported circumstances where compelling substitution for that method creates a material risk of death or serious health harm and the method is medically necessary for timely safe and suitable care. Nebraska's specified life-only exception and post-charge life-necessity evidence do not supply a usable exception for those necessary serious-health applications; this independent defect supports the existing protection at its proved nonviable scope.

**Controlling explanation:** Casey's necessary-care baseline requires protection before imminent death or catastrophic deterioration, and Fargo and Voinovich separate substantive adequacy from an intelligible emergency definition. The District Court credited explained clinical advantages for Carhart's intact method in recurring circumstances involving roughly ten to twenty annual cases: reduced instrumentation, retained parts, trauma, blood loss, operating time and infection risk. The findings support clinically consequential risk reduction in the identified applications, not universal superiority or a right to every preferred method.

The State properly invokes competent medical disagreement, the absence of controlled comparative studies, available alternatives and professional ethics. Those considerations receive weight; no physician or professional association has a constitutional veto. But the developed, credited evidence establishes the necessary-care applications here, and general availability of another method does not establish that it is timely, safe and suitable for those patients. The Court adopts no new numerical risk threshold or presumption that every comparative advantage is necessary.

Section 3(1) authorizes the defined life-saving care; the defect is not an assertion that it protects no life. Its terms do not independently authorize care needed to avoid serious nonfatal harm. The broader emergency-situation definition is not incorporated into that exception. A hearing after charges permits evidence on the same life criterion, not permission to provide the otherwise forbidden necessary-health treatment. Neither admissibility of the Director's findings nor a possible motion to delay trial supplies the missing substantive defense. Voinovich's Ohio alternative-method protections cannot be imported. This conclusion adds no general medical immunity and does not decide every future, precisely drawn method restriction with genuinely usable care safeguards.

### 4. Affirmance preserves the actual nonviable injunction and bars its evasion through dependent sanctions

**Holding and operative rule:** The existing declaration and injunction remain in force for Carhart, his patients and similarly situated persons regarding his D&E and D&X methods on nonviable fetuses, against the defendants and persons bound under Rule 65(d), with the existing county-attorney service direction. Criminal and licensing consequences cannot enforce those same unconstitutional applications, while independently lawful requirements and applications remain subject to Nebraska's section 8 severability direction and the judgment's actual limits.

**Controlling explanation:** Casey's sixth step requires relief corresponding to the proved violation; Voinovich preserves independently lawful provisions and dependent-duty analysis without automatic wholesale invalidation. The District Court expressly declined whole-statute facial relief. Affirming its bounded judgment does not create a nationwide or all-gestation injunction, decide fetal personhood, award damages or independently adjudicate the separate fee appeal. It also does not permit officials to reimpose the invalid prohibition through its dependent license sanctions.

Nebraska section 8 preserves the validity of remaining portions when a section or part is unconstitutional. It supplies no power to insert an intact-only definition or health exception and does not erase the sanction provisions for every lawful application. The enacted Director, petition, hearing and evidentiary procedures remain material to what the law does; the Court neither converts the life-only hearing into a health defense nor decides the unnecessary relationship between section 3(4)'s mandatory wording and the general sanction menu. Patient immunity remains intact. No new hearing, administrative veto, prosecution, damages award or statewide medical-policy revision is ordered.'''
proof=re.search(r'\*\*Burdens and proof:\*\* [^\n]+',standard)[0]
holdings=holding_open+framework+'\n\n'+proof+holding_rest

kernel='''**Case and dockets:** Stenberg v. Carhart; No. 99-830.
**Event and date:** Plenary merits decision, October Term 1999, chunk 9; 2000-06-28; argued 2000-04-25.
**Result:** Affirmed by six Justices on independent ordinary-D&E/access and necessary-health grounds; Kennedy would vacate and remand; Scalia and Thomas would reverse and remand.
**Version / lineage:** Original decision.

## Decision kernel

### Event, lawful reach, participation and entering law

The Public Projection states the event, statutory duties, clinical record, exact judgment, independent holdings and remedy. Certiorari review under 28 U.S.C. section 1254(1) concerns the Eighth Circuit's September 24, 1999 judgment, 192 F.3d 1142. The grant includes ordinary-D&E reach and absent health protection; the petition's additional fetal-personhood and wholesale-reconsideration proposals do not enlarge it. All nine participate at argument and decision, satisfying quorum. No new threshold defect, waiver, default, enforcement event or unreviewed fee component is invented.

The [frozen neutral packet](../freeze/OT_1999CHUNK9_STENBERG_NEUTRAL.md), [validation](../freeze/OT_1999CHUNK9_STENBERG_NEUTRAL_VALIDATION.md) and [focused entering law](../entering-law/OT_1999CHUNK9_STENBERG.md) preserve the complete Casey, Fargo and Voinovich rules and each prior public join. The actual statute is Nebraska LB23, not Ohio's different enactment. The independently decided June 28 matters supply no new abortion-method rule; earlier same-date opinions enter assignment order only. No historical current-case opinion becomes prior law, and no historical Voinovich certiorari denial replaces its actual merits decision.

All five official LB23 images were inspected in assembly, including the underlined new text missing from the PDF's searchable extraction. The Director's role, statutory references, licensing petition/hearing, life-necessity evidence, optional motion, admissibility, discipline options, consultation/response, reinstatement, referral and severability terms are preserved in the public statutory account. That account is a paraphrase verified against the images, not a manually reconstructed exact transcript. The older incomplete licensing extract is not the operative source.

### Stone's controlled position

Section II fixes affirmance on both independent grounds: practical ordinary-D&E coverage causing a substantial obstacle, and absent usable protection for circumstances in which substitution creates a material risk of death or serious health harm. The Court adopts both under the existing governing framework, without a new bodily-autonomy theory or a claim that every method preference is necessary. The actual as-applied nonviable remedy is left in place, as required. A different precisely defined procedure regulation, excluding standard D&E and preserving clinically usable serious-health care with appropriate culpability and no obstacle, remains a different case subject to the complete framework; it is not automatically validated.

Stone joins the complete opinion on these grounds and limits. No fallback is used. He does not adopt a new categorical vagueness ground, withdraw his earlier Voinovich disagreement on notice, choose a new statutory construction, or order new severability relief beyond affirmance of the actual judgment. Discussion of the existing governing notice rule preserves its force without converting his present substantive application into a retroactive join in the earlier rationale. No separate Stone writing is necessary.

### Form, fresh count, assignment and final compatibility

The [pre-count form receipt](../freeze/OT_1999CHUNK9_STENBERG_FORM.md) fixes one signed opinion stating the complete governing framework, two independently sufficient invalid applications and violation-matched affirmance. Kennedy's vacatur/remand and Scalia/Thomas's reversal remain distinct dispositions. No separate affirmation concurrence, categorical purpose holding or divided authorship is needed, and these choices precede any count.

The [fresh count](../freeze/OT_1999CHUNK9_STENBERG_ASSIGNMENT_COUNTS.json), from actual preceding opinion tables, is Stone-Zsela 10; Stevens 11; O'Connor 11; Scalia 10; Kennedy 11; Souter 11; Thomas 10; Ginsburg 11; Breyer 12. The last counted event is Mitchell v. Helms, June 28, 2000, delivered by Breyer. Hill's earlier Breyer lead and Dale's Souter lead are included in the same-date alphabetical sequence. No Alaska decree or unwritten opinion enters this count.

Stone is in the six-Justice formal judgment coalition and assigns. Complete-ground eligible authors are Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg and Breyer. The minimum eligible count is 10; the pool contains the first five, with counts 10 or 11. Breyer's count of 12 excludes him from this assignment despite his full joinder and any historical authorship. Neither Kennedy's baseline agreement nor Scalia/Thomas's notice agreement qualifies them for the Court opinion.

Souter is selected on fit. His actual Fargo and Voinovich opinions directly distinguish the legal work needed here: intelligibility and culpability are separate from an enacted method's substantive effect; a necessary-care safeguard must be usable; distinct state defenses cannot be imported; and relief follows proved applications. His current commitment explains why Voinovich's categorical-notice remand does not require another remand on this developed Nebraska record. Stone is the strongest lower-count alternative: his approved position precisely preserves both substantive grounds and the complete framework he authored. Souter nonetheless offers a concrete advantage in coordinating those intervening method, necessary-care and remedy applications without recasting the case as a general bodily-autonomy revision. He faithfully carries Stone's full case-specific objective. This is settled-ground fit, not expansion or an assumed entitlement from prior authorship; no commitment changes to support it.

Stevens, O'Connor, Souter, Ginsburg and Breyer each join the complete framework, actual D&E access finding, independent clinically supported necessary-health application and existing bounded remedy. O'Connor's willingness to consider a different intact-only law is retained subject to every remaining Casey step. Stevens/Ginsburg's historical purpose and preference arguments are not imported as additional holdings. Breyer's clinical assessment does not become a universal superiority rule. Stone's fixed position supports every Court proposition at this scope.

Kennedy does not join the Court opinion. He preserves the contextual intact-method construction, his constitutional necessary-care baseline and rejection of residual lesser-burden review, but seeks bounded further legal application rather than affirming the existing health determination. He writes a dissent seeking vacatur/remand, with no automatic dissolution or blanket enforcement. Thomas writes the shared reversal dissent, joined by Scalia, expressly preserving both Justices' constitutional objection rather than hiding it behind a narrower application dispute. The common dissent performs the legal work Scalia requires; no extra repetitive writing is invented. No post-reconciliation changed commitment or artificial circulation history occurs.

## Controlling holdings

'''

continuity='''

## Continuity and source status

Research cutoff: June 28, 2000. The official LB23 images and supported published district/appellate recitations establish the actual enactment and bounded record. The source limitation remains that no claim is made of exhaustive reading of every petition, brief and appendix page; a missing searchable passage or unreviewed volume establishes no missing court filing or litigant failure. No new clinical condition, quantitative risk estimate, binding Nebraska construction, certification procedure or enforcement event is supplied. The exact prior framework and district judgment directions are mechanically copied in this Record.

The public separate positions remain noncontrolling: Kennedy retains the necessary-care baseline but seeks a different application/remedy, while Scalia and Thomas reject the constitutional premise. O'Connor's constrained willingness to consider a different law is preserved in the common opinion. No roster, allotment or institutional-practice change occurs. The actual declaration and injunction remain; the case is not transformed into a new facial/all-gestation decree. The separate fee appeal receives no new determination.

This original Record is written in the current Run for validation and projection. Repository commitment remains the operator's task; no Git command or commit-reference existence check is claimed. Script checks confirm eleven Public Projection blocks, identical internal/public holdings, exact framework/judgment source copies, resolving relative links and ordinary controlling explanations under 350 words. The complete existing six-step rule is reproduced as the operative standard, not divided explanations or new reasoning evading the ceiling. Ledger, manifest, current projections, Render Input and final term validation remain integration steps.

## Adaptive audit annex

The [independent commitments](../freeze/OT_1999CHUNK9_STENBERG_COMMITMENTS.md) and [frozen historical reconciliation](../freeze/OT_1999CHUNK9_STENBERG_RECONCILED.md) preserve the full own-Justice comparisons, strongest contrary paths, join limits and disposition differences. The reconciliation read every historical writing and compared the complete official reporter; historical authorship and joins did not assign any current opinion.

| Justice | Frozen and final position | Own-source comparison and exact limit |
|---|---|---|
| Stevens | Affirm; full Court join | Full Casey/Fargo/Voinovich joins support actual access and necessary-care findings, with objective purpose and violation-specific relief. Historical liberty concerns remain, but no universal preference exemption or extra irrationality holding is necessary. |
| O'Connor | Affirm; full Court join | Both historical grounds remain supported. Her own complete-framework joins prevent an automatic guarantee that an intact-only law with a health exception is valid; all remaining steps still apply. |
| Scalia | Reverse/remand; joins Thomas | His constitutional objection remains independently sufficient; contextual construction and reasonable-regulation grounds do not erase controlling law or medical findings. The common dissent expressly states his constitutional disagreement, making a separate repetition unnecessary. |
| Kennedy | Vacate/remand; separate dissent | His actual necessary-care joins and Voinovich's distinct Ohio health defense prevent transferring the former method disposition to Nebraska's life-only regime without a supported application inquiry. He retains contextual construction and rejects the Court's final health application and residual lesser-burden rule. |
| Souter | Affirm; authors complete opinion | His Fargo/Voinovich distinctions require actual conduct, culpability, clinical alternatives and remedy analysis. Developed Nebraska coverage and clinical findings support decision rather than a categorical notice-based remand. |
| Thomas | Reverse/remand; authors common dissent | The constitutional disagreement, contextual construction and reasonable-regulation position survive. Historical obstacle-only Casey, a historical Voinovich certiorari denial and a whole-statute facial characterization cannot replace the actual governing law and bounded judgment. |
| Ginsburg | Affirm; full Court join | Complete Fargo/Voinovich joins support both independent applications and corresponding relief. Historical medical-choice and purpose concerns do not establish an unnecessary additional purpose holding or physician veto here. |
| Breyer | Affirm; full Court join | Credited clinical advantages are qualified, not universal; controlled-study absence does not eliminate explained supported evidence. His actual Voinovich remand was record- and defense-specific, not a universal duty to remand method restrictions. |

'''

annex_tail='''

No other material historical departure is found. Stevens/Ginsburg's additional historical concurrence reasoning is unnecessary, not silently converted into current law or affirmatively repudiated. The two departure lines identify concrete own-Justice premises; they are not a mechanical vote-matching exercise.

Internal vote audit: Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg and Breyer supply six full votes for the framework, each independent ground, and affirmance of the actual nonviable protection. Kennedy supplies one present vacatur/remand vote, not a seventh health-application or affirmance vote. Scalia and Thomas supply two reversal/remand votes. Three contextual-construction votes do not create one common dissenting remedy. Kennedy's necessary-care baseline assent does not supply his assent to the Court's final clinical application. No Marks synthesis or aggregation is required.

## Exact prior judgment source annex

The following operative district directions are mechanically copied from the frozen packet's actual appendix extraction. They preserve the original source pagination and OCR and define the existing relief affirmed; no enlarged replacement decree is authored here.

'''

event='''

## Public Projection

## Event

Stenberg v. Carhart, No. 99-830. Plenary merits decision; argued April 25, 2000; decided June 28, 2000. On writ of certiorari to the United States Court of Appeals for the Eighth Circuit, reviewing its September 24, 1999 judgment, 192 F.3d 1142. The questions concern Nebraska's enacted definition reaching ordinary dilation and evacuation, or D&E, and the absence of an independent necessary-health exception.

Carhart performs abortions before viability. The District Court credited specific safety advantages for his intact dilation-and-extraction method, or D&X, in recurring clinical circumstances; it did not find that method universally superior. It expressly declined whole-statute facial relief and protected Carhart, his patients and similarly situated persons regarding his D&E and D&X methods on nonviable fetuses. The Eighth Circuit affirmed on the ordinary-D&E/substantial-obstacle ground without deciding the separate intact-method or vagueness grounds. The separate fee appeal, fetal personhood and wholesale reconsideration of the governing framework are not decided here.

### Enacted duties and safeguards

LB23 was approved June 9, 1997 and became effective on passage and approval. Its definition, section 28-326(9), requires partial vaginal delivery of a living unborn child before killing and completing delivery; the elaboration requires deliberate and intentional delivery of a living child or a substantial portion into the vagina for a procedure the performer knows will kill it and that does kill it. The definition contains no viability limit. Death before the relevant removal does not satisfy the living-fetus element.

Section 3(1), codified at section 28-328(1), permits the procedure only when necessary to save the mother's life endangered by physical disorder, illness or injury, including a life-endangering physical condition caused by or arising from the pregnancy. It supplies no independent serious-health exception. The separate emergency-situation definition turns on the physician's good-faith clinical judgment concerning a condition requiring immediate abortion to avert death or delay creating serious risk of substantial impairment of a major bodily function; section 3(1) does not invoke or incorporate that broader definition.

Section 3(2) makes intentional and knowing unlawful performance a Class III felony. Section 3(3) prohibits prosecution of the woman under this section or for conspiracy to violate it; that patient immunity is distinct from a physician defense.

| Licensing or related provision | Enacted actor, condition and procedure |
|---|---|
| Section 3(4) | Intentional and knowing unlawful performance results in automatic suspension and revocation of the attending physician's Nebraska medical license by the Director of Regulation and Licensure pursuant to sections 71-147 through 71-161.20. |
| Section 3(5) | When the Attorney General or a county attorney files criminal charges under the section, the Attorney General must also file a section 71-150 suspension/revocation petition. A section 71-153 hearing must be set, and the physician must have an opportunity to present the same specified life-necessity evidence. A criminal defendant may move to delay the trial's beginning until the Director's section 71-155 order; delay is not automatic. The Director's findings on life necessity are admissible, not conclusive, in the criminal proceeding. |
| Sections 5-6 | Intentional and knowing performance is added to unprofessional conduct in section 71-148(15), with the same life-saving exception. The section 71-155 proceeding is summary and tried as an equity action before the Director or designated hearing officer. Affidavits may be admitted at their discretion; subpoena, oath, attendance, document-production and deposition powers remain. For this procedure charge the Director must make findings on the same life-necessity question. |
| General section 71-155 powers | The Director may order censure or reprimand, suspended judgment, probation, practice limitations, a severity-based civil penalty up to $10,000, suspension, revocation or dismissal. The relation of this general menu to section 3(4)'s mandatory wording is not resolved here. After a guilt finding, board consultation on sanctions or conditions is optional; if used, the licensee receives the request and recommendation and may respond in the manner the Director determines. |
| Suspension and reinstatement | No practice is permitted while the license is suspended or revoked. Suspension is for a definite period set by the Director; reinstatement may be automatic at expiration, conditional on satisfaction of prescribed terms, or subject to probation or practice limits. Revocation is permanent except that reinstatement may be sought after two years under section 71-161.04. |
| Separate board referral under section 7 | After Attorney General referral, the board may send an Attorney-General-approved letter of concern identifying the statute or rule and conduct at issue, advise on a voluntary assurance of compliance, or recommend a section 71-150 petition. The letter is board-signed and public. An assurance states the legal requirement and promised compliance, acknowledges that breach is unprofessional conduct, is signed by the licensee and public, and does not admit a prior violation. |

Section 4 extends the existing employment-protection remedy to the new section: a person whose employment or position is altered, impaired or terminated in violation of the listed provisions may seek the prescribed consequential damages, lost wages, reasonable attorney fees and litigation costs. That provision creates no patient damages award in this case. Section 8 preserves the validity and constitutionality of remaining portions when a section or part is invalidated; section 9 repeals the superseded provisions. None of these procedures supplies a new preprocedure medical-board veto or an independent necessary-health defense.

## Participation

All nine Justices participated at argument and decision: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer.

## Public Action

The Court affirms the judgment on two independent grounds: the prohibition's actual reach into ordinary D&E creates a substantial obstacle, and its life-only exception does not protect the supported necessary-health applications. The existing nonviable, as-applied declaration and injunction remain in force.

## Judgment & Remedy

**Affirmed by six Justices.** The three Justices opposing affirmance favor the distinct dispositions shown below.

| Disposition position | Justices | Remedy and relationship to the judgment |
|---|---|---|
| Affirm, six votes | Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg and Breyer | Leave the existing declaration and injunction for Carhart, his patients and similarly situated persons regarding his D&E/D&X methods on nonviable fetuses in place. |
| Vacate and remand, one vote | Kennedy | Identify and protect supported necessary-care applications under his retained baseline; preserve necessary dependent-sanction and interim protection as legally warranted. No automatic dissolution or blanket enforcement. |
| Reverse and remand, two votes | Scalia and Thomas | Remove the corresponding constitutional injunction at the granted scope; impose no prosecution, civil liability or administrative sanction by this judgment. |

The Court's affirmance is not a new whole-statute, nationwide or all-gestation injunction. The existing direction to serve the decision and judgment on Nebraska county attorneys and the binding scope under Rule 65(d) remain. No new damages, hearing or separate fee determination is ordered.

## Opinion Topology

| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | Souter | Stone-Zsela, Stevens, O'Connor, Ginsburg and Breyer | Affirms | Complete Casey standard, ordinary-D&E/access ground, independent necessary-health ground and existing bounded relief in full |
| Dissent | Kennedy | No additional join | Would vacate and remand | Contextual intact-method construction, retained necessary-care baseline, further application and remedy; no residual lesser-burden or completed health-application join |
| Dissent | Thomas | Scalia | Would reverse and remand | Constitutional objection, contextual construction and reasonable-regulation account, with actual governing law and injunction scope acknowledged |

The Court's six Justices adopt each independently sufficient ground at the same level of generality. Kennedy's necessary-care baseline does not add a vote to the Court's completed clinical application. Agreement among the three dissenters about contextual construction does not merge their remedies or other grounds. No narrowest-grounds synthesis is needed.

## Holdings

'''

tail='''

## Precedent Treatment

- Planned Parenthood of Southeastern Pennsylvania v. Casey retains protected choice, individualized viability, timely necessary life-and-health care and the complete six-step rule. Both independent invalidity grounds are applications of that rule; residual severe- and meaningful-interference protections remain, and no obstacle-only substitute is adopted.
- Fargo Women's Health Organization v. Schafer supplies the distinction between intelligibility, applicable fault and substantive access under the complete framework. An understandable life exception does not itself supply adequate necessary-health protection, and fault words do not automatically cure an exclusion of care.
- Women's Medical Professional Corp. v. Voinovich requires attention to actual prohibited acts, usable alternatives, distinct statutory defenses and violation-matched relief. Its rejection of categorical notice reasoning remains; its remand on the Ohio method record does not require remand on every method law. Ohio's enacted alternative-method defenses and Ohio severability rules do not become Nebraska law.
- Roe v. Wade and Doe v. Bolton retain the protected decision and clinical safeguards preserved in Casey; the independent trimester timetable remains displaced. No broader reconsideration or new fetal-personhood ruling is undertaken.

## Law After Decision

Nebraska cannot enforce LB23 in the nonviable Carhart-type applications covered by the existing judgment, including through criminal or licensing consequences dependent on the same invalid prohibition. Ordinary-D&E access and supported necessary-health applications each independently support that protection. A defined method, intentional conduct and a life-only exception do not end the substantive inquiry. The complete Casey framework remains controlling, and a materially different precise procedure regulation with clinically usable care protections would require its own full analysis. Patient immunity, independently lawful regulation and ordinary professional discipline remain; no general professional veto or whole-statute invalidity is created.

## Separate Writings

**Kennedy, dissenting.** He would vacate and remand rather than affirm or authorize immediate blanket enforcement. Reading the complete delivery-and-death sequence in context, he would confine the law to the intact method and rejects the Court's ordinary-D&E access ground. Potential-life and professional-ethics interests permit meaningful regulation; the physician's preferred technique or every asserted comparative advantage does not control the legislature. He also rejects the residual lesser-burden portion of the complete Casey framework.

He retains the necessary-life-and-health baseline he joined in Casey, Fargo and Voinovich. Voinovich's method analysis materially included Ohio's alternative-method health defense and preserved supported necessary-care applications. Nebraska has no corresponding defense: the exception and later licensing evidence concern only the stated life-saving condition. He therefore would require identification of the circumstances in which available alternatives are clinically inadequate for timely safe and suitable care under that retained baseline. He accepts the credited comparative reductions in the described surgical risks without finding every intact-method use necessary or joining the Court's completed health application.

The lower court may make the needed legal application on the existing record if adequate. His remand orders no automatic new hearing, filing or invented condition. It permits only a Nebraska-law-supported protective construction, preserves supported necessary-care and dependent-sanction protection, and requires ordinary consideration of interim relief. It neither inserts a new exception nor automatically dissolves existing protection. The serious necessary mental-health protection in Voinovich supports his adherence to necessary-care protection, not an imported medical test for every physical-risk claim here.

**Thomas, joined by Scalia, dissenting.** They would reverse the constitutional judgment at the granted scope and remand to remove the corresponding injunction. Their principal disagreement is with the constitutional abortion and necessary-health requirements themselves. They acknowledge Casey's complete framework and the actual Fargo and Voinovich holdings as the governing law from which they dissent; they do not replace that law with an obstacle-only description or a different facial-review threshold.

They favor the contextual intact-method construction and ordinary reasonable regulation for potential-life and medical-ethics purposes. The Attorney General's representation is not made binding on every prosecutor, and the credited clinical findings are not declared nonexistent or every alternative equally safe. Their constitutional objection supplies the reason for rejecting the Court's protective conclusion notwithstanding those facts. Agreement in earlier notice and severability propositions does not establish substantive validity, universal knowledge of illegality, good-faith immunity or a cure for every enforcement problem. They seek no new prosecution, damages, administrative sanction, fetal-personhood adjudication or injunction governing viable procedures. Their constitutional objection remains independent of their statutory-construction argument.

## Procedure After Action

The Eighth Circuit's judgment is affirmed. The existing declaration and permanent injunction protect Carhart, his patients and similarly situated persons regarding his D&E and D&X methods on nonviable fetuses. The defendants and their agents, servants and employees remain bound; Stenberg must serve the decision and judgment on Nebraska county attorneys, who and whose agents, servants and employees are bound as directed under Rule 65(d). Dependent criminal and license sanctions cannot enforce those protected applications. The Court adds no whole-statute facial invalidation, viable-fetus injunction, new hearing, damages award or separate fee decision. Independently lawful provisions and applications remain subject to section 8 and the actual judgment's limits.

## Source Notes

The [official five-page LB23 enactment](https://nebraskalegislature.gov/FloorDocs/95/PDF/Slip/LB23.pdf) supplies the complete definitions, life exception, patient immunity, licensing process, discipline provisions, severability and effective date; the printed underlined new terms govern where searchable text is incomplete. The [Eighth Circuit opinion, 192 F.3d 1142](https://static.case.law/f3d/192/html/1142-01.html) supplies the appellate grounds and reservations. The [record and briefs for No. 99-830](https://archive.org/details/micro_IA40385014_0347), particularly the supplemental appendix's district opinions and actual judgment directions, supply the qualified clinical findings and bounded injunction.

The clinical record establishes explained advantages in identified circumstances, not controlled numerical comparisons or universal superiority. Other litigation reproduced in the appendix is not a Nebraska finding. The enactment's broad emergency definition, section 3's narrower life exception and the same life-necessity hearing criterion remain distinct. No binding Nebraska high-court construction, new certification procedure or separate fee issue is assumed from the merits record.
'''

record=kernel+holdings+continuity+departure_lines+annex_tail+judgment_source+event+holdings+tail
public=record.split('## Public Projection\n',1)[1]
headers=re.findall(r'^## (.+)$',public,re.M)
assert headers==['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes'],headers
internal=record.split('## Controlling holdings\n',1)[1].split('\n## Continuity and source status',1)[0].strip()
public_holdings=public.split('## Holdings\n',1)[1].split('\n## Precedent Treatment\n',1)[0].strip()
assert internal==public_holdings
lengths=[len(x.split()) for x in re.findall(r'\*\*Controlling explanation:\*\* (.*?)(?=\n\n###|\Z)',holdings,re.S)]
assert len(lengths)==4 and max(lengths)<=350,lengths
assert framework in public_holdings
assert not re.search(r'(?i)\b(?:simulation|simulated|user-directed|workflow|git|sha-256|reconciliation|frozen|commitment|operator|model|fallback)\b',public)
missing=[x for x in re.findall(r'\]\(([^)]+)\)',record) if not x.startswith('https://') and not (path.parent/x.split('#')[0]).resolve().exists()]
assert not missing,missing
path.write_text(record,encoding='utf-8')
print({'record':str(path.relative_to(term)),'author':'Souter','judgment':'6 affirm; Kennedy vacate/remand; Scalia/Thomas reverse/remand','explanation_words':lengths,'eleven_blocks':True,'holdings_identical':True,'framework_copy_exact':True,'judgment_source_copy_exact':True,'relative_links_resolve':True})
