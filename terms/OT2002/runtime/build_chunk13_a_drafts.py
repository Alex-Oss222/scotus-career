from pathlib import Path
import json
import sys

BASE = Path('terms/OT2002')
OUT = BASE / 'runtime/chunk13-drafts'
OUT.mkdir(exist_ok=True)
stone = (BASE/'runtime/OT_2002CHUNK13_A_STONE.md').read_text(encoding='utf-8-sig')
reconciled = (BASE/'freeze/OT_2002CHUNK13_A_RECONCILED.md').read_text(encoding='utf-8-sig')
neutral = (BASE/'freeze/OT_2002CHUNK13_A_NEUTRAL.md').read_text(encoding='utf-8-sig')

def section(text, marker, next_marker='\n## '):
    start = text.index(marker)
    end = text.find(next_marker, start + len(marker))
    return text[start:end if end >= 0 else len(text)].strip()

ALL = ['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']
ASSOC = ALL[1:]
SIX = ['Stevens',"O'Connor",'Kennedy','Souter','Ginsburg','Breyer']
selected = sys.argv[1] if len(sys.argv) > 1 else None
data = json.loads((OUT/'A_specs.json').read_text(encoding='utf-8')) if selected and (OUT/'A_specs.json').exists() else []

def draft(case, number, docket, citation, date, argued, filename, result, form, compat, continuity, sources, blocks, eligible, assigner='Stone-Zsela', authority=None):
    if selected and selected != str(number):
        return
    fixed = section(stone, f'## {number}.')
    frozen = section(reconciled, f'## {number}.')
    packet = section(neutral, f'## {number}.')
    body = f'''**Case and dockets:** {case}; No. {docket}; {citation}.
**Event and date:** Merits decision, {date}; October Term 2002, chunk 13; argued {argued}.
**Result:** {result}
**Version / lineage:** Initial decision record; supersedes no completed adjudication.

## Event, participation, and entering law

The matter arrived through the review route and preserved questions stated in the Event block below. All nine seated Justices participated at argument and decision: Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, and Breyer. Nine participants satisfy the quorum; five votes decide each merits component. The final judgment, joins, substantive holdings, mandate, and remaining stage are stated in the bounded Public Projection and form the decision kernel.

The issue-specific reading slice is terms/OT2002/entering-law/OT_2002CHUNK13_{number}_LAW.md. It copies the term-opening governing law and effective current-term public law. The frozen neutral packet is terms/OT2002/freeze/OT_2002CHUNK13_A_NEUTRAL.md; the controlling non-Stone reconciliation is terms/OT2002/freeze/OT_2002CHUNK13_A_RECONCILED.md. Independent same-day decisions do not supply entering precedent. Research cutoff: {date}; substantive authorities are date eligible. The review-event date follows the approved inventory's historical-calendar scheduling basis; no additional Court action is imported from history.

## Form and governing propositions fixed before assignment

{form}

__ASSIGNMENT_BLOCK__

## Stone fixed core and compatibility

Source: terms/OT2002/runtime/OT_2002CHUNK13_A_STONE.md, the approved chunk supplement exposed only after non-Stone reconciliation. The complete source passage below is copied mechanically; it is not reauthored.

{fixed}

### Final compatibility and joins

{compat}

## Continuity and present law

The Public Projection's Holdings, Precedent Treatment, and Law After Decision state the exact controlling effect from the event date; the Opinion Topology fixes each source writing and join. The procedural effect is the mandate in Procedure After Action. No roster, allotment, or institutional practice changes.

{continuity}

## Adaptive audit annex — frozen non-Stone commitments and reconciliation

The following case-specific reconciliation passage is copied mechanically from the frozen handoff. It preserves each Associate's conclusion, authority, join boundary, historical comparison, and any supported changed premise. Historical descriptions in this annex are comparator evidence, not the Court's public action. Final form and authorship come from the assignment and topology above and below.

{frozen}

## Sources, source limits, and validation status

{sources}

The neutral record supplies supported facts and the adversarial paths; judicial evaluations are kept distinct from trial findings. No missing research item is treated as a litigant default. No reconstruction premise is needed for arrival at review. The original petitions, briefs, and appendices are not represented as read by assembly. The frozen reconciliation documents the complete opinion-source review and official Reports cross-check. The source passages reproduced internally were copied by script.

Assembly checked the approved fixed core, conditional trigger, final judgment by component, proposition-level joins, complete-resolution scope, preserved lower-court rulings, and the five-block negative-statement rule. Every public controlling explanation is below 350 words. Numerical and projection-structure checks are performed by the draft validator; final publication, serial assignment, and whole-term validation remain with integration. __PUBLICATION_STATUS__

## Public Projection

'''
    body += '\n\n'.join(f'## {key}\n\n{value.strip()}' for key,value in blocks.items())+'\n'
    (OUT/filename).write_text(body,encoding='utf-8')
    spec={'file':filename,'case':case,'date':date,'countable':True,'assigner':assigner,'eligible_authors':eligible,'full_joiners':eligible}
    if authority: spec['assignment_authority_text']=authority
    data[:] = [item for item in data if item['file'] != filename]
    data.append(spec)

