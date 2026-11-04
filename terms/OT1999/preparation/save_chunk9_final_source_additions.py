from pathlib import Path
from hashlib import sha256

base = Path('terms/OT1999/preparation')
def digest(p):
    return sha256(p.read_bytes()).hexdigest()
def save(name, text):
    (base/name).write_text(text, encoding='utf-8')

save('OT_1999CHUNK9_STENBERG_NEUTRAL_EXPOSURE_RECEIPT.md', '''# Internal control receipt: Stenberg neutral-context exposure

This receipt is control-only. Do not give it to the fresh neutral validator or independent model. The affected context is /root/validate_neutral. No Stenberg neutral freeze or commitment had been written when the incident occurred; none may be written by this context afterward.

During retrieval of the exact 1997 Nebraska statutory license provision, a web search intended to reach the official legislature site used a malformed site restriction and no domain filter. Queries were `site.nebraskalegislature.gov "28-328" "revocation" "Licensure"` and `site.nebraskalegislature.gov LB23 1997 partial birth abortion Director Regulation Licensure`. Results included target historical Supreme Court material and an explicit historical outcome snippet. The context stopped Stenberg framing immediately and notified the root. The result substance is not repeated here.

Under Engine section 3A, subsequent work by this context is limited to objective control-source extraction. A fresh neutral context must independently validate Stenberg with the allowed runtime neutral packet, current neutral law, original sanitized late handoffs, and the official LB23 source addition. It must not receive this receipt or any historical outcome material. A separate fresh independent model follows that validation.

Already frozen Jones revised, Henerey, Mobil, Alaska, Hill and Mitchell packets preceded this incident and are unchanged. No target Dale outcome was exposed. This receipt neither decides any component nor supplies law.
''')

pdf = base/'sources/chunk9_stenberg_lb23.pdf'
ocr = pdf.with_suffix('.txt')
save('OT_1999CHUNK9_STENBERG_LB23_SOURCE_ADDITION.md', '''# Stenberg: official LB23 source addition for fresh validation

Objective source extraction only; no completed neutral validation or modeling. The source is Nebraska Legislative Bill 23, approved June 9, 1997, from the official Legislature's saved slip-law PDF: https://nebraskalegislature.gov/FloorDocs/95/PDF/Slip/LB23.pdf . This is a predecision enactment, not a target Supreme Court source.

The complete five-page enactment is preserved at [official saved PDF](sources/chunk9_stenberg_lb23.pdf). Its embedded extracted text is preserved at [unaltered extraction](sources/chunk9_stenberg_lb23.txt). The embedded text is materially incomplete: it omits underlined new text on page 2, including section 3, and some amendments on page 3. It cannot substitute for the images or PDF. No missing words have been reconstructed.

All five pages were rendered directly from that PDF:

- [Page 1](sources/chunk9_stenberg_lb23_page_1.png): approval, purpose, and beginning of definitions.
- [Page 2](sources/chunk9_stenberg_lb23_page_2.png): full partial-birth definition and section 3, subsections (1)-(5), including the complete license provision and administrative-hearing/criminal-proceeding provision omitted by the earlier ellipsis.
- [Page 3](sources/chunk9_stenberg_lb23_page_3.png): professional-conduct amendments and beginning of amended section 71-155.
- [Page 4](sources/chunk9_stenberg_lb23_page_4.png): remainder of section 71-155, section 71-171.02, and severability in section 8.
- [Page 5](sources/chunk9_stenberg_lb23_page_5.png): repealers and effective-date clause.

The page 2 image was inspected and confirms the earlier extract's license ellipsis omits material source text. Section 3(5) also supplies procedural text that must be evaluated separately from section 3(4). The fresh validator must read the full enactment images, preserve the statutory qualifications and procedure in its own validation, and verify any proposed text transcription against the images. Related licensing amendments and severability are present in this source; their legal significance is for that fresh context. This addition makes no claim that the incomplete embedded OCR is a full statutory quotation.

SHA256 of official PDF: ''' + digest(pdf) + '\n\nSHA256 of unaltered embedded text extraction: ' + digest(ocr) + '\n')

