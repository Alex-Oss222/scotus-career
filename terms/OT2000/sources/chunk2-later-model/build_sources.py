from pathlib import Path
from html.parser import HTMLParser
import urllib.request
import hashlib
import json

ROOT = Path('terms/OT2000')
BASE = ROOT / 'sources/chunk2-later-model'
BASE.mkdir(parents=True, exist_ok=True)

class TextOnly(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag in ('p', 'div', 'h1', 'h2', 'h3', 'li', 'br'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

receipts = []
for name, url in [
    ('Tarkanian_1988', 'https://www.law.cornell.edu/supremecourt/text/488/179'),
    ('Welsh_1984', 'https://www.law.cornell.edu/supremecourt/text/466/740'),
    ('Segura_1984', 'https://www.law.cornell.edu/supremecourt/text/468/796'),
    ('First_Agricultural_1968', 'https://www.law.cornell.edu/supremecourt/text/392/339'),
    ('CoBank_2134_code', 'https://www.law.cornell.edu/uscode/text/12/2134'),
    ('CoBank_2023_code', 'https://www.law.cornell.edu/uscode/text/12/2023'),
    ('CoBank_2098_code', 'https://www.law.cornell.edu/uscode/text/12/2098'),
]:
    data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=45).read().decode('utf-8')
    parser = TextOnly()
    parser.feed(data)
    text = '\n'.join(line.strip() for line in ''.join(parser.parts).splitlines() if line.strip())
    for forbidden in ('One'+'Drive','Git'+'Hub'):
        assert forbidden.lower() not in text.lower()
    dest = BASE / (name+'.txt')
    dest.write_text(text, encoding='utf-8')
    receipts.append({'path':str(dest).replace('\\','/'), 'source':url, 'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})

parts = ['# CoBank statutory source copies\n\nThese reading copies preserve the enacted source text, including OCR artifacts. The current code pages show no amendment after 1988 for the reproduced operative provisions; only their pre-event enactments are used. No present-matter opinion is a source.\n']
def add(name, start, end, label, source):
    path = BASE / name
    text = path.read_text(encoding='utf-8')
    a = text.index(start)
    b = text.index(end, a)
    excerpt = text[a:b]
    parts.append('## '+label+'\n\nSource: '+source+'\n\n'+excerpt+'\n')
    receipts.append({'path':str(path).replace('\\','/'), 'excerpt_sha256':hashlib.sha256(excerpt.encode()).hexdigest(),'start':start,'end':end})

add('CoBank_1971.txt', 'SEC. 3.13.', 'TITLE IV', '1971 section 3.13, including both later-deleted sentences', 'https://www.govinfo.gov/content/pkg/STATUTE-85/pdf/STATUTE-85-Pg583.pdf')
add('CoBank_1985.txt', '(10) striking out the last two sentences', '(f) Title IV', '1985 section 205(e)(10)', 'https://www.govinfo.gov/content/pkg/STATUTE-99/pdf/STATUTE-99-Pg1678.pdf')
add('CoBank_1985.txt', 'SEC 101.', 'APPOINTMENT OF CONSERVATOR', '1985 replacement of section 4.0 and related funding provisions', 'https://www.govinfo.gov/content/pkg/STATUTE-99/pdf/STATUTE-99-Pg1678.pdf')
add('CoBank_1988.txt', '(p) Section 3.13', '12 use 2154.', '1988 section 805(p)', 'https://www.govinfo.gov/content/pkg/STATUTE-101/pdf/STATUTE-101-Pg1568.pdf')
for number in ('2134','2023','2098'):
    name='CoBank_'+number+'_code.txt'
    text=(BASE/name).read_text(encoding='utf-8')
    start='Each bank' if number=='2134' else ('The Farm Credit Banks' if number=='2023' else 'Each Federal land bank association')
    add(name,start,'Editorial Notes', 'Operative section '+number+' and enactment citation', 'https://www.law.cornell.edu/uscode/text/12/'+number)
dest=ROOT/'entering-law/OT_2000CHUNK2_cobank_statutes.md'
dest.write_text('\n'.join(parts),encoding='utf-8')
receipts.append({'output':str(dest).replace('\\','/'),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
(ROOT/'entering-law/OT_2000CHUNK2_LATER_SOURCE_SELECTION.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print('Saved seven source texts and statutory copy with hashes.')
