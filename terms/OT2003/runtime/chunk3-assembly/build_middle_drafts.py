from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
stone = (ROOT / 'runtime/OT_2003CHUNK3_STONE.md').read_text(encoding='utf-8-sig')
ALL = "Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer"
ASSOCIATES = "Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer"

def source_section(number):
    return re.search(r'(?ms)^## '+str(number)+r'\. .*?(?=^## \d+\. |\Z)', stone)[0].strip()

def audit_source(key):
    text = (ROOT / f'freeze/OT_2003CHUNK3_{key}_RECONCILED.md').read_text(encoding='utf-8-sig')
    first = text.split('## Preserved frozen commitment text')[0]
    comp = re.search(r'(?ms)^## (?:Comparator reconciliation|Full-opinion reconciliation|Full-opinion comparison|Full-opinion and footnote comparison|Historical comparison and operative legal differences)\n.*?(?=^## |\Z)', first)[0]
    rows = re.search(r'(?ms)^\| Justice \|.*?(?=\n\n|\Z)',text)[0]
    return comp.strip()+'\n\n### Frozen Justice-specific grounds and limits\n\n'+rows.strip()

def record(number, key, slug, case, date, result, kernel, compatibility, form, public):
    out = f'''**Case and dockets:** {case}
**Event and date:** Merits decision; {date}; October Term 2003, chunk 3.
**Result:** {result}
**Version / lineage:** Initial adjudication; supersedes no completed event.

## Decision kernel

{kernel.strip()}

**Participation and authority:** {ALL} participate at merits submission and decision. No case-specific nonparticipation is supplied. Nine participating Justices constitute a quorum; five votes suffice for an ordinary judgment and a controlling proposition. The supplied inventory places this matter before the Court for merits review. No new grant, argument date, filing or jurisdictional event is inferred.

**Research cutoff:** {date}. The applicable A or B entering-law slice, frozen neutral packet, preflight and reconciled conclusions supply the factual and legal baseline. Their supported published recitations are used at their stated scope; assembly has not independently read the complete petition, briefs and appendix and makes no such claim. The completed TWA and Concrete Works public projections precede this event and supply no change to the governing propositions here. Same-date matters share the preceding legal baseline and supply no rule to one another. Any earlier event completed during this Run must be screened before final commitment.

## Approved Chief Justice position and final compatibility

{compatibility.strip()}

### Exact approved Section II source

The following source section is copied mechanically from the approved runtime supplement. It remains internal and supplies no separate public account.

{source_section(number)}

## Form, judgment and opinions

{form.strip()}

{{{{ASSIGNMENT}}}}

## Controlling law and continuity

The complete controlling rules, proposition-level authority, explanations, precedent treatment and mandate are stated in the bounded Public Projection below and are the Record's controlling-holding account. No separate writing has a substantive function beyond the identified joins. Ordinary application to later facts is governed by the stated rules; record-specific work on remand and genuine questions outside review are identified separately rather than described collectively as unsettled law.

## Adaptive audit annex

**Frozen authority:** `terms/OT2003/freeze/OT_2003CHUNK3_{key}_RECONCILED.md` controls the eight Associate conclusions and their grounds. The following reconciliation account and Justice-specific rows are copied mechanically from that final handoff. Historical authorship is not an assignment input. No frozen commitment changes in this draft.

{audit_source(key)}

{{{{AUDIT}}}}

## Sources and validation status

The authorized neutral matter {number}, A/B preflight, applicable entering-law slice, final reconciled handoff and approved Section II were compared. Judgment and proposition arithmetic, remedy consistency, Chief fixed-core fidelity and the Section 8 complete-resolution/negative-statement rule were checked at draft stage. The exact sources and bounds of prior research remain in the frozen preflight and reconciliation. No independent grants, defaults, merits facts or post-cutoff law were added. Final assignment, later-written earlier-event screening, mechanical projection checks and term validation remain for finalization; this draft is not a completed Record.

## Public Projection

{public.strip()}
'''
    (OUT / (slug+'_draft.md')).write_text(out, encoding='utf-8', newline='\n')

