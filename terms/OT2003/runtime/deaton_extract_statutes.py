from pathlib import Path
import pymupdf

directory = Path(__file__).resolve().parents[1] / 'sources' / 'chunk2_b'
for subchapter in ('IV', 'V'):
    stem = f'deaton_uscode2000_subchap{subchapter}'
    document = pymupdf.open(directory / (stem + '.pdf'))
    pages = []
    for page in document:
        width, height = page.rect.width, page.rect.height
        left = page.get_text(clip=pymupdf.Rect(0, 40, width/2, height-30))
        right = page.get_text(clip=pymupdf.Rect(width/2, 40, width, height-30))
        pages.append(left + '\n' + right)
    content = '\n\n'.join(pages)
    (directory / (stem + '_columns.txt')).write_text(content, encoding='utf-8')
    section = '1344' if subchapter == 'IV' else '1362'
    following = str(int(section)+1)
    start = content.index('§ ' + section + '.')
    end = content.index('§ ' + following + '.', start)
    (directory / ('deaton_usc2000_' + section + '.txt')).write_text('Source: https://www.govinfo.gov/content/pkg/USCODE-2000-title33/pdf/USCODE-2000-title33-chap26-subchap' + subchapter + '.pdf\n\n' + content[start:end], encoding='utf-8')
    print(section, 'characters:', end-start)
