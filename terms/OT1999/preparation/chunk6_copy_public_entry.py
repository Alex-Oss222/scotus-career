from pathlib import Path
import argparse,re,os
ap=argparse.ArgumentParser();ap.add_argument('output',type=Path);ap.add_argument('source',type=Path);ap.add_argument('caption');a=ap.parse_args()
if not a.output.resolve().is_relative_to(Path('terms/OT1999').resolve()):raise SystemExit('Output outside term')
t=a.source.read_text(encoding='utf-8');heads=list(re.finditer(r'^### (.+)$',t,re.M));hits=[(i,m) for i,m in enumerate(heads) if m.group(1).startswith(a.caption)];assert len(hits)==1
i,m=hits[0];z=heads[i+1].start() if i+1<len(heads) else len(t);section=t[m.start():z].strip()
def relink(m):
 raw=m.group(1);path,sep,anchor=raw.partition('#');dest=(a.source.parent/path).resolve();relative=os.path.relpath(dest,a.output.resolve().parent).replace('\\','/')
 return ']('+relative+(sep+anchor if sep else '')+')'
section=re.sub(r'\]\((?!https?://|#)([^)]+)\)',relink,section)
text='# Date-eligible public position reading copy\n\nSource: '+a.source.as_posix()+'. Mechanically copied bounded public entry; no private material.\n\n'+section+'\n'
a.output.write_text(text,encoding='utf-8');print(a.output.as_posix())
