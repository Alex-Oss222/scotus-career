"""Redact Stone cert material for the clean reconciliation audit; preserve originals."""
from pathlib import Path
import hashlib
import re

term = Path(__file__).resolve().parents[1]
source = term / 'freeze/OT_1995CHUNK1_A_COMMITMENTS.md'
text = source.read_text(encoding='utf-8')
old = "The separate `freeze/OT_1995CHUNK1_A_CERT_COMMITMENTS.md` contains the neutral petition polls, including the separately modeled Stone petition positions."
assert old in text
text = text.replace(old, 'Only the separately projected eight-Associate petition rows are authorized for reconciliation.')
old = 'The separate poll supports a limited grant by seven petition-stage votes; Scalia and Thomas favor denial but provide conditional merits commitments if the Court takes the case.'
assert old in text
text = text.replace(old, 'Six Associates favor a limited grant; Scalia and Thomas favor denial but provide conditional merits commitments if the Court takes the case.')
header = '# Redacted A independent commitments for clean reconciliation\n\nOnly the two certificate/poll metadata sentences identified by the redaction script differ from the original. All merits commitments and grounds are copied unchanged. No Stone petition position is supplied. The original freeze remains preserved.\n\n'
out = term / 'freeze/OT_1995CHUNK1_A_RECONCILIATION_SCOPED_COMMITMENTS.md'
out.write_text(header + text, encoding='utf-8')
cert = (term / 'freeze/OT_1995CHUNK1_A_CERT_COMMITMENTS.md').read_text(encoding='utf-8')
sections = re.split(r'(?m)(?=^## )', cert)[1:]
parts = ['# A — eight-Associate petition commitments only', '', 'Mechanical projection of the frozen petition handoff. Stone row, private introductory material and combined totals are excluded. Grant questions and all eight Associate rows are unchanged.', '']
for section in sections:
    lines = section.splitlines()
    parts += [lines[0], '']
    parts += [line for line in lines if line.startswith('**Question for')]
    parts += ['']
    rows = [line for line in lines if line.startswith('|') and not line.startswith('| Stone-Zsela |')]
    assert len(rows) == 10, (lines[0], len(rows))
    parts += rows + ['']
target = term / 'freeze/OT_1995CHUNK1_A_NONSTONE_CERT_COMMITMENTS.md'
target.write_text('\n'.join(parts), encoding='utf-8')
for path in (source, out, target):
    print(path.name, hashlib.sha256(path.read_bytes()).hexdigest())