record(27,'NEBRASKA_EPA','nebraska_v_epa',
       'Nebraska v. Environmental Protection Agency; D.C. Circuit No. 01-1101; judgment below, 331 F.3d 995.',
       '2004-01-08','Affirm denial of the petition on the facial constitutional claims and preserve the rule-specific nonpresentation disposition, 9–0.',
       '''The D.C. Circuit denied Nebraska and the City of Alliance's petition challenging the Safe Drinking Water Act and EPA's arsenic regulation. The questions are facial Commerce Clause validity of noncommunicable-contaminant regulation and whether operational duties on publicly owned utilities commandeer state government. Petitioners also seek to reopen rule-specific objections they did not present to EPA; the record includes their waiver concession. EPA could consider implementation and the supporting evidence even though it could not invalidate Congress's statute.

The Act governs public and private water systems, including actual interstate supply and sales. The January 2001 arsenic rule sets .01 mg/L with compliance in 2006. The record establishes the commercial and interstate connection for valid applications, not facts about an absent wholly local system. The direct-sale mechanism supplies the constitutional ground; Holston, Ho and Deaton retain their distinct production, renovation and waterway mechanisms. The Court resolves the facial claims and leaves denial of review in place, with the rule's existing compliance schedule.''',
       '''Stone-Zsela expressly votes to affirm both facial grounds and leave the preservation disposition intact. He directly joins the commercial-water and public-operator holdings, their application, the denial of the requested injunction and the existing compliance schedule. His approved supplement does not state the Associates' independent rationale distinguishing agency presentation of a facial statutory claim from regulatory implementation objections. He therefore concurs in that component's judgment without joining its explanation or adding a ground. The standing fallback is unused because his disposition is expressly supplied.

The Chief's own-activity distinction, connection-before-magnitude ground, facial scope and rejection of a new deadline or sanction are preserved. His caution against adjudicating absent systems is honored by the facial holding and by not inventing an as-applied controversy. The opinion does not publish an unnecessary catalogue of absent systems or enforcement disputes.''',
       f'''Form is selected before author counts: one signed opinion after full merits submission, stating three related but distinct grounds for the same denial of review. The first two constitutional propositions have nine direct joins. The preservation explanation has the eight Associate joins and the Chief's judgment-only agreement. No separate writing is needed to restate that relationship. A single eligible Associate can carry the entire opinion; the parts are dictated by the legal questions, not by balance.

| Judgment component | Disposition | Supporting Justices | Opposing Justices |
|---|---|---|---|
| Facial Commerce Clause claim | Affirm denial | {ALL} | None |
| Anti-commandeering claim | Affirm denial | {ALL} | None |
| Unpreserved rule-specific objections | Leave nonpresentation disposition intact | {ALL} | None |

| Lead portion | Author | Direct rationale joins | Relationship |
|---|---|---|---|
| I–II: interstate commodity and public-operator rules | {{{{AUTHOR}}}} | All nine, including the author | Opinion of the Court |
| III: rule-specific preservation | {{{{AUTHOR}}}} | All eight Associates, including the author | Opinion of the Court; Stone-Zsela concurs in this judgment only |

The eight Associates are eligible for the complete lead. Stone-Zsela's preservation disposition supplies no complete-rationale eligibility. Fit concerns precise separation of direct commerce, sovereign compulsion and agency presentation; O'Connor and Scalia have especially direct prior work on the own-activity boundary, while any eligible pool member can express the complete common ground.''',
       f'''## Event

**Nebraska v. Environmental Protection Agency.** D.C. Circuit No. 01-1101; judgment below, 331 F.3d 995. Decided January 8, 2004, on merits submission. The Court reviews denial of Nebraska and the City of Alliance's petition challenging the Safe Drinking Water Act's regulation of noncommunicable contaminants and EPA's arsenic rule. The questions are whether the statute is facially invalid under the Commerce Clause and whether compliance duties on States and municipalities as water-system owners impermissibly commandeer them.

The Act directs EPA to set maximum contaminant levels for public water systems. The January 2001 rule sets arsenic at .01 mg/L, with compliance in 2006. Covered providers include public and private utilities and systems supplying water across state boundaries. Petitioners presented none of their current objections during rulemaking and conceded waiver of rule-specific objections.

## Participation

Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated in submission and decision.

## Public Action

The judgment denying the petition for review is affirmed.

## Judgment & Remedy

**Affirmed, 9–0, on all reviewed components. Supporting:** {ALL}.

Denial of relief on the facial Commerce Clause and anti-commandeering claims and the disposition of the unpreserved regulatory objections remain in force. The requested injunction against the statute or arsenic rule is denied. The existing rule governs covered providers according to its terms and its 2006 compliance schedule.

## Opinion Topology

{{{{AUTHOR}}}} delivered the opinion of the Court, in which {{{{OTHER_JOINERS}}}} joined. STONE-ZSELA, C. J., joined Parts I and II and concurred in the judgment on Part III without adding a ground.

| Portion | Direct rationale support | Relationship |
|---|---|---|
| I: interstate commercial-water regulation; II: public-operator compliance | All nine Justices | Opinion of the Court |
| III: preservation of rule-specific objections | {ASSOCIATES} | Opinion of the Court; Stone-Zsela agrees in the judgment |

## Holdings

**Authority for Holdings 1 and 2:** Parts I and II of {{{{AUTHOR}}}}'s opinion, joined by every other participating Justice. **Authority for Holding 3:** Part III of the same opinion, joined by all eight Associate Justices; Stone-Zsela concurs in that component's judgment.

**1. Congress may regulate the safety of drinking water sold in interstate utility commerce.** The sale and interstate supply of drinking water provide a direct commercial connection for federal contaminant standards, and noncommunicability of the contaminant does not remove that connection. Because the challenged statute validly reaches these interstate utility transactions, petitioners' facial claim that Congress lacks authority to regulate noncommunicable contaminants fails.

Lopez requires identification of the regulated class and its constitutional connection before aggregate magnitude can establish federal power. The water transactions here supply that connection themselves: Congress regulates the safety of the commodity sold across state boundaries. The objection that distribution often occurs locally and arsenic is not contagious does not answer those valid applications. Home Builders requires a supported mechanism fitted to the actual regulated class; it does not turn its distinct intrastate mechanisms into exclusive routes for regulating interstate commerce. The facial claim is therefore fully resolved by the established commercial applications.

**2. Valid operational standards may govern public water suppliers.** A federal law may regulate States and municipalities as operators of covered water systems without compelling them to enact federal policy or enforce federal rules against unrelated persons. Work and expense required to bring the government's own operation into compliance do not alone constitute commandeering; these operational duties are valid.

Condon distinguishes federal regulation of a State's own covered activity from conscription of its sovereign machinery. That distinction controls because the Act imposes contaminant duties on public and private suppliers as suppliers. New York prohibits a compulsory legislative program or the substitute assumption of private obligations, and Printz prohibits compelled state execution of a federal regulatory program directed at private persons. Neither prohibition is triggered merely because public employees must operate their own utility in conformity with federal safety standards. Public ownership does not transform those standards into a command to govern others.

**3. The facial statutory claim does not excuse the actual failure to present regulatory objections.** EPA's inability to invalidate its governing statute permits judicial consideration of the facial constitutional claim, but does not excuse nonpresentation of objections to the agency's own implementation that it could meaningfully address. On petitioners' actual nonpresentation and waiver concession, the rule-specific objections remain unpreserved.

Petitioners' futility argument treats two different agency functions as one. EPA could not strike down Congress's enactment, but could consider the proposed regulatory implementation, interpret its mandate and develop the evidentiary record. The preserved facial challenge accordingly supplies no route to reopen the scientific selection of the arsenic level. This ruling applies the actual preservation record, rather than imposing a universal presentation requirement on all constitutional claims.

## Precedent Treatment

- **United States v. Lopez:** Applied for an identified constitutional connection before magnitude; direct interstate commodity regulation supplies that connection here.
- **National Association of Home Builders v. Babbitt:** Applied for a supported mechanism fitted to the enacted class; its distinct intrastate routes do not restrict direct regulation of interstate sales.
- **Reno v. Condon:** Applied to public operators' own compliance duties; the operational and sovereign-enforcement distinction controls.
- **New York v. United States:** Distinguished because the statute regulates operation of a utility rather than commanding state legislation or assumption of private obligations; its structural prohibition retains force.
- **Printz v. United States:** Distinguished because the Act assigns no compelled state enforcement program against unrelated persons; its prohibition retains force.

## Law After Decision

Federal drinking-water safety standards may govern interstate utility sales and public suppliers' own operations on the grounds stated. The facial challenge cannot invalidate those applications. The denial of rule-specific review leaves EPA's arsenic standard and scheduled compliance requirements operative, while the actual-burden distinction between operator compliance and compelled government of others remains controlling.

## Separate Writings

## Procedure After Action

The petition for review remains denied. EPA may administer the arsenic rule, and covered providers remain subject to its existing 2006 compliance schedule.

## Source Notes

331 F.3d 995; Safe Drinking Water Act, 42 U.S.C. §§300f, 300g-1; U.S. Const., Art. I, §8, and Amdt. 10. The interstate utility applications and the actual agency-presentation record supply the bases for this facial and procedural decision.
''')

