from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
source = root / 'preparation/later-sources/erie-07. Joint Appendix_djvu.txt'
text = source.read_text(encoding='utf-8')

def page(number):
    matches = list(re.finditer(r'(?m)^' + str(number) + r'\s*$', text))
    assert len(matches) == 1, (number, len(matches))
    return matches[0].start()

selections = [
    (27, 30, 'October 19 hearing: limited temporary restraint and initial agreed facts'),
    (50, 51, 'October 19 hearing: offered evidence and decision to proceed to argument'),
    (53, 56, 'October 19 hearing: theatrical productions, counsel interpretation, and opposing response'),
    (67, 70, 'October 19 hearing: predicted enforcement against Kandyland and disputed owner liability'),
    (72, 86, 'December 21 hearing: full negotiation and final agreed record, including Equus nonenforcement'),
    (86, 91, 'December 21 hearing: arts-community statement and City response'),
    (103, 108, 'December 21 hearing: requested judicial narrowing and higher forms of expression'),
    (111, 117, 'December 21 hearing: construction versus rewriting, effects argument, and opposing response'),
]
out = ['''# Erie joint-appendix source supplement: exact record extracts

Source: the original archived joint appendix, saved at `preparation/later-sources/erie-07. Joint Appendix_djvu.txt` and `.pdf`, from https://archive.org/details/micro_IA40385014_0258 . All long text below is copied mechanically from the saved source. Printed joint-appendix page numbers, not the underlying transcript's bracketed page numbers, control the headings. OCR quirks and line wrapping remain; the source scans were used to verify the key passages, especially printed pages 53–55 and 80–89. This annex is evidence, not a current judicial ruling or a grant of authority to counsel's construction.

The full saved appendix was read: cover, contents, docket entries and every transcript through printed page 118. The contents refer to a complaint and lower opinions in a separate Petition Appendix; those cross-references do not make their full texts part of this saved joint appendix. This source supplement does not claim a new reading of those separate documents.

Source status must follow the accompanying neutral supplement. In particular, the final agreement on page 84 is distinct from a counsel interpretation of the ordinance on pages 53–54. The parties removed “artistic and social merit” language from the proposed fact; no statement below is authority for a categorical judicial exemption based on the perceived worth of expression.

''']
for first, after, label in selections:
    excerpt = text[page(first):page(after)]
    assert excerpt and excerpt.startswith(str(first))
    out.append(f'## Printed pages {first}–{after-1}: {label}\n\n```text\n{excerpt.rstrip()}\n```\n\n')
target = root / 'entering-law/OT_1999CHUNK4_ERIE_JA_SUPPLEMENT_EXTRACTS.md'
target.write_text(''.join(out), encoding='utf-8')
print('Erie original-source excerpts copied:', target.name)
