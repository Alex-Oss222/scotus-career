# OT1999 chunk 3 ? projection integration validation

Status: published and verified. The cumulative continuity and neutral projections cover 36 Court events and three admitted nonjudicial sources through March 6, 2000. This receipt validates projection integration only; it does not replace the chunk adjudication or term checks.

## Work performed

- Updated only workspace/continuity.md and workspace/neutral-projection.md after all twelve chunk-3 Records were written and publication was authorized. Ledger and manifest were not edited by this integration task.
- The preparation script selects the eleven Public Projection fields and the public Continuity material needed for published noncontrolling positions. It does not copy Stone inputs, frozen modeling, reconciliation, assignments or audit annexes into the neutral projection. Each new Event, Holdings, Precedent Treatment, Law After Decision and Source Notes field is copied mechanically; judgment/remedy and procedure are likewise retained. Heading depth changes are formatting only.
- Current corrected Record text supplies the Strout and Council statutory conditions and the final Flores-Ortega, Portuondo and Locke qualifications. Earlier source shorthand does not override those public fields.
- Prior Current Law and Material Published Noncontrolling Positions bodies are preserved exactly. The complete opening-pending block is identical to baseline, retaining all fourteen matters at their stated stages. Fiore remains open for the certified answer; no answer, deadline, default or follow-on disposition is invented.
- Removed only completed Strout from the pending-grant table. Adams remains the next scheduled item on March 6 in chunk 4 and shares the pre-March 6 entering-law baseline with the uncoordinated Portuondo and Locke decisions. The later processing order supplies no earlier-law influence.
- Demoted Continuing open matters to a level-three subsection of Current Procedure and Institution. Continuity has exactly the seven Engine blocks. Neutral retains its five public projection blocks. Stale completion/cursor/chunk references and the source cutoff were updated.

## Checks actually completed

- Recomputed the final signed-lead counts directly from actual public opinion tables and the two narrative authorship statements. Partial lead parts count once per author; per curiam opinions, summaries, certification and admitted sources are excluded. No earlier tally is used as authority. The table appears only in continuity.
- Verified one contiguous completed-events table containing all 39 dated rows in each projection, retaining the previous narrative after the table.
- Verified all twelve new Event, Holdings, Judgment & Remedy and Procedure After Action fields against their source Records, with formatting-only heading nesting where needed. Published noncontrolling material includes Portuondo's four-Justice lead rationale as well as the selected separate writings.
- Verified exact preservation of prior law, prior published positions and the opening-pending block; Strout removal; Adams retention; and Fiore's open status.
- Verified the source/research cutoff states October 18, 1999 through 2000-03-06 while preserving each admitted source's separate effective provisions.
- Verified absence of private Stone fields, lineage labels, historical-departure labels, reconciliation-commitment text and balance-pool metadata in the published projections. Neutral contains no counted-lead table or new private assignment metadata.
- All local relative file/directory link targets exist. Anchor interpretation and the full deterministic term checks remain with the root integration check; this receipt does not claim those unperformed checks.
- Rehashed both published files and all twelve input Records after publication; all match the identities below. No Git command was executed and no repository-commit or commit-hash validation is claimed.

## Recount

| Justice | Counted signed leads |
|---|---:|
| Stone-Zsela | 3 |
| Stevens | 3 |
| O'Connor | 4 |
| Scalia | 3 |
| Kennedy | 5 |
| Souter | 4 |
| Thomas | 3 |
| Ginsburg | 4 |
| Breyer | 3 |

Total counted signed leads: 32. Last counted event: United States v. Locke / Intertanko v. Locke, March 6, 2000. Earlier assignments stand.

## Published identities

| File | Bytes | SHA-256 |
|---|---:|---|
| workspace/continuity.md | 281468 | 3d888b9a4cacaadeabbacc732d3633c3a3fe108113c58a50f453ca41e79d212b |
| workspace/neutral-projection.md | 275615 | a4426a29f2e7b51373683089a26994ced0655fdc986fd27ecceccb9f836d548e |

## Input Record identities

| Record | SHA-256 |
|---|---|
| records/baral-v-united-states_merits_2000-02-22.md | 031967aa362d47980d3d5ec6c929df521de655be1fa5da349728a6559c655104 |
| records/hunt-wesson-v-franchise-tax-board_merits_2000-02-22.md | 2d6ee3f95e9127f386c5e1dd7893ed7f173de8fcea9cefef41ac0e7c353dbd27 |
| records/weisgram-v-marley_merits_2000-02-22.md | cc036875283da822c122423fc99000c9234de5c97dcb63113dc2d52a034a9996 |
| records/rice-v-cayetano_merits_2000-02-23.md | f4e07425153d86bf14834bcd54f4c013cb0da704ca67fe8bdb23d542c50c9875 |
| records/roe-v-flores-ortega_merits_2000-02-23.md | 0af73a7e1acca497d32461fa2003854dd72d287c63f71ed219eee3dbf7dcc6ba |
| records/rotella-v-wood_merits_2000-02-23.md | a2018e99e51566e687182508fbf014fc65b6abcbc309caae508a9f49362e7181 |
| records/village-of-willowbrook-v-olech_merits_2000-02-23.md | 273b9317c88eab53c3455039386c13dec2ee6d0c03f7fc9b48968750306306bb |
| records/strout-v-albanese_merits_2000-02-28.md | 620fdfffb49f12b46bd8c6d4084a9726e835fa679ff4f70792dc20469ac2f8e1 |
| records/shalala-v-illinois-council_merits_2000-02-29.md | 01fb693a23e7404e08693b4d4a2263c1d3bb0e226f544802dfe4bce3bd537233 |
| records/united-states-v-johnson_merits_2000-03-01.md | 7bc57fab48e39ec35a6207ad18682c2a95dd05a075fc1edcc691d00ad0fa5f28 |
| records/portuondo-v-agard_merits_2000-03-06.md | b327d5bca95ea2a3cbe9bd34f61009dd9f5bb6b9678f20573b807baaba268ca6 |
| records/united-states-v-locke-intertanko-v-locke_merits_2000-03-06.md | 4bcf6a6973029c61cd4653673ce1c52f9c566d71f55b0d044ce029160a27a098 |

Reproduction script: preparation/integrate_chunk3_projections.py. Baseline snapshots and the machine-readable check receipt are retained under tmp/chunk3-projection-integration/. No source Record, brief, frozen adjudicative handoff, foundation file, state tracker or public render was modified by this task.
