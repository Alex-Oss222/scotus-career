# OT1999 chunk 7 boundary and freeze checks

**Pass:** final.
**Checked:** 2026-11-03 21:02:14 UTC.
**Result:** PASS for the stated completed checks.

## Scope and limits

This is a deterministic boundary, byte-identity, structure and link check. It makes no legal, vote, coalition, merits, assignment-fit or historical-source conclusion. No Git command was run and no Git provenance or commit existence was checked. No read, listing, search or write entered the locked top-level private directory. Repository-wide and operating-system-wide write activity was not audited.

The checker reads only explicitly listed protected files, named governing files, scoped chunk 7 artifacts and source subdirectories, current term workspace files, and relative-link destinations reached from the new Records. It writes this report; its implementation is an ignored scratch file. No public render is created. Work in progress is checked as found, without changing Records or handoffs.

## Protected-file preservation

SHA-256 was recomputed for all 125 paths in the supplied pre-Run snapshot. The snapshot itself is the baseline; this is not a repository-history comparison.

| Protected group | Files |
|---|---:|
| terms/OT1999/records | 77 |
| terms/OT1999/briefs | 10 |
| terms/OT1999/output | 7 |
| state | 22 |
| foundation | 9 |

## Runtime and freeze preservation

`python -B tools/split_chunk.py terms/OT1999/briefs/OT_1999CHUNK7.md --check` returned exit status 0: `OK: 12 matters; runtime split is current`.

All six frozen/runtime pairs were compared byte for byte. Each aggregate commitment and reconciliation file was checked for exactly one exact-content inclusion of each scoped A and B original after CRLF/LF normalization. The aggregate files use CRLF where the scoped originals use LF; this changes line-ending bytes but no text. The four original scoped digests were compared with the values announced at stage completion.

| Frozen artifact | SHA-256 |
|---|---|
| COMMITMENTS_A | `0b6a2424d4f763343788fce4c93b8c03de77ed75306fc7fec2e98ce1b140004d` |
| COMMITMENTS_B | `f6fb7e8ff97e781bc8ff21519e629869f977d1b7bf8b259386dfb5718045c382` |
| RECONCILED_A | `6582780860fe9854a9ac0236cbe946214f20b09954542a2d3ac146e441b072e2` |
| RECONCILED_B | `dbc36699db629bcb80aa571d2362b968f9c2e131394e99b867b52631bf40f3fd` |
| COMMITMENTS | `d6de864f2303ca05fe683db08a17e30e0098b8b33738799aa04b4eee42c666a8` |
| RECONCILED | `5ef6650dbe55ded74b72d227bd351dd6599aa230bdeff7e36c381b6f82de8a35` |

The neutral compilation was checked for its five expected source markers in A, Ohler, Raleigh, B, Troxel order and for exactly one exact-content copy of each corresponding frozen packet after CRLF/LF normalization. Neutral A, Ohler and Raleigh have the same line-ending-only distinction; neutral B and Troxel also match as raw byte substrings. The raw neutral runtime split is separately validated against the approved brief; it is not expected to equal the validated neutral compilation.

## Record and link checks

12 new Records were present. For each, the four required opening labels, ISO event date, single Public Projection boundary, eleven exact block headings and order, and verbatim canonical-to-public Holdings text were checked. Labeled controlling-explanation bodies were counted by whitespace-delimited words against the ordinary 350-word ceiling. No special length designation is silently assumed.

| New Record | Controlling-explanation words |
|---|---|
| castillo-v-united-states_merits_2000-06-05.md | 225 |
| eisenberg-v-montgomery-county-public-schools_merits_2000-05-30.md | 224, 202, 215 |
| harris-trust-and-savings-bank-v-salomon-smith-barney_merits_2000-06-12.md | 299 |
| hartford-underwriters-v-union-planters-bank_merits_2000-05-30.md | 284 |
| mixon-v-ohio_merits_2000-06-05.md | 158, 229 |
| ohler-v-united-states_merits_2000-05-22.md | 270 |
| raleigh-v-illinois-department-of-revenue_merits_2000-05-30.md | 314 |
| sims-v-apfel_merits_2000-06-05.md | 239 |
| troxel-v-granville_merits_2000-06-05.md | 189 |
| united-states-v-barrett_merits_2000-05-22.md | 242, 87 |
| united-states-v-hubbell_merits_2000-06-05.md | 258 |
| vermont-agency-v-united-states-ex-rel-stevens_merits_2000-05-22.md | 211, 222 |

122 relative Markdown-link occurrences in the new Records were checked for file existence, with fragments checked when present. Destinations outside the repository or in the locked directory are rejected before file access.

181 current chunk 7 artifact/source and workspace files were scanned for actual prohibited hosted URLs, file URLs and local absolute Markdown destinations. The scan includes source file byte strings decoded for text; it is not a semantic audit of compressed PDF streams or remote pages. The pre-Run hash inventory does not include all old workspace/source files, so a prohibited-link finding there would require separate attribution before claiming it was newly introduced.

## Outstanding scope

All twelve new Records were present for this pass. The parent operator separately performs ledger, manifest, generated Render Input identity and whole-term checks using its no-Git validation path. This report does not substitute for those checks.

## Discrepancies

No discrepancy found within the checks and scope stated above.
