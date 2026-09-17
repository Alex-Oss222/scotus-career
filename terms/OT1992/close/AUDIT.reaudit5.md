# October Term 1992 — Fifth close re-audit

**Audit date:** September 17, 2026.  
**Result:** **Not ready for Commit. Finding 11(a) remains open in two lineage paragraphs.** Findings 11(b) and 11(c) are resolved. No new substantive discrepancy or separately numbered finding was identified.  
**Scope:** Report only; no source, candidate or tracker was repaired.

This report supplements [the fourth re-audit](AUDIT.reaudit4.md). Findings 1–10 and 12–15 retain their resolved status. The examined HEAD is `046534e947527c250637a8832cd81c428135193c`; the working tree was clean at intake. Read-only history and file hashes show that the intervening changes consist of the fourth audit report at `7924f22` and five provenance-paragraph edits across the Demos and Moreau records at `046534e`. No adjudicative text changed.

## Verification of the three remaining inaccuracies

| Fourth-pass item | Result | Evidence |
|---|---|---|
| 11(a): attribution of the present lineage wording | **Still open** | Both records correctly describe `ac3ebda` as adding a version-1.1 lineage account, but now attribute their present wording to `f47a06a` and `78397d1`. The actual paragraphs at those revisions differ from the current paragraphs, which were edited again at `046534e`. |
| 11(b): first ledger placement | **Resolved** | Both durable-publication paragraphs now distinguish publication without ledger rows at `e147769`, insertion in effective-date positions at `ac3ebda`, and relocation to the ledger's end with retrospective-recovery labels at `f47a06a`. Actual historical ledger rows confirm that sequence. The label “first appended” is expressly qualified by “not yet in append order,” so it no longer asserts false placement. |
| 11(c): Moreau's initial projection restoration | **Resolved** | The lineage and annex now correctly attribute restoration of “or understandings” and the no-presumed-consent clause in both downstream files to `3cc14e4`. They distinguish the further projection repairs at `563cb7b`: alignment of explanation wording, restoration of “the affected employees,” and completion of the input precedent-treatment sentence. Historical file contents and diffs support those allocations. |

## Exact remaining correction

**Locations:** Line 7, the Lineage paragraph, in the [Demos record](../records/Demos_v_Storrie_fee_motion_1993-03-08.md) and [Moreau record](../records/Moreau_v_Klevenhagen_merits_1993-05-03.md).

Both contain this clause:

> subsequent wording-only provenance repairs at commits `f47a06a` and `78397d1` produced this paragraph's present form.

The `046534e` diff itself disproves that attribution: it replaces the earlier attribution to `ac3ebda` with this clause and, for Moreau, also changes the account of the projection repairs. This is the same narrow defect identified in 11(a), with the inaccurate attribution moved to later commits. It does not affect law, votes, judgment, remedy, or adjudicative version.

For a concrete repair that avoids another self-referential wording claim, replace that clause in both paragraphs with:

> subsequent wording-only provenance repairs occurred at commits `f47a06a`, `78397d1`, and `046534e`.

That statement records completed historical edits without claiming that a past commit contains the newly edited paragraph verbatim. A wording-only correction does not require changing version 1.1, expanding a holding, or altering downstream projections. This audit does not make the replacement because the user prohibited edits to records.

## Regression checks before Commit

This was a repair-focused re-audit using the earlier audits as the baseline for unchanged substance, not a fresh reconstruction of every adjudication. Every changed line was reviewed against the fourth audit's examined revision. No new external-source retrieval is claimed.

- Hash comparison with the fourth audit's intake identifies only Demos and Moreau as changed among the previously examined artifacts. All three candidates, all eleven inputs, all eleven public renders, the other 124 records, workspace, inventory and opening trackers remain unchanged.
- All 126 record files are indexed; the actual ledger contains 126 distinct record links, with no missing or duplicate record. Its final two rows remain the expressly retrospective Demos and Moreau recoveries after DeBoer. Public chunks retain 123 entries and 123 closing lines.
- The four Demos/Moreau operative rules, authority statements and explanations, together with holding-specific precedent treatment, remain unchanged in their input Holdings blocks. Explanation counts remain 171/199 and 185/175 words. The previously reviewed permissible public paraphrases are unchanged.
- Candidate headers agree: **Last completed October Term: 1992**; **Processed through: July 26, 1993, after DeBoer v. DeBoer, No. A-64.**; **Edition: September 17, 2026**.
- Candidate file links and heading anchors resolve in their existing locations and under a prospective unchanged copy into `state/`. No exact duplicate holding text or Standards heading was found. The only mechanical holding/baseline comparison exceptions remain the previously reviewed Crosby spacing difference and opening-header replacement.
- The unchanged Standing State preserves the OT1993 roster and seniority, thirteen August 10 allotments, referral practice and eight carried matters: Zatko and companions, Wyoming, Reynolds, Grubbs, Martin No. 92-5618, Louisiana, Delaware and Nebraska. The previous roster, allotment, carry-forward and restricted-content checks remain undisturbed. Blair remains complete at this Court; its corrected provenance and the workspace's cumulative-law and neutral-projection repairs remain unchanged.

Working evidence is preserved in `tmp/reaudit1992-fifth/`: intake hashes, checking scripts, `checks.json`, `final-checks.json`, `history.json`, `repair.diff`, historical correction diffs and final integrity results. Mechanical comparisons support coverage and conservation; they do not independently decide legal meaning.

## Commit condition and boundaries

**Finding 11(a) alone remains open.** Commit still requires correction and verification of the two quoted clauses. No other repair is required by this pass.

The sole durable file written is `terms/OT1992/close/AUDIT.reaudit5.md`; scratch files are confined to `tmp/`. Earlier audits and all other existing close files are unchanged. Nothing under foundation, stone, state, or OT1992 briefs, runtime, records, render-inputs or output was modified; workspace was not modified. No git commit, checkout, branch or push command was run. No Term-Close Dossier or tracker replacement was performed.
