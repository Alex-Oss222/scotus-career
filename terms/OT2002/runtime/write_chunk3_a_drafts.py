from pathlib import Path
import json
import re

BASE = Path('terms/OT2002')
OUT = BASE / 'runtime' / 'chunk3-drafts'
OUT.mkdir(exist_ok=True)
reconciled = (BASE / 'freeze/OT_2002CHUNK3_A_INITIAL_RECONCILED.md').read_text(encoding='utf-8-sig')
stone = (BASE / 'runtime/OT_2002CHUNK3_A_INITIAL_STONE.md').read_text(encoding='utf-8-sig')
neutral = (BASE / 'freeze/OT_2002CHUNK3_A_NEUTRAL.md').read_text(encoding='utf-8-sig')

ALL = ['Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']
SEVEN = [j for j in ALL if j not in ['Stone-Zsela', 'Stevens']]
all_names = ', '.join(ALL)
seven_names = ', '.join(SEVEN)

def section(text, heading, level=2):
    prefix = '#' * level + ' '
    start = text.index(prefix + heading)
    stop = text.find('\n' + prefix, start + len(prefix))
    return text[start:stop if stop >= 0 else len(text)].strip()

def write_case(d):
    frozen = section(reconciled, d['frozen_heading'])
    approved = section(stone, d['stone_heading'])
    intake = section(neutral, d['stone_heading'])
    internal = f'''**Case and dockets:** {d['name']}; {d['citation']}; no Supreme Court docket supplied.
**Event and date:** Merits decision; 2003-01-14; October Term 2002; chunk 3.
**Result:** {d['result']}
**Version / lineage:** Original decision.

## Event and chronology

{d['event']}

The event date is the approved calendar assignment, not a historical Supreme Court merits date. The supplied posture is submission for plenary merits review of the identified federal appellate judgment; no separate argument or submission date is established. The substantive entering-law cutoff is immediately before January 14, 2003. Other uncoordinated January 14 events do not supply substantive law to this event. Research cutoff: January 14, 2003; no later event is used.

## Participation and law entering

All nine Justices participate at submission and decision: {all_names}. No nonparticipation is identified. Nine participants satisfy quorum; five votes establish a majority. This is merits review of the identified federal appellate judgment on the supplied questions, not a newly invented petition, oral argument, or docket.

{d['entering']}

The frozen neutral packet and the selected entering-law copy identify the relevant authority. The selected copy is a reading aid; the underlying decisions control. The original neutral language is retained below as intake support, subject to the express clarification and reconciliation stated in this Record.

## Stone's approved position and final compatibility

{d['stone_analysis']}

The approved case-specific supplement is copied without alteration in the annex. No standing fallback is used. No controlled substantive choice is supplied by inference. No actual circulation history is asserted: the following is final formulation compatibility against the frozen commitments.

## Public judgment and remedy

{d['judgment']}

## Opinion form and final joins

{d['form']}

| Writing | Author | Joined by | Relationship and scope |
|---|---|---|---|
{d['opinion_rows']}

{d['join_audit']}

## Assignment

@@ASSIGNMENT@@

## Controlling holdings

{d['holdings']}

## Precedent treatment and present force

{d['precedents']}

## Law after decision

{d['law_after']}

## Continuity and remaining proceedings

{d['procedure']}

{d['continuity']}

## Sources and status

The case-specific reported appellate judgment supplies the lower-court history, statutory account, supported record facts and relief below. These propositions are preserved in the frozen neutral intake below; no unavailable original pleading is represented as read. The adopted reconciliation supplies the independent Justice-specific grounds and limits. The selected entering-law reading copy supplies the holdings and proposition-level joins of the earlier controlling decisions. These sources establish the stated legal paths without inventing new trial findings or party concessions.

Source-to-fact map: {d['source_map']}

Authoritative assembly handoffs: terms/OT2002/freeze/OT_2002CHUNK3_A_INITIAL_RECONCILED.md; terms/OT2002/freeze/OT_2002CHUNK3_A_NEUTRAL.md; terms/OT2002/entering-law/OT_2002CHUNK3_A_SELECTED.md; terms/OT2002/runtime/OT_2002CHUNK3_A_INITIAL_STONE.md. {d.get('extra_source','')}

No Supreme Court historical merits comparator exists for this added review. The circuit's result establishes the judgment below, not any Justice's vote, author or join. The change or preservation of that lower judgment is not a Justice-specific historical departure. The present dates, Court action and joins are adjudicative conclusions within the authorized task, not recovered historical events.

Draft status: legal formulation and supplement compatibility reviewed; assignment and canonical publication remain to be completed by the integrating operator. Durable canonical location upon publication: terms/OT2002/records/{d['filename']}. Current-Term State commitment is incomplete until that publication and its checks occur.

@@VALIDATION@@

## Adaptive audit annex

### Reconciliation finding adopted

{d['reconciliation']}

### Frozen Associate commitments and alternatives

{frozen}

### Approved Stone supplement, verbatim

{approved}

### Frozen neutral intake, verbatim

{intake}

## Public Projection

## Event

{d['public_event']}

## Participation

All nine Justices participated: {all_names}.

## Public Action

{d['result']}

## Judgment & Remedy

{d['judgment']}

## Opinion Topology

{d['topology']}

## Holdings

{d['holdings']}

## Precedent Treatment

{d['precedents']}

## Law After Decision

{d['law_after']}

## Separate Writings

{d['separate']}

## Procedure After Action

{d['procedure']}

## Source Notes

{d['public_sources']}
'''
    (OUT / d['filename']).write_text(internal, encoding='utf-8')
    return {k:d[k] for k in ['name','filename','form','full_joiners','eligible_authors','assignment_authority','fit_alternatives','components']}

