"""Generate projections after the operator's substantive preservation gate.

This helper never decides a legal issue and never invokes Git. Repository tools
are unchanged; only the separately disclosed Git adapter is used where needed.
"""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1995'
gate = TERM / 'freeze/CHUNK1_PRESERVATION_COMPLETE.json'
assert gate.is_file(), 'Substantive preservation gate is required'
approved = json.loads(gate.read_text(encoding='utf-8'))
records = [TERM / 'records' / name for name in approved['records']]
assert len(records) == 11 and len(set(records)) == 11
assert {p.name for p in (TERM / 'records').glob('*.md')} == {p.name for p in records}
assert not any('Tuggle' in p.name for p in records)
for path in records:
    assert hashlib.sha256(path.read_bytes()).hexdigest() == approved['sha256'][path.name]
blockers = json.loads((TERM / 'runtime/assembly/BLOCKERS.json').read_text(encoding='utf-8'))
assert len(blockers) == 1 and blockers[0]['case'] == 'Tuggle v. Netherland'
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
results = []
def run(*args):
    result = subprocess.run([sys.executable, '-B', *map(str, args)], cwd=ROOT,
                            env=env, capture_output=True, text=True)
    results.append({'arguments':list(map(str,args)), 'returncode':result.returncode,
                    'stdout':result.stdout, 'stderr':result.stderr})
    (TERM / 'freeze/OT_1995CHUNK1_TOOL_RESULTS.json').write_text(
        json.dumps(results, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(result.stdout.strip())
    if result.returncode:
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)

run(TERM / 'runtime/no_git_tools.py', 'ledger')
run(ROOT / 'tools/rebuild_manifest.py', 'OT1995', '--stopped',
    blockers[0]['case'] + '=' + blockers[0]['blocker'])
run(TERM / 'runtime/refresh_chunk1_workspace.py')
run(ROOT / 'tools/build_render_input.py', TERM / 'render-inputs/OT_1995CHUNK1.md',
    *records, '--stopped', blockers[0]['case'] + ': ' + blockers[0]['blocker'])
run(TERM / 'runtime/check_chunk1.py')
run(TERM / 'runtime/no_git_tools.py', 'check')
print('Run projections generated and non-Git repository checks completed. No public render written.')