record(28,'EDWARDS','sec_v_edwards',
       'SEC v. Edwards; No. 02-1196; 540 U.S. 389.',
       '2004-01-13','Reverse and remand, 9–0, rejecting fixed return and contractual entitlement as categorical exclusions from the investment-contract definition.',
       '''The Eleventh Circuit reversed preliminary relief in the SEC's enforcement action because investors were promised fixed contractual payments. The granted question asks whether such a return can satisfy the federal investment-contract definition. Investors purchased payphones and could lease them back to the affiliated promoter, which selected sites and operated the equipment. The SEC alleged insufficient operating income and use of later investors' money for payments. Those remain allegations at the reviewed preliminary/dismissal posture.

The categorical question embraces both expected profits and reliance on others' efforts. The whole promoted arrangement must be evaluated under Howey, Forman and the securities statutes. Zandford separately preserves the actual violation elements and ordinary proof and remedies. Reversal requires reconsideration of classification and relief under the correct definition; the court below performs the remaining application and enforcement work.''',
       '''Stone-Zsela expressly supports reversal, both definitional rules, assessment of the complete promoted arrangement, the SEC's continuing burden to establish each element under the applicable procedural standard, and the bounded enforcement remand. He joins every governing proposition and the remedy. The opinion's distinction between an enforceable obligation and the managerial activity furnishing payment directly implements his approved reasoning. It leaves classification, preliminary protection and ultimate enforcement to their ordinary requirements. No fallback, separate writing or additional factual finding is needed.''',
       f'''Form is selected before author counts: one signed unanimous opinion after plenary merits submission. A single investment-contract definition resolves the two interrelated categorical errors; there is no basis for per curiam treatment, dividing authorship or generating a separate opinion. All nine Justices join every proposition and the full remand.

| Judgment component | Disposition | Supporting Justices | Opposing Justices |
|---|---|---|---|
| Fixed-return and contractual-entitlement exclusions | Reverse and remand | {ALL} | None |

| Writing | Author | Joins | Scope |
|---|---|---|---|
| Opinion of the Court | {{{{AUTHOR}}}} | {{{{OTHER_JOINERS}}}} | Complete definition, application and remand |

All nine Justices are eligible. Fit concerns faithful statutory categories, whole-arrangement analysis and separation of classification from proof and remedy; Scalia's adopted Zandford opinion and Ginsburg's integrated-transaction ground offer particularly direct demonstrated fits, subject to the actual balance pool. Stone-Zsela supports the same ground fully but has no distinct accommodation necessary to preserve unanimity.''',
       f'''## Event

**SEC v. Edwards.** No. 02-1196. Decided January 13, 2004, on merits submission. The Court reviews the Eleventh Circuit's reversal of preliminary relief in the SEC's enforcement action. The question is whether a promoted investment arrangement promising a fixed contractual return can be an investment contract under the federal securities laws.

Investors purchased payphones and could lease them back to an affiliated enterprise that selected sites, operated the equipment and promised a fixed annual return. The SEC alleges that operating income was insufficient and later investor funds supplied payments. Those allegations are accepted for the reviewed dismissal question rather than treated as final findings.

## Participation

Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated in submission and decision.

## Public Action

The judgment is reversed and the case remanded.

## Judgment & Remedy

**Reversed and remanded, 9–0. Supporting:** {ALL}.

The Eleventh Circuit's categorical investment-contract exclusions are rejected. The lower courts must reconsider the securities classification and requested enforcement relief under the complete investment-contract test and the applicable proof and remedial requirements.

## Opinion Topology

{{{{AUTHOR}}}} delivered the opinion of the Court, in which {{{{OTHER_JOINERS}}}} joined.

The complete opinion, definition, application and remand have nine direct joins.

## Holdings

**Authority:** {{{{AUTHOR}}}}'s opinion for a unanimous Court, joined by every other participating Justice.

**A fixed contractual return can be investment profit under Howey.** An investment contract may promise a fixed return: expected income from committed capital qualifies as profit, and a contractual right to payment does not itself eliminate reliance on the entrepreneurial or managerial efforts supplying that return. The SEC must establish an investment of money in a common enterprise with the required expectation of profits from others' efforts, assessed through the complete offered arrangement; these payphone arrangements cannot be excluded merely because the yield is fixed or contractually enforceable.

Howey examines the economic arrangement as a whole, including services offered with the property. Forman distinguishes investment income from a benefit bought for personal use. Its references to appreciation and participation in earnings illustrate that distinction; they do not exhaust the forms investment income may take. A fixed return is still income sought by committing capital to another's undertaking.

The contractual-entitlement argument confuses the duty to pay with the economic activity making payment possible. A promise establishes what the promoter owes, but does not generate the money needed to honor it. The equipment purchase, leaseback and operating services must therefore be considered together when evaluating dependence on management. Ownership of a tangible payphone alone does not answer that inquiry.

Reves's isolated suggestion concerning Forman's examples supplies no fixed-return exception to Howey. Its treatment of the separately listed note category retains its distinct function. Zandford requires the actual securities-law elements and operative connection, keeping correction of a categorical legal error separate from proof of a violation. On remand the lower courts must apply all investment-contract elements to the arrangement, determine any remaining violation allegations and assess requested preliminary or final relief under the governing standards.

## Precedent Treatment

- **SEC v. W. J. Howey Co.:** Applied to the whole promoted property-and-services arrangement; expected profits include fixed investment income.
- **United Housing Foundation v. Forman:** Applied for the investment-versus-consumption distinction; its examples do not establish a fixed-income exclusion.
- **Reves v. Ernst & Young:** Its suggestion that Forman's examples exhaust investment profits is rejected as noncontrolling dictum; the distinct test for the note category remains in force.
- **SEC v. Zandford:** Applied to preserve proof of the enacted securities elements and ordinary remedial requirements after correction of a categorical legal error.

## Law After Decision

Fixed and variable investment returns receive the same Howey inquiry. Courts evaluate the complete arrangement and its dependence on others' managerial efforts, while requiring proof of the remaining investment-contract elements and any asserted statutory violation. A contractual guarantee supplies no categorical exemption from that inquiry.

## Separate Writings

## Procedure After Action

The case returns for application of the corrected investment-contract definition and adjudication of the remaining enforcement and preliminary-relief questions. The SEC bears the applicable burdens for securities classification, a violation and each remedy sought.

## Source Notes

Securities Act §2(a)(1), 15 U.S.C. §77b(a)(1); Securities Exchange Act §3(a)(10), 15 U.S.C. §78c(a)(10); Howey, 328 U.S. 293; Forman, 421 U.S. 837; Reves, 494 U.S. 56. The allegation that later investments supplied payments remains an allegation at this posture.
''')

