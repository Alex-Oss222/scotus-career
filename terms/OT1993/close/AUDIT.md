# October Term 1993 — Fourth Re-audit

**Audit date:** September 28, 2026.
**Result:** FAIL — deterministic gate not cleared; fresh term-wide legal audit not reached.
**Current findings:** Two groups: zero critical, zero high, zero medium, two low.
**Publication status:** Staged close; Commit is not authorized.
**Observed repository HEAD:** `70f88c96b0a3be680c66a22ab95d9f957d11a6ac`, obtained by direct read-only object and reference inspection.

This report replaces the current Audit. The file actually present at intake was headed “Second Re-audit,” dated September 28, with R08–R11; it was not headed “Third Re-audit” as the task description anticipated. The current files and repository objects, rather than that naming discrepancy or the former report's conclusions, control this review. The naming discrepancy is disclosed as scope information, not counted as a content finding.

R08–R10 are corrected. R11's previously identified **active** workspace path is corrected. The wider snapshot sweep described in the task is not complete, and the required term-wide prohibited-source scan also fails. These are the two current findings below; neither is a finding that an authoritative vote, holding, judgment, or remedy was changed by the provenance removal.

The task expressly required that the remaining deterministic checks pass **before** the fresh AI legal review. That condition was not satisfied. Consequently this report does **not** certify a fresh substantive examination of every one of the 95 matters, either Holdings pass contribution, the complete Standards candidate, or the Standing State candidate. The all-matter checks below concern coverage, identity, dates, arithmetic and preservation. Their success cannot substitute for the gated legal review of votes, coalitions, holdings, precedent treatment, remedies, continuity and Justice-specific departures. The earlier Audit’s substantive conclusions are not adopted as findings of this pass.

Only this Audit and ignored scratch evidence under repository-root `tmp/ot1993_reaudit4/` were written. No content repair, publication, or Git command was performed.

## Method and deterministic results

The governing Engine, Render Contract, Court Composition, repository instructions and relevant tracker instructions were consulted. The first validation executed the unchanged main routine of `tools/check_term.py OT1993`. That script ordinarily launches Git to test commit existence. To obey the express prohibition on **any** Git command, a scratch `runpy` harness substituted only the commit-existence callback with direct read-only object lookup; a subprocess guard rejected Git execution. The Holdings synchronization and all eight runtime-split checks ran normally. The initial result was **exit 0, 14 lexical warnings**. The repository tool was not edited.

| Check | Current result and limits |
|---|---|
| Inventory → manifest → Record → Render Input → output | PASS for all 95 Court matters. There are 95 manifest events, 95 corresponding Court Records and 95 public entries. The additional Record is the South Carolina legislative source admission. Chunk counts are 12, 12, 12, 12, 12, 12, 12 and 11. No missing or duplicate event was found. |
| Effective-date order | PASS for inventory, manifest, Record dates, generated handoff order, render chronology and closing dates. Each chunk preserves inventory order within its effective-date groups. The express same-day dependency pairs remain separately documented; ordinary processing order supplies no legal dependency. |
| Participation, vote and join arithmetic | No arithmetic discrepancy found in the explicit component tallies, 136 judgment rows containing names, and 273 writing rows containing names. Named participants stay within the applicable roster. The eight prose judgment/topology entries were separately read. Irvine excludes Blackmun; Morgan Stanley and MCI exclude O’Connor. Sassower’s seven-member current-fee component remains distinct from its nine-member prospective decisions. This is clerical reconciliation, not fresh legal approval of the coalitions. |
| Runtime freshness | PASS: all eight approved chunk briefs match the three standard derived splits under the unchanged splitter’s check mode. Nothing was regenerated. |
| Public Projection → Render Input | PASS: all 95 generated event blocks match their bounded canonical Public Projections. Internal controlling-proposition, authority and controlling-explanation paragraph comparisons produced no drift. |
| Render structure and named-set comparison | Required entry boundaries, closing dates and full-form tables pass. All full-form named table sets are preserved. Sixteen table-to-prose diagnostics arise from compact output, not missing adjudications; eight additional input entries already state judgment in prose. No legal-content equivalence certification is inferred solely from these mechanical checks. |
| Links and anchors | FAIL under the task’s complete-term scope: R12. Across 815 term Markdown files other than the replaced Audit, 6,443 local or same-repository link occurrences were checked. Of 527 raw failures, 525 resolve through the already documented inherited-alias convention. The remaining two are actual deleted-source links in term-local scratch Records. The broader file scan also found three source attributions in two Python generators. |
| Commit existence and concise lineage | PASS for 126 genuine commit-reference occurrences in the term scan. All resolve to commit objects. The unresolved lexical candidates are source identifiers, a memorandum number, dates, an MD5 label or fragments of ordinary words—not additional missing commit claims. All 96 current Records match observed HEAD after newline normalization; all 96 ledger first-integration references reconcile with direct object inspection. The `.gitkeep` placeholder is not a Record. |
| Opening baseline provenance | The qualified baseline account remains supported: Standards and Composition match the cited opening snapshot; Holdings and Standing State have the already disclosed differences. No false byte-identity claim was substituted. |
| Candidate synchronization and cleanup | PASS for pre-Commit staging: exactly three candidates, the two Holdings pass notes, the Standards pass note and one canonical Audit; no Term-Close Dossier or competing candidate. All three candidates share the retained staged publication fields: last completed OT1992; processed through July 26, 1993 after DeBoer; edition September 17, 2026. Removing candidates and pass notes is due after successful Commit, not now. |
| Open-matter carry-forward | The 95 inventory events are completed. The Standing State candidate expressly includes the seven inherited open matters and Anderson’s underlying original writ, plus the fifteen user-added OT1994 matters. Day and Sassower’s current fee questions have express scope closures; Cavanaugh has a completed merits event. No carried matter is silently treated as adjudicated. This is the roster/docket reconciliation, not a replacement for the gated full candidate audit. |
| Current workspace and corrected-source propagation | The active continuity and neutral projections’ 457 explicitly labeled proposition/authority paragraphs each match current public Record paragraphs. The active completed-authority copy matches the corrected Good, Powell and Reed text. The broader claimed sweep fails: R13. |
| Provenance-removal boundary and substantive preservation | PASS for the bounded removal comparison described below. The removal did not alter public output, generated inputs, close candidates, workspace, votes, dispositions, remedies or holdings. Its residual references are R12. |

