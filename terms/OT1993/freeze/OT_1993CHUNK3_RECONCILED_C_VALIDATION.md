# OT1993 chunk 3 — reconciliation C source validation

## Completed read and source checks

The reconciliation context read the full extracted text of each downloaded official United States Reports PDF, including syllabus, opinion bodies, every separate writing, and footnotes. Truncated tool displays were followed by bounded reads covering the omitted pages. These are complete text reads of the reports, not headnote-only or partial-PDF reads. The existing downloaded PDFs themselves were not independently redownloaded or visually inspected in this stage. Primary report locations are:

| Matter | Official source | Complete pages read | Verified identity and topology |
|---|---|---|---|
| Ticor | https://tile.loc.gov/storage-services/service/ll/usrep/usrep511/usrep511117/usrep511117.pdf | 117–126; 10 PDF page markers; 20,115 text characters | No. 92-1988; March 1 argument; April 4, 1994 disposition; per curiam DIG; O'Connor dissent joined by Rehnquist and Kennedy; six-to-three threshold division. |
| J.E.B. | https://tile.loc.gov/storage-services/service/ll/usrep/usrep511/usrep511127/usrep511127.pdf | 127–163; 37 markers; 84,608 characters | No. 92-1239; November 2, 1993 argument; April 19, 1994 decision; Blackmun with Stevens, O'Connor, Souter, Ginsburg; O'Connor concurrence; Kennedy judgment concurrence; Rehnquist dissent; Scalia dissent with Rehnquist and Thomas; six-to-three reversal/remand. |
| Central Bank | https://tile.loc.gov/storage-services/service/ll/usrep/usrep511/usrep511164/usrep511164.pdf | 164–201; 38 markers; 86,108 characters | No. 92-854; November 30, 1993 argument; April 19, 1994 decision; Kennedy with Rehnquist, O'Connor, Scalia, Thomas; Stevens dissent with Blackmun, Souter, Ginsburg; five-to-four reversal. |
| McDermott | https://tile.loc.gov/storage-services/service/ll/usrep/usrep511/usrep511202/usrep511202.pdf | 202–221; 20 markers; 47,768 characters | No. 92-1479; January 11 argument; April 20, 1994 decision; Stevens for unanimous historical Court; no separate writing; reversal/remand. |

The page counts and character lengths were checked computationally against the preserved text files, not treated as proof of the legal conclusions. All dates and historical opinion joins above were checked against the report headers and writing headings. Every roster includes the eight sitting associates plus the relevant Chief; Breyer is absent. Rehnquist's historical vote is not imported as Stone's vote.

Lower-court complete-read verification is inherited from `OT_1993CHUNK3_NEUTRAL_C_VALIDATION.md`; the reconciliation context did not independently repeat those complete lower-opinion reads. Their saved source texts remain in `chunk3-neutral-c-sources/`. Their exact factual and remedial qualifications are preserved in the reconciliation. Original merits briefs, oral-argument transcripts, trial exhibits, and later settlement-approval orders were not recovered by this stage; no claim of exhaustive original-record review is made.

## Source-to-issue receipt

