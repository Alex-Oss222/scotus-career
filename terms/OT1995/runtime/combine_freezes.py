"""Assemble stage indexes/copies without changing the group handoffs."""
from pathlib import Path
import hashlib
import json
import sys

term = Path(__file__).resolve().parents[1]
stage = sys.argv[1]
assert stage in {'NEUTRAL_VALIDATED', 'COMMITMENTS', 'RECONCILED'}
parts, hashes = [], {}
for group in 'ABC':
    path = term / 'freeze' / f'OT_1995CHUNK1_{group}_{stage}.md'
    assert path.is_file() and path.stat().st_size > 100
    hashes[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    if stage == 'COMMITMENTS':
        runtime = term / 'runtime' / path.name
        assert runtime.read_bytes() == path.read_bytes(), f'Working/freeze mismatch: {path.name}'
    parts.append(path.read_text(encoding='utf-8'))
body = f'# OT1995 chunk 1 — {stage}\n\n'
body += 'Durably preserved stage handoffs; operator Git commitment pending. The group source/read receipts and control record disclose the context limitation and exact reading scopes. No Git operation has been performed.\n\n'
body += '\n\n---\n\n'.join(parts)
out = term / 'freeze' / f'OT_1995CHUNK1_{stage}.md'
out.write_text(body, encoding='utf-8')
if stage != 'NEUTRAL_VALIDATED':
    (term / 'runtime' / out.name).write_bytes(out.read_bytes())
(term / 'freeze' / f'OT_1995CHUNK1_{stage}_HASHES.json').write_text(json.dumps(hashes, indent=2) + '\n', encoding='utf-8')
print(f'{out.name}: assembled three unchanged group handoffs; SHA-256 manifest saved.')
