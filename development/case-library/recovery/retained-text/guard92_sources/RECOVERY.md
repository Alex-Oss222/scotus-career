# Conversation recovery manifest — guard92_sources

Recovered October 11, 2026 into this evidence-only directory. These files are complete earlier versions transcribed from retained tool output, or from a complete retained base plus the exact patches applied by this agent. They are not a recovered final library, and this directory is not the active `development/case-library/` implementation.

The original paths were relative to `development/case-library/`; those relative paths are preserved here. The originals were read from `/workspace/scotus-career/` during the OT1992 safeguard task. The then-reported source revision was `1ded4b1cae6c8d1634365f0ef45f43270d4a88f4`. This is source provenance, not a commit containing these development files.

## Complete earlier files retained

| Relative path | Recovery basis | Vintage and limits |
|---|---|---|
| `AGENTS.md` | Complete `cat` output | OT1992-era development boundary; later changes unknown. |
| `README.md` | Complete `cat` output | OT1992 expansion complete, before the subsequent OT1992 safeguards; later changes unknown. |
| `DESIGN.md` | Complete `cat` output | Includes original core design, full OT1991 expansion and OT1992 version-4 profile; later changes unknown. |
| `STATUS.md` | Complete `cat` output | Historical October 3, 2026 status reporting 116 tests, before the subsequent OT1992 safeguards. Its counts and completion statements are historical, not current validation. |
| `schemas/historical-sources.schema.json` | Complete `cat` output | Historical-source mapping schema version 1. Later revisions unknown. |
| `tools/source_checks.py` | Complete `cat` base plus this agent's exact citation-validation and numeric/subsection patches | Final helper state observed by this agent in the OT1992 safeguard task. Later updates unknown. |
| `tests/test_source_guards.py` | Complete `cat` output | Thirteen earlier source guard tests. Later changes unknown. |
| `tests/test_source_metadata.py` | Complete original add-file patch plus this agent's exact numeric/subsection regression patch | Twelve tests at this agent's final OT1992 safeguard handoff. Later updates unknown. |
| `tests/test_ot1992.py` | Complete `cat` output | Eleven OT1992 expansion tests, before later safeguards and term support. Later changes unknown. |

No gaps inside these files were filled from summaries or newly invented implementation. Recovery notes are confined to this manifest; the earlier file contents have not been updated to describe current coverage or made compatible with a new implementation.

## Missing material

This agent does not retain complete `pilot.py`, `pilot_inputs.py`, `pilot_views.py`, `term_catalogue.py`, the core case schema, selection schemas, `SAFEGUARDS.md`, `progress.json`, the synthetic example, other tests, full selection or historical-source manifests, generated snapshots, current pointers, or later OT1993–OT1995 additions. Earlier summaries describe some of them but are not exact source and were not turned into recovered files.

Some local citation evidence and document fragments survive in the conversation, but complete source manifests do not. No fragment is presented here as a complete manifest. This recovery does not establish the final original library's state or recover its later review results.

## Checks performed now

All four recovered Python files parse with `ast.parse`; the recovered JSON schema parses as JSON. The original integration tests were not run because their importer, fixtures, reviewed manifests and original relative repository layout are missing here. Previous pass results mentioned inside the recovered documents belong to the earlier task, not this recovery.

The hashes below identify these recovered bytes for subsequent copying and comparison. They are newly computed recovery hashes, not independent original checksums, and do not prove byte-for-byte identity with the lost filesystem.

```text
ab1f837a2181e4076178c58880a68242378b1ee2d6958ac226a7aa98e3c82f90  AGENTS.md
8509ec95f34db8f84cd6efc83aaf1047ffd32bc618e3f02a9b6882ea1fa8cc79  DESIGN.md
8cf6bc7400a494e801fcf056b99cd16b6718f04c0bd5c66507c770ed0bc66013  README.md
ae482bd4a1eb47d6bc92e27f94007b745bef05787201a5ea2c65a78de567836c  STATUS.md
4137014e39331055a8517ef2a63e9fcf6d2b3d6028bb7134fbaeee2efe2be02e  schemas/historical-sources.schema.json
1fb7c34f3a6bf0904b56d1269f914b696956dbfcbafd1ae4ec27f454a9de7455  tests/test_ot1992.py
f64620e59f44664b8d1430c38b9f016e2a91eddd881bd4a039a660eac6b23832  tests/test_source_guards.py
526085fbee0931192820be7a9d156993abe4a08fca29d8faf26dc657df38ab09  tests/test_source_metadata.py
7dfc3457e94feaa007983de28c790c3dc20e909efc319479e80aa2447f813dd7  tools/source_checks.py
```
