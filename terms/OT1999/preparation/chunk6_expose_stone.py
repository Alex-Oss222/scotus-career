"""Copy only one stage-authorized supplement from the mechanical runtime split."""
from pathlib import Path
import argparse,re
ap=argparse.ArgumentParser();ap.add_argument('caption');ap.add_argument('key');a=ap.parse_args()
assert re.fullmatch('[A-Z_]+',a.key)
folder=Path('terms/OT1999');source=folder/'runtime/OT_1999CHUNK6_STONE.md'
t=source.read_text(encoding='utf-8');starts=list(re.finditer(r'^# STONE PRE-VOTE CASE BRIEF\s*$',t,re.M));found=[]
for i,m in enumerate(starts):
 z=starts[i+1].start() if i+1<len(starts) else len(t);part=t[m.start():z]
 header=part.split('# SECTION II',1)[0]
 if a.caption in header:found.append(part.strip()+'\n')
assert len(found)==1,(a.caption,len(found))
target=folder/'runtime'/f'OT_1999CHUNK6_{a.key}_STONE.md'
target.write_text('# Approved per-matter assembly reading copy\n\nMechanically copied from the current runtime split; no independent revision.\n\n'+found[0],encoding='utf-8')
print(target.as_posix())
