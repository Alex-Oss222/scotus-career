# October Term 1997 — Confirming Close Audit

Audit date: October 26, 2026. Repair commit examined: `f57cd16b`.

F-01 through F-08 are resolved. One Low discrepancy remains, F-09: two current workspace inventory summaries retain outdated classification counts. The term is not ready for Close Commit until those existing paragraphs are corrected. The prior legal-substance audit remains clean; targeted review of every affected substantive part found no adjudication requiring correction.

Paths below are relative to `terms/OT1997/` unless stated otherwise. Line numbers identify the current audited files.

## Scope and method

This is a confirming re-audit of the previous audit and the operator's repairs, applying the Close protocol, Engine, Render Contract, tracker instructions, Court Composition and the user's standing close rulings. Records control over all projections. The previous audit's complete legal review covered 162 Court-action Records and the admitted statutory source; this re-audit reran the deterministic checks and independently reviewed the parts affected by the repair.

Read-only `git cat-file` comparisons identified 38 repaired files within the relevant term, tracker and governing-file scope. All 1,854 scoped working files matched their blobs at `f57cd16b` before this audit was replaced. The 23 repaired Records changed only internal assignment counts, pools, comparative explanations and associated totals. Each bounded Public Projection remained byte-identical across the repair. All other Records, all 13 Render Inputs and all 13 renders were unchanged. This establishes the boundary of the confirming legal review without claiming that a second complete merits review of every unchanged decision was performed.

The required checker was run before the remaining deterministic review and again after this report was written. Only the permitted checker and read-only `git cat-file` commands were used. No prohibited directory or file was accessed. The only repository file changed by this audit is `close/AUDIT.md`; ignored `tmp/` was used for scratch. The audit's CRLF line endings and UTF-8 encoding without a byte-order mark were preserved.

## Verification of the repairs

| Finding | Verification | Status |
|---|---|---|
| F-01 — inventory classification and totals | `case-list.md:9` and the complete manifest reconcile to 160 scheduled items: 151 MERITS, one ORIGINAL, four APPLICATION and four DISMISSAL. Ricci remains correctly classified as MERITS at `case-list.md:116` and `workspace/manifest.md:98`. The separate stale workspace summaries are F-09 below. | Resolved at the identified index and manifest locations |
| F-02 — W.P. reviewed docket | `case-list.md:85` and `workspace/manifest.md:73` identify Third Circuit No. 96-5416, preserve the exclusion of E.B., No. 96-5132, and agree with the controlling Record. | Resolved |
| F-03 — five designated artifact digests | All 34 recorded digest occurrences associated with the five designated files match their current bytes: `entering-law/OT_1997CHUNK1_REVALIDATED.md`, `entering-law/OT_1997CHUNK1_B.md`, `entering-law/OT_1997CHUNK1_RYBAR_EFFECTIVE.md`, `freeze/OT_1997CHUNK1_COMMITMENTS_RYBAR.md` and `freeze/OT_1997CHUNK1_COMMITMENTS_B.md`. Matching digests resolve F-03 under the standing ruling. | Resolved |
| F-04 — inherited navigation | Applied the express exemption for source navigation preserved inside `freeze/` and `entering-law/`. Working navigation was separately checked in Records, Render Inputs, renders, workspace and trackers. No link-resolution file is required or created. | Resolved |
| F-05 — two corrupted characters | `close/STANDARDS_AND_TESTS.candidate.md:6966` now contains the proper possessive in the habitat-rule title; line 11098 now identifies §107(a)(2). The surrounding rules and qualifications are unchanged and agree with the controlling NAHB and Bestfoods Records. | Resolved |
| F-06 — Aktepe assignment accounting | Aktepe is excluded as a threshold opinion. All four census artifacts, 23 Record counts, 11 omitted Kennedy pool memberships, three comparative-count explanations and dependent aggregate/digest references were verified. Detailed results appear below. | Resolved |
| F-07 — U.S. Shoe exclusions | `close/HOLDINGS.candidate.md:10693` and `close/STANDARDS_AND_TESTS.candidate.md:1957` now supply the operative predicates of the §1581(i) antidumping/countervailing exclusion and distinguish §1581(j)'s Tariff Act §305 exclusion. They match the controlling Record and preserve the protest-channel limitation. | Resolved |
| F-08 — final global scope and continuation cursor | `workspace/continuity.md:15370`, `:15372`, `:15374` and `workspace/neutral-projection.md:15582`, `:15584`, `:15586` now cover 162 Court actions through all 13 chunks, retain the admitted source separately, give September 28, 1998 as the final covered Court event, and identify all 160 scheduled items as completed with no unprocessed chunk. Pending stages and source limitations remain intact. | Resolved |