draft(
case='Federal Election Commission v. Beaumont',number=156,docket='02-403',citation='539 U.S. 146',date='2003-06-16',argued='2003-03-25',filename='Federal-Election-Commission-v-Beaumont_merits_2003-06-16.md',
result='Reverse the Fourth Circuit on the as-applied direct treasury-contribution restriction, 6–3, and remand; the independent-expenditure judgment remains undisturbed.',
form='One signed Opinion of the Court resolves the contribution-specific standard and its cumulative application to NCRL. One dissent states the common complete-source-exclusion objection. These forms and propositions are fixed on their legal grounds before counts or authors are considered. The six supporting the entire Court opinion are Stone-Zsela, Stevens, O\'Connor, Souter, Ginsburg, and Breyer. Kennedy, Scalia, and Thomas oppose the judgment on their common actual-fit ground. No separate contribution/expenditure reform or new scrutiny tier is adopted.',
compat='Stone reverses the direct-contribution exemption and joins every proposition of the Court opinion: an objectively grounded candidate-resource or circumvention interest, a government burden of close fit, and meaningful voluntary association through the actual functioning fund. The cumulative rationale answers the lost-pool objection through actual business receipts, direct candidate resources, demonstrated fund operation, and permitted organizational support; nominal fund availability alone is insufficient. His independent-expenditure limit is preserved in the judgment and mandate. No conditional branch or standing fallback is used; no approved position is narrowed or replaced. His directions concerning penalties and a new fund are honored by the ordinary reversal and existing lawful channel, without adding redundant public disclaimers.',
continuity='Kennedy writes a dissent joined by Scalia and Thomas. Their published noncontrolling position accepts contribution-specific scrutiny and preventive source regulation but finds complete exclusion of this overwhelmingly individual-funded treasury inadequately justified. A separately collected fund is a different pool, even when genuinely functioning. They preserve Stengel\'s rejection of categorical nonprofit immunity and the existing contribution/expenditure distinction. The dissent supplies no unlimited-contribution rule. This source-specific objection remains relevant to future burden and fit comparisons.',
sources='The neutral packet establishes NCRL\'s nonprofit status, absence of shareholders, predominantly individual funding, some business-corporation receipts, operating candidate-contribution fund, Fourth Circuit summary-judgment posture, and limited grant. The official Reports citation and the reconciliation metadata establish argument date and review route. Exact governing text: terms/OT2002/entering-law/OT_2002CHUNK13_A_STATUTES.md, 2 U.S.C. §441b(a)–(b); official source https://www.govinfo.gov/content/pkg/USCODE-2002-title2/html/USCODE-2002-title2-chap14-subchapI-sec441b.htm. Current-law support is Stengel, Russell, Day, Shrink Missouri, Mariani, and Lamb in the issue slice; the copied Mariani and Shrink dissent passages are in OT_2002CHUNK13_A_PUBLIC_WRITINGS.md. Official fact cross-check: https://tile.loc.gov/storage-services/service/ll/usrep/usrep539/usrep539146/usrep539146.pdf. No business-funding percentage, completed evasion, actual quid pro quo, or failure of the fund is found.',
eligible=['Stone-Zsela','Stevens',"O'Connor",'Souter','Ginsburg','Breyer'],
blocks={
'Event':'''Federal Election Commission v. Beaumont, No. 02-403, 539 U.S. 146. Merits decision, June 16, 2003. Argued March 25, 2003. On writ of certiorari to the United States Court of Appeals for the Fourth Circuit, which affirmed summary judgment exempting North Carolina Right to Life from the federal prohibition on direct corporate treasury contributions. The question is whether that prohibition may constitutionally apply to this nonprofit advocacy corporation, which accepts some business-corporation funds and operates a separate voluntary political fund that has contributed to federal candidates. The independent-expenditure component of the judgment is outside the grant.''',
'Participation':'Chief Justice Stone-Zsela and Justices Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, and Breyer participated.',
'Public Action':'The judgment on direct treasury contributions is reversed, and the case is remanded.',
'Judgment & Remedy':'''**Judgment:** Reversed and remanded on the as-applied direct-contribution claim, 6–3.

**Supporting:** Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg, Breyer.

**Opposing:** Scalia, Kennedy, Thomas.

The lower court must remove the declaration and injunction insofar as they prevent application of the direct-contribution restriction to NCRL. The independent-expenditure judgment remains undisturbed.''',
'Opinion Topology':'''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | __LEAD_AUTHOR__ | __LEAD_JOINERS__ | Reversal and remand | All holdings and the contribution-specific mandate |
| Dissenting opinion | Kennedy | Scalia, Thomas | Would affirm the as-applied direct-contribution exemption | Complete-source-exclusion and actual-fit ground |''',
'Holdings':'''### Direct contributions by this advocacy corporation

**Holding and operative rule:** A restriction on an advocacy corporation's direct candidate contributions must serve an objectively grounded important corruption or circumvention interest and be closely fitted to that interest while preserving meaningful voluntary association. The government meets that burden for NCRL's treasury contributions through the cumulative combination of direct candidate control over contributed resources, the treasury's actual receipt of business-corporation funds, the preventive source-channel interest, an operating voluntary fund that has contributed to federal candidates, and permitted organizational support for that fund.

**Authority:** The Opinion of the Court, joined in full by Stone-Zsela, Stevens, O'Connor, Souter, Ginsburg, and Breyer. These six directly adopt both the standard and its application.

**Controlling explanation:** Direct contributions place resources under a candidate's control. Buckley preserves the difference between that transfer and independent advocacy. Stengel rejects a categorical exemption for ideological nonprofits' direct gifts; MCFL's independent-expenditure holding does not supply one. Russell, Shrink Missouri, Mariani, and Lamb require the government to justify the actual restriction, and Day protects genuine voluntary pooling. NCRL's message and corporate form cannot do that work.

Here the treasury accepts business-corporation money that can enter the candidate-contribution stream, and the established political fund demonstrates a usable means of collective candidate support. Section 441b permits the organization to establish, administer, and solicit for the voluntary fund. The dissent correctly identifies a burden in losing access to the existing treasury pool. The Court answers that burden through the combined source risk and demonstrated operation, including organizational support, rather than by the existence of another account alone. Preventive regulation need not await a completed evasive transfer. The absence of shareholders and predominance of individual donations matter, but do not remove the actual business-fund route or the direct-transfer interest on this record. This contribution-specific application preserves meaningful association through the lawful fund.

**Operative qualifications:** Incorporation, advocacy viewpoint, or nominal availability of a segregated account alone is insufficient. A materially different source or channel record must be tested under the same government burden. The statutory fund remains voluntary: compelled dues, coercive collections, and commercial-transaction receipts cannot finance its contributions.''',
'Precedent Treatment':'''- Buckley v. Valeo supplies the contribution/expenditure distinction and retains its force.
- Federal Election Commission v. National Right to Work Committee supplies the regulated-fund structure and protections for economic payers; its rationale is applied through actual fit.
- Federal Election Commission v. Massachusetts Citizens for Life concerns independent spending and does not create a direct-contribution exemption.
- Kentucky Right to Life v. Stengel retains its rejection of categorical ideological-nonprofit immunity; this decision supplies a record-specific application.
- Russell v. Burris and Nixon v. Shrink Missouri Government PAC retain the government's objectively grounded interest and close-fit burden.
- Day v. Holahan retains protection for genuine voluntary pooling.
- Mariani v. United States requires examination of complete source exclusion and meaningful operation of the retained channel.
- Missouri Republican Party v. Lamb requires a separate fit inquiry into actual candidate resources or genuine conduits; another account's existence is not a complete answer.''',
'Law After Decision':'''The direct treasury-contribution restriction is enforceable against NCRL on this funding and fund-operation record. Existing contribution doctrine remains the governing reusable rule: the government must establish the actual interest and fit while preserving meaningful voluntary association. NCRL may continue candidate support through its existing lawful voluntary fund, and the independent-expenditure judgment retains its force.''',
'Separate Writings':'''**Kennedy, dissenting, joined by Scalia and Thomas.** The dissent accepts the contribution standard and Stengel's rejection of categorical nonprofit immunity. It also accepts preventive safeguards directed to business sources and genuine conduits. But NCRL's treasury consists overwhelmingly of voluntary individual support, and its existing fund collects a different pool. Actual use of that fund answers whether it is merely nominal; it does not by itself justify complete exclusion of the chosen association's treasury. Mariani's source-specific objection and Lamb's separate fit requirement therefore support affirmance on this record. The dissent recognizes the business receipts and administrative support as substantial contrary considerations, but finds their combined justification insufficient for this total source restriction.''',
'Procedure After Action':'The case returns to the Fourth Circuit for a judgment conforming to the reversal of direct-contribution relief. Ordinary statutory enforcement must identify the prohibited transfer and proceed under the applicable procedures and defenses; the surviving independent-expenditure judgment governs that separate component.',
'Source Notes':'No. 02-403; 539 U.S. 146; 2 U.S.C. §441b(a)–(b). The record establishes some business-corporation receipts and actual use of NCRL\'s political fund.'
})

