from pathlib import Path
import re
import argparse
ap=argparse.ArgumentParser()
ap.add_argument('output');ap.add_argument('pattern');args=ap.parse_args()
out=Path(args.output).resolve();root=Path(__file__).resolve().parents[3]
assert out.is_relative_to(root/'terms/OT1999')
parts=['# Earlier published positions','', 'Mechanically copied bounded public entries. Their controlling and noncontrolling status is unchanged.']
found=[]
for year in range(1991,1999):
    for p in (root/'terms'/f'OT{year}'/'output').glob('*.md'):
        text=p.read_text(encoding='utf-8');matches=list(re.finditer(r'^### (.*)$',text,re.M))
        for i,m in enumerate(matches):
            if re.search(args.pattern,m[1]):
                end=matches[i+1].start() if i+1<len(matches) else len(text)
                parts+=['','Source: '+p.relative_to(root).as_posix(),'',text[m.start():end].strip()]
                found.append(m[1])
out.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('\n'.join(found))
