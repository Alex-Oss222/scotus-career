from pathlib import Path
import hashlib

base = Path('terms/OT2000')
name = 'OT_2000CHUNK8_COMMITMENTS_kdm.md'
frozen = base / 'freeze' / name
data = frozen.read_bytes()
working = base / 'runtime' / name
if working.exists() and working.read_bytes() != data:
    raise SystemExit('Unexpected differing runtime handoff; no overwrite performed')
working.write_bytes(data)
assert working.read_bytes() == data
neutral = base / 'freeze/OT_2000CHUNK8_NEUTRAL_KDM_REFRESH.md'
assert hashlib.sha256(neutral.read_bytes()).hexdigest() == '2b3e28def3e41f30913e7d8e9e2f62523ec5efbd7ab6362470e647d577913bb9'
public = base / 'entering-law/OT_2000CHUNK8_JUNE18_PUBLIC_FINAL.md'
assert hashlib.sha256(public.read_bytes()).hexdigest() == '4f5f290c2387cb930be8bea25c69f77f3e982c1cc712cd86cc53db138808666b'
body = data.decode('utf-8')
for justice in ['Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']:
    assert '### Justice ' + justice in body
assert body.count('### Justice ') == 8
for bad in ['One' + 'Drive', 'Git' + 'Hub', 'file://', 'C:/', 'C:\\', 'https://']:
    assert bad not in body
files = [
    'freeze/OT_2000CHUNK8_NEUTRAL_KDM_REFRESH.md',
    'freeze/OT_2000CHUNK8_NEUTRAL_B_REFRESH_RECEIPT.md',
    'freeze/OT_2000CHUNK8_NEUTRAL_B_SOURCE_KDM.md',
    'entering-law/OT_2000CHUNK8_B_RELIGION.md',
    'entering-law/OT_2000CHUNK8_B_STANDARDS.md',
    'entering-law/OT_2000CHUNK8_B_PRIOR_PUBLIC.md',
    'entering-law/OT_2000CHUNK8_B_CURRENT_GOOD_NEWS.md',
    'entering-law/OT_2000CHUNK8_B_CURRENT_CHILDREN.md',
    'entering-law/OT_2000CHUNK8_JUNE18_PUBLIC_FINAL.md',
]
lines = [
    '# K.D.M. independent-model freeze receipt', '',
    'The frozen commitment and runtime copy are byte-identical. All eight Associate sections and the three component commitments were checked. This receipt verifies artifacts and stated boundaries, not the correctness of a legal judgment or historical reconciliation.', '',
    'The refreshed neutral and final June 18 public-law files retain the SHA-256 values in the clean neutral refresh receipt. No neutral/source file was written by this modeling task. No current-case historical Supreme Court disposition, comparator, private Stone position, other model, reconciled file or raw Record annex was opened. No authorship or final Court disposition was selected. General model knowledge is not claimed to have been erased.', '',
    'K.D.M. uses actual Freiler law; the former dependency is discharged. Fresh historical reconciliation is the next stage. The formal regulatory-decree scope, equal eligibility versus entitlement distinction, stipulated adequacy and safety, absence of an actual secular onsite comparator, and all published entering-law qualifications are explicit.', '',
    'Checks completed: eight named individual commitments; all three components covered; runtime identity; neutral refresh identity; final June 18 public-law identity; absence of machine/cloud-link strings in the commitment. No repository commands were run.', '',
    '## Artifact identity', '',
    '| Artifact | SHA-256 |', '|---|---|',
    f'| `freeze/{name}` | `{hashlib.sha256(data).hexdigest()}` |',
    f'| `runtime/{name}` | `{hashlib.sha256(data).hexdigest()}` |', '',
    '## Authorized source identities', '',
    'For combined reading files, only the K.D.M.-relevant selections identified in the commitment were used. Hashing the containing file does not assert that unrelated entries were substantively read.', '',
    '| Artifact | SHA-256 |', '|---|---|',
]
for rel in files:
    lines.append(f'| `{rel}` | `{hashlib.sha256((base/rel).read_bytes()).hexdigest()}` |')
receipt = ('\n'.join(lines) + '\n').encode('utf-8')
for folder in ['freeze', 'runtime']:
    path = base / folder / 'OT_2000CHUNK8_COMMITMENTS_kdm_RECEIPT.md'
    if path.exists() and path.read_bytes() != receipt:
        raise SystemExit('Unexpected differing receipt; no overwrite performed')
    path.write_bytes(receipt)
print('KDM freeze/runtime identity and neutral-source hashes verified.')
