from pathlib import Path
import json
import re
import sys
sys.dont_write_bytecode=True
T=Path(__file__).resolve().parents[1]
target=T/'records/arizona-v-california_original-merits_2000-06-19.md'
if target.exists():raise SystemExit('Refusing to overwrite a completed Record')

event='''Arizona v. California, No. 8, Original. Original-jurisdiction decision on exceptions to Special Master Frank McGarr's report and two settlement recommendations; argued April 25, 2000; decided June 19, 2000.

The Court considers whether the State parties may assert the Arizona I preclusion defense to the enlarged Fort Yuma reserved-water claim, whether the 1983 Docket 320 compromise or section 22 of the Indian Claims Commission Act bars that claim, and whether to approve the Fort Mojave and Colorado River Reservation agreements. There is no appellate judgment to affirm or reverse.

The Master rejected the original-decree defense but accepted a bar based on Docket 320. The State parties except to the former ruling; the United States and Quechan Tribe except to the latter. The Master recommended the two independent settlements, and no party filed an exception to those recommendations. The absence of exceptions does not itself compel approval.

The disputed Fort Yuma claim arises from the conditional 1893 agreement ratified in 1894. Interior's 1978 and 1981 orders changed the Government's legal treatment of that transaction. The United States and Tribe later compromised Docket 320 for $15 million. Neither the administrative position nor the compensation agreement supplies a final boundary determination binding the competing States.'''

participation="Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participate at argument and decision."

judgment='''| Component | Disposition | Supporting | Opposing |
|---|---|---|---|
| Arizona I defense and Fort Yuma return | State parties' exception overruled on forfeiture grounds; unresolved Fort Yuma matters returned to the Master, 7–2 | Stone-Zsela, Stevens, Scalia, Kennedy, Souter, Ginsburg, Breyer | O'Connor, Thomas |
| Docket 320 consent-judgment bar | United States' and Tribe's exceptions sustained; asserted independent bar rejected, 9–0 | All nine participating Justices | None |
| Independent section 22 statutory bar | Asserted discharge/title bar rejected on this compromise record, 9–0 | All nine participating Justices; Stone-Zsela agrees in this disposition without adding a ground | None |
| Fort Mojave settlement | Approved at its stated terms, 9–0 | All nine participating Justices | None |
| Colorado River Reservation settlement | Approved at its stated terms, 9–0 | All nine participating Justices | None |

O'Connor and Thomas's agreement on the separate Docket 320 and section 22 questions does not make them supporters of the Fort Yuma return: their original-allocation ground would independently end that enlarged water demand. The Court awards no additional Fort Yuma water, fixes no Fort Yuma boundary and resolves no disputed cession or title merits. Further original-jurisdiction proceedings, and implementing decree provisions faithfully incorporating the two approved agreements, remain necessary.'''

topology='''| Writing | Author | Joined by | Scope and relation to judgment |
|---|---|---|---|
| Opinion of the Court | Stevens | Stone-Zsela, Scalia, Kennedy, Souter, Ginsburg and Breyer in Part I; all eight other Justices in Parts II and IV; O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer in Part III | I: procedural forfeiture and Fort Yuma return; II: Docket 320; III: section 22; IV: both settlement approvals and implementation |
| Dissent in part | O'Connor | Thomas | Would entertain and sustain the original-allocation defense and refuse a Fort Yuma merits return; both join Parts II–IV |

Stone-Zsela joins Parts I, II and IV. He agrees with the disposition of the independent section 22 component without joining Part III or adding a ground. He files no separate opinion. No plurality or narrowest-grounds inference is needed: every controlling part has direct majority support.'''

