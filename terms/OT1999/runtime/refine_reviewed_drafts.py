import json
from pathlib import Path
root=Path(__file__).parent
for stem in ['kimel','wardlow']:
    p=root/f'assembly_{stem}.json'
    d=json.loads(p.read_text(encoding='utf-8'))
    h=d['blocks']['Holdings']
    if stem=='kimel':
        h=h.replace('or relief for the specified retaliation violation. These distinct provisions are not collapsed into one identical rule, and no such filing is found here.', 'or legal or equitable relief for alleged violations of §215(a)(3), the prohibition on retaliation for protected FLSA complaints, proceedings or testimony. These distinct provisions are not collapsed into one identical rule, and no such governmental filing is adjudicated here.')
        h=h.replace("Parts II–III of {AUTHOR}'s opinion are joined in full by the other members of the five-Justice coalition: Stone-Zsela, Stevens, Souter, Ginsburg, and Breyer.", "Parts II–III of {AUTHOR}'s opinion have direct support from Stone-Zsela, Stevens, Souter, Ginsburg, and Breyer.")
    else:
        h=h.replace("Part II of {AUTHOR}'s opinion is joined by the other members of the five-Justice coalition: Stone-Zsela, Stevens, Souter, Ginsburg, and Breyer.", "Part II of {AUTHOR}'s opinion has direct support from Stone-Zsela, Stevens, Souter, Ginsburg, and Breyer.")
    d['blocks']['Holdings']=h
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print('Kimel termination language and both authority clauses refined; no Record written.')
