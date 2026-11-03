from pathlib import Path
import re
selected=[('terms/OT1996/output/OT_1996CHUNK12.md','Akins v. FEC'),('terms/OT1997/output/OT_1997CHUNK13.md','Federal Election Commission v. Maine Right to Life Committee')]
parts=['# NCRL additional date-eligible published positions','Derived verbatim reading copy from prior public renders. No private inputs or current-matter comparator appears. The cited public decisions supply the positions at their stated scope.']
for filename,caption in selected:
 text=Path(filename).read_text(encoding='utf-8')
 starts=list(re.finditer(r'^### (.+)$',text,re.M))
 found=[(i,m) for i,m in enumerate(starts) if m.group(1).startswith(caption)]
 assert len(found)==1
 i,m=found[0];end=starts[i+1].start() if i+1<len(starts) else len(text)
 section=text[m.start():end].strip()
 # Normalize prior artifact links relative to this new location.
 section=re.sub(r'\]\((?!https?://|#)([^)]+)\)',lambda m: ']('+__import__('os').path.relpath((Path(filename).parent/m.group(1).split('#')[0]).resolve(),Path('terms/OT1999/entering-law').resolve()).replace('\\','/')+('#'+m.group(1).split('#',1)[1] if '#' in m.group(1) else '')+')',section)
 parts+=['Source: '+filename,section]
Path('terms/OT1999/entering-law/OT_1999CHUNK6_NCRL_PUBLIC_POSITIONS.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
print('Copied two bounded public entries for neutral validation.')
