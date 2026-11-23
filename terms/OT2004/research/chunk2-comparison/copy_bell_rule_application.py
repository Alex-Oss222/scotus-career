from pathlib import Path
base=Path('terms/OT2004/research/chunk2-comparison')
s=(base/'bell_full.txt').read_text(encoding='utf-8')
def between(a,b):
    x=s.index(a)
    y=s.index(b,x)+len(b)
    return s[x:y]
cone=between('"The jury also found that the murders in question', 'Id., at 94-95.')
dicks=between('"directed at', 'Dicks, supra, at 132.')
pritchett=between('"Although the Tennessee aggravating circumstances', 'Pritchett, 621 S. W. 2d, at 139 (citation omitted).')
melson_suffering=between('"the uncontradicted proof shows', 'Melson, supra, at 367.')
melson_brutality=between('"a killing wherein the victim is struck', 'Melson, supra, at 367.')
intro='''# Bell v. Cone — neutral state rule and application supplement

This handoff contains the state construction and the state court's actual application, as quoted in an authenticated published recitation. It contains no assessment that those actions establish a sufficient federal adjudication or cure. Each block below is copied mechanically from the complete primary source `bell_full.txt` and cross-checked against `bell_official.txt`; no original state brief or transcript is claimed recovered. The legal status of each quoted passage is a state rule or a state judicial finding, not an independently established historical fact beyond that description.

## 1. Dicks construction

State v. Dicks, 615 S. W. 2d 126, 132 (Tenn. 1981), supplies this construction of the heinousness aggravator. Source recitation: 543 U.S. 458.

'''
parts=[intro,dicks,'''\n\n## 2. Pritchett's stated narrowing rule

State v. Pritchett, 621 S. W. 2d 127, 139 (Tenn. 1981), states the operative construction below. The decision also treated instantaneous death as insufficient for its torture branch and a second shotgun blast after the victim's death as insufficient to establish the requisite depravity. Source recitation: 543 U.S. 458–459. These qualifications describe the state rule; this handoff makes no federal holding about it.

''',pritchett,'''\n\n## 3. Melson's applications

State v. Melson, 638 S. W. 2d 342, 367 (Tenn. 1982), gives these concrete applications. The first concerns conscious suffering and opportunity to resist; the second describes an application based on repeated blows and the resulting injuries. They are the state court's factual characterizations and legal applications in Melson. Source recitation: 543 U.S. 458–459.

''',melson_suffering,'\n\n',melson_brutality,'''\n\n## 4. The actual direct-review passage in Cone

The following is the Tennessee Supreme Court's own explanation of the heinousness aggravator in State v. Cone, 665 S. W. 2d 87, 94–95 (Tenn. 1984), quoted at 543 U.S. 449. It preserves what the state court said about resistance, multiple blows, noninstantaneous deaths, fear and the jury's finding. Whether that explanation actually applied the authoritative rule, decided the particular federal claim, or corrected a distinct constitutional defect remains for independent analysis under the governing law.

''',cone,'''\n\n## 5. Application boundaries

The companion `BELL_NEUTRAL_SOURCE_FACTS.md` supplies the separate risk-to-others aggravator disposition, the state appellate references to Pritchett and Melson, the differing collateral/default accounts, and section 2254(b)(2)'s permitted merits-denial alternative. The express harmlessness ruling on the rejected risk-to-others aggravator is not silently transferred to a distinct heinousness defect. Neither the state quotations nor an absent case name is conclusive by itself about every federal claim or corrective requirement.

Only the preceding state rules and findings, their actual chronology, and those companion procedural facts enter this supplement. No later state decision is used to establish what the 1984 court necessarily did. The state adjudication's applicable federal-law cutoff must be identified separately; no later federal doctrine is backdated.
''']
(base/'BELL_NEUTRAL_RULE_APPLICATION.md').write_text(''.join(parts),encoding='utf-8')
print('Wrote state-only quotation handoff:',len(''.join(parts)),'characters')
