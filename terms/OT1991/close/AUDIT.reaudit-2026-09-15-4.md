# October Term 1991 — Fresh term-close audit

**Audit date:** September 15, 2026.  
**Result:** One unresolved handoff discrepancy remains, affecting 28 fields in twelve early events. The coordinated close is not ready for Commit.  
**Proposed common cutoff:** July 17, 1992, after Benten v. Kessler.  
**Action:** Report only; no repair, adjudication, or tracker replacement.

This report preserves [AUDIT.md](AUDIT.md) and the [first](AUDIT.reaudit-2026-09-15.md), [second](AUDIT.reaudit-2026-09-15-2.md), and [third](AUDIT.reaudit-2026-09-15-3.md) reaudits. It uses a new filename because AGENTS.md, rule 2, states: “Nothing in `close/` is modified once written.” Earlier findings were checked against the current files; an earlier report was not treated as proof of a present defect.

## Scope and governing sources

The audit compares the three term-opening trackers, all 125 current record files (124 Court events and the October 23 institutional source), the case inventory, final manifest and ledger, final Term Continuity Note and Current-Term Neutral Projection, the three closing candidates, and all fourteen public chunk renders. The effective Render Inputs, including the older correction supplements, were checked to identify the public handoffs and distinguish current authority from superseded material.

The governing sources are [AGENTS.md](../../../AGENTS.md), the [Engine](../../../foundation/ENGINE.md), [Render Contract](../../../foundation/RENDER_CONTRACT.md), [Court Composition](../../../foundation/COURT_COMPOSITION.md), and the [Holdings](../../../foundation/templates/HOLDINGS_TEMPLATE.md), [Standards and Tests](../../../foundation/templates/STANDARDS_AND_TESTS_TEMPLATE.md), and [Standing State](../../../foundation/templates/STANDING_STATE_TEMPLATE.md) instructions. Records control; public renders are cross-checks.

Three parallel reviews covered chunks 1–5, 6–10, and 11–14. The principal review covered the opening baseline, institutional source, term-wide reconciliation, carry-forwards, candidate structure and references, and current Casey workspace. The review examined operative rules, authority, limits, precedent treatment, remedies and continuity throughout the record set, with judgment, topology and audit material examined for the relevant authority questions. Full-file mechanical comparisons were distinguished from semantic review. This is not a fresh reconstruction of every external source or every superseded modeling statement, and no historical result or new modeled vote was substituted for a canonical decision.

The expressly authorized Casey version 1.5 result governs: Stone, Blackmun, Stevens, O'Connor and Souter directly adopt the complete six-step framework. Its preserved earlier objections are provenance, not current law. The record's specific direction to propagate the user's own public text with no substantive alteration also governs that text's presentation; the audit does not treat departures from routine length bands in that adopted text as an unresolved defect. The older separate-file correction convention for Holmes, Suter/Montana, Alaska and Harris is respected.

## Unresolved discrepancy

### Controlling-holding wording remains paraphrased in twelve early Render Inputs

**Classification:** Record-to-Render-Input handoff fidelity. No changed legal rule, coalition, disposition or remedy was identified from these wording differences.

[AGENTS.md](../../../AGENTS.md), line 85, requires the record's controlling-holding section to be carried into the Render Input's Holdings block **unchanged**. The ensuing standard identifies the operative rule, authority, controlling explanation and precedent treatment as its elements. The current inputs now preserve all 61 controlling-explanation paragraphs in the chunks 1–5 range verbatim. However, twelve events still reword other controlling-holding text: **14 operative-rule paragraphs, nine authority paragraphs and five precedent-treatment paragraphs — 28 fields altogether**.

The table identifies every confirmed actual-word difference in those fields. It excludes differences consisting only of whitespace, Markdown, punctuation or apostrophe typography. Placement of precedent treatment in the separately required seventh block is not itself a defect. The unchanged-text requirement applies to the record-to-input handoff; a faithful public narrative may use the Render Contract's permitted presentation flexibility.

