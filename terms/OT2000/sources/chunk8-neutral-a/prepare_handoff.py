from pathlib import Path
import re
import urllib.request
from html.parser import HTMLParser

base = Path('terms/OT2000')
sources = base / 'sources/chunk8-neutral-a'
class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]
    def handle_data(self, value): self.parts.append(value)

for sec in ['2244', '2254', '2263']:
    chapter = '154' if sec == '2263' else '153'
    url = f'https://www.govinfo.gov/content/pkg/USCODE-2000-title28/html/USCODE-2000-title28-partVI-chap{chapter}-sec{sec}.htm'
    raw = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read().decode()
    parser = Parser(); parser.feed(raw)
    text = '\n'.join(v.strip() for v in parser.parts if v.strip())
    start=text.index('\u00a7'+sec+'.')
    end=text.find('\n(Added ',start)
    if end<0: end=text.find('\n(June ',start)
    if end<0: end=len(text)
    (sources / f'28-USC-{sec}-2000.txt').write_text(text[start:end]+'\n',encoding='utf-8')

def read(name): return (sources/name).read_text(encoding='utf-8')
def span(text, first, last, offset=0):
    a=text.index(first,offset); b=text.index(last,a)
    return text[a:b].strip()
parts=['# Source text for the June 18 matters',
       'These are script-copied passages from the identified source texts. Archival OCR preserves its spelling and page breaks; quoted dispositive wording should be checked against the linked source where OCR is uncertain. No historical Supreme Court disposition in the present matters is included.']
for sec in ['2244','2254','2263']:
    parts += [f'## 28 U.S.C. {sec}: 2000 edition',read(f'28-USC-{sec}-2000.txt')]
s=read('Freiler_2._Petition_for_Writ_of_Certiorari.txt')
parts += ['## Freiler: resolution, petition page 2',
          'Source: Internet Archive item micro_IA40385014_0363, petition, page 2. The first paragraph instructs teachers; only the next two are to be read. The final paragraph uses "or", not the panel opinion\'s initially printed "and". The rehearing material acknowledges that correction.',
          span(s,'Whenever, in classes of elementary or high school,',"' Although the resolution",10000)]
s=read('Idaho_08._Joint_Appendix_Vol_I.txt')
parts += ['## Idaho: 1873 order, Joint Appendix pages 47-48',
          span(s,'November 8, 1873.','U. S. GRANT.',60000)+'\nU. S. GRANT.',
          '## Idaho: 1888 railroad enactment, Joint Appendix pages 137-140',
          span(s,'May 30, 1888.','STAT I.',190000),
          '## Idaho: 1889 negotiation enactment, Joint Appendix page 144',
          span(s,'Act of March 2, 1889','145',200000)]
s=read('Idaho_09._Joint_Appendix_Vol_II.txt')
parts += ['## Idaho: admission and accepted constitutional terms, Joint Appendix pages 370-372',
          span(s,'EXHIBIT 2294','EXHIBIT 205',174000)]
(base/'entering-law/OT_2000CHUNK8_A_SOURCE_TEXT.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')

runtime=(base/'runtime/OT_2000CHUNK8_NEUTRAL.md').read_text(encoding='utf-8')
names=['Duncan v. Walker','Idaho v. United States','Freiler v. Tangipahoa Parish Board of Education']
modules=[]
for name in names:
    m=re.search(r'^# '+re.escape(name)+r'\s*$',runtime,re.M)
    nxt=re.search(r'^# (?!SECTION)[^\n]+',runtime[m.end():],re.M)
    modules.append(runtime[m.start():m.end()+nxt.start() if nxt else len(runtime)].strip())
