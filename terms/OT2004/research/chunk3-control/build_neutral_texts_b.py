from pathlib import Path
import hashlib, json

base=Path(__file__).resolve().parent
k=(base/'karaha-official.txt').read_text(encoding='utf-8')
c=(base/'convention-official-canada.txt').read_text(encoding='utf-8')
u=(base/'section207-cornell.txt').read_text(encoding='utf-8')

def span(text,start,end):
 a=text.index(start); b=text.index(end,a)
 return text[a:b].rstrip()

clauses=[
 ('JOC article 13.2(a), (d), quoted at pp. 5–6 n.7', span(k,'If the Dispute cannot be settled within thirty','JOC, Art. 13.2(a),(d).')),
 ('ESC section 8.2(a), quoted at pp. 5–6 n.7', span(k,'If the Dispute cannot be settled within forty-five','\n5\ngenerated.')+'\n'+span(k,'the appointment of the second arbitrator, to act','Both contracts contained the following additional')),
 ('Common finality/enforcement clause, p. 6 n.7',span(k,'The award rendered in any arbitration commenced','\n6\nOn September')),
 ('Common governing-law clause, p. 22 n.30',span(k,'provided:  “This Contract shall be governed','\n31  Pertamina')),
 ('Indonesian procedural references, pp. 22–23 n.31',span(k,'The parties expressly agree to waive the','\n22\nUnless')+'\n'+span(k,'Procedure so that the arbitration need not be','\n32  Albert')),
 ('Convention Article V(1) opening condition',span(c,'1\u00a0Recognition and enforcement of the award may be refused','\n(a)')),
 ('Convention Article V(1)(e)',span(c,'(e)\u00a0The award has not yet become binding','\n2\u00a0Recognition')),
 ('Convention Article VI',span(c,'Article VI\n','\nArticle VII')),
 ('9 U.S.C. §207',span(u,'Within three years after an arbitral award','\nStatutory Notes')),
]
head='''# Neutral exact texts — Karaha Bodas

Mechanically copied from saved downloaded sources by `build_neutral_texts_b.py`. Original source line breaks, ellipses, and brackets are retained. These are the opinion's quoted contract passages, not a claim that the underlying contracts were recovered in full. No reviewing disposition or reasoning appears here. The paragraphs split by PDF page layout are joined only at their exact continuation; no words have been supplied.

Contract source: official Fifth Circuit opinion, https://www.ca5.uscourts.gov/opinions/pub/02/02-20042-CV0.wpd.pdf, pp. 5–6 n.7 and 22–23 nn.30–31. Convention source: the treaty text reproduced by Canada's Department of Justice, https://laws-lois.justice.gc.ca/eng/acts/U-2.4/page-2.html. Only the 1958 treaty is used, not Canadian implementing law. Section 207 source: https://www.law.cornell.edu/uscode/text/9/207; its source credit records the 1970 enactment and no subsequent amendment. Current web-page dates do not change those historical texts.

The Convention's remaining defenses are not silently repealed by this bounded extract. Article V(1)'s request-and-proof language applies to subsection (e). Article VI's discretion and the enforcing party's application condition for security must remain distinct.

'''
(base/'NEUTRAL_TEXTS_B.md').write_text(head+'\n\n'.join('## '+title+'\n\n```text\n'+body+'\n```' for title,body in clauses)+'\n',encoding='utf-8')
# Retain only the operative public texts, without site navigation.
(base/'convention-official-canada.txt').write_text(span(c,'Article I\n','\nTable of Contents') if '\nTable of Contents' in c else c,encoding='utf-8')
(base/'section207-cornell.txt').write_text(span(u,'Within three years after an arbitral award','\nU.S. Code Toolbox') if '\nU.S. Code Toolbox' in u else u,encoding='utf-8')
receipt={'sources':[{'file':name,'sha256':hashlib.sha256((base/name).read_bytes()).hexdigest()} for name in ['karaha-official.txt','convention-official-canada.txt','section207-cornell.txt']], 'limits':'UNCITRAL 37-page PDF download produced no usable substantive text and was not relied upon or certified as read. Official Canadian reproduction of all sixteen treaty articles read in full instead. Current Cornell section 207 and enactment credit read in full.'}
(base/'neutral-texts-b-receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print('NEUTRAL_TEXTS_B.md: exact source substrings copied')
