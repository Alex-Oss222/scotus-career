from pathlib import Path

base=Path(__file__).resolve().parent
p=base/'chunk13-drafts/Sell-v-United-States_merits_2003-06-16.md'
t=p.read_text(encoding='utf-8')
changes={
    'solely to permit trial of serious criminal charges, including serious nonviolent property offenses':'solely to permit trial of serious nonviolent criminal charges, including serious property offenses',
    'A serious prosecution can supply the necessary interest':'Prosecution of serious nonviolent charges can supply the necessary interest',
    'Courts retain the legal decision, informed by clinical evidence, without a universal numerical success rate or proof quantum.':'Courts retain the legal decision, informed by clinical evidence.',
    'This answer concerns the categorical claim presented; it does not equate every First Amendment protection with due process or announce a general level of scrutiny for medical intervention.':'This answer resolves the categorical First Amendment claim presented.',
    ' He would apply the proposed limit to this unexecuted order and comparable pending or direct-review proceedings, while leaving collateral vehicles, finality and independent remedy requirements to govern completed cases.':'',
    'Serious prosecution may justify restoration medication only through':'Prosecution of serious nonviolent charges may justify restoration medication only through'
}
for old,new in changes.items():
    assert old in t,old
    t=t.replace(old,new)
t=t.replace('No logical-subset construction or Marks aggregation is necessary:',"The granted prosecution-only category is serious nonviolent charges. The actual holding's wording states that grant boundary without changing any Associate's support for the rule within it. No logical-subset construction or Marks aggregation is necessary:")
p.write_text(t,encoding='utf-8')
# Keep the preparation script's generated text aligned with the corrected draft.
p=base/'build_chunk13_c_drafts.py'
t=p.read_text(encoding='utf-8')
for old,new in changes.items():
    t=t.replace(old,new)
p.write_text(t,encoding='utf-8')
print('Sell grant scope and public explanation cleanup applied.')
