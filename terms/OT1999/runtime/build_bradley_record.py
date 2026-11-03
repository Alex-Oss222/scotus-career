from pathlib import Path
import re
import json

root = Path(__file__).resolve().parents[1]
target = root / 'runtime/bradley-v-arkansas-department-of-education_merits_2000-06-12.draft.md'
holdings = '''**Common authority:** Justice Thomas's Opinion of the Court is joined in full by Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Ginsburg and Breyer. All nine directly adopt the following holding, application and limits.

### Actual acceptance of the disclosed IDEA funding condition supplies consent

**Holding and operative rule:** A State that voluntarily accepts IDEA assistance after the effective express condition in §§1403 and 1415 consents to federal judicial enforcement of the obligations of that funded program, within the recipient, claim and remedy covered by the condition. Arkansas's acceptance under that notice removes sovereign immunity from the Bradley IDEA action, including the same sovereign immunity asserted for the named officer in his official capacity; it supplies neither a general waiver for Arkansas nor consent inferred from ordinary regulated activity.

**Controlling explanation:** The condition identifies the State, the federal forum and violations of IDEA. Section 1415 places federal judicial review among the procedures attached to the funded education program. Arkansas conceded both the spending-power validity of IDEA and its receipt of IDEA funds; its acceptance followed the express immunity condition. The present record supplies no retroactive surprise or coercive demand defeating that acceptance.

Atascadero requires unmistakable notice of federal suit. That requirement is satisfied here. Dellmuth identifies the earlier absence of the necessary statutory clarity; the express provision cures that notice defect. The heading and abrogation phrasing of §1403 do not obscure the consequence that the operative text discloses to a recipient. Congressional intent alone is insufficient, but the State's actual acceptance supplies the additional choice.

College Savings Bank rejects consent inferred from continued ordinary commerce and leaves particular accepted-benefit conditions unresolved. Accepting this identified assistance on disclosed enforcement terms is the different transaction that was absent there. South Dakota v. Dole requires a relationship between the condition and the funded undertaking; enforcing the duties of this very program satisfies that requirement. Cedar Rapids preserves an expressly disclosed IDEA obligation despite substantial compliance costs; cost alone does not erase the condition. None of these decisions dispenses with actual acceptance or establishes a universal waiver from federal funding.

The consent ground resolves the immunity appeal. The Court need not decide independent Article I or Section 5 abrogation. A difference between IDEA's protection and the constitutional minimum does not itself defeat preventive enforcement, as Boerne and Florida Prepaid establish, but neither does it establish IDEA's constitutional validity. No individual constitutional violation is an added prerequisite to proceeding on the consent ground.

**Operative qualifications and limits:** Section 1403(c) applies to violations occurring in whole or in part after October 30, 1990. Section 1403(b) makes legal and equitable remedies available only to the same extent as against another public entity; it creates no additional category of relief. The Bradleys seek prospective compliance, not compensatory or punitive damages. Lane's distinction between substantive coverage and consent to a particular remedy remains applicable; no unrequested damages question is decided.

Section 1415(i)(2) permits an aggrieved party's civil action concerning the presented complaint after the specified administrative decision and appeal route: a party aggrieved under subsection (f) or (k) without a subsection (g) appeal, or a party aggrieved by the administrative appeal decision, may proceed in a competent state court or federal district court without an amount-in-controversy requirement. The court receives the administrative record, hears additional evidence at a party's request, and grants appropriate relief on the preponderance of the evidence. Section 1415(l) preserves rights, procedures and remedies under the Constitution, the Americans with Disabilities Act of 1990, title V of the Rehabilitation Act of 1973, and other federal laws protecting children with disabilities. Before a civil action under those laws seeking relief also available under IDEA is filed, it requires exhaustion of subsections (f) and (g) to the same extent as for an IDEA action. Immunity denial neither finds these predicates satisfied nor excuses them.

The Court decides no educational violation, hearing violation, exhaustion issue, individual liability or particular decree. An independent prospective-officer claim still requires a connected officer, an ongoing federal violation and genuinely prospective relief; a treasury claim for past injury cannot become prospective by naming an employee. The Court creates no new defendant or officer claim. Jim C. and its Section 504 claim are outside the grant; IDEA acceptance establishes no Section 504 waiver. That statute's own federal-suit notice, accepted assistance and remedial scope require separate consideration in a case properly presenting them.'''

