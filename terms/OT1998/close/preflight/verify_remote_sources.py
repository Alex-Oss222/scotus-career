from pathlib import Path
import urllib.request, urllib.error, urllib.parse, json, os, base64, hashlib, concurrent.futures
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'terms/OT1998/close/preflight'
REF='bba783c4cc408c15bc00b3b2492a5df22ae4d3f8'
BASE='https://api.github.com/repos/Alex-Oss222/scotus-career'
headers={'Accept':'application/vnd.github+json','User-Agent':'Codex-OT1998-close-source-verification'}
if os.environ.get('GH_TOKEN'):headers['Authorization']='Bearer '+os.environ['GH_TOKEN']
source=json.loads((OUT/'missing_record_link_targets.json').read_text())
paths=sorted({x['target'] for x in source['canonical_record_link_occurrences']})
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=25) as response:return json.load(response)
def resolve(rel):
    parts=Path(rel).parts
    if not rel.startswith('terms/OT1998/') or '..' in parts or 'stone' in parts or any(p.startswith('MASTER_JURISPRUDENCE') for p in parts):
        return {'path':rel,'status':'rejected unsafe path'}
    target=ROOT/rel
    try:
        meta=get(BASE+'/contents/'+urllib.parse.quote(rel,safe='/')+'?ref='+REF)
        if meta.get('type')!='file':return {'path':rel,'status':'not a file'}
        if meta.get('encoding')=='base64':data=base64.b64decode(meta['content'])
        else:
            blob=get(BASE+'/git/blobs/'+meta['sha'])
            if blob.get('encoding')!='base64':raise RuntimeError('unexpected blob encoding')
            data=base64.b64decode(blob['content'])
        blob_sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if blob_sha!=meta['sha']:raise RuntimeError('blob mismatch')
        for parent in target.parents:
            if parent==ROOT:break
            if parent.is_symlink():raise RuntimeError('symlink parent')
        if target.exists():
            if target.read_bytes()!=data:raise RuntimeError('existing bytes differ')
            status='existing identical'
        else:
            target.parent.mkdir(parents=True,exist_ok=True)
            with target.open('xb') as stream:stream.write(data)
            status='hydrated exact pinned-main bytes'
        return {'path':rel,'status':status,'bytes':len(data),'git_blob':blob_sha,'sha256':hashlib.sha256(data).hexdigest()}
    except urllib.error.HTTPError as exc:return {'path':rel,'status':'HTTP '+str(exc.code)}
    except Exception as exc:return {'path':rel,'status':type(exc).__name__+': '+str(exc)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:results=list(executor.map(resolve,paths))
receipt={'pinned_main':REF,'scope':'Canonical Record source links missing only from local checkout; original paths restored only from verified remote bytes','results':results}
(OUT/'REMOTE_SOURCE_HYDRATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'checked':len(results),'hydrated':sum(r['status']=='hydrated exact pinned-main bytes' for r in results),'existing_identical':sum(r['status']=='existing identical' for r in results),'unresolved':[r for r in results if 'git_blob' not in r]},indent=2))