duncan,idaho,freiler=modules
duncan=duncan.replace("**Question Granted:** Faithful formulation of the statutory question reviewed; the petition's precise wording has not been independently verified.","**Question Granted:** The statutory question is independently verified in the petitioner's merits brief, page i: whether a prior federal habeas petition is an application for State post-conviction or other collateral review within section 2244(d)(2).")
duncan=duncan.replace('**Uncertainty:** The complete first and second petitions and any request for equitable relief are unavailable. The record does not establish government obstruction, court misdirection, or extraordinary circumstances preventing timely refiling. Such facts cannot be assumed to avoid either construction\'s consequences.',
'**Source clarification:** The archived Joint Appendix contains the first and second federal pleadings. The respondent\'s merits brief, page 5, confirms that equitable tolling was argued below and not reached by the court of appeals. No finding of government obstruction, misleading judicial instruction, or extraordinary prevention of timely refiling is established by this preflight. Availability of equitable relief, its governing standard, and entitlement on this record must not be conflated; reversal of statutory tolling may leave the preserved equitable argument for lawful lower-court consideration.')
duncan=duncan.replace('**Record limitation:** The available record does not include a separate petition appendix or complete trial transcript. Unverified details are not findings.',
'**Record support:** The archive supplies the petition appendix, both merits briefs, and the Joint Appendix. Relevant federal pleadings and lower orders are included there. This preflight does not certify a complete page-by-page review of the large appendix or decide the underlying robbery claims. No specific material fact is declared unavailable.')
duncan += '\n\n## Preflight supplement: preserved alternative and scope\n\nRespondent also argues that timely filing itself satisfies section 2244(d)(1), so that time should not continue running while the initial habeas application is pending; he invokes American Pipe and Burnett as support for judicial tolling consistent with statutory purpose. This is a litigated alternative, not an invented concession. The contrary path distinguishes timeliness of the original application from timeliness of a new application after dismissal, and distinguishes statutory exclusion from equitable protection. Respondent further asks, if federal pendency does not suspend time, for prompt exhaustion decisions and notice/election procedures before dismissal; this is a requested safeguard, not an existing general duty supplied by entering law. Neither the statutory question nor the existence of the request establishes that such a duty resolves Walker\'s own later filing. Sections 2254(b)(1)-(3) retain exhaustion, the permission to deny an unexhausted application on the merits, and express counsel waiver; denial permission is not a command. Source: respondent merits brief, pages 16-28.\n\nThe first petition combined section 1983 and habeas claims. The district court could not determine exhaustion; it did not adjudicate the claims on their merits. Petitioner\'s brief, pages 8-10, identifies the first pleading at Joint Appendix 79a-90a and the second at 23a-46a. The first included counsel-withdrawal allegations across the robbery judgments; the second concerned the third conviction and pleaded disclosure and lineup-counsel grounds. These source descriptions do not establish an independent filing defect or permit an unpresented merits resolution.\n'
freiler=freiler.replace('The Fifth Circuit found that the disclaimer\'s text and context protected a particular religious account and undermined its asserted purposes of critical thinking and intellectual freedom.',
'The Fifth Circuit rejected the claimed critical-thinking purpose but accepted two other purposes as sincere and secular: disclaiming an orthodoxy inferable from evolution\'s exclusive curricular placement and reducing offense to students and parents. It nevertheless held the actual text and context impermissibly advanced the protected biblical account under the effect and endorsement approaches. The district court had instead invalidated the resolution for lack of a secular purpose. These are distinct lower-court grounds.')
freiler += '\n\n## Preflight supplement: text, record, review scope, and remedy\n\nThe entire resolution is copied in the Source Text slice from the petition, page 2. It preserves the operative OR between forming one\'s own opinion and maintaining parental beliefs. The panel\'s initial AND transcription was acknowledged on rehearing; its constitutional judgment remained its own. The teacher-direction paragraph itself is not one of the two paragraphs to be read to students. Evaluate the actual complete resolution, not the transcription error or a shortened paraphrase.\n\nThe lower court considered the disclaimer as a whole and expressly did not decide whether its first spoken paragraph alone would be invalid. A court may explain why a particular feature matters without rewriting the school board\'s policy or presuming severability. Preservation of lawful academic study, ordinary conscience protection, and private expression does not require a replacement curriculum.\n\nThe Fifth Circuit also affirmed a section 1988 fee award of $49,444.50; the verified petition question concerns only the constitutional disclaimer. There is no independently verified fee-calculation question in the supplied review. The fee judgment is background and may have an ordinary consequence if the underlying merits judgment changes; no new fee rule or amount should be invented. The district court also referred to Louisiana\'s parallel constitutional provision. The appellate judgment reviewed here rests on the federal First Amendment and identifies that as its sole constitutional issue; the lower state reference does not establish an independently sufficient, separately analyzed state-law ground.\n\nThe April 1994 adoption discussion and the resolution are recoverable in the petition appendices; the petition, opposition and reply are retained. This is the supplied merits event following the supplied pending grant. No historical Supreme Court petition disposition is adopted, and no argument date is invented. The assigned June 18 date is a scheduling premise. The neutral legal arguments may be developed under intervening controlling law, without pretending that nonexistent post-grant briefs were filed.\n'
header='''# OT2000 chunk 8: June 18 neutral handoff A

Scope: Duncan v. Walker; Idaho v. United States; Freiler v. Tangipahoa Parish Board of Education. Decision-making is reserved for independent modeling. The supplied matter descriptions identify the anticipated merits stage; ordinary jurisdiction, preservation, reachability, and lawful narrower dispositions remain to be assessed under the Engine.

## Entering law and chronology

Research cutoff: June 18, 2001. These uncoordinated events share the baseline immediately before that date. Same-date Saucier and Mead do not govern them. Later events in this chunk do not enter. No material participation exception is identified; the seated Court is in the Standards slice.

Read these derived slices with the neutral case modules:

- [Selected Holdings](../entering-law/OT_2000CHUNK8_A_HOLDINGS.md)
- [Standards and roster](../entering-law/OT_2000CHUNK8_A_STANDARDS.md)
- [Effective current-term law and published positions](../entering-law/OT_2000CHUNK8_A_CURRENT.md)
- [Earlier published positions](../entering-law/OT_2000CHUNK8_A_PUBLIC_POSITIONS.md)
- [Exact source texts](../entering-law/OT_2000CHUNK8_A_SOURCE_TEXT.md)

Artuz, effective November 7, supplies the distinction between application-filing rules and claim-relief bars. It does not answer federal pendency. Good News Club, effective June 11, preserves the distinction between genuinely private access and official instruction, religious adoption, solicitation, or pressure. Children's Healthcare, effective April 23, preserves the limited accommodation and actual-function inquiries; Marshfield, effective February 27, preserves examination of the continuing actual governmental presentation. None decides this curriculum. Atkinson's May 29 fee-land tax ruling neither determines ownership nor replaces the Alaska title test. The Alaska implementing decree carries the earlier title test forward without new assent to its rationale. Coeur d'Alene's earlier immunity disposition does not decide this United States title suit.

The source texts and preserved party arguments support alternative paths; their historical post-divergence descriptions of other Supreme Court decisions are not independent current law. Use the supplied Holdings and public-position slices for those authorities. Current-case Supreme opinion links in the original modules identify the supplied factual provenance only and are not an invitation to read a historical disposition during modeling.

'''
(base/'freeze/OT_2000CHUNK8_NEUTRAL_A.md').write_text(header+'\n\n'.join([duncan,idaho,freiler])+'\n',encoding='utf-8')
print('Wrote neutral handoff and source texts')