coned = {
 'name':'Consolidated Edison Co. of New York, Inc. v. Pataki',
 'citation':'292 F.3d 338',
 'filename':'Consolidated-Edison-Co-of-New-York-Inc-v-Pataki_merits_2003-01-14.md',
 'frozen_heading':'Consolidated Edison Co. of New York, Inc. v. Pataki —',
 'stone_heading':'31. Consolidated Edison Co. of New York, Inc. v. Pataki',
 'result':'Affirmed, 9–0; the permanent injunction against Chapter 190 remains effective, with the limited remand for correction of the clerical error preserved.',
 'event':'''The Second Circuit affirmed the permanent injunction against enforcement of New York Chapter 190 under Article I, §10 and remanded to correct a clerical error in the judgment. State officials seek reversal; Con Ed seeks protection from the cost-disallowance and refund command. The questions are whether a corporation may invoke the Bill of Attainder Clause and whether this particular retrospective command imposes legislative punishment without judicial trial. The outage began February 15, 2000; the PSC began prudence review March 30, 2000; Chapter 190 became law August 8, 2000; the plant restarted in January 2001; the appellate opinion issued June 5, 2002.''',
 'entering':'''Article I, §10 governs legislative punishment by a State. Ambassador Books & Video, Inc. v. City of Little Rock distinguishes identification from punishment and requires historical, functional and purpose analysis; it did not decide corporate coverage. Nixon v. Administrator of General Services and United States v. Lovett supply the punishment and allocation-of-functions principles. Selective Service System v. Minnesota Public Interest Research Group leaves the burden of establishing punishment with the challenger. Genuine specific regulation and retrospective economic adjustment are not categorically forbidden.''',
 'stone_analysis':'''Stone affirms the injunction and clerical-correction remand and joins every proposition of the Court's opinion. His approved coverage rule, single punishment inquiry, claimant's burden and preservation of independent prudence review coincide with the reconciled eight-Associate rationale. The injunction reaches the whole proved punitive command because that is the actual command adjudged unlawful. Stone's proposed presumption favoring that scope unless officials establish a complete narrower cure is preserved as a proposal, not attributed to the Associates or made a new general burden rule. No distinct narrower-cure dispute requires resolving that proposal here. The Court's actual complete injunction fully accords with his fixed remedial result; a separate writing would add only an unapplied remedial proposal. His direct-review transition position creates no conflict with the ordinary immediate operation of the decision; no selective prospectivity is imposed. Equal protection and takings supply no additional adopted holding.''',
 'judgment':f'''**Affirmed, 9–0.**

**Supporting:** {all_names}.

The permanent injunction bars enforcement of Chapter 190's cost-disallowance and refund commands in full. The limited remand to correct the clerical error in the judgment remains in place. Independent lawful PSC prudence review remains available; the judgment establishes neither that every replacement-power cost was prudent nor an entitlement to reimbursement. The approximately $250 million at stake is not a damages award.''',
 'form':'''Form fixed before authorship or balance counts: one signed opinion of the Court after plenary merits submission. Corporate coverage and application of the punishment inquiry are related propositions in one constitutional adjudication with a common full-rationale coalition; they do not justify separate leads or a summary disposition.''',
 'opinion_rows':'| Opinion of the Court | @@LEAD@@ | @@LEAD_JOINERS@@ | Full opinion and judgment; all nine Justices support both holdings and the bounded injunction. |',
 'join_audit':'''Every Associate fully joins coverage, the combined punishment inquiry, its application and the injunction, subject to the individual limits copied below. The opinion preserves all of those limits: no universal corporate-rights rule, no naming or hostility shortcut, no requirement to retain the PSC's prior arrangement, no least-burdensome-alternative test and no recovery entitlement. Stone fully joins those propositions. No commitment changes after reconciliation; no partial join, separate writing or Marks question is necessary.''',
 'holdings':'''### Corporate protection against legislative punishment

**Holding and operative rule:** A corporation may invoke Article I, §10 when a state enactment identifies it and imposes punishment for past wrongdoing without judicial trial. This protection concerns the corporation's legal and property interests under this guarantee; it does not confer every right belonging to a natural person.

**Authority:** The unanimous opinion of the Court, authored by @@LEAD@@ and joined by @@LEAD_JOINERS@@, controls both holdings and the stated remedy.

**Controlling explanation:** The Court holds that the constitutional restraint turns on the legislative act and the nature of its punishment. A State cannot avoid the prohibition merely because the property subjected to punishment is held corporately. United States v. Lovett supplies the prohibition against noncapital legislative penalties and the separation of punishment from legislative adjudication. Nixon v. Administrator of General Services requires punishment beyond mere identification. Ambassador Books & Video, Inc. v. City of Little Rock applies that distinction to identifiable businesses but leaves this corporate-coverage issue for decision. Historical punishments often affected bodily liberty or the occupations of natural persons. That history informs what counts as punishment; it does not create an exception permitting the same prohibited method against an entity's property. The guarantee therefore reaches this asserted punitive financial disability without resolving unrelated corporate claims to personal rights.

### Chapter 190 imposes legislative punishment

**Holding and operative rule:** A challenger must establish identification, punishment and the absence of judicial trial; historical treatment, functional operation and legislative purpose inform one punishment inquiry rather than three cumulative requirements. Chapter 190's legislative determination of Con Ed's completed wrongdoing, combined with its conclusive denial and refund of all replacement-power costs for the identified outage, imposes punishment without trial and cannot be enforced.

**Authority:** The same unanimous Court opinion.

**Controlling explanation:** The Court holds that this law's combined operation supplies the constitutional defect. It names Con Ed, declares the company's completed operation unreasonable and makes that determination conclusively bar all replacement-power recovery for the outage, including repayment of amounts already collected. The Legislature itself fixes culpability and the complete financial consequence; the consequence does not depend on adjudicating which costs were imprudent.

Protecting ratepayers and allocating utility risk are legitimate regulatory objectives. Nixon and Ambassador Books establish that naming one operator, imposing a substantial burden, acting retrospectively or expressing hostility does not alone establish punishment. The Court accepts those limits. But describing who benefits from this command does not answer its operative character: a legislative judgment of past fault supplies the entire event-specific sanction without trial. That combination distinguishes this measure from genuine prospective rate regulation or an independently adjudicated cost disallowance. Neither an historically identical penalty nor a criminal conviction is necessary.

Selective Service System v. Minnesota Public Interest Research Group preserves the challenger's burden; the Court adds no motive presumption or least-restrictive-means test. The injunction fits the entire proved cost-disallowance and refund command. Ordinary lawful prudence review remains possible, and actual prudent costs and recoverable amounts remain matters for that process. The attainder holding supplies complete relief, so equal protection and takings do not furnish additional grounds for this judgment.''',
 'precedents':'''- **Ambassador Books & Video, Inc. v. City of Little Rock:** Applies its separation of identification from punishment and its historical, functional and purpose inquiry; distinguishes genuine prospective business regulation from this completed-conduct penalty. Its protection for genuine regulation remains effective, while the present decision expressly establishes corporate coverage of this guarantee.
- **Nixon v. Administrator of General Services, 433 U.S. 425:** Applies the punishment inquiry and preserves the principle that identification alone is insufficient.
- **United States v. Lovett, 328 U.S. 303:** Applies the prohibition of legislative punishment without trial to a punitive financial disability rather than limiting the Clause to a criminal conviction or capital penalty.
- **Selective Service System v. Minnesota Public Interest Research Group, 468 U.S. 841:** Preserves the challenger's burden to establish punishment; no burden shift or required least burdensome alternative is added.''',
 'law_after':'''Corporations may invoke the state Bill of Attainder Clause against punitive disabilities affecting their legal and property interests. The decision expressly resolves that coverage question and applies the existing punishment inquiry to Chapter 190. Specific regulation, ordinary prospective rates, neutral cost-allocation rules and independent prudence proceedings remain lawful when nonpunitive. The whole adjudged command is unenforceable; the decision creates no general remedial presumption, corporate entitlement to recover costs, or constitutional requirement to preserve an existing regulatory procedure.''',
 'procedure':'''The injunction remains effective. Upon the mandate, enforcing officials must omit Chapter 190's disallowance and refund command from implementation; regulatory orders and calculations may rest on independent lawful prudence findings. Reimposition of the same statutory command remains subject to enforcement of the injunction. A genuinely independent prudence determination proceeds through the ordinary regulatory review process. The lower court corrects the clerical error as already directed.''',
 'continuity':'''No separate writing is published. The corporate-coverage holding and the precise punishment application enter current law on January 14, 2003. No connected later event or factual outcome is presumed.''',
 'source_map':'''292 F.3d 338 supports the outage and statutory chronology, the PSC process, the enacted fault finding and complete cost command, the estimated financial stake, and the permanent injunction with its clerical-correction remand. The fresh Con Ed addendum identifies punishment and excess over regulation as contested legal characterizations, which the independent commitments resolved rather than presuming. The constitutional conclusions and Court joins come from the completed reconciliation and final compatibility inquiry.''',
 'extra_source':'Con Ed clarification: terms/OT2002/freeze/OT_2002CHUNK3_FRESH_NEUTRAL_ADDENDUM.md, Consolidated Edison section only.',
 'reconciliation':'''All eight Associate commitments were approved without substantive change. The enacted fault determination and complete retrospective sanction independently establish punishment; the adjective punitive in the intake was not used as a found fact. Corporate coverage is guarantee-specific. Ordinary prudence review survives, and the circuit result supplies no additional equal-protection holding or authorship.''',
 'public_event':'''Consolidated Edison Co. of New York, Inc. v. Pataki, 292 F.3d 338. Merits decision, January 14, 2003. On review of the Second Circuit's affirmance of a permanent injunction against New York Chapter 190 and its limited remand to correct a clerical error. The questions are whether a corporation is protected against state bills of attainder and whether Chapter 190's targeted replacement-power cost disallowance and refund command imposes punishment for past wrongdoing without judicial trial. The underlying outage began February 15, 2000; the statute became law August 8, 2000; the appellate judgment issued June 5, 2002.''',
 'topology':'@@LEAD@@ delivered the opinion of the Court, in which @@LEAD_JOINERS@@ joined. The opinion and both holdings are unanimous.',
 'separate':'',
 'public_sources':'U.S. Const., Art. I, §10; 2000 N.Y. Laws ch. 190; Consolidated Edison Co. of New York, Inc. v. Pataki, 292 F.3d 338. The approximately $250 million figure describes the costs at stake rather than an adjudicated award.',
 'full_joiners':ALL,
 'eligible_authors':ALL,
 'assignment_authority':'Stone-Zsela',
 'fit_alternatives':{'Stevens':'His Ambassador Books opinion supplies the direct identification-versus-punishment distinction and permits precise explanation of this different enacted operation.','Souter':'His accepted functional inquiry can integrate the fault finding, actual command and legitimate ratepayer argument without a naming shortcut.','Stone-Zsela':'His approved guarantee-specific coverage and unitary punishment inquiry directly support the full rationale; compare against the strongest eligible lower-count alternative without treating his proposed remedial presumption as adopted.','Ginsburg':'Her accepted distinction between genuine economic regulation and conclusive punitive adjudication fits the corporate property issue and bounded injunction.'},
 'components':[{'component':'Affirm injunction against Chapter 190; preserve clerical-correction remand','vote':'9–0','support':ALL,'oppose':[]}]
}