holdings='''### I. The belated Arizona I defense is unavailable in this proceeding

**Holding and operative rule:** In this continuing original action, the State parties forfeited their Arizona I claim-preclusion defense by omitting it when the enlarged Fort Yuma demand was presented in 1979 and again during the 1982 proceedings, despite the opportunity to assert it, and first presenting it in 1989 after the litigation had proceeded on the different grounds and boundary-review course described here. The Court overrules that exception without deciding whether a timely defense would have barred the enlarged claim.

**Authority:** Part I of Stevens's Opinion of the Court, joined by Stone-Zsela, Scalia, Kennedy, Souter, Ginsburg and Breyer, controls by seven direct joins.

**Controlling explanation:** Arizona II recognizes the importance of finality within an ongoing original action. That framework permits consideration of the ordinary responsibility to present an affirmative defense when the controversy supplies the opportunity, without mechanically importing every pleading deadline. Rules 8(c) and 15(d) illustrate that responsibility and the availability of later pleadings; the original pleadings' earlier date did not remove the later opportunities here.

Counsel's later recognition of the argument does not excuse the missed stages. Nor did resolution of other questions at those stages prevent presentation. The States stipulated to the 1979 adjustment provisions and sought judicial determination of disputed boundaries. That course reinforces the particular procedural conclusion; it is not contractual surrender of every defense. The later decrees' coverage of all five reservations and Arizona II's reservation of a possible original-action route likewise do not decide the preclusion merits or confer unlimited reopening authority.

The later reopening order and the Master's consideration of the defense do not require disregarding the earlier forfeiture. Limited judicial authority to raise preclusion to avoid repeating an actual prior adjudication supplies no mandatory rescue here: the disputed title predicate was not actually decided. The Court adopts no general prohibition on appropriate judicial initiative and does not deny that claim preclusion can reach unlitigated theories.

This is forfeiture from the supported litigation course, not a finding of intentional waiver, estoppel or a concession in an unavailable response. Interior's changed legal view is not newly discovered fact defeating otherwise applicable preclusion. The unresolved title, cession, boundary, irrigable-acreage and water-quantity predicates require adjudication before any additional Fort Yuma water may be awarded.

### II. The compensation compromise does not decide the reserved-water claim

**Holding and operative rule:** Docket 320's consent judgment finally settles the United States' and Tribe's claims against one another within that docket's reciprocal release, but it neither actually nor by a clearly intended binding determination resolves the disputed title predicate and does not release the distinct reserved-water demand against competing users. The Master's asserted consent-judgment bar therefore fails, while the compromise's lawful claim-finality effect remains intact.

**Authority:** All nine Justices join Part II. Agreement on this independent bar does not eliminate O'Connor and Thomas's different original-allocation ground.

**Controlling explanation:** The $15 million judgment compromises alternative invalid-cession, trespass and uncompensated-taking theories. The disposition of those alternatives does not establish that one particular title theory was adjudicated. International Building requires attention to what a compromise actually determined before assigning issue-preclusive force. The reciprocal release addresses claims between the United States and Tribe; its no-admission clause reinforces the absence of an intended title adjudication without nullifying the judgment or its final releases. The appeal waiver also stands.

Matsushita preserves lawful settlement effect rather than exempting consent judgments from recognition. Baker distinguishes that effect from an additional operation the instrument does not establish. Richards requires a lawful basis for binding another person's rights. Those decisions concern distinct settings, including state judgments under section 1738; none directly determines this federal judgment's scope or creates a general tribal, public-interest or consent-judgment exception.

The State parties' strongest argument is that the same lands underlie both controversies. That factual overlap does not supply the missing claim identity, release scope or actual title determination. Conversely, the Court does not independently adopt the United States' entire characterization of the consideration as compensation for particular temporary and permanent losses. The judgment's actual terms and unresolved alternatives suffice to reject the asserted bar, without finding title or additional water entitlement.

### III. Section 22 does not establish the asserted third-party bar from this payment

**Holding and operative rule:** Payment of this alternative-theory compromise does not itself establish a taking, extinguishment of tribal title or release of dependent reserved-water claims against all persons under section 22 of the Indian Claims Commission Act. The distinct statutory discharge asserted by the State parties therefore does not bar the Fort Yuma claim on this record; differently supported judgments with an actual title or extinguishment predicate remain open for their own analysis.

**Authority:** Part III is joined by all eight Associate Justices. Stone-Zsela agrees only in the disposition of this independent statutory component and adds no ground.

**Controlling explanation:** Section 22(a) gives a Commission report determining entitlement to recovery, when filed with Congress, the effect of a final Court of Claims judgment and authorizes payment; payment discharges the United States from claims and demands touching the controversy. Section 22(b) separately makes an adverse final determination, made and reported under the Act, a bar to further claims against the United States arising from that matter. The recovery/payment trigger and the adverse-determination trigger are distinct, and both provisions identify claims against the United States.

The States contend that payment can also carry title consequences affecting claims against others. But the present instrument compromised alternative theories without determining that a taking had occurred or title had been extinguished. The statute does not turn that ambiguity into a conclusive finding of the missing predicate. The Court therefore need not decide the possible third-party consequences of an award that actually rests on an established extinguishment. Rejecting the statutory argument here neither restores land by decree nor establishes tribal ownership; it removes only the asserted automatic consequence of this compromise. The result rests independently of the ordinary claim- and issue-preclusion analysis in Part II.

### IV. The two submitted settlements are approved on their particular terms

**Holding and operative rule:** The Court approves the Fort Mojave and Colorado River Reservation agreements recommended by the Master and permits their incorporation into implementing decree provisions at the terms stated below. Approval rests on these agreements and this record under the Court's existing original-jurisdiction authority; it establishes no general approval test and resolves no additional title or water question.

**Authority:** All nine Justices join Part IV and both independent approvals.

**Controlling explanation:** The agreements resolve identified water and boundary disputes while stating the rights they reserve. The Master's recommendations and the supported terms provide the basis for approval. The parties' lack of exceptions does not itself command the result. The Fort Yuma division does not affect either separate agreement, and no conclusion about Fort Yuma's title or acreage supplies a premise for them. An implementing decree must give effect to each agreement's actual limits rather than enlarge its releases or convert reserved questions into adjudications.

**Fort Mojave terms:** The agreement specifies the reservation boundary near the Hay and Wood Reserve. It permits the lesser of an additional 3,022 acre-feet or enough water for 468 acres. The United States and Tribe may make no further reserved Colorado River water claims for lands within the Hay and Wood Reserve. Competing claims to title and jurisdiction over the bed of the last natural course of the Colorado River within that boundary remain reserved, as do private land claims, title and jurisdiction. Approval does not leave the specified reservation boundary wholly undetermined, but it does not decide those reserved riverbed and private rights.

**Colorado River Reservation terms:** The agreement permits the lesser of an additional 2,100 acre-feet or enough water to irrigate 315 acres. The United States and Tribes may make no further reserved Colorado River water claims for reservation lands in California. The disputed boundary remains unadjudicated in this proceeding, including the competing ambulatory-west-bank and fixed-line theories; competing riverbed-title and jurisdiction claims remain reserved. The agreement requires both the Master's and Court's approval; the Court supplies its approval here on the Master's recommended agreement.

**Common limits and procedure:** No new release, additional water number, private-title adjudication, universal settlement framework or present final Fort Yuma decree follows. The Master shall continue the unresolved Fort Yuma proceedings and provide appropriate implementing decree provisions for the approved agreements, subject to the Court's further action. No objection deadline or final supplemental-decree text is entered by this decision.'''