In the table, **Input 1** means [OT_1991CHUNK1.md](../render-inputs/OT_1991CHUNK1.md) and **Input 2** means [OT_1991CHUNK2.md](../render-inputs/OT_1991CHUNK2.md). Numbers are current file line numbers. Paired numbers identify distinct component paragraphs, in matching order. A dash means no confirmed wording discrepancy in that field.

| Event and authoritative record | Operative rule: record → input | Authority: record → input | Precedent treatment: record → input |
|---|---|---|---|
| [United States v. Ibarra](../records/United_States_v_Ibarra_merits_1991-10-15.md) | 21 → Input 1:29 | 23 → Input 1:31 | 29 → Input 1:36 |
| [Zatko v. California](../records/Zatko_v_California_fee_motions_1991-11-04.md) | 19 → Input 1:163 | 21 → Input 1:165 | 25 → Input 1:170 |
| [Hafer v. Melo](../records/Hafer_v_Melo_merits_1991-11-05.md) | 20 → Input 1:206 | 22 → Input 1:208 | 28 → Input 1:213 |
| [Board of Governors v. MCorp Financial](../records/Board_of_Governors_v_MCorp_Financial_merits_1991-12-03.md) | 21 → Input 1:249 | 23 → Input 1:251 | — |
| [Griffin v. United States](../records/Griffin_v_United_States_merits_1991-12-03.md) | 21 → Input 1:292 | 23 → Input 1:294 | 29 → Input 1:299 |
| [Estelle v. McGuire](../records/Estelle_v_McGuire_merits_1991-12-04.md) | 39, 46 → Input 2:35, 42 | — | — |
| [Southwest Marine v. Gizoni](../records/Southwest_Marine_v_Gizoni_merits_1991-12-04.md) | 31 → Input 2:85 | 32 → Input 2:87 | 34 → Input 2:92 |
| [Wooddell v. IBEW Local 71](../records/Wooddell_v_IBEW_Local_71_merits_1991-12-04.md) | 33, 39 → Input 2:129, 136 | 34, 40 → Input 2:131, 138 | — |
| [Gibson v. Florida Bar](../records/Gibson_v_Florida_Bar_merits_1991-12-04.md) | 39, 45 → Input 2:189, 196 | — | — |
| [Simon & Schuster v. Crime Victims Board](../records/Simon_and_Schuster_v_Crime_Victims_Board_merits_1991-12-10.md) | 31 → Input 2:239 | — | — |
| [Ardestani v. INS](../records/Ardestani_v_INS_merits_1991-12-10.md) | 31 → Input 2:282 | — | — |
| [Union Bank v. Wolas](../records/Union_Bank_v_Wolas_merits_1991-12-11.md) | — | 32 → Input 2:327 | — |

Examples establish the nature and limits of this finding:

- Ibarra's record says “upon disposition of the motion; this rule does not determine,” while the input says “upon disposition; the rule does not decide.” The record's authority paragraph names the eight participating Justices; the input substitutes “Unanimous per curiam opinion.” Its precedent paragraph is also compressed. The named participation and substantive explanation elsewhere preserve the decision's meaning, but do not satisfy the unchanged-text instruction.
- Zatko's record states the full current-submission, extreme-abuse, fee, petition-form and prospective-ban qualifications in two sentences. The input rewrites both sentences. Its restored explanation supplies the relevant detail; the audit does not infer a newly altered filing rule.
- Wolas's rule and explanation already match. Its authority field changes “Scalia's separate writing agrees” to “Scalia's concurrence agrees.” That is substantively consistent but still a wording change.

Estelle's first authority paragraph differs only by a comma and is excluded. MCorp's precedent paragraph differs only by the apostrophe in “Boire's” and is excluded. Mireles's paraphrased no-controlling-treatment statement is excluded because its equal division supplies no controlling holding. No corresponding controlling-text handoff discrepancy was found in chunks 3–14, including their effective correction supplements.

