# Agostini: check validation

**Recorded UTC:** 2026-10-23T19:45:36.729258+00:00

**Status:** Non-Git deterministic checks passed with the verified scoped presentation exception.

Checker exit code after the scoped presentation check: 0. Holdings synchronization and all other original checks ran. The raw chunk-11 freshness check and the exact source-derived exception are reported separately in the tool output. The read-only child checks ran in-process with bytecode writes disabled.

**Operational limitation:** Git object-existence checks and commitment were not performed. No external process was launched.

**Tool:** tools/check_term.py

**Tool SHA-256:** 326c640d289d5d64df847ed573cc5999289cf691fa9a92bb814389cdb0508ca7

## Tool output

```text
Raw chunk-11 split equality failed for NEUTRAL and STONE, as expected for five scoped editorial omissions.
Scoped chunk-11 equality passed: five hash-constrained source-line operations only; all retained content, all other matters and COMPARATOR match the generated source.
Non-Git deterministic checks passed with the explicitly checked chunk-11 presentation exception: OT1996.
Git object-existence checks skipped: 47 calls; 31 distinct candidate hashes.
```