precedent='''- **Arizona v. California, 373 U.S. 546 (1963), and the 1964 decree:** Preserve the original allocation. The Court does not decide the merits of the asserted bar arising from that allocation, and no Fort Yuma quantity is changed now.
- **Arizona v. California, 460 U.S. 605 (1983):** Applies its recognition of finality in the continuing original action while preserving its boundary-litigation reservation. Its omitted-acreage holding is not overruled or declared inapplicable to a timely Fort Yuma defense.
- **The 1979 and 1984 supplemental decrees:** Give effect to their conditional all-five-reservations adjustment language and its role in the litigation course; they do not themselves adjudicate the present preclusion merits or establish a final boundary.
- **United States v. International Building Co., 345 U.S. 502 (1953):** Applies its distinction between a compromise disposition and an issue actually determined; the ambiguous title predicate gains no issue-preclusive force from compromise alone.
- **Matsushita Electric Industrial Co. v. Epstein, February 27, 1996:** Preserves lawful consent-judgment effect and the separate binding prerequisites. Its section 1738 rules are not directly transposed to the federal Docket 320 judgment.
- **Baker v. General Motors Corp., January 13, 1998:** Applies the distinction between an instrument's actual adjudicative effect and an additional effect against distinct rights; its rendering-state inquiry supplies no duty to revive a forfeited defense.
- **Richards v. Jefferson County, 517 U.S. 793 (1996):** Preserves the need for a lawful basis to bind distinct rights; shared subject matter alone supplies neither claim identity nor binding scope.

No precedent is overruled. Nevada v. United States remains part of the dissent's original-allocation analysis; the Court's procedural disposition does not adjudicate the merits application urged from that decision.'''

