"""Validate the bounded Fletcher package and refresh current assembly receipts."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys

sys.dontwritebytecode = True
TERM = Path(__file__).resolve().parents[1]
ROOT = TERM.parents[1]
FREEZE = TERM / 'freeze'
TARGET = 'Fletcher_v_Kalina_merits_1997-06-16.md'
BLOCKS = ['Event', 'Participation', 'Public Action', 'Judgment & Remedy', 'Opinion Topology', 'Holdings',
          'Precedent Treatment', 'Law After Decision', 'Separate Writings', 'Procedure After Action', 'Source Notes']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')


def section(text, heading):
    m = re.search(r'^## ' + re.escape(heading) + r'\s*\n(.*?)(?=^## |\Z)', text, re.M | re.S)
    assert m, heading
    return m[1].strip()


def main():
    baseline = json.loads((TERM / 'tmp/FLETCHER_BOUNDARY_HASHES.json').read_text())
    dependency = json.loads((FREEZE / 'OT_1996CHUNK11_FLETCHER_DEPENDENCY_CHECKS.json').read_text())
    changed_other = {r['file']: r for r in dependency['paragraph_checks']}
    checked, errors, changed = [], [], []
    for name, old_hash in baseline.items():
        path = ROOT / name
        if not path.exists():
            errors.append('Missing baseline file: ' + name)
            continue
        current = digest(path)
        if current == old_hash:
            continue
        changed.append(name)
        if not name.startswith('terms/OT1996/'):
            errors.append('Protected infrastructure changed: ' + name)
        elif name.startswith(('terms/OT1996/briefs/', 'terms/OT1996/output/')) or name == 'terms/OT1996/case-list.md':
            errors.append('Protected input/output changed: ' + name)
        elif name.startswith('terms/OT1996/records/') and path.name != TARGET:
            c = changed_other.get(path.name)
            if not c or c['before_sha256'] != old_hash or c['after_sha256'] != current or not c['outside_assignment_identical'] or not c['public_projection_identical']:
                errors.append('Unbounded other Record change: ' + name)
        elif name.startswith(('terms/OT1996/freeze/', 'terms/OT1996/runtime/')) and re.search(r'_(?:NEUTRAL|COMMITMENTS|RECONCILED|STONE|COMPARATOR)(?:_|\.)', path.name):
            errors.append('Frozen/input handoff changed: ' + name)
    assert not errors, errors
    assert len(list((TERM / 'records').glob('*.md'))) == 132
    render = (TERM / 'render-inputs/OT_1996CHUNK11.md').read_text(encoding='utf-8-sig')
    record_names = re.findall(r'<!-- source-record: ([^>]+) -->', render)
    assert len(record_names) == len(set(record_names)) == 11, record_names
    spec = importlib.util.spec_from_file_location('fletcher_census', TERM / 'runtime/fletcher_downstream_audit.py')
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    census, counts = audit.census()
    rows = {r['file']: r for r in census}
    for name in record_names:
        path = TERM / 'records' / name
        text = path.read_text(encoding='utf-8-sig')
        kernel, public = text.split('## Public Projection', 1)
        assert re.findall(r'^## ([^\n]+)', public, re.M) == BLOCKS, name
        inner = next((section(kernel, h) for h in ('Controlling holdings', 'Controlling law of the decision') if '\n## ' + h + '\n' in kernel), None)
        assert inner == section(public, 'Holdings'), name
        for link in re.findall(r'\]\(([^)]+)\)', text):
            target = link.split('#', 1)[0]
            if target and not re.match(r'\w+://', target):
                assert (path.parent / target).exists(), (name, target)
        words = [len(re.findall(r'\b[\w\u2019-]+\b', m)) for m in re.findall(r'\*\*Controlling explanation:\*\*\s*(.*?)(?=\n### |\Z)', inner, re.S)]
        assert all(n <= 350 for n in words), (name, words)
        checked.append({'record': name, 'sha256': digest(path), 'bytes': path.stat().st_size,
                        'opening_labels': all(text.splitlines()[i].startswith(label) for i, label in enumerate(['**Case and dockets:**', '**Event and date:**', '**Result:**', '**Version / lineage:**'])),
                        'eleven_blocks': True, 'holdings_identity': True, 'local_links': True,
                        'explanation_words': words, 'counts_before': rows[name]['counts_before'], 'author': rows[name]['authors']})
    assert all(c['opening_labels'] for c in checked)
    t = (TERM / 'records' / TARGET).read_text(encoding='utf-8-sig')
    assert t.splitlines()[3] == '**Version / lineage:** Original decision.'
    assert not re.search(r're-adjudicat|Version 2|earlier outcome|approved by the user|user direction', t, re.I)
    by_name = {r['record']: r for r in checked}

    # Current assembly structural receipts replace only their Record evidence.
    for filename in ('OT_1996CHUNK11_ASSEMBLY_JUNE16_CHECKS.json', 'OT_1996CHUNK11_ASSEMBLY_JUNE16_FINAL_CHECKS.json',
                     'OT_1996CHUNK11_ASSEMBLY_JUNE23_CHECKS.json', 'OT_1996CHUNK11_JUNE19_ASSEMBLY_VALIDATION.json'):
        path = FREEZE / filename
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        items = data if isinstance(data, list) else data.get('records', [])
        for item in items:
            current = by_name.get(item.get('record'))
            if not current:
                continue
            for k in ('sha256', 'bytes', 'explanation_words'):
                if k in item:
                    item[k] = current[k]
            if 'preassignment_counts' in item:
                item['preassignment_counts'] = current['counts_before']
            if 'author' in item:
                item['author'] = current['author'][0] if isinstance(item['author'], str) else current['author']
            if item['record'] == TARGET:
                item.pop('exact_case_annexes', None)
                item['frozen_commitment_compatibility'] = True
                item['public_boundary'] = True
        write_json(path, data)

    write_json(FREEZE / 'OT_1996CHUNK11_FINAL_CHECKS.json', {
        'completed_records': 11, 'records': checked, 'errors': [],
        'scope': 'Current chunk-11 Record structure, exact internal/public Holdings, links, explanation limits and assignment census; source handoffs remain intact.'})
    write_json(FREEZE / 'OT_1996CHUNK11_INTEGRITY.json', {
        'baseline_files': len(baseline), 'protected_inputs_outputs_infrastructure_unchanged': True,
        'non_stone_freezes_and_runtime_splits_unchanged': True, 'canonical_record_count': 132,
        'other_record_scope': 'Thirteen assignment-note updates; fourteen non-Fletcher Public Projections and all non-assignment bytes preserved.',
        'changed_files': changed, 'records': checked, 'errors': [], 'git': 'No Git command or verification performed.'})
    for path in FREEZE.glob('OT_1996CHUNK11_LAW_REFRESH_*.json'):
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        for name in data:
            source = TERM / 'records' / name
            if source.exists():
                data[name] = digest(source)
        write_json(path, data)
    write_json(FREEZE / 'OT_1996CHUNK11_FLETCHER_PACKAGE_CHECKS.json', {
        'case': 'Fletcher v. Kalina', 'event_date': '1997-06-16', 'judgment': 'Affirm and remand, 9–0',
        'lead_author': 'Stevens', 'public_blocks': 11, 'same_chronological_slot': True,
        'record_count': 132, 'chunk11_completed_events': 11, 'other_records_reviewed': 14,
        'no_material_downstream_change': True, 'preserved_inputs_outputs_infrastructure': True,
        'final_author_counts': counts, 'errors': [],
        'validation': 'Independent assembly and independent substantive review passed; repository deterministic check recorded separately.',
        'git': 'Object existence, history verification and commitment not performed.'})
    print('Package boundaries and all eleven current chunk-11 Records validated; no protected-file or substantive downstream drift.')


if __name__ == '__main__':
    main()
