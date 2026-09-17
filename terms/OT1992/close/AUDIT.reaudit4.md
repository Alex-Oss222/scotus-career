# October Term 1992 — Fourth close re-audit

**Audit date:** September 17, 2026.  
**Result:** **Not ready for Commit. Finding 11 remains partly resolved.** Three correction-history statements remain inaccurate; none changes the adjudication. No new substantive discrepancy or separately numbered finding was identified.  
**Scope:** Report only. No candidate, record, workspace, input, render or opening tracker was changed.

This report supplements [the third re-audit](AUDIT.reaudit3.md), retaining the original finding numbers and the resolved status of findings 1–10 and 12–15. The examined HEAD is `78397d1f4d39564d7d1e5bf368b0e905c6397fb2`. The working tree was clean at intake. Read-only history establishes that the repair after the third re-audit changes only three provenance paragraphs in each of the Demos and Moreau records. The intervening `aa43ee1` adds the third re-audit report. These are existing commit references; this pass made no commit.

## Finding 11 — verification of the hand repair

The repair now correctly distinguishes initial record publication at `e147769` from the later ledger recovery. It correctly identifies the changes made inside each record by `3cc14e4`: Demos's full-form selection, prospective-restriction explanation expansion and added prospective Denton treatment; Moreau's two explanation expansions. Demos's current-filing explanation and reservation, and Moreau's operative alternative and consent limit, were already present in the original records. The repair also correctly recognizes that `ac3ebda` edited the record files' lineage paragraphs, while `563cb7b` did not edit those records.

The synchronized versions, input metadata, unchanged Holdings handoffs, Blair provenance and corrected workspace ledger remain intact. The following statements nevertheless prevent closure of finding 11.

### 11(a). The current lineage wording is attributed to the wrong commit

**Locations:** Lineage paragraph in the [Demos record](../records/Demos_v_Storrie_fee_motion_1993-03-08.md) and [Moreau record](../records/Moreau_v_Klevenhagen_merits_1993-05-03.md), line 7 in each.

Both now say: **“Commit `ac3ebda` changed this Lineage paragraph to its present form.”** The actual `ac3ebda` paragraphs differ from the present paragraphs. They were subsequently edited in `f47a06a` and again in the just-examined `78397d1` repair. The historical attribution is therefore still false even though the new distinction between file edits and substantive edits is sound.

**Required correction:** Describe `ac3ebda` as adding the version-1.1 lineage account, followed by later provenance repairs at `f47a06a` and `78397d1`; remove the claim that it produced the paragraph's present wording. Further wording-only repairs need not change the adjudicative version or any downstream holding.

### 11(b). The first ledger insertion is still described as being in append order

**Locations:** Validation and durable commitment, final paragraph of both records; cross-check the [workspace ledger](../workspace.md#term-working-ledger-index).

Both now attribute the first ledger row to `ac3ebda` **“as a retrospective recovery placed in actual append order rather than at its [effective] date,”** followed by relocation and express labeling at `f47a06a`.

The first-insertion commit is correct, but its placement is not. In the actual `ac3ebda` workspace:

- Demos was inserted between Delo v. Lashley (March 8) and Reno v. Flores (March 23).
- Moreau was inserted between Turner Broadcasting (April 29) and United States v. Idaho (May 3).

Those were effective-date positions within the existing ledger, not append-order positions. Only `f47a06a` moved the rows to the ledger's end, after DeBoer, and expressly identified the retrospective recovery. The current workspace already has that correct placement and needs no change.

**Required correction:** State that `e147769` published the records without ledger rows; `ac3ebda` first inserted the rows in effective-date positions; and `f47a06a` moved them to the end and labeled them retrospective recoveries. Preserve the original effective dates and chronology cursor.

### 11(c). Moreau assigns the initial projection restoration to the later follow-up repair

**Locations:** Moreau's Lineage paragraph and its Version 1.1 correction note in the Adaptive audit annex, lines 7 and 84.

The revised account says that `563cb7b` corrected the downstream omission of the “or understandings” alternative and the no-presumed-consent limit. Those two protections were already restored to both the input and public render in `3cc14e4`. Direct inspection of both files at that revision confirms the operative phrase **“agreements or understandings”** and the explanation **“this holding does not presume it from selection of a representative alone.”**

`563cb7b` made further projection repairs: it aligned explanation wording with the record, restored “the affected employees” in the operative proposition, and completed the input's precedent-treatment sentence. It did not first restore the two protections named in the current provenance account.

**Required correction:** Attribute the initial alternative/consent restoration to `3cc14e4`, alongside that commit's record-explanation expansions; describe `563cb7b` as the subsequent projection-fidelity repair. Retain the correct statement that those two protections were already in the original source record. No holding or explanation needs expansion or re-adjudication.

## Regression checks before Commit

This is a repair-focused re-audit using the prior audits as the review baseline for unchanged substance, not a fresh historical reconstruction of all adjudications. Every changed line was reviewed against the third re-audit's examined revision. Historical file contents and diffs, rather than commit-message descriptions alone, establish the findings above.

- Hash comparison with the third re-audit intake identifies only Demos and Moreau as changed among the previously examined artifacts. Their changes are confined to lineage, correction notes and durable-publication accounts. All three candidates, all eleven inputs, all eleven public renders, the other 124 records, workspace, inventory and opening trackers are unchanged.
- All 126 records remain indexed exactly once in the actual ledger; no record is missing or duplicated. Public chunks retain 123 entries and 123 closing lines. The ledger still ends with the two expressly retrospective recoveries.
- Demos and Moreau retain all four operative rules, authority statements and controlling explanations unchanged in their respective input Holdings blocks, including the holding-specific precedent treatment. The source explanations remain 171/199 and 185/175 words. The already-reviewed public paraphrases remain permissible; no new projection defect is identified.
- All three candidate header values agree: **Last completed October Term: 1992**; **Processed through: July 26, 1993, after DeBoer v. DeBoer, No. A-64.**; **Edition: September 17, 2026**.
- Candidate file links and heading anchors resolve in their existing locations and under a prospective unchanged copy into `state/`. No exact duplicate holding text or Standards heading was found. The mechanical comparison's only exceptions remain the previously reviewed Crosby spacing difference and replacement of the opening header; no new omission is indicated.
- Standing State retains the OT1993 roster and seniority, thirteen August 10 circuit assignments, referral practice and eight carried matters: Zatko and companions, Wyoming, Reynolds, Grubbs, Martin No. 92-5618, Louisiana, Delaware and Nebraska. The roster and allotments agree with Composition. Blair remains complete at this Court; the current ledger, cumulative-law projection and neutral-comparator repairs remain unchanged.

Working evidence is preserved under `tmp/reaudit1992-fourth/`: intake hashes, checking scripts, `checks.json`, `final-checks.json`, `history.json`, `repair.diff`, saved correction diffs and `integrity.json`. The history evidence includes the actual ledger neighbors and both Moreau projection texts at the relevant revisions. No new external-source retrieval is claimed.

## Commit condition and boundaries

**Finding 11 alone remains open.** Commit requires accurate provenance for the three statements above and verification of that limited repair. All previously resolved findings remain resolved. No candidate rewrite, vote change, holding change, remedy change or new adjudication is required by this report.

The sole durable file written by this pass is `terms/OT1992/close/AUDIT.reaudit4.md`; scratch files are confined to `tmp/`. Earlier audits and all other existing close files are unchanged. Nothing under foundation, stone, state, or OT1992 briefs, runtime, records, render-inputs or output was modified; the workspace was not modified. No git commit, checkout, branch or push command was run. No Term-Close Dossier or tracker replacement was performed.