**Required resolution before a clean audit:** Project the authoritative controlling-holding wording unchanged into the affected Render Inputs, preserving the actual decisions and all unaffected event blocks. Check the resulting public projections for required substance and depth. This finding supplies no basis to change a vote, holding, authority scope, remedy or underlying record. No repair was performed in this audit.

## Checks that passed

| Check | Result |
|---|---|
| Opening baseline | Holdings and Standards start empty. All three opening trackers identify no completed simulated term, the October 7, 1991 opening baseline and September 14, 2026 edition. No prior registered proposition requires rollover. |
| Synchronized candidate headers | All three use exactly `Last completed October Term: 1991`; `Processed through: July 17, 1992, after Benten v. Kessler.`; `Edition: September 15, 2026`. |
| Inventory, manifest and ledger | The inventory has 124 Court events. The manifest has those events and the October 23 institutional source as 125 completed dated rows, followed by the separately pending Coleman petition: 126 rows. Dated rows are in effective-date order. The numbered ledger accounts for 125 distinct existing record files; none is absent or unindexed. The fuller Harris captions resolve to their supplied A-766 and A-768 dockets. |
| Same-day and correction treatment | Corrections replace the relevant effective event rather than add a new Court event. The expressly dependent Harris sequence and coordinated airport companions remain distinguished from independent same-day decisions. Casey, Lucas and Espinosa retain their independent June 29 entering-law boundaries where recorded; Benten remains the final July 17 action. |
| Natural anchors and fields | All 150 primary Holdings case/area blocks supply docket and decision date. There are 272 Holding fields and 272 Current force fields, plus twelve independent-alternative fields and twelve corresponding force fields. No duplicate complete Holding or alternative text was found. All 98 Standards entries contain the required core fields. Candidate links and prospective Holdings navigation fragments resolve. These mechanical checks supplement, rather than replace, semantic review. |
| Controlling-law coverage | No omitted controlling proposition, duplicate substantive holding, or promotion of noncontrolling reasoning into either closing law register was identified. Cross-area entries divide different questions; independent grounds and operative qualifications remain distinct. Ordinary applications of unchanged doctrine do not automatically require a new Standards entry. |
| Fractured and nonprecedential authority | The candidates preserve the relevant direct majorities, valid recorded narrower grounds, unresolved fractures and judgment-only support. Equal divisions, unexplained orders and PFZ's dismissal acquire no invented substantive law. Reynolds's unexplained interim order and the Harris-specific further-stay restriction are not promoted into general doctrine. Benten's reasoned relief-specific holding remains limited to its actual ground. |
| Public accounting | The fourteen renders contain 124 bounded event entries and 124 closing lines. Authorized older correction insertions appear without duplicate Court events. Public blocker sections list no cleared-blocker history. The current workflow-metadata scan disclosed no prohibited version/lineage disclosure in a public entry. |
| Roster, seniority and allotments | Standing State's nine occupied seats, service dates, seniority and thirteen circuit allotments agree with the Composition and October 23 admitted source at the OT1992 opening. The opening referral practice is carried unchanged. |
| Standing State scope | Only the permitted header, current Court, allotments, standing practices and four docket lines appear. There is no positions register, dependency/history section or premature future transition. Ordinary remands to lower courts are not treated as pending Supreme Court matters. |

### Open matters carried forward

