"""Preserve manually approved initial Records; never replace an existing event.

The caller supplies a completed scoped public-audit receipt and exact filenames.
This helper checks identity only. The root must separately review Stone fidelity,
actual effective law, assignment and the private completion text before calling it.
"""
from pathlib import Path
import hashlib
import json
import sys

term = Path(__file__).resolve().parents[1]
receipt_name, *names = sys.argv[1:]
assert names and all(Path(n).name == n and n.endswith('.md') for n in names)
receipt = json.loads((term / 'freeze' / receipt_name).read_text(encoding='utf-8'))
entries = receipt.get('drafts', receipt.get('public_drafts', []))
audited = {Path(x['path']).name: x['sha256'] for x in entries}
prepared = []
for name in names:
    draft = term / 'runtime/assembly' / name
    public_path = draft.with_name('PUBLIC_DRAFT_' + name)
    public_bytes = public_path.read_bytes()
    assert hashlib.sha256(public_bytes).hexdigest() == audited[public_path.name]
    text = draft.read_text(encoding='utf-8')
    projection = text.split('## Public Projection', 1)[1].strip() + '\n'
    assert projection == public_path.read_text(encoding='utf-8').strip() + '\n'
    meta = json.loads(draft.with_suffix('.json').read_text(encoding='utf-8'))
    assert meta['record'] == name
    destination = term / 'records' / name
    assert not destination.exists(), f'No correction authority: {destination}'
    prepared.append((draft, destination, projection, meta))

saved = []
for draft, destination, projection, meta in prepared:
    destination.write_bytes(draft.read_bytes())
    public_copy = term / 'entering-law' / ('PUBLIC_' + destination.name)
    public_copy.write_text(
        '# Bounded current-term public reading copy\n\n'
        f"Authority: canonical event {meta['case']}, {meta['date']}; natural-key Record {destination.name}. "
        'The following Public Projection is copied unchanged; no audit or private material is included.\n\n'
        + projection, encoding='utf-8')
    meta['status'] = 'durably preserved; operator Git commitment pending'
    draft.with_suffix('.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    saved.append({'record': destination.name,
                  'sha256': hashlib.sha256(destination.read_bytes()).hexdigest(),
                  'public_sha256': hashlib.sha256(projection.encode('utf-8')).hexdigest(),
                  'audit_receipt': receipt_name,
                  'status': meta['status']})
log = term / 'freeze/CHUNK1_LATER_PRESERVATION.json'
previous = json.loads(log.read_text(encoding='utf-8')) if log.exists() else []
log.write_text(json.dumps(previous+saved, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(saved, ensure_ascii=False, indent=2))