record(31,'FREW','frew_v_hawkins',
       'Frew v. Hawkins; No. 02-628; 540 U.S. 431.',
       '2004-01-14','Reverse the categorical immunity ruling and remand for decree enforcement and the remaining compliance and remedial work, 9–0.',
       '''Texas Medicaid beneficiaries brought a federal challenge concerning early and periodic screening, diagnostic and treatment services. After state agencies were dismissed, the responsible officials entered a detailed implementation decree. The district court later found noncompliance and directed corrective measures. The Fifth Circuit reversed enforcement on the premise that every decree violation must itself constitute a fresh violation of the Medicaid statute.

The question is prospective enforceability against the bound officials of a lawful decree resolving a federal dispute and furthering federal objectives, including implementation terms beyond the statute's general commands. Young and the adopted Verizon Maryland prospective-officer rule supply the enforcement channel; Firefighters supplies the scope of lawful consent relief; Rufo supplies continuing obligation and modification requirements. The class seeks prospective compliance, not accrued treasury compensation. The lower courts retain their ordinary task of reviewing actual compliance findings and appropriate corrective measures. Any supported modification motion must satisfy Rule 60(b)(5).''',
       '''Stone-Zsela votes to reverse and remand, directly joining the complete enforcement and modification rules. His approved practical relief requires a concrete compliance schedule addressing established failures, evidence of performance and lawful enforcement upon noncompliance. The common mandate incorporates that direction after ordinary review of the actual compliance findings and remedies, rather than making a new Supreme Court finding about which disputed details are established. The class-wide decree remains the obligation: officials must demonstrate that any proposed narrower corrective measure fully cures a proved breach. A properly supported Rule 60(b)(5) request must be decided under Rufo; unilateral noncompliance and indefinite unnecessary supervision are both inconsistent with the controlling framework.

Those directions implement the frozen Associates' shared ground that actual compliance, corrective measures and modification are remand work under established rules. They create no new remedial entitlement outside the decree or burden on unrelated conduct. The Chief joins every proposition and the mandate; the standing fallback is unused. The immunity question is resolved through the sufficient prospective-officer ground. General abrogation and waiver theories add no holding or separate-writing function.''',
       f'''Form is selected before author counts: one signed unanimous opinion after plenary review, with a prospective-enforcement holding and its distinct continuing-obligation/modification rule. Their legal relationship permits a single author and complete joins; no negotiation history or separate writing is invented.

| Judgment component | Disposition | Supporting Justices | Opposing Justices |
|---|---|---|---|
| Categorical Eleventh Amendment bar to federal decree enforcement | Reverse and remand | {ALL} | None |

| Writing | Author | Joins | Scope |
|---|---|---|---|
| Opinion of the Court | {{{{AUTHOR}}}} | {{{{OTHER_JOINERS}}}} | Both controlling propositions and complete compliance/remedial mandate |

All nine Justices are eligible. Fit concerns the boundary between prospective officer relief and immunity, lawful implementation beyond statutory minima, and disciplined supervision/modification. Thomas's adopted Verizon Maryland Part III and Stone-Zsela's adopted Rufo authorship provide particularly direct demonstrated fits. Kennedy and Souter fully joined the operative Rufo rules and supply strong alternatives for coordinating enforcement with return of administrative responsibility. No expansion accommodation is required; final choice depends on the actual balance pool.''',
       f'''## Event

**Frew v. Hawkins.** No. 02-628. Decided January 14, 2004, on merits submission. The Court reviews the Fifth Circuit's reversal of enforcement relief for a federal Medicaid consent decree. The question is whether the Eleventh Amendment bars prospective enforcement against state officials when lawful implementation terms are more detailed than the statute itself.

Texas Medicaid beneficiaries challenged the administration of early and periodic screening, diagnostic and treatment services. After the state agencies were dismissed, the officials entered a detailed consent decree resolving the federal dispute. The district court later found failures to comply and directed corrective measures. The Fifth Circuit required each alleged decree violation to establish a new, independent statutory violation.

## Participation

Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated in submission and decision.

## Public Action

The judgment is reversed and the case remanded.

## Judgment & Remedy

**Reversed and remanded, 9–0. Supporting:** {ALL}.

The categorical immunity bar is rejected. The decree remains an enforceable federal judicial obligation, and the case returns for review of the actual compliance findings and remedial issues and for effective prospective enforcement under the standards below.

## Opinion Topology

{{{{AUTHOR}}}} delivered the opinion of the Court, in which {{{{OTHER_JOINERS}}}} joined.

Both controlling holdings and the complete mandate have nine direct joins.

## Holdings

**Authority for both holdings:** {{{{AUTHOR}}}}'s opinion for a unanimous Court, joined by every other participating Justice.

**1. Lawful federal implementation terms are prospectively enforceable against the bound officials.** A federal court may enforce a consent decree against state officials when it resolves a dispute within federal subject-matter jurisdiction, stays within the general scope of the pleadings and furthers the governing federal law's objectives. Lawful implementation terms may be more specific than the statute and need not each independently repeat an enforceable statutory command; the party seeking enforcement must establish the operative decree and noncompliance under the applicable standards.

Ex parte Young and Verizon Maryland permit prospective relief against responsible officials enforcing federal obligations. Firefighters recognizes that a consent decree may prescribe lawful relief beyond what a contested liability judgment alone would require. The Medicaid decree meets the federal-origin and federal-purpose requirements here. Once entered, its lawful implementation terms become judicial obligations rather than optional methods officials may discard.

Texas's proposed term-by-term statutory-minimum condition would make those implementation terms unenforceable precisely where they perform their agreed remedial work. Rufo treats an operative decree as binding until lawfully altered. State administrative discretion is protected through the decree's federal scope and lawful modification, rather than by treating accepted details as immune from enforcement. Pennhurst continues to exclude independent state-law commands, and Edelman preserves the boundary against retrospective compensation from the State. This decree and the class's prospective compliance request remain within those boundaries.

**2. Modification and termination follow the decree's purposes and Rule 60(b)(5).** Officials seeking modification must prove a significant change in facts or law making continued enforcement inequitable; any modification must be suitably tailored to that change while preserving lawful protection of the decree's remaining purposes. Actual anticipation and acceptance of the relevant risk impose a heavy burden, and dissatisfaction, a new administration or a cheaper lawful alternative alone is insufficient; judicial supervision should end when the decree's obligations and legitimate remedial purposes have been satisfied.

Rufo supplies both the required showing and the tailoring rule. It permits practical adjustment without reducing every negotiated obligation to the bare statutory or constitutional minimum. The decree is a means to secure an effective, durable remedy, so continued federal supervision must remain tied to its obligations and purposes. Completion restores ordinary administrative responsibility; an assertion that completion occurred must be assessed on the actual record. The availability of modification does not permit officials to disregard operative duties while seeking different terms. Enforcement and modification therefore remain distinct judicial tasks under the same continuing decree.

## Precedent Treatment

- **Ex parte Young:** Applied as the prospective-officer route for enforcing the lawful federal obligation.
- **Verizon Maryland v. Public Service Commission:** Applied for prospective relief against responsible officials and the distinction from retrospective State compensation.
- **Local No. 93, International Association of Firefighters v. Cleveland:** Applied to consent relief within federal jurisdiction, the pleadings' general scope and the federal law's objectives, including lawful implementation beyond minimum contested relief.
- **Rufo v. Inmates of Suffolk County Jail:** Applied to the decree's continuing obligation, significant-change and accepted-risk requirements, and tailored modification preserving remaining lawful purposes.
- **Pennhurst State School and Hospital v. Halderman:** Its prohibition on independent state-law enforcement against officials is preserved; these obligations implement the federal dispute.
- **Edelman v. Jordan:** Its retrospective State-compensation limit remains effective; the relief sought here is prospective decree compliance.

## Law After Decision

Federal implementation decrees meeting the stated jurisdictional, pleading-scope and federal-purpose conditions bind the responsible officials beyond a word-for-word repetition of the underlying statute. Courts enforce their lawful prospective terms, assess actual noncompliance and tailor corrective relief to the decree's purposes. Officials may obtain modification on Rufo's required showing, and unnecessary supervision ends when the obligations and legitimate purposes have been satisfied.

## Separate Writings

## Procedure After Action

The lower courts must review the actual compliance findings and remedial issues under their ordinary standards. For established failures, the district court must enter or restore a concrete compliance schedule, require evidence of performance and use lawful enforcement if officials fail to comply. Relief implements the existing class-wide obligation; officials proposing a narrower corrective measure must establish that it fully cures the proved breach. The court must also decide any properly supported Rule 60(b)(5) request under the significant-change and tailoring requirements. The decree remains operative until lawfully altered or its satisfied obligations warrant termination.

## Source Notes

42 U.S.C. §§1396a(a)(43), 1396d(r); Federal Rules of Civil Procedure 60(b)(5) and 65; Eleventh Amendment; Firefighters, 478 U.S. 501; Young, 209 U.S. 123; Pennhurst, 465 U.S. 89; Edelman, 415 U.S. 651. The decree resolves a federal dispute and furthers the Medicaid program's objectives. Existing compliance findings and the corresponding corrective measures remain subject to ordinary lower-court review.
''')

