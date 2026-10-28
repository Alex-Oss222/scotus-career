from pathlib import Path
import hashlib

term = Path('terms/OT1998')
name = 'OT_1998CHUNK7_B_READY3_RECONCILED.md'
frozen = term / 'freeze' / name
runtime = term / 'runtime' / name
model = term / 'freeze' / 'OT_1998CHUNK7_B_INDEPENDENT_COMMITMENTS.md'
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
assert digest(model) == '8efa539396b454c5de079ee31ca0420efc9443350cb32d6b511acd1152433e16'
assert frozen.read_bytes() == runtime.read_bytes()
text = frozen.read_text(encoding='utf-8')
expected = ['Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']
sections = [
    ('El Paso', '## El Paso Natural Gas Co. v. Neztsosie — May 3, 1999'),
    ('Redmon', '## Redmon v. United States — May 10, 1999'),
    ('Saenz', '## Saenz v. Roe — May 17, 1999'),
]
receipts = []
for case, heading in sections:
    start = text.index(heading)
    end = text.find('\n## ', start + len(heading))
    body = text[start:end if end != -1 else len(text)]
    for justice in expected:
        assert ('| ' + justice + ' |') in body, (case, justice)
    receipts.append(f'- {case}: eight named Justice rows present; section bounded by its level-two heading and the next level-two heading.')
sources = ['lasalle-ZO.txt', 'lasalle-ZC.txt', 'lasalle-ZD.txt', 'el-paso-ZO.txt', 'saenz-ZO.txt', 'saenz-ZD.txt', 'saenz-ZD1.txt', 'redmon_resource.txt', 'redmon_us_opposition.txt']
lines = [
    '# OT1998 chunk 7 — B three-ready reconciliation validation', '',
    'This receipt validates the filesystem handoff only. No Git operation was used, and no repository commit, Stone assembly or term check is claimed.', '',
    '## Deterministic checks actually completed', '',
    f'- Independent freeze preserved: `{digest(model)}`.',
    f'- Reconciled freeze/runtime byte identity: PASS. SHA-256 `{digest(frozen)}`.',
    *receipts,
    '- Reported non-Stone arithmetic: El Paso 8 vacate/remand on both components; Redmon 3 reverse/search + 1 vacate/reserved application + 4 affirm = 8, with express R2 minimum-relief acceptance separately stated; Saenz 7 affirm + 1 reverse = 8.',
    '- LaSalle is expressly held; no reconciled vote is released for it. Aguirre-Aguirre and PBGC are excluded.',
    '- No Stone merits vote or author assignment is supplied.', '',
    '## Source reading and qualitative checks', '',
    'The reconciliation context read the complete Cornell texts and notes listed below, the complete Redmon lower opinion with every writing and note, and the complete official Redmon opposition. Official volume excerpts independently checked disposition and historical lineup. These are actual reading receipts, not script judgments. The legal comparison, source classification, remedy limits and Justice-specific basis are in the frozen handoff.', '',
]
for source in sources:
    path = term / 'sources' / 'chunk7-control' / source
    lines.append(f'- `{source}`: {path.stat().st_size} bytes; SHA-256 `{digest(path)}`.')
lines += ['',
    '## Pending authorized-stage work', '',
    'Fresh LaSalle neutral validation/modelling/reconciliation; event-specific law refresh where material; Stone revalidation and assembly; assignment count; Canonical Decision Records and public projection validation; generated Render Input and workspace checks; check_term. None is certified by this receipt.', '',
]
target = term / 'freeze' / 'OT_1998CHUNK7_B_READY3_RECONCILIATION_VALIDATION.md'
target.write_text('\n'.join(lines), encoding='utf-8', newline='\n')
print('PASS: ' + frozen.as_posix())
print('SHA256 ' + digest(frozen))
print(target.as_posix())
