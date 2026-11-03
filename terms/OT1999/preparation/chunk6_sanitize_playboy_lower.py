"""Copy the full lower opinion, withholding two excluded procedural references."""
from pathlib import Path
import hashlib
import json
import re

term = Path(__file__).resolve().parents[1]
folder = term / 'sources/chunk6-neutral'
receipt = []
for suffix in ['cap', 'independent-body']:
    source = folder / f'playboy-lowerfindings-{suffix}.txt'
    original = source.read_text(encoding='utf-8')
    clean, first = re.subn(r",?\s*aff'd mem\.,.*?(?=\(“PI Opinion”\))", ' [Excluded procedural reference omitted] ', original, flags=re.S)
    clean, second = re.subn(r'After affir[\s-]*mance of that order by the Supreme Court,\s*', '[Excluded procedural reference omitted] ', clean)
    assert first == second == 1, (suffix, first, second)
    assert '117 S.Ct. 1309' not in clean
    target = folder / f'playboy-lowerfindings-{suffix}-neutral.txt'
    target.write_text(clean, encoding='utf-8')
    receipt.append({'source': source.name, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'neutral_copy': target.name, 'neutral_sha256': hashlib.sha256(target.read_bytes()).hexdigest(), 'bounded_omissions': first + second, 'method': 'All remaining source text, including findings, legal analysis and footnotes, copied unchanged; no neutral fact or argument was authored.'})
(term / 'preparation/OT_1999CHUNK6_PLAYBOY_NEUTRAL_COPY_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print('Two complete neutral reading copies saved; two bounded procedural omissions in each.')
