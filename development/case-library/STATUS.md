# Case-library rebuild status

**Caught up through the closed OT1995 term. Production integration: disabled.**

Updated October 11, 2026. This is a newly tested version-2 rebuild, not recovery of the lost original implementation or a new Court audit. Source baseline: `672abecfcb0a47c98e47b29ff02104f8b9ad6e74`. Later upstream case-index formatting is not an adjudication change; the importer also tests separated chunk tables.

[Open the catalogue browser](builds/94795938180682ff581c7ddeca4921514fd4b8a90365224ea0d5bb4bcf09d0fb/index.html) · [Desktop preview](review/browser-desktop.png) · [Validation report](review/rebuild-validation.json)

| Term | Inventory rows mapped | Court events | Admitted sources | Total Records |
|---|---:|---:|---:|---:|
| OT1991 | 124 | 125 | 1 | 126 |
| OT1992 | 123 | 123 | 3 | 126 |
| OT1993 | 95 | 95 | 1 | 96 |
| OT1994 | 99 | 99 | 2 | 101 |
| OT1995 | 115 | 116 | 10 | 126 |
| **Total** | **556** | **558** | **17** | **575** |

All ten OT1995 chunks and earlier in-place corrections are included from current Records. Bowersox has two events under one scheduled row. Coleman's supplemental OT1991 petition is retained outside scheduled inventory. Twelve final OT1995 carryovers remain pending underlying matters, separately from completed events. All 556 inventory rows resolve with explicit metadata/manifest evidence and six retained exact-quote exceptions; this is not automatic case-identity merging.

The new index contains 3,248 distinct recognized citation strings / 8,154 mentions and 6,070 reference occurrences: 4,004 existing repository pointers, 1,987 external pointers and 79 missing or unsupported locations. These are occurrences, not unique verified documents. The 362 Record notes retain source limitations, missing locations, chronology qualifiers and supplemental status. All event dates have observed evidence; Coleman's supplemental petition has no explicit ledger effective date, which remains null. A URL or file hash does not establish historical authenticity or legal force.

## Fresh validation

- All **99 new tests passed**, including seven Chromium tests. Archived historical tests are not counted.
- Twelve additional targeted stress runs passed: six rounds with three concurrent writers each, three killed-writer recoveries and three injected publication-race rollbacks.
- The real browser exposed all 575 Records, including all 126 OT1995 Records. All 19,372 local file links and 581 same-page anchors resolve. All 270 term/chunk/type filter combinations, five searches, JavaScript-disabled browsing and four viewport widths passed. No automatic external requests or browser errors occurred. External URLs and cross-file Markdown fragments were not remotely/semantically verified.
- Current-source validation passes. An identical build reuses the same snapshot. The catalogue binds 658 consumed source/tool/schema/input fingerprints and relevant directory membership.
- All 7,758 protected tracked files match the pre-rebuild hashes. Authoritative Records, sources, state, foundations, renders, freezes and production tools are unchanged. Only the isolated development area and its root instruction boundary were edited.

Snapshot: `94795938180682ff581c7ddeca4921514fd4b8a90365224ea0d5bb4bcf09d0fb`. This is a point-in-time report; `library.py status` validates and reports the live pointer.

## What remains outside catch-up

The original case-ID registry, reviewed historical-document mappings and snapshot history were unavailable. Recovered older files and patches are preserved separately; the new path-based Record IDs do not pretend to be a lossless migration. Historical packet completeness, unresolved source research, full legal citation recognition, cross-term case-identity curation, later-treatment review and stage-specific retrieval remain unimplemented or unreviewed.

No Open / Run / Render / Close hook was added. A separate integration readiness review and later explicit authorization are required before any Court stage uses a derived handoff. The current library is usable for isolated development navigation now.