draft(
case='Virginia v. Hicks',number=153,docket='02-371',citation='539 U.S. 113',date='2003-06-16',argued='2003-04-30',filename='Virginia-v-Hicks_merits_2003-06-16.md',
result='Reverse the whole-policy facial-overbreadth judgment unanimously and remand for remaining preserved grounds.',
form='One signed unanimous Opinion of the Court resolves the state-judgment review route and the whole-policy substantiality question. The permission practice may be assumed defective for that sufficient holding. The opinion preserves the actual-policy denominator and leaves the second granted forum question for a record and disposition requiring it. All nine support the complete opinion. No separate writing performs additional legal work once those qualifications appear in the controlling opinion. The form and propositions are fixed before counts or authors.',
compat='Stone joins all holdings and the bounded reversal. The review-route proposition applies ASARCO to the state judgment and does not assert that Hicks could initiate the same third-party suit in federal court. The facial rule demands substantial protected reach without a personal-expression prerequisite or categorical immunity for conduct regulation. The remaining preserved grounds, state-law severability, and functional forum inquiry are preserved. His express exclusion of automatic conviction reinstatement is an operative remand limit. No conditional branch or standing fallback is used. The sole drafting discretion is nonmaterial formulation; neither judgment nor burden changes.',
continuity='All nine directly join the holdings. Souter and Breyer\'s denominator concern is embodied in the Court\'s identification of the policy actually invalidated, so no separate concurrence is issued. This decision is a June 16 legal dependency for the library matter only at its actual scope: substantial overbreadth, the distinction from standing, and the limits of an inadequate facial showing. It supplies no library forum, filtering, or funding rule. No historical downstream event is inferred.',
sources='The neutral packet establishes Richmond\'s street conveyance, the housing authority\'s entry policy, Hicks\'s written barment and return, the unwritten expressive-permission practice, the state judgment, and the absence of a claim that his arrested conduct was expression. The metadata in the frozen reconciliation and official Reports establish argument and decision dates and certiorari route. Official cross-check: https://tile.loc.gov/storage-services/service/ll/usrep/usrep539/usrep539113/usrep539113.pdf. The entering-law slice supplies Broadrick, ASARCO, R. A. V., Forsyth County, Thomas, Watchtower, First Unitarian, and the exact current Black public holdings. The state-law denominator is the policy actually invalidated; no severability fact or frequency of expressive visits is newly found.',
eligible=ALL,
blocks={
'Event':'''Virginia v. Hicks, No. 02-371, 539 U.S. 113. Merits decision, June 16, 2003. Argued April 30, 2003. On writ of certiorari to the Supreme Court of Virginia, which affirmed reversal of Hicks's trespass conviction because the housing authority's policy was facially overbroad. The granted questions concern this defendant's ability to invoke overbreadth and whether constitutional limits on expressive-entry discretion depend on forum status. Richmond conveyed the Whitcomb Court streets to its housing authority, which excluded people lacking a legitimate business or social purpose. Hicks returned after written barment and denied permission; he does not claim his arrested conduct was protected expression. The state court relied on unwritten permission requirements for leafleting and demonstrating without deciding the streets' forum status.''',
'Participation':'All nine Justices participated: Stone-Zsela, Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, and Breyer.',
'Public Action':'The judgment is reversed, and the case is remanded.',
'Judgment & Remedy':'''**Judgment:** Reversed and remanded, 9–0.

**Supporting:** Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer.

The rejected facial ground cannot support wholesale invalidation. The state court must adjudicate any remaining preserved as-applied, forum, vagueness, or state-law ground before entering the resulting criminal judgment. Reversal does not automatically reinstate the conviction.''',
'Opinion Topology':'''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | __LEAD_AUTHOR__ | __LEAD_JOINERS__ | Reversal and remand | All holdings and the bounded mandate |''',
'Holdings':'''### Review of the state judgment and the overbreadth claim

**Holding and operative rule:** A defendant's lack of protected expression in his own conduct does not categorically defeat an overbreadth claim entertained by a state court. Virginia's concrete injury from the adverse state judgment supports this Court's Article III review under ASARCO, while substantial overbreadth remains a distinct federal merits requirement.

**Authority:** The unanimous Opinion of the Court. All nine Justices directly join this holding and the remaining holdings.

**Controlling explanation:** ASARCO distinguishes review of an injurious state judgment from commencement of an action in federal court. Federal trial standing rules do not retroactively displace the state court's access rules. Broadrick permits challenges designed to protect expression chilled beyond the litigant's own conduct, but imposes a substantive limit on that exceptional remedy. Hicks's personal conduct therefore supplies neither a categorical bar to considering his claim nor proof of its facial merit. Whether he could initiate the same third-party action in federal court is unnecessary to this review route and remains undecided.

### Whole-policy substantial overbreadth

**Holding and operative rule:** Facial overbreadth requires a supported showing that a policy's unconstitutional applications to protected expression are substantial in relation to its legitimate sweep. A potentially unlawful expressive-permission practice does not, on this record, establish the substantial protected reach necessary to invalidate the entire trespass policy.

**Authority:** The unanimous Opinion of the Court, on the common coalition stated above.

**Controlling explanation:** Broadrick protects against substantial deterrence of expression while withholding wholesale invalidation for a merely possible defect. The policy has extensive legitimate operation in excluding unauthorized nonexpressive entry. Unwritten discretion over leafleting or demonstrating may present a serious expressive-access problem, but that concern does not supply the further comparison needed for the whole policy the state court invalidated. The Court assumes the identified permission defect for purposes of this sufficient ground. Hicks still fails to establish that the policy's unconstitutional expressive reach is substantial relative to its lawful applications.

The inquiry may rest on the rule's terms, its actual operation, and realistically implicated protected conduct; it imposes neither a numerical quota nor a mandatory empirical survey. A regulation's conduct label supplies no immunity. Conversely, the possibility that discretion chills some speakers does not eliminate the required comparison. The relevant rule is the actual policy invalidated below, and any narrower state-law severance must follow state law. A supported narrower expressive injury remains entitled to its appropriate adjudication and cure.

### Forum status and remaining expressive claims

**Holding and operative rule:** The failure of the whole-policy showing resolves the facial judgment even assuming the challenged expressive discretion is unlawful. The second granted question does not require a definitive forum classification in this disposition; any surviving expressive-access claim must receive the governing function-and-use inquiry, and a conveyance of ownership alone does not settle it.

**Authority:** The unanimous Opinion of the Court, on the common coalition stated above.

**Controlling explanation:** First Unitarian requires attention to retained public function and use, rather than title alone. The state court left forum status undecided, and the sufficient substantiality ground does not depend on resolving that classification. Thomas supplies rules for reasonable, bounded permit administration; Forsyth County addresses standardless expressive discretion. Their protections remain available when a preserved claim and the actual access record require them. The remand therefore calls for adjudication of surviving grounds before the criminal disposition, rather than an inference that the facial reversal approves the unwritten permission practice.''',
'Precedent Treatment':'''- ASARCO Inc. v. Kadish is applied to review of a state judgment causing concrete injury, preserving the distinction from initiation of a federal action.
- Broadrick v. Oklahoma retains its substantial-overbreadth requirement for the actual rule challenged, including general conduct regulations.
- First Unitarian Church v. Salt Lake City retains its functional treatment of public access despite a transfer of title.
- Forsyth County v. Nationalist Movement retains its protection against standardless expressive-permit discretion.
- Thomas v. Chicago Park District retains the distinction between reasonable bounded administration and censorship discretion.
- R. A. V. v. City of St. Paul and Virginia v. Black retain their actual controlling facial holdings and separately identified opinion authority; neither substitutes a possible defect for this record's missing whole-policy substantiality showing.''',
'Law After Decision':'''Lower courts must distinguish permission to present a third-party overbreadth claim from proof that the actual rule substantially burdens protected expression relative to its legitimate operation. This trespass policy's wholesale invalidation cannot stand on the showing made. Preserved narrower claims remain governed by their own expressive-access and state-law rules, including functional forum analysis and lawful severability.''',
'Separate Writings':'',
'Procedure After Action':'The case returns to the Supreme Court of Virginia to identify and adjudicate the remaining preserved grounds and enter the criminal disposition they support. Any severance follows state law. The rejected inference from permission discretion alone cannot sustain continued whole-policy invalidation.',
'Source Notes':'No. 02-371; 539 U.S. 113; Broadrick v. Oklahoma, 413 U.S. 601; ASARCO Inc. v. Kadish, 490 U.S. 605. The arrested conduct is not asserted to be protected expression; the specific expressive-permission applications and forum classification remain subject to their own preserved record.'
})

