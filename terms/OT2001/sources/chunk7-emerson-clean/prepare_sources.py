from pathlib import Path
import urllib.request
from pypdf import PdfReader
from html.parser import HTMLParser

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)
    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())

base = Path(__file__).parent
items = [
    ('fifth_circuit', 'https://www.ca5.uscourts.gov/opinions/pub/99/99-10331.cr0.wpd.pdf', 'pdf'),
    ('federal_response', 'https://www.justice.gov/osg/brief/emerson-v-united-states-response', 'html'),
]
for name, url, ext in items:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req, timeout=90).read()
    path = base / (name + '.' + ext)
    path.write_bytes(data)
    if ext == 'pdf':
        reader = PdfReader(path)
        text = '\n\n'.join(f'--- PDF page {i+1} ---\n' + (p.extract_text() or '') for i, p in enumerate(reader.pages))
        print(name, 'pages', len(reader.pages))
    else:
        parser = TextParser()
        parser.feed(data.decode('utf-8'))
        text = '\n'.join(parser.parts)
    (base / (name + '.txt')).write_text(text, encoding='utf-8')
    print(name, len(data), len(text))
