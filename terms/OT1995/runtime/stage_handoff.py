"""Mechanically scope generated chunk inputs after their stage prerequisites exist."""
from pathlib import Path
import hashlib
import re
import sys

term = Path(__file__).resolve().parents[1]
stage, group = sys.argv[1:]
assert stage in {'COMPARATOR', 'STONE'} and group in {'A', 'B', 'C'}
required = [group]
if stage == 'STONE':
    # Different case groups may be assembled in parallel only after their own
    # reconciliation freezes; all independent chunk commitments must exist.
    assert (term / 'freeze/OT_1995CHUNK1_COMMITMENTS.md').is_file()
suffix = 'COMMITMENTS' if stage == 'COMPARATOR' else 'RECONCILED'
for letter in required:
    p = term / 'freeze' / f'OT_1995CHUNK1_{letter}_{suffix}.md'
    assert p.is_file() and p.stat().st_size > 100, f'Missing handoff: {p.name}'
source = term / 'runtime' / f'OT_1995CHUNK1_{stage}.md'
raw = source.read_text(encoding='utf-8')
sections = re.split(r'(?m)(?=^## OT1995-)', raw)[1:]
selected = []
for section in sections:
    date = re.search(r'\*\*Event:\*\* (\d{4}-\d{2}-\d{2})', section).group(1)
    actual = 'A' if date <= '1995-10-30' else 'B' if date <= '1995-11-13' else 'C'
    if actual == group:
        selected.append((date, section))
assert len(selected) == 4, (group, len(selected))
body = f'# OT1995 chunk 1 — {group} {stage} stage input\n\n'
body += 'Mechanically copied from the generated section-homogeneous runtime input. Stage access only; no independent revision.\n\n'
body += ''.join(section for _, section in sorted(selected, key=lambda x: (x[0], x[1].splitlines()[0])))
out = term / 'freeze' / f'OT_1995CHUNK1_{group}_{stage}_INPUT.md'
out.write_text(body, encoding='utf-8')
print(f'{out.name}: 4 exact sections; source SHA-256 {hashlib.sha256(source.read_bytes()).hexdigest()}; handoff SHA-256 {hashlib.sha256(out.read_bytes()).hexdigest()}')
