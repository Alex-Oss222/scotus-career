import json
from pathlib import Path
p=Path(__file__).with_name('assembly_torres.json')
d=json.loads(p.read_text())
d['blocks']['Holdings']=d['blocks']['Holdings'].replace("Covenant §203(c) expressly requires equal municipal representation; §501(b) preserves Congress's power to consent to that provision despite §501(a)'s application of specified guarantees as if the Commonwealth were a State.", "Covenant §203(c) expressly requires equal municipal representation. Section 501(a) makes Fourteenth Amendment §1 applicable as if the Commonwealth were a State, to the extent it does not apply of its own force; §501(b) preserves the validity of, and Congress's power to consent to, §203.")
d['blocks']['Separate Writings'] += ' His proposed remedy would not invalidate autonomous local island institutions.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print('Torres constitutional source and Stone remedy boundary made explicit; no Record written.')