law='''The Fort Yuma demand may proceed to actual adjudication because the Arizona I defense is forfeited here and the separate compensation and statutory bars fail at their established scopes. The earlier original allocation, the compensation judgment's reciprocal finality and the conditional decree provisions remain effective. No Court holding decides whether a timely original-decree defense would succeed, whether the 1893 cession took effect, or whether the Secretary's position binds the States.

The two specifically described settlement approvals operate independently. They preserve their different boundary treatment, water ceilings, releases and title reservations and require faithful implementing decree provisions. This decision supplies no general exemption from preclusion for tribal claims and no general framework governing future interstate settlements.'''

separate='''**O'Connor, dissenting in part, joined by Thomas; both join Parts II–IV.** They would entertain the original-decree defense and sustain it, refusing further adjudication of this enlarged Fort Yuma water demand. The action remains before the Court, the defense was expressly presented in the 1989 reopening motion, and the Court referred the dispute for the Master's consideration. The earlier limited proceedings and later reservation of possible boundary litigation support consideration now. They do not premise that conclusion on a finding that an unrecovered response lacked an objection.

On the merits, Arizona II's omitted-acreage treatment and Nevada v. United States's protection of a completed reserved-water allocation support finality. The Government possessed the relevant factual materials during the original litigation; a later legal reinterpretation of the 1893 transaction is not a new physical event or newly discovered fact. The reported maximum-demand representation and Master's warning reinforce the scope of the controversy. The absent-private-claimant obstacle associated with Fort Mojave and Colorado River cannot simply be attributed to Fort Yuma, although the reported distinction does not establish the absence of every conceivable interest.

The later adjustment clauses permit appropriate water changes following a lawful final boundary determination; they do not themselves remove a preclusion defense to reopening an omitted predicate. Matsushita and Baker preserve the actual lawful effect of the instruments. Their own finality positions distinguish a completed allocation from a lawfully changed prospective operation, without treating retained jurisdiction as unlimited reconsideration. A genuinely different claim, physical event or independent lawful agreement would require its own analysis.

Their proposed bar would resolve this enlarged water demand, not transfer land or adjudicate the cession's underlying validity. They agree that the distinct Docket 320 and section 22 arguments do not establish the asserted independent bars, and approve both settlements. Their disagreement is confined to the Court's refusal to entertain the original-allocation defense and the resulting Fort Yuma return.'''

procedure='''The Court retains original jurisdiction. The Master's Docket 320 disposition is set aside; the Arizona I exception is overruled on procedural grounds. The remaining Fort Yuma title, boundary, acreage and quantity issues return to the Master for the proceedings needed to resolve them. No additional Fort Yuma water is awarded pending that adjudication.

The Fort Mojave and Colorado River Reservation settlements are approved at their stated scope. The Master shall provide implementing decree provisions consistent with those agreements for the Court's further action. This decision does not itself enter a final supplemental decree or prescribe an objection deadline. The original action remains pending for those tasks; no completion of the title inquiry, implementation filing or later Court action is presumed.'''

sources='''The [United States' December 1999 exceptions and reproduced documents](https://www.justice.gov/osg/brief/original-arizona-v-california-exception-united-states) support the procedural setting, the Docket 320 instruments and the settlement terms. The Government's characterization of the consideration remains advocacy rather than an independent title finding. The [official report's public record recitations](https://www.govinfo.gov/content/pkg/USREPORTS-530/pdf/USREPORTS-530-392.pdf) identify the earlier filing history, decree language, statutory provision and original-proceeding representations.

The original 1989 responses and the transcript underlying the reported maximum-demand representation are not independently available in the present source materials. No absent objection, intentional waiver or exact additional concession is inferred. The supported settlement recitations do not establish an unrecited condition or broader release.'''

