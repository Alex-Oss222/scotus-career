# October Term 2000 - Confirming Close Re-audit

Audit date: November 9, 2026.
Repair reviewed: `60c7186b`.

**Disposition:** F1-F3 are resolved. Two discrepancies remain: F4 (Medium, incomplete statement of Children's Healthcare's operative statutory qualifications) and F5 (Low, a malformed possessive in the Standards candidate). The term is not ready for Close Commit.

## Scope and method

The review covers 114 completed events through June 28, 2001, eight chunks, the final workspace, frozen and generated handoffs, public renders, and the three staged tracker candidates. Records control over projections. Locations below are repository-relative and use one-based line numbers in the current files.

The saved prior audit deferred its legal-substance stage. After the deterministic checks passed, this re-audit performed a fresh substantive review across all 114 events, with deeper examination of material fractures, changed premises, Justice-specific departures, remedies and candidate incorporation. Existing source materials and earlier governing decisions were used; this report does not claim independent reacquisition of every historical archive document or rereading of every duplicated annex. The Children's Healthcare statutory terms were also checked against the official enactment.

Only this audit is changed. Git use was limited to the expressly permitted term checker and read-only `git cat-file` lookups. The repair commit and its parent resolve; inspection of their OT2000 trees identifies exactly four changed files, and each current repaired file matches its repair-commit blob. Full repository commitment-order reconstruction remains reserved to the operator, as the ledger discloses. No prohibited directory or filename was accessed.

The standing directions govern this review: absent GitHub repository URLs are intentional; unresolved relative navigation inside preserved `freeze/` and `entering-law/` copies is exempt; corrections must remain seamless, without correction-specific version, lineage, receipt or narrative in Records or public copies. Their absence is required and is not a defect.

## Verification of prior findings

| Finding | Result and current locations |
|---|---|
| F1 - Oakland participation | Resolved. Breyer's nonparticipation is now included at `workspace/manifest.md:147`, `workspace/continuity.md:5804,5823`, and `workspace/neutral-projection.md:4599,4643`. These agree with the Oakland Record at lines 8, 18 and 116 and its eight-person judgment. Existing Hatter, New Hampshire and Pollard exceptions remain; no reason for absence is invented. |
| F2 - Kansas carryover | Resolved. Kansas appears at `workspace/manifest.md:3,137-142`, `workspace/continuity.md:9,5798,5960`, and `workspace/neutral-projection.md:9,4636,5881`. The June 11 decision on exceptions is complete, while damages calculation and preparation of judgment remain before the Special Master. The summaries retain Arizona/Fort Yuma, zero uncompleted scheduled inventory events, and Fiore's distinct lower-court habeas work. `close/STANDING_STATE.candidate.md:61` already carries Kansas correctly. |
| F3 - Kansas navigation | Resolved. All four hrefs at `records/Kansas_v_Colorado_merits_2001-06-11.md:227` now begin with `../freeze/` and resolve to their intended files. The Record's substantive text and Public Projection are unchanged. |

The repair comparison shows only those participation, carryover and navigation edits. All four repaired files retain their CRLF endings. Oakland's public copies already disclose Breyer's absence, and Kansas's public copies already preserve the pending original action; the workspace repairs introduce no new Court action or adjudicative premise.

## Deterministic results

