"""Scoped Vey resumption checks. Never execute Git; never traverse locked inputs."""
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1996'
PREFIX = TERM / 'freeze/OT_1996CHUNK6_68_RESUMPTION'
BASE = Path(str(PREFIX) + '_BASELINE.json')

def digest(data):
    return hashlib.sha256(data).hexdigest()

def load_tool(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'tools' / (name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def baseline():
    if BASE.exists():
        raise SystemExit('Baseline already exists; refusing to overwrite')
    files = [TERM / 'case-list.md']
    for folder in ['briefs', 'output', 'records', 'render-inputs', 'workspace']:
        files.extend(sorted((TERM / folder).glob('*.md')))
    for folder in ['foundation', 'state']:
        files.extend(sorted((ROOT / folder).rglob('*')))
    result = {'files': {}, 'later_records': {}}
    for p in files:
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        data = p.read_bytes()
        result['files'][rel] = digest(data)
        if p.parent == TERM / 'records':
            text = data.decode('utf-8')
            event = re.search(r'^\*\*Event and date:\*\*.*?(\d{4}-\d{2}-\d{2})', text, re.M)
            if event and event[1] >= '1997-04-14':
                result['later_records'][rel] = text
    BASE.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(f'Baseline: {len(result["files"])} files; {len(result["later_records"])} later Records')

def ledger():
    old = (TERM / 'workspace/ledger.md').read_text(encoding='utf-8')
    cached = {}
    for line in old.splitlines():
        if not line.startswith('| ') or '../records/' not in line:
            continue
        cells = [x.strip() for x in line.strip('|').split('|')]
        filename = re.search(r'\(../records/([^)]*)\)', line)[1]
        cached[filename] = (int(cells[0]), cells[-2])
    mod = load_tool('rebuild_ledger')
    mod.git_added = lambda root, path: cached.get(path.name, (2**63 - 1, 'uncommitted'))
    sys.argv = ['tools/rebuild_ledger.py', 'OT1996']
    mod.main()
    p = TERM / 'workspace/ledger.md'
    text = p.read_text(encoding='utf-8').replace(
        'Generated from canonical Records in Git commitment order. Records control if this index conflicts with them.',
        'Generated from canonical Records. Existing commitment order and first-record identifiers are preserved from the prior ledger without Git verification; the newly written Vey Record is appended as uncommitted for operator review. Effective order is in the manifest. Records control if this index conflicts with them.')
    p.write_text(text, encoding='utf-8')
    Path(str(PREFIX) + '_LEDGER_RECEIPT.json').write_text(json.dumps({
        'tool': 'tools/rebuild_ledger.py', 'git_commands_executed': 0,
        'cached_existing_rows': len(cached),
        'method': 'Run original main with git_added replaced by prior-ledger order and provenance; new Record uncommitted. No provenance verified.'
    }, indent=2) + '\n', encoding='utf-8')

def check():
    mod = load_tool('check_term')
    skipped = []
    def defer_git(root, sha):
        skipped.append(sha)
        return True  # Bypass only; receipt explicitly does not certify existence.
    mod.git_object_exists = defer_git
    original_run = subprocess.run
    def forbid_git(args, *a, **kw):
        if isinstance(args, (list, tuple)) and Path(str(args[0])).stem.lower() == 'git':
            raise RuntimeError('Git execution forbidden')
        return original_run(args, *a, **kw)
    subprocess.run = forbid_git
    sys.argv = ['tools/check_term.py', 'OT1996']
    stream = io.StringIO()
    exit_code = 0
    with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
        try:
            mod.main()
        except SystemExit as exc:
            exit_code = exc.code or 0
    subprocess.run = original_run
    report = stream.getvalue()
    report += '\nGit-object existence checks DEFERRED by explicit user instruction; bypass is not a passed provenance check.\n'
    Path(str(PREFIX) + '_CHECK.txt').write_text(report, encoding='utf-8')
    Path(str(PREFIX) + '_CHECK.json').write_text(json.dumps({
        'non_git_exit_code': exit_code, 'git_commands_executed': 0,
        'deferred_git_object_identifiers': sorted(set(skipped)),
        'deferred_count': len(skipped),
        'original_checker_sha256': digest((ROOT / 'tools/check_term.py').read_bytes()),
        'method': 'Original check_term main; git_object_exists bypassed and all subprocess Git commands forbidden. No assertion of Git-object existence.'
    }, indent=2) + '\n', encoding='utf-8')
    print(report)
    if exit_code:
        raise SystemExit(exit_code)

def verify():
    baseline_data = json.loads(BASE.read_text(encoding='utf-8'))
    allowed = {
        'terms/OT1996/workspace/manifest.md',
        'terms/OT1996/workspace/ledger.md',
        'terms/OT1996/workspace/continuity.md',
        'terms/OT1996/workspace/neutral-projection.md',
        'terms/OT1996/render-inputs/OT_1996CHUNK6.md',
    } | set(baseline_data['later_records'])
    changed, errors = [], []
    for rel, expected in baseline_data['files'].items():
        p = ROOT / rel
        if not p.exists() or digest(p.read_bytes()) != expected:
            changed.append(rel)
            if rel not in allowed:
                errors.append('Protected file changed: ' + rel)
    replacements = {
        'Chandler_v_Miller_merits_1997-04-15.md': (
            'Vey has no completed event and supplies no law.',
            'The April 14 Vey decision concerning financial leave and prospective extraordinary-writ filing conditions changes no Fourth Amendment, candidacy, or remedial premise here.'),
        'Blessing_v_Freestone_merits_1997-04-21.md': (
            'No uncompleted Vey action supplies law or procedure.',
            'The April 14 Vey decision concerning financial leave and prospective extraordinary-writ filing conditions changes no Title IV-D, \u00a71983, statutory-transition, or remedial premise here.'),
        'New_Mexico_Department_of_Human_Services_v_Joseph_A_merits_1997-04-21.md': (
            'Vey remains unadjudicated.',
            'The April 14 Vey decision concerning financial leave and prospective extraordinary-writ filing conditions changes no decree-termination, Rule 52, or modification premise here.'),
    }
    later_checks = {}
    for rel, before in baseline_data['later_records'].items():
        after = (ROOT / rel).read_bytes().decode('utf-8')
        old, new = replacements[Path(rel).name]
        good = before.count(old) == 1 and after == before.replace(old, new)
        later_checks[rel] = {'only_authorized_entering_note_changed': good,
                             'public_projection_unchanged': before.split('## Public Projection', 1)[1] == after.split('## Public Projection', 1)[1]}
        if not good:
            errors.append('Unexpected later Record difference: ' + rel)
    manifest = (TERM / 'workspace/manifest.md').read_text(encoding='utf-8')
    new_manifest_rows = [line for line in manifest.splitlines() if line.startswith('| 199') and '| OT_1996CHUNK' in line]
    chunk_rows = [line for line in new_manifest_rows if '| OT_1996CHUNK6 |' in line]
    if len(new_manifest_rows) != 153 or len(chunk_rows) != 12 or any('| Completed:' not in line for line in chunk_rows):
        errors.append('Manifest inventory or chunk 6 completion mismatch')
    ri = (TERM / 'render-inputs/OT_1996CHUNK6.md').read_text(encoding='utf-8')
    sources = re.findall(r'<!-- source-record: ([^>]+) -->', ri)
    if len(sources) != 12 or len(set(sources)) != 12 or '**Stopped matters:**' in ri:
        errors.append('Render Input must contain twelve unique events and no stopped notice')
    records = list((TERM / 'records').glob('*.md'))
    old_records = {rel for rel in baseline_data['files'] if rel.startswith('terms/OT1996/records/')}
    added = sorted(p.relative_to(ROOT).as_posix() for p in records if p.relative_to(ROOT).as_posix() not in old_records)
    if len(added) != 1 or 'In_re_Vey_' not in added[0] or not added[0].endswith('_1997-04-14.md'):
        errors.append('Expected exactly one new Vey April 14 Record')
    freeze_hashes = {
        'OT_1996CHUNK6_68_NEUTRAL.md': '83ea1913d1eb8be2b004ec59ef8ad0c0b0080c0fb355090ab2cca5a387905a21',
        'OT_1996CHUNK6_68_COMMITMENTS.md': 'b3a785d2307d8f6c5e59de43dbd50027a5a597d89df402840d4b27b73ce2729e',
        'OT_1996CHUNK6_68_RECONCILED.md': '15dc747cd95134cf7a3bfe14b1388228ea1c237d0570429b88f97e8d4ee8f61c',
        'OT_1996CHUNK6_68_FINANCIAL_NEUTRAL.md': 'efe69e45b7963ec5876731e8f8a68adaebc777dc6374708d0f22e5d43c7985cb',
        'OT_1996CHUNK6_68_FINANCIAL_COMMITMENTS.md': '9ba8e0d8c49511ff1fcb811a402882c08f3b7d11c6ba48dbc8e58699a91dba29',
        'OT_1996CHUNK6_68_FINANCIAL_RECONCILED.md': 'cbe798751e6c2705d8bb64d51d51f8ef9f091b62a43152ef2bd917562d63dea1',
        'OT_1996CHUNK6_68_PREPARATION_RECEIPT.md': '8e53a09f8ed4483efd1a9cc6f501ee92ce9eb9162a180feeb0717a3427515657',
    }
    for name, expected in freeze_hashes.items():
        if digest((TERM / 'freeze' / name).read_bytes()) != expected:
            errors.append('Frozen handoff changed: ' + name)
    for name in ['FINANCIAL_COMMITMENTS', 'FINANCIAL_RECONCILED']:
        filename = 'OT_1996CHUNK6_68_' + name + '.md'
        if (TERM / 'freeze' / filename).read_bytes() != (TERM / 'runtime' / filename).read_bytes():
            errors.append('Freeze/runtime difference: ' + filename)
    for name in ['continuity.md', 'neutral-projection.md']:
        t = (TERM / 'workspace' / name).read_text(encoding='utf-8')
        if '71 Court events and 2 admitted sources' not in t:
            errors.append(name + ': incorrect coverage count')
        if re.search(r'^.*\bVey\b.*Stopped:', t, re.M):
            errors.append(name + ': stale Vey stop')
        vey_public = (TERM / 'records/In_re_Vey_financial_leave_1997-04-14.md').read_text(encoding='utf-8').split('## Public Projection\n', 1)[1]
        public_topology = re.search(r'^## Opinion Topology\n(.*?)(?=^## )', vey_public, re.M | re.S)[1].strip()
        local_topology = 'Authority: [Record](../records/In_re_Vey_financial_leave_1997-04-14.md).\n\n#### Opinion Topology\n\n' + public_topology + '\n\n#### Holdings'
        if t.count(local_topology) != 1:
            errors.append(name + ': Vey public coalition declaration missing or altered')
    for folder in ['briefs', 'output']:
        before = {rel for rel in baseline_data['files'] if rel.startswith('terms/OT1996/' + folder + '/')}
        after = {p.relative_to(ROOT).as_posix() for p in (TERM / folder).glob('*.md')}
        if after != before:
            errors.append(folder + ': protected file inventory changed')
    result = {
        'protected_file_count': len(baseline_data['files']),
        'changed_existing_files': changed, 'new_records': added,
        'later_record_checks': later_checks,
        'inventory_events': len(new_manifest_rows), 'chunk6_events': len(chunk_rows),
        'render_input_records': sources, 'total_records': len(records),
        'frozen_handoff_hashes_verified': freeze_hashes,
        'errors': errors, 'git_commands_executed': 0,
        'note': 'Git-object existence and commitment remain for operator; no public output is modified.'
    }
    Path(str(PREFIX) + '_INTEGRITY.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(1)

def notes():
    receipt = TERM / 'freeze/OT_1996CHUNK6_68_DEPENDENCY_REVIEW.md'
    if not receipt.exists():
        raise SystemExit('Final dependency receipt is required before note changes')
    baseline_data = json.loads(BASE.read_text(encoding='utf-8'))
    replacements = {
        'Chandler_v_Miller_merits_1997-04-15.md': (
            'Vey has no completed event and supplies no law.',
            'The April 14 Vey decision concerning financial leave and prospective extraordinary-writ filing conditions changes no Fourth Amendment, candidacy, or remedial premise here.'),
        'Blessing_v_Freestone_merits_1997-04-21.md': (
            'No uncompleted Vey action supplies law or procedure.',
            'The April 14 Vey decision concerning financial leave and prospective extraordinary-writ filing conditions changes no Title IV-D, \u00a71983, statutory-transition, or remedial premise here.'),
        'New_Mexico_Department_of_Human_Services_v_Joseph_A_merits_1997-04-21.md': (
            'Vey remains unadjudicated.',
            'The April 14 Vey decision concerning financial leave and prospective extraordinary-writ filing conditions changes no decree-termination, Rule 52, or modification premise here.'),
    }
    for rel, before in baseline_data['later_records'].items():
        path = ROOT / rel
        if path.read_bytes() != before.encode('utf-8'):
            raise SystemExit('Later Record changed since baseline: ' + rel)
        old, new = replacements[path.name]
        assert before.count(old) == 1
        path.write_bytes(before.replace(old, new).encode('utf-8'))
        print('Entering-law note only: ' + path.name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['baseline', 'ledger', 'check', 'verify', 'notes'])
    globals()[parser.parse_args().action]()
