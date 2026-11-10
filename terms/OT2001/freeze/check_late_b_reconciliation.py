from pathlib import Path
import hashlib
import json
import re

base = Path('terms/OT2001')
names = ['Stevens', "O'Connor", 'Scalia', 'Kennedy', 'Souter', 'Thomas', 'Ginsburg', 'Breyer']
paths = [base / 'freeze/OT_2001CHUNK6_LATE_B_JUNE10_RECONCILED.md', base / 'freeze/OT_2001CHUNK6_LATE_B_JUNE17_RECONCILED.md']
texts = [p.read_text(encoding='utf-8') for p in paths]
counts = {n: sum(len(re.findall(r'^\| ' + re.escape(n) + r' \|', t, re.M)) for t in texts) for n in names}
aggregate_path = base / 'freeze/OT_2001CHUNK6_LATE_B_RECONCILED.md'
aggregate = aggregate_path.read_text(encoding='utf-8')
checks = {
    'justice_rows': counts,
    'tables': sum(t.count('| Justice |') for t in texts),
    'exact_subhandoffs_in_aggregate': [t in aggregate for t in texts],
    'absolute_local_paths_in_handoffs': any(re.search(r'(?<![A-Za-z])[A-Za-z]:[\\/]', t) for t in texts),
}
assert all(v == 7 for v in counts.values()), counts
assert checks['tables'] == 7
assert all(checks['exact_subhandoffs_in_aggregate'])
assert not checks['absolute_local_paths_in_handoffs']
originals = {
    'OT_2001CHUNK6_LATE_B_JUNE10_COMMITMENTS.md': '82cb23cbe13a1d0be041ab85b4a556e4fb0da5dbb127c13c50ddbe741afb3c67',
    'OT_2001CHUNK6_LATE_B_JUNE17_COMMITMENTS.md': 'a765350c20a32a46ab39304cecae4493a3604ef70a29b8f28f442b279dbc2f0e',
    'OT_2001CHUNK6_LATE_B_COMMITMENTS.md': '29ee90e843f355c85c3c63806315558499b23ee8fb484740c1aa1dcf76205597',
}
for name, expected in originals.items():
    assert hashlib.sha256((base / 'freeze' / name).read_bytes()).hexdigest() == expected, name
checks['original_commitments_unchanged'] = True
files = paths + [aggregate_path, base / 'runtime/OT_2001CHUNK6_LATE_B_COMPARATOR.md', base / 'entering-law/OT_2001CHUNK6_THROUGH_MAY28_PUBLIC.md']
files += [p for p in (base / 'sources/chunk6-comparator').iterdir() if p.name.startswith(('traffic-stream_', 'morgan_', 'barnes_', 'watchtower_', 'newport_'))]
checks['sha256'] = {p.as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(base / 'freeze/OT_2001CHUNK6_LATE_B_RECONCILIATION_CHECKS.json').write_text(json.dumps(checks, indent=2) + '\n', encoding='utf-8')
print(json.dumps(checks, indent=2))