precedent = '''- **Atascadero State Hospital v. Scanlon, 473 U.S. 234 (1985):** Applies its requirement of unmistakable notice of a federal-suit condition; actual IDEA acceptance under the express text satisfies that requirement rather than displacing it.
- **Dellmuth v. Muth, 491 U.S. 223 (1989):** Distinguishes the earlier statutory absence of a clear State/federal-suit provision; its clarity requirement remains, while §1403 supplies the notice missing there.
- **South Dakota v. Dole, 483 U.S. 203 (1987):** Applies relatedness to enforcement of this funded program and preserves the coercion limit; the record does not establish a coercive demand defeating the conceded program acceptance.
- **College Savings Bank v. Florida Prepaid Postsecondary Education Expense Board (June 23, 1999):** Applies the distinction between congressional intent and actual State consent. Its rejection of consent inferred from ordinary commercial participation remains; the Court resolves the reserved accepted-benefit question only for the identified IDEA condition.
- **Cedar Rapids Community School District v. Garret F. (March 3, 1999):** Preserves the enforceability of a disclosed IDEA obligation despite continuity or substantial cost. Its service holding does not establish this claim's merits, immunity or a damages entitlement.
- **Lane v. Peña, 518 U.S. 187 (1996):** Applies the distinction between substantive duty and consent to the asserted remedy. This State-program holding supplies no general federal or State damages waiver.
- **Seminole Tribe of Florida v. Florida; Florida Prepaid Postsecondary Education Expense Board v. College Savings Bank; Kimel v. Florida Board of Regents:** Preserve the distinct inquiries into express suit authorization and constitutional power. Florida Prepaid's Article I holding and Kimel's application remain controlling; this consent decision neither relies on nor rejects an independent application of that power to IDEA.
- **City of Boerne v. Flores; Florida Prepaid; United States v. Morrison / Brzonkala v. Morrison:** Preserve fitted preventive Section 5 legislation reaching some conduct not independently unconstitutional. No blanket IDEA invalidity, constitutional education right or mandatory individual-violation rule follows; IDEA's Section 5 validity remains undecided here.
- **Kentucky v. Graham, 473 U.S. 159 (1985):** Applies the identity of the sovereign immunity asserted in official capacity with that possessed by the governmental entity; the same consent defeats that immunity without deciding personal liability.
- **Ex parte Young; Edelman v. Jordan; Idaho v. Coeur d'Alene Tribe of Idaho:** Preserve the connected-officer, ongoing-federal-violation and genuinely prospective-relief requirements, including the bar on treating retrospective treasury compensation as prospective relief. No separate officer decree is entered.'''

opinion = '''| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| Opinion of the Court | Thomas | Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Ginsburg and Breyer | Unanimous affirmance of the IDEA immunity denial | Entire informed-funding-consent ground, statutory and remedial limits, constitutional reservations and bounded return |'''

judgment = '''**Affirmed and remanded, 9–0.**

**Supporting:** Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer.

The judgment denying sovereign immunity in the Bradley IDEA action is affirmed on the funding-consent ground. The case returns through the Eighth Circuit for ordinary adjudication in the District Court. The Court establishes no violation of a free appropriate public education obligation or hearing requirement and awards no damages, injunction, fees or other relief. The same sovereign-immunity defense asserted for Crowley in official capacity fails within the accepted condition; personal-capacity liability is not decided. No judgment is entered concerning Jim C., Section 504 or other ungranted claims.'''

event = '''Bradley v. Arkansas Department of Education. Merits decision, June 12, 2000; certiorari granted March 20, 2000; submitted on full merits briefing April 25, 2000. On writ of certiorari to the United States Court of Appeals for the Eighth Circuit, reviewing 189 F.3d 745 (August 31, 1999), appellate No. 98-1010. Review is confined to the Bradley IDEA immunity ruling; the accompanying appellate No. 98-1830, Jim C., is outside the grant.

Arkansas seeks reversal of the denial of immunity to the Department of Education and its employee Mike Crowley. The District Court's November 21, 1997 order in No. LR-C-96-1004 denied dismissal or summary judgment and stayed the merits during the immunity appeal. The Eighth Circuit affirmed the IDEA denial on accepted-funding terms and also discussed prospective officer relief. The questions concern clear federal-suit notice, actual acceptance and the scope of that consent, with independent abrogation grounds unnecessary if consent suffices.

Thomas and Dianna Bradley, on behalf of their son David, allege deficient procedures for review of his individualized education program and failure to perform IDEA responsibilities. The asserted hearing-timing and witness-process failures are allegations, not findings. They seek prospective compliance rather than compensatory or punitive damages.'''