record(32,'KONTRICK','kontrick_v_ryan',
       'Kontrick v. Ryan; No. 02-819; 540 U.S. 443.',
       '2004-01-14','Affirm the Seventh Circuit and leave the denial of discharge in force, 9–0.',
       '''The Seventh Circuit affirmed denial of Kontrick's discharge and rejection of his postmerits timeliness objection. After extensions of the original deadline, Ryan amended his discharge objection to add the family-account theory without obtaining a further extension. Kontrick answered and contested the merits through an adverse adjudication before asserting that the bankruptcy court lacked subject-matter jurisdiction. Untimeliness is conceded for the granted question.

Sections 1334 and 157 confer statutory competence over bankruptcy and discharge objections. Section 2075 and Rule 9030 limit the jurisdictional effect of procedural rulemaking. Rules 4004 and 9006 regulate filing and enlargement. Carlisle distinguishes mandatory procedural authority from jurisdiction and reserved forfeiture; Henderson requires attention to source, placement and function. Castro's recharacterization warning concerns a court changing a litigant's procedural vehicle, unlike this omitted defense to a knowingly litigated claim. The actual denial of discharge remains effective.''',
       '''Stone-Zsela joins the nonjurisdictional classification and the postmerits forfeiture rule, the continued force of timely invoked procedural limits, the creditor's ordinary proof burden and the affirmance. The decision grants no equitable extension: it recognizes loss of an unasserted defense after adjudication of the claim. The Chief's exact limitation concerning forbidden extensions when a timely objection is made is expressed in the controlling rule. Equitable tolling, relation back and the precise last permissible premerits assertion point lie outside the granted postmerits question. His entire fixed core is preserved; no fallback or separate writing is required.''',
       f'''Form is selected before author counts: one signed unanimous opinion after plenary review resolves the relationship between congressionally conferred jurisdiction, mandatory national rules and forfeiture at the specified procedural stage. That doctrinal clarification supplies the form independently of counts. All nine Justices join the entire holding and final judgment.

| Judgment component | Disposition | Supporting Justices | Opposing Justices |
|---|---|---|---|
| Postmerits invocation of bankruptcy filing defense | Affirm; discharge denial stands | {ALL} | None |

| Writing | Author | Joins | Scope |
|---|---|---|---|
| Opinion of the Court | {{{{AUTHOR}}}} | {{{{OTHER_JOINERS}}}} | Jurisdiction, forfeiture, operative qualification and affirmance |

All nine Justices are eligible. Scalia's adopted Carlisle and Henderson opinions provide an especially direct fit for the source/function distinction and consistent treatment of a mandatory rule. Ginsburg's precise separation of statutory competence and procedural defense is also directly supported; Stone-Zsela's approved authority/procedure distinction is fully compatible without a special expansion role. The final assignment must use the actual balance pool.''',
       f'''## Event

**Kontrick v. Ryan.** No. 02-819. Decided January 14, 2004, on merits submission. The Court reviews the Seventh Circuit's affirmance of denial of discharge and rejection of Kontrick's postmerits timing objection. The question is whether Bankruptcy Rules 4004 and 9006 impose a subject-matter jurisdictional limit that survives an adverse merits adjudication, or a procedural defense forfeited by failing to invoke it before that adjudication.

Ryan amended his objection to discharge to allege fraudulent family-account transfers after extensions of the filing deadline and without a further extension. Kontrick answered the theory and contested summary judgment on the merits. Only after the court decided the claim against him did he assert untimeliness. The amendment's untimeliness is conceded for the question before the Court.

## Participation

Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated in submission and decision.

## Public Action

The judgment is affirmed.

## Judgment & Remedy

**Affirmed, 9–0. Supporting:** {ALL}.

The postmerits timing defense is forfeited. The adjudicated denial of discharge remains in force.

## Opinion Topology

{{{{AUTHOR}}}} delivered the opinion of the Court, in which {{{{OTHER_JOINERS}}}} joined.

The complete rule, application and affirmance have nine direct joins.

## Holdings

**Authority:** {{{{AUTHOR}}}}'s opinion for a unanimous Court, joined by every other participating Justice.

**A debtor forfeits this filing defense by first raising it after the claim is adjudicated on the merits.** Bankruptcy Rules 4004 and 9006 regulate claim processing and enlargement rather than subject-matter jurisdiction; a debtor who litigates an objection to discharge through an adverse merits determination before raising untimeliness forfeits that defense. The creditor retains the burden to prove the discharge objection, and the rules' restrictions continue to govern when the debtor timely invokes them; forfeiture supplies no power to grant an extension the rules forbid over a timely objection.

Congress conferred jurisdiction over bankruptcy proceedings through 28 U.S.C. §§1334 and 157, including objections to discharge under §157(b)(2)(J). Section 2075 and Rule 9030 prevent procedural rules from enlarging or restricting that jurisdiction. Rule 4004 generally requires an objection within sixty days after the first date set for the creditors' meeting and permits an extension for cause on a motion filed before the period expires. Rule 9006(b)(3) confines enlargement to the conditions Rule 4004 permits. Those provisions regulate the orderly assertion of claims and defenses; they do not make an omitted procedural defense a perpetual challenge to statutory competence.

Carlisle enforced a timely invoked national-rule deadline while distinguishing remedial authority from jurisdiction and leaving forfeiture open. Henderson likewise examines the source, placement and function of a timing command. Here the separate jurisdictional statutes and procedural rules make the distinction clear. Kontrick's strict-enlargement argument concerns the court's authority to extend a deadline over a timely objection, which differs from a debtor's ability to insist on an unraised defense after losing on the merits. He answered the family-account theory and litigated it through judgment. That conduct forfeited the timing defense without a finding that he intentionally surrendered it or an equitable extension of the deadline.

Equitable tolling, relation back and the precise final point for asserting the defense before merits adjudication lie outside the accepted postmerits question. The rule decided here resolves Kontrick's attempt to undo the completed merits determination.

## Precedent Treatment

- **Carlisle v. United States:** Applied for the distinction between mandatory procedural limits and subject-matter jurisdiction. The present decision resolves postmerits forfeiture of this bankruptcy defense while preserving Carlisle's timely-objection holding.
- **Henderson v. United States:** Applied for classification of a timing command through its source, placement and function rather than a jurisdictional label; the different statutory timetable at issue there retains its own treatment.

## Law After Decision

The specified bankruptcy filing and enlargement rules remain mandatory procedural prescriptions, but their protection is lost when a debtor first invokes untimeliness after adjudication of the discharge objection's merits. Statutory subject-matter jurisdiction survives that filing defect, and a timely invoked objection continues to receive the rules' prescribed treatment.

## Separate Writings

## Procedure After Action

The denial of discharge stands, and the bankruptcy court may continue administering the estate with that judgment in force.

## Source Notes

28 U.S.C. §§1334, 157(b)(2)(J), 2075; Bankruptcy Rules 4004(a), 4004(b), 9006(b)(3), 9030. Untimeliness is conceded for review. The debtor litigated the family-account objection through an adverse merits determination before asserting the defense.
''')

