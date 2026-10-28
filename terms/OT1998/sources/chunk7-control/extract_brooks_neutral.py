from pathlib import Path
from fetch_sources import Text
ROOT=Path(__file__).resolve().parent
h=(ROOT/'brooks_resource.html').read_text(encoding='utf-8')
a=h.index('<div class="num" id="p43">'); b=h.index('<div class="num" id="p54">',a)
p=Text(); p.feed(h[a:b]); t='\n'.join(x.strip() for x in ''.join(p.out).splitlines() if x.strip())
out='# Brooks — lower opinion paragraphs 43–53\n\nMechanically extracted verbatim from the retained Public.Resource.Org HTML source of 158 F.3d 1230, paragraphs 43–53. This is a lower-court opinion excerpt, not a Supreme Court ruling or an endorsed factual inference. Paragraph numbers and text are preserved. No source-control substantive conclusion is supplied.\n\n'+t+'\n'
dest=ROOT.parents[1]/'entering-law'/'OT_1998CHUNK7_BROOKS_PARAS43_53_NEUTRAL.md'
dest.write_text(out,encoding='utf-8'); print(dest.name)