procedure = '''The immunity appeal is resolved. On issuance of the mandate, the case returns through the Eighth Circuit for ordinary IDEA proceedings in the District Court. The mandate affirms immunity denial and directs no particular evidentiary hearing, finding, educational arrangement or award. Administrative prerequisites, the actual federal duty, proof, proper-defendant requirements and available relief remain for adjudication on their own terms. Any independent prospective-officer relief requires its own established predicates. No companion proceeding is brought within the grant.'''

law = '''Effective June 12, 2000, actual voluntary acceptance of IDEA assistance under the express federal-suit condition supplies program-specific consent. Lower courts must distinguish that acceptance from general federal receipts, ordinary regulated activity and congressional intent alone. This holding adds an application of accepted-benefit consent left unresolved in College Savings; its commercial-consent rule remains unchanged. Consent removes this immunity defense while preserving the statute's temporal and remedial limits and the ordinary prerequisites to relief. Existing Article I and preventive Section 5 law remains effective, without a new IDEA abrogation holding. No law concerning Section 504 immunity is adjudicated.'''

sources = '''The [official Eighth Circuit opinion, 189 F.3d 745](https://ecf.ca8.uscourts.gov/opndir/99/08/981010P.pdf), supplies the interlocutory posture, Arkansas's program-receipt and spending-validity concessions, the claims' prospective character and the distinct Jim C. disposition. The [United States' intervention brief](https://www.justice.gov/sites/default/files/crt/legacy/2010/12/14/bradley.pdf) supplies the pleaded procedural complaints and the argument concerning post-enactment acceptance; its advocacy does not establish a merits violation. The [enacted 1997 IDEA text, Public Law 105-17](https://www.govinfo.gov/content/pkg/PLAW-105publ17/pdf/PLAW-105publ17.pdf), supplies §§604 and 615, codified at §§1403 and 1415. The grant and submission dates identify this proceeding's limited review; no Supreme Court docket number is supplied.'''