record(33,'RUBIN','rubin_v_santa_monica',
       'Rubin v. City of Santa Monica; judgment below, 308 F.3d 1008.',
       '2004-01-15','Affirm dismissal on the granted municipal speech and equal-protection question, 9–0; the separate Secretary-of-State dismissal remains undisturbed outside that question.',
       '''Rubin qualified for the Santa Monica City Council ballot and proposed peace activist as his optional designation. The City applied a rule permitting specified office or principal professional, vocational or occupational descriptions while excluding generic status labels, including activist. The field allows no more than three words identifying the current principal work or that during the preceding calendar year. Candidates may also submit a separate statement of up to 200 words distributed at city expense. The Court accepts the properly pleaded livelihood allegations at the dismissal stage.

The constitutional controversy remains live because the election interval is too short for complete review and the supplied intended recurrence supports prospective relief. The grant concerns the municipal speech and equal-protection rule. The lower judgment separately dismissed the California Secretary of State because the State's regulation expressly excludes municipal elections and the City adopted it independently, without the Secretary's direction or encouragement. That separate dismissal remains undisturbed outside the granted municipal question. This preserves the lower judgment without a new Supreme Court standing disposition or a municipal merits judgment against the Secretary.

Burdick and Cartwright govern actual burden, precise interests and fit at the severe, substantial and ordinary levels. Timmons and Schrader protect official recognition of genuine nominations and truthful party identity. Van Susteren supplies a distinct ordinary-burden application without deciding this optional designation field. Cook's congressional Elections Clause source is not transferred to municipal elections.''',
       '''Stone-Zsela expressly joins affirmance of the granted municipal speech/equality challenge, the ordinary-burden classification under Cartwright, the genuine-neutrality and identifying-function conditions, acceptance of the alleged vocation and the prospective scope. His position permits actual political professions to qualify on the same neutral terms: the opinion sustains generic-status specificity, not exclusion because of a cause. It gives alternative communication its proper evidentiary weight without treating it as a cure for viewpoint discrimination.

The Secretary's independent dismissal receives no new holding. Section II does not supply a standing rationale against that defendant, but no such component is adjudicated by this Court: the narrower mandate expressly leaves the dismissal outside the granted municipal question undisturbed. The standing fallback is therefore unused rather than supplying an invented Chief rationale. All nine Justices directly join the complete opinion at its actual scope, with no separate writing necessary.''',
       f'''Form is selected before author counts: one signed unanimous opinion after plenary merits submission. The ordinary-burden rule and its municipal equal-protection application answer the related constitutional question together; the recurring controversy and granted-scope boundary support the stated prospective mandate. There is no separate Secretary merits holding or separate authoring part.

| Judgment component | Disposition | Supporting Justices | Opposing Justices |
|---|---|---|---|
| Granted municipal speech and equal-protection challenge | Affirm dismissal | {ALL} | None |

| Writing | Author | Joins | Scope |
|---|---|---|---|
| Opinion of the Court | {{{{AUTHOR}}}} | {{{{OTHER_JOINERS}}}} | Complete granted-question rule, application, scope and prospective disposition |

All nine Justices are eligible. Fit concerns applying the full calibrated scale without understating a truthful-identification interest, distinguishing genuine nomination from generic description, and preserving viewpoint neutrality. Souter's adopted Cartwright opinion and Stevens's adopted Schrader opinion are particularly direct grounds of fit; Thomas's adopted Van Susteren ordinary-burden analysis supplies another demonstrated fit. Stone-Zsela fully supports the same formulation, and no new accommodation or exceptional self-assignment rationale is necessary. Final choice must follow the actual balance pool.''',
       f'''## Event

**Rubin v. City of Santa Monica.** Judgment below, 308 F.3d 1008. Decided January 15, 2004, on merits submission. The Court reviews dismissal of the municipal speech and equal-protection challenge to a neutral rule restricting an optional ballot designation to specified office or principal professional, vocational or occupational identification. Rubin seeks declaratory and prospective relief permitting the designation peace activist.

Rubin qualified for the 2000 City Council ballot. The City declined his proposed generic status designation under its adopted rule, which includes activist among the excluded status labels. The field permits up to three words identifying the current principal profession, vocation or occupation or the principal one during the preceding calendar year. Candidates may submit a separately distributed statement of up to 200 words at city expense. The Court accepts the pleaded allegation that activism supplies Rubin's livelihood. The short election cycle and intended recurrence preserve the prospective controversy after the completed election.

## Participation

Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated in submission and decision.

## Public Action

The judgment is affirmed on the granted municipal constitutional question.

## Judgment & Remedy

**Affirmed on the municipal speech and equal-protection claims, 9–0. Supporting:** {ALL}.

The requested declaratory and prospective relief requiring the disputed designation is denied. The Secretary of State's separate dismissal remains undisturbed outside the granted municipal question. The completed election remains closed.

## Opinion Topology

{{{{AUTHOR}}}} delivered the opinion of the Court, in which {{{{OTHER_JOINERS}}}} joined.

The complete granted-question rule, application and prospective disposition have nine direct joins.

## Holdings

**Authority:** {{{{AUTHOR}}}}'s opinion for a unanimous Court, joined by every other participating Justice.

**A neutral generic-status exclusion may govern this optional identification field.** A government may reserve an optional ballot designation for defined official or occupational identification and exclude generic political status descriptions when the consistently applied rule is viewpoint neutral, imposes an ordinary burden and reasonably serves concise, intelligible and nonmisleading identification. The government must identify that purpose and fit; an otherwise qualifying profession may not be rejected merely because of the cause it advances. The challenged rule satisfies those conditions and defeats the presented speech and municipal equal-protection claims.

Burdick requires assessment of the actual burden against the precise regulatory interests and their fit. Cartwright identifies the complete scale: severe burdens require narrow tailoring to a compelling interest; substantial burdens require an important objective and a demonstrated substantial relationship to the restriction's actual reach; reasonable, nondiscriminatory ordinary burdens may be justified by important regulatory interests. The burden here is ordinary. Rubin remains a candidate, the field supplies optional identifying information, and the restriction withholds no genuine nomination or truthful party designation.

The classification is sustained on its actual function. Activist is a broad status describing many different activities, and the exclusion applies across causes. Accepting Rubin's allegation that activism is his livelihood does not require every general description of that livelihood to appear in a field reserved for more specific identification. Officials must apply that distinction without disfavoring peace advocacy or another viewpoint. The separate candidate statement reduces the practical burden but could not cure viewpoint discrimination.

Timmons and Schrader protect meaningful recognition of an actual party nomination or truthful party identity; other campaign opportunities alone cannot replace that recognition. This rule addresses a different field and supplies a reasonable identifying distinction. Van Susteren confirms that actual ordinary burdens receive meaningful, proportionate review. The same neutral functional distinction and burden assessment defeat the claim of unequal treatment between a generic status and qualifying office or occupational descriptions. Cook's prohibition on congressional-ballot policy penalties rests on a distinct constitutional source; this municipal rule imposes no comparable ideological penalty under the First and Fourteenth Amendment inquiry.

## Precedent Treatment

- **Burdick v. Takushi:** Applied for actual burden, precise interests and fit within the full ballot system.
- **Cartwright v. Barnes:** Applied at all three levels of its calibrated scale; this restriction falls at the ordinary level on its actual operation.
- **Timmons v. Twin Cities Area New Party:** Distinguished because the rule withholds no official recognition of a genuine party nomination; the meaningful-recognition holding remains in force.
- **Schrader v. Blackwell:** Distinguished because an optional generic status does not establish the truthful party identity protected there; its recognition rule and its rejection of alternative speech as an automatic substitute remain effective.
- **Van Susteren v. Jones:** Applied for meaningful review of an ordinary burden supported by an actual regulatory connection, while its primary-entry condition remains distinct from this designation rule.
- **Cook v. Gralike:** Distinguished at its congressional Elections Clause source and official policy-penalty scope; it supplies no authority for viewpoint-selective municipal administration.

## Law After Decision

Election officials may apply the reviewed neutral status rule to the optional designation field while permitting qualifying office and occupational identification. The rule's identifying function, actual ordinary burden and consistent treatment across viewpoints supply its constitutional justification. An official's rejection of a qualifying profession because of its cause would fail the neutrality condition of this rule.

## Separate Writings

## Procedure After Action

The municipal defense judgment stands, and officials may administer the sustained designation rule in future elections. Rubin retains the available candidate statement and ordinary campaign channels. The separate Secretary-of-State dismissal is undisturbed.

## Source Notes

Rubin v. City of Santa Monica, 308 F.3d 1008; California Elections Code §13107 and implementing designation regulations; U.S. Const., Amdts. 1 and 14. California's regulation expressly excludes municipal elections; Santa Monica adopted the rule independently. The Secretary's separate dismissal lies outside the granted municipal constitutional question. Rubin's pleaded livelihood facts are accepted at the dismissal stage.
''')
