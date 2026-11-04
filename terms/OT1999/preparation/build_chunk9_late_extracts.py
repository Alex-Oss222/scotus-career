"""Copy operative source text and make smaller, case-specific law handoffs."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[3]
CACHE=ROOT/'tmp/ot1999_chunk9_late_sources'
PREP=ROOT/'terms/OT1999/preparation'
LAW=ROOT/'terms/OT1999/entering-law'

def source(name): return (CACHE/name).read_text(encoding='utf-8')
def between(s,a,b):
    start=s.index(a)
    return s[start:s.index(b,start+len(a))].strip()

parts=['# OT1999 chunk 9 - source terms copied for fresh neutral validation',
       'These are mechanical source copies, not new findings or adopted legal conclusions. OCR artifacts are retained. The labeled sources distinguish pleaded questions, enacted terms recited in judgments, and the exact approved simulation premise. The same-matter Supreme Court outcome and reasoning are not included.']
jobs=[
 ('Dale - petition question','https://archive.org/details/micro_IA40385014_0345','dale_02.txt','QUESTION PRESENTED','PARTIES TO THE PROCEEDING'),
 ('Mitchell - petitioners merits question','https://archive.org/details/micro_IA40385014_0270','mitchell_08.txt','QUESTION PRESENTED','PARTIES TO THE PROCEEDINGS'),
 ('Stenberg - petitioners merits questions','https://archive.org/details/micro_IA40385014_0347','stenberg_10.txt','QUESTIONS PRESENTED','LIST OF PARTIES'),
 ('Hill - all six statutory subsections reproduced below','https://static.case.law/p2d/973/html/1246-01.html','hill_lower.txt','(1) The general assembly recognizes','      5\n'),
 ('Mitchell - statutory terms reproduced in Part III.A','https://static.case.law/f3d/151/html/0347-01.html','mitchell_lower.txt','Chapter 2 provides financial assistance','Once Louisiana receives'),
 ('Stenberg - definition, exception and penalties recited below','https://static.case.law/f3d/192/html/1142-01.html','stenberg_lower.txt','No partial-birth abortion shall','Shortly after the passage'),
 ('Stenberg - statutory provisions recited in the merits brief, including patient immunity','https://archive.org/details/micro_IA40385014_0347','stenberg_10.txt','I. Neb.','III. U.S. Const.'),
 ('Stenberg - exact district-court judgment directions','https://archive.org/details/micro_IA40385014_0347','stenberg_03.txt','IT IS ORDERED that:','2. Judgment will be withheld'),
]
for title,url,file,a,b in jobs:
    parts += ['## '+title,'Source: ['+file+']('+url+').',between(source(file),a,b)]
neutral=(ROOT/'terms/OT1999/runtime/OT_1999CHUNK9_NEUTRAL.md').read_text(encoding='utf-8')
premise=next(line for line in neutral.splitlines() if line.startswith('* **Simulation Premise') and 'Chapter 2' in line)
parts += ['## Mitchell - exact approved operational premise',
          'Source: `terms/OT1999/runtime/OT_1999CHUNK9_NEUTRAL.md`, Mitchell Section I.A. Copied unchanged.',premise]
(PREP/'OT_1999CHUNK9_LATE_SOURCE_EXTRACTS.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')

s=(LAW/'OT_1999CHUNK9_LATE.md').read_text(encoding='utf-8')
def sections(text,level):
    ms=list(re.finditer(r'^#{'+str(level)+r'} (.+)$',text,re.M))
    return [(m.group(1),text[m.start():ms[i+1].start() if i+1<len(ms) else len(text)].strip()) for i,m in enumerate(ms)]
top=dict(sections(s,2))
current=top['Effective current-term public law and positions']
prior=top['Prior public Justice positions - scoped source copies']
case_standards={
 'DALE':[],
 'HILL':['Speech burdens in a content-neutral injunction'],
 'MITCHELL':['Lemon test','Private religious viewpoints in public forums and printing benefits'],
 'STENBERG':['Protected choice and the six-step standard for previability regulation','Medical emergency and the separate disclosure-health defense','North Dakota definitions and separate enforcement conditions']}
case_priors={'DALE':['Hurley'],'HILL':['Madsen','Schenck'],'MITCHELL':['Agostini','Jackson v. Benson'],'STENBERG':['Voinovich']}
for case in case_standards:
    ps=['# OT1999 chunk 9 - '+case+' entering-law copy',top['Chronology and reading scope']]
    for st in case_standards[case]:ps+=[top['Standards and Tests selection: '+st]]
    ps+=[top[case.title()+' - controlling prior holdings']]
    if case=='MITCHELL':ps+=[current]
    for title,body in sections(prior,3):
        if any(title.startswith(k+' - published source') for k in case_priors[case]) or (case=='DALE' and title.startswith('Hurley v.')):ps+=[body]
    out=LAW/('OT_1999CHUNK9_'+case+'.md');out.write_text('\n\n'.join(ps)+'\n',encoding='utf-8')
    print(out.name,out.stat().st_size)
print('Source extracts ready')
