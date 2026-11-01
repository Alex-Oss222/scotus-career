from pathlib import Path
import re
import json
import pymupdf

root = Path(__file__).resolve().parent
out = root.parents[1] / 'preparation' / 'OT_1999CHUNK3_LATER_NEUTRAL_EXCERPTS.md'

def read(name):
    return (root / name).read_text(encoding='utf-8')

def between(text, first, last, start=0):
    a = text.index(first, start)
    b = text.index(last, a + len(first))
    return text[a:b].strip()

def clean_headers(text):
    # Remove only identifiable publication/page headers, preserving source words.
    patterns = [r'^=== PDF PAGE .*?===\s*$', r'^529US1 Unit:.*$',
                r'^.*Cite as: 529 U\. S\..*$',
                r'^\d*\s*SHALALA v\. ILLINOIS COUNCIL ON LONG\s*$',
                r'^TERM CARE, INC\.\s*$', r'^Stevens,J\., dissenting\s*$',
                r'^Appendix to opinion of the Court\s*$',
                r'^\d*\s*UNITED STATES v\. LOCKE\s*$',
                r'^Page \d+\s*$', r'^TITLE \d+.*$', r'^§ \d+\s*$']
    for pat in patterns:
        text = re.sub(pat, '', text, flags=re.M)
    return re.sub(r'\n{3,}', '\n\n', text).strip()

parts = ['# OT1999 chunk 3 — neutral source excerpts\n\n'
         'These passages were copied by script from saved primary-source PDFs or their archived OCR. '
         'Page headers alone are removed where specified. Line breaks, ligatures, hyphenation, and OCR errors remain; '
         'the linked PDF is the reference for typography. The selection excludes the pending matters’ historical Supreme Court holdings, reasoning, and lineups. '
         'A lower court’s procedural action or a party’s position is identified as such and is not current simulated law. '
         'See the companion fact addendum for scope and source limits.\n']

def add(title, source, text):
    parts.append('## ' + title + '\n\n' + source + '\n\n```text\n' + text.strip() + '\n```\n')

doc = pymupdf.open(root / 'micro_IA40386005_1011 1. Petition for Writ of Certiorari.pdf')
add('Strout — historical statutory appendix',
    '[Petition, appendix C, pp. 30a–32a](https://archive.org/details/micro_IA40386005_1011). '
    'PDF pages 66–68, extracted in full. The scans of pages 66 and 68 were visually checked. '
    'The OCR omits some enumeration digits; the statute contains §2951 conditions 1–7, including the repealed fourth item.',
    '\n\n'.join(doc[i].get_text() for i in (65, 66, 67)))

t = read('illinois-council.txt')
a = t.index('42 U. S. C.', t.index('APPENDIX TO OPINION OF THE COURT'))
b = t.index('JusticeStevens, dissenting.', a)
add('Illinois Council — statutory appendix',
    '[529 U.S. 25–30, statutory appendix](https://www.govinfo.gov/content/pkg/USREPORTS-529/pdf/USREPORTS-529-1.pdf). '
    'The appendix reproduces §1395cc(h)(1), not paragraph (h)(2). That reference is preserved, not silently erased; '
    'no inference about an (h)(2) case is supplied. Publication headers are removed.', clean_headers(t[a:b]))

add('Johnson — 18 U.S.C. §3624(e)',
    '[1999 United States Code](https://www.govinfo.gov/content/pkg/USCODE-1999-title18/pdf/USCODE-1999-title18-partII-chap229-subchapC-sec3624.pdf). Entire subsection (e).',
    clean_headers(between(read('usc18-3624.txt'), '(e) SUPERVISION', '(f) MANDATORY')))
add('Johnson — 18 U.S.C. §3583(e)',
    '[1999 United States Code](https://www.govinfo.gov/content/pkg/USCODE-1999-title18/pdf/USCODE-1999-title18-partII-chap227-subchapD-sec3583.pdf). Entire subsection (e); distinct alternatives remain distinct.',
    clean_headers(between(read('usc18-3583.txt'), '(e) MODIFICATION', '(f) WRITTEN')))

t = read('locke.txt')
add('Locke — sixteen state provisions as described in the judgment below',
    '[529 U.S. 117–119, appendix quoting 148 F.3d 1057–1058](https://www.govinfo.gov/content/pkg/USREPORTS-529/pdf/USREPORTS-529-89.pdf). '
    'These are the lower court’s descriptions, not complete regulatory text. Publication headers and the appendix heading are removed.',
    clean_headers(t[t.index('“1. Event Reporting', t.index('APPENDIX TO OPINION OF THE COURT')):]))
t = read('usc46-3703-corrected.txt')
add('Locke — 46 U.S.C. §3703',
    '[1999 United States Code](https://www.govinfo.gov/content/pkg/USCODE-1999-title46/pdf/USCODE-1999-title46-subtitleII-partB-chap37-sec3703.pdf). Entire operative section, excluding historical/revision notes.',
    clean_headers(between(t, '§ 3703. Regulations', '(Pub. L. 98', t.index('§ 3703. Regulations'))))
t = read('usc33-2718.txt')
add('Locke — 33 U.S.C. §2718',
    '[1999 United States Code](https://www.govinfo.gov/content/pkg/USCODE-1999-title33/pdf/USCODE-1999-title33-chap40-subchapI-sec2718.pdf). Entire operative section, excluding source notes. Publication headers removed.',
    clean_headers(between(t, '§ 2718. Relationship', '(Pub. L. 101', t.index('§ 2718. Relationship'))))

t = read('micro_IA40385014_0260 04. Joint Appendix_djvu.txt')
add('Portuondo — prosecutor’s comments, objections, and trial ruling',
    '[Joint appendix, pp. 44–56](https://archive.org/details/micro_IA40385014_0260). '
    'Copied from the Archive OCR, including the surrounding credibility argument and the mistrial motion/ruling. '
    'Transcript page numbers in brackets and appendix page breaks are preserved. This is trial material, not later Supreme Court analysis.',
    between(t, '\n44 \n', '\n57 \n', 60000))
t = read('micro_IA40385014_0260 02. Petition for Writ of Certiorari_djvu.txt')
add('Portuondo — lower-court rehearing treatment of Teague',
    '[Petition appendix, pp. 73a–75a, reproducing the Second Circuit’s rehearing opinion](https://archive.org/details/micro_IA40385014_0260). '
    'The excerpt records when the contention was raised and the panel’s refusal to decide it; the last sentence concerns rehearing in the Second Circuit.',
    between(t, "Appellee's petition argues", 'VAN GRAAFEILAND, Circuit Judge, dissenting:', 140000))

out.write_text('\n'.join(parts), encoding='utf-8')
print(json.dumps({'output': str(out.relative_to(root.parents[3])), 'characters': out.stat().st_size}))
