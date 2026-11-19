# OT1997 chunk 4 integration preparation

Derived aggregation only. Original scoped freezes remain the authorities. No workspace files were written by aggregation.

| Kind | Source | SHA-256 |
|---|---|---|
| COMMITMENTS | OT_1997CHUNK4_A_COMMITMENTS.md | `174891a3e818d5635f987161f5c10f01366a4c6e1be6878a87d9a703d5c8d976` |
| COMMITMENTS | OT_1997CHUNK4_B_COMMITMENTS.md | `29948191f51abdac746a652c7f05026827172f765e95c34f786942b2417a3733` |
| COMMITMENTS | OT_1997CHUNK4_NCUA_COMMITMENTS.md | `29e280cfa878a27a28e15fa4942decb58ba7e5447b17790ee86a7007d8b4bca9` |
| RECONCILED | OT_1997CHUNK4_A_RECONCILED.md | `a5d7516885dfa53f79a224a7f22f720fa4c832f4ab061f84eac743e0a23e31d1` |
| RECONCILED | OT_1997CHUNK4_B_RECONCILED.md | `1f6cd3df9c6f17af5adfb7c5772e0c1606c7acf033f180b5595ddf8b2670bfb2` |
| RECONCILED | OT_1997CHUNK4_NCUA_RECONCILED.md | `8df1ea7ef8f64366bc43b7782998aefabdb260af7a08180358f1964ee42ac89e` |

## Prepared workspace integration

`python terms/OT1997/tools/integrate_chunk4.py check` builds the proposed cumulative workspace replacements in memory after the manifest rebuild. `apply` writes them only after all thirteen chunk-4 manifest rows link completed Records and the term contains exactly fifty-one Records (fifty Court events and one admitted source).

The script preserves earlier law, published positions, opening authority paragraphs, institutional tables, and all five opening carryover rows. It copies each new full Public Projection with heading and relative-link relocation, copies any exact bounded `Additional Published Continuity` section, and carries procedural terms from Public Action and Procedure After Action. No other private or audit section enters either projection.

It updates only designated status/scope paragraphs and the manifest pending-stage footer; adds both Arteaga petitions and the March 16 paid-compliance condition; preserves Brown; and specifies pre-March-3 law for the independent Kawaauhau v. Geiger peer. All existing source blocks and qualifications remain intact.

No Git command is used. All writes stay within terms/OT1997 or tmp. No top-level stone directory access occurs. Git-object verification remains deferred as stated in the tooling controls. No public render is generated.

## Preparation verification and remaining commands

Targeted status, scope, pending-stage, section-count and preservation transformations were exercised in memory against both existing workspace projections and the actual Arteaga Public Projection. The manifest transformation preserved its existing content and added exactly two Arteaga pending-stage rows. This was a preparation check, not the final thirteen-Record integration check. No workspace file was written.

After all thirteen Records are final, run these commands from the repository root:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python terms/OT1997/tools/restricted_tools.py ledger
python terms/OT1997/tools/restricted_tools.py manifest
python terms/OT1997/tools/integrate_chunk4.py check
python terms/OT1997/tools/integrate_chunk4.py apply
```

Then generate the chunk Render Input with the original builder through `restricted_tools.py render`, supplying all thirteen explicit Record paths, and run `restricted_tools.py check`. The integration's `check` is a no-write preflight; `apply` is deliberately a one-time replacement and refuses stale source wording or duplicate Arteaga footer rows. Do not run it a second time after successful application. Re-run `integrate_chunk4.py aggregate` only if an authoritative scoped freeze changed before final integration; source hashes document the exact copied bytes.
