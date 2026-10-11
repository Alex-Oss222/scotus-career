# Rebuild design

The catalogue is a pointer index. JSON Schema version 2 describes generated Record entries, explicit inventory mappings, historical/source references, citation mentions, and separate operator annotations. Record IDs are deterministic from canonical repository paths: in-place corrections keep identity; renames require explicit review. Matching a name, docket, or citation does not merge cases or establish a legal relationship.

Court-event Records and admitted-source Records have separate kinds. Inventory rows remain source rows, including their exact captions, dockets and area-of-law metadata. Multiple events can point to one inventory row; pending underlying matters remain separate closing carryovers. Event dates and explicit ledger effective dates are distinct. Unknown dates remain null. Filename or same-day ordering never establishes intervening law.

Historical URLs are locally observed pointers, not remotely verified documents. Citation occurrences point to exact source lines; they do not establish adoption, treatment, or controlling force. Full simulation Records are mixed material, not approved inputs for restricted stages. Explicit source gaps and unverified mappings remain visible.

Operator annotations live in inputs/annotations.json, separate from generated files. Aliases, notes and named extensions survive regeneration. Core fields reject unknown keys; extensions cannot override core behavior or integration flags. The rebuilt identities and mappings are new and cannot be represented as a lossless migration from the unavailable original manifests.

Writers acquire an exclusive process lock, collect and validate inputs, stage immutable outputs, recheck source bytes and directory membership, and atomically replace CURRENT.json only after verification. Live CLI reads check fingerprints and regenerate expected metadata/views to detect consistent but incorrect edits. Recovery preserves damaged pointer bytes and old build directories. Static HTML cannot check current source freshness and displays that limitation.

Ordinary updates do not change schema_version. No source files are copied as a new PDF corpus. No tools decide legal meaning. Incremental refresh after completed chunks and full reconciliation after term close remain a proposal for later integration, not an active hook.
