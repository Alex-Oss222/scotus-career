# Deterministic tools

These tools remove clerical drift. They do not adjudicate.

- `split_chunk.py` regenerates the neutral, Stone, and historical-comparator split from an approved brief and can fail on stale copies.
- `project_render_input.py` copies each Record's bounded `Public projection` into the physically separate Render Input used by Render.
- `check_term.py` checks directory shape, public-voice leakage, Record headers, projection presence, Render Input/output correspondence, and split-file presence.

No tool may predict a Justice's vote, select a coalition, decide precedent meaning, determine whether a historical departure is justified, apply *Marks*, choose a remedy, or generate a holding. Those are legal-modeling tasks governed by `foundation/ENGINE.md`.