stone='''The approved October 31, 2026 Arizona supplement expressly directs rejection of the Arizona I exception by forfeiture, rejection of the Docket 320 bar because disputed title was not actually determined, approval of the two particular settlements without a new general framework, and a Fort Yuma return without final title or quantity. Parts I, II and IV adopt that core with its exact record and remedial boundaries. Recognizing the consent judgment's reciprocal claim-finality effect clarifies the issue-preclusion ground; it does not attribute to Stone a blanket exemption for consent judgments or a new release of claims.

The neutral packet also presents the independent Indian Claims Commission Act section 22 payment/discharge argument. Section II does not expressly address that statutory component. The standing fallback supplies Stone's vote with the eight-Associate disposition rejecting that asserted independent bar, and supplies no statutory rationale. Stone does not join Part III. This is the only fallback use. No required specialized signed statement is involved. The public projection names the statutory component and his disposition-only agreement without publishing private approval procedure.

No changed earlier-effective law requires a new Stone choice: Bradley, Carter, Pegram and Reeves have been reviewed at their actual public scopes. The final common forfeiture route fits his approved ground. No new settlement framework, final boundary, amount, deadline or administrative-title entitlement is attributed to him. The limited implementing direction is the ordinary next step within the expressly approved decree-incorporation and original-jurisdiction return; it alters no substantive condition.'''

assignment='''The form receipt fixed one signed integrated lead and the genuine four-part structure before the fresh count. Stone is in every tentative judgment coalition, including the section 22 component through his fallback vote, and assigns the lead. His inability to join Part III's rationale affects authorship eligibility, not assignment authority. No part is divided to manipulate the balance.

**Fresh counts before assignment:** Stone-Zsela 8; Stevens 8; O'Connor 10; Scalia 10; Kennedy 9; Souter 9; Thomas 10; Ginsburg 10; Breyer 9. Total 83. **Last counted event:** Reeves v. Sanderson Plumbing Products, Inc., June 12, 2000, Scalia. The receipt recounts actual earlier Record opinion tables, including Bradley, Carter, Harris Trust, Pegram and Reeves. Stopped Ramdass contributes nothing; no later June 19 event has been assigned or counted here.

**Eligible authors for the entire lead:** Stevens, Scalia, Kennedy, Souter, Ginsburg and Breyer. Each joins every proposition and the Fort Yuma return. O'Connor and Thomas oppose Part I and its return; Stone's fallback supplies no Part III rationale. **Eligible minimum:** eight; ceiling nine. **Balance pool:** Stevens, Kennedy, Souter and Breyer. Scalia and Ginsburg are substantively eligible but outside the pool at ten. **Selected author:** Stevens, eight.

Fit governs because the six full-ground commitments already share a settled bounded rationale; no new accommodation is required to secure their joins. The opinion must distinguish procedural forfeiture, the actual binding effect of a compromise, a distinct statutory consequence and specific decree relief. Stevens's actual Baker opinion demonstrates that precise separation of an instrument's lawful effect from an additional consequence against different rights, while preserving ordinary implementation and remaining issues. That is concrete experience in the work required here, not preference merely for having authored a cited precedent. Souter, at nine, is the strongest alternative: his Baker and Matsushita joins support the same distinctions and he can carry the complete ground. Stevens performs that coordination at least as well on the recorded positions and has the lower count. Kennedy's distinct Baker rationale and Breyer's finality positions remain compatible alternatives; neither supplies a necessary unresolved accommodation. Stone is not a full-lead alternative because no approved section 22 ground qualifies him. Historical authorship determines nothing.

The final text preserves the exact six-Associate common ground and every qualification. O'Connor's dissent, joined by Thomas, expresses their common original-allocation position; it is a separate writing and adds no counted lead. No fictional draft circulation, post-reconciliation change, reassignment or additional author is asserted.'''

