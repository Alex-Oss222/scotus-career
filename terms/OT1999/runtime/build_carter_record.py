from pathlib import Path
import re
import json
root=Path(__file__).resolve().parents[1]
case='Carter v. United States'
name='carter-v-united-states_merits_2000-06-12.md'
event='''Carter v. United States, No. 99-5716. Merits decision, June 12, 2000; argued April 19, 2000. On writ of certiorari to the Third Circuit, 185 F.3d 863 (1999), affirming the District of New Jersey conviction under the completed-taking branch of the first paragraph of 18 U.S.C. §2113(a). The question is whether bank larceny under §2113(b) is a necessarily included offense under Federal Rule of Criminal Procedure 31(c).

Carter admitted taking bank money but disputed force or intimidation. He entered the bank on September 9, 1997 wearing a ski mask, crossed the teller counter and fled with approximately $16,000. His contact with a departing customer is disputed: his account describes an accidental bump, while the Government describes a push back into the bank. The indictment alleges approximately $14,000, a distinct amount, in a knowing and willful taking by force, violence and intimidation from a teller's person and presence at an FDIC-insured bank. The jury returned its verdict January 23, 1998; the robbery sentence was 215 months. Separate Pennsylvania larceny convictions and concurrent sentences are outside this review.

The trial court rejected the larceny instruction as categorically unavailable under circuit precedent. Carter's letter asserted a broader larceny theory; the attached charge described the higher grade using the obsolete $100 threshold. The applicable statute uses $1,000. The Court does not rewrite that request or resolve the disputed contact.'''
judgment='''**Affirmed, 5–4.**

**Supporting:** Stone-Zsela, O'Connor, Scalia, Kennedy and Thomas.
**Opposing:** Stevens, Souter, Ginsburg and Breyer.

The Third Circuit's judgment is affirmed as against the refusal of the requested §2113(b) instruction. Carter's robbery conviction and sentence remain undisturbed on this ground. No acquittal, substituted larceny conviction, sentence reduction or new trial is ordered. Independent issues not before the Court and the separate Pennsylvania convictions are unaffected.'''
topology='''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | O'Connor | Stone-Zsela, Scalia, Kennedy and Thomas throughout; Stevens, Souter, Ginsburg and Breyer in Part III only | Affirms the denied-instruction judgment | I: intent; II: carrying away; III: aggravated value and noninclusion of that grade; IV: application and limits |
| Dissent in part | Ginsburg | Stevens, Souter and Breyer | Would vacate the categorical noninclusion disposition and remand; joins Part III | Basic-inclusion construction, request and evidence inquiries, and reservation of the higher-grade election |'''
holdings='''**Authority:** O'Connor's Opinion of the Court is joined throughout by Stone-Zsela, Scalia, Kennedy and Thomas. These five directly support Parts I, II and IV. All nine join Part III's additional-value proposition and its limited subset conclusion. Each independent ground below has its own stated scope; a shared value holding does not resolve basic larceny by itself.

### I. Specific theft intent is an additional larceny element

**Holding and operative rule:** In the completed forcible-or-intimidating taking charged here, §2113(a)'s first paragraph requires knowing conduct satisfying its taking conditions, but does not require §2113(b)'s additional intent to steal or purloin. That additional purpose independently prevents either grade of §2113(b) from being necessarily included under Rule 31(c).

**Controlling explanation:** Schmuck compares statutory elements as legally construed, not the facts that happen to establish both crimes. Section 2113(b) expressly adds a theft purpose to its taking requirement; the charged portion of subsection (a) specifies knowing conduct involving force and violence or intimidation without that additional purpose. The separate entry paragraph expressly requires an intent to commit a qualifying felony or larceny. Its wording cannot be transplanted into the completed-taking branch.

Morissette requires attention to inherited culpability, and Staples and X-Citement Video require the fault appropriate to the enacted offense. They do not require every common-law incident of an analogous offense when the statutory description already identifies culpable conduct. This construction does not punish an innocent accidental taking or remove the knowledge requirement. The claim that removal of feloniously was stylistic and robbery traditionally aggravated larceny cannot overcome the enacted contrast. Bell confirms that this statutory scheme is not simply an unchanged common-law code. The Court construes those descriptions; different wording alone is not a mechanical element test.

### II. Carrying away independently prevents inclusion

**Holding and operative rule:** Section 2113(b) requires taking and carrying away the property, while the charged completed-taking branch of §2113(a) does not require the additional carrying away. That difference independently defeats inclusion of either larceny grade, even if their culpability requirements were assumed to coincide.

**Controlling explanation:** Congress wrote both taking and carrying away in subsection (b), but taking by the stated forcible means in the relevant part of subsection (a). The argument that takes implicitly includes the slight movement associated with common-law larceny is substantial, but it would erase the separately enacted movement requirement in comparing these descriptions. The common-law relationship does not compel identical statutory ingredients. Schmuck requires that each lesser element be necessary to the greater, rather than that the charged conduct ordinarily satisfies both. Carter's actual flight with the money cannot establish that legal necessity. The result rests on construction of the completed offense, not simply on the separate availability of an attempt prosecution.

### III. The higher grade also requires value exceeding $1,000

**Holding and operative rule:** Value exceeding $1,000 is an element of §2113(b)'s grade carrying a ten-year maximum, and is not merely a sentencing factor. Because the charged §2113(a) taking has no value threshold, that higher larceny grade is not itself a statutory subset of robbery.

**Controlling explanation:** The value language occurs in the description of prohibited conduct and is repeated in the separate higher and lower grades. Its role and sharply different maximum punishments support offense-element treatment. Almendarez-Torres, Jones and Castillo supply statute-specific aggravated-element analogues, without creating a universal constitutional rule for every maximum-increasing fact. Carter's original sentencing-factor theory fails under the enacted structure.

The approximately $14,000 allegation and approximately $16,000 trial account do not make a value threshold an element of statutory robbery. Schmuck's comparison does not become an indictment-specific comparison merely because the amount is alleged. The correct threshold is $1,000, following the 1996 amendment; the proposed $100 instruction is not silently corrected. This holding alone does not decide the lower larceny grade, whose inclusion the Court rejects on Parts I and II. The Court does not determine whether the lower paragraph demands affirmative proof that value cannot exceed $1,000.

### IV. The elements failure resolves the requested instruction

**Holding and operative rule:** Because neither larceny grade is necessarily included in the charged completed robbery under the Court's intent and movement constructions, the denied §2113(b) instruction supplies no ground to disturb the conviction. A defendant's request alone does not create a Rule 31(c) exception to those statutory differences.

**Controlling explanation:** The elements test protects charging responsibility, notice and the jury's legally available choices. Carter's admission of taking money and dispute about force cannot change it. Keeble explains why an included alternative may be necessary when a rational jury could convict of the lesser while acquitting of the greater; it does not dispense with statutory inclusion. The Court therefore need not decide the Government's independent rational-jury argument or resolve the disputed physical contact.

The proposed election of a higher grade presupposes an independently included basic theft, which Parts I and II reject. Unilateral consent to notice also does not itself answer Schmuck's reciprocity objection or the independent charging safeguards. Stirone protects the actual grand-jury charge but does not itself decide every defendant-requested grade proposal. Awareness of facts, consent to an instruction, legal sufficiency of the indictment, grand-jury waiver and admission of an offense element remain distinct. No missing value allegation or completed waiver is found. The Court reserves whether the full indictment independently charges another offense and decides no separate charging route.

**Limits common to the judgment:** The decision concerns the charged completed-taking configuration, not every extortion, attempt or entry offense. It decides neither entitlement to another offense instruction nor any independent trial error. Section 2113(a) permits a fine under title 18, imprisonment up to twenty years, or both. Section 2113(b)'s higher grade permits a fine under title 18, imprisonment up to ten years, or both; its lower paragraph specifies a fine no greater than $1,000, imprisonment up to one year, or both. These descriptions create no new sentencing determination in Carter's case.'''
precedent='''- **Schmuck v. United States, 489 U.S. 705 (1989):** Applies legally construed statutory elements and preserves the independent rational-jury inquiry; factual overlap and a unilateral instruction request do not replace inclusion.
- **Morissette v. United States, 342 U.S. 246 (1952):** Preserves appropriate culpability and common-law context without importing every common-law ingredient into the distinct statutory descriptions.
- **Staples v. United States; United States v. X-Citement Video:** Apply contextual fault analysis; neither requires the additional theft purpose for this already culpable taking. X-Citement Video's distinction between an existing factual finding and unresolved indictment consequences remains.
- **Bell v. United States, 462 U.S. 356 (1983):** Applies the recognition that bank-larceny coverage is not confined to unchanged common-law larceny; Bell does not itself decide Rule 31(c) inclusion.
- **Jerome v. United States; Prince v. United States:** Preserve their actual statutory settings without using the statute's title or general structure to erase the contrasting completed-taking elements.
- **Almendarez-Torres v. United States; Jones v. United States (March 24, 1999); Castillo v. United States (June 5, 2000):** Apply their statutory aggravated-element treatment as analogues for the higher-value grade. Their ordinary charging and jury consequences remain; no general constitutional sentencing rule or actual indictment defect is found here.
- **Keeble v. United States, 412 U.S. 205 (1973):** Preserves the function of an included, evidence-supported alternative; neither prerequisite is removed.
- **Stirone v. United States, 361 U.S. 212 (1960):** Preserves protection of the actual grand-jury charge; its prosecution-created enlargement setting does not itself settle every defendant-requested election.
- **Mosley v. United States:** The Court's procedural disposition established no bank-larceny elements rule; it supplies no merits authority for this decision.'''
separate='''**Ginsburg, dissenting in part, joined by Stevens, Souter and Breyer; all four join Part III.** The dissent construes the charged completed forcible taking to retain theft intent and movement. Robbery's inherited relation to larceny, the statutory context and the stylistic deletion of feloniously support those legally construed elements. Morissette and the contextual approaches of Staples and X-Citement Video support that reading; Bell's broader theft coverage does not require removing these ingredients from completed robbery. The dissent applies Schmuck's elements test rather than reviving a factual-relationship test.

The four agree that the higher grade adds value exceeding $1,000 and is not a statutory subset. They construe the lower paragraph as the basic theft grade, with a one-year maximum when aggravated value is not established as an offense element. The Government need not prove that the sum could not exceed $1,000: taking more money does not make basic theft innocent. The lower-value language limits unaggravated punishment; proof of a larger amount alone does not authorize the higher maximum without the aggravated offense's requirements.

On that construction basic larceny is included. Carter's letter asserted larceny as the answer to disputed force or intimidation, while the attached charge used a deficient higher-grade formulation. The categorical circuit rule bypassed whether the actual broader request sought a legally available basic instruction. The dissent would vacate that categorical determination and return for request scope, ordinary preservation, treatment of the correct threshold and the Government's independent rational-jury contention. Proof sufficient for robbery does not establish that every rational jury must reject only-theft treatment. The dissent makes no credibility finding and requires no instruction on every unrequested lesser crime.

The dissent reserves both adoption and categorical rejection of a higher-grade election. An affirmative request and the indictment's actual amount allegation are material, but do not alone settle Schmuck's reciprocity concern or all charging consequences. The limited grade-election proposal must be distinguished from factual relatedness and supported under the actual charge and any legally necessary consent or waiver. Almendarez-Torres, Jones and Castillo preserve the distinction between factual awareness and the proper aggravated charge; X-Citement Video preserves indictment questions despite an existing culpability finding. Those decisions do not forbid every valid defendant election or establish a missing allegation here. Stirone likewise does not by itself resolve this proposal. No grand-jury waiver, element admission or new charge is inferred.

The proposed return could still end in denial on a lawful request or evidentiary ground. Error and remedy follow only if an included, properly requested and evidence-supported instruction should have been given. The dissent orders neither acquittal, entry of a larceny conviction, sentence reduction nor an automatic new trial and finds neither harmfulness nor harmlessness.'''
law='''The Court adds a controlling construction of the completed-taking bank-robbery offense: §2113(b)'s specific theft purpose and carrying away each independently preclude lesser-offense inclusion. The higher-value element separately defeats felony inclusion, with all nine Justices agreeing on that limited proposition. Rule 31(c) remains an elements inquiry, followed by a distinct rational-jury inquiry only when inclusion is established. The Court leaves the lower grade's upper-value proof question, independent indictment route and other statutory configurations unresolved.'''
procedure='''The mandate affirms the Third Circuit on the denied-larceny-instruction issue. No new trial, sentencing proceeding or lesser conviction is directed. The decision leaves independent matters outside the grant and the separate Pennsylvania convictions undisturbed.'''
sources='''The [1998 United States Code, §2113](https://www.govinfo.gov/content/pkg/USCODE-1998-title18/html/USCODE-1998-title18-partI-chap103-sec2113.htm) supplies the operative statute and the 1996 threshold amendment. The [docket's Records and Briefs collection](https://archive.org/details/micro_IA40385014_0393) contains the petition, opposition, joint appendix, merits briefs and reply; JA1 supplies the January 23, 1998 verdict, JA2–3 the indictment, and JA4–9 the actual instruction request. The [United States' merits brief](https://www.justice.gov/osg/brief/carter-v-united-states-merits) supplies its independent evidentiary argument. The two accounts of customer contact remain disputed; the indictment and trial amounts are distinct. No quoted decisional language is required.'''
rec=(root/'freeze/OT_1999CHUNK8_CARTER_RECONCILED.md').read_text(encoding='utf-8-sig')
annex=rec.split('## Eight individual reconciliations',1)[1].split('## Disposition boundaries',1)[0].strip()
internal=f'''**Case and dockets:** {case}; No. 99-5716.
**Event and date:** Plenary merits decision, 2000-06-12; October Term 1999, chunk 8.
**Result:** Affirmed, 5–4; the denied bank-larceny instruction does not disturb the robbery judgment.
**Version / lineage:** Original Canonical Decision Record; supersedes no adjudication. Uses the revised Carter neutral and commitment handoffs and frozen reconciliation; the original commitment section is superseded only as documented there.

## Event and participation

{event}

All nine participate at argument and decision: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No nonparticipation basis is supplied. Nine satisfy quorum; five suffice for a majority. The lawful channel is certiorari to the final appellate criminal judgment.

## Entering law and cutoff

Research cutoff: immediately before June 12, 2000. Effective law includes Castillo, June 5; uncoordinated same-day events supply no substantive authority. The A slice, CARTER_PRIOR_PUBLIC and Castillo-only C_CURRENT_PUBLIC supply the actual law. The neutral correction withdraws the erroneous characterization of Scalia and O'Connor's Schmuck dissent: that dissent addressed the mail-fraud nexus and supplies no objection to the elements test. No later general constitutional sentencing holding is imported. The official statute's first paragraph, entry paragraph and two value grades were read distinctly; the saved neutral record distinguishes allegation, trial account and actual requested wording.

## Stone compatibility

The approved October 31, 2026 supplement directs affirmance on §2113(b)'s separate intent, taking-and-carrying-away and value requirements, while preserving independent issues. Stone's whole-opinion join follows that exact core. The value analysis is confined to the higher grade; the independent intent and movement holdings carry his stated noninclusion conclusion for either grade without attributing a nonexistent robbery value element. His reservation of whether the indictment independently alleges another offense is retained. No evidence finding, independent charging ground, acquittal or new error remedy is added. Castillo reinforces statutory element treatment without displacing his approved core. No fallback, substantive narrowing or unapproved separate ground is used.

## Judgment and remedy

{judgment}

## Opinion topology

{topology}

## Opinion form and assignment

The form receipt fixes one integrated signed plenary lead and one common dissent before fresh counts. Stone is in the judgment coalition and assigns. Full-lead eligibility is determined by support for all four parts, not the unanimous additional-value proposition alone.

**Fresh counts:** Stone-Zsela 8; Stevens 8; O'Connor 9; Scalia 9; Kennedy 9; Souter 9; Thomas 9; Ginsburg 9; Breyer 9. Total 79. **Last counted event:** Bradley v. Arkansas Department of Education, June 12, 2000, Thomas. The fresh count derives authors from actual Record tables, including Bradley; later-alphabetic Harris Trust is excluded, and its preexisting assignment is preserved.

**Eligible authors for the integrated lead:** Stone-Zsela, O'Connor, Scalia, Kennedy and Thomas. Every one supports the complete grounds, remedy and limits; Stone qualifies by his approved core. All nine support Part III alone, but division is unnecessary because five can write the whole. The eligible minimum is eight, ceiling nine. **Balance pool:** Stone-Zsela, O'Connor, Scalia, Kennedy and Thomas. **Chosen author:** O'Connor, nine.

Fit governs; no expansion accommodation or changed vote is needed. O'Connor's own Staples concurrence distinguishes the factual knowledge necessary for culpable conduct from a further specific purpose, and her X-Citement Video join applies culpability contextually. That is the central work of explaining why the completed forcible taking is not innocent but need not carry §2113(b)'s added theft purpose. She also supports carrying away and aggravated value as separate statutory grounds. Stone, eight, is the strongest alternative: his approved analysis supplies the complete three-element comparison and accurate remedy limits. O'Connor's specifically recorded knowledge-versus-purpose distinction offers the concrete drafting fit for answering the common-law objection without accidental-taker liability; the one-count difference remains inside the authorized pool. Scalia's Jones and Castillo opinions also fit the value issue, but value alone cannot resolve both grades. Thomas remains eligible despite the preceding Bradley assignment. No ability, historical-authorship or importance rule excludes anyone. O'Connor delivers the integrated lead and counts once.

Ginsburg writes the common dissent because her actual contextual-construction and X-Citement Video charge/remedy reasoning express its basic-inclusion and bounded-return ground; Stevens, Souter and Breyer join in full. This selection uses those actual positions, not historical authorship. Part III's express four additional joins simply project a proposition each frozen row affirmatively supports; they change no judgment or substantive commitment. No fictional circulation is asserted.

## Controlling holdings

{holdings}

## Precedent treatment

{precedent}

## Current law and continuity

{law}

{procedure}

No institutional or roster change follows. This Supreme Court event is completed; no new open matter or compulsory later hearing is created.

## Published noncontrolling positions

{separate}

## Adaptive audit annex

The following individual grounds and historical-departure explanations are copied mechanically from the frozen reconciliation. The four returning Associates' value agreement supplies no assent to either independent intent or movement ground. Their specific prior charging and bounded-mandate positions justify reserving the historical dissent's affirmative grade election, while preserving its basic-inclusion direction. The four affirming Associates' three grounds remain unchanged. The final joins and remedies were checked against each row; no new neutral fact or changed commitment is supplied.

{annex}

## Sources and validation

{sources}

Internal inputs are freeze/OT_1999CHUNK8_A_NEUTRAL.md (Carter), A_CARTER_NEUTRAL_CORRECTION.md, A_CARTER_ANALYTICAL_SUPPLEMENT_NEUTRAL.md, CARTER_COMMITMENTS_REVISED.md and CARTER_RECONCILED.md; runtime/OT_1999CHUNK8_CARTER_STONE.md; the authorized entering-law copies; and CARTER_FORM.md / CARTER_COUNTS.json in freeze. Full historical opinion and separate-writing verification was completed in reconciliation; assembly relies on that source-specific freeze, not a claim of independently rereading every historical filing.

Self-validation: five affirm and four dissent; five full-lead supporters; nine Part III supporters; author plus four full joins and four limited joins reconcile; intent and movement independently address both grades; value alone addresses only the higher grade; $1,000 governing threshold and actual $100 request remain distinct; no invented indictment omission, waiver, fact finding or statutory exception; all Stone conditions and all frozen Associate qualifications retained. Each controlling explanation is below 350 words. The assembly validation receipt records computational checks. Workspace integration, render-input generation, term-wide validation and repository commitment remain separate operator tasks.

## Public Projection

## Event

{event}

## Participation

Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated at argument and decision.

## Public Action

The Court affirms the Third Circuit's judgment on the denied bank-larceny instruction.

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

{separate}

## Procedure After Action

{procedure}

## Source Notes

{sources}
'''
draft=root/'runtime'/name.replace('.md','.draft.md');draft.write_text(internal,encoding='utf-8')
public=internal.split('## Public Projection\n')[1]
expected=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
assert re.findall(r'^## (.*)$',public,re.M)==expected
assert public.split('## Holdings\n')[1].split('\n## Precedent Treatment')[0].strip()==holdings
lengths=[len(x.split()) for x in re.findall(r'\*\*Controlling explanation:\*\* (.*?)(?=\n### |\n\*\*Limits common|\Z)',holdings,re.S)]
assert len(lengths)==4 and max(lengths)<=350,lengths
assert not re.search(r'simulat|workflow|October 31, 2026|GitHub|OneDrive',public,re.I)
dest=root/'records'/name;assert not dest.exists();dest.write_text(internal,encoding='utf-8')
receipt={'case':case,'record':name,'public_blocks':'pass','holdings_identity':'pass','explanation_word_counts':lengths,'judgment':'5-4','full_lead_support':5,'Part_III_support':9,'Stone_frozen_compatibility':'reviewed; no fallback or substantive change','no_overwrite':'pass','not_performed':['workspace integration','render input','term-wide validation','Git commitment']}
(root/'freeze/OT_1999CHUNK8_CARTER_ASSEMBLY_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
