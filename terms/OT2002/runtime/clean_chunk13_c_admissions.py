from pathlib import Path

base=Path(__file__).resolve().parent
edits={
    'Gratz-v-Bollinger_merits_2003-06-23.md':{
        ' Sandoval preserves the separate operation of valid, definite §602 requirements; demographic differences in other criteria do not themselves establish a regulatory violation in this action.':'',
        "The judgment neither requires another school's precise design nor treats all supported consideration of race as forbidden.":'Supported consideration of race remains available under the existing governing rule.'
    },
    'Grutter-v-Bollinger_merits_2003-06-23.md':{
        ' A distinct regulatory-effects claim is outside the theories presented and is not created from demographic differences.':'',
        ' remain justified, without a judicially fixed calendar expiration.':' remain justified.',
        ' A future year selected without that factual basis would neither establish present validity nor decide future need.':'',
        ' rather than a fixed judicial calendar.':'.',
        "; Powell's entire diversity rationale is not treated as a prior majority holding.":'.',
        '; the denied policy theories establish no violation requiring such relief here.':'.'
    }
}
for name,changes in edits.items():
    p=base/'chunk13-drafts'/name
    text=p.read_text(encoding='utf-8')
    for old,new in changes.items():
        assert old in text,(name,old)
        text=text.replace(old,new)
    p.write_text(text,encoding='utf-8')
    script='build_chunk13_c_admissions.py' if name.startswith('Gratz') else 'build_chunk13_c_grutter.py'
    p=base/script
    text=p.read_text(encoding='utf-8')
    for old,new in changes.items():
        text=text.replace(old,new)
    p.write_text(text,encoding='utf-8')
print('Admissions five-block cleanup applied without changing frozen annexes.')