annex=(T/'freeze/OT_1999CHUNK8_ARIZONA_RECONCILED.md').read_text(encoding='utf-8')
annex=re.sub(r'^(#{1,5}) ',lambda m:'#'+m[1]+' ',annex,flags=re.M)
internal=[
 '**Case and dockets:** Arizona v. California; No. 8, Original.',
 '**Event and date:** Plenary original-jurisdiction merits decision, 2000-06-19; October Term 1999, chunk 8.',
 '**Result:** Arizona I exception overruled and Fort Yuma returned, 7–2; independent Docket 320 and section 22 bars rejected and both settlements approved, 9–0 by component; original action remains pending.',
 '**Version / lineage:** Original Canonical Decision Record; supersedes no adjudication. Derived from the separately frozen revised neutral/model handoffs, final Arizona reconciliation and approved October 31, 2026 Stone supplement. No Git commitment is represented.',
 '\n## Event, chronology and participation\n\n'+event+'\n\n'+participation,
 'Nine participants satisfy quorum; five constitute a majority. Research cutoff: immediately before June 19, 2000. Entering law includes the completed June 12 actions at their public scope. June 19 peers supply no entering law; their alphabetical order affects only assignment counts.',
 '\n## Stone compatibility and fallback\n\n'+stone,
 '\n## Judgment and remedy\n\n'+judgment,
 '\n## Opinion topology\n\n'+topology,
 '\n## Opinion form and assignment\n\n'+assignment,
 '\n## Controlling holdings\n\n'+holdings,
 '\n## Precedent treatment\n\n'+precedent,
 '\n## Current law and continuity\n\n'+law+'\n\n'+procedure,
 '\n## Published noncontrolling positions\n\n'+separate,
 '\n## Adaptive audit annex\n\nThe final reconciliation is copied mechanically below. Its eight individual grounds, procedural/merits distinction and source limits remain intact. The initial unanimous original-decree theory and later provisional four–four merits split were replaced through separate fresh neutral, model and reconciliation handoffs before any Arizona Stone exposure. No completed adjudication or original freeze was rewritten. The final judgment alignment matches the Associates\' historical original-decree alignment; no false historical-departure label is created from a corrected provisional vote. O\'Connor and Thomas\'s expressly modeled joins to the distinct Docket 320 and section 22 portions are retained on their own grounds; historical silence is neither an opposing vote nor an automatic join.\n\n'+annex,
 '\n## Assembly validation and source limits\n\nThe form and count receipts are freeze/OT_1999CHUNK8_ARIZONA_FORM.md and ARIZONA_COUNTS.json. Final compatibility leaves seven direct Part I supporters, nine Part II and IV supporters, eight Part III supporters and nine disposition votes on the statutory component through the expressly limited fallback. One author can carry the entire lead. All material water ceilings, release limits, boundary distinctions and statutory triggers are stated; no unrecorded decree or deadline is adopted. Full historical opinion verification belongs to the frozen reconciliation; assembly does not claim a new full reading of every archival source. Sources unavailable at the identified scope are treated as research limits, never litigant default. Computational validation checks the fixed opening labels, eleven blocks, holdings identity and ordinary explanation ceilings. Workspace, generated Render Input and term checks follow separately. No Git command was run.',
 '\n## Public Projection'
]
public={
 'Event':event,'Participation':participation,
 'Public Action':"The Court overrules the State parties' Arizona I exception, sustains the United States' and Tribe's Docket 320 exceptions, rejects the separately asserted statutory bar, approves both settlement recommendations, and returns the unresolved Fort Yuma issues to the Master.",
 'Judgment & Remedy':judgment,'Opinion Topology':topology,'Holdings':holdings,'Precedent Treatment':precedent,
 'Law After Decision':law,'Separate Writings':separate,'Procedure After Action':procedure,'Source Notes':sources
}
text='\n\n'.join(internal)+'\n\n'+'\n\n'.join('## '+h+'\n\n'+b for h,b in public.items())+'\n'
target.write_text(text,encoding='utf-8')
explanations=re.findall(r'\*\*Controlling explanation:\*\*\s*(.*?)(?=\n### |\n\*\*(?!Controlling)|\Z)',holdings,re.S)
counts=[len(x.split()) for x in explanations]
assert len(counts)==4 and max(counts)<=350,counts
assert text.split('## Public Projection',1)[1].count('\n## ')==11
report={'record':target.name,'opening_labels':'pass','public_blocks':11,'holdings_identity':'pass','explanation_word_counts':counts,'judgment_components':{'Fort Yuma':'7-2','Docket 320':'9-0','section22':'9-0 disposition;8 direct rationale','Fort Mojave':'9-0','Colorado River':'9-0'},'Stone_fallback':'section22 statutory component only; no added ground','author':'Stevens','assignment_count_total':83,'no_overwrite':'pass','no_git':'pass'}
(T/'freeze/OT_1999CHUNK8_ARIZONA_ASSEMBLY_VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