The accepted checker completion heuristic and external URL reachability remain tool/documentation limitations, not findings. Neither was repaired or re-flagged. The check did not fetch all 532 distinct external links.

## Current findings

### R12 — Low — Deleted-source references remain inside the term’s scratch files

The two ordered source-file deletions are present, and the live briefs, canonical Records, runtime and freeze files contain no remaining reference to any of the three prohibited source-target families. Nevertheless, the task specifically requires **no file anywhere in the term** to retain such a citation. Five references to the deleted method source survive in four files under `terms/OT1993/tmp/`:

| Live file | Line | Remaining defect |
|---|---:|---|
| [assemble_madsen.py](../tmp/assemble_madsen.py) | 203 | Bare source-name attribution in generated Record text. |
| [build_june24_records.py](../tmp/build_june24_records.py) | 226 | Deleted-source Markdown link in Record text or its generator. |
| [build_june24_records.py](../tmp/build_june24_records.py) | 252 | Deleted-source Markdown link in Record text or its generator. |
| [gottshall_carlisle_merits_1994-06-24.md](../tmp/gottshall_carlisle_merits_1994-06-24.md) | 18 | Deleted-source Markdown link in Record text or its generator. |
| [shannon_merits_1994-06-24.md](../tmp/shannon_merits_1994-06-24.md) | 20 | Deleted-source Markdown link in Record text or its generator. |

The two Markdown files contain an actual `read with` link to the deleted source. The June 24 generator contains those same two links in text it can recreate. The Madsen generator still names the deleted source in its `Source:` attribution. These are source attributions, not a diagnostic discussion of a deleted filename. None is a canonical adjudication, but being scratch or ignored does not satisfy the task’s express “anywhere in the term” condition. Repository-root audit scratch is a different location.

No reference to either nonexistent review-source family was found in the remaining term files. This report links only to the live affected files and does not reintroduce a citation to the deleted targets.

**Required resolution:** Remove the residual provenance attributions from these retained files, or remove/relocate obsolete term-local scratch under the operator’s authorized cleanup policy. Preserve the surrounding reasoning and remedy text. Re-run the complete-term scan, including Python generators and scratch subdirectories. No repair was made in this pass.

### R13 — Low — The claimed repository-wide reconciliation of entering-law snapshots is incomplete

The original active-reading-path defect in R11 is resolved. The current workspace and its chunk-8 completed reading copy should not be changed back. However, direct inspection found **40 residual passages across 28 older snapshot files**: Good’s abbreviated timing rule in fourteen entering-law copies and fourteen frozen entering projections; Powell’s malformed punctuation in ten of those frozen projections; and Reed’s superseded future-relative operative label in the two frozen chunk-8 entering projections.