gibson = {
 'name':'Gibson v. County of Washoe',
 'citation':'290 F.3d 1175',
 'filename':'Gibson-v-County-of-Washoe_merits_2003-01-14.md',
 'frozen_heading':'Gibson v. County of Washoe —',
 'stone_heading':'29. Gibson v. County of Washoe',
 'result':'Affirmed, 9–0; the supported County screening/evaluation and medication-policy claims return for ordinary further proceedings, with the remaining dispositions preserved.',
 'event':'''The Ninth Circuit reversed summary judgment for the County on the supported mental-health policy claims while affirming summary judgment for the named deputies and supervising sergeant. Its opinion issued May 22, 2002. The County seeks judgment based on absence of a constitutional violation by the named employees and asserted lack of policy culpability or cause; Gibson seeks trial of the County's own policies concerning her husband's care and death. The question is whether a deliberately indifferent County policy may cause an actionable medical-care deprivation despite the named officers' lack of the subjective awareness required for personal liability.''',
 'entering':'''Section 1983 and the Fourteenth Amendment govern the pretrial detainee's custodial medical-care protection. Monell requires the municipality's own policy or legally effective custom. Collins separates a federal deprivation from municipal attribution. Canton and Carter require a deliberate municipal choice, sufficient notice and actual causal connection; Carter permits a pattern or a sufficiently obvious recurring need concerning a clear constitutional duty without invariably requiring identical prior incidents. Farmer preserves individualized awareness and reasonable-response limits for personal liability. Rule 56 requires supported evidence and permissible inferences to be considered favorably to the nonmovant. Section 3626 continues to govern any properly presented prospective prison-conditions relief.''',
 'stone_analysis':'''Stone affirms the supported screening and medication-policy return, preserves the individual and unappealed dispositions, and joins the full Court opinion. His approved deprivation, policy, known-or-obvious risk, municipal fault and causal-injury requirements are fully retained. The return restores this family's County claims, with liability and compensation to be established through ordinary proof; a death alone establishes neither. His proposed common-policy remedial allocation expressly depends on a live prospective claim, proved common injury and remedial jurisdiction. None is established in this summary-judgment record, so that branch is not triggered and supplies no present presumption, schedule or injunction. The preserved full supplement specifies his narrower conditions for any later equitable proceeding; no such future proceeding or factual predicate is invented. Section 3626 is unchanged. No standing fallback or substantive narrowing discretion is used. The absence of a separate writing reflects full compatibility on the actual issue, not adoption by the Associates of his conditional future proposal.''',
 'judgment':f'''**Affirmed, 9–0.**

**Supporting:** {all_names}.

The supported County claims concerning screening/evaluation and medication handling return for ordinary further proceedings, including trial if the remaining procedural requirements are satisfied. Summary judgment for the named deputies and sergeant, rejection of the unsupported communications-policy theory, and the unappealed consortium and state-law dispositions remain intact.''',
 'form':'''Form fixed before authorship or balance counts: one signed opinion of the Court after plenary merits submission. The municipal-liability rule and the limited Rule 56 application form one supported rationale; no separate lead or changed form is needed.''',
 'opinion_rows':'| Opinion of the Court | @@LEAD@@ | @@LEAD_JOINERS@@ | Full opinion and judgment; all nine join the municipal rule, its Rule 56 application and the limited return. |',
 'join_audit':'''All eight Associates join the Court's actual-deprivation, attributable-policy, municipal-fault and causal requirements and its limited summary-judgment application. The opinion neither combines innocent employees' information into personal awareness nor derives culpability from the death. O'Connor's specific-notice limit, Kennedy's prevention/causation limit, Souter's awareness distinction, Thomas's refusal to adopt Farmer's Eighth Amendment rationale and Ginsburg's exclusion of unsupported communications claims remain intact. Thomas joins the present Fourteenth Amendment municipal-policy reasoning under Collins and Carter; his earlier Farmer judgment agreement is not recast as an earlier rationale join. Stone supports the same entire formulation. No commitment changes, partial joins, separate writings or Marks issue arise.''',
 'holdings':'''### The municipality's own policy may cause a constitutional deprivation

**Holding and operative rule:** A municipality may be liable under §1983 for its own deliberately indifferent custodial policy that actually causes a denial of constitutionally required medical care, even when the named employees lack the personal awareness required for their liability. The claimant must prove an actual constitutional deprivation, an attributable municipal policy or legally effective custom, a deliberate municipal choice concerning a known or obvious constitutional need, and an identified defect closely related to and actually causing the injury; negligence, employment alone and pooled employee knowledge do not suffice.

**Authority:** The unanimous opinion of the Court, authored by @@LEAD@@ and joined by @@LEAD_JOINERS@@, controls the rule, the summary-judgment application and the limited return for further proceedings.

**Controlling explanation:** The Court holds that a named employee's exoneration does not collapse the separate inquiries into the deprivation and its municipal source. Monell requires the municipality's own causal policy or custom. Collins separates the underlying constitutional wrong from attribution; the absence of a custody-based duty in its voluntary-employment setting does not govern a pretrial detainee's custody. Canton requires deliberate municipal choice and a close causal connection. Carter permits notice through a pattern or a sufficiently obvious need to perform a clear constitutional duty in known recurring circumstances; identical prior injuries are not invariably necessary.

The County correctly insists on an actual deprivation and more than negligent administration. But the named deputies' lack of relevant awareness establishes neither that all required care was furnished nor that a County policy could not disable that care. Farmer's individual-awareness rule does not permit combining employees' innocent information to manufacture personal culpability. The municipal claim instead must identify and prove the County's own deliberately indifferent policy and its injury-producing operation. This preserves the underlying constitutional-injury requirement rather than substituting institutional responsibility for it.

### The supported screening and medication evidence permits further proceedings

**Holding and operative rule:** At summary judgment, a claimant must identify evidence permitting a reasonable finding on every required municipal-liability element. The evidence concerning delayed mental-health evaluation and handling of psychotropic medication meets that standard here; the surviving claims return under the ordinary preponderance-of-the-evidence burden, while the unsupported communications theory and the preserved personal and unappealed dispositions remain excluded.

**Authority:** The same unanimous Court opinion.

**Controlling explanation:** The Court holds that the evidence, viewed under Rule 56, supports a distinct policy inquiry. The jail regularly held mentally ill detainees, policymakers knew of that recurring population, and the evidence concerns practices postponing evaluation until an acutely disturbed person cooperated and treating relevant medication as property rather than a signal for assessment. General knowledge of mental illness alone would not suffice. These particular practices, combined with the recurring constitutional responsibility and medication evidence, permit a finding beyond hindsight that more training might have helped.

The County remains entitled to contest policy authority or effective custom, deliberate choice, deprivation and actual cause. Death during restraint does not itself establish a medical-care violation or that a different policy would have prevented the injury. The reasonable-force and personal-awareness rulings therefore survive, but they do not decide the independent medical-policy claim. The communications theory lacks the necessary policymaker-notice support and cannot survive merely by association with the supported policies. On remand, the family must prove the surviving elements and any compensable injury; ordinary factual and remedial adjudication under those rules does not make the municipal standard unresolved.''',
 'precedents':'''- **Monell v. Department of Social Services, 436 U.S. 658:** Applies the municipality's own policy-or-custom and causation requirements; employer-based liability remains forbidden.
- **Collins v. City of Harker Heights, 503 U.S. 115:** Applies the separate inquiries into constitutional deprivation and municipal attribution; distinguishes voluntary employment from actual pretrial custody.
- **City of Canton v. Harris, 489 U.S. 378:** Applies demanding municipal fault, notice, identified deficiency and causal connection; no negligence or hindsight standard replaces them.
- **Carter v. City of Philadelphia, March 13, 2000:** Applies its pattern-or-obvious-recurring-need notice rule and actual-cause requirement without adding an invariably identical-prior-incident condition.
- **Farmer v. Brennan, 511 U.S. 825:** Preserves individualized actual awareness and the protection for a reasonable response; neither collective awareness nor a failed reasonable response supplies personal culpability. The distinct municipal inquiry does not alter that rule.''',
 'law_after':'''Existing municipal and custodial law governs. A municipality cannot obtain judgment automatically from the named employees' lack of personal awareness when supported evidence independently connects an actual medical-care deprivation to its own deliberately indifferent policy. The same demanding deprivation, attribution, fault and causation requirements control analogous custodial policy claims. The decision supplies neither institutional strict liability nor a new aggregate-awareness test. Section 3626's requirements for prospective prison-conditions relief remain unchanged.''',
 'procedure':'''The case returns for ordinary proceedings on the supported County screening/evaluation and medication-policy claims. The trial issues must identify those surviving policies. The family bears the ordinary preponderance burden on the required liability elements and must establish compensable loss under the applicable damages rules; the County may contest each. The affirmed personal judgments and the excluded communications, consortium and state-law dispositions remain effective.''',
 'continuity':'''No separate writing is published. Stone's conditional future equitable-remedy proposal does not become current law or a public holding. No live prospective predicate is established, and no new common-policy remedial presumption or implementation obligation enters the state of the case.''',
 'source_map':'''290 F.3d 1175 supports the custodial episode, medical information and named-defendant limitations, the policy evidence, the County's recurring mentally ill population, the appellate summary-judgment treatment, the communications-policy deficiency and the unappealed claims. Collins, Carter and Farmer in the entering-law slice establish their exact controlling propositions and joins; the frozen commitments preserve Thomas's distinct Farmer relationship.''',
 'reconciliation':'''The limited affirmance and all eight full joins were approved without substantive change. Collins separates deprivation from attribution; Carter does not invariably require prior identical incidents; Farmer supplies no collective-awareness shortcut. The evidence permits proceedings, not a liability finding. All personal, communications and unappealed dispositions retain their bounded treatment.''',
 'public_event':'''Gibson v. County of Washoe, 290 F.3d 1175. Merits decision, January 14, 2003. On review of the Ninth Circuit's May 22, 2002 judgment reversing summary judgment for the County on supported mental-health policy claims and affirming judgment for the named deputies and supervising sergeant. The question is whether a County policy may cause an actionable denial of a detainee's serious medical needs despite the named officers' lack of the subjective awareness required for personal liability.''',
 'topology':'@@LEAD@@ delivered the opinion of the Court, in which @@LEAD_JOINERS@@ joined. The opinion and judgment are unanimous.',
 'separate':'',
 'public_sources':'42 U.S.C. §1983; U.S. Const., Amdt. 14; Fed. Rule Civ. Proc. 56; Gibson v. County of Washoe, 290 F.3d 1175. The policy and causal issues return on supported summary-judgment evidence, not findings of municipal liability.',
 'full_joiners':ALL,
 'eligible_authors':ALL,
 'assignment_authority':'Stone-Zsela',
 'fit_alternatives':{'Ginsburg':'Her Carter opinion directly supplies the source-specific omission, notice and causation framework now applied to supported jail policies.','Stevens':'His Collins opinion supplies the precise distinction between a constitutional deprivation and its municipal attribution, including the custody-versus-employment distinction.','Souter':'His Farmer opinion permits careful separation of individual awareness from independent municipal policy without pooling information.','Stone-Zsela':'His approved application explicitly combines all liability elements with the Rule 56 limits; his conditional future equitable proposal supplies no authorship advantage for the present issue.'},
 'components':[{'component':'Affirm the limited County return and preserve personal, communications and unappealed dispositions','vote':'9–0','support':ALL,'oppose':[]}]
}