The deliberate absence of GitHub repository URLs from published trackers is not a defect. No finding requires adding a repository file.

### F-06 verification detail

The chunk-8 baseline and current censuses independently recompute to 68 and 76 counted authorship credits, respectively, with Kennedy at seven and eight. The chunk-11 census contains 124 Records and 98 counted credits, with Kennedy at eleven. Every before/after count transition in its JSON reconciles, and its copied opinion tables match the current Records. Aktepe's existing uncounted classification is preserved.

The corrected preassignment Kennedy counts were checked in every affected Record:

| Record group | Verified Kennedy count | Record coverage |
|---|---:|---|
| Early chunk 8 | 7 | Benjamin; Bronx Household; Rice |
| Remaining affected chunk 8 | 8 | Forbes; Bousley; Montana; Ohio Forestry; Stewart; Textron; Gavin; Thompson |
| Affected chunk 11 | 11 | Forney; Hohn; Yeskey; Phillips; Zeran; Caron; Gebser; Pearson; Scott; Bajakajian; Schacht; Swidler |

All eleven required Kennedy pool additions are present: Forbes, Montana, Ohio Forestry, Textron, Gavin, Thompson, Forney, Hohn, Yeskey, Phillips and Caron. The three comparisons in Benjamin, Bronx Household and Rice now use the corrected equal counts. The additional NAHB and runtime chunk-9 tallies reconcile. All 103 modified digest occurrences in the seven dependent artifacts match their referenced current targets; unchanged hashes of bounded earlier workspace snapshots were evaluated as those snapshots.

The corrected pools retain the same minima and every selected author. Targeted legal review tested the assignment explanations against Engine §8 and the relevant frozen commitments and reconciliations, including the newly available Kennedy alternatives. Each assignment retains a concrete case-specific fit. Partial joins, judgment-only fallback, Associate-Justice assignment authority in Bronx Household and Zeran, and Gebser's complete-lead eligibility remain correctly distinguished. No authorship, coalition, holding or remedy change is required.

## Deterministic checks

