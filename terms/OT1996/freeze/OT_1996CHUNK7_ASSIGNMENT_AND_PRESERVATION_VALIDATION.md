# OT1996 chunk 7 — assignment and preservation validation

**Result:** Pass for all eleven completed Court Records. No unresolved assignment or preservation discrepancy was found within this audit scope. Matter 74 remains stopped; it has no Record, assignment or lead-opinion credit.

This audit applies Engine §8 and the relevant AGENTS Run and Record rules. It independently reads the actual public opinion tables or prose, examines each current assignment statement and its partial-join boundaries, and tests the necessary same-case frozen and approved scope. It neither changes adjudications nor repeats the underlying merits research.

## Independent recount

The original helper was inspected but was not imported or executed by the independent recount. Every original receipt matches on the ordered prior Record list, case/date ordering key, delivering author, exact topology SHA-256, all nine counts, total and last counted event. Every reviewed counted Record contains one signed plenary lead; repeated part or partial-join rows receive no extra credit. Later-event exclusion lists were deliberately not required to match, because those Records did not necessarily exist at the original assignment.

LAVAS and Lynce count as signed decisions after plenary argument despite their threshold/remand outcomes. Signed summary Roy, the other summary or per curiam dispositions, procedural actions, separate writings, and all admitted statutory sources—including the newly admitted Minnesota chapter 419—do not count. Brown (matter 74) has no completed event to count. Existing assignments remain untouched.

A final-stage check briefly observed a Johnson topology hash differing only because assembly cleanup temporarily serialized the same text with LF rather than its original CRLF line endings. The author row, joins and substantive text were identical. Assembly restored the original serialization; an independent raw-byte reread and the final complete retally match the untouched original receipt exactly. The companion JSON preserves both diagnostic hashes. No original receipt or assignment was rewritten.

| Matter | Prior leads | Stone | Stevens | O'Connor | Scalia | Kennedy | Souter | Thomas | Ginsburg | Breyer | Last counted |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 73 | 59 | 6 | 7 | 9 | 6 | 6 | 8 | 5 | 6 | 6 | Blessing_v_Freestone_merits_1997-04-21.md |
| 72 | 60 | 6 | 7 | 9 | 6 | 6 | 8 | 5 | 7 | 6 | Kadic_and_Doe_v_Karadzic_merits_1997-04-21.md |
| 75 | 62 | 6 | 7 | 9 | 6 | 6 | 8 | 7 | 7 | 6 | New_Mexico_Department_of_Human_Services_v_Joseph_A_merits_1997-04-21.md |
| 76 | 63 | 6 | 7 | 9 | 6 | 7 | 8 | 7 | 7 | 6 | Pic_A_State_Pennsylvania_v_Reno_merits_1997-04-28.md |
| 77 | 64 | 6 | 7 | 9 | 6 | 7 | 8 | 7 | 7 | 7 | Richards_v_Wisconsin_merits_1997-04-28.md |
| 78 | 65 | 6 | 7 | 9 | 7 | 7 | 8 | 7 | 7 | 7 | Strate_v_A_1_Contractors_merits_1997-04-28.md |
| 79 | 66 | 6 | 7 | 9 | 7 | 7 | 8 | 8 | 7 | 7 | Timmons_v_Twin_Cities_Area_New_Party_merits_1997-04-28.md |
| 80 | 67 | 6 | 7 | 9 | 7 | 8 | 8 | 8 | 7 | 7 | Doe_v_SEPTA_merits_1997-05-05.md |
| 81 | 68 | 6 | 7 | 9 | 7 | 8 | 9 | 8 | 7 | 7 | Harbor_Tug_and_Barge_v_Papai_merits_1997-05-12.md |
| 82 | 69 | 6 | 7 | 9 | 7 | 8 | 9 | 8 | 8 | 7 | Inter_Modal_Rail_Employees_v_Atchison_merits_1997-05-12.md |
| 83 | 70 | 7 | 7 | 9 | 7 | 8 | 9 | 8 | 8 | 7 | Johnson_v_United_States_merits_1997-05-12.md |

## Eligibility, assignment authority and author

Whole-opinion eligibility below requires a full join to every governing proposition. Disposition-only agreement and partial joins do not qualify. The Chief’s rule governs a coordinated opinion when he assigns an actual judgment component; pure Associate assignments remain outside its mandatory pool.

| Matter | Assignor basis | Eligible whole-opinion authors | Binding pool | Chosen author |
|---|---|---|---|---|
| 73 | Chief, all judgment components | Stevens, O'Connor, Kennedy, Souter, Ginsburg, Breyer | Stevens, Kennedy, Ginsburg, Breyer | Ginsburg |
| 72 | Stevens, reversal; Chief, discovery disposition | Stevens, O'Connor, Kennedy, Souter, Thomas | Kennedy, Thomas | Thomas |
| 75 | Chief | Stone-Zsela, Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | Stone-Zsela, Stevens, Scalia, Kennedy, Thomas, Ginsburg, Breyer | Kennedy |
| 76 | Chief | Stevens, O'Connor, Kennedy, Souter, Thomas, Ginsburg, Breyer | Stevens, Kennedy, Thomas, Ginsburg, Breyer | Breyer |
| 77 | Chief, jurisdiction; Stevens, remedial reservation | Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | Scalia, Stevens, Kennedy, Thomas, Ginsburg, Breyer | Scalia |
| 78 | Chief, live controversy; O'Connor, reversal | O'Connor, Scalia, Kennedy, Thomas, Breyer | Scalia, Kennedy, Thomas, Breyer | Thomas |
| 79 | O'Connor alone | O'Connor, Scalia, Kennedy, Thomas, Breyer | Inapplicable: Associate assignment | Kennedy |
| 80 | Chief, both genuine judgment components | O'Connor, Scalia, Kennedy, Souter, Thomas | Scalia, Kennedy, Souter, Thomas | Souter |
| 81 | Stevens alone | Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, Breyer | Inapplicable: Associate assignment | Ginsburg |
| 82 | Chief | Stone-Zsela, Stevens, O'Connor, Kennedy, Souter, Thomas, Ginsburg, Breyer | Stone-Zsela, Stevens, Breyer | Stone-Zsela |
| 83 | Chief, common vacatur/default-first remand; Stevens, reaching Teague and additional binding old-rule direction | Stevens, Souter, Ginsburg, Breyer | Stevens, Ginsburg, Breyer | Stevens |

