from pathlib import Path
import hashlib
import json

base = Path('terms/OT2000')
expected = {
    "freeze/OT_2000CHUNK8_NEUTRAL_TYLER_REFRESH.md": "d722dd6db2f551ae0f18f0bc924bd5d79e3a7d646d43379fccae7dfe42c7e192",
    "freeze/OT_2000CHUNK8_COMMITMENTS_tyler.md": "c8e302a3bd7bf96b394e957c3197a003fbc0c3d8ec6bab3a15be7f10fcb641c1",
    "runtime/OT_2000CHUNK8_COMMITMENTS_tyler.md": "c8e302a3bd7bf96b394e957c3197a003fbc0c3d8ec6bab3a15be7f10fcb641c1",
    "freeze/OT_2000CHUNK8_TYLER_PRESENTED_ISSUES_SOURCE.md": "3c8d21b82b2c4dda6a0cca0b4a7f6273f86adf1fa5bc1af4297aad3a22887522",
    "freeze/OT_2000CHUNK8_TYLER_BRIEF_FACTS_VALIDATED.md": "b21a820f77b40fde66dca574ba283a47de1d662c28ac7c7db8e1f182e6b0a8cb"
}
actual = {name: hashlib.sha256((base / name).read_bytes()).hexdigest() for name in expected}
assert actual == expected
names = [
    'OT_2000CHUNK8_COMMITMENTS_tyler_REFRESH.md',
    'OT_2000CHUNK8_NEUTRAL_TYLER_SCOPE_ADDENDUM.md',
    'OT_2000CHUNK8_TYLER_SCOPE_VALIDATION_RECEIPT.md',
]
pairs = [(base / 'freeze' / name, base / 'runtime' / name) for name in names]
for frozen, working in pairs:
    assert not working.exists() or working.read_bytes() == frozen.read_bytes()
    working.write_bytes(frozen.read_bytes())
    assert working.read_bytes() == frozen.read_bytes()
body = pairs[0][0].read_text(encoding='utf-8')
assert body.count('### Justice ') == 8
for bad in ['One' + 'Drive', 'Git' + 'Hub', 'file://']:
    assert bad not in body
print(json.dumps({str(path.relative_to(base)).replace(chr(92), '/'): hashlib.sha256(path.read_bytes()).hexdigest() for pair in pairs for path in pair}))
