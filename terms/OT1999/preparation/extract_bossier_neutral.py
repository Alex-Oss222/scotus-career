from pathlib import Path
import re

root = Path('terms/OT1999/preparation')
s = (root/'chunk2-control-sources/USREPORTS-528-320.txt').read_text(encoding='utf-8')
# Only pagination/running headers are removed; excerpt body is copied verbatim.
s = re.sub(r'\n--- PDF PAGE \d+ ---\n\d+\n(?:Cite as: 528 U. S. 320 \(2000\)|RENO v. BOSSIER PARISH SCHOOL BD\.)\n(?:Opinion of the Court|Opinion of Souter, J\.)\n', '\n', s)
def take(a,b,start=0):
    i=s.index(a,start); j=s.index(b,i)
    return s[i:j].strip()
pieces = [
('Procedural background, 528 U.S.323-326', take('Like every other political subdivision', '\nII\nBefore proceeding')),
('Mootness positions and election timing, 528 U.S.327; statements are claims, not findings', take('The Board contends that these', '\nWe need not pause')),
('Stipulated school-desegregation history and conflicting testimony, 528 U.S.344', take('As the parties have stipulated', '\nWhen the Board') + '\n\n[Excerpt break]\n\n' + take('During the 1980', '\nOther evidence')),
('Advisory committee history, 528 U.S.345', take('Although the Board rep-', '\n“Policy,”')),
('Timing and districting features, 528 U.S.346-347', take('Fol-\nlowing the rebuff from the Police Jury', '\nIn addressing the need')),
('Requests to participate and presentation of the NAACP map, 528 U.S.347-348', take('The Board then spent nearly a year', '\nThere is evidence')),
('Attributed statements, 528 U.S.348; preserve dispute shown in following excerpt', take('According to one\nblack leader', '\nAlthough the NAACP plan')),
('Dispute concerning attributed statement, 528 U.S.348 n.4', take('4 Musgrove denied making the statement.', '\nIf, as the')),
('Adoption chronology, 528 U.S.348-349', take('Although the NAACP plan received no further public con-', '\n3 One other') + '\n\n' + take('hearing on the plan one week later', '\nII\nThe signiﬁcance')),
('Board admissions concerning effect, 528 U.S.349', take('The Board has also conceded the discrimi-', '\nEven without')),
('District feasibility stipulations, 528 U.S.350', take('The Board joined in a stipulation', '\nAs to the sec-')),
('Polarization evidence and limitation, 528 U.S.350-351', take('As to the sec-', '\nSecond, the Police Jury plan', s.index('The Board does not dispute'))),
('Board cartographer testimony, 528 U.S.351', take('Even the Board', '\n6 The parties agreed')),
('Election-evidence qualification, 528 U.S.351 n.6', take('6 The parties agreed', '\n7 Counsel')),
('Precinct changes: objection, available process, consultation, 528 U.S.352', take('The Board’s cartographer and lawyer objected', '\nJudge Kessler')),
('Precinct counts, 528 U.S.352 n.8', take('While the NAACP plan required 46 precinct splits', '\nSecond, and more importantly')),
('Consultant testimony, 528 U.S.353', take('Joiner\nacknowledged in his testimony', '\nSplitting pre-')),
]
header = '''# Bossier Parish - sanitized source extracts for neutral validation

Source: Official United States Reports, 528 U.S.320; source URL https://www.govinfo.gov/content/pkg/USREPORTS-528/pdf/USREPORTS-528-320.pdf

Exact excerpts were copied mechanically from the official report; running headers and pagination alone were removed. These are selected factual, procedural, stipulated, and attributed evidentiary recitations, not target Court conclusions. Fresh neutral validation must preserve whether each proposition is a stipulation, admission, allegation, disputed testimony, or lower-court finding. Historical prior procedural recitations require consistency checking against current simulated law. The originals of the briefs and appendix have not been independently read; this source establishes published recitation only.

**Material limit:** The official opinion's record recitation reports findings of legitimate purposes (prompt preclearance and ease of implementation), but does not supply a distinct finding that the Board would have adopted the identical plan absent racial purpose. Do not convert one into the other. A needed same-decision finding must be supported independently or remain unresolved. The Board's claimed lack of future use and opponents' proposed special-election relief remain arguments. The excerpts omit the target Court's resolution of those issues. The heading labels below are source classifications, not findings by this preparation.

'''
out=header+'\n\n'.join('## '+title+'\n\n'+text for title,text in pieces)+'\n'
(root/'OT_1999CHUNK2_BOSSIER_NEUTRAL_SOURCE_EXTRACT.md').write_text(out,encoding='utf-8')
print(len(out), 'characters; excerpts',len(pieces))