- **73 — Kadic / Doe v. Karadzic:** Stone disposition-only on particular service and supplemental-claim grounds; Scalia and Thomas reject the two additional actions. Ginsburg carries the whole opinion; partial-join rows count only once.
- **72 — Metropolitan Life v. Robertson-Ceco:** Stone seeks vacatur rather than reversal and supplies no discovery rationale; Scalia withholds independent-fairness Part III-A; Ginsburg and Breyer reject sufficient contacts. Frozen discovery adjudication supports the Chief component. Thomas also lies within the discovery-only pool.
- **75 — Pic-A-State v. Reno:** Every Justice joins all three holdings and qualifications; all nine are eligible, including Stone.
- **76 — Richards v. Wisconsin:** Scalia and Stone withhold Part III appellate method; judgment agreement does not supply full-opinion eligibility.
- **77 — Strate v. A-1 Contractors:** Stone lacks Part II general-ceiling ground and opposes Part V relief. The Chief assigns part, so the whole coordinated opinion is subject to balance.
- **78 — Timmons v. Twin Cities Area New Party:** The admitted conditional enactment presents a genuine threshold component independently frozen before assembly. Stone reaches the merits but supplies no enactment-specific rationale and opposes reversal; the Chief does not assign the merits.
- **79 — Doe v. SEPTA:** The sole merits ground assumes the asserted right. Scalia and Thomas fully join that assumption-based opinion despite their separate source objection. There is no separate disputed threshold judgment component. The listed pool is comparative only; the Chief's binding balance rule does not govern this Associate assignment.
- **80 — Harbor Tug & Barge v. Papai:** Stone fully joins fleet/status Parts I-II but only the Part III independent-appeal disposition through fallback; the three dissenters join only Part III. The five Associates who join all Parts can carry the whole opinion. Souter is one above the eligible minimum.
- **81 — Inter-Modal Rail Employees v. Atchison:** There is one reviewed disposition. Stone joins the coverage rule but seeks formal reversal instead of the eight Associates' vacatur. A proposition join creates no additional judgment component or Chief assignment. The mandatory Chief pool is expressly inapplicable.
- **82 — Johnson v. United States:** Scalia withholds Parts II-III in the frozen reconciled commitment and actual topology. Stone's approved supplement supports every governing proposition. His self-assignment compares Stevens and Breyer and identifies precise coordination of his new appellate-plainness proposal with an assumed injury and independent fourth-step refusal. He is the sole lowest-count member, not the sole pool member; this is a supported fit choice, not a compulsory self-assignment or an ability exclusion.
- **83 — Lambrix v. Singletary:** Approved Stone and the five audited old-rule supporters share removal of the same appellate disposition and default first on remand. The binding prohibition on renewed Teague denial has additional operative force supported by five only. Stone supplies no old-rule join. Preserve six-vote common relief separately from the five-vote binding instruction; this is an actual division in remand instructions rather than an extra component created from a shared rationale. O'Connor withholds Part I, and the three new-rule affirmers reject the vacatur/old-rule mandate. The final Record preserves I (seven), II/III-B (five), and III-A (six), with Stevens delivering one coordinated lead. Stevens is in the minimum-count pool and the statement compares Breyer and Ginsburg on the precise guidance, allocation and separate-remedy work; Souter is fully eligible but outside the pool.

The form-first statements were checked against the resulting single lead, genuine judgment components and separate writings. Each chosen author is eligible; each Chief-governed author falls within the actual minimum-plus-one pool. The stated fit choices address the case’s work and compare supported alternatives without treating ability, historical authorship or mere disposition agreement as eligibility. No artificial author division or new component was needed to meet a count.

## Preservation

An independent SHA-256 comparison verified all **1469** named pre-existing term files in the supplied baseline and all **7** named governing/state files. No file was missing or changed. The eleven original assignment receipts also retain their first-observed hashes throughout this audit. The companion JSON records the exact named scope, hashes, counts and per-case evidence.

The term baseline intentionally excludes case-insensitive chunk7 paths and the four mutable workspace projections. It therefore does **not** establish an initial hash for the approved chunk 7 brief. This result proves preservation only for the named baseline files; runtime-split freshness, projection/Render Input identity and the full term check are separate root validations. Current new-Record and topology hashes are recorded as audit evidence, not as proof of a pre-Run baseline.

No Git command or Git metadata access was used. Commit-hash existence and repository commitment were not verified or claimed. The restricted top-level private directory was neither read nor traversed. This auditor wrote only the durable validation files in `terms/OT1996/freeze/` and scratch evidence/scripts under `tmp/`.

## Limits and remaining workflow

No unresolved assignment or preservation discrepancy remains in this scope. The existing matter-74 assembly stop remains open: its multiway disposition split supplies no judgment majority, and no stopped-matter opinion was assigned. This audit is not a representation that the entire chunk has a completed disposition for every inventory item, nor is it a general merits or provenance audit.

[Machine-readable evidence](OT_1996CHUNK7_ASSIGNMENT_AND_PRESERVATION_VALIDATION.json).
