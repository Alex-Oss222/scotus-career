from pathlib import Path
import urllib.request, urllib.parse, json
out = Path('terms/OT2001/sources/chunk6-a')
out.mkdir(parents=True, exist_ok=True)
items = {'holmes':'micro_IA40385014_0502','zandford':'micro_IA40385014_0490','echazabal':'micro_IA40385014_0454','devlin':'micro_IA40385014_0503','lile':'micro_IA40385014_0447'}
for key, item in items.items():
    data = json.load(urllib.request.urlopen('https://archive.org/metadata/'+item, timeout=30))
    choices = [x for x in data['files'] if x['name'].endswith('_djvu.txt') and any(t in x['name'] for t in ['Petition for','Petitioners Brief','Respondents Brief','Joint Appendix','Reply Brief'])]
    print(key, [x['name'].split(' ',1)[1] for x in choices], flush=True)
    for entry in choices:
        name = entry['name']
        url = 'https://archive.org/download/'+item+'/'+urllib.parse.quote(name)
        filename = key+'-'+name.split(' ',1)[1].replace(' ','_')
        target = out/filename
        if target.exists():
            continue
        try:
            request = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
            content = urllib.request.urlopen(request, timeout=25).read().decode('utf-8')
        except Exception as error:
            print('download unavailable', filename, str(error), flush=True)
            continue
        target.write_text('Source: '+url+'\n\n'+content, encoding='utf-8')
        print('saved', filename, len(content), flush=True)
