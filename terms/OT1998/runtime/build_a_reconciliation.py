from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'freeze/OT_1998CHUNK6_A_COMMITMENTS.md'
text = source.read_text(encoding='utf-8')
start = text.index('## 1. Central State')
end = text.index('## 4. Jones')
header = '''# OT1998 chunk 6 — first three reconciled Associate commitments

**Status:** Durable historical-reconciliation handoff for Central State, Kumho Tire and South Central Bell. Final non-Stone commitments below retain the independent-model text verbatim. The reconciliation qualifications following them govern interpretation. This is neither an entered judgment nor an opinion assignment.

**Boundary:** This fresh reconciliation context received only the authorized frozen neutral, legal and public-position handoffs, frozen Associate commitments and scoped historical comparator. No current Stone position, separately frozen Stone petition position, private Stone material, raw Decision Record, or Git material was accessed. Public earlier positions in authorized reading copies are continuity evidence only. No blind claim extends to ordinary background model knowledge.

**Cutoffs:** March 22, 1999 for Central State; March 23, 1999 for Kumho Tire and South Central Bell. All eight Associates participate. Stone is absent from these determinations. The Central State petition poll is internal; it is distinct from the summary-merits count.

'''
notes = '''
## Historical reconciliation conclusions

### Central State

The complete official per curiam and all separate writings confirm the independent commitments. O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer support grant and summary reversal on the bounded federal rationality ground; Stevens would deny review and, if review occurs, insist on plenary consideration. His historical dissent expressly withheld an ultimate merits position. His frozen stage objection must therefore never become a vote to affirm Ohio's federal rule. The historical reported merits count supplies no independently published petition poll.

The altered simulated Heller premise has been examined rather than silently replaced by historical Heller. Souter, O'Connor and Stevens adopted Heller's actual-disadvantage inquiry; Kennedy, Scalia and Thomas retained its distinct rational family-participation holding. Beach still supplies the no-empirical-certainty rule. Ginsburg and Breyer's published Equality Foundation positions likewise require a real relationship to the enacted disability. The workload category and teaching objective supply that relationship for the seven reversing Associates, unlike the disconnected proof disadvantage or sweeping civic foreclosure. No Justice's judgment changes during reconciliation.

Ginsburg's historical concurrence, joined there by Breyer, confirms ordinary rationality, the limited scope of summary adjudication, and Ohio's freedom to decide independent state law. Those points are already accommodated in the bounded common ground and remand; history does not require importing a separate writing. Stevens's separate-writing function is his national-significance/summary-treatment objection and concern that a management objective alone must not obscure the comparison with other workers. No affirmative merits invalidation or new academic-freedom holding follows.

**Source limit:** The official footnote describes grandfathering of collective agreements in effect on the statute's effective date until expiration, a detail absent from the frozen neutral packet. It is not used to choose a vote or retroactively broaden the holding. This handoff authorizes no determination that an existing agreement was displaced. If assembly proposes to describe that statutory operation, the missing detail must first pass fresh neutral validation. The official dissent also emphasizes the state-constitutional basis of the Ohio discussion; the frozen premise remains review of the supplied federal ground with independent Ohio law expressly left open. No new state-ground finding is made here.

### Kumho Tire

All eight Associates retain K1–K2. O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer retain K3 and reversal; Stevens retains vacatur and appellate application. Every Associate's frozen judgment and operative proposition matches the historical comparator at this level. The match is also independently supported by simulated Daubert and Joiner: the uniform review and inference rules survived, Kennedy's application was joined by the seven now sustaining exclusion, and Stevens previously reserved application for the appellate court.

The historical Scalia concurrence confirms a boundary already present in K2: discretion chooses a reasonable method of screening, not inadequate screening or abandonment of it. Its historical O'Connor and Thomas joins are evidence, not assigned future joins. Their frozen complete K2 agreement preserves that proposition without requiring a redundant separate opinion. Stevens's necessary separate-position function remains the grant/remedy distinction; he does not contest the common Rule 702 rule, command admission, or find the factual exclusion erroneous. The Court of Appeals must apply the right standard on his proposed route. No other author's historical assignment is imported.

The source's finer application details beyond the sanitized objective handoff are not made new decisional premises. K3 rests on the already frozen record of the four-sign method, actual wear and repair, acknowledged symptoms, inferential threshold, and flexible reconsideration. The rule permits this exclusion; it does not require every judge to exclude every visual-inspection proffer.

### South Central Bell

Each of the eight Associates retains S1–S3. The historical unanimous judgment and common grounds confirm review of a State's own judgment, rejection of stranger preclusion, actual franchise-tax discrimination and failure of compensation. Simulated Richards and unanimous Fulton independently support those same results. The conditional remedy in S3 derives from existing simulated Fulton, Reich and surviving McKesson; it is not a representation that the historical opinion chose refunds or adopted a replacement tax.

Scalia and Thomas's narrower West Lynn position does not prevent their full join on this express foreign/domestic discrimination and the established compensation predicates. The historical O'Connor and Thomas concurrences concern the State's late invitation to abandon dormant-Commerce-Clause doctrine. The frozen neutral packet establishes no such preservation event; no lateness, waiver or separate-writing assignment is imported. O'Connor's historical refusal to reconsider the doctrine and Thomas's procedural concurrence do not alter their frozen application of binding law at the stated scope. No supported contrary Justice-specific premise requires a changed vote.

The historical figures, exact letter requesting abeyance, and asserted litigation concessions are not imported into the frozen facts. The authorized common rationale rejects only the legally insufficient binding relationship described in the packet and the supported unequal tax operation. Independent state remedial choices remain for remand.

## Source-reading receipt and release limits

Read completely: Central State official U.S. Reports pp.124–134, including its statute footnote and Stevens's five footnotes; Cornell Kumho 97-1709.ZS, ZO, ZC and ZX; Cornell South Central Bell 97-2045.ZS, ZO, ZC and ZC1, including every writing and all supplied footnotes. Cross-checked dispositions, opinion structure and operative passages against the bounded official Kumho and South Central Bell extracts. Cornell copies are complete individual writings, not combined-page fragments. Historical sources serve comparison only.

Authorized frozen neutral packets, supplement, objective Kumho record and headers, relevant selected Holdings/Standards, published positions and current Equality Foundation public material were read. Their text remains unchanged. No new original petition, merits brief, joint appendix, consent, waiver, concession or factual finding is certified. No material neutral premise is silently patched.

**Final reconciliation result:** No changed Associate judgment or operative-rule join in these three matters. No author is assigned. Existing join barriers, grounds, limits and remedies above remain operative. The Central State statutory-operation detail is a scope limit requiring neutral treatment only if that operation is to be stated; it is not a reason to stop the bounded federal judgment already supported by the packet.
'''
payload = header + text[start:end] + notes
payload += '\n**Independent commitment input SHA-256:** ' + hashlib.sha256(source.read_bytes()).hexdigest() + '\n'
for folder in ('runtime', 'freeze'):
    (ROOT / folder / 'OT_1998CHUNK6_A_FIRST3_RECONCILED.md').write_text(payload, encoding='utf-8', newline='\n')
print('First-three reconciliation written identically to runtime and freeze.')
