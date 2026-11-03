from pathlib import Path
import importlib.util
import json
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms/OT1999'
spec = importlib.util.spec_from_file_location('build_render_input', ROOT / 'tools/build_render_input.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
records = []
for p in (TERM / 'records').glob('*.md'):
    t = p.read_text(encoding='utf-8')
    m = re.search(r'^\*\*Event and date:\*\*.*$', t, re.M)
    if m and re.search(r'chunk 8\b', m[0], re.I):
        records.append(p)
stops = json.loads((TERM / 'runtime/OT_1999CHUNK8_STOPS.json').read_text(encoding='utf-8'))
if len(records) + len(stops) != 12:
    raise SystemExit(f'Incomplete chunk: {len(records)} Records and {len(stops)} stopped matters')
sys.argv = ['build_render_input.py', str(TERM / 'render-inputs/OT_1999CHUNK8.md')]
sys.argv += [str(p) for p in records]
for case, reason in stops.items():
    sys.argv += ['--stopped', case + ': ' + reason]
mod.main()
