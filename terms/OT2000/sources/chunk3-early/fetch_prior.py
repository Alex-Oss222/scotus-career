from urllib.request import Request, urlopen
from pathlib import Path
import re
import html

out = Path('terms/OT2000/sources/chunk3-early')
out.mkdir(parents=True, exist_ok=True)
for name, key in [('huddleston_1988', '485/681')]:
    url = 'https://www.law.cornell.edu/supremecourt/text/' + key
    raw = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30).read().decode()
    body = raw[raw.index('id="tab_default_1"'):raw.index('<div class="tab-pane" id="tab_default_2"')]
    body = body[body.index('>') + 1:]
    body = re.sub(r'</(?:p|div|h[1-6])>', '\n', body)
    text = html.unescape(re.sub(r'<[^>]*>', '', body))
    text = '\n'.join(line.strip() for line in text.splitlines() if line.strip())
    (out / (name + '.txt')).write_text('Source: ' + url + '\n\n' + text + '\n', encoding='utf-8')
    print(name, len(text))