internal = '''**Case and dockets:** Bradley v. Arkansas Department of Education; Eighth Circuit No. 98-1010; no Supreme Court docket number supplied.
**Event and date:** Plenary merits decision, 2000-06-12; October Term 1999, chunk 8.
**Result:** IDEA immunity denial affirmed, 9–0, on actual acceptance of the disclosed funding condition; ordinary adjudication on remand, without an award.
**Version / lineage:** Original Canonical Decision Record; supersedes no adjudication. Derived from the frozen chunk 8 A neutral and non-Carter reconciled handoffs and the approved October 31, 2026 Bradley supplement.

## Event, chronology and participation

{event}

The March 20 grant and April 25 full-merits submission are adopted scheduling premises already recorded in the frozen neutral packet, not fabricated historical Supreme Court events. No additional oral argument or Supreme Court docket is posited. All nine Justices participate at submission and decision: Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. Nine participants satisfy quorum; five votes suffice for a majority. No supplied recusal or later change affects participation.

Research cutoff: immediately before June 12, 2000. Substantive entering law is effective through June 5. Same-day Harris Trust and other uncoordinated June 12 cases do not supply entering law. Same-day alphabetical order affects assignment counts only.

## Entering law and source limits

The authorized A entering-law slice supplies College Savings, Florida Prepaid, Lane, Boerne, Cedar Rapids and the other identified immunity authorities. A_CURRENT_PUBLIC supplies Kimel and Morrison. Those actual holdings control instead of contrary historical versions quoted below. The official lower opinion supports Arkansas's receipt and spending-validity concessions and the absence of compensatory or punitive damages claims. The intervention brief supports the stated timing of the program acceptance and procedural allegations, without transforming advocacy into findings. The enacted IDEA excerpt verifies the distinct temporal, remedy, administrative-review and exhaustion provisions.

The lower court's categorical Article I bar and its premise that any statutory protection beyond the constitutional minimum defeats Section 5 cannot become governing law. Consent suffices without adopting or resolving either independent abrogation alternative. The source record establishes no educational violation, exhaustion result, coercive dependence, individual liability or particular decree. These are reservations for ordinary litigation, not defaults inferred from unavailable research.

## Stone's approved position and final compatibility

Source: runtime/OT_1999CHUNK8_BRADLEY_STONE.md, approved October 31, 2026, subject to actual earlier effective law. The fixed core affirms on identified funding consent, returns the IDEA claim for ordinary adjudication without finding a FAPE or hearing violation or awarding relief, retains program/claim/remedy limits, reserves independent abrogation, and preserves proper prospective-officer relief while excluding Jim C. and Section 504 from judgment.

The final opinion supports every element of that core. Its clear-notice and actual-acceptance rule is Stone's express ground. Its treatment of constitutional alternatives rejects an automatic constitutional-tort prerequisite without turning preventive authority into blanket IDEA validity. Its separate officer requirements and refusal to borrow IDEA acceptance for Section 504 preserve his stated limits. Section 1403(b) and (c) and the existing §1415 predicates explain enacted limits, not new exceptions or burdens. No substantive narrowing, additional independent ground or unapproved remedy is attributed to him. Stone joins the entire opinion and the judgment; no standing fallback is used and no separate writing performs additional legal work. Earlier Kimel and Morrison do not displace his approved conditional baseline or require a renewed choice.

## Judgment and remedy

{judgment}

## Opinion topology

{opinion}

## Opinion form and assignment

The Bradley form receipt fixed one integrated signed plenary opinion before the fresh count was inspected. One legal ground and its necessary limits resolve the only granted judgment component. Neither opinion form nor proposition structure was selected to affect counts. Chief Justice Stone-Zsela assigns because he joins the unanimous judgment coalition and every proposition of the common ground.

**Fresh counts before assignment:** Stone-Zsela 8; Stevens 8; O'Connor 9; Scalia 9; Kennedy 9; Souter 9; Thomas 8; Ginsburg 9; Breyer 9. Total: 78. The count receipt derives authors from actual earlier Record opinion tables, not previous assignment tallies. **Last counted event:** United States v. Hubbell, June 5, 2000, Kennedy. Preexisting same-day Harris Trust follows Bradley alphabetically and is excluded from this recount; its assignment remains undisturbed.

**Eligible full-ground authors:** All nine named participants. Each Associate's frozen reconciliation supports the whole informed-consent ground and every limiting proposition; Stone qualifies by his approved position, not fallback. The minimum is eight and the ceiling nine. **Balance pool:** Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. **Selected author:** Thomas, eight.

Fit governs; no unresolved objection requires an expansion accommodation. The opinion's work is to distinguish an unmistakable forum condition from general statutory coverage, and actual acceptance from legislative intent, while retaining remedy-specific limits. Thomas's recorded College Savings join demands genuine State choice, and his Kimel statutory dissent insists that the private federal action itself be clearly authorized. His frozen Bradley commitment explains why the unusually direct IDEA text and actual grant acceptance satisfy those distinct concerns. That contrast gives him a concrete fit for explaining consent without importing the constitutional disagreement or weakening the clarity standard. Stone, also eight, is the strongest alternative: his approved framework equally carefully separates consent, power and remedy. Thomas's express clarity objection in the prior immunity case makes the present textual answer particularly direct, without needing new accommodation. Stevens, also eight, offers Cedar Rapids experience and remains fully eligible; that earlier authorship neither confers preference nor disqualifies him. Souter's Lane reasoning supplies strong remedy precision at nine. No ability, ideology, importance or historical authorship exclusion applies. Thomas's one integrated lead counts once.

## Controlling holdings

{holdings}

## Precedent treatment

{precedent}

## Current law and continuity

{law}

{procedure}

There is no roster, circuit-allotment or institutional-practice change. The Court's merits event is completed; continued proceedings below do not make this Supreme Court appeal an unresolved manifest matter. No Section 504 companion event is completed or carried forward by this Record.

## Published noncontrolling positions

No separate opinion or other published noncontrolling position issues. The previously published constitutional disagreements retained in the audit are not newly published alternative holdings or writings in Bradley.

## Adaptive audit annex

The eight Associate commitments, source-specific grounds and historical comparison below are copied mechanically from the frozen reconciliation's Bradley section. Every final disposition and join remains within that commitment; no post-reconciliation change or hypothetical circulation is asserted. Its unused Article I alternatives remain private audit information and are not counted as holdings. No historical Supreme Court Bradley merits decision exists, so no Justice-specific historical Supreme Court departure is asserted. The lower court's different constitutional premises are identified expressly and not adopted.

Assembly exposure disclosure: an initial read of the combined non-Carter reconciliation also displayed its already-frozen Pegram and Reeves sections. No Pegram or Reeves Stone supplement or assignment was accessed during this Bradley assembly. That incidental assembly-stage exposure did not supply a Bradley fact or ground and does not claim a narrower actual exposure than occurred.

{frozen}

## Source map and validation

{sources}

Internal evidence: freeze/OT_1999CHUNK8_A_NEUTRAL.md (Bradley only); freeze/OT_1999CHUNK8_A_NONCARTER_RECONCILED.md (Bradley); runtime/OT_1999CHUNK8_BRADLEY_STONE.md; entering-law/OT_1999CHUNK8_A.md and A_CURRENT_PUBLIC.md; runtime/OT_1999CHUNK8_PRIOR_OPINIONS.md for assignment tables only; freeze/OT_1999CHUNK8_BRADLEY_FORM.md and BRADLEY_COUNTS.json. The official lower opinion was read completely across bounded reads, including notes 6 and 7 and its distinct companion judgment. The relevant enacted sections were read directly. The full intervention brief and its factual framing were validated in the frozen neutral stage; assembly makes no new claim of having read that entire brief.

Substantive self-check completed: one granted component; nine judgment supporters; author plus eight complete joins; every controlling proposition supported by that same nine; no partial join or Marks inference; consent distinct from congressional power, substantive duty and remedy; actual funding acceptance and the concessions distinguished from alleged violations; no Section 504 judgment or invented Supreme Court docket; no educational award; all statutory temporal and remedy qualifications retained; Stone's complete core respected without fallback; no changed Associate commitment. Computational draft validation checks the exact opening labels, eleven-block order, projection holdings identity, topology count, legal-explanation ceiling and nonexistence of an overwritten Record. The validation receipt is freeze/OT_1999CHUNK8_BRADLEY_ASSEMBLY_VALIDATION.json. Repository commitment, workspace integration, render-input generation and term-wide checks are performed separately by the operator; this Record does not certify unperformed operations.

## Public Projection

### Event

{event}

### Participation

Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer participated at submission and decision.

### Public Action

The Court affirms the denial of sovereign immunity in the granted Bradley IDEA action and remands for ordinary proceedings.

### Judgment & Remedy

{judgment}

### Opinion Topology

{opinion}

### Holdings

{holdings}

### Precedent Treatment

{precedent}

### Law After Decision

{law}

### Separate Writings

No separate writing issues.

### Procedure After Action

{procedure}

### Source Notes

{sources}
'''

reconciled = (root / 'freeze/OT_1999CHUNK8_A_NONCARTER_RECONCILED.md').read_text(encoding='utf-8-sig')
frozen = re.search(r'(?ms)^## Bradley v\. Arkansas Department of Education\n.*?(?=^## Pegram)', reconciled).group(0).strip()
# Keep copied headings within the audit annex; substantive source bytes are unaltered.
frozen = re.sub(r'(?m)^(#{2,3}) ', r'\1## ', frozen)
data = internal.format(event=event, judgment=judgment, opinion=opinion, holdings=holdings, precedent=precedent, law=law, procedure=procedure, sources=sources, frozen=frozen)
head, public = data.split('## Public Projection\n', 1)
blocks = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes']
for block in blocks:
    public = public.replace('### ' + block + '\n', '## ' + block + '\n')
target.write_text(head + '## Public Projection\n' + public, encoding='utf-8')
print(target.relative_to(root))
