"""Task baseline for authorized Thomasson resumption; no Git or external writes."""
from pathlib import Path
import hashlib
import json
import re

term = Path(__file__).resolve().parents[1]
target = term / 'freeze/OT_1996CHUNK10_THOMASSON_TASK_BASELINE.json'
if target.exists():
    raise SystemExit('Baseline already exists; refusing to replace it.')
paths = [term / 'case-list.md']
for folder in ['records', 'briefs', 'output', 'runtime', 'freeze', 'workspace', 'render-inputs']:
    paths.extend(p for p in (term / folder).rglob('*') if p.is_file())
rows = {}
for path in paths:
    data = path.read_bytes()
    row = {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
    if path.parent.name == 'records':
        text = data.decode('utf-8-sig')
        m = re.search(r'^\*\*Event and date:\*\*.*?(\d{4}-\d{2}-\d{2})', text, re.M)
        row['event_date'] = m[1] if m else None
        result = re.search(r'^\*\*Result:\*\*.*$', text, re.M)
        row['result'] = result[0] if result else None
        if '## Public Projection' in text:
            row['public_sha256'] = hashlib.sha256(text.split('## Public Projection', 1)[1].encode()).hexdigest()
    rows[path.relative_to(term).as_posix()] = row
target.write_text(json.dumps({'purpose': 'Pre-integration byte baseline; no Git verification', 'files': rows}, indent=2), encoding='utf-8')
print(f'Saved {len(rows)} term-file hashes; {sum(k.startswith("records/") for k in rows)} preexisting Records.')