- **Term checker:** `python tools/check_term.py OT2000` passes. Its two warnings are false commit-reference matches: the Library of Congress source identifier at `records/Alabama_v_Bozeman_merits_2001-06-11.md:188`, and the Third Circuit amendment filename at `records/Sterling_v_Borough_of_Minersville_merits_2001-04-24.md:247`. Neither is a Git reference. Actual referenced commit lookups produce no remaining missing-object finding.
- **Inventory and effective order:** All 114 inventory events reconcile to 114 unique Records, manifest completions and ledger entries. Record identities, dates, results and ledger fields agree. The eight chunk totals are 12, 15, 14, 15, 14, 15, 14 and 15. The inventory's organizational date annotations were handled explicitly rather than relying on the stock checker's incomplete recognition of that table format. Render coverage, closing boundaries and effective-date order agree. Uncoordinated same-date events retain their common entering-law baseline.
- **Freshness and public identity:** Runtime splits pass the checker's freshness checks. All eight commitment pairs and eight reconciliation pairs match their frozen counterparts byte-for-byte. Every generated Render Input event matches its Record's bounded Public Projection. Fresh digest checks also pass for all 45 chunk-2 handoffs, 17 chunk-3 index entries, 15 chunk-8 Records in both final receipts, and 30 selected chunk-8 handoffs.
- **Participation, votes and assignments:** Compact and component judgment counts reconcile with the named coalitions, including Bush's three-way division and the complex Hicks and Lorillard tables. Public disclosure limits remain intact. The opinion-table census reproduces 103 counted signed plenary lead opinions and 11 excluded events: Stone-Zsela 10, Stevens 12, O'Connor 12, Scalia 11, Kennedy 11, Souter 12, Thomas 12, Ginsburg 11 and Breyer 12. These totals do not substitute for proposition-level eligibility or reconstruct historical commitment order.
- **Navigation and presentation:** The local scan checks 1,889 href occurrences across 164 Markdown files; all tested local paths and anchors resolve. Candidate navigation is resolved at its intended publication destination, substituting the staged Holdings candidate where appropriate. The 1,099 external links are distinguished from local references; their availability was not comprehensively retested. No reference-definition or HTML-href gap was found. All 235 labeled controlling explanations in each of the Record Public Projection, Render Input and public-output layers satisfy the ordinary 350-word ceiling.
- **Candidates and carry-forward:** The three common publication fields agree and deliberately retain the opening values pending coordinated advancement at Commit. All 2,740 opening Holding fields remain intact. The Standards candidate has 940 unique entries, accounts for all 114 Records, and its recorded digest matches. Its 109 additions or replacements have the required core fields; the other 831 entries retain their substance, with three documented title-reference updates. No component cites a candidate document as its substantive authority. The Standing State candidate preserves the nine-seat OT2001 roster, thirteen circuit allotments, unchanged referral practice and the Arizona and Kansas carryovers. Candidates and pass notes properly remain until successful Commit.

## Legal-substance results

Fresh review covered the controlling rules, proposition-level coalitions, qualifications, judgments and remedies of all 114 events, together with their historical-departure explanations and public projections. Targeted checks examined internal Justice matrices, frozen support and actual prior governing holdings where a changed premise or difficult coalition required them.

The principal fractures remain accurately bounded. Bush's judgment positions are distinct from issue majorities; Green Tree supplies no invented complete proof-allocation rule; Coss and Saucier supply no synthesized general rationale; Atwater's rule coalition remains distinct from its application division; Kansas's exact interest cutoff remains distinct from its controlling compensation and period propositions. Garrett's independent grounds, Whitman's partial joins, Mead's rule/remand distinction, Lorillard's component-specific grounds and Zadvydas's implementation coalition are preserved. Justice-specific departure support was checked against relevant earlier holdings and published positions, including the criminal-review, sovereign-immunity, religious-function, thermal-search, immigration and property-law sequences.

The Oakland repair preserves its distributor-specific statutory and equitable grounds, eight participating Justices, lawful enforcement discretion and patient-specific reservations. The Kansas repair preserves the completed exceptions decision, its fractured cutoff, recommittal and pending original action. The three candidates preserve the reviewed controlling authority, earlier holdings' surviving force and material remedial boundaries. Apart from F4's incomplete statement of retained statutory conditions and F5's typographical defect, this review identifies no additional legal-substance or projection discrepancy.

## Remaining unresolved discrepancies

### F4 - Medium - Children's Healthcare omits operative institutional-eligibility limits

**Files and lines:**