draft(
case='Overton v. Bazzetta',number=154,docket='02-94',citation='539 U.S. 126',date='2003-06-16',argued='2003-03-26',filename='Overton-v-Bazzetta_merits_2003-06-16.md',
result='Reverse the facial invalidation of the child-visitor, former-prisoner, and substance-abuse visitation restrictions and the facial Eighth Amendment judgment, 9–0, and remand.',
form='One signed lead opinion has three genuine parts: I, compatible surviving family association and the governing Turner standard; II, the three provision-specific facial Turner applications; III, the bounded Eighth Amendment application. Seven join Part I: Stone-Zsela, Stevens, O\'Connor, Kennedy, Souter, Ginsburg, and Breyer. All eight Associates join Part II. All nine join Part III. A single author from the six Associates supporting every part can carry the complete opinion. Stone writes a concurrence addressing his Part-II judgment-only relationship and the actual-application qualifications. Scalia and Thomas join Parts II and III as sufficient applications and withhold Part I; their broader antecedent-entitlement disagreement appears as a joint concurrence in the judgment as to Part I. This form follows the actual propositions and frozen differences before assignment counts.',
compat='Stone\'s primary position remains preserved verbatim above: targeted protection against the automatic minimum and provision-specific reconsideration of the other restrictions, with a proposed effective-cure presumption and all PLRA qualifications. The actual Court, on eight frozen Associate votes, expressly holds the facial showing insufficient for each challenged association component. This satisfies his precise approved trigger, "If the facial showing is held insufficient," rather than treating disagreement alone as a trigger. His conditional disposition therefore reverses these unsupported facial components while preserving concrete indefinite-suspension, arbitrary-restoration, and unavailable-realistic-contact claims. The condition expressly gives greater weight to institutional predictions but preserves the retained interest. He joins Part I\'s compatible-surviving-association rule and standard, and Part III\'s independent objective-threshold rejection. His conditional judgment does not adopt every evaluative inference supporting Part II; that relationship is judgment-only. The primary effective-cure presumption, remedial implementation procedure, and transition for that proposed rule do not activate because the facial violation it would cure is not established. They remain approved private alternatives, not current law or a separate public remedial holding. No standing fallback is used. No full-opinion author eligibility is attributed to Stone.',
continuity='Chief Justice Stone-Zsela\'s concurrence preserves the significance of actual alternatives and the difference between two-year eligibility and guaranteed restoration. It accepts reversal of the insufficient facial showing while requiring concrete indefinite, arbitrary, or dangerous applications to be tested under their own facts. His proposed facial invalidation and effective-cure presumption do not become published law. Scalia\'s concurrence, joined by Thomas, accepts Turner as a sufficient alternative for these applications and binding Farmer as in Delaney, while withholding recognition of a general entitlement to visitation assistance. Their distinction between a retained compatible liberty and an affirmative institutional service remains noncontrolling. The six overlapping Associates adopt the whole lead opinion. Future prospective relief remains subject to amended §3626, including the federal-law-requirement condition; this event supplies no new prison decree.',
sources='The frozen neutral packet and its mechanically copied Overton regulation supplement establish the exact child, escort, former-prisoner, approved-list, disciplinary, and restoration qualifications. The neutral facts distinguish actual letters and calls from nominal substitutes and supply no individual restoration outcome. The reconciliation metadata and official Reports establish argument date and review route. Official cross-check: https://tile.loc.gov/storage-services/service/ll/usrep/usrep539/usrep539126/usrep539126.pdf. The issue slice supplies Turner, Pell, Shaw, Gerber\'s public holdings and Scalia/Thomas dissent, Farmer, Helling, Delaney, and amended §3626. Its older Helling/Farmer current-force quotation uses the original federal-permission formulation; the controlling selected Standards entry expressly records the November 26, 1997 amendment requiring federal law to require any contrary-to-state-law relief. That dated statutory update controls.',
eligible=SIX,
blocks={
'Event':'''Overton v. Bazzetta, No. 02-94, 539 U.S. 126. Merits decision, June 16, 2003. Argued March 26, 2003. On writ of certiorari to the United States Court of Appeals for the Sixth Circuit, which affirmed facial invalidation of Michigan's noncontact-visitation restrictions. The questions concern surviving association under the First and Fourteenth Amendments, the restrictions' relationship to legitimate penological interests, and the Eighth Amendment.

The approved visitor list allows unlimited immediate family and ten other designated visitors, subject to the governing restrictions; qualified clergy and attorneys on official business need not be listed. Visitors under eighteen must be the inmate's children, stepchildren, grandchildren, or siblings. A child may not visit after the inmate's parental rights have been terminated. An eligible child must be accompanied by an adult who is an immediate family member of the child or inmate, or the child's legal guardian. A former prisoner must be immediate family and obtain the warden's prior approval. Repeated substance-abuse violations suspend ordinary visits while preserving attorney and clergy access; the inmate may apply after two years for restoration in the warden's discretion.''',
'Participation':'All nine Justices participated: Stone-Zsela, Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, and Breyer.',
'Public Action':'The facial judgment is reversed, and the case is remanded.',
'Judgment & Remedy':'''**Judgment:** Reversed and remanded, 9–0, on each of the child-visitor, former-prisoner, and repeated-substance-abuse visitation components and the independent facial Eighth Amendment ground.

**Supporting each component:** Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer.

The lower courts must remove the facial injunction and conduct any properly remaining proceedings under the governing constitutional rules. Concrete claims of indefinite suspension, arbitrary restoration, or absence of realistic contact retain their own factual and legal inquiry.''',
'Opinion Topology':'''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | __LEAD_AUTHOR__ | __LEAD_JOINERS__ (all parts); Stone-Zsela (Parts I and III); Scalia and Thomas (Parts II and III) | Reversal and remand on every component | The six full supporters join Parts I–III; Stone-Zsela concurs in the judgment on Part II; Scalia and Thomas concur in the judgment on Part I |
| Opinion concurring in part and concurring in the judgment | Stone-Zsela | — | Joins Parts I and III and the judgment on Part II | Facial sufficiency and concrete application limits |
| Opinion concurring in part and concurring in the judgment | Scalia | Thomas | Joins Parts II and III and the judgment on Part I | Sufficient alternative applications without a general institutional-assistance entitlement |''',
'Holdings':'''### I. Compatible family association and the governing standard

**Holding and operative rule:** Incarceration does not extinguish protected family association that is compatible with confinement. Restrictions on the retained interest are governed by Turner's reasonable relationship to legitimate penological objectives, considering the rational connection, actual alternative means, institutional impact of accommodation, and ready alternatives; the standard does not demand the least restrictive means.

**Authority:** Part I of the Opinion of the Court, directly supported by Stone-Zsela, Stevens, O'Connor, Kennedy, Souter, Ginsburg, and Breyer. Scalia and Thomas join the subsequent applications as sufficient alternatives rather than this recognition of the retained interest.

**Controlling explanation:** Pell recognizes that custody permits substantial communication restrictions while leaving compatible constitutional protection. Turner makes that protection responsive to actual institutional conditions. Shaw applies the ordinary inquiry without a heightened tier, and Gerber requires an operational examination of a claimed compatible interest rather than categorical dismissal. Prisoners must establish the burden and the absence of the required reasonable relationship. Officials must identify legitimate, neutral objectives and supported connections, receiving the latitude inherent in prison administration. Actual letters, telephone calls, supervision, capacity, and security therefore matter; none is conclusive merely because it appears in a regulation. This protection does not entail unrestricted visits or every preferred visitor. It provides the standard for reviewing the restrictions actually challenged.

### II. The three challenged regulatory designs

**Holding and operative rule — child visitors:** The facial showing is insufficient to invalidate the limitation of under-eighteen visitors to the inmate's children, stepchildren, grandchildren, and siblings, the exclusion of a child after parental rights terminate, or the requirement of accompaniment by an adult immediate family member of the child or inmate or the child's legal guardian. These provisions bear a reasonable relationship to child protection and orderly supervision under Turner.

**Authority:** Part II of the Opinion of the Court, directly joined by Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, and Breyer. Stone-Zsela concurs in the judgment on these applications.

**Controlling explanation:** The limits reduce the number and variety of children prison personnel must supervise and protect children visiting a custodial environment. The escort rule permits responsible family members on either side of the relationship and legal guardians; it does not confine accompaniment to one particular adult. The terminated-rights restriction respects the legal severance of that parental relationship. Noncontact design reduces some physical-transfer risks, but does not eliminate child welfare and supervision. Remaining communication and the institutional effects of broader accommodation support the restrictions. The record supplies no ready alternative that achieves those objectives at only negligible institutional cost. Turner consequently does not justify facial invalidation.

**Holding and operative rule — former prisoners:** Requiring a former prisoner both to be immediate family and to obtain the warden's prior approval survives this facial Turner challenge because it reasonably addresses security and renewed criminal contacts while preserving an approved family exception.

**Authority:** The same eight-Justice Part-II coalition.

**Controlling explanation:** The State may take account of the risks associated with a former prisoner's return without treating every relative as automatically eligible or categorically excluded. The family exception and prior-approval requirement work together. Noncontact visits still entail supervision, contacts within the institution, and resource demands. Turner permits these reasonable administrative predictions, and the challengers have not demonstrated an equally effective ready alternative imposing only negligible costs. Ordinary communication alternatives remain relevant without being ideal substitutes for a visit.

**Holding and operative rule — repeated substance abuse:** The record does not establish facial invalidity of suspending ordinary visits after repeated substance-abuse violations, preserving attorney and clergy visits, and allowing an application for discretionary restoration after two years. Deterrence, remaining communication, and institutional costs establish a sufficient Turner relationship on this facial showing; two years marks eligibility to apply, not guaranteed restoration or a constitutional safe harbor for every later duration.

**Authority:** The same eight-Justice Part-II coalition.

**Controlling explanation:** Drug and alcohol discipline serves a legitimate institutional objective, and loss of ordinary visitation can deter repeated violations even when the violation did not occur during a visit. The noncontact setting therefore does not defeat the disciplinary connection. Attorney and clergy access remains, and letters and calls supply additional means of communication whose actual utility matters. A less severe sanction is not a ready alternative merely because it is less severe; the challenger must show the relevant negligible-cost alternative under Turner. The facial record does not establish that restoration discretion necessarily produces permanent or arbitrary exclusion. Concrete indefinite suspensions, irrational denials, or an actual absence of realistic contact require the governing test on their own facts.

### III. The separate Eighth Amendment claim

**Holding and operative rule:** Loss of ordinary visitation does not by itself establish objectively serious deprivation or a substantial risk of serious harm. The challenged regulatory design and this facial record fail that threshold under Wilson, Farmer, Helling, and Delaney, so the independent facial Eighth Amendment judgment cannot stand.

**Authority:** Part III of the Opinion of the Court, directly joined by all nine Justices as a bounded application of the governing conditions rules.

**Controlling explanation:** Wilson separates objective seriousness from culpability. Farmer requires actual appreciation and unreasonable disregard of a substantial danger; Helling permits prevention of an intolerable serious future risk, and Delaney applies that framework to an established serious deprivation rather than a disciplinary label. Ordinary visits, their duration, and the actual available contact must be assessed together. The design shown here does not establish the grave deprivation required for this facial claim. A proved severe or dangerous later application remains subject to the conditions rules. Actual knowledge may be shown circumstantially, but obviousness does not compel the inference; an objectively reasonable response defeats deliberate indifference. Preventive relief requires a current serious danger and knowing unreasonable nonresponse likely to continue. An association injury cannot substitute for these distinct elements.''',
'Precedent Treatment':'''- Turner v. Safley retains its unified, deferential operational inquiry and is applied separately to each restriction.
- Pell v. Procunier supplies compatible surviving communication protection within custody.
- Shaw v. Murphy preserves the ordinary Turner standard without a special content-based enhancement.
- Gerber v. Hickman retains actual review of a claimed compatible interest; the present record supports different provision-specific applications.
- Wilson v. Seiter retains separate objective and subjective requirements.
- Farmer v. Brennan retains actual awareness, circumstantial proof, reasonable-response protection, and current-danger requirements.
- Helling v. McKinney retains preventive protection against a proved intolerable serious future risk.
- Delaney v. DeTella supplies the binding conditions framework without making duration or a disciplinary label conclusive.
- Lewis v. Casey retains the actual-injury boundary and statutory conditions for any future prison decree.''',
'Law After Decision':'''The challenged designs survive facial review under Turner, while compatible family association remains protected through its operational standard. The two-year restoration point permits an application; the lawfulness of concrete later duration, denial, and actual communication conditions is judged on those facts. The independent Eighth Amendment elements remain distinct. Any later federal prison-conditions prospective relief must satisfy amended 18 U.S.C. §3626: necessity to correct the proved federal violation, narrow drawing, least intrusive effective means, and substantial weight to adverse public-safety and criminal-justice effects. Relief contrary to state or local law additionally requires that federal law require it, that it be necessary, and that no other relief correct the violation; existing supported findings may meet those requirements.''',
'Separate Writings':'''**Stone-Zsela, concurring in part and concurring in the judgment.** The Chief Justice joins the retained-association standard and the independent Eighth Amendment application. He accepts reversal of the insufficient facial showing on the association components while emphasizing the need to examine real family contact. The two-strike minimum creates a serious fit concern because the substance violation need not involve visitation, and eligibility to request restoration is no guaranteed end to separation. Giving institutional predictions greater weight for this facial disposition still leaves concrete indefinite suspension, arbitrary restoration, and an absence of realistic alternatives subject to actual review. A proved conditions claim must independently establish serious danger and culpability, and a resulting decree must satisfy the PLRA.

**Scalia, concurring in part and concurring in the judgment, joined by Thomas.** They accept the full Turner applications as sufficient to reject these facial claims and the bounded Farmer application as in Delaney. Their Gerber distinction between a compatible liberty and a claimed entitlement to institutional assistance leads them to withhold the broader retained-visitation recognition in Part I. The accepted applications do not require that recognition. They preserve review of rights actually retained and do not replace binding conditions law with categorical immunity for a disciplinary label.''',
'Procedure After Action':'The case returns for removal of the facial injunction and any properly remaining proceedings. A supported concrete claim must be evaluated under its own association or Eighth Amendment elements, and any prospective decree must satisfy the applicable amended §3626 findings.',
'Source Notes':'No. 02-94; 539 U.S. 126; Michigan Administrative Code Rule 791.6609 (1999); Michigan Compiled Laws §791.268a; 18 U.S.C. §3626(a)(1). The restoration rule permits an application after two years and leaves reinstatement to the warden; this facial record supplies no individual restoration outcome.'
})

