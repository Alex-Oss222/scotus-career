from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
directory = root / 'sources' / 'chunk2_b'
url = 'https://www.govinfo.gov/content/pkg/CFR-2003-title33-vol3/pdf/CFR-2003-title33-vol3-sec328-3.pdf'
pdf = directory / 'deaton_cfr2003_3283.pdf'
pdf.write_bytes(urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read())
reader = PdfReader(pdf)
content = '\n\n'.join(page.extract_text() or '' for page in reader.pages)
destination = directory / 'deaton_cfr2003_3283.txt'
destination.write_text('Source: ' + url + '\n\n' + content, encoding='utf-8')
print(str(destination))
print('Pages:', len(reader.pages))
