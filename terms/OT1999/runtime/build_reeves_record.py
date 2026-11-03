from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
name='reeves-v-sanderson-plumbing-products-inc_merits_2000-06-12.md'
event='''Reeves v. Sanderson Plumbing Products, Inc., No. 99-536. Merits decision, June 12, 2000; argued March 21, 2000. On writ of certiorari to the Fifth Circuit, 197 F.3d 688 (1999), which displaced a jury's age-discrimination verdict on Rule 50 sufficiency grounds. The questions concern the inference from prima facie proof and disbelief of the employer's stated reason, and the proper examination of the trial record on judgment as a matter of law.

Reeves was fifty-seven and had worked for Sanderson for forty years. He supervised a regular production line in the Hinge Room. Department manager Caldwell was forty-five; Oswalt, in his thirties, supervised another line. After an audit, the company asserted inaccurate attendance and time records. Manufacturing director Chesnut, the company president's spouse, joined the recommendation to discharge Reeves and Caldwell. Oswalt had already left; the employer's assertion that it would also have discharged him is not an actual discharge.

Reeves disputed the recordkeeping accusations through testimony and documents and offered age-directed comments, differential treatment and evidence of Chesnut's dominant influence. The company disputes that evidence's accuracy, timing, meaning and connection to discharge and relies on other participants and older managers. The jury found age discrimination and willfulness. The District Court awarded $35,000 and matching liquidated damages and later $28,490.80 in front pay. The employer made and renewed Rule 50 motions and alternatively requested a new trial. The Court reviews the sufficiency ruling, not a new calculation of these awards.'''
judgment='''**Reversed and remanded, 9–0.**

**Supporting:** Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer.

The Fifth Circuit's Rule 50 judgment for the employer is reversed. The trial evidence is legally sufficient to support the age-discrimination verdict; the verdict is to stand unless an ordinary, properly preserved and verdict-compatible independent ground warrants further relief. The remand permits consideration of remaining appellate issues, including an unresolved alternative new-trial ground if otherwise reviewable. It does not reopen the sufficiency question decided here, direct a particular new trial or make a new monetary, liquidated-damages or front-pay award.'''
topology='''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | Scalia | Stone-Zsela, Stevens, O'Connor, Kennedy, Souter, Thomas, Ginsburg and Breyer | Unanimous reversal and bounded remand | Entire permissive-inference, whole-record Rule 50, actual-sufficiency and remedy holding |'''
holdings='''**Common authority:** Justice Scalia's Opinion of the Court is joined in full by the other eight Justices identified in Opinion Topology. All nine directly support each rule, application and remedial qualification below.

### I. Prima facie proof and material falsity can support discrimination

**Holding and operative rule:** A prima facie case together with evidence permitting rejection of the employer's material explanation may support a finding of intentional discrimination without an additional category of direct or independent proof. It neither compels liability nor invariably defeats judgment as a matter of law: the strength of the initial inference, the probative force of falsity and the rest of the evidence the court must credit determine whether discrimination is a reasonable inference.

**Controlling explanation:** Hicks already rejects both automatic liability and a demand for a special further kind of evidence. Aikens recognizes that the employer's actual motivation can be proved circumstantially. Once the employer produces a nondiscriminatory account, Burdine leaves the ultimate burden of persuasion with the plaintiff; rejecting the account does not revive a compulsory presumption. But a factfinder may reasonably regard an invented account as evidence concealing discrimination, considered with the initial showing and the whole record.

Hazen Paper requires age actually to motivate the decision. Falsehood, unfairness, personal hostility or another unlawful motive is not automatically age discrimination. A conclusively established different lawful reason can defeat the proposed inference. So can weak falsity evidence together with otherwise conclusive independent evidence against discrimination. These are applications of ordinary sufficiency, not a checklist demanding more evidence in every case. Merely imagining another possible motive does not defeat an inference reasonably supported by the actual proof. Substantial prima facie and falsity evidence can therefore sustain liability without a separate evidentiary category. The Court does not define every insufficient future case, alter an unpresented mixed-motive allocation or decide disparate impact.

### II. Rule 50 preserves reasonable jury inferences while considering the whole record

**Holding and operative rule:** Rule 50 requires consideration of the whole record, drawing reasonable inferences for the verdict winner and making no credibility choices or weighing of evidence. The court disregards evidence favorable to the movant that the jury was free to disbelieve, while considering uncontradicted and unimpeached evidence the jury was required to accept; testimony from disinterested witnesses is a relevant circumstance, not an inflexible witness-label rule.

**Controlling explanation:** Anderson supplies the distinction between determining whether a reasonable jury can find for a party and deciding which evidence is more persuasive. A court cannot displace the verdict by crediting disputed employer testimony or selecting among reasonable accounts. It also cannot exclude every item simply because the employer introduced it: source alone does not determine whether the jury was free to reject the evidence.

Weisgram preserves appellate authority to direct judgment on a properly preserved Rule 50 motion when the admissible record is insufficient, including after correction of an evidentiary admission. That authority is not permission to reweigh a valid record. Evidence conclusively establishing a lawful explanation remains material, but disputed testimony and reasonable contrary inferences must receive the treatment Rule 50 requires. The Court uses the ordinary sufficiency standard rather than either complete deference to all verdicts or categorical invisibility of movant evidence.

### III. This record supports the verdict and cannot be rejected for lack of extra proof

**Holding and operative rule:** Reeves's prima facie showing, material evidence rebutting the recordkeeping explanation, and evidence connecting age-directed comments to Chesnut's role and influence permit a reasonable finding of intentional age discrimination. The employer is not entitled to judgment as a matter of law on this record, and the remand cannot restore the same sufficiency judgment through a renewed demand for additional proof.

**Controlling explanation:** Reeves's testimony and documents addressed the actual attendance practices, time-clock use and disciplinary records. The jury could find the employer's account materially unworthy of belief. The age-directed comments were accompanied by evidence of Chesnut's participation in the recommendation and influence within the company. The question is their connection to the decision in the complete record, not whether a label excludes them from consideration.

The contrary accounts about timing, other decisionmakers and older employees do not conclusively defeat that inference. Crediting those accounts as decisive would require the weighing Rule 50 forbids. Oswalt's earlier departure cannot be treated as a completed discharge of a younger comparator; the claimed hypothetical action remains the employer's assertion. Consolidated Coin keeps relative-age evidence tied to the actual inference rather than making protected-group membership dispositive. The combined evidence supports the jury's age finding under Hazen Paper, not merely a conclusion that the dismissal was unfair.

This is a determination of the actual evidence's legal sufficiency, not a rule that every pretext case succeeds. Weisgram preserves genuinely independent, properly presented new-trial and remedial issues. Any such issue must be addressed on its own basis and consistently with the sufficiency holding. The Court neither assumes that an alternative ground is preserved and meritorious nor prescribes a new trial or award. Willfulness and the existing monetary components receive no new determination merely from this reversal.

**Limits:** Section 623(a)(1) concerns covered employment action because of age; §631(a) begins the Act's age protection at forty. The Court does not decide every ADEA proof framework or impose an under-forty comparator requirement. Employer production, plaintiff persuasion, evidentiary sufficiency and remaining remedial questions remain distinct. No liability follows merely from pension status, a mistaken business judgment, personal animosity or any false explanation.'''
precedent='''- **St. Mary's Honor Center v. Hicks:** Applies its existing rejection of both compulsory liability from pretext alone and a mandatory further category of proof. No replacement persuasion allocation or revived presumption is adopted.
- **Texas Department of Community Affairs v. Burdine; McDonnell Douglas Corp. v. Green:** Preserve employer production and ultimate plaintiff persuasion under the assumed indirect framework; disbelief has evidentiary force without shifting that burden.
- **Postal Service Board of Governors v. Aikens:** Applies the focus on actual discrimination and the availability of circumstantial proof.
- **Hazen Paper Co. v. Biggins:** Applies actual age motivation as the liability question; falsehood or another improper motive is not by itself age discrimination. Its willfulness and reserved disparate-impact issues are not redecided.
- **O'Connor v. Consolidated Coin Caterers Corp.:** Preserves the evidentiary significance of relative age without an under-forty replacement condition or a categorical result from workforce ages.
- **Anderson v. Liberty Lobby, Inc.:** Applies the prohibition on weighing and credibility choices in determining whether a reasonable factfinder may rule for the protected party.
- **Weisgram v. Marley Co.; Neely v. Martin K. Eby Construction Co.:** Preserve lawful appellate Rule 50 authority and proper consideration of independently supported new-trial grounds. Neither permits reweighing this sufficient record or guarantees a new trial on remand.'''
law='''Hicks's permissive inference governs ordinary discrimination proof without a special additional-evidence requirement. Courts evaluate its strength in the whole record under Rule 50, keeping ultimate persuasion with the plaintiff and preserving truly conclusive contrary proof. The Court adds a controlling application sustaining this verdict's evidentiary basis. Remaining independent appellate grounds may be considered within ordinary preservation and remedy limits; they cannot recreate the rejected sufficiency demand.'''
procedure='''The case returns to the Fifth Circuit. Its judgment for the employer is reversed; Reeves's verdict is reinstated unless an ordinary independent, properly preserved and verdict-compatible ground warrants further relief. Any unresolved alternative new-trial ground must be considered only if otherwise reviewable. The Court orders no particular retrial, new award or front-pay calculation and leaves no license to redetermine the legal sufficiency resolved here.'''
sources='''The [Records and Briefs collection for No. 99-536](https://archive.org/details/micro_IA40385014_0340) contains the petition reproducing the opinion below, opposition, joint appendix and merits submissions. The [United States and EEOC amicus](https://www.justice.gov/osg/brief/reeves-v-sanderson-plumbing-products-inc-amicus-merits) addresses the permissible inference and whole-record treatment of movant evidence. The record distinguishes an actual departure by Oswalt from the employer's predicted discharge and distinguishes the indictment-free employment dispute's competing testimony from established findings. The reported jury verdict and existing awards establish procedural history; the Court grants no new amount.'''
# The final source sentence distinguishes evidence without introducing unrelated procedural terminology.
sources=sources.replace("the indictment-free employment dispute's competing testimony", "competing testimony")
rec=(root/'freeze/OT_1999CHUNK8_A_NONCARTER_RECONCILED.md').read_text(encoding='utf-8-sig')
annex=re.search(r'(?ms)^## Reeves.*?(?=^## Completed checks)',rec)[0].strip()
annex=re.sub(r'(?m)^(#{2,3}) ',r'\1## ',annex)
text=f'''**Case and dockets:** Reeves v. Sanderson Plumbing Products, Inc.; No. 99-536.
**Event and date:** Plenary merits decision, 2000-06-12; October Term 1999, chunk 8.
**Result:** Reversed and remanded, 9–0; the age-discrimination verdict is supported by sufficient evidence, subject only to genuinely independent preserved grounds.
**Version / lineage:** Original Canonical Decision Record; supersedes no adjudication. Uses the frozen A neutral and non-Carter reconciliation and approved October 31, 2026 Reeves supplement.

## Event and participation

{event}

All nine participate at argument and decision: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No nonparticipation is supplied. Nine satisfy quorum; five suffice for a majority. Certiorari permits review of the appellate Rule 50 judgment.

## Entering law and research cutoff

Research cutoff: immediately before June 12, 2000. Substantive entering law is effective through June 5; no same-day adjudication enters merely through processing order. The A and A_PRIOR_PUBLIC holdings and published opinions supply Hicks, Hazen Paper and Consolidated Coin; A_CURRENT_PUBLIC supplies Weisgram. The historical Hicks majority's broader formulation is not substituted for the actual narrow controlling proposition and preserved Burdine allocation. The actual trial record, not an operator credibility finding, supplies the disputed evidence. No later age-causation or mixed-motive doctrine is imported.

## Stone compatibility

The approved October 31 supplement requires reversal, ordinary Rule 50 and pretext-inference review, no automatic liability or special pretext-plus evidence category, and reinstatement subject to an ordinary verdict-compatible independent ground. The whole-opinion join preserves each term. The stated exceptions require a conclusively lawful explanation or an otherwise unreasonable discrimination inference, not an imagined alternative motive. The Court's actual-sufficiency determination prevents a second version of the same rejected demand. Preserved new-trial or remedial issues are not presumed successful, and no new award is imposed. The current core does not reassert Stone's earlier noncontrolling Hicks burden proposal; the ordinary governing allocation is retained without adding a new burden. No fallback or changed approved choice is required.

## Judgment and remedy

{judgment}

## Opinion topology

{topology}

## Opinion form and assignment

The form receipt fixed one signed integrated opinion before fresh counts. Stone joins the unanimous judgment and every proposition and assigns. No separate writing or division is needed; Ginsburg's warning against disguised pretext-plus review is preserved in the common rule rather than automatically copying her historical concurrence.

**Fresh counts:** Stone-Zsela 8; Stevens 8; O'Connor 10; Scalia 9; Kennedy 9; Souter 9; Thomas 10; Ginsburg 10; Breyer 9. Total 82. **Last counted event:** Pegram v. Herdrich, June 12, 2000, Ginsburg. The fresh recount derives authors from actual Record opinion tables, including Bradley, Carter, preexisting Harris Trust and Pegram. Ramdass is stopped and contributes no opinion count.

**Eligible full-ground authors:** All nine. Each supports the complete controlling ground, actual sufficiency and bounded verdict-preserving remedy; Stone qualifies under his approved core, not fallback. The eligible minimum is eight and ceiling nine. **Balance pool:** Stone-Zsela, Stevens, Scalia, Kennedy, Souter and Breyer. O'Connor, Thomas and Ginsburg are eligible but outside the pool at ten. **Chosen author:** Scalia, nine.

Fit governs because no unresolved objection needs an expansion accommodation. Scalia's actual Hicks controlling opinion already states both halves of the governing distinction: no automatic liability and no mandatory extra-proof category. His further Hicks writing distinguishes the spent production presumption from circumstantial persuasion without demanding pretext-plus. The present opinion must carry precisely those boundaries into Rule 50 and the actual record. Stone, eight, is the strongest alternative because his approved core expressly embraces the same inference, record treatment and bounded remedy. Scalia's directly articulated distinction gives the specific fit advantage for explaining why preserving plaintiff persuasion does not justify discarding this jury's inference; the one-count difference is within the pool. Stevens, eight, can also apply the controlling rule despite his earlier preference for a stronger consequence, and is not excluded for that published disagreement. No general ability, historical authorship or importance preference controls. Scalia delivers one lead and counts once.

## Controlling holdings

{holdings}

## Precedent treatment

{precedent}

## Current law and continuity

{law}

{procedure}

This Supreme Court event is completed. No institutional change or new Supreme Court pending matter follows; lower appellate issues remain only within the specified mandate.

## Published noncontrolling positions

No separate writing issues. Prior published Hicks preferences are not newly published alternate rules here; all nine accept the present common ground and limits.

## Adaptive audit annex

The following reconciled individual grounds and historical comparison are copied mechanically from the frozen Reeves section. The complete historical opinion and Ginsburg concurrence confirmed the frozen permissible-inference, review and caution grounds; no historical authorship is imported. All eight final joins remain within those commitments. Stevens and Souter need not withdraw their earlier stronger views to join this sufficient rule. Ginsburg's reservation is answered by the express rejection of speculative lawful motives and disguised extra-proof demands. No material post-reconciliation change or fictional circulation occurs.

{annex}

## Sources and validation

{sources}

Internal inputs: freeze/OT_1999CHUNK8_A_NEUTRAL.md (Reeves); freeze/OT_1999CHUNK8_A_NONCARTER_RECONCILED.md (Reeves); runtime/OT_1999CHUNK8_REEVES_STONE.md; the A, A_PRIOR_PUBLIC and A_CURRENT_PUBLIC excerpts; freeze/OT_1999CHUNK8_REEVES_FORM.md and REEVES_COUNTS.json. The actual Hicks and Hazen public entries and Weisgram were read; complete current historical-writing verification is recorded in reconciliation rather than falsely certified as repeated in assembly.

Self-check: nine judgment votes and nine complete opinion supporters; each qualification preserves both possible discrimination inference and genuinely insufficient cases; movant evidence is not categorically excluded; hypothetical Oswalt discharge is not a fact; plaintiff persuasion is distinct from production; the actual sufficiency holding is binding on return; existing awards are history rather than new grants; preserved alternative grounds remain conditional. All Stone terms match and no fallback is used. Each explanation remains below 350 words. Computational checks confirm exact labels and eleven public blocks, identical holdings and nonoverwrite. Workspace, render-input and term-wide checks remain operator tasks.

## Public Projection

## Event

{event}

## Participation

Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated at argument and decision.

## Public Action

The Court reverses the Fifth Circuit's judgment for the employer and remands within the verdict-preserving limits stated below.

## Judgment & Remedy

{judgment}

## Opinion Topology

{topology}

## Holdings

{holdings}

## Precedent Treatment

{precedent}

## Law After Decision

{law}

## Separate Writings

No separate writing issues.

## Procedure After Action

{procedure}

## Source Notes

{sources}
'''
draft=root/'runtime'/name.replace('.md','.draft.md');draft.write_text(text,encoding='utf-8')
public=text.split('## Public Projection\n')[1]
expected=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
assert re.findall(r'^## (.*)$',public,re.M)==expected
assert public.split('## Holdings\n')[1].split('\n## Precedent Treatment')[0].strip()==holdings
lengths=[len(x.split()) for x in re.findall(r'\*\*Controlling explanation:\*\* (.*?)(?=\n### |\n\*\*Limits:|\Z)',holdings,re.S)]
assert len(lengths)==3 and max(lengths)<=350,lengths
assert not re.search(r'simulat|workflow|October 31, 2026|GitHub|OneDrive',public,re.I)
dest=root/'records'/name;assert not dest.exists();dest.write_text(text,encoding='utf-8')
receipt={'case':'Reeves v. Sanderson Plumbing Products, Inc.','record':name,'blocks':'pass','holdings_identity':'pass','explanation_words':lengths,'judgment_support':9,'full_opinion_support':9,'Stone':'full express-core join; no fallback','no_overwrite':'pass','not_performed':['workspace integration','render input','term checks','Git commitment']}
(root/'freeze/OT_1999CHUNK8_REEVES_ASSEMBLY_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt,indent=2))
