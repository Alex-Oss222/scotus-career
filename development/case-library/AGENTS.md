# Case library

A read-only research aid; see README.md.

- It is not authority and not an input to Open, Run, Render or Close. Using it in a Court stage requires the user's explicit authorization.
- Keep it read-only: it must never write, move or delete repository files, and it must never list or open anything under `stone/`.
- Standard library only, Python 3.10 or later; it must keep running on Windows and Linux.
- Do not commit generated output such as `citator --md` pages unless the user asks.
- Change short names through `aliases.json`, not by editing Records or case lists.
