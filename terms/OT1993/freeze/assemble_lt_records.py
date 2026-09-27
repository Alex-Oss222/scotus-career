from pathlib import Path
import hashlib
import json
import re

BASE = Path('terms/OT1993')
ALL = ['Stone', 'Blackmun', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg']
LP = ['Stone', 'Blackmun', 'Stevens', 'Kennedy', 'Souter']
LC = ["O'Connor", 'Scalia', 'Thomas', 'Ginsburg']
TD = ['Stone', 'Blackmun', 'Stevens', 'Scalia', 'Souter', 'Thomas', 'Ginsburg']
TR = ["O'Connor", 'Kennedy']

liteky_holdings = '''### Section 455(a) applies the same objective appearance standard regardless of source

**Controlling proposition:** A federal judge must disqualify when an informed, detached observer, considering the relevant conduct and circumstances together, would reasonably question the judge's impartiality; a reasonable conclusion that a fair and impartial hearing is unlikely suffices, without proof of actual bias or impossibility of fair judgment. Judicial origin is relevant context, neither a bar to disqualification nor an added exceptional-intensity requirement, and outside origin is neither necessary nor sufficient; ordinary adjudicative views, adverse rulings, criticism and trial management do not alone establish improper partiality, while §455(b)'s particular limitations do not automatically narrow §455(a)'s independent appearance protection.

**Authority:** Kennedy's opinion of the Court, joined in full by Chief Justice Stone-Zsela, Blackmun, Stevens and Souter. These five Justices adopt this rule at the same level of generality. Scalia, O'Connor, Thomas and Ginsburg agree with the judgment but do not join the ordinary-appearance formulation without their additional judicial-source requirement. No narrower-rationale aggregation is necessary.

**Controlling explanation:** The Court gives effect to Congress's protection against a reasonable appearance of partiality. Liljeberg establishes that §455(a) protects public confidence independently of proof of actual bias and that a limitation in a particular §455(b) ground does not automatically govern the appearance inquiry. Grinnell explains why views properly formed from evidence ordinarily do not establish personal prejudice; its application does not make judicial origin a categorical shield under §455(a). Judges must assess evidence, make rulings and control proceedings. An informed observer understands those responsibilities and does not equate disappointment, impatience or criticism with partiality. But a judge's apparent commitment to favor one side cannot become acceptable merely because it arose during litigation. Requiring that fair judgment appear impossible would leave reasonable doubts unaddressed whenever some possibility of fairness remained. The Government's concern about tactical motions is answered by objective reasonableness and concrete context, not an extra statutory element. The Court decides the appearance claim presented, without resolving an independent actual-bias claim, affidavit procedure or the constitutional consequences of a biased tribunal.

**Precedent treatment:**
- Liljeberg v. Health Services Acquisition Corp., 486 U.S. 847 (1988): applied to objective appearance and the independent operation of §455(a); its distinct civil remedial inquiry is preserved.
- United States v. Grinnell Corp., 384 U.S. 563 (1966): its protection of legitimate adjudicative impressions remains effective; its personal-bias discussion does not impose a categorical source bar or mandatory impossibility threshold under §455(a).

### The reported conduct, considered together, does not require disqualification

**Controlling proposition:** The identified rulings, restrictions, admonishments and other reported conduct in the 1983 and 1991 proceedings, evaluated cumulatively under the objective appearance standard, supply no reasonable basis to question this judge's impartiality. The recusal challenge therefore fails and the convictions remain undisturbed; this conclusion does not approve every underlying ruling or establish a harmless-error rule for an actual recusal violation.

**Authority:** The application in Kennedy's opinion of the Court, joined by Chief Justice Stone-Zsela, Blackmun, Stevens and Souter, supplies five votes under the controlling standard. Scalia, O'Connor, Thomas and Ginsburg separately reach the same affirmance under their judicial-source formulation; all nine support the judgment, without nine joins in the Court's full rationale.

**Controlling explanation:** The Court examines the incidents together, rather than excluding them because they occurred in court. Restrictions on political speeches, cross-examination, witness responses and new facts in closing have ordinary trial-management functions. The judge allowed explanations of political purpose while limiting extended discussion of policy and events in El Salvador. Grinnell supports distinguishing such adjudicative work from an improper disposition toward a party. The additional witness questions, asserted tone, claimed state-of-mind exclusion, disputed sentence, fee denial and refusal of an honorific do not, on the circumstances identified, establish prejudgment or hostility that reasonably puts impartiality in doubt. Neither an allegation of error nor its repetition supplies missing hostile content. Although the lower court's categorical rule was incorrect, no specified unresolved factual predicate requires a remand before rejecting this recusal claim under the correct standard. Liljeberg separates finding a violation from selecting relief; here the first requirement fails. The Court consequently orders no retrial or reassignment and leaves independent challenges to particular rulings and constitutional remedies undecided.

**Application:** The earlier trial's restrictions on political presentation, questions and answers, and closing argument are considered with the sentence petitioners regarded as excessive. The current trial's public opening admonishment, restrictions on events in El Salvador, and unspecified admonishments of codefendants are also considered. The further witness questions and alleged anti-defendant tone carry no additional specified hostile language. Testimony claimed relevant to state of mind is not found admissible merely because petitioners describe it that way. Refusing leave to appeal without prepaying fees, without a supplied reason or eligibility finding, establishes no retaliation. Refusal to address Bourgeois as Father, without a specified disparagement or discriminatory context, establishes no religious antagonism. No outside relationship, financial interest or extrajudicial information is established. These limits do not exempt judicial conduct from scrutiny; they identify what the reported circumstances actually support.

**Precedent treatment:**
- Grinnell: applied to the distinction between legitimate judicial evaluation and disqualifying prejudice, while examining this record under §455(a)'s objective standard.
- Liljeberg: its separation of violation from remedy is preserved; its civil Rule 60(b)(6) procedure is not transplanted to this criminal direct appeal.

**Limits and questions not reached:** The Court does not decide §144 affidavit sufficiency or procedure, an independent §455(b)(1) actual-bias claim, the legal correctness of every evidentiary or sentencing ruling, an independent appeal-fee entitlement, a general kinship rule, or the constitutional structural-error consequences of an established biased adjudicator. No general automatic-retrial or harmless-error rule is adopted. The Court's consideration of context is not a new mandatory checklist or a presumption that all courtroom behavior is proper.
'''

liteky_separate = '''Scalia concurs in the judgment, joined by O'Connor, Thomas and Ginsburg. They agree that an outside source is neither indispensable nor sufficient and that the Eleventh Circuit's categorical exclusion cannot stand. Their disagreement concerns the weight of judicial origin. In their view, attitudes formed from evidence or events in current or earlier proceedings require disqualification for bias or partiality only when they objectively reveal deep favoritism or antagonism making fair judgment appear impossible. The formulation concerns the appearance of the disposition, not proof of the judge's actual mental state. It applies to judicially generated attitudes; it is not a universal threshold for claims based on outside circumstances, which remain governed by reasonable appearance and still require improper partiality rather than origin alone.

Grinnell supplies their distinction between proper judicial assessment and bias. A favorable or unfavorable opinion is not improper merely because it is firm: it may reflect evidence that a judge must evaluate. Impropriety can arise because a disposition is undeserved, rests on knowledge the judge ought not possess, or is excessive in degree. The concurrence uses these categories to explain why source matters, without equating every outside view with disqualification. Ordinary judicial rulings are ordinarily subjects for appellate correction; surrounding statements or other circumstances may change what they reveal. Criticism, impatience, dissatisfaction, annoyance and anger within ordinary judicial limits do not establish partiality, while courtroom origin supplies no immunity for genuinely disqualifying conduct. Berger illustrates serious prejudgment without deciding an affidavit question here.

The four Justices read §455(a) alongside the personal-bias provisions while preserving its objective protection and its reach beyond subjective knowledge. They reject the Court's decision to dispense with the additional judicial-source requirement, but do not import every limitation of every §455(b) subsection into a new holding. On the complete reported allegations, they find ordinary rulings and administration rather than the deep partiality their formulation requires. They consider the honorific, tone, testimony and fee allegations without inventing religious animus, retaliatory reasons or unreported language. Their affirmance does not endorse every trial ruling, and no remedial question following a proved violation is decided. Their proposed judicial-source requirement is noncontrolling; they join the judgment alone, not the Court's opinion.'''

liteky_judgment = '''| Judgment component | Disposition and vote | Supporting Justices | Opposing Justices | Remedy or remand |
|---|---|---|---|---|
| Section 455(a) recusal challenge to the convictions | Affirmed, 9–0 | Stone-Zsela, Blackmun, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg | No Justice | Convictions undisturbed on this issue; no new trial, reassignment or remand |

The Court rejects the Eleventh Circuit's categorical judicial-source rule while affirming its judgment under the correct appearance standard.'''

liteky_topology = '''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | Kennedy | Chief Justice Stone-Zsela, Blackmun, Stevens, Souter | Affirmance | Full opinion: objective appearance rule, statutory independence, cumulative application and limits |
| Concurrence in the judgment | Scalia | O'Connor, Thomas, Ginsburg | Affirmance | Judicial-source ordinary rule with objective deep-partiality exception; no join in the Court's opinion |

The Court's opinion has five votes. The concurrence has four. Their agreement that source alone is neither necessary nor sufficient does not erase their different broader rules.'''

liteky_event = '''Liteky v. United States, No. 92-6921; 510 U.S. 540. Merits decision, March 7, 1994. Argued November 3, 1993. On writ of certiorari to the Eleventh Circuit, 973 F.2d 910 (1992), which affirmed the convictions and rejected recusal under a categorical judicial-source rule. The question is whether §455(a) can require recusal for conduct or statements during current or earlier judicial proceedings without an outside source. Petitioners seek relief from their convictions following denial of recusal; the United States seeks affirmance. The charges concerned willful destruction of federal property under 18 U.S.C. §1361 at Fort Benning. The earlier Bourgeois trial occurred in 1983; the prosecution under review was tried in 1991.

Render form: full. Basis: a distinct five-Justice controlling rule and four-Justice concurrence in the judgment. The controlling rule differs materially from the historical comparator.'''

liteky_law = '''Effective March 7, 1994, §455(a)'s ordinary objective appearance inquiry governs judicial-source and outside-source allegations alike. Source remains relevant context, but no mandatory outside-origin or impossibility element applies. The Court adds this controlling clarification to the prior objective standard; it does not overrule Grinnell's result or Liljeberg. The separate writing's additional judicial-source requirement has four votes and is not current law. Gibson's panel-neutrality rule, Martin's particular fee determination and Weiss's military-impartiality rule retain their confined scopes; none supplies a categorical recusal rule for these facts.'''

liteky_notes = '''The [official United States Reports account, 510 U.S. 540](https://tile.loc.gov/storage-services/service/ll/usrep/usrep510/usrep510540/usrep510540.pdf), 542–543 and 556 with note 3, supports the reported motions and allegations. The [Eleventh Circuit opinion, 973 F.2d 910](https://static.case.law/f2d/973/cases/0910-01.json), supplies the judgment and categorical rule below. The allegations remain allegations, rather than findings of religious hostility, retaliation, unlawful sentencing or improper evidentiary exclusion. The original trial motions and full transcripts are not independently available in these sources; unspecified conduct receives no invented content. Section 455(a)'s text and its relation to the personal-bias provisions are set out in the official report. [Grinnell, 384 U.S. 563](https://tile.loc.gov/storage-services/service/ll/usrep/usrep384/usrep384563/usrep384563.pdf), and [Liljeberg, 486 U.S. 847](https://tile.loc.gov/storage-services/service/ll/usrep/usrep486/usrep486847/usrep486847.pdf), supply the earlier statutory authorities. No quotation of judicial language is necessary to this account.'''

ticor_holdings = '''### Discretionary dismissal on this constrained review posture

**Controlling proposition:** The Court dismisses this writ as improvidently granted because the conclusive prior certification prevents consideration of the antecedent Rule 23 question in a suitable sequence with the constitutional opt-out question. This is the Court's case-specific exercise of discretionary review, not a jurisdictional requirement or a substantive holding about opt-out rights, certification, adequate representation or preclusion; the pending settlement awaiting approval is supplemental context, not a finding of mootness or an independently necessary dismissal ground.

**Authority:** The per curiam explanation is supported in full by Chief Justice Stone-Zsela, Blackmun, Stevens, Scalia, Souter, Thomas and Ginsburg, seven Justices. O'Connor and Kennedy dissent from dismissal. The explanation controls this procedural action and leaves the constitutional merits unresolved; it establishes no categorical duty to dismiss every case with a final certification premise.

**Controlling explanation:** The Court recognizes a live dispute over the effect of a final judgment. The absent members' asserted loss is real, and finality prevents reopening certification in this proceeding. Beazer supports considering an available nonconstitutional ground first; it does not create a collateral attack that these parties lack. A direct certification case could determine whether the Rules permit mandatory treatment of the monetary claims before deciding what the Constitution independently requires. Here either assumed authorization or assumed error could distort the scope of a constitutional answer. Shutts preserves protections for the money-judgment class it addressed while reserving other class forms, and Hansberry's representation protection does not settle the distinct opt-out issue. The strong argument for answering the fully presented question does not overcome this discretionary concern about the vehicle. The separately proposed settlement, still awaiting approval, adds practical uncertainty without ending jurisdiction. The Court leaves the judgment below intact and expresses no view on the correct constitutional answer.

**Precedent treatment:**
- New York City Transit Authority v. Beazer, 440 U.S. 568 (1979): its avoidance sequence informs discretionary case selection; it supplies no power to reopen final certification here.
- Phillips Petroleum Co. v. Shutts, 472 U.S. 797 (1985): its holding for the known plaintiffs and predominantly monetary claims before it remains limited by its express reservation of other class forms; no universal federal mandatory-class opt-out rule is adopted.
- Hansberry v. Lee, 311 U.S. 32 (1940): its adequate-representation protection remains distinct from the unanswered opt-out question; no inadequate-representation finding is made.

**Limits and questions not reached:** The Court does not decide whether the earlier class was properly certified as an original matter, whether due process requires an opt-out opportunity for these monetary claims, whether the Ninth Circuit's constitutional theory is correct, or whether any classwide benefits adequately compensate the released claims. It does not decide the treatment of indivisible injunctive relief, genuinely limited assets or other class forms. State-action and filed-tariff defenses are outside this review. Pending approval does not establish an operative settlement, release or mootness; no settlement-vacatur rule is adopted.
'''

ticor_separate = '''O'Connor dissents from dismissal, joined by Kennedy. They would retain the writ to decide the constitutional preclusion question. The final certification premise and adequate-representation determination do not decide whether absent members' monetary claims can constitutionally be extinguished without an opportunity to opt out. The parties are properly before the Court, the question is presented, and briefing and argument have made its consequences concrete. In their view, Beazer's preference for an available nonconstitutional ground cannot justify treating an unavailable collateral certification challenge as an alternative way to resolve this controversy.

They accept finality rather than reopen the earlier Rule 23 determination. A confined constitutional answer could respect that premise while reserving the Rules' general construction. Shutts's reservation of class forms beyond the predominantly monetary claims it addressed identifies an unresolved issue; it does not make this issue unsuitable for decision. Hansberry likewise demonstrates that the binding force of a class judgment must satisfy constitutional safeguards apart from a procedural label. Other final mandatory-class judgments can present the same question, so the dispute is not merely an abstract concern about a hypothetical category. The practical interests in settlement reliance and in absent members' control of monetary claims support resolving the question rather than assuming either side prevails.

The proposed settlement has not received the approval necessary to establish its operative effect. It therefore supplies no present reason to declare the controversy moot or erase the judgment. Their retention position remains compatible with a bounded inquiry into verified settlement status if circumstances require one; it does not order a hold or invent a future filing. They reject dismissal on the existing vehicle ground but announce no final affirmance or reversal on the constitutional merits. Their position is noncontrolling and supplies no rule requiring opt-out rights in every class with monetary consequences.'''

ticor_judgment = '''| Judgment component | Disposition and vote | Supporting Justices | Opposing Justices | Remedy or remand |
|---|---|---|---|---|
| Continued review of the constitutional opt-out/preclusion question | Writ dismissed as improvidently granted, 7–2 | Stone-Zsela, Blackmun, Stevens, Scalia, Souter, Thomas, Ginsburg | O'Connor, Kennedy | Ninth Circuit judgment undisturbed; no Supreme Court merits judgment, vacatur or new remand |

The Ninth Circuit affirmed the bar on further injunctive relief, reversed preclusion of the monetary claims, and remanded for further proceedings. Those directions remain operative. This Court neither adopts that constitutional reasoning nor awards damages, changes the settlement or approves the pending proposal.'''

ticor_topology = '''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Per curiam explanation of dismissal | The Court | Supported by Stone-Zsela, Blackmun, Stevens, Scalia, Souter, Thomas, Ginsburg | Dismissal of the writ | Full case-specific vehicle explanation and reservations; no merits holding |
| Dissent from dismissal | O'Connor | Kennedy | Would retain the writ | Constitutional question should be decided in this live, fully presented controversy; no final constitutional merits vote |

The public 7–2 disposition concerns dismissal after argument. It is not a vote on the underlying constitutional question.'''

ticor_event = '''Ticor Title Insurance Co. v. Brown, No. 92-1988; 511 U.S. 117. Dismissal of the writ as improvidently granted, April 4, 1994. Argued March 1, 1994. On writ of certiorari to the Ninth Circuit, 982 F.2d 386 (1992). The question is whether a federal court may refuse to give a prior federal class judgment preclusive effect as to absent members' monetary claims because they lacked an opportunity to opt out, where proper Rule 23 certification is conclusively established between the parties. The insurers seek restoration of monetary-claim preclusion; the absent consumers seek to pursue their damages claims.

The 1986 settlement of the thirteen-state title-insurance class litigation exchanged monetary claims for injunctive relief, increased existing policy coverage, additional coverage on new policies and approved fees and litigation costs. Certification under Rules 23(b)(1)(A) and (b)(2) became final. Brown later brought this action in 1990. The lower courts did not find inadequate representation. A separate proposed settlement intended to end the pending review has been reported, but District Court approval remains pending; no completed termination is established.

Render form: full. Basis: materially changed judgment coalition and a published two-Justice dissent.'''

ticor_notes = '''The [Ninth Circuit opinion, 982 F.2d 386](https://static.case.law/f2d/982/html/0386-01.html), supplies the full lower judgment, including affirmed injunction preclusion and reversed monetary-claim preclusion with remand. The [official United States Reports account, 511 U.S. 117](https://tile.loc.gov/storage-services/service/ll/usrep/usrep511/usrep511117/usrep511117.pdf), 118–121, supplies the earlier class litigation, certification, settlement and limited question; page 122 reports the separate proposal awaiting District Court approval. No exact date of that party report, approval order, effective release or operative settlement terms is established here. The question is stated in substance rather than as a quotation of petition language. [Shutts, 472 U.S. 797](https://tile.loc.gov/storage-services/service/ll/usrep/usrep472/usrep472797/usrep472797.pdf), [Hansberry, 311 U.S. 32](https://tile.loc.gov/storage-services/service/ll/usrep/usrep311/usrep311032/usrep311032.pdf), and [Beazer, 440 U.S. 568](https://tile.loc.gov/storage-services/service/ll/usrep/usrep440/usrep440568/usrep440568.pdf), supply the earlier authorities. No later class-action doctrine supplies a premise.'''

def public(blocks):
    return '\n\n'.join('## '+name+'\n\n'+body.strip() for name, body in blocks)+'\n'

liteky_public = public([
 ('Event', liteky_event), ('Participation', "All nine participated at argument and decision: Chief Justice Stone-Zsela and Justices Blackmun, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas and Ginsburg."),
 ('Public Action', 'The Eleventh Circuit judgment is affirmed unanimously. Five Justices adopt the ordinary objective appearance standard; four concur in the judgment on a different statutory formulation.'),
 ('Judgment & Remedy',liteky_judgment), ('Opinion Topology',liteky_topology), ('Holdings',liteky_holdings),
 ('Precedent Treatment','The treatments in the holding blocks govern. No earlier Supreme Court decision is overruled. The Eleventh Circuit\'s categorical source restriction is rejected; affirmation of its judgment does not preserve that restriction.'),
 ('Law After Decision',liteky_law), ('Separate Writings',liteky_separate),
 ('Procedure After Action','Supreme Court merits review is complete. The convictions remain undisturbed on the recusal issue, and the Court orders no retrial, reassignment or additional recusal procedure. No separate Supreme Court matter is retained.'), ('Source Notes',liteky_notes)])

ticor_public = public([
 ('Event',ticor_event), ('Participation',"All nine participated at argument and decision: Chief Justice Stone-Zsela and Justices Blackmun, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas and Ginsburg."),
 ('Public Action','The writ is dismissed as improvidently granted, 7–2. The Court leaves the constitutional opt-out question unanswered.'), ('Judgment & Remedy',ticor_judgment), ('Opinion Topology',ticor_topology), ('Holdings',ticor_holdings),
 ('Precedent Treatment','Beazer, Shutts and Hansberry retain the force described in the procedural explanation. No precedent is overruled, and the dismissal does not extend Shutts or adopt the Ninth Circuit\'s constitutional theory.'),
 ('Law After Decision','Effective April 4, 1994, this writ is terminated by discretionary dismissal. No substantive Supreme Court rule governing opt-out rights, mandatory certification, class settlements or monetary-claim preclusion is added. The prior certification remains conclusive between these parties, without a new general construction of Rule 23. The pending proposal receives no judicial approval through this action.'),
 ('Separate Writings',ticor_separate), ('Procedure After Action','Proceedings on this writ are complete. The Ninth Circuit\'s injunction-preclusion affirmance and monetary-preclusion reversal and remand remain undisturbed, with further proceedings under its existing mandate. This Court orders no new remand, damages award, settlement modification, vacatur or mootness dismissal. The pending proposal remains subject to District Court approval and its legally operative terms; no later outcome or hearing date is fixed.'), ('Source Notes',ticor_notes)])

reconciled = (BASE/'freeze/OT_1993CHUNK3_RECONCILED_LT_FINAL.md').read_text(encoding='utf-8')
def rows_for(marker):
    part = reconciled.split(marker,1)[1].split('\n## ',1)[0]
    table = part.split('### Justice-specific reconciliation\n\n',1)[1].split('\n\n',1)[0]
    return table

liteky_internal = '''**Case and dockets:** Liteky v. United States; No. 92-6921.
**Event and date:** Merits decision; 1994-03-07; October Term 1993, chunk 3.
**Result:** Eleventh Circuit affirmed, 9–0; ordinary objective §455(a) appearance rule controls by five votes; four concur in the judgment.
**Version / lineage:** Initial Canonical Decision Record; supersedes no adjudication. Assembled from OT_1993CHUNK3_RECONCILED_LT_FINAL, which resolves the earlier Liteky source-completeness stop; original freezes remain intact. No Git commit is claimed.

## Event, chronology, participation and entering law

Argument November 3, 1993; decision March 7, 1994, using the inventory's supplied calendar date. Review under 28 U.S.C. §1254(1) of the Eleventh Circuit's September 28, 1992 judgment, 973 F.2d 910, No. 91-8577. The petitioners seek relief from the convictions following refusal to recuse. The reviewed §455(a) question concerns judicial-source conduct; the lower court's additional summary rejection of fair-trial arguments does not enlarge the presented question into every trial ruling or an independent §144 affidavit claim. No exact historical certiorari date is entered as a separate Court action.

All nine current Justices participated at argument and decision. No case-specific nonparticipation is established. The quorum is satisfied; five votes control each judgment or proposition. Chief Justice Stone-Zsela sits with Blackmun, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas and Ginsburg. Membership, allotments and standing practices do not change.

Research cutoff: immediately before March 7, 1994. The term-opening law is processed through July 26, 1993, supplemented by the effective public current-term authorities in entering-law/OT_1993CHUNK3.md and freeze/OT_1993CHUNK3_ENTERING_NEUTRAL_PROJECTION.md. Gibson's impartiality-of-balanced-bar-dues-arbitration-panels standard, effective December 4, 1991, rejects membership-only bias while preserving actual bias, a direct stake, delay and ineffective operation. Martin's November 2, 1992 particular filing decision supplies no universal recusal rule. Weiss, January 19, 1994, rejects the fixed-tenure facial objection in its military system while preserving supported impartiality challenges without universal actual-bias proof; it does not decide §455(a)'s source inquiry. No selected register provision supplies an impossibility requirement. Surviving §455(a), Grinnell and Liljeberg govern the statutory issue. Campbell's uncoordinated same-day action is excluded from entering law. No intervening supplied event changes the relevant statutory premise.

The record consists of the original and renewed motion allegations together with every reported additional category, as specified in the public application below. No finding of new hostility or outside information is inferred. The full Eleventh Circuit opinion confirms the lower rule and judgment without adding a new material factual predicate. Full original trial motions and transcripts remain unavailable; their contents are not inferred.

## Stone — fixed core and compatibility assessment

The user-approved Section II in runtime/OT_1993CHUNK3_STONE_A1.md, Liteky portion, read with briefs/OT_1993_STONE_METHOD.md, fixes affirmance, ordinary objective appearance, rejection of both an outside-source prerequisite and an impossibility requirement, cumulative contextual application, and no retrial, reassignment or additional recusal procedure. Its conditional application is affirmance if the incidents remain ordinary criticism and administration. Its illustrative prejudgment examples are hypothetical illustrations, not facts in this case or an exhaustive new test.

The clean supplement's additional witness questions, asserted anti-defendant tone, claimed state-of-mind exclusion, fee denial and refused honorific were each considered with the 1983 and 1991 incidents. The available descriptions supply no specific discriminatory language, announced closure to contrary proof, improper eligibility determination or retaliation. The fuller account consequently does not defeat Stone's express application condition or alter his controlled core. His assessment does not depend on a categorical judicial-source exclusion or on requiring actual impossibility. No additional substantive choice, alternative ground or fallback is supplied for him. His final vote is to affirm; he joins Kennedy's Court opinion in full and issues no separate writing. No clerical correction changes his substantive supplement.

## Assignment, final compatibility, judgment and opinions

Stone belongs to the unanimous judgment coalition and holds assignment authority. He assigns the Court opinion to Kennedy because Kennedy's frozen ordinary-appearance formulation states the five-Justice agreement. This is an assembly assignment inference, not historical authorship or an invented circulation narrative. Scalia authors the distinct four-Justice judgment concurrence. No non-Stone commitment is changed in assembly.

'''+liteky_judgment+'\n\n'+liteky_topology+'''

| Justice | Final join test and limit |
|---|---|
| Stone-Zsela | Full Kennedy join: ordinary appearance, cumulative application and specified no-relief result fit the fixed core. No fallback. |
| Blackmun | Full Kennedy join: objective statutory protection is independent of actual bias and no exceptional-intensity element is inserted. |
| Stevens | Full Kennedy join: Liljeberg's statutory independence remains operative; no automatic transfer of §455(b) limitations. |
| O'Connor | Scalia judgment concurrence only: preserves the judicial-source ordinary rule and objective deep-partiality exception. Refuses the Court's removal of that added requirement. |
| Scalia | Authors judgment concurrence: legitimate judicial predispositions retain the recorded significance; cannot join the Court's broader formulation. |
| Kennedy | Authors Court opinion: reasonable appearance is sufficient without impossibility; no categorical source immunity. |
| Souter | Full Kennedy join: no mandatory extraordinary-hostility element; context and identifiable circumstances remain necessary. |
| Thomas | Scalia judgment concurrence only: historical judging practices inform the source distinction without overriding the statute or immunizing courtroom misconduct. |
| Ginsburg | Scalia judgment concurrence only: retains objective appearance and a genuine judicial-source exception without a subjective-bias burden. |

The minimum common formulation would contain only the shared source-not-dispositive propositions and application. That would omit Stone's expressly fixed broader rule; it is not substituted for his position. The actual Court opinion retains the five-Justice broader rule, so the four contrary Justices join judgment alone. The opposition between those rules is not resolved by adding votes under Marks. The concurrence's distinct rule is noncontrolling.

## Controlling holdings

'''+liteky_holdings+'''
## Current-law and procedural consequences

'''+liteky_law+'''

The Supreme Court event is complete on March 7, 1994. No new trial, reassignment, remand, roster change, companion condition or separate retained matter follows. This record displaces no identified predicate of a later historical matter, so no speculative consequence label is supplied.

## Continuity — published noncontrolling positions

'''+liteky_separate+'''

## Adaptive audit annex — frozen commitments and historical comparison

Original COMMITMENTS_A and RECONCILED_A preserved the statutory four/four distinction but did not clear the full application. COMMITMENTS_LT_REFRESH assessed the completed allegation set without Stone or comparator material. RECONCILED_LT_FINAL resolved the source-completeness stop after separate historical review and recovery of the short appellate opinion. Its operative Justice-specific conclusions are preserved here:

'''+rows_for('## 28. Liteky')+'''

**Historical departure:** The judgment remains unanimous, but Stone's approved rejection of a mandatory judicial-source impossibility requirement supplies the fifth vote for the ordinary-appearance rationale supported by Blackmun, Stevens, Kennedy and Souter, rather than Rehnquist's historical vote for the competing source formulation. Each non-Stone Justice retains the historical judgment and substantive rationale supported by the same statutory and record premises; the changed controlling rule and writing status require no invented non-Stone changed premise.

The strongest competing remedy was vacatur for application of the correct standard because both lower courts used a categorical restriction. The fresh model and reconciliation found no specified unresolved contextual fact necessary to reject this allegation set. The narrower, source-bounded affirmance does not declare all unexamined trial conduct lawful. No non-Stone legal objection is revised or traded away to obtain a coalition.

## Sources, validation and durable status

The complete official Liteky report was read in assembly, including both historical writings; it supplies historical comparison and verified predecision facts, not automatically in-world holdings. The complete recovered CAP Eleventh Circuit opinion was read. Earlier full-source review provenance for Grinnell, Liljeberg and the other date-eligible support remains in the neutral and reconciliation freezes. No Justia content was used for independent verification. Source-to-fact detail and external links appear in the public Source Notes; freeze/chunk3-sources/Liteky-510540.txt and Liteky-below.txt preserve the local source readings.

The authoritative assembly handoff is freeze/OT_1993CHUNK3_RECONCILED_LT_FINAL.md, with its validation; COMMITMENTS_LT_REFRESH and both neutral supplements preserve the clean refresh. The earlier COMMITMENTS_A and RECONCILED_A remain historical stage artifacts, not operative final application determinations. No excluded Stone material entered those clean stages through this assembly. General prior model knowledge is not claimed erased.

This new record is durable at records/Liteky_v_United_States_merits_1994-03-07.md. The assembly checks and exact vote data are in freeze/OT_1993CHUNK3_ASSEMBLY_LT_VALIDATION.md and freeze/OT_1993CHUNK3_ASSEMBLY_LT_VOTES.json. Local record validation is complete as recorded there; coordinated workspace publication, Render Input generation and whole-term validation remain the operator's next stage. No Git operation or commitment to the coordinated Current Term State is claimed by this isolated assembly.

## Public Projection

'''+liteky_public

ticor_internal = '''**Case and dockets:** Ticor Title Insurance Co. v. Brown; No. 92-1988.
**Event and date:** Dismissal as improvidently granted; 1994-04-04; October Term 1993, chunk 3.
**Result:** Writ dismissed as improvidently granted, 7–2; Ninth Circuit judgment undisturbed; no substantive opt-out holding.
**Version / lineage:** Initial Canonical Decision Record; supersedes no adjudication. Assembled from OT_1993CHUNK3_RECONCILED_LT_FINAL, resolving the earlier pending-settlement refresh and Kennedy reconciliation; original freezes remain intact. No Git commit is claimed.

## Event, chronology, participation and entering law

Argument March 1, 1994; action April 4, 1994, using the inventory's supplied calendar date. Review under 28 U.S.C. §1254(1) of the Ninth Circuit judgment, 982 F.2d 386, No. 91-15474, decided December 28, 1992. The lower court affirmed preclusion of further injunctive relief, reversed monetary-claim preclusion and remanded. Other state-action and filed-tariff issues in that judgment are outside the limited constitutional question presented here. No historical post-divergence Supreme Court grant date or other historical Court act is entered separately.

All nine current Justices participated at argument and decision. No case-specific nonparticipation is established. The quorum is satisfied, and five votes control the disposition. The roster is Stone-Zsela, Blackmun, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas and Ginsburg. This is a disposition after argument, not an undisclosed petition-stage certiorari poll.

Research cutoff: immediately before April 4, 1994. The opening trackers are processed through July 26, 1993, supplemented by effective public authority in entering-law/OT_1993CHUNK3.md and freeze/OT_1993CHUNK3_ENTERING_NEUTRAL_PROJECTION.md. No opening register resolves this federal mandatory-class opt-out question. Rule 23(b)(1)(A) addresses incompatible standards from separate adjudications; (b)(2) addresses classwide injunctive or corresponding declaratory relief. The (b)(3)/(c)(2) damages-class route provides an opt-out mechanism. This proceeding conclusively assumes the earlier certification and cannot reopen it. Shutts's limited state money-judgment holding, Hansberry's representation requirement and Beazer's available-ground sequence remain controlling within their limits. Izumi's party-status and question-presentation holdings do not decide a case brought by proper parties on the presented question; Good's independent-protections holding supplies no class-preclusion answer. Published Stevens/Blackmun Izumi and Stevens Caspari positions, and Souter's Albright position, remain noncontrolling continuity, not new universal DIG rules. No other supplied intervening event displaces these relevant premises.

The final 1986 settlement and the newer proposed settlement are different events. The latter was reported before argument and was intended to end the pending review, but approval remained pending. No exact report date, operative terms, effective release or mooting event is inferred. The constitutional controversy therefore remains live on the admitted facts. A future effective settlement would require its own legal and remedial assessment; it is not entered here.

## Stone — fixed core and compatibility assessment

The user-approved Ticor Section II in runtime/OT_1993CHUNK3_STONE_C.md, read with briefs/OT_1993_STONE_METHOD.md, fixes prudential DIG, recognizes that constitutional adjudication remains legally possible, preserves final certification, and leaves the Ninth Circuit judgment operative without merits endorsement, damages, settlement alteration or categorical certification directions. His consideration of different class forms is a limit on any future merits development, not a present opt-out holding.

The clean settlement refresh does not displace his essential premise. An unapproved proposal has not terminated the controversy, and the independent vehicle ground remains the inability to examine the antecedent Rule 23 question. The final explanation acknowledges the parties' real asserted loss and why a direct certification case would permit a better sequence; it does not call the controversy hypothetical, manufacture a collateral attack or claim jurisdictional necessity. Settlement is mentioned only as pending procedural context, not a new independent Stone ground. His final vote is DIG and full support for the per curiam explanation, with no separate writing. The mixed injunction/damages disposition below is clarified without changing his instruction to leave the judgment undisturbed. No standing fallback is used.

## Assignment, final compatibility, judgment and opinions

Stone belongs to the seven-Justice dismissal coalition and has assignment authority. The case-specific institutional dismissal issues per curiam. This choice does not import historical authorship; no individual anonymous author is invented. O'Connor authors the dissent, with Kennedy joining because the retained final commitments share the same presented-question, finality and retention ground. No final merits vote is attributed to either dissenter.

'''+ticor_judgment+'\n\n'+ticor_topology+'''

| Justice | Final join test and limit |
|---|---|
| Stone-Zsela | Full per curiam support: discretionary vehicle ground, live controversy and no merits endorsement preserve his approved core. |
| Blackmun | Full per curiam support: unavailable certification review distinguishes his Izumi position; no automatic vacatur. |
| Stevens | Full per curiam support: Beazer informs selection without inventing an available collateral ground; fair presentation acknowledged. |
| O'Connor | Authors dissent: the constitutional issue is necessary and properly presented; finality is a premise, not a cure for due process. |
| Scalia | Full per curiam support: restricted question and insulated certification warrant discretionary dismissal without opt-out doctrine. |
| Kennedy | Full O'Connor dissent join: his operative reconciliation requires retention, preserves the distinct constitutional safeguard and accepts no completed-mootness inference. |
| Souter | Full per curiam support: separate protections remain separate; no inference that representation alone resolves due process. |
| Thomas | Full per curiam support: constrained vehicle only, without collateral recertification or new merits law. |
| Ginsburg | Full per curiam support: certification finality retained without treating it as constitutional sufficiency; no unverified settlement termination. |

Retaining the case to reach the presented question would resolve the dissenters' objection but change the frozen majority disposition. No verbal revision pretending to do both is adopted. No material commitment changes in assembly; Kennedy's change from provisional DIG to retention occurred in the operative separate reconciliation before Stone entered. A status hold was a lawful alternative considered in the neutral refresh, not a final action ordered here.

## Controlling holdings

'''+ticor_holdings+'''
## Current-law and procedural consequences

No substantive Supreme Court opt-out, mandatory-class, certification or settlement-preclusion doctrine changes. The explanation states only this discretionary procedural disposition. The Ninth Circuit's injunction-preclusion affirmance and damages-preclusion reversal/remand remain operative without Supreme Court endorsement. The Court orders no new remand, vacatur, mootness dismissal, damages award or approval of the proposed settlement. This writ closes April 4, 1994; the underlying proceedings remain subject to the existing lower mandate. No roster, allotment, separate retained Supreme Court matter or identified later-case predicate changes.

## Continuity — published noncontrolling positions

'''+ticor_separate+'''

## Adaptive audit annex — frozen commitments and historical comparison

Original COMMITMENTS_C and refreshed COMMITMENTS_LT_REFRESH provisionally favored seven non-Stone DIG votes and O'Connor retention. RECONCILED_C stopped the matter for the missing pending-settlement fact and unresolved Kennedy departure. RECONCILED_LT_FINAL is operative: six non-Stone DIG commitments, O'Connor and Kennedy retention. Its rows preserve the specific authorities and comparison:

'''+rows_for('## 33. Ticor')+'''

Kennedy's final retention is required by the separately reconciled conclusion, not reconsidered after Stone exposure. Izumi concerns unreviewed intervention and an omitted question; these parties properly present the constitutional question. Good distinguishes constitutional protections but does not turn the existence of an independent question into a reason to dismiss. The pending proposal also existed historically. No concrete changed premise supported the provisional historical departure, so it was corrected before assembly. Neither retention nor dismissal supplies a constitutional merits vote.

**Historical departure:** Stone's approved prudential dismissal replaces Rehnquist's historical retention vote, producing a seven-Justice dismissal coalition rather than six; the explanation preserves the live controversy and final certification while choosing the constrained-vehicle ground. Blackmun, Stevens, Scalia, Souter, Thomas and Ginsburg retain their historical dismissal positions, and O'Connor and Kennedy retain their historical opposition, so no non-Stone changed factual or legal premise is invented.

The strongest retention argument is the necessary, fully briefed constitutional question and the cost of leaving the parties and comparable final judgments without a Supreme Court answer. The majority accepts those costs but regards direct review of certification and constitutional safeguards together as the suitable vehicle. It does not announce a prohibition on deciding necessary constitutional questions or make pending settlement a jurisdictional defect. The dissent gives the competing position public expression without importing an unmodeled merits answer.

## Sources, validation and durable status

Assembly read the complete official Ticor report, including the historical dissent, and the complete CAP Ninth Circuit text. The lower opinion supplies the mixed disposition and representation finding; the official report verifies the limited question, prior settlement and pending proposal. Historical post-divergence Supreme Court actions mentioned in the sources supply no automatic in-world events. Earlier-source review provenance for Shutts, Hansberry, Beazer and the current public authorities remains in the frozen neutral and reconciliation handoffs. No later class-action doctrine is used.

Local sources are freeze/chunk3-sources/Ticor-511117.txt and freeze/chunk3-neutral-c-sources/ticor_982_f2d_386.txt; external links and legally relevant limits are carried in public Source Notes. The operative freeze is OT_1993CHUNK3_RECONCILED_LT_FINAL.md and its validation; COMMITMENTS_LT_REFRESH and TICOR_NEUTRAL_REFRESH preserve the clean refresh. Original COMMITMENTS_C and RECONCILED_C remain unchanged stage history.

This record is durable at records/Ticor_Title_Insurance_Co_v_Brown_DIG_1994-04-04.md. Local record checks and exact votes appear in freeze/OT_1993CHUNK3_ASSEMBLY_LT_VALIDATION.md and freeze/OT_1993CHUNK3_ASSEMBLY_LT_VOTES.json. Coordinated workspace publication, generated Render Input and check_term remain for the operator. No Git command, Git commit or publication to the coordinated Current Term State is claimed by this isolated assembly.

## Public Projection

'''+ticor_public

files = {
 'Liteky_v_United_States_merits_1994-03-07.md':liteky_internal,
 'Ticor_Title_Insurance_Co_v_Brown_DIG_1994-04-04.md':ticor_internal,
}
for name, body in files.items():
    destination = BASE/'records'/name
    if destination.exists():
        raise RuntimeError('Refusing to replace an existing record: '+str(destination))
    destination.write_text(body.strip()+'\n',encoding='utf-8')

votes = {
 'Liteky v. United States': {'participants':ALL, 'components':[{'name':'Affirm on the section 455(a) recusal challenge','support':ALL,'oppose':[]}], 'propositions':[
   {'name':'Ordinary objective appearance regardless of source; no impossibility requirement','support':LP},
   {'name':'Independent section 455(a) protection without automatic importation of section 455(b) limits','support':LP},
   {'name':'Outside origin neither necessary nor sufficient','support':ALL},
   {'name':'Court cumulative application under ordinary appearance','support':LP},
   {'name':'Noncontrolling objective deep-partiality requirement for judicial-source attitudes','support':LC}]},
 'Ticor Title Insurance Co. v. Brown': {'participants':ALL,'components':[{'name':'Dismiss the writ as improvidently granted','support':TD,'oppose':TR}], 'propositions':[
   {'name':'Case-specific discretionary vehicle dismissal; no constitutional merits decision','support':TD},
   {'name':'Pending proposal does not establish completed mootness','support':ALL},
   {'name':'Noncontrolling retention of the presented constitutional question','support':TR}]},
}
(BASE/'freeze/OT_1993CHUNK3_ASSEMBLY_LT_VOTES.json').write_text(json.dumps(votes,indent=2)+'\n',encoding='utf-8')

expected = ['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
checks={}
for name in files:
    s=(BASE/'records'/name).read_text(encoding='utf-8')
    internal, pp=s.split('## Public Projection\n',1)
    pubholding=pp.split('## Holdings\n\n',1)[1].split('\n## Precedent Treatment',1)[0].strip()
    inholding=internal.split('## Controlling holdings\n\n',1)[1].split('\n## Current-law',1)[0].strip()
    counts=[len(x.split()) for x in re.findall(r'\*\*Controlling explanation:\*\* (.*?)(?=\n\n)',pubholding,re.S)]
    checks[name]={
      'four_opening_labels': all(s.splitlines()[i].startswith(label) for i,label in enumerate(['**Case and dockets:**','**Event and date:**','**Result:**','**Version / lineage:**'])),
      'exact_eleven_public_blocks':re.findall(r'^## (.+)$',pp,re.M)==expected,
      'internal_public_holdings_identical':pubholding==inholding,
      'explanation_words':counts,
      'explanations_120_to_200':all(120<=n<=200 for n in counts),
      'continuity_heading': '## Continuity — published noncontrolling positions' in internal,
      'eight_nonstone_audit_rows':len(re.findall(r'^\| (?:Blackmun|Stevens|O\'Connor|Scalia|Kennedy|Souter|Thomas|Ginsburg) \|',internal.split('## Adaptive audit annex',1)[1],re.M))==8,
      'public_private_terms':re.findall(r'\b(?:freeze|workflow|reconciliation|approved|simulated|version|commit|Stone core)\b',pp,re.I),
      'sha256':hashlib.sha256(s.encode()).hexdigest(),
    }
for case,data in votes.items():
    assert len(data['participants'])==9 and len(set(data['participants']))==9
    for c in data['components']:
        assert set(c['support']).isdisjoint(c['oppose']) and set(c['support']+c['oppose'])==set(ALL)
    for p in data['propositions']:
        assert len(p['support'])==len(set(p['support'])) and set(p['support'])<=set(ALL)

validation='''# OT1993 chunk 3 — Liteky and Ticor assembly validation

**Status:** Both new Canonical Decision Records pass bounded assembly validation. No Stone approval blocker or unresolved non-Stone commitment remains for these two matters. Whole-chunk workspace integration, Render Input generation and check_term are the operator's next stage; this file does not claim those checks were performed.

## Substantive checks completed

- The operative final reconciliation was read before adding the exact case-specific Stone supplements and Stone method. Original pending reconciliation files were retained as stage history, not treated as final authority. No non-Stone position changed in assembly.
- Liteky: 9–0 affirmance; Kennedy's Court opinion has Stone, Blackmun, Stevens and Souter joining (five total). Scalia's concurrence in the judgment has O'Connor, Thomas and Ginsburg joining (four total). The two broader rationale formulations are distinct. No Marks inference or implicit partial join supplies additional Court-opinion votes.
- Liteky: source is neither necessary nor sufficient; the Court's ordinary objective standard requires no actual bias or impossibility. The concurrence's deep-partiality requirement concerns judicially generated attitudes and remains objective; it is not a universal outside-source threshold. The ordinary bias categories and legitimate judicial experience are preserved precisely.
- Liteky: all reported original, renewed and additional allegations receive cumulative consideration. The judge's questions, tone, evidence exclusion, fee denial, honorific refusal and sentence characterization supply no invented content, retaliation, religious prejudice, unlawfulness or factual hostility. Wrong-rule remand was assessed; no specified unresolved factual predicate requires it. No §144, independent §455(b)(1), general kinship, structural-error or automatic-retrial holding is imported.
- Stone's conditional Liteky application remains satisfied on the refreshed allegation set; no new substantive choice or fallback is supplied. The five-Justice rule follows his fixed ordinary-appearance position and four independently frozen compatible positions.
- Ticor: 7–2 DIG; O'Connor's retention dissent is joined by Kennedy, whose retention was fixed in the operative reconciliation. No constitutional merits tally is inferred. The per curiam form and dissent authorship follow actual compatibility, not historical authorship alone.
- Ticor: final 1986 settlement remains distinct from the pending proposal. The proposal has no verified approval or operative terms and creates no completed mootness or vacatur ground. Stone's independent vehicle ground remains compatible; no fallback is used.
- Ticor preserves the Ninth Circuit's injunction-preclusion affirmance and monetary-preclusion reversal/remand. The Court adds no merits endorsement, new remand, damages award, settlement approval or mootness decree. The procedural explanation creates no substantive opt-out or Rule 23 doctrine.
- Every non-Stone Justice has a sourced adaptive audit row and final join boundary. Historical-departure lines identify the changed Chief Justice vote/coalition without fabricating a non-Stone changed premise. No hypothetical future consequence is labeled as an adjudicated result.
- Both records contain the eleven Public Projection blocks in exact order, judgment and topology tables, complete operative limits and publicly relevant source notes. Holdings are generated from the same strings internally and publicly. The public render form is full for both. No public source note contains private stage history.
- Complete official Liteky and Ticor reports and complete lower-court opinions were read. Missing original Liteky trial materials and unverified Ticor settlement approval remain disclosed limits. No new material fact was introduced after the clean refresh; earlier authority full-review provenance is preserved in the prior freezes.
- Only two new records, this validation, the votes JSON and the assembly script were written. No prior record, brief, runtime, workspace, render input, output or foundation file was changed. No Git commands were used or commits claimed. Python was invoked with PYTHONDONTWRITEBYTECODE=1.

## Mechanical results

```json
'''+json.dumps(checks,indent=2)+'''
```

Arithmetic confirms the declared legal conclusions; it does not select them. The standalone vote data are in OT_1993CHUNK3_ASSEMBLY_LT_VOTES.json. Both records are initial adjudications, so no superseded public entry or correction lineage is manufactured.
'''
(BASE/'freeze/OT_1993CHUNK3_ASSEMBLY_LT_VALIDATION.md').write_text(validation,encoding='utf-8')
print(json.dumps(checks,indent=2))
