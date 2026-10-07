"""Mechanical section scoping; no adjudication and no Git access."""
from pathlib import Path
import re
import hashlib
import json

term = Path(__file__).resolve().parents[1]
targets = {'VERA': 'OT1995-077', 'EGELHOFF': 'OT1995-079', 'LEAVITT': 'OT1995-082'}
receipt = {}
for kind in ('NEUTRAL', 'STONE', 'COMPARATOR'):
    source = term / 'runtime' / f'OT_1995CHUNK8_{kind}.md'
    text = source.read_text(encoding='utf-8')
    blocks = re.split(r'(?=^## OT1995-)', text, flags=re.M)
    for key, inventory in targets.items():
        chosen = [b for b in blocks if b.startswith('## ' + inventory)]
        assert len(chosen) == 1, (kind, inventory)
        out = term / 'runtime' / f'OT_1995CHUNK8_REVISION_{key}_{kind}.md'
        out.write_text(chosen[0], encoding='utf-8')
        receipt[out.name] = hashlib.sha256(out.read_bytes()).hexdigest()
(term / 'freeze' / 'OT_1995CHUNK8_REVISION_SCOPING.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print('Scoped regenerated sections for three matters; approved brief untouched.')
