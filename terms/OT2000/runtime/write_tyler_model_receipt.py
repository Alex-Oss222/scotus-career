from pathlib import Path
import hashlib

base = Path('terms/OT2000')
draft = base / 'runtime/tyler_model_working.md'
data = draft.read_bytes()
body = data.decode('utf-8')
assert 'SOURCE_PENDING' not in body
for justice in ['Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']:
    assert '### Justice ' + justice in body
assert body.count('### Justice ') == 8
for bad in ['One' + 'Drive', 'Git' + 'Hub', 'file://', 'C:/', 'C:\\']:
    assert bad not in body
expected = {
    'freeze/OT_2000CHUNK8_NEUTRAL_TYLER_REFRESH.md': 'd722dd6db2f551ae0f18f0bc924bd5d79e3a7d646d43379fccae7dfe42c7e192',
    'freeze/OT_2000CHUNK8_TYLER_INSTRUCTION_SOURCE.md': '3312713a6bf622e1e1e6277135213fca1bb6c68ddcc2d479998a7ce3c5d3b742',
    'freeze/OT_2000CHUNK8_TYLER_INSTRUCTION_VALIDATED.md': 'cf0e57a37ed796c8028adc2bb4e690a7bc9e6ff00338fc262835e5f036bb2c16',
    'sources/chunk8-prediv/teague.txt': 'a854f02ebcfa22d90ab7532d5f40169f5bdfd0ae9bbc2d698b69a31c18ace573',
}
for rel, digest in expected.items():
    assert hashlib.sha256((base / rel).read_bytes()).hexdigest() == digest
name = 'OT_2000CHUNK8_COMMITMENTS_tyler.md'
for folder in ['freeze', 'runtime']:
    path = base / folder / name
    if path.exists() and path.read_bytes() != data:
        raise SystemExit('Unexpected differing commitment; no overwrite performed')
    path.write_bytes(data)
assert (base / 'freeze' / name).read_bytes() == (base / 'runtime' / name).read_bytes()
source_paths = [
    *expected,
    'freeze/OT_2000CHUNK8_C_JUNE18_REFRESH_RECEIPT.md',
    'freeze/OT_2000CHUNK8_TYLER_BRIEF_FACTS_VALIDATED.md',
    'freeze/OT_2000CHUNK8_RECORD_SOURCE_VALIDATION_RECEIPT.md',
    'entering-law/OT_2000CHUNK8_C_HOLDINGS.md',
    'entering-law/OT_2000CHUNK8_C_STANDARDS.md',
    'entering-law/OT_2000CHUNK8_C_CURRENT.md',
    'entering-law/OT_2000CHUNK8_C_PUBLIC_WRITINGS.md',
    'entering-law/OT_2000CHUNK8_C_SOURCE_TEXT.md',
    'sources/chunk8-prediv/teague_retrieval.json',
]
lines = [
    '# Tyler independent-model freeze receipt', '',
    'Frozen commitment and runtime copy are byte-identical. All eight Associate sections cover reviewability, statutory meaning, application of prior holdings, alternative retroactivity request and remedy. This receipt verifies completed artifact checks, not legal correctness or historical reconciliation.', '',
    'The model read the clean refreshed neutral, the released exact instruction and validation, and the released attributed briefing-fact supplement before freezing. Shared new-rule status is treated as a briefing premise, not a judicial retroactivity finding. The first-filing day, exact prior appellate day and original claim inventory remain unknown in the excerpts; no statutory failure or satisfaction is invented from that limit. Reversal commitments remove the reviewed retroactivity ground without silently resolving every independent gate.', '',
    'The complete relevant Teague writings and footnotes at report pages 288–326 were read. Original author/join limits are preserved. Later actual entering-law holdings govern any divergence. No current-matter historical Supreme Court opinion, raw current-case brief/archive cover, comparator, private Stone material, other model or reconciled file, or private Record annex was read. No repository commands were run.', '',
    'Duncan is actual entering law and its former source gate is cleared. The material June 25 public-law screen remains required before June 28 assembly. These commitments are ready for fresh historical reconciliation now; no pending case outcome or Court count is supplied.', '',
    'Checks completed: eight named Associate sections; all specified components addressed; original refreshed-neutral identity; instruction source and validation identity; primary Teague source identity; paired commitment identity; absence of forbidden machine/cloud-link strings. Combined source-file hashes do not claim that unrelated entries were substantively relied on.', '',
    '## Artifact identity', '', '| Artifact | SHA-256 |', '|---|---|',
    f'| `freeze/{name}` | `{hashlib.sha256(data).hexdigest()}` |',
    f'| `runtime/{name}` | `{hashlib.sha256(data).hexdigest()}` |', '',
    '## Authorized source identities', '', '| Artifact | SHA-256 |', '|---|---|',
]
for rel in source_paths:
    lines.append(f'| `{rel}` | `{hashlib.sha256((base / rel).read_bytes()).hexdigest()}` |')
receipt = ('\n'.join(lines) + '\n').encode('utf-8')
for folder in ['freeze', 'runtime']:
    path = base / folder / 'OT_2000CHUNK8_COMMITMENTS_tyler_RECEIPT.md'
    if path.exists() and path.read_bytes() != receipt:
        raise SystemExit('Unexpected differing receipt; no overwrite performed')
    path.write_bytes(receipt)
assert draft.resolve().parent == (base / 'runtime').resolve()
draft.unlink()
print('Tyler freeze/runtime identity, eight Associate sections, source hashes and cleanup verified.')
