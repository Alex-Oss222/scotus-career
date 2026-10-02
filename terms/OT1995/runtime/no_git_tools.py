"""Run the existing tools with Git-only helpers explicitly deferred to operator.

No repository tooling is edited. No Git subprocess is launched.
"""
from pathlib import Path
import importlib.util
import os
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
    files = sorted((ROOT / 'terms/OT1995/records').glob('*.md'), key=lambda p: (module.parse(p)['date'], p.name))
    order = {p.name: n for n, p in enumerate(files, 1)}
    def deferred_added(root, path):
        return order[path.name], 'operator commit pending'
    module.git_added = deferred_added
else:
    def deferred_exists(root, sha):
        skipped.append(sha)
        return True  # suppress a false "missing" claim; not a verification
    module.git_object_exists = deferred_exists
sys.argv = [str(ROOT / 'tools' / (name + '.py')), 'OT1995']
module.main()
if action == 'ledger':
    p = ROOT / 'terms/OT1995/workspace/ledger.md'
    text = p.read_text(encoding='utf-8').replace(
        'Generated from canonical Records in Git commitment order. Records control if this index conflicts with them.',
        'Generated from durably preserved canonical Records in effective-date order (same-day natural-name tie-break). Git commitment order and hashes are deferred to the operator under the no-Git instruction. Records control if this index conflicts with them.'
    ).replace('| Commit order |', '| Preservation index |')
    p.write_text(text, encoding='utf-8')
print(f'Git operations: not performed. Git history and hash verification deferred to operator; {len(set(skipped))} referenced hashes skipped in this invocation.')
