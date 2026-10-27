import json
import urllib.request
from pathlib import Path

base = Path(__file__).resolve().parent
receipt = []
for name, volume, page in [('WITTERS', '474', '0481'), ('MUELLER', '463', '0388'), ('NYQUIST', '413', '0756')]:
    url = f'https://static.case.law/us/{volume}/cases/{page}-01.json'
    data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
    case = json.loads(data)
    (base / f'{name}_PRIOR.json').write_bytes(data)
    opinions = case['casebody']['opinions']
    (base / f'{name}_PRIOR.txt').write_text('\n\n'.join(o['text'] for o in opinions), encoding='utf-8')
    receipt.append({'name': name, 'url': url, 'date': case['decision_date'], 'opinions': [(o.get('type'), o.get('author'), len(o['text'])) for o in opinions]})
(base / 'JACKSON_PRIOR_SOURCE_RECEIPT.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt, indent=2))
