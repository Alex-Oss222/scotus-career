from pathlib import Path
from urllib.request import Request, urlopen
import fitz

root = Path(__file__).resolve().parents[1]
directory = root / 'sources' / 'chunk2_b'
for subchapter in ('IV', 'V'):
    url = f'https://www.govinfo.gov/content/pkg/USCODE-2000-title33/pdf/USCODE-2000-title33-chap26-subchap{subchapter}.pdf'
    stem = f'deaton_uscode2000_subchap{subchapter}'
    pdf = directory / (stem + '.pdf')
    pdf.write_bytes(urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read())
    document = fitz.open(pdf)
    pages = [page.get_text(sort=True) for page in document]
    (directory / (stem + '.txt')).write_text('Source: ' + url + '\n\n' + '\n\n'.join(pages), encoding='utf-8')
    print(stem, 'pages:', len(pages), 'characters:', sum(map(len, pages)))
