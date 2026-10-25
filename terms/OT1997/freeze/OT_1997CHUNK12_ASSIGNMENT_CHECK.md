# OT1997 chunk 12 — independent assignment baseline check

## Finding

The actual pre-June 25, 1998 Records establish **106 counted signed plenary merits opinions and 106 author credits**:

| Justice | Count before June 25 |
|---|---:|
| Stone-Zsela | 12 |
| Stevens | 11 |
| O'Connor | 12 |
| Scalia | 11 |
| Kennedy | 11 |
| Souter | 13 |
| Thomas | 12 |
| Ginsburg | 12 |
| Breyer | 12 |
| **Total** | **106** |

The last counted event is *United States v. Bajakajian*, June 22, 1998, authored by Thomas. The later same-date *Wisconsin Department of Corrections v. Schacht* threshold opinion adds no credit.

The already existing *Swidler & Berlin v. United States* Record, June 25, names Stevens as the sole lead author. Its credit enters only for same-date cases alphabetically after *Swidler*, including *United States v. Balsys*, and for later dates. It does not enter earlier June 25 peers' assignments. With Swidler alone added to the predate baseline, Stevens becomes 12 and the total becomes 107; any other newly completed earlier same-date cases must also be counted afresh at the relevant assignment.

## Independent method and scope

Read Engine §8's countable-opinion and chronology rules. Mechanically extracted only each existing Record's event/date, Public Projection Opinion Topology, and internal opinion-form/assignment statements. The examined population was the 135 Records dated before June 25 plus the existing Swidler Record. No current chunk 12 briefs, runtime substantive handoffs, Stone position, or commitment materials were read.

Every delivering author was independently identified from the actual topology: the named author cells for the Court/lead/judgment-announcing portions, or the direct prose authorship statement. A Justice delivering multiple parts of the same lead receives one credit. Form classifications came from each event and its own form/assignment statement, never from a filename's `merits` token or an earlier reported total. Earlier assignment tallies encountered in those statements were not used as count authority.

Result: 106 qualifying predate decisions; 29 excluded predate events; one later same-date existing opinion (Swidler). No qualifying decision has more than one delivering Justice, so there are no additional multi-author credits. No qualifying lead lacks an identified author. The independent authors and classifications match the root helper for all 136 examined Records. This check does not reopen any completed assignment.

The scoped extraction and independent classification receipt are retained at `tmp/chunk12_assignment_verify_extract.json` and `tmp/chunk12_assignment_verified.json`. The Records and Engine remain the authorities.

## Thirteen signed threshold exclusions

| Matter | Named lead author | Own recorded form / basis for exclusion |
|---|---|---|
| Jefferson v. City of Tarrant | Breyer | Jurisdictional dismissal; its assignment states that this procedural opinion adds no count. |
| Lee v. Harcleroad | Stevens | Reasoned threshold decision; its assignment expressly excludes the threshold lead and separate writings. |
| Spencer v. Kemna | Breyer | Own-threshold mootness disposition; its assignment states that neither it nor its dissent adds a signed plenary merits lead count. |
| Aktepe v. United States | Kennedy | Its event is a plenary justiciability decision. Its own assignment expressly says: “This signed threshold opinion is uncounted under Section 8: it resolves nonjusticiability, not the merits, notwithstanding plenary review.” |
| Texas v. United States | Stevens | Signed ripeness threshold disposition; explicit count treatment is uncounted. |
| Campbell v. Louisiana | Breyer | Standing is adjudicated, not the discrimination merits; its recorded threshold character excludes the signed opinion. |
| Ohio Forestry Association v. Sierra Club | Scalia | Pure ripeness threshold action; its assignment expressly denies plenary-merits lead credit. |
| Stewart v. Martinez-Villareal | Souter | Threshold classification returns an unadjudicated claim for consideration; no signed lead-merits credit. |
| Textron Lycoming v. United Automobile Workers | Thomas | Jurisdictional disposition before contract merits; its assignment denies lead-merits credit. |
| Calderon v. Ashmus | Stone-Zsela | Article III threshold decision; its classification leaves the author's count unchanged. |
| Forney v. Apfel | Scalia | Signed appellate-jurisdiction threshold opinion; its form statement excludes it despite a precedential jurisdictional rule. |
| Hohn v. United States | Ginsburg | Jurisdiction/certificate-remand threshold disposition, not collateral merits; its form statement excludes every writing from counted credit. |
| Wisconsin Department of Corrections v. Schacht | Thomas | Signed jurisdictional threshold decision; its assignment expressly adds no counted credit. |

Aktepe's `merits` filename does not override its event and express form. Including it would incorrectly raise Kennedy from 11 to 12 and the pre-June 25 total from 106 to 107. Some later Records report that inflated baseline; those prior tallies do not control this prospective recount, and their adjudications and assignments are left intact.

## Other exclusions and authorship checks

The remaining sixteen exclusions are Brown, Arteaga and Glendora filing orders; City of Monroe, Newsweek, Hetzel's summary disposition and New Mexico ex rel. Ortiz summary actions; Hetzel's separate certiorari grant; Caterpillar and Lewis v. Brunswick dismissals; Rogers's dismissal as improvidently granted; Triestman and Dorsainvil per curiam jurisdictional dismissals; the two Breard application Records; and the PLRA admitted source Record. Rogers's signed lead and the Breard signed explanations remain excluded because their own actions are procedural/applications, not counted plenary merits decisions. Separate writings supply no credits.

Multipart leads, including Jeffries, Hudson, City of Chicago, Joiner, Clanton, Valot, Fields, W.P., Almendarez-Torres, Woodard, Bird, Ricci, Waste Management, Zeran and Gebser, were checked for different delivering authors rather than counted once per table row. Their relevant lead portions have one delivering Justice per decision. No missed additional credit was found.

No Git command was executed. No top-level `stone/` path was accessed, listed, or searched. Writes were confined to `tmp/` and this authorized `terms/OT1997/freeze/` memorandum. This is an assignment-count verification, not a representation of Git commitment or full-term substantive audit.
