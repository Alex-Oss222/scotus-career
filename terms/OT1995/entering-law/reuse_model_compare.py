import hashlib
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
name = 'EGELHOFF'
slice_path = BASE / f'OT_1995CHUNK8_REVISION_{name}.md'
snapshot = BASE / 'OT_1995CHUNK8_PRE_JUNE13_NEUTRAL_PROJECTION.md'
text = slice_path.read_text(encoding='utf-8-sig')
prior = snapshot.read_text(encoding='utf-8-sig')
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
prior_norm = norm(prior)
rows = []
for rel in re.findall(r'\]\((OT_1995CHUNK8_REVISION_EGELHOFF_PUBLIC_LAW/[^)]+)\)', text):
    path = BASE / rel
    public = path.read_text(encoding='utf-8-sig')
    content = re.sub(r'^## Public Projection\s*', '', public)
    rows.append({'file': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'complete_public_text_in_prior_snapshot': norm(content) in prior_norm})
out = {'snapshot_sha256': hashlib.sha256(snapshot.read_bytes()).hexdigest(), 'slice_sha256': hashlib.sha256(slice_path.read_bytes()).hexdigest(), 'public_copies': rows}
(BASE / 'OT_1995CHUNK8_EGELHOFF_REVISION_COMPARISON.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'public_count':len(rows), 'complete_matches':sum(r['complete_public_text_in_prior_snapshot'] for r in rows), 'nonmatches':[r['file'] for r in rows if not r['complete_public_text_in_prior_snapshot']]}))