| Check | Result |
|---|---|
| Required term checker | `python tools/check_term.py OT1997` passes, exit 0, with 16 warnings. Each warning is a source identifier or text fragment caught by the commit heuristic, not a missing recorded commit. |
| Opening Holdings synchronization | `python tools/holdings_volumes.py check` passes. Doctrinal volumes and the continuous compatibility view are synchronized. |
| Inventory, manifest, ledger and Records | All 160 scheduled captions, chunks, dockets, dates and classifications match the manifest, and all scheduled rows are completed. All 163 distinct Records match the ledger: 162 Court actions plus the admitted statutory source. The current-global workspace classification exception is F-09. |
| Render coverage | All 162 Court actions occur in the 13 generated handoffs and renders. Counts by chunk are 12, 12, 13, 13, 13, 12, 12, 12, 12, 12, 12, 12 and 15. The admitted PLRA source is separately accounted for. |
| Public Projection identity | Every bounded Public Projection matches its generated Render Input. The eleven-block interfaces, event coverage and dates reconcile. Repair comparisons also confirm unchanged public substance. |
| Runtime freshness | All 13 current runtime splits pass comparison with the approved briefs, including the operative scoped updates. |
| Effective dates and dependencies | Manifest and ledger dates agree with Records; each chunk's events are in effective-date order. No future-dated Record dependency was found. Same-day references preserve the applicable entering-law baseline or concern assignment accounting; they do not import independent peer decisions as earlier law. |
| Participation, judgments and joins | The roster and applicable nonparticipation reconcile. Checked 148 numeric judgment-table rows, 104 compact numeric judgment blocks and 411 topology rows, with prose and common-coalition exceptions reviewed. Nonreaching votes, partial joins, judgment-only agreement and AT&T's O'Connor nonparticipation remain correctly distinguished. |
| Working links and anchors | All 2,353 local references across 219 files resolve, including 1,223 anchor references. Frozen/derived-copy navigation was excluded from the defect test as directed. |
| Recorded Git objects and repair dependencies | Recorded commit and blob identifiers resolve through permitted `git cat-file` lookups. Source numbers, escaped statutory text, byte counts and incidental hexadecimal-looking text were distinguished from Git references. F-03 digests and the edited assignment dependencies pass the specific checks above. |
| Candidate staging and cleanup | The three candidates retain matching staged publication metadata. Candidates and five pass notes properly await Close Commit cleanup; they must not be removed during this audit. No tracker was published. |
| Carry-forward and next-term setting | All fourteen separately pending Court matters retain their stages and conditions. The two Arteaga petitions and four Breard proceedings remain distinct. Davenport and Jean remain separate OT1998 reservations. Candidate Standing State preserves the permitted docket-only form, nine-Justice roster, seniority, thirteen circuit allotments and standing referral practice. |

## Confirming legal-substance review

The prior clean legal-substance result remains supported. The repair changed no controlling judgment, proposition-level coalition, holding, precedent treatment, merits remedy, published separate writing or Justice-specific historical departure. The legal review of the repaired assignment explanations is stated above; unchanged public bytes were an additional preservation check, not a substitute for examining those explanations.

The U.S. Shoe candidate repairs accurately carry the unanimous controlling jurisdiction rule. They identify the determinations covered by §1581(i), keep the distinct §1581(j) exclusion separate, preserve the requirement to use the protest channel when it actually governs, and do not turn jurisdictional treatment of the levy into its constitutional characterization. The refund, fee and nonexport limits remain unchanged.

The NAHB character repair preserves the economic-conversion-only holding, the separate habitat-harm and conditional-permit requirements, and the noncontrolling status of Stone's additional proposal. The Bestfoods repair preserves the distinction between derivative liability under veil-piercing law and direct pollution-related operation, including the temporal and attribution limits and reserved questions.

The repaired workspace scope and cursor properly distinguish completed scheduled review from a pending Supreme Court stage. They infer no later compliance event or terminal disposition and do not convert lower-court remands into pending Supreme Court proceedings. F-09 concerns only the reported inventory classifications and supplies no basis to reopen an adjudication.

## Remaining discrepancy

### F-09 — Low — Two current workspace inventory summaries retain stale classifications

**Files and lines:**

| File | Line |
|---|---:|
| `workspace/continuity.md` | 15319 |
| `workspace/neutral-projection.md` | 15531 |

**Discrepancy:** Both paragraphs expressly describe the current case index and manifest but still report 150 MERITS and five DISMISSAL. The repaired index and manifest contain 151 MERITS and four DISMISSAL. These are current global statements, not bounded historical summaries. The 160-item total, one ORIGINAL and four APPLICATION remain correct.

**Exact fix:** In each of those two existing paragraphs, replace `150 MERITS` with `151 MERITS` and `five DISMISSAL` with `four DISMISSAL`. Preserve the remaining wording, historical summaries, pending-stage conditions and existing line endings. No new file, new holding, change of authorship or adjudication correction is required.

## Disposition

F-01 through F-08 are resolved. F-09 is the sole remaining discrepancy. Correct the two existing workspace paragraphs and confirm their agreement with the index and manifest before Close Commit. No other legal or deterministic discrepancy was found in this confirming review. This audit changes no adjudication and publishes no candidate to `state/`.

READY FOR CLOSE COMMIT: NO
