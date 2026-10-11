# Safeguards and their limits

This rebuild receives its own tests. None of the earlier 357-test result or historical stress-test counts is reused as certification.

The new suite exercises source/metadata extraction, exact inventory reconciliation, missing/ambiguous sources, multiple events, separate event/effective dates, source symlinks, escaped Markdown tables, strict JSON, preserved annotations and extension boundaries. Storage tests cover immutable outputs, source bytes changed with timestamps preserved, directory membership, tool/schema changes, process contention, killed writers, interrupted publication, corrupt pointers, extra/traversing files, symlinked outputs, and recovery retaining damaged evidence. Rehashed catalogue/HTML changes are checked against a fresh extraction rather than trusted because their hashes agree.

Writers use an operating-system lock. They stage and fsync files, verify the generated outputs, recheck consumed source hashes and directory membership, replace CURRENT.json atomically, and check again. A failed post-publication check restores the old pointer. Other writers must cooperate with the lock. The library does not lock Court source files: external editors may change them later, so CLI reads revalidate every time. A static browser is only a point-in-time view.

Fingerprint checks detect changes, not source authenticity or an attacker with control of the tool and every input. Recorded external URLs are not fetched. Existing repository source pointers are checked for navigable file locations, not authenticated as historical originals. Citation recognition is deliberately limited to supported reporter/statutory forms; it is not an exhaustive legal citation parser and creates no precedent-treatment labels. Existing Markdown fragments are preserved, not certified as an adjudication-safe bounded section.

Historical case IDs and operator-reviewed mappings could not be recovered. The new path-based Record identifiers and separately evidenced inventory links avoid claiming that those lost identities were reconstructed exactly. Full Record search can expose internal material and is restricted to this development area.

Production activation, stage-permitted retrieval, historical packet completeness and substantive source review remain outside this catch-up. Missing source notes and unknown metadata do not alter the Court's decisions or create a litigant default.
