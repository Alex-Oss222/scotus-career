from pathlib import Path
import json,re,sys
sys.dont_write_bytecode=True
root=Path(__file__).resolve().parents[3]
term=root/'terms/OT1999'
case=sys.argv[1]
if case=='CARMELL':
    draft=term/'preparation/CARMELL_RECORD_DRAFT.md'
    if not draft.exists():draft=term/'records/carmell-v-texas_merits_2000-05-01.md'
    text=draft.read_text(encoding='utf-8')
    recon=(term/'freeze/OT_1999CHUNK6_CARMELL_RECONCILED.md').read_text(encoding='utf-8')
    start=recon.index('| Justice |')
    end=recon.index('\n\n',start)
    if '<!-- FROZEN_JUSTICE_TABLE -->' in text:
        assert draft.parent.name=='preparation'
        text=text.replace('<!-- FROZEN_JUSTICE_TABLE -->',recon[start:end])
        draft.write_text(text,encoding='utf-8')
    support=['Stone-Zsela','Stevens','Scalia','Souter','Thomas','Breyer']
    oppose=["O'Connor",'Kennedy','Ginsburg']
    author='Stevens'
elif case=='NCRL':
    draft=term/'preparation/NCRL_RECORD_DRAFT.md'
    if not draft.exists():draft=term/'records/north-carolina-right-to-life-inc-v-bartlett_merits_2000-05-01.md'
    text=draft.read_text(encoding='utf-8')
    recon=(term/'freeze/OT_1999CHUNK6_NCRL_RECONCILED.md').read_text(encoding='utf-8')
    start=recon.index('| Justice |')
    end=recon.index('\n\n',start)
    if '<!-- FROZEN_JUSTICE_TABLE -->' in text:
        assert draft.parent.name=='preparation'
        text=text.replace('<!-- FROZEN_JUSTICE_TABLE -->',recon[start:end])
        draft.write_text(text,encoding='utf-8')
    support=['Stone-Zsela','Stevens',"O'Connor",'Scalia','Kennedy','Souter','Thomas','Ginsburg','Breyer']
    oppose=[]
    author=sys.argv[2]
else:raise SystemExit('Unsupported case')
labels=['**Case and dockets:**','**Event and date:**','**Result:**','**Version / lineage:**']
assert all(line.startswith(label) for line,label in zip(text.splitlines()[:4],labels))
pp=text.split('## Public Projection\n',1)[1]
if case=='NCRL':
    assert 'unproduced guide' not in pp and 'under an invented text' not in pp
    assert 'nor decides whether the second guide satisfies a different, sufficiently definite rule' in pp
heads=re.findall(r'^## (.+)$',pp,re.M)
assert heads==['Event','Participation','Public Action','Judgment & Remedy','Opinion Topology','Holdings','Precedent Treatment','Law After Decision','Separate Writings','Procedure After Action','Source Notes'],heads
assert len(set(support+oppose))==9 and not set(support)&set(oppose)
count=json.loads((term/f'freeze/OT_1999CHUNK6_{case}_COUNTS.json').read_text(encoding='utf-8'))
assert author in support
assert count['counts'][author]<=min(count['counts'][j] for j in support)+1
assert f'| Opinion of the Court | {author} |' in pp
explanations=re.findall(r'\*\*Controlling explanation:\*\* (.*?)(?=\n\n####|\n\n## |\Z)',pp,re.S)
words=[len(s.split()) for s in explanations]
assert all(n<=350 for n in words),words
assert '<!-- FROZEN_JUSTICE_TABLE -->' not in text
assert not re.search(r'(?i)(version|lineage|simulat|user.directed|approved|workflow|reconcil|frozen|2026)',pp)
for match in re.finditer(r'\]\(([^)]+)\)',text):
    target=match.group(1).split('#')[0]
    if target.startswith(('http:','https:')) or not target:continue
    if target.endswith('_ASSEMBLY_VALIDATION.md'):continue
    assert (term/'records'/target).resolve().exists(),target
print(json.dumps({'case':case,'eleven_blocks':heads,'participants':len(set(support+oppose)),'judgment':[len(support),len(oppose)],'author':author,'pool_checked':True,'controlling_explanation_words':words,'frozen_table_identity':recon[start:end] in text,'local_links_checked':True},indent=2))