draft(
case='United States v. American Library Association, Inc.',number=159,docket='02-361',citation='539 U.S. 194',date='2003-06-23',argued='2003-03-05',filename='United-States-v-American-Library-Association_merits_2003-06-23.md',
result='Reverse both library-program facial invalidations and remand for judgment rejecting the facial claims, 5–4.',
form='One signed Opinion of the Court states Part I, the common statutory permission and distinct program boundaries, with nine direct joins, and Part II, the directly shared record-specific facial conclusion, with O\'Connor, Scalia, Kennedy, Thomas, and Breyer. Those five support every governing proposition of the lead opinion and are eligible authors. O\'Connor is the senior participating Justice in the judgment majority and assigns. Additional signed concurrences preserve O\'Connor\'s service ground with Scalia and Thomas, Kennedy\'s practical-access ground, and Breyer\'s contextual scrutiny; these are independent differences, not a unified five-Justice general forum or subsidy theory. Stevens, Souter with Ginsburg, and Stone write distinct dissents. All four dissenters join Part I alone. No Marks aggregation is used: Part II has five direct proposition-level joins. Form and propositions precede counts or author selection.',
compat='Stone joins only Part I\'s permissible disabling construction and operative statutory boundaries. His primary judgment remains affirmance of protection against the mandatory-filter funding conditions. He adopts strict scrutiny after the challengers\' distinct substantial-overbreadth showing, regards the trial-established blocking and practical barriers as sufficient, applies Dole\'s unconstitutional-condition limit, and proposes his actual-common-barrier effective-cure presumption bounded by jurisdiction, injury, program distinctions, and severability. His alternative vacatur/remand branch applies only if the disabling construction requires fresh factual or remedial assessment. The construction here is already the one his primary position expressly accepts: a whole-session adult request for lawful reading without explanation, as permission rather than proof of performance. Neither a new construction nor a new material factual premise is introduced. The other Justices\' different appraisal of the same showing does not activate his condition. Stone therefore dissents; he is not converted to a vacatur vote or the majority\'s facial rejection. He joins no broader service, forum, government-message, or subsidy rationale. No standing fallback or substantive narrowing is used. His proposed remedy and scrutiny remain noncontrolling. HICKS_REFRESH_PENDING',
continuity='The controlling propositions are limited to the statutory permission and directly shared facial insufficiency on this record. O\'Connor, joined by Scalia and Thomas, publishes the particular funded-service ground together with meaningful adult access; their three votes establish no broader Court doctrine. Kennedy publishes a practical-access ground focused on significant final access burdens and concrete denial, delay, disclosure, or obstruction. Breyer publishes contextual means scrutiny balancing the specific burdens, purposes, and lawful adult request rather than ordinary rational-basis review. Stevens publishes the distinction between local selection and a compulsory nationwide condition on an opened resource. Souter, joined by Ginsburg, publishes the distinction between statutory discretion and assured effective access and supports fitted adult relief with independent minor-use provisions preserved. Stone publishes strict scrutiny for the compelled adult restriction and his bounded effective-cure remedy proposal, retaining the injunction. These positions are noncontrolling except where the five directly join Part II or all nine join Part I. No general Marks rationale is recognized.',
sources='The neutral packet establishes the two statutory programs, filtering/overblocking record, Government representation, trial concerns, parties, and three-judge judgment. The reconciliation metadata and official Reports establish March 5 argument and direct appellate review. Exact text is in terms/OT2002/entering-law/OT_2002CHUNK13_A_STATUTES.md; official sources are https://www.govinfo.gov/content/pkg/USCODE-2002-title20/html/USCODE-2002-title20-chap72-subchapII-part1-sec9134.htm and https://www.govinfo.gov/content/pkg/USCODE-2002-title47/html/USCODE-2002-title47-chap5-subchapII-partII-sec254.htm. Official fact cross-check: https://tile.loc.gov/storage-services/service/ll/usrep/usrep539/usrep539194/usrep539194.pdf. The issue slice supplies the exact controlling Reno, Denver, Forbes, Finley, Rosenberger, Velazquez, Free Speech Coalition, and Center for Reproductive Law holdings; prior separate positions are copied in OT_2002CHUNK13_A_PUBLIC_WRITINGS.md. The June 16 Hicks public-law dependency requires the exact completed projection before final publication. No finding of universally prompt access or uniformly obstructed whole-session requests is added.',
eligible=["O'Connor",'Scalia','Kennedy','Thomas','Breyer'],assigner="O'Connor",
authority='O\'Connor is the most senior participating Associate Justice among the five supporting reversal. Stone-Zsela and Stevens oppose reversal. Her assignment must preserve the direct shared facial ground and the independently published differences; the Chief\'s mandatory balance-pool rule does not govern her assignment, although the resulting signed lead opinion counts.',
blocks={
'Event':'''United States v. American Library Association, Inc., No. 02-361, 539 U.S. 194. Merits decision, June 23, 2003. Argued March 5, 2003. On direct appeal from a three-judge United States District Court for the Eastern District of Pennsylvania, which held the Children's Internet Protection Act's challenged library-filtering conditions facially unconstitutional and enjoined denial of the covered federal assistance. The questions are whether the conditions violate the First Amendment or exceed Congress's spending authority.

The conditions cover specified E-rate assistance under 47 U.S.C. §254(h)(6) and Library Services and Technology Act assistance under 20 U.S.C. §9134(f). They require protection against visual depictions of obscenity and child pornography, and, for users under seventeen, material harmful to minors. Commercial filters both miss prohibited material and block substantial lawful material. The Government represented that an adult may request disabling of the entire filter without explaining a reason. The District Court identified delay, staffing, privacy, and deterrence concerns.''',
'Participation':'All nine Justices participated: Stone-Zsela, Stevens, O\'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, and Breyer.',
'Public Action':'The facial judgment concerning both library programs is reversed, and the case is remanded.',
'Judgment & Remedy':'''**Judgment:** Reversed and remanded, 5–4, as to the facial invalidation and injunction under both E-rate and LSTA.

**Supporting:** O'Connor, Scalia, Kennedy, Thomas, Breyer.

**Opposing:** Stone-Zsela, Stevens, Souter, Ginsburg.

The District Court must enter judgment rejecting the facial claims and remove the injunction founded on them. Stone-Zsela would retain the injunction against the challenged conditions. Stevens, Souter, and Ginsburg would retain adult-access protection and return the decree for fitting to the distinct programs, lawful separability, and independently operable minor-use provisions.''',
'Opinion Topology':'''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | __LEAD_AUTHOR__ | __LEAD_JOINERS__ (Parts I and II); Stone-Zsela, Stevens, Souter, Ginsburg (Part I only) | Reversal and remand | Part I: statutory permission and boundaries; Part II: directly shared facial conclusion |
| Concurring opinion | O'Connor | Scalia, Thomas | Supports reversal | Particular library-service explanation in addition to the common holdings |
| Concurring opinion | Kennedy | — | Supports reversal | Practical adult-access ground and concrete application review |
| Concurring opinion | Breyer | — | Supports reversal | Contextual means scrutiny and proportionality |
| Opinion concurring in part and dissenting in part | Stevens | — | Joins Part I; opposes facial rejection | Local selection versus compulsory federal restriction; fitted adult-access protection |
| Opinion concurring in part and dissenting in part | Souter | Ginsburg | Joins Part I; opposes facial rejection | Discretionary permission versus effective access; fitted adult relief |
| Opinion concurring in part and dissenting in part | Stone-Zsela | — | Joins Part I; would retain the injunction | Strict scrutiny, unconstitutional conditions, and bounded effective-cure relief |''',
'Holdings':'''### I. Lawful disabling and the distinct funding conditions

**Holding and operative rule:** The statutes permit disabling for bona fide research or other lawful purposes, which are alternative grounds; an adult may request an entire unfiltered session for lawful reading without identifying sites or explaining a purpose. E-rate's disabling clause expressly applies during adult use, whereas LSTA's clause contains no adult-use limitation. This is statutory permission, not a command that every request be granted or a factual finding that effective access exists at every library.

**Authority:** Part I of the Opinion of the Court, directly joined by all nine Justices.

**Controlling explanation:** The text permits an authorized person to disable the technology protection measure for lawful purposes. Ordinary lawful reading fits that term without a patron's explaining a research project or identifying a particular blocked page. The Government's representation accords with that permissible reading. It narrows the claimed statutory burden but does not establish what every library actually does. The express adult-use language in §254(h)(6)(D) cannot be inserted into §9134(f)(3), and permission cannot be rewritten as a mandatory-access guarantee. The Court assesses the facial claim under this construction and the conditions' actual scope.

**Program boundaries:** LSTA's identified computer-purchase and direct Internet-cost restriction applies to a covered library that does not receive the specified discounted services. E-rate's condition excludes libraries receiving discounted services solely for purposes other than Internet access, Internet service, or internal connections. The required technology covers Internet-access computers; obscenity and child pornography are the adult categories, with the additional harmful-to-minors category for users under seventeen. Harmful-to-minors material must satisfy all three statutory elements: taken as a whole and with respect to minors, prurient appeal in nudity, sex, or excretion; a patently offensive depiction, description, or representation, with respect to suitability for minors, of actual or simulated sexual acts or contact, normal or perverted sexual acts, or lewd exhibition of genitals; and, taken as a whole, lack of serious literary, artistic, political, or scientific value as to minors. The child-pornography cross-reference operates subject to Free Speech Coalition's existing protection of nonobscene material made without actual-child exploitation; incorporation does not restore its invalidated protected coverage.

### II. The present facial speech and spending challenges

**Holding and operative rule:** Under the permitted whole-session, explanation-free adult-access construction, the present record of overblocking and practical concerns does not establish substantial unconstitutional adult exclusion relative to the conditions' legitimate operation sufficient to invalidate either funding program on its face. The dependent claim that these conditions induce unconstitutional library conduct therefore supplies no ground for this facial injunction; a significant actual denial, material delay, compelled disclosure, or other substantial access obstruction remains subject to an appropriately supported challenge.

**Authority:** Part II of the Opinion of the Court. O'Connor, Scalia, Kennedy, Thomas, and Breyer directly join this exact proposition and the mandate; its force does not depend on combining their different broader explanations under Marks.

**Controlling explanation:** Broadrick and Hicks require a supported comparison of substantial protected reach with legitimate operation. Reno protects lawful adult Internet expression, and Denver requires attention to real access burdens rather than a nominal alternative. Neither decision makes an ordinary lawful whole-session request equivalent to the compulsory restrictions adjudicated there. Filtering's errors and practical concerns must be considered together with the permission to obtain an unfiltered adult session without disclosing a reason.

The dissent argues that systematic default blocking and discretionary release themselves establish the necessary substantial burden. That is the central disagreement. The record does establish substantial overblocking and practical concerns, but does not establish a significant obstruction of the lawful adult election sufficient to sustain this facial decree. Statutory permission is not proof that every request is honored, and the Court does not treat one conceivable lawful implementation as dispositive. Its conclusion concerns the showing across the conditions' operation, with the lawful adult-access route included.

Dole retains the bar on conditions inducing unconstitutional conduct. The funding relationship alone cannot answer an established speech burden. Here the predicate substantial unconstitutional adult exclusion needed for the facial relief has not been established under the permissible construction. Accordingly, both the speech and dependent spending grounds fail for this facial injunction. Materially obstructive actual administration remains subject to constitutional review on its own supported record.''',
'Precedent Treatment':'''- Broadrick v. Oklahoma and Virginia v. Hicks supply substantial-overbreadth review of the actual challenged operation, distinct from standing and from an every-application requirement.
- Reno v. American Civil Liberties Union retains protection of lawful adult Internet expression; its criminal restriction differs from the present funding and disabling arrangement.
- Denver Area Educational Telecommunications Consortium v. FCC retains its rejection of the integral compulsory delayed-access system and its distinction from ordinary voluntary requests.
- South Dakota v. Dole retains the constitutional limits on conditional spending, including the prohibition on inducing unconstitutional conduct.
- Arkansas Educational Television Commission v. Forbes and National Endowment for the Arts v. Finley retain their actual selective-programming holdings; their force remains tied to the program and restriction adjudicated.
- Rosenberger v. Rector and Visitors of the University of Virginia, Legal Services Corp. v. Velazquez, and Center for Reproductive Law and Policy v. Bush retain protection of the independent expression within their actual benefit and program settings.
- Ashcroft v. Free Speech Coalition continues to govern the protected reach of the incorporated child-pornography definitions.''',
'Law After Decision':'''The two statutory funding conditions remain applicable according to their distinct terms, including lawful disabling, while the facial injunction is removed. Adults may request whole-session disabling for lawful reading without identifying sites or explaining reasons. Significant actual denial, delay, disclosure burdens, or other substantial obstruction must be evaluated on a supported record. The common holding resolves this facial showing; the independently published service and scrutiny explanations retain their stated, different coalitions.''',
'Separate Writings':'''**O'Connor, concurring, joined by Scalia and Thomas.** These Justices consider the actual service Congress assists together with the lawful adult election. Libraries exercise selection in providing a usable resource, and Forbes and Finley protect genuine institutional selection within their respective programs. Filtering aimed at unlawful material and protection of minors, coupled with permitted explanation-free adult access, fits this assisted service sufficiently to defeat the facial challenge. Their ground addresses this library design; funding terminology does not create immunity for material unconstitutional administration or penalties on independent expression.

**Kennedy, concurring.** Prompt whole-session disabling without explanation would leave no substantial adult-access burden. The record establishes overblocking and practical concerns but does not establish a significant burden on that lawful election sufficient for the facial decree. The difference from Denver's compulsory access machinery is material. Actual denial, material delay, disclosure requirements, or another substantial obstruction would call for review of the practice that produces it. Kennedy joins the common construction and record-specific facial conclusion rather than the broader institutional-service explanation.

**Breyer, concurring.** The constitutional inquiry should examine this program's actual burden and means. Protection against unlawful images and minors' exposure are serious interests; imperfect filters impose burdens, but the lawful whole-session request matters to their extent. On this record the request burden does not produce disproportionate harm sufficient to invalidate the conditions facially. This contextual scrutiny is more demanding than ordinary rational-basis review and does not rest on rigid forum classification. Materially obstructive local practices remain separately reviewable.

**Stevens, concurring in part and dissenting in part.** Local librarians' selection differs from a nationwide condition compelling filters across an otherwise opened Internet resource. The default barrier burdens readers and authors whose lawful material the filters remove. Permitting a request does not eliminate the burden of asking or the discretion surrounding release. Reno, Denver, Velazquez, and Center for Reproductive Law require attention to that actual private-expression burden. Stevens would retain protection for adults and remand to fit the decree to the distinct statutory provisions and independently lawful minor protections.

**Souter, concurring in part and dissenting in part, joined by Ginsburg.** Acquiring selected material and blocking an acquired open resource are different acts. Extensive overblocking and discretionary release establish substantial protected reach in their assessment. Part I correctly permits an explanation-free whole-session request, but its permission does not entitle every patron to an unblocked terminal or establish effective performance. The delay and privacy concerns therefore cannot be answered as though Congress guaranteed prompt release. Reno, Denver, and Velazquez protect the actual access path, while Finley's bounded selection holding does not settle compulsory blocking. They would preserve fitted adult-access relief, with LSTA separability and independently operable minor-use provisions respected.

**Stone-Zsela, concurring in part and dissenting in part.** The Chief Justice joins the permissible disabling construction but finds substantial unconstitutional adult restriction on the developed record. The challengers must establish substantial protected reach relative to legitimate applications; one possible lawful implementation does not defeat that showing. Once the compulsory adult burden is shown, Reno's demanding protection requires a compelling interest and narrow tailoring, including why feasible less restrictive means cannot adequately serve the interest. Child protection may be compelling, but does not justify suppressing adults' lawful reading through an ineffective access route.

The filters' overblocking, requests to staff, waiting, privacy loss, and deterrence remain practical burdens despite statutory permission. A genuinely selective acquisition decision differs from compulsory exclusion across an otherwise opened adult Internet service. Forbes and Finley protect actual selection; they do not turn this requirement into the library's own message. Dole prevents funding conditions from inducing the unconstitutional operation.

He would retain the injunction against denying the covered assistance for noncompliance with the offending conditions. Lewis v. Casey confines relief to the actual common barrier and affected persons. Within injury, jurisdiction, severability, and the two programs' distinct boundaries, he would presume condition-level relief unless the Government demonstrates a narrower complete cure. That is his proposed remedial rule. A proposed cure must actually address prompt disabling, privacy, staffing, and deterrence; written assurances alone are insufficient. Lawful eligibility criteria, child protections, precise unlawful-material restrictions, voluntary collection choices, and unrelated grants remain available.''',
'Procedure After Action':'The case returns to the three-judge District Court for entry of judgment rejecting the facial claims and removal of the injunction resting on them. The separate statutory funding and compliance provisions then govern within their own terms. A supported challenge to materially obstructive administration receives the constitutional inquiry appropriate to that actual practice.',
'Source Notes':'No. 02-361; 539 U.S. 194; 20 U.S.C. §9134(f); 47 U.S.C. §254(h)(6)–(7). The Government\'s representation permits an adult request without explanation; it is distinct from the District Court\'s findings and concerns about how filtering and release operate.'
})

(OUT/'A_specs.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Wrote', len(data), 'drafts and A_specs.json')
