from pathlib import Path
from urllib.request import Request, urlopen
import fitz

base = Path('terms/OT1996/freeze/sources')
sources = {
    'B_Askin_2510_1994': 'https://www.govinfo.gov/content/pkg/USCODE-1994-title18/pdf/USCODE-1994-title18-partI-chap119-sec2510.pdf',
    'B_Askin_CALEA_1994': 'https://www.govinfo.gov/content/pkg/STATUTE-108/pdf/STATUTE-108-Pg4279.pdf',
}
for name, url in sources.items():
    pdf = base / (name + '.pdf')
    if not pdf.exists():
        pdf.write_bytes(urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read())
    doc = fitz.open(pdf)
    pages = [page.get_text() for page in doc]
    (base / (name + '.txt')).write_text('Source: ' + url + '\n\n' + '\n\n'.join(pages), encoding='utf-8')
    print(name, len(pages), pdf.stat().st_size)

# Copy complete official pages containing the definition and amendment history;
# no primary-source passage is reconstructed from model-generated text.
code = fitz.open(base / 'B_Askin_2510_1994.pdf')
act = fitz.open(base / 'B_Askin_CALEA_1994.pdf')
out = ['# Askin statutory source pages — mechanically copied text\n',
       '1994 Code text must be read with its 1986 and 1994 amendment history. The 1994 Code main text already incorporates the October 25, 1994 cordless amendment. It is not the unamended law at interception.\n']
for page in [0, 1, 2]:
    out += [f'\n## Official Code PDF page {page+1}\n', code[page].get_text()]
for page in [11, 12]:
    out += [f'\n## Public Law 103-414 PDF page {page+1}\n', act[page].get_text()]
(base / 'B_Askin_2510_EXACT_PAGES.md').write_text('\n'.join(out), encoding='utf-8')
