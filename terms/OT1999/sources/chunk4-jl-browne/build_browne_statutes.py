from pathlib import Path
import re
import pymupdf

base = Path('terms/OT1999/sources/chunk4-jl-browne')
out = Path('terms/OT1999/entering-law/OT_1999CHUNK4_BROWNE_STATUTES.md')
parts = ['# Browne — statutory reading copy\n\nDerived verbatim copies only. Source texts, effective dates and applicable enacted amendments control. Some copied historical text has OCR or line-break defects; no computation is authorized by this copy. The neutral packet identifies the applicable transitions and the claims actually presented.']

for name, num, nxt in [('USCODE-1994-title26-chap65.txt', '6404', '6405'), ('USCODE-1994-title26-chap76.txt', '7421', '7422'), ('USCODE-1994-title26-chap76.txt', '7422', '7423'), ('USCODE-1994-title26-chap67.txt', '6601', '6602')]:
    p = (base / name).read_text(encoding='utf-8')
    start = p.index('§ ' + num + '. ')
    end = p.index('§ ' + nxt + '. ', start + 10)
    sec = p[start:end]
    stop = sec.find('(Aug. 16, 1954')
    if stop >= 0:
        sec = sec[:stop]
    parts.append('\n## 1994 Code section ' + num + '\n\nSource: ../sources/chunk4-jl-browne/' + name + '\n\n' + sec.strip())

d = pymupdf.open('terms/OT1999/sources/chunk4-neutral/USCODE-1994-title26-chap68.pdf')
p = '\n'.join(x.get_text() for x in d)
for num, nxt in [('6651', '6652'), ('6654', '6655')]:
    start = re.search(r'§\s*' + num + r'\.\s*Failure', p).start()
    end = start + 10 + re.search(r'§\s*' + nxt + r'\.', p[start + 10:]).start()
    sec = p[start:end]
    stop = sec.find('(Aug. 16, 1954')
    if stop >= 0:
        sec = sec[:stop]
    parts.append('\n## 1994 Code section ' + num + '\n\nSource: ../sources/chunk4-neutral/USCODE-1994-title26-chap68.pdf\n\n' + sec.strip())

for name, heads in [('PL104-168.txt', ['SEC. 301. EXPANSION', 'SEC. 302. REVIEW']), ('PL105-206.txt', ['SEC. 3305. SUSPENSION', 'SEC. 3309. ABATEMENT'])]:
    p = (base / name).read_text(encoding='utf-8')
    for head in heads:
        start = p.index(head)
        m = re.search(r'\nSEC\. \d+', p[start + len(head):])
        end = start + len(head) + m.start() if m else len(p)
        parts.append('\n## Enactment and transition\n\nSource: ../sources/chunk4-jl-browne/' + name + '\n\n' + p[start:end].strip())

parts.append('\n## Required presidential designation, July 22, 1998\n\n' + (base / '1998-07-22-presidential-designation.txt').read_text(encoding='utf-8'))
p = (base / 'micro_IA40386014_0207 1. Petition for Writ of Certiorari_djvu.txt').read_text(encoding='utf-8')
rs = p.index('(c) SHOWING OF REASONABLE CAUSE.')
for title, start, end in [('RFRA reproduced in petition appendix', p.index('42 U. S. Code Chapter'), p.index('Treas. Regs. SECTION 301.6404-0.')), ('Treasury Regulation 301.6651-1(c), reproduced in petition appendix', rs, p.index('Internal Revenue Manual', rs))]:
    parts.append('\n## ' + title + '\n\nSource: petition appendix, Archive item micro_IA40386014_0207.\n\n' + p[start:end].strip())

parts.append('''
## Scope and unresolved forum construction

The 1996 expansion of section 6404(e) applies to tax years beginning after July 30, 1996, so the original ministerial-act text governs the 1993–95 liabilities. The separate 1996 judicial-review provision applies to requests made after that enactment and was renumbered to section 6404(i) in 1998; its statutory text creates an action to review interest-abatement discretion and specifies claimant eligibility and a 180-day mailing condition. It does not by its own text condition that action on a section 6213 deficiency petition. Whether that route excludes the pleaded RFRA interest-refund theory is an issue to decide, not a conclusion supplied by this copy. The 1998 new suspension/disaster relief does not automatically cover these 1993–95 liabilities. The government separately invoked 28 U.S.C. 2201 and 26 U.S.C. 7421 against prospective relief; exact full title 28 statutory text was not recovered in the attempted official 1994 endpoints. No new construction of those forum/remedy provisions is supplied by the preparation. Original party briefs and preserved arguments are available for independent threshold adjudication.
''')
out.write_text('\n'.join(parts) + '\n', encoding='utf-8')
print(out.as_posix(), len(out.read_bytes()))
