"""Deterministic bounded-change verification; no Git operations."""
from pathlib import Path
import hashlib
import json
import re
import difflib

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1995'
baseline = json.loads((TERM / 'freeze/OT_1995CHUNK8_REVISION_PRESERVATION.json').read_text(encoding='utf-8'))
renames = {
    'Vera_and_consolidated_standing_1996-06-13.md': 'Vera_and_consolidated_merits_1996-06-13.md',
    'Leavitt_v_Jane_L_certiorari_1996-06-17.md': 'Leavitt_v_Jane_L_summary_merits_1996-06-17.md',
}
new_name = 'Montana_v_Egelhoff_merits_1996-06-13.md'
peers = {
    'Jaffee_v_Redmond_merits_1996-06-13.md',
    'Koon_and_Powell_v_United_States_merits_1996-06-13.md',
    'Rise_v_Oregon_merits_1996-06-14.md',
    'Melendez_v_United_States_merits_1996-06-17.md',
    'Calderon_v_Moore_summary_review_1996-06-17.md',
    'Gray_v_Netherland_merits_1996-06-20.md',
}
errors, changed, peer_diffs = [], [], {}
def sha(data): return hashlib.sha256(data).hexdigest()
def field(text, label):
    return re.search(r'^\*\*' + re.escape(label) + r':\*\* (.+)$', text, re.M).group(1)
for relative, info in baseline['files'].items():
    original = ROOT / relative
    path = original
    if original.parent == TERM / 'records' and original.name in renames:
        path = original.with_name(renames[original.name])
        if original.exists(): errors.append('Superseded Record still exists: ' + relative)
    if not path.exists():
        errors.append('Missing expected file: ' + str(path.relative_to(ROOT)))
        continue
    digest = sha(path.read_bytes())
    if digest == info['sha256']: continue
    changed.append(str(path.relative_to(ROOT)))
    if original.parent != TERM / 'records':
        errors.append('Protected non-Record changed: ' + relative)
    elif original.name not in renames and original.name not in peers:
        errors.append('Unauthorized Record changed: ' + relative)
    elif original.name in peers:
        before = (ROOT / 'tmp/chunk8_revision_before' / original.name).read_text(encoding='utf-8')
        after = path.read_text(encoding='utf-8')
        for label in ('Case and dockets', 'Event and date', 'Result'):
            if field(before, label) != field(after, label): errors.append('Peer identity/result changed: ' + original.name)
        if before.split('## Public Projection', 1)[1] != after.split('## Public Projection', 1)[1]:
            errors.append('Peer Public Projection changed: ' + original.name)
        peer_diffs[original.name] = ''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile='before', tofile='after'))
    elif original.name in renames:
        before = (ROOT / 'tmp/chunk8_revision_before' / original.name).read_text(encoding='utf-8')
        after = path.read_text(encoding='utf-8')
        old_date = re.search(r'\d{4}-\d{2}-\d{2}', field(before, 'Event and date')).group()
        now_date = re.search(r'\d{4}-\d{2}-\d{2}', field(after, 'Event and date')).group()
        if old_date != now_date: errors.append('Target event date changed: ' + original.name)

records = sorted((TERM / 'records').glob('*.md'))
if len(records) != 106: errors.append(f'Expected 106 canonical Records, found {len(records)}')
if not (TERM / 'records' / new_name).exists(): errors.append('Missing Egelhoff Record')
render = (TERM / 'render-inputs/OT_1995CHUNK8.md').read_text(encoding='utf-8')
names = re.findall(r'<!-- source-record: ([^>]+) -->', render)
if len(names) != 12 or len(set(names)) != 12: errors.append('Chunk 8 must have exactly 12 distinct Records')
if '**Stopped matters:**' in render: errors.append('Stale stopped-matter metadata')
for name in names:
    if not (TERM / 'records' / name).exists(): errors.append('Render source missing: ' + name)
receipt = {
    'status': 'PASS' if not errors else 'FAIL', 'errors': errors,
    'record_count': len(records), 'chunk8_completed_count': len(names),
    'changed_initial_files': changed, 'peer_note_diffs': peer_diffs,
    'protected_files': 'All original output files, approved brief, case-list and untargeted/nonpeer Records checked against initial SHA256.',
    'git': 'Not performed; history/hash-existence verification deferred to operator.',
}
(TERM / 'freeze/OT_1995CHUNK8_REVISION_SCOPE_CHECK.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in receipt.items() if k != 'peer_note_diffs'}, indent=2))
if errors: raise SystemExit(1)
