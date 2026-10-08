import html
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path('terms/OT1995/entering-law')
queries = [
    ('Colorado', 'collection:us-supreme-court AND ("95-489" OR title:"Colorado Republican")'),
    ('Umbehr', 'collection:us-supreme-court AND ("94-1654" OR title:Umbehr)'),
    ('OHare', 'collection:us-supreme-court AND ("95-191" OR title:"O Hare")'),
    ('Denver', 'collection:us-supreme-court AND ("95-124" OR "95-227" OR title:"Denver Area")'),
]
for name, query in queries:
    url = 'https://archive.org/advancedsearch.php?' + urllib.parse.urlencode({'q':query, 'output':'json', 'rows':30, 'fl[]':['identifier','title']}, doseq=True)
    data = json.load(urllib.request.urlopen(url))
    (ROOT / f'CHUNK10_{name.upper()}_IA_LISTING.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
    print(name, json.dumps(data['response']))
for name in ['COLORADO','UMBEHR','OHARE','DENVER']:
    source = ROOT / f'CHUNK10_{name}_LOWER_SOURCE.html'
    text = html.unescape(re.sub('<[^>]+>', ' ', source.read_text(encoding='utf-8')))
    (ROOT / f'CHUNK10_{name}_LOWER_SOURCE.txt').write_text(text, encoding='utf-8')
