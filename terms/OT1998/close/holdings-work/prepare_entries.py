from pathlib import Path
import json,re,hashlib,unicodedata

ROOT=Path(__file__).resolve().parents[4]
WORK=ROOT/'terms/OT1998/close/holdings-work'
ROWS=json.loads((WORK/'record_extractions.json').read_text())

def normalize(text):
    text=unicodedata.normalize('NFKC',text).replace('’',"'")
    return re.sub(r'[^\w]+',' ',text).lower().strip()

def identity(r):
    h=r['header'].replace('**Case and dockets:** ','').strip()
    cut=re.search(r';|, No\.?s?\.? |; No',h)
    name=h[:cut.start()] if cut else h
    tail=h[cut.end():].strip() if cut else 'No separately established Supreme Court docket.'
    if cut and cut.group().startswith(', No'):tail='No. '+tail
    tail=re.sub(r';?\s*OT1998\.?','',tail).strip()
    return name,tail

def transform(r):
    ss=r['sections']; h=ss.get('Holdings','')
    # Copy only the Record's operative rule, controlling authority, and express
    # application/limit blocks. The legal admission/area map is separately reviewed.
    h=re.sub(r'\*\*Controlling explanation[^*]*\*\*.*?(?=\n\*\*|\n#{3,6} |\Z)','',h,flags=re.S)
    h=re.sub(r'^#{3,6} ', '##### ',h,flags=re.M)
    h=re.sub(r'\*\*(?:Holding and operative rule|Operative rule)[.:]?\*\*:?','**Holding:**',h)
    h=re.sub(r'\*\*(?:Authority|Common authority|Authority and scope)[.:]?\*\*:?','**Proposition-level authority:**',h)
    h=re.sub(r'\*\*(?:Limits|Questions not reached|Operative qualifications retained)[.:]?\*\*:?','**Limits and questions not reached:**',h)
    h=re.sub(r'\*\*Application[.:]?\*\*:?','**Material application:**',h)
    h=re.sub(r'\*\*(?:Application, remedy and limits|Application and limits|Common limits and remedy|Limits and remedy|Questions not reached and remedial limits|Remand limit)[.:]?\*\*:?','**Limits and operative remedy:**',h)
    h=re.sub(r'\n{3,}','\n\n',h).strip()
    return h

def draft(chunks,areas,excluded=None):
    excluded=excluded or {}; result=[]; checks=[]
    for r in ROWS:
        if r['chunk'] not in chunks:continue
        f=r['file'];name,dockets=identity(r)
        if f in excluded:
            result.append({'file':f,'excluded':excluded[f]});continue
        area=areas[f.split('_merits_')[0].split('_threshold_')[0].split('_application_')[0]]
        h=transform(r)
        if not h.startswith('#####') and not re.search(r'^##### ',h,re.M):
            h='##### The question resolved by the Court\n\n'+h
        ss=r['sections']
        text=f'#### {name}\n\n**Docket or dockets:** {dockets}\n**Decided:** {r["date"]}.\n\n'+h
        if ss.get('Precedent Treatment'):text+='\n\n**Treatment of earlier authority:**\n\n'+ss['Precedent Treatment']
        if ss.get('Law After Decision'):text+='\n\n**Limits and questions not reached:** '+re.sub(r'^As of [^,]+, \d{4}, ','',ss['Law After Decision'])
        # The final editorial pass selects legally operative mandate components.
        text+='\n\n**Operative remedy or transition:** '+ss.get('Judgment & Remedy','')
        result.append({'file':f,'area':area,'text':text+'\n'})
        output=(ROOT/f'terms/OT1998/output/OT_1998CHUNK{r["chunk"]}.md').read_text()
        rules=re.findall(r'\*\*(?:Holding and operative rule|Operative rule)[.:]?\*\*:?\s*(.*?)(?=\n\n|\Z)',ss.get('Holdings',''),re.S)
        missing=[x for x in rules if normalize(x) not in normalize(output)]
        checks.append({'file':f,'render':f'OT_1998CHUNK{r["chunk"]}.md','operative_rules':len(rules),'rules_not_verbatim_after_typography_normalization':missing})
    (WORK/('draft_entries_'+''.join(map(str,chunks))+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2))
    (WORK/('render_checks_'+''.join(map(str,chunks))+'.json')).write_text(json.dumps(checks,ensure_ascii=False,indent=2))
    return result,checks