- Ticor pp.118–121 verify the final certification premise, settlement and claims, question, and court below. Pages 121–122 state the historical vehicle reasoning, and pp.122–126 the opposing retention rationale. Page 122 adds the objective party-reported proposed settlement awaiting District Court approval. That neutral fact was isolated in `OT_1993CHUNK3_TICOR_NEUTRAL_REFRESH.md`; it triggers clean refresh rather than an outcome-informed commitment patch. No completed mootness is inferred. Kennedy's historical retention differs from the original frozen DIG and remains pending reconciliation after refresh.
- J.E.B. pp.129–130 confirm the already supplied record; pp.135–146 state the historical heightened-scrutiny rule, nonquota limits, neutral-reason/pretext distinction and procedural inquiry. Pages 146–151 confirm O'Connor's governmental-strike limit and practical/private-actor reservations; pp.151–154 establish Kennedy's individual-right and impartial-juror rationale without a full majority-opinion join. Pages 154–163 contain the two dissents. Historical harmless-error comments are not converted into a separate modeled holding or a finding about the proper inquiry on remand.
- Central Bank pp.167–170 confirm secondary-claim posture and competing evidence; pp.170–191 contain the text, structure, criminal-statute, historical-interpretation and policy arguments; pp.191–192 preserve potential primary liability while reversing the secondary claim. Pages 192–201 establish the four dissenters' retention position, but do not adjudicate their ultimate view of recklessness or the lower judgment after that issue. Their modeled conditional scienter/affirmance commitments are therefore identified as independent modeling, never historical votes. The newly observed p.191 oral-argument concession is not adopted as an added neutral premise. Historical Mertens discussion at pp.175,184 is checked against the actual opening Mertens holding and may not enlarge its expressly reserved cause-of-action question.
- McDermott pp.204–207 verify claims, damages, settlement, relief and lower result; pp.207–217 compare three credit methods; pp.218–221 preserve the one-satisfaction and Edmonds limits and reversal/remand. Footnotes 10–12 preserve AmClyde's unreviewed contract ruling, requested River Don share, and nondecision of whether the lower court correctly applied its rejected dollar-credit method. The original lower-court evidentiary remand limit remains in force. No division of the combined 30% is invented. References to relative fault do not disapprove the lower court's use of relative causation (p.216 n.25).

Actual entering-law sources reviewed include the selected Musick, Peeler holding and standard, McCollum standard, actual NOW and Meyer public projections, relevant sanitized Izumi/James Daniel Good/Harris/John Hancock continuity, and the opening Mertens holding. Historical source quotations are comparison material only. The actual Mertens remedial holding remains narrower than the comparator's characterization; no vote change follows because the original frozen grounds do not rely on that characterization.

## File identity and deterministic checks

Original freeze and runtime commitments remain byte-identical, with SHA-256 `411B7603A84F041BA4C92E95EE2B3DEB25DFEE48287FAC8BD03935830AE83C83`. They were read and never edited. Freeze and runtime `OT_1993CHUNK3_RECONCILED_C.md` are byte-identical, SHA-256 `006CBA7ADB5AACE4A3FEB34E133274818952553AF0F879A838C87EDE9B7A209E`.

Source text hashes, in `freeze/chunk3-sources/`:

| File | SHA-256 |
|---|---|
| Ticor-511117.txt | 13049A162AD84D80DEE29EC6B26DCE2E003E7AFD4FF9EF1972743AECDE2F875E |
| JEB-511127.txt | 9C129B7C460DBC4CD2861CD4C98DBA7EF755A3028ADA31F6EDC77CB600620269 |
| CentralBank-511164.txt | D2CEDA887E567E5D6FA71E1821469F5940AD8965F307DFFFA4D87B3F4B8473BC |
| McDermott-511202.txt | B0EF93A859127CA72C86BDAAF4729B178339738019DC273C9E64AACD504A00DA |

The three completed reconciliation tables each contain all eight non-Stone Justices exactly once. Arithmetic independently checked: 32+38+30=100; $2.1 million × .38=$798,000; × .32=$672,000; $2.1 million × .70−$1 million=$470,000; settlement plus River Don share=$1,798,000. The result is not treated as an unconditional payment mandate.

Non-Stone counts are six/two in J.E.B., four/four on Central Bank's existence question, and eight on McDermott. J.E.B. judgment agreement is not equated with all six joining an entire opinion. Central Bank's four/four split omits the unmodeled ninth Justice and is not a Court equal division. Ticor's original seven/one threshold split is preserved as original provisional data only and is not declared reconciled.

## Definitive status and remaining blocker

J.E.B., Central Bank, and McDermott are ready for assembly within the frozen limits. Ticor awaits clean neutral validation and a separate frozen commitment delta for the proposed-settlement fact, followed by final reconciliation, including Kennedy's threshold position. This is the only unresolved blocker in this group.

No Stone materials were opened; no final author or assignment was chosen; no Court record or law was created. All writes were within `terms/OT1993/`. No Git command or Python process was run. Git durability, final compatibility and assignment, canonical records, Public Projections, render-input identity, workspace updates, and `check_term.py` remain the operator's later work; none is represented as completed here.
