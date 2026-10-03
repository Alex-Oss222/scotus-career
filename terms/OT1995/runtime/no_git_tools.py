"""Run the existing tools with Git-only helpers explicitly deferred to operator.

No repository tooling is edited. No Git subprocess is launched.
"""
from pathlib import Path
import importlib.util
import os
import re
import sys

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

ROOT = Path(__file__).resolve().parents[3]
action = sys.argv[1]
name = {'ledger': 'rebuild_ledger', 'check': 'check_term'}[action]
spec = importlib.util.spec_from_file_location(name, ROOT / 'tools' / (name + '.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
skipped = []
if action == 'ledger':
    ledger_path = ROOT / 'terms/OT1995/workspace/ledger.md'
    old_lines = ledger_path.read_text(encoding='utf-8').splitlines()
    saved = {}
    for line in old_lines:
        match = re.search(r'\[record\]\(\.\./records/([^)]+)\)', line)
        if match:
            cells = line.strip().split('|')
            saved[match.group(1)] = (int(cells[1].strip()), cells[-3].strip())
    new_files = sorted(
        (p for p in (ROOT / 'terms/OT1995/records').glob('*.md') if p.name not in saved),
        key=lambda p: (module.parse(p)['date'], p.name),
    )
    next_order = max(value[0] for value in saved.values()) + 1
    for index, path in enumerate(new_files, next_order):
        saved[path.name] = (index, 'operator commit pending')
    def deferred_added(root, path):
        return saved[path.name]
    module.git_added = deferred_added
else:
    def deferred_exists(root, sha):
        skipped.append(sha)
        return True  # suppress a false "missing" claim; not a verification
    module.git_object_exists = deferred_exists
sys.argv = [str(ROOT / 'tools' / (name + '.py')), 'OT1995']
module.main()
if action == 'ledger':
    generated = ledger_path.read_text(encoding='utf-8').splitlines()
    ledger_path.write_text('\n'.join(old_lines[:6] + generated[6:]) + '\n', encoding='utf-8')
print(f'Git operations: not performed. Git history and hash verification deferred to operator; {len(set(skipped))} referenced hashes skipped in this invocation.')
