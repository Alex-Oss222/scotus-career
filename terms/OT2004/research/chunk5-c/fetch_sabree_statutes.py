from pathlib import Path
from html.parser import HTMLParser
import urllib.request
import concurrent.futures

DEST = Path(__file__).parent

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)
    def handle_endtag(self, tag):
        if tag.lower() in {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'li', 'pre'}:
            self.parts.append('\n')

PATHS = {
    '1396a': 'chap7-subchapXIX-sec1396a',
    '1396d': 'chap7-subchapXIX-sec1396d',
    '1396c': 'chap7-subchapXIX-sec1396c',
    '1320a-2': 'chap7-subchapXI-partA-sec1320a-2',
    '1320a-10': 'chap7-subchapXI-partA-sec1320a-10',
    '1983': 'chap21-subchapI-sec1983',
}

def fetch(item):
    name, suffix = item
    url = f'https://www.govinfo.gov/content/pkg/USCODE-2004-title42/html/USCODE-2004-title42-{suffix}.htm'
    raw = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
    stem = DEST / f'sabree_2004_{name}'
    stem.with_suffix('.html').write_bytes(raw)
    parser = Text()
    parser.feed(raw.decode('utf-8'))
    text = ''.join(parser.parts)
    stem.with_suffix('.txt').write_text('Source: ' + url + '\n\n' + text, encoding='utf-8')
    return name, len(raw), len(text)

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(6) as pool:
        for result in pool.map(fetch, PATHS.items()):
            print(result)
