"""Write reviewed group-A assembly drafts; no authority is created by this helper."""
from pathlib import Path
import json
import re

T = Path(__file__).resolve().parents[1]
OUT = T / 'runtime/assembly'
OUT.mkdir(exist_ok=True)
ALL = ['Stone-Zsela', 'Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']
ASSOC = ALL[1:]
recon = (T / 'freeze/OT_1995CHUNK1_A_RECONCILED.md').read_text(encoding='utf-8')
def section(title, next_title):
    # The final clean audit may organize its retained rows differently. Preserve
    # the entire clean handoff in the source map; the case-specific table below
    # remains the assembly's express compatibility record.
    return ''

def write(d):
    h = d['holdings'].strip()
    roster = 'Chief Justice Stone-Zsela and Justices Stevens, O’Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, and Breyer.'
    private = f'''**Case and dockets:** {d['case']}; {d['docket']}.
**Event and date:** {d['event']}; {d['date']}.
**Result:** {d['result']}
**Version / lineage:** Initial adjudication; no earlier Decision Record is superseded. Durable stage files preserved; operator Git verification and commitment pending under the express no-Git instruction.

## Event, channel, participation, and entering law

{d['posture']}

{roster} All nine participate at submission and decision; no nonparticipation is established. No oral-argument date is supplied or invented. Quorum: nine, exceeding the statutory six. A merits judgment requires five votes. {d.get('threshold','The inventory expressly assigns this merits review; no separate petition poll or grant date is invented.')}

{d['law_entering']}

## Stone: fixed core and final compatibility

{d['stone']}

The standing fallback is not used. No roadmap or locked-directory material is an adjudicative input. The approved core is compatible at the exact joins below; disposition agreement supplies no additional rationale join.

## Judgment, final joins, and assignment

{d['judgment']}

{d['topology']}

{d['assignment']}

## Controlling holdings

{h}

## Precedent treatment and resulting law

{d['precedents']}

{d['after']}

## Published continuity positions and procedure

{d['separate']}

{d['procedure']}

## Adaptive audit annex

{d['audit']}

The [validated neutral packet](../freeze/OT_1995CHUNK1_A_NEUTRAL_VALIDATED.md), [independent merits commitments](../freeze/OT_1995CHUNK1_A_COMMITMENTS.md), and [final clean reconciliation](../freeze/OT_1995CHUNK1_A_RECONCILED.md) preserve each Associate's original alternatives, strongest counterargument, authorities, barriers, and comparator test. The final table above records compatibility with this opinion, not fictional draft exchanges. There is no material post-reconciliation change to a non-Stone commitment. The [control record](../freeze/OT_1995CHUNK1_CONTROL.md) discloses the cross-context fallback and the superseded cert-exposed reconciliation proposal; only the subsequent Stone-clean audit is the final A reconciliation. No pristine-context or Git-commit claim is made.

{d.get('cert','')}

## Sources, cutoff, and validation

**Research cutoff:** {d['date']}; later events supply no adjudicative premise. The modern retrieval process supplies evidence of date-eligible materials, not later law. The source-stage read receipts and [factual digest](../sources/PREFLIGHT_A_FACTS.md) distinguish full texts, bounded excerpts, party assertions, and unavailable records. [Source log](../sources/PREFLIGHT_A_SOURCE_LOG.md); [entering-law copy](../entering-law/OT_1995CHUNK1_A.md); [Collins supplement](../entering-law/OT_1995CHUNK1_A_SUPPLEMENT.md). Source and legal limits are stated in the holdings and public notes. No claim of complete trial-record review exceeds those receipts.

{d['sources']}

Assembly review separates judgment counts from opinion joins, legal review from new factual findings, and controlling rules from separate positions. Companion metadata records component arithmetic. Canonical preservation, actual intervening-law refresh, Public Projection identity and deterministic results are reported in the chunk validation artifact; this Record makes no claim that operator Git verification has occurred.

## Public Projection

## Event

{d['public_event']}

## Participation

{roster} All nine participate.

## Public Action

{d['action']}

## Judgment & Remedy

{d['judgment']}

## Opinion Topology

{d['topology']}

## Holdings

{h}

## Precedent Treatment

{d['precedents']}

## Law After Decision

{d['after']}

## Separate Writings

{d['separate']}

## Procedure After Action

{d['procedure']}

## Source Notes

{d['sources']}
'''
    (OUT / d['record']).write_text(private, encoding='utf-8')
    meta = {k:d[k] for k in ['record','case','date','judgments','writings','law_summary','published_positions','next_stage']}
    meta.update(disposition=d['result'], participants=ALL, blockers=[])
    (OUT / (Path(d['record']).stem + '.json')).write_text(json.dumps(meta, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')

wood_majority = ['Stone-Zsela', "O'Connor", 'Scalia', 'Kennedy', 'Thomas']
wood_other = ['Stevens', 'Souter', 'Ginsburg', 'Breyer']
write(dict(
record='Wood_v_Bartholomew_summary_merits_1995-10-10.md', case='Wood v. Bartholomew', docket='No. 94-1419', date='1995-10-10', event='Certiorari grant and reasoned summary merits decision',
result='Certiorari granted; Ninth Circuit reversed and remanded, 5–4 on summary disposition. The four opposing Justices leave the ultimate merits open.',
posture='The petition challenges the Ninth Circuit’s September 6, 1994 reversal, 34 F.3d 870, of the District Court’s denial of habeas relief. The appellate remedy permitted retrial on premeditation within a reasonable time or reduction to simple first-degree murder; the January 13, 1995 District Court order implemented that mandate. Review concerns whether the nondisclosed polygraph information establishes material suppression under Brady and the intervening Kyles decision. Independent ineffective-assistance and false-testimony theories were not reached below and are not decided here. This is a petition-stage summary action, not an argued plenary decision.',
threshold='The independent petition poll satisfies the Rule of Four; its individual votes are internal and are not published. The summary merits action separately has five votes.',
law_entering='The opening law applies without an earlier current-term event. The exact Standards heading is **Collective Brady materiality and investigating-team responsibility**. Kyles (April 19, 1995), Souter for Stone-Zsela, Stevens, O’Connor, Ginsburg, and Breyer, controls through **Collective suppression undermines confidence in this conviction**, **The prosecutor’s responsibility includes the investigating team**, and **A completed material Brady violation requires no second duplicative harmlessness showing**. Bagley supplies reasonable probability, understood as undermined confidence rather than probable acquittal. Schiro (January 19, 1994) and Caspari (February 23, 1994) preserve distinct presentation-sensitive nonretroactivity questions; none is adjudicated here.',
stone='Stone grants review and reverses the existing Brady relief with a remand. He accepts lawful investigative, preparation and derivative evidentiary uses even when the original information is excluded, insists on collective assessment, and finds the supplied investigative counterfactual unsupported. The source validation identifies no authenticated concrete lead requiring application of his conditional branch. He does not find an unqualified counsel concession, an admissibility safe harbor, a per-item burden, or guilt-stage use of penalty witness Bell. Those limits appear expressly in the shared opinion; the approved core is unchanged.',
judgment='**Judgment:** Reversed and remanded, **5–4 on summary disposition**. **Supporting:** Stone-Zsela, O’Connor, Scalia, Kennedy, Thomas. **Opposing summary disposition:** Stevens, Souter, Ginsburg, Breyer; they favor plenary consideration and express no final merits vote. The Ninth Circuit’s present Brady basis for conditional relief cannot stand. The lower courts must conform the implementing order to this judgment and address only independently remaining, procedurally available matters. No new trial, reduction of conviction, release, or dismissal of all habeas claims is ordered.',
topology='Justice O’Connor delivers the Court’s opinion, joined by Chief Justice Stone-Zsela and Justices Scalia, Kennedy, and Thomas. Justices Stevens, Souter, Ginsburg, and Breyer note their dissent from summary disposition; they do not join the merits opinion and file no substantive separate opinion.',
assignment='Chief assignment: Stone belongs to the five-Justice judgment coalition. Its shared ground is already settled: a supported collective lawful-use counterfactual, not categorical inadmissibility. O’Connor is assigned the opinion because her Kyles join and her reconciled record application directly connect that controlling rule to the limited summary remedy. Stone is the strongest alternative: his approved formulation performs the same separation. O’Connor offers the concrete advantage of expressing the Kyles majority principle while carrying the three Kyles dissenters’ compatible evidentiary limit. No new accommodation or changed join is invented. OT1994’s actual assignments trigger no concentration ceiling; this is the first current-term Chief assignment.',
holdings='''### Unsupported investigative possibilities do not establish material suppression

The Court holds that inadmissibility of undisclosed information does not, by itself, foreclose a Brady claim based on a lawful investigative or preparation use. But the defendant must identify a supported way in which disclosure, considered collectively with the other suppressed material and against the whole trial record, creates a reasonable probability of a different result; the assertion that counsel might have investigated differently does not establish that consequence.

**Authority:** O’Connor’s opinion, joined by Stone-Zsela, Scalia, Kennedy, and Thomas, supplies five votes for this rule and its application.

**Controlling explanation:** Brady makes material favorable suppression a constitutional injury, and Bagley asks whether it undermines confidence in the result. Kyles requires collective assessment and protects supported uses in preparing and presenting the defense; it does not require each item independently to establish materiality. Those principles extend beyond placing the withheld document itself in evidence. They also require more than a chain of hoped-for discoveries.

The undisclosed information concerns Rodney’s deceptive polygraph responses and Tracy’s technically inconclusive result, together with the examiner’s favorable impression. None establishes perjury, a confession, or a new admissible account. The asserted interviews, inconsistencies and other investigative fruits remain conjectural on the presented claim. Considering both witnesses together does not supply the missing supported evidentiary consequence. Their importance to premeditation warrants attention, but cannot itself prove that disclosure would have produced useful evidence. Bartholomew admitted the robbery and shootings but contested premeditation; the existing attack on Rodney and the gun’s single-action operation remained part of the trial evidence. No new finding about the disputed assembly or testing of the gun is made. The Court does not decide the scientific truth of the examinations or rely on counsel having conceded away every conceivable use. Nor does it add Bell’s penalty-stage testimony to the guilt record. The lower court’s speculative theory therefore does not establish entitlement to its conditional writ.

No second harmless-error test is imposed after a completed material Brady violation. Independent habeas claims and any properly available antecedent defenses remain outside this holding.

**Precedent treatment:** Brady and Bagley are applied; Kyles’s collective lawful-use and confidence-based requirements are applied without an admissibility exception or an additional prejudice burden.''',
precedents='- **Brady v. Maryland:** Applied to favorable suppressed information; nondisclosure alone does not establish materiality.\n- **United States v. Bagley:** Applied through the reasonable-probability, confidence-in-the-result standard; probable acquittal is not required.\n- **Kyles v. Whitley:** Applied to the combined lawful preparation and evidentiary uses; no per-item threshold, categorical inadmissibility bar, or second duplicative harmlessness inquiry is created.',
after='Excluded information may support a Brady claim through sufficiently supported lawful uses. This claim fails because the asserted evidentiary change remains speculative. The existing collective materiality rule and prosecution-team responsibility remain intact; independent habeas claims acquire no new disposition.',
separate='Stevens, Souter, Ginsburg, and Breyer dissent from deciding the case summarily. Their notation leaves the ultimate Brady application and final remedy for plenary consideration; it is neither a vote to affirm the conditional writ nor an opinion adopting a competing materiality rule. No substantive separate writing is filed.',
procedure='The case returns to the Ninth Circuit for proceedings consistent with reversal of the presented Brady ground. Any remaining claim must independently satisfy its procedural and substantive requirements. The Court does not direct state retrial, sentence reduction, or unconditional release.',
audit='''| Justice | Frozen final commitment and compatibility |
|---|---|
| Stevens | Opposes summary disposition; Kyles lawful-use concerns remain for plenary consideration. No merits join is inferred. |
| O’Connor | Summary reversal on supported collective materiality; joins because the opinion excludes a categorical inadmissibility rule and an unproved counsel concession. |
| Scalia | Summary reversal; his Kyles dissent required an evidenced change in the combined record. The opinion does not impose per-item materiality. |
| Kennedy | Summary reversal; his Kyles dissent join supports rejecting the unsupported causal chain, without a second habeas-prejudice burden. |
| Souter | Opposes summary disposition; his Kyles authorship supports lawful uses but supplies no present merits vote. |
| Thomas | Summary reversal; collective evidentiary support remains absent, without a new innocence prerequisite. |
| Ginsburg | Opposes summary disposition; reserves the ultimate lawful-use application. |
| Breyer | Opposes summary disposition; reserves the ultimate application and remedy. |

Historical comparison: the complete report discloses the same four Associates dissenting from summary disposition, not from the ultimate merits. The initial proposed summary vacatur was superseded only through the clean reconciliation. No material departure from the disclosed historical procedural alignment remains. The opinion’s actual Kyles ground does not import every historical factual characterization or unpublished merits preference.''',
cert='The separate [petition commitment handoff](../freeze/OT_1995CHUNK1_A_CERT_COMMITMENTS.md) records all nine grants of the limited Brady question, their institutional grounds, and Stone’s neutral default status. Stone’s subsequently exposed approved supplement independently directs a grant of that same question; it does not change the previously modeled poll. The grant admits no independent ineffective-assistance or false-testimony question. The poll remains internal.',
sources='[Ninth Circuit judgment, 34 F.3d 870](https://static.case.law/f3d/34/html/0870-01.html), and the [petition-stage record](https://archive.org/details/micro_IA40385013_0583) support the lower posture and the parties’ investigative-use dispute. The complete counsel testimony is not established by the bounded materials; no dispositive concession is found. The State’s description of Tracy’s test differs from the lower court’s technically inconclusive characterization. The rule is applied without resolving that source conflict or any new gun-testing fact.',
public_event='**Wood v. Bartholomew, No. 94-1419 — October 10, 1995.** Summary review of the Ninth Circuit’s reversal of the District Court’s habeas denial. The appellate mandate required a conditional retrial on premeditation within a reasonable time or reduction to simple first-degree murder. No oral argument. The question is whether the withheld polygraph information supports that relief under collective materiality principles.',
action='Certiorari granted on the presented Brady question; a reasoned summary opinion reverses the judgment below.',
judgments=[dict(component='Summary reversal and remand',disposition='Reverse and remand',support=wood_majority,oppose=wood_other,other=[],printed_tally='5-4')],
writings=[dict(author="O'Connor",joiners=['Stone-Zsela','Scalia','Kennedy','Thomas'],scope='All controlling holdings',controlling=True)],
law_summary='Brady reaches supported lawful investigative/preparation uses of excluded information; collective confidence-based materiality still requires a supported evidentiary consequence. The speculative polygraph investigation theory does not sustain the conditional writ; independent claims and defenses remain open.',
published_positions=['Stevens, Souter, Ginsburg, and Breyer oppose summary disposition and favor plenary consideration; ultimate merits remain open, and no substantive separate opinion is filed.'],
next_stage='Remand to conform the lower implementing order and address only independently remaining, procedurally available claims.'
))

doe_majority=['Stone-Zsela','Stevens','Souter','Ginsburg','Breyer']
doe_dissent=["O'Connor",'Scalia','Kennedy','Thomas']
write(dict(
record='Doe_v_Taylor_ISD_merits_1995-10-16.md',case='Doe v. Taylor Independent School District',docket='Fifth Circuit No. 90-8431; no separate Supreme Court docket supplied',date='1995-10-16',event='Assigned merits decision on individual supervisory immunity',
result='Affirmed and remanded: denial of Lankford’s immunity, 5–4; Caplinger’s immunity, 9–0 in judgment, on an eight-Justice notice rationale; pure factual-sufficiency review excluded unanimously.',
posture='The en banc Fifth Circuit, March 3, 1994, 15 F.3d 443, affirmed the denial of principal Eddy Lankford’s immunity, reversed the denial of superintendent Mike Caplinger’s immunity, and remanded. The admitted merits review concerns those separable legal immunity rulings on the properly assumed facts. It neither adjudicates the teacher’s or district’s liability nor awards damages. An appeal asking only whether the evidence supports the assumed facts is outside the collateral-order channel under Johnson. The Court affirms the separable legal judgment; any such factual-only portion must be dismissed, without finding that a specifically identified additional appeal exists.',
law_entering='Wood (October 10) concerns Brady materiality and does not alter this immunity dispute. The operative Standards headings are **Relevant precedent in appellate qualified-immunity review**, **Qualified-immunity legal appeals and factual sufficiency**, and **Individual-capacity liability for official conduct under §1983**. Elder (February 23, 1994) requires examination of all relevant law; Johnson (June 12, 1995) bars factual-sufficiency collateral review; Hafer (November 5, 1991) separates personal responsibility from office. Collins (February 26, 1992) distinguishes underlying wrong and attribution and reserves deliberate bodily injury. Albright (January 24, 1994) produced no controlling general substantive-due-process rationale. Farmer (June 6, 1994) supplies an actual-awareness analogy only. These later decisions do not create conduct-time notice for 1986–1987.',
stone='Stone affirms both officials’ different immunity outcomes. He supports a knowing, personal and causal supervisory wrong against Lankford on assumed facts, with conduct-date notice supplied by earlier bodily-integrity and supervisory cases, not later Farmer or May 1987 cases for a February omission. He supports Caplinger’s judgment because the latter’s own limited knowledge and responses do not establish knowing disregard on this record, not because the governing duty was unclear. That distinct merits rationale receives a separate concurrence, not an invented join in the eight Associates’ notice analysis. The January/February notice inconsistency remains unresolved; knowledge is not imputed from the principal. Stone joins the legal/factual jurisdictional boundary.',
judgment='''| Component | Disposition | Supporting | Opposing |
|---|---|---|---|
| Lankford’s legal immunity | Denial affirmed; remanded, **5–4** | Stone-Zsela, Stevens, Souter, Ginsburg, Breyer | O’Connor, Scalia, Kennedy, Thomas |
| Caplinger’s legal immunity | Immunity affirmed, **9–0 in judgment** | All nine participating Justices | None |
| Pure factual-sufficiency appeal | Outside immediate appellate jurisdiction; dismiss any such portion, **9–0** | All nine participating Justices | None |

The surviving Lankford claim returns for ordinary proceedings on actual knowledge, culpable inaction and causation. Neither liability nor damages is established. The equal-protection alternatives receive no new merits disposition; the lower court’s procedural treatment, based on no identified different responsibility or additional damages, is preserved.''',
topology='''| Writing / portion | Author and joins | Status |
|---|---|---|
| Part I: legal/factual appellate boundary | Ginsburg; Stone-Zsela, Stevens, O’Connor, Scalia, Kennedy, Souter, Thomas, Breyer join | Court, nine |
| Part II: Lankford’s personal supervisory wrong and notice | Ginsburg; Stone-Zsela, Stevens, Souter, Breyer join | Court, five |
| Part III: Caplinger’s conduct-date immunity | Ginsburg; Stevens, O’Connor, Scalia, Kennedy, Souter, Thomas, Breyer join | Court, eight; Stone-Zsela concurs in judgment |
| Concurrence in the Caplinger judgment | Stone-Zsela, alone | No culpable personal deprivation on the assumed facts; noncontrolling alternative |
| Concurrence in part and dissent in part | O’Connor; Scalia, Kennedy, Thomas join | Joins Parts I and III; would also grant Lankford immunity |''',
assignment='Chief assignment: Stone is in every judgment majority and assigns the single divided opinion to Ginsburg. Her Elder authorship provides a concrete advantage in integrating all relevant conduct-date authorities while preserving Johnson’s limits and separate official-specific rationales. Stone is the strongest alternative for the substantive knowing-acquiescence rule, but his different Caplinger ground would require the same divided structure and does not answer the Associates’ notice ground more directly. Fit, not an assumed expansion of commitments, governs. O’Connor’s separate opinion expresses the four preserved notice objections. The assignment count is now O’Connor one, Ginsburg one; the preceding-term review triggers no two-term ceiling.',
holdings='''### Legal immunity review accepts the properly assumed facts

An immediate qualified-immunity appeal may decide a separable legal question on the plaintiff’s properly supported assumed facts, but may not decide only whether the evidence is sufficient to establish those facts. A factual-sufficiency portion must be dismissed; the appellate court may not choose whose account is true or resolve disputed knowledge and causation by recasting those questions as law.

**Authority:** Ginsburg’s Part I, joined by all eight other participating Justices, controls unanimously.

**Controlling explanation:** Johnson v. Jones distinguishes an appealable immunity question from a dispute about the sufficiency of proof. Elder v. Holloway requires the appellate court to examine the relevant law, not to reconstruct a more favorable factual record for the officer. Here the officials may obtain review of the legal consequences of the properly assumed record. They may not secure findings that warnings were never given or that their inaction did not contribute to the abuse. The inconsistent January and February descriptions of Caplinger’s first notice are not resolved by this Court. No ruling that an identified item of evidence is credible, or that Doe has proved her claim, follows.

**Precedent treatment:** Johnson’s jurisdictional boundary and Elder’s legal-review rule are applied without expansion of collateral appellate jurisdiction.

### Knowing, causally effective acquiescence in a teacher’s sexual abuse is personal wrongdoing

A school supervisor violates a pupil’s bodily-integrity right when the supervisor actually knows of sexual abuse through school authority, or of a substantial risk of that abuse, deliberately and unreasonably disregards that known danger despite authority and a reasonable opportunity to take protective action, and that culpable inaction causes injury or its continuation. A reasonable response is not actionable merely because injury still occurs. Awareness may be proved circumstantially, but warning signs do not compel that finding and what an official merely should have known is insufficient. The properly assumed Lankford facts describe that personal knowing acquiescence, not negligence or liability merely for supervising the teacher; the relevant preconduct law gave fair notice of the wrong, so immunity does not bar the claim at this stage.

**Authority:** Ginsburg’s Part II, joined by Stone-Zsela, Stevens, Souter, and Breyer, controls by five votes.

**Controlling explanation:** Ingraham recognizes bodily security. The teacher's exploitation of his official authority and access supplies the pleaded governmental connection, although some acts occurred away from school. Monell forbids vicarious liability, and Rizzo requires a causal link to the supervisor's own conduct.

Ford limits responsibility to direction, participation or approval. Reimer and Vela reject liability merely for failing to adopt preventive policies while recognizing responsibility for affirmative unlawful policies causing injury. Chinchello reads Rizzo more narrowly as requiring more than awareness and inaction and describes other courts' inaction cases through communicated approval. These formulations are not interchangeable; they expose the danger of converting inadequate supervision into vicarious liability. Wanger and Bowen nevertheless recognize personal responsibility where the supervisor's own deliberately indifferent conduct or inaction causes the constitutional injury. The restricted conduct assumed here—actual awareness, deliberately unreasonable nonresponse within the principal's authority, and causal prolongation of abuse—falls within that principle. No finding that Lankford communicated approval to the teacher is made.

The dismissed earlier physical-conduct report, repeated warnings, and February valentine and suspected relationship support the assumed knowledge. The alleged failure to act meaningfully may have permitted continued injury. Those are legal-review assumptions, not findings; the earlier sexual contact, later intercourse and continued abuse remain distinct for causation. Negligent failure to discover misconduct, a state reporting breach alone, or supervisory office would not suffice.

For pre-May 1987 omissions, notice comes from earlier law. Jefferson's direct-restraint holding and Lopez's school-supervision analysis reinforce evaluation of the alleged later continuation, but their different settings and Lopez's rejection of liability on its facts remain material. Neither creates a general monitoring duty or supplies retroactive notice. Farmer's later actual-awareness formulation is only a current analogy. Doe must still prove awareness, unreasonable disregard and attributable injury.

**Precedent treatment:** Ingraham is applied to bodily integrity; Monell and Rizzo retain their personal-attribution limits. Hafer confirms individual-capacity liability for one’s own wrong. Collins’s reserved deliberate-injury setting is distinguished from its voluntary-employment omissions. Farmer is used only as a current analogy, not conduct-time notice.

### Caplinger is immune on the distinct notice question

On Caplinger’s own assumed information and responses, the conduct-time law did not clearly establish that his particular supervisory conduct violated Doe’s federal right. He therefore receives qualified immunity on the presented individual supervisory claim; the Court does not decide whether that conduct actually violated the Constitution or attribute the principal’s fuller knowledge to him.

**Authority:** Ginsburg’s Part III, joined by Stevens, O’Connor, Scalia, Kennedy, Souter, Thomas, and Breyer, controls by eight votes. Stone-Zsela concurs only in this component’s judgment.

**Controlling explanation:** Elder requires the full relevant legal landscape, while Hafer requires individualized responsibility. Caplinger arrived in July 1986 and was not told the principal’s earlier history or the February valentine. His response to later reports included inquiries, an interview of Doe in which she denied sex, and warnings to the teacher; the promised wider meeting did not occur. Those facts cannot be replaced by an assumption that he knew everything Lankford knew. Nor does the Court resolve the lower opinion’s conflicting January/February notice descriptions.

The preconduct supervisory cases did not clearly define this particular combination of limited information, investigation and alleged inadequate follow-through as constitutional wrongdoing. Jefferson and Lopez, issued in May 1987, cannot illuminate earlier omissions retroactively and do not, for later conduct, equate this superintendent’s individual circumstances with the principal’s alleged knowing acquiescence. A broad duty to protect children does not answer the required particularized notice inquiry. Conversely, the judgment does not excuse an official merely because his notice came later: sufficiently clear personal knowledge and duty would require their own analysis. The constitutional merits remain reserved.

**Precedent treatment:** Elder and Hafer are applied to the superintendent separately. No broad immunity for school officials, no mandatory merits-first sequence, and no endorsement of his response as constitutionally adequate is established.''',
precedents='''- **Ingraham v. Wright:** Supplies the established bodily-security interest; applied to abuse through school authority.
- **Monell v. Department of Social Services; Rizzo v. Goode:** Preserve the bar on vicarious liability and require a causal link to the defendant’s own wrong.
- **Hafer v. Melo:** Applied to each individual officer’s own conduct and personal immunity.
- **Elder v. Holloway:** Applied to review of all relevant law while fixing fair notice to the time of conduct.
- **Johnson v. Jones:** Applied to exclude pure evidence-sufficiency review.
- **Collins v. Harker Heights:** Its voluntary-employment omission holding does not decide knowing participation in deliberate bodily abuse; its separation of wrong and attribution remains effective.
- **Farmer v. Brennan:** Its actual-awareness and reasonable-response analysis is an analogy, not a retroactive school-duty rule.
- **Albright v. Oliver:** Its fractured rationales supply no controlling general rule displacing the pleaded bodily-integrity claim.
- **Shillingford, Woodard, Wanger, Bowen, Languirand, and Hinshaw:** Their preconduct personal-culpability and causation reasoning informs notice; their distinct facts and limitations remain intact. **Jefferson and Lopez:** Their May 1987 dates preclude retroactive notice, and their differing direct-action and supervisory settings limit their later relevance.''',
after='Knowing and causally effective supervisory acquiescence in abuse through school authority supports this bodily-integrity claim; negligent protection or supervisory status alone does not. Lankford’s immunity denial leaves proof for further proceedings. Caplinger’s judgment rests on the particular conduct-time notice ground, with the merits reserved by the Court. The jurisdictional distinction between law and factual sufficiency remains unchanged.',
separate='''**Stone-Zsela, concurring in the Caplinger judgment.** The Chief Justice joins Parts I and II but would resolve Caplinger’s component on the merits. Each official must be assessed on his own information and response. Caplinger’s later and more limited information, inquiries, interview and warnings, despite their alleged deficiencies, do not amount on the assumed facts to the knowing disregard potentially shown against Lankford. The date of notice alone is no excuse; the decisive distinction is personal culpability. The Chief Justice does not rely on the absence of close precedent, impute the principal’s knowledge, resolve the January/February conflict, or establish a general right to an adequate school investigation. This ground is not the Court’s Caplinger holding.

**O’Connor, joined by Scalia, Kennedy, and Thomas, concurring in part and dissenting in part.** These Justices join the legal/factual review boundary and Caplinger’s immunity, but would grant Lankford immunity too. Ingraham’s bodily-security principle and the teacher’s obvious wrong do not by themselves settle the separate supervisor’s constitutional obligation during 1986–1987. The contemporary cases distinguished personal action, policy, affirmative linkage and omissions, and often rejected the asserted supervisory liability. Hafer’s personal-responsibility rule and Elder’s complete review do not eliminate that specificity problem. Farmer and other later formulations cannot provide retrospective notice. The dissent assumes the pleaded facts for this legal inquiry; it neither endorses abuse nor holds that every omission is beyond §1983.''',
procedure='The case returns for proceedings on Lankford’s surviving claim, with no finding of liability or damages. Caplinger retains individual immunity within the presented claim. Any purely factual-sufficiency appellate portion is dismissed. The Court decides no district liability, separate Title IX claim, or additional equal-protection merits question.',
audit='''| Justice | Final commitment and scope of compatibility |
|---|---|
| Stevens | Denies Lankford immunity on knowing personal causal acquiescence; Collins authorship and Farmer join preserve wrong/attribution distinctions. Joins Caplinger only on conduct-date immunity and Part I. |
| O’Connor | Would grant both officials immunity; Hafer and Elder support individualized contemporaneous notice. Joins Parts I/III, dissents from II. |
| Scalia | Particular supervisory duty not clearly established; Albright/Collins and Farmer positions do not erase the teacher’s bodily wrong. Joins I/III only. |
| Kennedy | Personal attribution and uncertain omission duty support immunity; conditional Albright remedy theory is not a general bar. Joins I/III only. |
| Souter | Farmer’s circumstantial actual-awareness reasoning supports the assumed causal-acquiescence path, not constructive knowledge. Joins I/II/III, with Caplinger’s merits reserved. |
| Thomas | Distinguishes obvious teacher injury from clear separate supervisory duty. Joins I/III only; no school rule is inferred from his Farmer reservation. |
| Ginsburg | Elder supports all relevant law without a fact-identical requirement; bounded knowing acquiescence defeats Lankford immunity. Writes I/II/III and reserves Caplinger merits. |
| Breyer | Johnson requires assumed facts and rejects appellate factfinding. Joins bounded Lankford rule and Caplinger notice ground; no participation in Farmer or Albright is attributed. |

Historical comparison: the historical Lankford petition was denied without a merits opinion or disclosed individual poll. The expressly assigned merits review changes that procedural premise. There is no historical Supreme Court merits alignment to copy or depart from; lower separate writings supply opposing legal arguments, not votes for the present Court. Four Associates’ Lankford dissent and the eight-Justice Caplinger notice rationale remain exactly within the final handoff. Stone’s additional merits position does not change any Associate’s rationale.''',
sources='[En banc Fifth Circuit opinion and separate writings, 15 F.3d 443](https://static.case.law/f3d/15/html/0443-01.html) supply the assumed record, procedural judgment and competing conduct-date authorities. The lower narrative and application differ over whether Caplinger first received notice in January or February; the Court does not settle that discrepancy. No actual knowledge, causation or credibility finding is made. The equal-protection alternatives and the district’s responsibility receive no new merits determination.',
public_event='**Doe v. Taylor Independent School District — October 16, 1995.** Review of the en banc Fifth Circuit’s individual supervisory-immunity judgment, No. 90-8431, 15 F.3d 443. The questions concern each official’s personal responsibility and conduct-time notice, and the permissible scope of immediate appellate review.',
action='The Court issues a merits opinion affirming the separable legal immunity judgment and remanding within the limits of immediate appellate jurisdiction.',
judgments=[dict(component='Lankford immunity',disposition='Affirm denial and remand',support=doe_majority,oppose=doe_dissent,other=[],printed_tally='5-4'),dict(component='Caplinger immunity',disposition='Affirm immunity',support=ALL,oppose=[],other=[],printed_tally='9-0'),dict(component='Factual-sufficiency appellate boundary',disposition='Dismiss any purely factual portion',support=ALL,oppose=[],other=[],printed_tally='9-0')],
writings=[dict(author='Ginsburg',joiners=[x for x in ALL if x!='Ginsburg'],scope='Part I',controlling=True),dict(author='Ginsburg',joiners=['Stone-Zsela','Stevens','Souter','Breyer'],scope='Part II',controlling=True),dict(author='Ginsburg',joiners=[x for x in ASSOC if x!='Ginsburg'],scope='Part III',controlling=True),dict(author='Stone-Zsela',joiners=[],scope='Caplinger judgment concurrence',controlling=False),dict(author="O'Connor",joiners=['Scalia','Kennedy','Thomas'],scope='Lankford dissent; joins Parts I/III',controlling=False)],
law_summary='On properly assumed facts, actual knowing, deliberately unreasonable and causally effective supervisory acquiescence in sexual abuse through school authority defeats Lankford immunity; negligence or status alone does not. Caplinger receives immunity on the particular conduct-date notice ground, with constitutional merits reserved. Johnson excludes purely factual-sufficiency appeals.',
published_positions=['Stone-Zsela would grant Caplinger judgment because his own limited knowledge and responses do not establish knowing disregard, rather than for lack of clear law.','O’Connor, Scalia, Kennedy, and Thomas would grant Lankford immunity because the particular contemporaneous supervisory duty was insufficiently clear; they join Caplinger immunity and the appellate boundary.'],next_stage='Lankford claim returns for proof of actual knowledge, culpability and causation; Caplinger immunity remains; no liability or damages adjudicated.'
))

write(dict(
record='Hodge_v_Jones_merits_1995-10-23.md',case='Hodge v. Jones',docket='Fourth Circuit No. 93-1182; no separate Supreme Court docket supplied',date='1995-10-23',event='Assigned merits decision on immunity and prospective mootness',
result='Judgment for individual defendants affirmed, 9–0; eight Justices rest damages on qualified immunity, while Stone-Zsela concurs on the merits. Prospective expunction/declaratory relief is moot, unanimously.',
posture='The Fourth Circuit, July 19, 1994, 31 F.3d 157, reversed the District Court’s interlocutory liability judgment and directed judgment for the officials. The preserved claim concerns retention of the confidential paper investigation report recording clearance after a child-abuse inquiry. Review reaches the legal immunity issue and the continuing controversy over prospective relief; it does not add the distinct inaccurate AMF coding episode that the complaint was not amended to assert. No damages amount or attorney-fee entitlement is decided.',
law_entering='Wood changes no relevant rule. Doe’s October 16 holding concerns actual knowing, causally effective acquiescence in physical abuse through school authority and conduct-date personal immunity; it does not establish an informational-retention right or retroactive notice in 1989–1990. The exact relevant Standards headings remain **Relevant precedent in appellate qualified-immunity review** and **Qualified-immunity legal appeals and factual sufficiency**. Elder and Johnson govern legal review; Collins separates a state duty from constitutional injury; Albright supplies no Court-wide requirement of custody or financial loss. Whalen, Paul, Roth, Olim and the then-relevant Hewitt principles address different protected interests and cannot be merged into a general retention rule.',
stone='Stone affirms the damages judgment on the merits: retaining this accurate confidential cleared report, without actual public disclosure, family interference or a legal disability, does not establish the claimed deprivation. A state procedure alone is not a substantive federal entitlement. He does not join the Associates’ lack-of-clear-law ground, and his preserved merits view is separately published. He joins mootness because the applicable period expired and plaintiffs do not contend that required expunction failed. The report is distinguished from the erroneous, unpleaded AMF code, and neither universal harmlessness of confidential records nor proof of actual destruction is asserted. The corrected packet therefore does not require changing his approved core.',
judgment='**Judgment:** Affirmed, **9–0 in judgment**. **Supporting:** Stone-Zsela, Stevens, O’Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer. **Opposing:** None. The individual defendants receive judgment on the presented damages claims. Eight Justices rest that result on qualified immunity; Stone-Zsela rests it on absence of the claimed deprivation. All nine hold the presented expunction and related declaratory requests moot. No constitutional merits judgment of the Court, order authorizing future disclosure, or disposition of the unpleaded inaccurate-code claim follows.',
topology='''| Writing / portion | Author and joins | Status |
|---|---|---|
| Part I: individual damages immunity | O’Connor; Stevens, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer join | Court, eight; Stone-Zsela concurs in judgment |
| Part II: prospective mootness | O’Connor; Stone-Zsela, Stevens, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer join | Court, nine |
| Concurrence in part and in the judgment | Stone-Zsela, alone | Joins Part II; distinct merits ground for damages, noncontrolling |''',
assignment='Chief assignment: Stone joins both judgment components, so assigns the opinion to O’Connor. Her Hafer and Elder positions give a concrete advantage in expressing personal damages immunity while preserving the constitutional question and distinguishing prospective relief. Stone is the strongest alternative for separating injury, procedure and remedy, but his fixed affirmative merits ground does not supply the eight Associates’ shared notice rationale. Assigning him would require a separate majority author for that work. O’Connor can carry the complete divided opinion without a changed commitment. The actual current assignments are O’Connor two and Ginsburg one. No author exceeded half in OT1994, so the two-consecutive-term ceiling does not bar this case-specific fit assignment.',
holdings='''### The officials are immune on the preserved confidential-retention claim

The Court holds that the individual officials have qualified immunity from damages for the challenged 1989–1990 retention of the cleared, confidential investigation record because the asserted federal duties of disclosure, expunction and procedural treatment of that retained report were not clearly established then. The holding reserves whether the preserved conduct violated a constitutional or state-created substantive right; it does not authorize every confidential file, inaccurate entry or disclosure.

**Authority:** O’Connor’s Part I, joined by Stevens, Scalia, Kennedy, Souter, Thomas, Ginsburg, and Breyer, controls by eight votes. Stone-Zsela agrees only with this component’s judgment.

**Controlling explanation:** Elder requires examination of all relevant law at the proper conduct date. Whalen recognizes the significance of personal information while examining confidentiality protections; Paul distinguishes reputation alone from deprivation of a protected status; Roth and Olim distinguish a protected interest from a procedure standing by itself. Those authorities did not clearly resolve this particular claim about limited retention of a cleared child-protection report. A general interest in family autonomy or privacy does not itself supply that specific notice.

The report did not establish a finding that the parents were dangerous. The preserved record establishes no removal, interference with a particular parental decision, public publication, loss of a benefit or job, or revoked clearance. Statutory access by specified recipients was limited, not absolute secrecy. The separate erroneous AMF sexual-abuse code existed, but was not added to the complaint; the Court neither erases that error nor adjudicates a new claim based on it. The lower court’s conclusion that AMF was the statutory central registry is not an enacted command or an issue resolved here.

A possible constitutional injury is not defeated simply because it lacks confinement or monetary loss. Albright established no such general rule. But uncertainty over the underlying privacy and state-created-interest questions does not defeat these officials’ bounded conduct-date immunity. The Court therefore need not reconstruct an unresolved statutory entitlement or decide the constitutional merits.

**Precedent treatment:** Elder is applied to particularized historical notice; Whalen, Paul, Roth and Olim retain their distinct functions. Albright’s separate rationales are not converted into controlling law.

### The presented prospective requests no longer pose a live controversy

The requests for expunction and related declaratory relief are moot because the applicable five-year retention period expired in January 1994 and plaintiffs do not contend that required expunction then failed. The five-year rule applied if no further incidents were reported involving the same alleged perpetrator; this disposition neither applies the separate later 120-day rule retroactively nor finds destruction on evidence outside the record.

**Authority:** O’Connor’s Part II, joined by all eight other participating Justices, controls unanimously.

**Controlling explanation:** Prospective relief must address a continuing controversy, distinct from a surviving claim for past damages. The presented expunction request depends on ongoing retention past the applicable period. With that period expired and no contention that required expunction failed, the requested prospective order and related declaration would decide no continuing injury asserted here. The fact that damages remain disputed does not keep that separate prospective claim alive. Nor does a contingent fear of future disclosure establish a new retained record or an exception to mootness. The judgment rests on the claim as presented, not an independently authenticated destruction certificate. It decides no fee entitlement or new remedy for the unpleaded computer-code episode.

**Precedent treatment:** Ordinary live-controversy principles are applied to the particular relief sought; the damages immunity holding is not used to establish prospective mootness.''',
precedents='''- **Elder v. Holloway:** Applied to all relevant conduct-date law without a mandatory merits-first sequence.
- **Whalen v. Roe:** Its concern with personal information and confidentiality remains intact; it did not clearly establish the particular expunction duty asserted here.
- **Paul v. Davis:** Its distinction between reputation and a protected deprivation informs notice; no universal tangible-loss requirement is adopted.
- **Board of Regents v. Roth; Olim v. Wakinekona:** Preserve the distinction between a substantive protected interest and mandatory procedure alone. No disputed Maryland entitlement is conclusively construed.
- **Collins v. Harker Heights:** Its separation of constitutional injury and state duties remains intact; no general confidential-record merits rule is derived.
- **Albright v. Oliver:** Its fractured positions remain noncontrolling as a general restriction on constitutional injury.
- **Doe v. Taylor Independent School District:** Its knowing, causally effective physical-abuse rule is distinguished from this informational-retention dispute and cannot supply retroactive notice.''',
after='The decision establishes the officials’ qualified immunity on the particular preserved damages claim and mootness of the presented prospective requests. The Court leaves constitutional informational privacy, any disputed substantive statutory entitlement, inaccurate coding and broader disclosure questions unresolved. Stone-Zsela’s merits rationale changes no controlling law.',
separate='**Stone-Zsela, concurring in part and in the judgment.** The Chief Justice joins the prospective mootness holding but would reject the damages claim because the asserted constitutional deprivation is absent on this record. The State may retain an accurate, confidential account of a legitimate investigation; a report recording clearance is not a finding of parental dangerousness. No separation, public disclosure, particular family interference or legal disability is established. Roth and Olim distinguish state procedure from a substantive federal entitlement, so a claimed procedural departure alone is insufficient. This ground is limited to the preserved report and injuries. It does not approve knowingly false records, retention contrary to an enforceable substantive right, broad dissemination, or automatic family restrictions, and does not deny all constitutional protection to intimate information. The Chief Justice does not rest on lack of close precedent. His merits conclusion is not the Court’s holding.',
procedure='Judgment for the individual defendants stands within the presented damages claim. The expunction and related declaratory requests are dismissed as moot. The Court orders no new retention schedule or hearing, resolves no fee entitlement, and adds no claim concerning the inaccurate AMF classification.',
audit='''| Justice | Frozen commitment and final compatibility |
|---|---|
| Stevens | Immunity and prospective mootness; Collins separates state duty and federal injury, while his Albright position preserves possible privacy injury. Joins I/II, not Stone’s merits ground. |
| O’Connor | Immunity and mootness; Hafer/Elder support personal conduct-date notice without deciding the constitutional question. Writes I/II. |
| Scalia | Immunity and mootness; particular federal source remains uncertain under Collins/Albright, without endorsing every confidential file. Joins I/II. |
| Kennedy | Immunity and mootness; Elder/Albright support distinct notice analysis, not a universal state-remedy defense. Joins I/II. |
| Souter | Immunity and mootness; no universal palpable-consequence requirement is imposed by his Albright position. Joins I/II. |
| Thomas | Immunity and mootness; mandatory procedure alone supplies no clearly settled federal damages duty. Joins I/II. |
| Ginsburg | Immunity and mootness; Elder considers all law, but later Valmonte’s employment barrier supplies neither earlier notice nor the present facts. Joins I/II. |
| Breyer | Immunity and mootness; Johnson bars new appellate findings, including an invented destruction fact. Joins I/II. |

Historical comparison: the historical certiorari denial disclosed no merits holding, individual merits position or poll. The assigned merits event therefore has no historical Supreme Court merits lineup to import. Judge Powell’s lower immunity-only approach is an adversarial source, not a present Justice’s vote. Actual Doe law changes no frozen premise: deliberate personal participation in physical abuse does not decide this information claim or confer conduct-time notice years earlier. No material circulation revision occurs.''',
sources='[Fourth Circuit judgment and separate concurrence, 31 F.3d 157](https://static.case.law/f3d/31/html/0157-01.html) supply the record, the separate unpleaded coding episode, and the prospective posture. The five-year condition and separate later 120-day rule remain distinct. The full historical Maryland provisions are not conclusively reconstructed here; the Court resolves immunity without deciding a new statutory entitlement. Expunction is not independently certified: plaintiffs’ lack of a contrary contention supplies the stated mootness premise.',
public_event='**Hodge v. Jones — October 23, 1995.** Review of the Fourth Circuit’s judgment, No. 93-1182, 31 F.3d 157, on damages arising from confidential retention of a cleared child-protection report and on prospective expunction and declaratory relief.',
action='The Court affirms judgment for the individual officials and resolves the presented prospective claims as moot.',
judgments=[dict(component='Individual damages judgment',disposition='Affirm',support=ALL,oppose=[],other=[],printed_tally='9-0'),dict(component='Prospective expunction and related declaration',disposition='Moot',support=ALL,oppose=[],other=[],printed_tally='9-0')],
writings=[dict(author="O'Connor",joiners=[x for x in ASSOC if x!="O'Connor"],scope='Part I immunity',controlling=True),dict(author="O'Connor",joiners=[x for x in ALL if x!="O'Connor"],scope='Part II mootness',controlling=True),dict(author='Stone-Zsela',joiners=[],scope='Damages merits concurrence; joins Part II',controlling=False)],
law_summary='Officials have conduct-date qualified immunity for the preserved 1989–1990 confidential cleared-report retention claim; constitutional and disputed statutory merits remain reserved. Prospective expunction/declaration is moot after the applicable conditional five-year period expired with no contention expunction failed; no destruction finding or retroactive 120-day rule.',
published_positions=['Stone-Zsela rejects the damages claim on the merits for lack of the claimed deprivation on the accurate confidential-report record, reserving false records, enforceable substantive rights, broad disclosure and actual family restrictions; he joins mootness.'],next_stage='Individual damages judgment stands; presented prospective claims moot; no new retention rule, fee ruling, or inaccurate-code adjudication.'
))

blocker='Stone’s approved disposition treats the Ake violation as conceded, but the Commonwealth expressly withdrew that concession in its 1995 opposition. Renewed approval is required to proceed on an express assumption of an available Ake violation while remanding contested predicates and preserving Stone’s Chapman position; no such approval has arrived. A final violation determination would instead require the complete requests, assistance, preservation and prior-state-ruling record.'
(OUT/'BLOCKERS.json').write_text(json.dumps([dict(case='Tuggle v. Netherland',blocker=blocker,neutral_blocker='The Ake threshold is contested after withdrawal of the earlier concession. No terminal Court event has occurred; antecedent request, assistance, preservation and state-ruling questions remain unresolved.')],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Three group-A drafts and Tuggle blocker metadata written; no canonical record preserved.')
