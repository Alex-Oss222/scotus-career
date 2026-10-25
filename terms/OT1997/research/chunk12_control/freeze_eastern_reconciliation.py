from pathlib import Path
import hashlib

base = Path('terms/OT1997')
source = base / 'freeze/OT_1997CHUNK12_COMMITMENTS_JUNE25_HISTORICAL.md'
raw = source.read_bytes()
text = raw.decode('utf-8')
start = text.index('## Eastern Enterprises v. Apfel')
end = text.index('## National Endowment', start) if '## National Endowment' in text[start:] else text.index('## NEA', start)
section = text[start:end]
target = base / 'freeze/OT_1997CHUNK12_RECONCILED_EASTERN.md'
assert not target.exists(), 'Completed freezes are immutable; choose a new authorized handoff if correction is necessary.'
header = '''# OT1997 chunk 12 — reconciled non-Stone commitments: Eastern Enterprises v. Apfel

Status: completed historical reconciliation; filesystem-durable handoff. Decision cutoff: June 25, 1998. No author assignment and no Stone position is included. The original frozen commitments remain unchanged. The operative commitments are the adopted E1–E3 and Justice rows copied below, subject to the express clarifications in this reconciliation. No outcome or ground requires a material historical departure.

## Scope and source discipline

This is a reconciliation context, not a neutral modeler. It received the frozen neutral and commitments, the entering-law slice, this case's clean comparator and the bounded control verification. It did not receive the raw runtime comparator, original briefs, private position, private Decision Record audit or control receipt. An earlier Diamondstone comparator extraction inadvertently displayed the opening of the adjacent Monge comparator; that bounded limitation was disclosed to the operator, supplies no premise here and was never passed to a neutral modeler. Historical writings are evidence of the individual Justices' positions, not entering law. The no-Git instruction means this freeze is durable on the filesystem for later operator handling.

## Actual sources and material tests

- Frozen neutral: `OT_1997CHUNK12_NEUTRAL_JUNE25_HISTORICAL.md`, Eastern section and source supplement, including the actual tier-three assignment, pre-1966 employment and early fund participation, later subsidiary ownership/dividends, and the distinction between the assessed annual premium and competing lifetime estimates.
- Frozen entering law: `OT_1997CHUNK12_ENTERING_LAW_JUNE25.md`, Concrete Pipe's actual contextual takings and rational pooled-allocation holdings; Carlton's rational review of retrospective operation and distinct O'Connor/Scalia/Thomas positions; Phillips's ownership-only holding and reserved taking/compensation questions. None replaces the actual facts with a per se rule about money, a fixed lookback deadline or automatic immunity from private contribution limits.
- Historical comparison: [official United States Reports, 524 U.S. 498–568](https://www.govinfo.gov/content/pkg/USREPORTS-524/pdf/USREPORTS-524-498.pdf), saved as `research/chunk12_control/USREPORTS-524-498.pdf` and mechanically extracted `.txt`; the control verifier read the complete opinion set. This context read the substantive plurality analysis, including its remedial channel, historical funding distinctions and all merits/remedy qualifications, and the complete Thomas, Kennedy, Stevens and Breyer writings. The decisive checks are plurality 519–538, Kennedy 539–550, Stevens 550–553 and Breyer 553–568, including their notes. No original party brief was opened.

The compensation-channel objection survives independently of the Government's position: the three takings proponents accept equitable protection because mandatory transfers to the private Combined Fund would not sensibly carry a corresponding Treasury reimbursement under this scheme. That is not a general exception to compensation as the remedy for a lawful taking. Kennedy rejects the property predicate and does not join the plurality's Tucker Act reasoning; neither do the four affirmers.

The fund obligation operates against Eastern's general assets without selecting an account, accrued interest, lien or parcel. Kennedy and the four affirmers reject the asserted taking on that antecedent ground. Phillips identifies ownership of actual interest and leaves taking/compensation separate; it does not displace their distinction. O'Connor, Scalia and Thomas instead apply the actual Concrete Pipe contextual method to an unusually remote obligation, without making every liability a taking. The historical comparator confirms this same disagreement; no prior simulated holding compels its erasure.

The due-process division also remains. Carlton requires rationality of the retrospective operation itself and leaves severe different applications open. Kennedy treats this case as a rare arbitrary mismatch, rather than declaring all retroactivity unconstitutional. The four affirmers accept a rational legislative connection between the assigned former workers, the earlier shared benefit undertaking and the scheme, with later ownership/dividends as additional context. The historical dissent's distinction between an enforceable lifetime contract and rational reliance on an industry understanding supports that limited ground. These Justices need not find that Eastern entered an enforceable lifetime promise, and they do not hold that former employment alone justifies every future obligation. The frozen neutral treats the contested expectation account as a reported rationale, not a new adjudicated fact; reconciliation does not turn it into one. Scalia and Thomas's rejection of substantive economic due process is a separate method, not a join in the affirmers' application.

## Final disposition and join matrix

| Justice | Disposition | Final grounds and permitted joins | Historical check |
|---|---|---|---|
| Stevens | Affirm the constitutional enforcement judgment. | E1 district-court merits posture; E2 rejects taking of unspecified general assets; E3 sustains rational retrospective allocation on the workforce/fund relationship with ownership context. No automatic revenue safe harbor, enforceable-contract finding or unrestricted employment-only rule. | His historical joins and separate dissent support rejection of both challenges, including deference to rational legislative evaluation of the pre-1974 benefit understanding. No changed premise is needed. |
| O'Connor | Reverse and remand for declaratory/injunctive relief against Eastern's tier-three assessments. | E1 bounded equitable channel and E2 contextual taking, considering severity, remote reach and mismatch with later lifetime guarantees together. E3's serious concern may be stated, but she does not supply an independent due-process invalidation holding. | Historical takings analysis and remedy remain intact. Actual Carlton does not create a one-year ceiling; actual Phillips does not decide this taking by ownership alone. |
| Scalia | Reverse and remand for the same bounded relief. | Joins E1 and E2 at O'Connor's stated scope. Does not join Kennedy's substantive economic due-process ground; no procedural defect is found. His rejection of that substantive theory is not an affirmative vote for all the affirmers' reasoning. | Historical takings join and the date-eligible Carlton/TXO objection support precisely these limits. |
| Kennedy | Reverse and remand solely on due process. | Rejects E2 because no identified property interest is appropriated; joins the five-Justice rejection at that level only. E3 finds an exceptionally severe and remote imposition lacking the requisite rational relationship. He does not join the three proponents' E1 compensation analysis. | His historical separate writing confirms both the property distinction and rare-invalidity due-process rationale. No new factual finding of total economic exit or universal lookback limit is used. |
| Souter | Affirm. | E1 merits posture, E2 general-liability distinction, and E3 rational retrospective connection to the former workers and fund participation. No newly adjudicated lifetime promise or unlimited retroactivity rule. | Historical joins in both dissents and actual Concrete Pipe/Carlton support the frozen limited rationale. |
| Thomas | Reverse and remand for bounded tier-three relief. | Joins E1/E2 contextual taking; rejects independent substantive economic due-process invalidation. No per se dollar or temporal threshold. | Historical takings join confirms the ground. His historical suggestion that Calder might be reconsidered in another case is not needed to decide any component and is not imported as an additional simulated writing or holding. |
| Ginsburg | Affirm. | E1 merits posture, E2 lack of specific property appropriation, E3 rational retrospective allocation grounded in employment/fund participation and continuing ownership context. No indemnity adjudication or contract finding. | Historical dissent joins support these grounds; absence of a prior participation in Concrete Pipe does not prevent applying its governing rule. |
| Breyer | Affirm. | E1 merits posture, E2 general-liability distinction, E3 rational allocation based on the full relationship rather than a claim that any past employment suffices. Severity is acknowledged; approximate legislative allocation need not be mathematically exact. | Historical separate dissent, joined by the other three affirmers, supports the same limited disposition and distinction between reasonable industry expectations and enforceable promises. |

## Reconciliation conclusion and limits

All eight frozen dispositions are retained: four reverse (O'Connor, Scalia and Thomas on takings; Kennedy only on due process), and four affirm (Stevens, Souter, Ginsburg and Breyer). Five reject the general-liability takings ground, but they divide on the judgment. No Marks or other common-rationale claim may combine Kennedy's due-process invalidation with the three takings votes: neither rationale is a logical subset of the other.

Relief is confined to the tier-three assignments actually assessed against Eastern. No invalidation of tiers one or two, other operators' assignments, unassigned beneficiaries, the separate 1992 plan, a new statutory assignment claim, contractual indemnity, or a fixed damages award is adopted. No independent historical departure line is warranted. The no-binding-contract distinction and unresolved corporate/indemnity issues are limits on the decision, not blockers to these commitments. A proposed broader resolution of those issues would require fresh neutral source work and affected modeling; assembly may not infer it from this freeze.

No unresolved blocker remains for this bounded reconciliation. Stone participation, final compatibility, controlling effect and assignment belong to assembly after its authorized handoff.

## Adopted original Eastern commitments — mechanically copied

The following original case section supplies the full two-path comparison, Justice-specific date-eligible support, objections and E1–E3 definitions adopted above. Its text is copied mechanically, not rewritten. The foregoing express qualifications govern any potential ambiguity about joining the Tucker Act analysis or an employment-only rule.

'''
target.write_text(header + section, encoding='utf-8', newline='\n')
assert source.read_bytes() == raw
written = target.read_text(encoding='utf-8')
assert written.endswith(section)
print(str(target), len(target.read_bytes()), hashlib.sha256(target.read_bytes()).hexdigest())
print('original unchanged', hashlib.sha256(raw).hexdigest())