Good’s old paragraph states the reporting and commencement duties without the corrected §1603(b) office-proceedings trigger, §1604 district-court/Court of International Trade scope, Attorney General after-inquiry alternatives, and Treasury-direction consequence. The [current Good Record](../records/United_States_v_James_Daniel_Good_Real_Property_merits_1993-12-13.md#public-projection) supplies those conditions. Powell’s frozen paragraphs retain `unreasonable?for example`; the [current Powell Record](../records/Powell_v_Nevada_merits_1994-03-30.md#public-projection) uses proper dash punctuation. Reed’s two frozen operative rules still describe the statutory provision relative to a future enactment; the [current Reed Record](../records/Reed_v_Farley_merits_1994-06-20.md#public-projection) uses the then-effective statutory formulation.

| Snapshot file | Affected passage and current line |
|---|---|
| [OT_1993CHUNK1_COMPLETED_PUBLIC_AUTHORITY.md](../entering-law/OT_1993CHUNK1_COMPLETED_PUBLIC_AUTHORITY.md) | Good: 590 |
| [OT_1993CHUNK2_COMPLETED_PUBLIC_AUTHORITY.md](../entering-law/OT_1993CHUNK2_COMPLETED_PUBLIC_AUTHORITY.md) | Good: 590 |
| [OT_1993CHUNK3_COMPLETED_PUBLIC_AUTHORITY.md](../entering-law/OT_1993CHUNK3_COMPLETED_PUBLIC_AUTHORITY.md) | Good: 590 |
| [OT_1993CHUNK4_COMPLETED_PUBLIC_AUTHORITY.md](../entering-law/OT_1993CHUNK4_COMPLETED_PUBLIC_AUTHORITY.md) | Good: 590 |
| [OT_1993CHUNK5_COMPLETED_PUBLIC_AUTHORITY.md](../entering-law/OT_1993CHUNK5_COMPLETED_PUBLIC_AUTHORITY.md) | Good: 424 |
| [OT_1993CHUNK6_COMPLETED_PUBLIC_AUTHORITY.md](../entering-law/OT_1993CHUNK6_COMPLETED_PUBLIC_AUTHORITY.md) | Good: 694 |
| [OT_1993CHUNK7_COMPLETED_PUBLIC_AUTHORITY.md](../entering-law/OT_1993CHUNK7_COMPLETED_PUBLIC_AUTHORITY.md) | Good: 694 |
| [OT_1993CHUNK8_BEFORE_DEGRANDY_PUBLIC.md](../entering-law/OT_1993CHUNK8_BEFORE_DEGRANDY_PUBLIC.md) | Good: 699 |
| [OT_1993CHUNK8_BEFORE_JUNE24_PUBLIC.md](../entering-law/OT_1993CHUNK8_BEFORE_JUNE24_PUBLIC.md) | Good: 699 |
| [OT_1993CHUNK8_BEFORE_JUNE27_PUBLIC.md](../entering-law/OT_1993CHUNK8_BEFORE_JUNE27_PUBLIC.md) | Good: 699 |
| [OT_1993CHUNK8_BEFORE_JUNE30_PUBLIC.md](../entering-law/OT_1993CHUNK8_BEFORE_JUNE30_PUBLIC.md) | Good: 699 |
| [OT_1993CHUNK8_ENTERING_PUBLIC_AUTHORITY.md](../entering-law/OT_1993CHUNK8_ENTERING_PUBLIC_AUTHORITY.md) | Good: 7282 |
| [OT_1993CHUNK8_THROUGH_TURNER_PUBLIC.md](../entering-law/OT_1993CHUNK8_THROUGH_TURNER_PUBLIC.md) | Good: 699 |
| [OT_1993CHUNK8_TURNER_ROUTE_CLARIFIED_PUBLIC.md](../entering-law/OT_1993CHUNK8_TURNER_ROUTE_CLARIFIED_PUBLIC.md) | Good: 699 |
| [OT_1993CHUNK2_ENTERING_CONTINUITY.md](../freeze/OT_1993CHUNK2_ENTERING_CONTINUITY.md) | Good: 114 |
| [OT_1993CHUNK2_ENTERING_NEUTRAL_PROJECTION.md](../freeze/OT_1993CHUNK2_ENTERING_NEUTRAL_PROJECTION.md) | Good: 116 |
| [OT_1993CHUNK3_ENTERING_CONTINUITY.md](../freeze/OT_1993CHUNK3_ENTERING_CONTINUITY.md) | Good: 152 |
| [OT_1993CHUNK3_ENTERING_NEUTRAL_PROJECTION.md](../freeze/OT_1993CHUNK3_ENTERING_NEUTRAL_PROJECTION.md) | Good: 154 |
| [OT_1993CHUNK4_ENTERING_CONTINUITY.md](../freeze/OT_1993CHUNK4_ENTERING_CONTINUITY.md) | Good: 166; Powell: 600 |
| [OT_1993CHUNK4_ENTERING_NEUTRAL_PROJECTION.md](../freeze/OT_1993CHUNK4_ENTERING_NEUTRAL_PROJECTION.md) | Good: 166; Powell: 600 |
| [OT_1993CHUNK5_ENTERING_CONTINUITY.md](../freeze/OT_1993CHUNK5_ENTERING_CONTINUITY.md) | Good: 176; Powell: 610 |
| [OT_1993CHUNK5_ENTERING_NEUTRAL_PROJECTION.md](../freeze/OT_1993CHUNK5_ENTERING_NEUTRAL_PROJECTION.md) | Good: 178; Powell: 612 |
| [OT_1993CHUNK6_ENTERING_CONTINUITY.md](../freeze/OT_1993CHUNK6_ENTERING_CONTINUITY.md) | Good: 210; Powell: 678 |
| [OT_1993CHUNK6_ENTERING_NEUTRAL_PROJECTION.md](../freeze/OT_1993CHUNK6_ENTERING_NEUTRAL_PROJECTION.md) | Good: 212; Powell: 680 |
| [OT_1993CHUNK7_ENTERING_CONTINUITY.md](../freeze/OT_1993CHUNK7_ENTERING_CONTINUITY.md) | Good: 223; Powell: 691 |
| [OT_1993CHUNK7_ENTERING_NEUTRAL_PROJECTION.md](../freeze/OT_1993CHUNK7_ENTERING_NEUTRAL_PROJECTION.md) | Good: 225; Powell: 693 |
| [OT_1993CHUNK8_ENTERING_CONTINUITY.md](../freeze/OT_1993CHUNK8_ENTERING_CONTINUITY.md) | Good: 236; Powell: 704; Reed: 2043 |
| [OT_1993CHUNK8_ENTERING_NEUTRAL_PROJECTION.md](../freeze/OT_1993CHUNK8_ENTERING_NEUTRAL_PROJECTION.md) | Good: 238; Powell: 706; Reed: 2045 |

This is a limited propagation/sweep discrepancy, not a newly established adjudicative error. Records remain authoritative; the stale files are earlier snapshots rather than the current workspace’s governing path. Their historical status is why this finding is low severity. It nevertheless prevents confirming the task’s assertion that the **full-repository** snapshot sweep has already reconciled these three corrections. The earlier report expressly distinguished historical snapshots from its active-path finding; this report does not silently expand that earlier finding or call its verified active-path repair unsuccessful.

**Required resolution:** Complete the expressly intended reconciliation of these derived reading copies, or document precisely which historical artifacts are intentionally retained and route readers to corrected authority without asserting current textual identity. Preserve true freeze history and the completed adjudications. A corrective pass must distinguish derived entering projections from immutable substantive commitment handoffs. No file was corrected in this audit.

Three additional older Turner reading copies differ from the current Record in review-route/posture text. A later route-clarified copy and the active completed copy supply the corrected text. Those older snapshots are disclosed in the scratch identity comparison; their historical existence is not treated as an additional current-law defect or as part of the specifically requested Good/Powell/Reed sweep. Broad lexical hits in unrelated habeas background and earlier-term material likewise were not converted into Reed findings.

## Verified disposition of R08–R11

| Prior finding | Current verification |
|---|---|
| R08 — Posters ’N’ Things alternatives | RESOLVED. Standards line 1788 now states imported, exported, transported, or sold through the mail or by any other means, together with the normal lawful course of business and traditional tobacco-use conditions. It keeps the independent authorized-person exception and does not add a primary-use condition to the tobacco exception. |
| R09 — Carter qualification | RESOLVED. Standards line 2451 says “does not satisfy every requirement,” retaining private appropriateness, public inadequacy, financial risk and equitable amount limits. It no longer says that every requirement may fail. |
| R10 — Irvine reserved question | RESOLVED. Standards line 3784 identifies this 1917 inter vivos trust, created before the 1932 gift-tax enactment, and preserves conditional regulatory applicability and the separate later-disclaimer reservation. The unsupported earlier-year cutoff is gone. |
| R11 — Active workspace reading path | RESOLVED at the locations the former report identified: the live continuity/neutral rules and their linked chunk-8 completed authority copy carry the corrected Good, Powell and Reed passages. The wider snapshot sweep is separately and narrowly addressed in R13. |

These conclusions come from current text comparison against the corrected Records, not an assumption that operator corrections succeeded.

## Provenance-removal verification

Direct object comparison identifies the removal as commit `f97f7959fab59916b102e9df8cda2e5633a13904`, compared with its parent `6dafdbfac84d01dc435ce6edc7de36706fa7b570`. This is a concise verification of the identified change, not a demand for narrative commit archaeology. No Git executable was invoked.

The removal changed 103 paths: two deleted source/provenance documents and 101 modified files—eight chunk briefs, twenty-two Records, twenty-four freeze files and forty-seven runtime files. **Zero** paths under output, render-inputs, close or workspace changed in that commit. At audit intake, the current retained tracked term files matched the removal commit after ordinary newline normalization; the subsequent observed commits concern OT1994. Deleted targets remain absent.

The eight chunk briefs contain 95 matter modules. The removal’s 184 brief hunks affect only the repeated interpretive-method and revision-trace fields in 92 modules. They remove the source invitation and provenance list. The remaining method paragraph still states text, context, history, structure, precedent, practical consequences, source-authorized equity, equal regard and unchanged legal burdens. The remaining revision-trace sentence preserves the distinction between historical opinions and in-world precedent. Those two surviving formulations were read and are coherent. The other three modules were unchanged. **Every brief’s actual case-specific reasoning, judgment, remedy, conditions and limits is unchanged by this removal.** This bounded preservation check does not pronounce every pre-existing brief proposition legally correct.

Each changed Record was compared with its pre-removal object and the revised paragraph was read in context. All twenty-two changes delete only the external provenance attribution, with the necessary singular verb/pronoun adjustments where two sources became one. The substantive clauses still follow complete grammatical subjects: the relevant approved scoped supplement, runtime section or Stone input. The revised paragraphs preserve their grounds, joins, reservations, remedies and express limits. All twenty-two Records’ Result lines and complete Public Projections are identical before and after; the other seventy-four Records are unchanged. Thus the comparison covers all **95 Court matters and the separate source Record**, not a sample of publicly visible results.

The unchanged public artifacts and bounded internal changes establish that this removal introduced no vote, disposition, remedy or holding change. The remaining term-local scratch citations fail cleanup scope under R12; they do not undo that preservation result. No new incoherent sentence was found in the changed briefs or Records. All three standard runtime splits remain fresh against the edited briefs.

## Work still required before Commit

R12 and R13 prevent a clean deterministic gate. Resolve or expressly settle their scope, rerun the deterministic checks, and then perform the requested **fresh** legal audit across all 95 matters and the complete coordinated candidates. That review must still examine each proposition’s authority and qualifications, the separate judgment and rationale coalitions, precedent treatment, remedy, continuity and Justice-specific historical departures. Both Holdings pass contributions—chunks 1–5 and chunks 6–8—remain within that required scope. The complete Standards register must be tested independently against opening law and Records; the Standing State candidate must receive the corresponding full source review. No blanket substantive PASS is carried forward from the superseded Audit.

Audit evidence is retained in ignored repository-root `tmp/ot1993_reaudit4/`: initial validator transcript; current deterministic inventory, date and arithmetic results; current link and anchor results; direct object provenance checks; removal diffs and paragraph comparisons; current snapshot sweep; and preservation verification. These are checking aids, not law. The report states the checks actually completed and does not label a blocked stage as passed.

**Final verification:** The unchanged validator’s main routine was rerun through the same no-Git harness against this replacement report: exit 0, with 15 lexical warnings. The extra warning is an ordinary-word fragment in this report, not a missing commit. All 36 report links resolve to existing local targets; its three Public Projection anchors are present. The before/after preservation comparison found all **1,569 protected files unchanged**, with no added or removed protected file. Only the Audit and repository-root scratch evidence changed.

**Operator conclusion:** FAIL — Commit not authorized; fresh term-wide legal stage blocked by the deterministic gate. **Findings: 0 critical, 0 high, 0 medium, 2 low.**
