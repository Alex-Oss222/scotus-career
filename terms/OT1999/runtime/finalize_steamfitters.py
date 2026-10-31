import json
from pathlib import Path
from assembly_record_writer import write_record
p=Path(__file__).with_name('assembly_steamfitters.json')
d=json.loads(p.read_text())
d['kernel']=d['kernel'].replace('earlier actual OT1999 Records must be screened at release.', 'the effective Flippo, Lesage, Fiore, Drye and Torres Records change none of the statutory-causation, pleading or entity-capacity premises. Lesage separates injury from particular relief in its admissions setting but is not imported as a RICO rule. Paul and United Reporting have no effective event; no proposal from either becomes law or an authorship count.')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
write_record(p,'Thomas',d['lead_support'],"Thomas is selected to keep the funds' real property loss, statutory capacity and causal entitlement distinct while applying the settled Holmes rule to two separate chains and the Clayton Act independently. His complete Holmes joins and Brown Group join support each of those boundaries and permit an opinion that applies the binding rule without reopening its disputed historical derivation. Souter is the strongest alternative because of his Holmes opinion; Thomas can carry the same settled ground with zero counted leads against Souter's one. Stone can likewise carry the grounds, but his additional explanatory interests establish no concrete fit or coalition advantage over Thomas, so self-assignment is not selected. No expansion accommodation is needed.",True)
