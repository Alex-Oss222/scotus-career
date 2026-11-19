from pathlib import Path

base=Path(__file__).resolve().parent
changes={
    'Gratz-v-Bollinger_merits_2003-06-23.md':{
        'Alexander v. Sandoval, April 24, 2001: preserves §601 intentional treatment and holds that no private action enforces §602 disparate-impact regulations.':
        "Alexander v. Sandoval, April 24, 2001: preserves §601's intentional-treatment requirement."
    },
    'Grutter-v-Bollinger_merits_2003-06-23.md':{
        'Sandoval distinguishes §601 intentional treatment from §602 disparate-impact regulations, which no private action enforces.':
        "Sandoval preserves §601's intentional-treatment requirement.",
        'Alexander v. Sandoval, April 24, 2001: preserves §601 intentional-treatment protection and holds that no private action enforces §602 disparate-impact regulations.':
        "Alexander v. Sandoval, April 24, 2001: preserves §601's intentional-treatment protection."
    }
}
for name,replacements in changes.items():
    path=base/'chunk13-drafts'/name
    text=path.read_text(encoding='utf-8')
    for old,new in replacements.items():
        assert old in text,(name,old)
        text=text.replace(old,new)
    path.write_text(text,encoding='utf-8')
    script='build_chunk13_c_admissions.py' if name.startswith('Gratz') else 'build_chunk13_c_grutter.py'
    path=base/script
    text=path.read_text(encoding='utf-8')
    for old,new in replacements.items():
        text=text.replace(old,new)
    path.write_text(text,encoding='utf-8')
print('Public statutory discussion confined to the decided section 601 claims.')