source = Path('tmp/ot1999_chunk9_late_sources/dale_lower.txt')
s = source.read_text(encoding='utf-8')
a = s.index('2. LAD Exceptions')
b = s.index('B. The Common Law', a)
excerpt = s[a:b]
save('OT_1999CHUNK9_DALE_LAD_SOURCE.md', '''# Dale: LAD exceptions and statutory application in the judgment below

This objective reading copy is mechanically extracted from the saved predecision New Jersey Supreme Court opinion, Dale v. Boy Scouts of America, 160 N.J. 562, 734 A.2d 1196 (August 4, 1999). Public source: https://static.case.law/nj/160/html/0562-01.html . Saved source: `tmp/ot1999_chunk9_late_sources/dale_lower.txt`.

The complete majority subsections on LAD exceptions and the resulting statutory violation are copied without substantive edits, from `2. LAD Exceptions` through the text immediately before `B. The Common Law`. The source's OCR and reporter pagination remain. Statutory citations resembling `10:5-51`, `10:5-5l`, or `10:5—5l` refer to subsection l in this discussion. The material contains distinctly-private, religious-educational-facility, and parental exceptions; adult-selectivity arguments; and privilege/advantage scope. These are the state court's statutory analysis and reported record characterizations, not an independent determination of the federal constitutional question.

This supplement does not freeze Dale. The completed June 26 Jones public law still must be added to Dale's entering law and evaluated by a fresh neutral validator before a fresh independent model. It supplies no Jones outcome.

Saved source SHA256: ''' + digest(source) + '\n\n## Exact copied lower-court text\n\n' + excerpt)
assert excerpt == (base/'OT_1999CHUNK9_DALE_LAD_SOURCE.md').read_text(encoding='utf-8').split('## Exact copied lower-court text\n\n',1)[1]

alaska_pdf = Path('terms/OT1999/sources/chunk9/alaska/joint-motion-2000-06-07.pdf')
save('OT_1999CHUNK9_ALASKA_EO_CITATION_SOURCE_NOTE.md', '''# Alaska: proposed decree paragraph D citation check

Scope: objective citation verification of the actual June 7, 2000 joint motion's proposed decree. This is an additional neutral source note; the existing frozen packet and validation receipt are preserved unchanged. No prior adjudication or source note is silently corrected.

The image of PDF page 22 (printed appendix page 6a), paragraph D, in the actual June 7 filing clearly prints `Executive Order No. 3739-A (1923)`. Thus 3739-A in the mechanically copied proposed terms is faithful to the filing; it is not an OCR substitution. The paragraph identifies the coastal boundary of the National Petroleum Reserve-Alaska, beginning on the western bank of the Colville River and continuing through the stated geographical features to the northwestern extremity of Icy Cape. Those terms remain as printed.

The operator reports that the earlier 1997 public source notes instead cite Executive Order 3797-A. This validator has not reopened a raw 1997 Record. The discrepancy is a source-citation discrepancy; the current filing alone does not establish a new substantive reservation, a changed boundary, or an alteration of the prior adjudicated title rule. Establishing which number correctly identifies the 1923 instrument requires verification of that instrument or an independently authoritative predecision source. Do not correct the frozen proposed text to 3797-A and do not silently correct the 1997 entry to 3739-A merely to force consistency. If an instrument-number correction is established, state that it corrects the citation while separately determining whether the instrument and boundary identity are unchanged.

Source: `terms/OT1999/sources/chunk9/alaska/joint-motion-2000-06-07.pdf`, PDF page 22; saved page image `tmp/alaska-proposal-page-22.png`. Inspected directly after the discrepancy was reported. The already preserved actual filing controls the description of what the parties proposed; a target Supreme Court disposition was not consulted.

Actual filing SHA256: ''' + digest(alaska_pdf) + '\n')

for name in ['OT_1999CHUNK9_STENBERG_NEUTRAL_EXPOSURE_RECEIPT.md','OT_1999CHUNK9_STENBERG_LB23_SOURCE_ADDITION.md','OT_1999CHUNK9_DALE_LAD_SOURCE.md','OT_1999CHUNK9_ALASKA_EO_CITATION_SOURCE_NOTE.md']:
    print(name + ' ' + digest(base/name))