| File | Line(s) |
|---|---|
| `terms/OT2000/records/Childrens_Healthcare_Is_a_Legal_Duty_v_Min_De_Parle_merits_2001-04-23.md` | 128, 297 |
| `terms/OT2000/render-inputs/OT_2000CHUNK4.md` | 1137 |
| `terms/OT2000/output/OT_2000CHUNK4.md` | 1130 |
| `terms/OT2000/workspace/continuity.md` | 2041 |
| `terms/OT2000/workspace/neutral-projection.md` | 1902 |
| `terms/OT2000/close/HOLDINGS.candidate.md` | 36606 |
| `terms/OT2000/close/STANDARDS_AND_TESTS.candidate.md` | 8690 |

**Discrepancy:** The Record makes the institutional restrictions part of the conditions limiting its constitutional permission, but refers to defined physical care and religious-service, medical-provider ownership and affiliation restrictions without stating the underlying requirements. It then states exceptions to the omitted ownership and affiliation prohibitions. The omission propagates through the public copies, workspace and Holdings candidate. The Standards candidate conditions permission on independent statutory eligibility and disclaims a complete eligibility code; that preserves its limited ambition but does not state the material qualifications it expressly retains. The issue was identified at `close/STANDARDS_AND_TESTS_PASS.md:23,104` and remained for this audit.

The governing completeness rule requires operative qualifications in their own terms. These terms are available in `runtime/OT_2000CHUNK4_CHILD_STATUTE.md:48-72` and [Public Law 105-33, section 4454, 111 Stat. 427-428](https://www.govinfo.gov/content/pkg/PLAW-105publ33/html/PLAW-105publ33.htm), adding Social Security Act section 1861(ss)(1)(C), (F) and (G). This is a completeness defect in the retained legal limits; it establishes no actual institutional noncompliance.

**Exact fix:** In an authorized repair, state the omitted requirements in the Record's controlling conditions and Public Projection:

1. The institution supplies only nonmedical nursing items and services to patients choosing sole reliance on religious healing, for whom medical health services conflict with their beliefs.
2. Because of its religious beliefs, it provides no medical items or services to its patients through its personnel or otherwise, including screening, examination, diagnosis, prognosis, treatment and drug administration.
3. It cannot be owned by, share common ownership with, or hold an ownership interest in a medical-treatment/services provider; separately, it cannot be affiliated with such a provider or an individual owning an interest in one.

Preserve the existing statutory qualifications at their separate scopes: interests below five percent are disregarded for the ownership rule; the affiliation exceptions cover uncompensated governing-body service, the specified institutional personnel's family relationships, and vendors serving both provider types. Retain the separate election exceptions for involuntary or legally required treatment, the existing care and review requirements, and the absence of any individual entitlement or compliance finding.

Propagate the completed terms to the listed workspace and candidate locations; regenerate the affected Render Input from the Record and replace only this event's public entry, preserving the other entries. Keep the correction seamless and preserve line endings. Update the Standards pass note's limitation and coverage statements after repair and refresh its candidate digest. No change to the adjudicated votes, joins, constitutional grounds or remedy is supported or required by this finding.

### F5 - Low - Malformed possessive in the Rogers standard

**File and line:** `terms/OT2000/close/STANDARDS_AND_TESTS.candidate.md:7133`.

**Discrepancy:** The current rule contains the literal ASCII text `law?s` in its statement of the law's reasonably apparent reach. This is present in the file bytes, not a display-encoding artifact. It occurs once across the checked Records, public copies, workspace and close files; the candidate scan finds no additional word-internal question mark or replacement-character defect.

**Exact fix:** Replace only `law?s` with `law's`, preserving CRLF and the surrounding rule. Refresh the candidate digest in `close/STANDARDS_AND_TESTS_PASS.md` after the authorized candidate repairs. No doctrine, authority or effective date changes.

No tracker publication or candidate cleanup has been performed. F4 and F5 must be repaired and confirmed before Close Commit.

READY FOR CLOSE COMMIT: NO
