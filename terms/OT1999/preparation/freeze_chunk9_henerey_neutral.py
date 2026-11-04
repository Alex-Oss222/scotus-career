from pathlib import Path
import hashlib

term = Path(__file__).resolve().parents[1]
paths = [term/'preparation'/'OT_1999CHUNK9_HENEREY_CONTROL_FACTS.md', term/'preparation'/'OT_1999CHUNK9_HENEREY_RULE_SOURCE.md', term/'entering-law'/'OT_1999CHUNK9_HENEREY.md']
texts = [p.read_text(encoding='utf-8-sig').rstrip() for p in paths]
intro = '''# Frozen neutral packet — Henerey v. City of St. Charles, School District

Fresh neutral validation completed November 3, 2026. This packet supplies no modeled vote, assignment, Stone position or target historical Supreme Court outcome. It supplements and corrects generic framing in the approved runtime Section I without editing that input. Exact saved source handoffs are copied below.

## Event and current law

The approved simulation grant was March 20, 2000, with argument or submission May 2 and merits consideration June 26. The review concerns the December 29, 1999 Eighth Circuit judgment at 200 F.3d 1128, affirming summary judgment. These Supreme Court calendar placements are supplied scheduling premises, not recovered historical orders. The nine seated Justices are Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer; no case-specific nonparticipation is supplied. Independent modeling concerns the eight Associates.

Use the OT1998-close law as supplemented by effective current-term law, including June 19 Santa Fe at its actual scope. The current cursor is June 26. Uncoordinated June 26 decisions share entering law and operate together only prospectively. No current-case legal conclusion follows from the fact that review was granted.

## Independent framing and completeness checks

The first granted issue concerns whether this particular expression is independent student advocacy or part of the school's sponsored educational process; the second concerns the permissible enforcement of genuinely viewpoint-neutral rules. The grant's wording supplies no stipulation that this enforcement was neutral. The court must identify the governing protection before deciding whether the actual grounds and sanction satisfy it.

The record is at summary judgment, with evidence and reasonable inferences viewed favorably to Henerey. The majority's tacit-approval and neutrality conclusions and Wolle's contrary pretext, notice and sanction inferences must remain distinct. No trial found either the asserted pretext or its absence. The principal disqualified Henerey before the completed count revealed his majority; the packet does not invent retaliation for the electoral result. The number of distributed items differs in the reported accounts and does not require an invented reconciliation.

The principal's stated advance-approval ground and the appellate court's independent content-related ground must each be tested. A supported lawful ground may sustain judgment, but a merely imaginable reason is not the actual causation showing. An inference of one impermissible reason is not automatically final liability: Settle preserves the protected-conduct and substantial-or-motivating-factor showing and a separate preponderance same-decision defense. Neither the validity of a general approval rule nor the mere controversial character of a subject settles actual enforcement or sanction.

KJ-R's copied text preserves separate location approval, previous-day-or-earlier approval, additional time for difficult materials, stamping, the listed unacceptable categories, the superintendent-or-assistant fundraising exception, and the residual permission for materials outside the forbidden categories. The policy excerpt is expressly incomplete. It cannot establish a fixed twenty-four-hour decision guarantee, a universal disruption condition for every category, or the validity of an unquoted clause.

The available paths are to apply Hazelwood and sustain a supported legitimate sanction, to apply Hazelwood but vacate for a material factual or legal defect in the actual grounds or sanction, or to apply Tinker to independent expression with its distinct requirements. Framing these paths supplies no conclusion about the factual inferences or final judgment. Settle does not impose universal curricular viewpoint neutrality; Boring addresses a teacher's personal claim over assigned institutional instruction, while Good News/Good Sports concerns actual private access. Santa Fe's official representative religious-choice mechanism does not itself classify every student election as official speech.

The summary-judgment damages controversy must remain separate from any expired office claim. Defendant identity, personal and official capacities, municipal attribution, conduct-date immunity and available relief are not interchangeable. April 1997 governs immunity notice; later Boring and Santa Fe may be merits law without supplying retroactive notice. A vacatur need not compel a trial, discovery, reinstatement, approval of a message or damages. A supported independent lawful disposition remains available on remand.

## Readiness and exact source limits

Ready for independent modeling on the supplied granted questions and source-supported alternatives. The packet does not certify recovery of the complete original Rule KJ-R, trial record, exact damages demand, a waiver, an immunity ruling below or hypothetical Supreme Court briefs. Any result relying on an unquoted policy clause, a particular damages amount, established waiver or a previously decided immunity defense requires that specific source. Their absence is not litigant default. No current factual premise is supplied merely to avoid an inconvenient record dispute.

Research cutoff for merits law is June 26, 2000; the conduct-date inquiry remains separately limited to April 1997. The exact Settle reusable-rule entry and Boring public dissent were requested and supplied before freeze. The lower court's historical Good News/Good Sports disposition is superseded by the actual simulated holding in the copied slice. No unresolved material omission prevents the bounded classification, actual-ground and sanction analysis.

'''
packet = intro
for label, text in zip(['Validated objective source extraction','Exact published policy excerpt','Exact focused entering-law handoff'], texts):
    packet += f'## {label}\n\n{text}\n\n'
