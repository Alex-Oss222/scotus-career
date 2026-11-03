from pathlib import Path
import argparse,re,os
ap=argparse.ArgumentParser();ap.add_argument('output',type=Path);ap.add_argument('records',type=Path,nargs='+');a=ap.parse_args()
if not a.output.resolve().is_relative_to(Path('terms/OT1999').resolve()):raise SystemExit('Output outside term')
parts=['# Effective current-term public law reading copy','Only bounded Public Projection blocks follow. Records remain authority. Apply each event only from its effective date; uncoordinated same-day decisions do not supply entering law to one another.']
for source in a.records:
 t=source.read_text(encoding='utf-8');mark='## Public Projection';assert t.count(mark)==1
 pp=t.split(mark,1)[1].strip()
 def relink(m):
  raw=m.group(1);path,sep,anchor=raw.partition('#');relative=os.path.relpath((source.parent/path).resolve(),a.output.resolve().parent).replace('\\','/')
  return ']('+relative+(sep+anchor if sep else '')+')'
 pp=re.sub(r'\]\((?!https?://|#)([^)]+)\)',relink,pp)
 parts+=['Source: '+source.as_posix(),pp]
a.output.write_text('\n\n'.join(parts)+'\n',encoding='utf-8');print(a.output.as_posix())
