import json
import urllib.request
from pathlib import Path

base = Path(__file__).resolve().parent
url = 'https://static.case.law/us/487/cases/0589-01.json'
data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
case = json.loads(data)
(base / 'BOWEN_PRIOR.json').write_bytes(data)
(base / 'BOWEN_PRIOR.txt').write_text('\n\n'.join(o['text'] for o in case['casebody']['opinions']), encoding='utf-8')
print(json.dumps({'url': url, 'date': case['decision_date'], 'opinions': [(o.get('type'), o.get('author'), len(o['text'])) for o in case['casebody']['opinions']]}, indent=2))