| Matter | Authoritative continuing status | Candidate treatment |
|---|---|---|
| Zatko, No. 91-5052 and sixteen companions | The November 25, 1991 paid-docketing condition remains unresolved; no admitted source establishes compliance, noncompliance or later action on the petitions. Record lines 29–32; workspace lines 4912 and 5294. | One docket line carries that unresolved condition without deciding any petition. |
| Wyoming v. Oklahoma, No. 112, Original | Declaration and injunction issued; original jurisdiction retained for implementation. Record lines 31 and 111–117. | One docket line retains implementation jurisdiction. |
| Coleman v. Thompson, petition No. 91-8336 | Application A-877 ended; the distinct petition remains pending until its own dated action. Record lines 85–87 and the final manifest. | One docket line carries the petition, without inventing a poll, result or date. |
| Reynolds v. IAAF, No. A-954 | Limited trials protection remains in force pending further order; the trials' start is not an automatic termination. Record lines 34 and 85. | One docket line carries the continuing interim protection. |

The [Standing State candidate](STANDING_STATE.candidate.md), lines 58–61, contains all four. No additional user-added lower-court case or unresolved Supreme Court proceeding requiring another docket line was identified. Harris's permission condition remains a condition on a concluded application, with no new request established; it does not justify inventing a pending matter or a prohibited filing-conditions register.

## Earlier findings independently verified as cleared

- **Casey's three remaining workspace contradictions:** Workspace lines 3959, 3969 and 3971 now state the nine-Justice timetable result, Kennedy's distinct retained-core ground, and the conditional State justification-and-fit burden after the meaningful-interference threshold. They agree with the operative version 1.5 record and the current Neutral Projection.
- **Gade's unnamed savings boundary:** Record lines 23 and 70, Render Input chunk 12 line 428 and public output line 379 now supply the §4(b)(4) workers'-compensation and employer/employee rights, duties and liabilities qualification. They preserve it without turning it into a new construction deciding the occupational-license question.
- **Felix and Robertson's prose self-join wording:** Felix record lines 93 and 106 and Robertson line 90 now name the authors and the other joining Justices correctly. Input 7 lines 60, 73 and 404 and workspace lines 1204, 1211 and 1296 agree. Aggregate topology lists include each author once in the correct total and do not add a vote.
- **Early controlling explanations:** All 61 explanation paragraphs in the chunks 1–5 records now occur verbatim in the proper event's Render Input. The prior explanation-text complaint is cleared. The rule, authority and precedent wording listed above remains unresolved; the earlier finding is therefore only partially cleared.

The previously repaired Casey supersession and reporting safeguards, Lujan standing elements, Gizoni reserved question, Hunter reconciliation evidence, Zatko caption/count, Wrigley contractor qualification, Estelle cutoff and Presley entering-law date were also checked in their relevant ranges; no renewed discrepancy was identified. The [Standards source-limitation note](STANDARDS_AND_TESTS.BLOCKERS.md) correctly identifies Wrigley's former gap as resolved. The workspace's former standalone Casey version 1.2 link is preserved historical correction provenance, not a missing current authority.

## Coverage evidence and preservation

The range reviews cover 41 Court records plus the institutional source in chunks 1–5, 46 Court records in chunks 6–10 including the older corrections, and 37 Court records in chunks 11–14: 125 current source records altogether. The final manifest and ledger provide their complete natural-key index. Current controlling sections were compared throughout; superseded Casey modeling was not counted as operative law.

Working evidence is confined to `tmp/audit_1991_current/`: the three range reports, mechanical field/link/count results, inventory identity checks and input-preservation snapshot. The later handoff checks found all 105 labeled rules, 211 authority/explanation paragraphs and 345 precedent segments in chunks 6–10 preserved after typography and whitespace normalization. For chunks 11–14, all 112 labeled rules and the substantive paragraphs of the controlling sections were preserved; all 31 Casey operative rules occur exactly once in Holdings. These are text and consistency checks, not mechanical determinations of legal meaning.

All 246 preexisting files in the preservation snapshot remained unchanged, including foundation, state, the OT1991 sources, workspace, candidates and earlier audits. The only durable audit artifact added is this report; working files remain under `tmp/`. No `git commit`, `git checkout`, `git branch` or `git push` was run. The term-opening trackers remain authoritative until a separately authorized coordinated Commit pass after the unresolved discrepancy is cleared.