craigmiles = {
 'name':'Craigmiles v. Giles',
 'citation':'312 F.3d 220',
 'filename':'Craigmiles-v-Giles_merits_2003-01-14.md',
 'frozen_heading':'Craigmiles v. Giles —',
 'stone_heading':'32. Craigmiles v. Giles',
 'result':'Reversed and remanded, 7–2, for dissolution of the injunction against the funeral-director qualification for the plaintiffs\' existing merchandise-only retail businesses.',
 'event':'''The Sixth Circuit's December 6, 2002 judgment affirmed the Eastern District of Tennessee's injunction against applying the funeral-director qualification to the plaintiffs' existing retail businesses. The district court found due-process and equal-protection violations after trial. Licensing officials seek reversal and dissolution; the retailers seek preservation of the injunction. Review concerns the qualification's rational relation to the stores' actual activity and the asserted legitimacy of protecting incumbents from competition alone. The distinct Privileges or Immunities theory is outside the grant. The existing-business injunction did not invalidate the entire Funeral Directors and Embalmers Act.''',
 'entering':'''Beach Communications governs ordinary economic rational-basis review: a reasonably conceivable legitimate basis suffices without formal findings or empirical certainty, and the challenger must negate such a basis. Lee Optical permits imperfect regulatory lines; Nordlinger preserves distinctions rationally supporting actual legitimate objectives. Heller and Romer require a relation to the actual disadvantage while rejecting an automatic least-restrictive-alternative duty. Moreno and Cleburne preserve the limits against bare harm and irrational prejudice. Naked intrastate incumbent protection as a sole public end is not settled by those holdings. The Court independently reviews legal rationality while accepting the supported trial findings.''',
 'stone_analysis':'''Stone dissents on both granted constitutional grounds and would affirm the existing-business injunction. His supplement expressly evaluates the real merchandise instruction, the 37 examination questions and the discipline rationale, and concludes their overlap insufficient on this combined trial record. His conditional reversal branch requires a genuine rational connection to the unified qualification. The seven Associates' contrary legal evaluation of the same accepted facts does not establish a changed record or authorize replacing Stone's express core with that branch. He recognizes ordinary economic deference and no fundamental occupational right, but would extend the public-end limit to naked incumbent protection and find that the challengers negated a legitimate relation here. He adopts no part of the controlling application and is not eligible to author its lead. His separate dissent preserves his full approved rule, distinctions and remedial allocation; Stevens does not join that broader remedial presumption merely because both would affirm. No standing fallback is invoked.''',
 'judgment':f'''**Reversed and remanded, 7–2.**

**Supporting:** {seven_names}.

**Opposing:** Stone-Zsela and Stevens.

The lower court must dissolve the injunction barring application of the funeral-director qualification to the plaintiffs' existing merchandise-only retail businesses. The challenged qualification survives the granted due-process and equal-protection challenges. Review remains confined to that existing-business injunction; the separate Privileges or Immunities claim is outside the grant.''',
 'form':'''Form fixed before authorship or counts: one signed opinion of the Court after plenary merits submission, with distinct dissents by Stevens and Stone-Zsela. The two constitutional challenges receive the same rational-connection answer and produce one injunction disposition. The substantive disagreement over that application requires reasoned dissent but no fragmented lead or component assignment.''',
 'opinion_rows':'''| Opinion of the Court | @@LEAD@@ | @@LEAD_JOINERS@@ | Full rationale and reversal; O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. |
| Dissent | Stevens | No other Justice | Would affirm on due-process and equal-protection grounds; rejects the actual fit of the overall qualification. |
| Dissent | Stone-Zsela | No other Justice | Would affirm on both grounds; proposes the public-end extension and the bounded remedial presumption described below. |''',
 'join_audit':'''The seven full-rationale joiners accept the existing businesses' boundaries, the small but real curriculum overlap, the 37 merchandising examination questions and the trial findings about caskets. Their opinion rests on the competence/accountability connection, not an invented activity or empirical finding of improved outcomes. It preserves rational review of the actual disadvantage and does not decide that incumbent rents alone are legitimate. Each of their recorded limits is satisfied, and none changes position after reconciliation. Stevens's actual-fit objection is answered in the controlling explanation; the answer does not induce his join or alter his frozen view. Stone's express application remains contrary. The two dissenters share an affirmance vote but no joint writing is inferred. No Marks synthesis is needed because seven Justices join the same rationale.''',
 'holdings':'''### The actual merchandising and accountability connection satisfies ordinary review

**Holding and operative rule:** An ordinary economic qualification that implicates neither a fundamental right nor a suspect class satisfies due process and equal protection when it has a reasonably conceivable rational connection to a legitimate public objective; the challenger must negate that connection without demanding empirical certainty, formal findings or the least burdensome system. Tennessee's funeral-director qualification may be applied to these merchandise-only retailers because its actual merchandise instruction and examination, together with professional discipline, rationally connect the qualification to competence and accountability in this specialized sales market.

**Authority:** The opinion of the Court, authored by @@LEAD@@ and joined by @@LEAD_JOINERS@@, is supported in full by O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. Seven Justices adopt this rule, its application to both granted constitutional grounds and dissolution of the injunction.

**Controlling explanation:** The Court holds that the trial findings do not negate every reasonably conceivable legitimate connection. Beach Communications permits supported economic generalizations without proof that the legislature chose the best system. Lee Optical allows imperfect regulatory lines, and Nordlinger permits substantial disparities when an actual legitimate purpose rationally explains them. Heller and Romer retain scrutiny of the relationship to the disadvantage imposed; they do not require a separate, least burdensome scheme whenever one is imaginable.

These stores do not handle bodies, arrange funerals or burials, embalm or make advance-need sales. Much of the required preparation concerns services they never perform. But the curriculum includes merchandise instruction, and 37 of 250 examination questions concern funeral merchandising. A common professional qualification and disciplinary system can rationally serve informed selection, ethical sales and accountability when goods are sold in the funeral market. This is a permissible legislative connection, not a new finding that the qualification measurably improves casket quality.

The dissent's strongest objection concerns the entire entry barrier, not the mere existence of useful instruction. The Court nevertheless rejects its application because ordinary review does not impose proportionality between the curriculum and each specialty's daily work. The findings about casket quality, unrestricted burial choices and the substantial unrelated training defeat some proposed safety explanations; they do not eliminate the actual merchandise and accountability connection. Existing fraud remedies and a possible retail-specific license do not make the common qualification irrational.

Moreno and Cleburne continue to prohibit illegitimate ends and irrational distinctions. The Court does not decide whether incumbent protection standing alone is a legitimate end: the second question's premise that no independent rational public connection exists is not established in this record. The distinct Privileges or Immunities theory lies outside the grant.''',
 'precedents':'''- **FCC v. Beach Communications, Inc., 508 U.S. 307:** Applies the reasonably conceivable legitimate-basis rule, challenger's burden and absence of a formal-findings requirement; it supplies no immunity for an irrational or impermissibly motivated line.
- **Williamson v. Lee Optical of Oklahoma, Inc., 348 U.S. 483:** Applies legislative latitude in economic regulation without requiring an optimally tailored occupation or curriculum.
- **Nordlinger v. Hahn, 505 U.S. 1:** Applies its tolerance of substantial disparities supported by legitimate policy differences; protection of an existing business's profits alone is not decided.
- **Heller v. Doe, 509 U.S. 312:** Preserves the required relationship to the actual disadvantage and its separate holding that a less extensive alternative does not alone invalidate a rational classification.
- **Romer v. Evans, 517 U.S. 620:** Preserves real rational-connection review without empirical certainty or least-restrictive-means requirements; distinguishes an unexplained disability from this actual merchandising and accountability connection.
- **Department of Agriculture v. Moreno, 413 U.S. 528, and City of Cleburne v. Cleburne Living Center, 473 U.S. 432:** Preserve the limits against bare harm and irrational prejudice; the Court adds no categorical rule that incumbent protection by itself is legitimate.''',
 'law_after':'''The existing rational-basis standard governs the reviewed licensing requirement. A unified occupational qualification may cover a merchandise-only specialty when actual merchandise instruction, examination and common professional accountability supply a rational connection to legitimate consumer interests, despite substantial training concerning other professional services. The decision imposes no curriculum-proportionality test and adopts no fundamental occupational right. It leaves unresolved the legitimacy of naked incumbent protection as the sole end because the actual record supplies a distinct rational public connection; it does not approve an arbitrary credential merely because incumbents benefit.''',
 'procedure':'''The case returns for dissolution of the existing-business injunction. Officials may enforce the reviewed qualification against the covered retail activity consistently with the judgment. The disposition concerns these granted due-process and equal-protection challenges and the existing injunction; the rejected Privileges or Immunities theory remains outside this review.''',
 'continuity':'''The two dissents below are published noncontrolling positions, each dated January 14, 2003. Stevens retains his actual-fit and impartial-public-purpose objection to the overall professional-entry barrier while accepting the real merchandise content. Stone retains his proposed extension against naked incumbent protection, his conclusion that the record negates a legitimate connection, and his proposed materially-equivalent-activity remedial presumption. Neither supplies current law or an additional majority holding.

''' ,
 'source_map':'''312 F.3d 220 supplies the trial findings, stores' actual activities, 1972 definition amendment, alternative school/apprenticeship routes, examination content, challenged statutes, December 6 judgment and existing-business injunction. The frozen commitments independently evaluate those accepted facts. No empirical improvement, future body handling, advance-need activity or federal Funeral Rule coverage is invented.''',
 'reconciliation':'''The seven-Associate reversal and Stevens affirmance were approved without substantive change. Ordinary Beach deference remains compatible with Heller and Romer's actual-disadvantage requirement. Merchandise competence and accountability supply the seven's legitimate rationale; incumbent protection alone is not adopted. Stevens's substantive objection remains a dissent. The circuit disposition supplies no Supreme Court historical lineup.''',
 'public_event':'''Craigmiles v. Giles, 312 F.3d 220. Merits decision, January 14, 2003. On review of the Sixth Circuit's December 6, 2002 affirmance of an injunction against applying Tennessee's funeral-director qualification to the plaintiffs' existing retail businesses. The questions are whether requiring that qualification for merchandise-only retailers violates due process or equal protection, and whether protecting incumbents from competition alone supplies a legitimate governmental interest. The separate Privileges or Immunities theory is outside the grant.''',
 'topology':'@@LEAD@@ delivered the opinion of the Court, in which @@LEAD_JOINERS@@ joined. Stevens and Stone-Zsela filed separate dissenting opinions. No Justice joined either dissent.',
 'separate':'''**Stevens, dissenting.** Stevens would affirm the existing-business injunction under ordinary rational-basis review. His approach in Beach and Nordlinger asks whether an impartial legislature could pursue the asserted purpose and whether that purpose rationally explains the actual inequality. He accepts that the curriculum teaches some merchandising; he rejects the conclusion that this limited content explains exclusion from the entire retail activity until the seller completes the substantially unrelated professional qualification. The trial findings concerning the stores' limited work, casket quality and the entry burden supply the basis for that conclusion. A private benefit cannot justify itself merely because the statute creates it. His objection does not demand the least restrictive fraud law or an optimally efficient course: it concerns the relationship of the whole prerequisite to the actual trade. Bare preservation of incumbent rents supplies no independent legitimate justification in his view.

**Stone-Zsela, dissenting.** The Chief Justice would affirm on both due-process and equal-protection grounds. Beach and Lee Optical permit imperfect economic lines, but Moreno and Cleburne preserve a legitimate-public-end requirement. He would extend that limit to bare protection of incumbent sellers from harmless competition. Incidental incumbent benefits, consumer protection, redistribution, aid to a distressed industry and Nordlinger's protection of established commitments remain distinguishable legitimate objectives.

He accepts the merchandising instruction, the 37 examination questions and the possible value of professional discipline. On this combined record, however, the stores perform none of the defining services that principally occupy the education and apprenticeship; the burial choices and quality findings also undermine the proposed casket-safety explanation. Discipline's usefulness does not itself connect those unrelated entry prerequisites to the admitted retail activity. Challengers retain the burden of negating reasonably conceivable legitimate explanations; no empirical proof, least restrictive system or specially optimized curriculum is constitutionally required.

He would retain relief against this separable qualification and presume equivalent protection for materially equivalent merchandise-only activity unless the State establishes that a narrower decree fully cures the proved violation. The trial findings and remedial jurisdiction must define the covered activity. Bodily care, funeral arrangements, advance-need transactions and lawful sales regulation remain outside that invalidation. The State could not obtain narrower relief by merely promising discretionary nonenforcement against the named stores. His rule would govern still-open direct-review cases under Harper, subject to Reynoldsville's independent procedural, immunity and remedial limits; final judgments remain closed and collateral relief requires its own authorization.''',
 'public_sources':'U.S. Const., Amdt. 14; Tenn. Code §§62-5-101 and 62-5-201 and the related training and disciplinary provisions; Craigmiles v. Giles, 312 F.3d 220. The trial findings concern merchandise-only businesses with limited, rather than nonexistent, relevant training in the required curriculum.',
 'full_joiners':SEVEN,
 'eligible_authors':SEVEN,
 'assignment_authority':"O'Connor",
 'fit_alternatives':{'Thomas':'His Beach opinion states the exact conceivable-basis rule and retained Moreno/Cleburne limits now applied to a proved partial curriculum overlap.','Souter':'His Heller and Romer opinions permit precise reconciliation of actual-disadvantage review with the supported merchandising and accountability ground.','O\'Connor':'Her Beach, Nordlinger and Heller participation commitments support a concise actual-connection ruling while retaining ordinary economic latitude.','Kennedy':'His Heller family-participation rationale helps explain why availability of less extensive alternatives does not defeat this genuine regulatory connection.'},
 'components':[{'component':'Due-process challenge and injunction dissolution','vote':'7–2','support':SEVEN,'oppose':['Stone-Zsela','Stevens']},{'component':'Equal-protection challenge and injunction dissolution','vote':'7–2','support':SEVEN,'oppose':['Stone-Zsela','Stevens']}]
}

craigmiles['continuity'] += craigmiles['separate']
metadata = []
for item in [coned, craigmiles, gibson]:
    metadata.append(write_case(item))
(BASE/'runtime/OT_2002CHUNK3_A_INITIAL_ASSEMBLY.json').write_text(json.dumps({'event_date':'2003-01-14','draft_only':True,'assignment_order':'Consolidated Edison; Craigmiles; Gibson, interleaved with any other same-date cases by alphabetical case name','cases':metadata}, indent=2), encoding='utf-8')
print('Wrote three reviewable assembly drafts and assignment metadata.')
