"""Check task boundaries and source/projection identities without Git."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

term = Path(__file__).resolve().parents[1]
baseline = json.loads((term / 'freeze/OT_1996CHUNK10_THOMASSON_TASK_BASELINE.json').read_text(encoding='utf-8'))['files']
allowed = {'workspace/manifest.md', 'workspace/ledger.md', 'workspace/continuity.md',
           'workspace/neutral-projection.md', 'render-inputs/OT_1996CHUNK10.md'}
changed = []
for rel, old in baseline.items():
    path = term / rel
    assert path.exists(), 'Preexisting file removed: ' + rel
    if hashlib.sha256(path.read_bytes()).hexdigest() != old['sha256']:
        changed.append(rel)
assert set(changed) <= allowed, 'Unexpected existing-file change: ' + str(set(changed) - allowed)

record = term / 'records/Thomasson_v_Perry_merits_1997-06-09.md'
doc = record.read_text(encoding='utf-8')
labels = ['**Case and dockets:**', '**Event and date:**', '**Result:**', '**Version / lineage:**']
assert all(line.startswith(label) for line, label in zip(doc.splitlines(), labels))
public = doc.split('## Public Projection', 1)[1].strip()
raw_record = record.read_bytes()
protected = raw_record.split(b'## Sources and validation status', 1)[0] + b'## Public Projection' + raw_record.split(b'## Public Projection', 1)[1]
dependency = (term / 'freeze/OT_1996CHUNK10_THOMASSON_DEPENDENCY_REVIEW.md').read_text(encoding='utf-8')
dependency_hash = re.search(r'\| New substantive prefix plus Public Projection \| `([0-9a-f]{64})`', dependency)[1]
assert hashlib.sha256(protected).hexdigest() == dependency_hash, 'Reviewed substantive Record changed'
expected = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology',
            'Holdings', 'Precedent Treatment', 'Law After Decision', 'Separate Writings',
            'Procedure After Action', 'Source Notes']
assert re.findall(r'^## (?:\d+\. )?(.+)$', public, re.M) == expected
assert not re.search(r'user-directed|simulated|research cutoff|Version 2|244a75ac|803cc547|operator|workflow', public, re.I)

render = (term / 'render-inputs/OT_1996CHUNK10.md').read_text(encoding='utf-8')
blocks = re.findall(r'<!-- source-record: ([^>]+) -->\n(.*?)(?=\n---\n|\Z)', render, re.S)
assert len(blocks) == len({name for name, _ in blocks}) == 12
assert '**Completed events:** 12.' in render
assert '**Stopped matters:**' not in render
for name, body in blocks:
    source = (term / 'records' / name).read_text(encoding='utf-8').split('## Public Projection', 1)[1].strip()
    assert source == body.strip(), 'Projection drift: ' + name

manifest = (term / 'workspace/manifest.md').read_text(encoding='utf-8')
rows = [line for line in manifest.splitlines() if line.startswith('| 199') and '| OT_1996CHUNK' in line]
assert len(rows) == 153
old_manifest = (term.parents[1] / 'tmp/thomasson_before_manifest.md').read_text(encoding='utf-8')
old_rows = [line for line in old_manifest.splitlines() if line.startswith('| 199') and '| OT_1996CHUNK' in line]
assert len(old_rows) == len(rows)
status_changes = []
for old_line, new_line in zip(old_rows, rows):
    old_cells = [x.strip() for x in old_line.strip('|').split('|')]
    new_cells = [x.strip() for x in new_line.strip('|').split('|')]
    assert old_cells[:6] + old_cells[7:] == new_cells[:6] + new_cells[7:], 'Inventory slot or metadata changed'
    if old_cells[6] != new_cells[6]:
        status_changes.append(new_cells[2])
assert status_changes == ['Thomasson v. Perry +']
chunk10 = [line for line in rows if '| OT_1996CHUNK10 |' in line]
assert len(chunk10) == 12 and all('| Completed: ' in line for line in chunk10)
thomasson = [line for line in chunk10 if '| Thomasson v. Perry +' in line]
assert len(thomasson) == 1 and thomasson[0].startswith('| 1997-06-09 |')
assert record.name in thomasson[0]

for name in ['continuity.md', 'neutral-projection.md']:
    workspace = (term / 'workspace' / name).read_text(encoding='utf-8')
    assert 'Coverage: **118 Court events and 3 admitted sources**' in workspace
    assert 'cursor: **1997-06-16**' in workspace
    assert 'Thomasson remains unadjudicated' not in workspace
    assert 'Thomasson v. Perry remains stopped' not in workspace
    for block in ['Opinion Topology', 'Holdings', 'Precedent Treatment', 'Law After Decision', 'Procedure After Action']:
        match = re.search(r'^## (?:\d+\. )?' + re.escape(block) + r'\s*\n(.*?)(?=^## |\Z)', public, re.M | re.S)
        assert match and match[1].strip() in workspace, name + ' missing copied ' + block

links = []
for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc):
    if re.match(r'[a-z]+://', raw, re.I):
        continue
    path_part = unquote(raw.split('#', 1)[0].strip('<>'))
    destination = (record.parent / path_part).resolve() if path_part else record
    assert destination.exists(), 'Unresolved local Record link: ' + raw
    links.append(raw)

existing_records = [key for key in baseline if key.startswith('records/') and key.endswith('.md')]
result = {
    'status': 'passed',
    'preexisting_records_unchanged': len(existing_records),
    'new_record': record.name,
    'new_record_sha256': hashlib.sha256(record.read_bytes()).hexdigest(),
    'dependency_review_substantive_binding': dependency_hash,
    'all_frozen_handoffs_unchanged': True,
    'briefs_case_list_and_outputs_unchanged': True,
    'existing_files_changed': changed,
    'render_input_events': len(blocks),
    'public_projection_identity': 'all twelve exact',
    'manifest_events': len(rows),
    'manifest_status_changes_only': status_changes,
    'chunk10_completed': len(chunk10),
    'chunk10_stopped': 0,
    'chronology_cursor': '1997-06-16',
    'new_record_local_links_resolve': len(links),
    'git_verification': 'not performed; no Git commands permitted',
}
target = term / 'freeze/OT_1996CHUNK10_THOMASSON_STRUCTURAL_VALIDATION.json'
target.write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
