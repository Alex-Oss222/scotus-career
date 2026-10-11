# Retained OT1994 core safeguard work

Recovered from the guard94_core agent's retained conversation on October 11, 2026. This is a passive recovery copy, not an active case-library installation.

The original work followed the full OT1994 expansion in the October 3, 2026 development session. It lived under `/workspace/scotus-career/development/case-library/` in the earlier workspace. The work was local, uncommitted and unpushed. No archive or independent saved branch was created by this agent.

## Exact retained material

- `tests/test_core_lifecycle94.py`: the complete final test module added by this agent, including its subsequent explicit `test_pilot` fixture import adjustment. Its original relative path was `development/case-library/tests/test_core_lifecycle94.py`.
- `patches/001-pilot-live-read-reviewed-inputs.patch`: the exact retained patch that bound live snapshot reads to separately reviewed inputs and reused prepared comparison content during builds/publication.
- `patches/002-pilot-shared-search-lookup.patch`: the exact retained patch, coordinated with the search agent, that delegated lookup to `pilot_views.search_matches`.

The patches preserve their original `apply_patch` format and absolute target path. They are not ordinary numbered-hunk Git patches. Do not apply them blindly: the matching original `pilot.py` and the required helper implementations must first be recovered and checked. Patch 002 specifically depends on search helpers supplied by another agent in `pilot_views.py`.

## Limits and original verification

This recovery contains no complete `pilot.py`, schema, reviewed selection or source manifest, catalogue snapshot, or authoritative Court source. Omitted code has not been invented. The test module imports `test_ot1994` and `test_pilot` and depends on the original tools, schemas, reviewed manifests and temporary repository fixture machinery; this directory cannot run those tests by itself.

In the original workspace, the nine tests in this module passed in 31.607 seconds. The same task also passed 14 existing core guards, 11 recovery tests and six term lifecycle tests, for 40 focused tests. Those are historical results, not a test run against this recovery copy. Recovery-time checking is limited to parsing the retained Python source without importing or executing its unavailable dependencies.

No active `development/case-library/` directory, integration hook or production dependency is created by this recovery. The original policy kept production integration disabled.
