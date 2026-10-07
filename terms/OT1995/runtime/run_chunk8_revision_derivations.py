"""Run the requested existing derivation tools, with Git hooks deferred."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1995'
manifest = (TERM / 'workspace/manifest.md').read_text(encoding='utf-8')
records = []
for line in manifest.splitlines():
    if '| OT_1995CHUNK8 |' in line:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        assert cells[6].startswith('Completed: ')
        name = cells[6].removeprefix('Completed: ')
        assert Path(name).name == name
        records.append(TERM / 'records' / name)
assert len(records) == len(set(records)) == 12
commands = [
    [sys.executable, '-B', str(TERM / 'runtime/no_git_tools.py'), 'ledger'],
    [sys.executable, '-B', str(ROOT / 'tools/rebuild_manifest.py'), 'OT1995'],
    [sys.executable, '-B', str(ROOT / 'tools/build_render_input.py'),
     str(TERM / 'render-inputs/OT_1995CHUNK8.md'), *map(str, records)],
    [sys.executable, '-B', str(TERM / 'runtime/no_git_tools.py'), 'check'],
]
logs = ['# Chunk 8 revision derivation and validation log', '',
        'Original repository tool mains are used. The ledger and term check run through the disclosed adapter solely to avoid Git operations. Existing first-record metadata is retained; the new Record remains pending operator commit. Referenced commit existence is not verified.', '']
for argv in commands:
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
    logs += ['## ' + Path(argv[2]).name + ' ' + (argv[3] if len(argv) == 4 else ''), '',
             '```text', result.stdout.rstrip(), result.stderr.rstrip(),
             'exit_code=' + str(result.returncode), '```', '']
    (TERM / 'freeze/OT_1995CHUNK8_REVISION_TOOL_VALIDATION.md').write_text('\n'.join(logs), encoding='utf-8')
    print(result.stdout, end='')
    if result.stderr:
        print(result.stderr, end='', file=sys.stderr)
    if result.returncode:
        raise SystemExit(result.returncode)
