"""Copy current public decision blocks into the coordinated OT1996 projections."""
from pathlib import Path
import re
BASE=Path(__file__).resolve().parents[1]
NAMES=['Agostini_v_Felton_merits_1997-06-23.md','City_of_Boerne_v_Flores_merits_1997-06-25.md','Lawyer_v_Department_of_Justice_merits_1997-06-25.md']
EXPECTED=['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes']
def nested(text):
    return re.sub(r'^(#{3,}) ',r'##\1 ',text,flags=re.M)
def parsed(name):
    text=(BASE/'records'/name).read_text(encoding='utf-8')
    public=text.split('\n## Public Projection\n',1)[1].strip()
    headings=list(re.finditer(r'^## (.+)$',public,re.M))
    blocks={m.group(1):public[m.end():headings[i+1].start() if i+1<len(headings) else len(public)].strip() for i,m in enumerate(headings)}
    if list(blocks)!=EXPECTED: raise RuntimeError('Invalid public blocks: '+name)
    result=re.search(r'^\*\*Result:\*\* (.+)$',text,re.M).group(1)
    return blocks,result
for filename in ['continuity.md','neutral-projection.md']:
    path=BASE/'workspace'/filename
    raw=path.read_bytes(); text=raw.decode('utf-8').replace('\r\n','\n')
    for name in NAMES:
        blocks,result=parsed(name)
        link='Authority: [Record](../records/'+name+').'
        pattern=re.compile(r'^### [^\n]+\n\n'+re.escape(link)+r'\n\n[\s\S]*?(?=^### |^## |\Z)',re.M)
        matches=list(pattern.finditer(text))
        if len(matches)!=3: raise RuntimeError((filename,name,'expected three public projections',len(matches)))
        replacements=[]
        for i,m in enumerate(matches):
            header=m.group(0).split(link,1)[0]+link+'\n\n'
            if i==0:
                body='\n\n'.join('#### '+k+'\n\n'+nested(blocks[k]) for k in ['Holdings','Precedent Treatment','Law After Decision'])
            elif i==1: body=nested(blocks['Separate Writings'])
            else: body=nested(blocks['Procedure After Action'])
            replacements.append((m.start(),m.end(),header+body+'\n\n'))
        for start,end,replacement in reversed(replacements): text=text[:start]+replacement+text[end:]
        if filename=='continuity.md':
            lines=text.splitlines(keepends=True)
            targets=[i for i,l in enumerate(lines) if l.startswith('| ') and ('[Record](../records/'+name+')') in l]
            if len(targets)!=1: raise RuntimeError('Missing completed-event row: '+name)
            i=targets[0]; cells=lines[i].strip().strip('|').split('|')
            if len(cells)!=4: raise RuntimeError('Unexpected event row')
            cells[2]=' '+result+' '
            lines[i]='|'+'|'.join(cells)+'|\n'
            text=''.join(lines)
    newline='\r\n' if b'\r\n' in raw else '\n'
    path.write_bytes(text.replace('\n',newline).encode('utf-8'))
    print(path)
