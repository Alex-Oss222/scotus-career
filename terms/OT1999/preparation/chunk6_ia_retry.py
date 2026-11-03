from pathlib import Path
import json,urllib.request,urllib.parse
out=Path('terms/OT1999/sources/chunk6-records')
metadata=json.loads((out/'geier-metadata.json').read_text(encoding='utf-8'))
for suffix in ['06. Petitioners Brief_djvu.txt','07. Respondents Brief.pdf','07. Respondents Brief_djvu.txt']:
 target=out/('geier-'+suffix)
 if target.exists(): continue
 filename='micro_IA40385014_0277 '+suffix
 url='https://'+metadata['d1']+metadata['dir']+'/'+urllib.parse.quote(filename)
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (legal research)'})
  target.write_bytes(urllib.request.urlopen(req,timeout=60).read())
  print(suffix,'saved')
 except Exception as e:print(suffix,str(e))
receipt='''# Carmell and Geier record-source retrieval

The Internet Archive collection's own advanced-search listing was searched separately by docket and case name. Saved query responses identify Carmell as micro_IA40385014_0295 and Geier as micro_IA40385014_0277. Item metadata and per-document text/PDF sources were downloaded. The individual petition, joint appendix and merits-brief files are separable from the combined volume. Combined micro_* files include historical Supreme Court opinion material and are excluded from neutral modeling.

Retrieval alone is not a claim of full substantive reading. No conclusion that a fact or citation is absent from these records rests on this retrieval. Stage-specific supplements identify passages actually used. Original filing images and OCR remain sources; OCR discrepancies require checking the saved PDF.

Public source locations: https://archive.org/details/micro_IA40385014_0295 and https://archive.org/details/micro_IA40385014_0277 .
'''
(out/'RETRIEVAL.md').write_text(receipt,encoding='utf-8')
