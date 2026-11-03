from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
name='pegram-v-herdrich_merits_2000-06-12.md'
event='''Pegram v. Herdrich, No. 98-1949. Merits decision, June 12, 2000; argued February 23, 2000. On writ of certiorari to the Seventh Circuit, 154 F.3d 362 (1998), reviewing its revival of an amended ERISA fiduciary-breach count. The issue is whether the challenged HMO treatment and incentive functions support that count. The posture is failure to state a claim, not findings after an ERISA trial.

Herdrich participated through her husband's State Farm employment in an HMO option. HAMP was owned through Carle Clinic, whose physician shareholders supplied care. Medical necessity and outside referrals depended on Carle physicians' judgment; the alleged incentives rewarded lower testing, outside-facility use and referrals. Herdrich alleged that an ultrasound was delayed after discovery of an inflamed abdominal mass and that she was required to travel to a distant Carle facility. Her appendix ruptured, causing peritonitis. Her malpractice claims produced a $35,000 jury judgment, which is outside this review.

The reviewed amended count seeks plan-focused relief under §§409 and 502(a)(2) for the general incentive arrangement and refers to administration of disputed or nonroutine claims. It names no individual physician. Two state fraud counts preceded removal; one was dismissed and the other amended into this ERISA count. The superseded fraud pleading is not an independently presented nondisclosure claim.'''
judgment='''**Reversed and remanded, 9–0.**

**Supporting:** Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer.

The Seventh Circuit's revival of the reviewed amended fiduciary-breach count is reversed. On remand that count shall be dismissed. The $35,000 malpractice judgment and unreviewed counts remain undisturbed. No damages, plan restoration amount, disgorgement, fee award, new individual-physician claim or entitlement to amend is ordered.'''
topology='''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | Ginsburg | Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas and Breyer throughout; Stone-Zsela in Part I only | Unanimous reversal and dismissal mandate | I: function-specific mixed-treatment rule; II: ordinary risk sharing and plan-asset predicates; III: independent assumed-administration pleading ground and its limits |
| Concurrence in part and in the judgment | Stone-Zsela | No other Justice | Joins Part I and reversal with dismissal of the amended count | Mixed-treatment ground; reserves independent administration, misrepresentation and asset-misuse questions rather than joining Parts II–III |'''
holdings='''### I. Inseparable treatment decisions are not fiduciary administration

**Holding and operative rule:** A treating physician does not act as an ERISA fiduciary when making an inseparable decision about medically appropriate treatment and the benefit delivered through that treatment. A separate discretionary decision applying plan-coverage terms can be fiduciary administration, whoever makes it; the rule creates no general HMO exemption and does not exclude every decision involving medical information.

**Authority:** Part I of Ginsburg's Opinion of the Court, joined by all eight other Justices, supplies nine direct votes.

**Controlling explanation:** Section 3(21)(A) attaches fiduciary status to the specified function, rather than every act of a person who performs some plan duties. Varity applies that inquiry to actual administration and protects participants from disloyal administrative conduct. It does not convert medical judgment into plan administration simply because treatment also determines the benefit furnished. The medical-necessity and referral decisions inseparable from furnishing the care here belong to the treatment function. HMO incentives do not, merely by their existence, change that capacity.

Herdrich correctly distinguishes the employer's choice of a plan from a nonsponsor's later acts. Spink and Hughes Aircraft preserve independent fiduciary implementation. The present boundary therefore depends on the act, not employer or corporate status. A physician can administer coverage, and calling a decision medical cannot conceal that distinct function. Conversely, financial consequences do not turn ordinary treatment into ERISA administration. Travelers preserves the distinct setting of ordinary medical regulation; this holding resolves fiduciary status and enters no general malpractice-preemption judgment.

### II. An ordinary incentive arrangement alone establishes neither fiduciary breach nor plan assets

**Holding and operative rule:** Establishing or carrying out an ordinary general compensation and risk-sharing arrangement for providing medical care does not, by that fact alone, establish ERISA fiduciary conduct or breach. The HMO itself is not the employer's ERISA plan, and its revenues and profits are not automatically plan assets; actual authority or control over management or disposition of a plan asset remains governed by the statutory asset branch without an additional discretion requirement.

**Authority:** Part II has eight direct supporters: Ginsburg, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas and Breyer. Stone-Zsela does not join.

**Controlling explanation:** John Hancock requires separate consideration of property, function and liability. The premise that the business furnishing the benefit is itself the plan would improperly make its entire income subject to plan restoration. No general ownership rule governing every premium arrangement follows from rejecting that premise.

Spink separates design from implementation, and Hughes Aircraft examines independently alleged breaches instead of treating economic advantage as breach by itself. The same distinctions matter here. Ordinary medical risk sharing compensates for the service arrangement; it does not alone establish the exercise of an ERISA function or a disloyal act in such a function. Physician ownership does not erase the statutory requirements. This is neither a general net-benefit defense to proved misconduct nor approval of every incentive system. A direct reward for denying a claim, an arrangement making impartial administration impossible, genuine asset diversion and actual disloyal administration present different predicates, none adjudicated by the pleaded general-arrangement theory.

### III. The amended structural theory fails even assuming genuine claims administration

**Holding and operative rule:** Even assuming in Herdrich's favor that the amended reference to disputed and nonroutine claims describes genuine discretionary plan administration, the pleaded general year-end incentive arrangement alone states no independently disloyal claims determination, administration contrary to the plan or direct reward for denying a claim. The reviewed amended count therefore fails on that independent ground, and restoration of supplemental medical-expense payments cannot follow merely by labeling the entire HMO the plan.

**Authority:** Part III is joined by the same eight Associates as Part II and independently supports dismissal. Stone-Zsela joins the judgment on Part I's treatment ground, not this additional rationale.

**Controlling explanation:** The Court gives the administration allegation its asserted scope for this inquiry. It does not find a new administrative event or erase that allegation by treating every HMO decision as treatment. Varity preserves concrete administrative loyalty duties, while Hughes Aircraft requires the alleged implementation theory itself to identify a breach after its legal predicates are examined. The ordinary structural incentive does not alone supply that missing breach.

The strongest contrary argument combines owner control, decision authority and the incentive into self-interested administration. Those circumstances may matter when an actual disloyal determination is alleged, but they do not establish that the ordinary arrangement itself violates the duty or that all business funds belong to the plan. The lower court disclaimed automatic liability for all incentives and characterized care as withheld solely to enlarge bonuses. That characterization and the malpractice verdict are not independent findings of disloyal plan administration or plan loss. The Court applies the ordinary pleading standard and resolves no disputed medical-adequacy question.

Section 409's responsibility and plan-restoration framework and §502(a)(2)'s authorized enforcement channel remain distinct from §502(a)(3)'s individual equitable channel. Mertens's limit on §502(a)(3) compensation is not the ground for dismissal of this §409/§502(a)(2) claim. The requested plan remedy fails on the pleaded predicates, not a categorical rule barring lawful plan restoration.

**Limits and questions not reached:** Section 3(21)(A) separately reaches discretionary plan management, authority or control over management or disposition of plan assets, compensated investment advice or authority or responsibility to provide it, and discretionary authority or responsibility in plan administration. It also includes persons designated under §405(c)(1)(B). Its registered-investment-company qualification provides that plan investment in a registered company's securities alone does not make the company, adviser or principal underwriter a fiduciary or party in interest, except insofar as the company, its investment adviser or its principal underwriter acts in connection with a plan covering employees of the company, adviser or principal underwriter; duties under other law remain. That qualification is not a factual issue here.

No independent disclosure, benefits-reimbursement, contract, malpractice-preemption, regulatory, personal-physician-liability or particular asset-ownership claim is decided. Prior statements about administrator or fiduciary status elsewhere do not establish the challenged function or a supported judicial-estoppel bar here; disclosure responsibility and responsibility for the disclosed incentive are distinct. The amended count does not revive superseded fraud allegations. Direct per-denied-claim rewards, actual asset misuse, misrepresentations and genuinely disloyal administration retain their own statutory predicates and remedies. The Court awards no plan amount and establishes no fee or amendment entitlement.'''
precedent='''- **Varity Corp. v. Howe:** Applies the function-specific inquiry and preserves concrete fiduciary administration and disloyal-misrepresentation liability; its individual equitable-redress holding does not convert this plan-focused claim into a different remedy channel.
- **Lockheed Corp. v. Spink:** Applies the separation of design and actual implementation without immunizing independent administration; sponsor status alone does not decide this claim.
- **Hughes Aircraft Co. v. Jacobson:** Applies its independent examination of implementation and breach predicates rather than equating an advantageous structure with misconduct. Its actual-asset and genuine-administration reservations remain.
- **John Hancock Mutual Life Insurance Co. v. Harris Trust & Savings Bank:** Applies separate inquiries into asset status, function and breach, rather than equating business funds with plan property.
- **Firestone Tire & Rubber Co. v. Bruch:** Preserves trust-law guidance within the enacted fiduciary functions; discretion over treatment alone is not discretion in plan administration.
- **Mertens v. Hewitt Associates:** Preserves §502(a)(3)'s traditional-equity limits but does not bar lawful §409 restoration or supply the reason for dismissing this §502(a)(2) claim.
- **New York State Conference of Blue Cross & Blue Shield Plans v. Travelers Insurance Co.; De Buono v. NYSA-ILA Medical and Clinical Services Fund:** Preserve the distinct operation of ordinary medical regulation; the Court makes no general preemption ruling here.'''
law='''Medical treatment inseparable from the benefit furnished is outside the fiduciary-administration function, while genuine coverage administration remains subject to ERISA. The eight-Justice alternative separately requires an independently supported breach even when administration is assumed; the ordinary general incentive alone does not supply it. HMO form supplies neither fiduciary status for treatment nor immunity for administration. Function, actual plan property, breach and statutory relief remain separate inquiries.'''
separate='''**Stone-Zsela, concurring in part and in the judgment.** He joins the function-specific rule in Part I and the reversal directing dismissal of this amended fiduciary claim. His ground concerns treatment decisions inseparable from the benefit delivered through treatment; payment incentives do not turn that medical function into ERISA administration. He does not join the additional business/asset rationale or the independent no-breach determination that assumes genuine administration in Parts II–III. His position leaves pure administrative decisions, fiduciary misrepresentations, plan-asset misuse and viable malpractice, disclosure, contract and regulatory theories to their own requirements. That reservation supplies no disagreement with the dismissal or new adjudication of those distinct theories.'''
procedure='''The case returns to the lower courts for dismissal of the reviewed amended ERISA fiduciary count. The existing $35,000 malpractice judgment and matters outside this review remain undisturbed. The mandate imposes no new medical, disclosure, regulatory or plan-payment duty and grants no separate right to amend.'''
sources='''The [Records and Briefs collection for this docket](https://archive.org/details/micro_IA40385014_0281) supplies the petition, appendix, joint appendix and merits submissions; the amended count is at petition appendix 83a–87a. The [United States and Department of Labor amicus](https://www.justice.gov/osg/brief/pegram-v-herdrich-amicus-merits) distinguishes medical functions from administration and the general arrangement from an independently alleged breach. The [1998 ERISA fiduciary definition](https://www.govinfo.gov/content/pkg/USCODE-1998-title29/html/USCODE-1998-title29-chap18-subchapI-subtitleA-sec1002.htm), [duty provision](https://www.govinfo.gov/content/pkg/USCODE-1998-title29/html/USCODE-1998-title29-chap18-subchapI-subtitleB-part4-sec1104.htm), and [enforcement provision](https://www.govinfo.gov/content/pkg/USCODE-1998-title29/html/USCODE-1998-title29-chap18-subchapI-subtitleB-part5-sec1132.htm) supply the enacted distinctions. Treatment and incentive allegations are not ERISA trial findings, and the malpractice judgment establishes no independent plan loss.'''
rec=(root/'freeze/OT_1999CHUNK8_A_NONCARTER_RECONCILED.md').read_text(encoding='utf-8-sig')
annex=re.search(r'(?ms)^## Pegram.*?(?=^## Reeves)',rec)[0].strip()
annex=re.sub(r'(?m)^(#{2,3}) ',r'\1## ',annex)
text=f'''**Case and dockets:** Pegram v. Herdrich; No. 98-1949.
**Event and date:** Plenary merits decision, 2000-06-12; October Term 1999, chunk 8.
**Result:** Reversed and remanded, 9–0, for dismissal of the reviewed amended ERISA fiduciary count; existing malpractice judgment undisturbed.
**Version / lineage:** Original Canonical Decision Record; supersedes no adjudication. Uses the frozen A neutral and non-Carter reconciliation and approved October 31, 2026 Pegram supplement.

## Event and participation

{event}

All nine Justices participate at argument and decision. No nonparticipation is supplied. Nine satisfy quorum and five votes suffice. The lawful route is certiorari reviewing the appellate revival of this amended count.

## Entering law and cutoff

Research cutoff: immediately before June 12, 2000; common substantive baseline through June 5. The A slice supplies Varity, Spink, Hughes Aircraft, John Hancock, Mertens and Travelers at their actual simulated scopes. Same-day Harris Trust is counted for assignment but supplies no entering law. No later managed-care authority is used. The claim is §409/§502(a)(2), not an assumed individual §502(a)(3) damages demand. The actual amended claim controls instead of superseded fraud assertions. The source record permits a pleading disposition but not a new medical finding or universal premium-ownership rule.

## Stone compatibility and exact joins

The approved October 31 supplement expressly requires reversal and dismissal on the function-specific, inseparable mixed-treatment ground and preserves pure administration, fiduciary misrepresentations, plan-asset misuse, malpractice and lawful regulation. Stone joins Part I and the judgment. His approved core does not supply an independent breach ruling assuming genuine administration, nor the separate plan-asset/business ground. He therefore withholds Parts II–III. His concurrence preserves these actual reservations; it does not manufacture a disagreement with the result or import the eight Associates' grounds into his position. This is a partial join within the existing fixed core, not a change of remedy or newly added ground. The standing fallback is unnecessary: the only reviewed count's disposition is expressly supplied, and its silence about an independent alternative does not authorize adding reasons. No Associate commitment changes to accommodate Stone.

## Judgment and remedy

{judgment}

## Opinion topology

{topology}

## Opinion form and assignment

The form receipt fixed one signed integrated lead and Stone's limited concurrence before fresh counts. Three parts reflect the actual function, business/property and conditional breach questions. Chief Justice Stone-Zsela assigns because he joins the unanimous judgment; full-ground eligibility remains separate from that judgment agreement.

**Fresh counts:** Stone-Zsela 8; Stevens 8; O'Connor 10; Scalia 9; Kennedy 9; Souter 9; Thomas 10; Ginsburg 9; Breyer 9. Total 81. **Last counted event:** Harris Trust and Savings Bank v. Salomon Smith Barney Inc., June 12, 2000, Thomas. The recount uses actual earlier Record opinion tables, including Bradley, Carter and the preexisting Harris Trust. No later assignment or stopped Ramdass count enters.

**Eligible full-ground authors:** Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. All eight fully support all three parts. Stone is ineligible for the whole lead because his approved core supports only Part I; his count does not set the full-lead minimum. The eligible minimum is eight, ceiling nine. **Pool:** Stevens, Scalia, Kennedy, Souter, Ginsburg and Breyer. O'Connor and Thomas remain substantively eligible but their ten counts place them outside this pool. **Chosen author:** Ginsburg, nine. No split is needed because eight authors can carry the integrated lead.

Fit governs. Ginsburg's Spink and Hughes Aircraft opinions directly distinguish business design from fiduciary implementation and then examine an alleged implementation theory's own missing breach predicates. John Hancock supplies her separate property-function analysis. This opinion requires exactly that separation: dismiss mixed treatment as nonfiduciary, preserve actual administration, and test the asserted structural breach even when administrative status is assumed. Stevens, eight, is the strongest eligible alternative through his Varity and Hughes Aircraft joins; he could faithfully carry all limits, but Ginsburg's directly articulated implementation and property analysis offers the concrete integration advantage. Stone's approved treatment ground is narrower and does not qualify him for the full lead or an assumed-administration accommodation; no general ability judgment excludes him. No expansion, reassignment, historical authorship or fictional circulation is invoked. The integrated lead counts once for Ginsburg.

## Controlling holdings

{holdings}

## Precedent treatment

{precedent}

## Current law and continuity

{law}

{procedure}

No institutional change or new Supreme Court pending matter follows. Independent lawful theories remain governed by their own predicates; the reservation does not establish that any has been pleaded or is entitled to relief.

## Published noncontrolling positions

{separate}

## Adaptive audit annex

The complete Pegram reconciliation is copied mechanically below, preserving each Associate's grounds, limits and historical comparison. The conditional administration rationale assumes the claimant's allegation for legal sufficiency; it does not change the neutral facts or pretend that the historical Court adopted this alternative. Actual Spink/Hughes Aircraft implementation holdings support its separate treatment. No judgment departure occurs. Every Associate fully joins the final bounded ground without revision; Stone's limited concurrence supplies no added Associate ground.

{annex}

## Sources and validation

{sources}

Internal inputs: freeze/OT_1999CHUNK8_A_NEUTRAL.md (Pegram); freeze/OT_1999CHUNK8_A_NONCARTER_RECONCILED.md (Pegram); runtime/OT_1999CHUNK8_PEGRAM_STONE.md; authorized A law; freeze/OT_1999CHUNK8_PEGRAM_FORM.md and PEGRAM_COUNTS.json. Assembly read the relevant enacted exact extracts and actual prior holdings; full current historical opinion and note verification belongs to the frozen reconciliation. No unseen complete filing is claimed read in assembly.

Substantive self-check: nine judgment supporters; nine Part I supporters; eight Parts II–III supporters; author and joins reconcile without treating Stone's judgment agreement as a full join. The current count is plan-focused; Mertens is not its dismissal ground. The asset branch has no added discretion requirement; real administration and distinct misconduct remain open. The conditional assumption neither disregards the pleading nor imposes a heightened pleading rule. Malpractice amount, unreviewed counts, no individual defendant and all remedy limits are retained. Controlling explanations stay below 350 words. The computational receipt checks fixed labels, block order, identical holdings and nonoverwrite. Term-wide validation and projections remain operator tasks.

## Public Projection

## Event

{event}

## Participation

Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated at argument and decision.

## Public Action

The Court reverses revival of the amended ERISA fiduciary count and directs its dismissal on remand.

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
draft=root/'runtime'/name.replace('.md','.draft.md');draft.write_text(text,encoding='utf-8')
public=text.split('## Public Projection\n')[1]
expected=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
assert re.findall(r'^## (.*)$',public,re.M)==expected
assert public.split('## Holdings\n')[1].split('\n## Precedent Treatment')[0].strip()==holdings
lengths=[len(x.split()) for x in re.findall(r'\*\*Controlling explanation:\*\* (.*?)(?=\n### |\n\*\*Limits and questions|\Z)',holdings,re.S)]
assert len(lengths)==3 and max(lengths)<=350,lengths
assert not re.search(r'simulat|workflow|October 31, 2026|GitHub|OneDrive',public,re.I)
dest=root/'records'/name;assert not dest.exists();dest.write_text(text,encoding='utf-8')
receipt={'case':'Pegram v. Herdrich','record':name,'blocks':'pass','holdings_identity':'pass','explanation_words':lengths,'judgment_support':9,'Part_I':9,'Parts_II_III':8,'Stone':'Part I and judgment only; no fallback','no_overwrite':'pass','not_performed':['workspace integration','render input','term checks','Git commitment']}
(root/'freeze/OT_1999CHUNK8_PEGRAM_ASSEMBLY_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt,indent=2))