out = term/'freeze'/'OT_1999CHUNK9_HENEREY_NEUTRAL.md'
receipt = term/'freeze'/'OT_1999CHUNK9_HENEREY_NEUTRAL_VALIDATION.md'
if out.exists() or receipt.exists():
    raise RuntimeError('Refusing to replace existing freeze')
out.write_text(packet, encoding='utf-8', newline='\n')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
body = '''# Henerey — fresh neutral validation receipt

Status: READY for independent non-Stone modeling; no votes or assignments produced.

Allowed sources actually used: `AGENTS.md`; `foundation/ENGINE.md`; Henerey Section I in `runtime/OT_1999CHUNK9_NEUTRAL.md`; the three handoffs identified below; and scoped institutional, chronology, school-speech and Henerey entries/searches in `workspace/neutral-projection.md`. This continuing neutral-only context also validated other current-chunk neutral handoffs; it has received no Henerey Stone supplement, comparator, commitment, raw Record or excluded current-case Supreme Court disposition.

The validator checked neutral framing, competing positions, lower-court alternative grounds and dissent, current-law scopes, statute/policy qualifications, summary-judgment proof posture, causal burdens and distinct remedy/defense limits. It requested and received the Settle Standards and Tests entry and the exact Boring public dissent before freeze. Their saved text is mechanically copied along with the rest of the handoffs.

The key correction to the original Section I is that its characterization of viewpoint neutrality cannot replace adjudication of the supported contrary inference. The principal's actual process ground and appellate content ground remain separate, as do Tinker and Hazelwood paths. More-than-one-school-day review for difficult materials is preserved; no mandatory twenty-four-hour guarantee is inferred. The program label does not itself resolve viewpoint, actual cause or proportionality of the sanction.

Exact remaining source limits: the complete KJ-R, exact damages demand, trial-record facts beyond the published recitation, alleged waiver, any lower immunity ruling and hypothetical Supreme Court briefs are unrecovered. A decision depending on one must obtain the particular source or leave that component to ordinary lawful proceedings. No blanket source-gap blocker or invented fact is imposed on the supported merits questions. The validator has not itself read the original appellate PDF; the source extractor certifies all fourteen pages, including dissent, and this receipt claims only independent validation of the supplied sanitized handoffs.

Snapshot integrity:

'''
for p in paths+[out]:
    body += f'- `{p.relative_to(term).as_posix()}`: SHA-256 `{sha(p)}`.\n'
receipt.write_text(body, encoding='utf-8', newline='\n')
assert all(t in out.read_text(encoding='utf-8') for t in texts)
print('Henerey neutral packet and receipt created. All three exact handoff copies verified.')
