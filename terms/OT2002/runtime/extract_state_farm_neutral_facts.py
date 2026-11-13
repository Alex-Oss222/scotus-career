from pathlib import Path
import hashlib

base = Path('terms/OT2002')
src = base / 'sources/chunk8-comparators'
majority = (src / '01-1289.ZO.html.txt').read_text(encoding='utf-8')
separate = (src / '01-1289.ZD2.html.txt').read_text(encoding='utf-8')

def between(text, start, end):
    a = text.index(start)
    b = text.index(end, a + len(start))
    return text[a:b].strip()

excerpts = [
    ('Accident, liability investigation, excess exposure, later payment and bad-faith proceedings',
     between(majority, 'In 1981, Curtis Campbell', 'Before the second phase of the action against State Farm')),
    ('Punitive-phase scope, trial evidence and actual amounts',
     between(majority, 'The second phase addressed State Farm', 'The Utah Supreme Court sought to apply')),
    ('Reported reasons for the state appellate disposition and penalty comparisons',
     between(majority, 'The Utah Supreme Court sought to apply', 'We granted certiorari.')),
    ('Specific reported trial finding and conduct toward the insureds',
     between(majority, 'The trial court found that State Farm', 'While we do not suggest')),
    ('Character and duration of compensated injury',
     between(majority, 'the Campbells were awarded $1 million', 'The compensatory damages for the injury suffered here')),
    ('Character of the emotional-distress evidence',
     between(majority, 'Much of the distress was caused by the outrage', '; and it is a major role of punitive damages')),
    ('Reported earlier Texas award and its procedural status',
     between(majority, 'The award was rendered in a first-party lawsuit;', 'With respect to the Utah Supreme Court’s second justification')),
    ('Reported comparable Utah civil sanction',
     between(majority, 'The most relevant civil sanction under Utah state law', ', an amount dwarfed')),
    ('Reported scope and operation of the claims program',
     between(separate, 'Ample evidence allowed the jury to find', 'But cf. ante, at 13, 17')),
    ('Reported trial record concerning local implementation, vulnerability, documents and nexus to this claim',
     between(separate, 'Evidence the jury could credit demonstrated', 'The Utah Supreme Court, relying on the trial court’s record-based recitations')),
    ('Reported purposes for admission of other-acts evidence',
     between(separate, 'The evidence was admissible, the trial court ruled:', 'Viewed in this light')),
]

header = '''# State Farm: source-only record excerpts for fresh neutral validation

**Matter:** State Farm Mutual Automobile Insurance Co. v. Campbell, No. 01-1289; April 7, 2003.
**Status:** Source extraction only. This file is not a validated supplement, new finding, commitment or Court action. A fresh neutral context must validate framing and source limits before fresh affected modeling.

Source: the published primary judicial texts of State Farm, 538 U.S. 408 (2003), as saved in the term source collection. The passages below are copied mechanically. They preserve citations, qualifications and source ellipses. They report facts, testimony, findings and lower-court reasons, with their stated source character; they do not establish independent examination of the original appendix, briefs or transcript. Contrasting recitations concerning nationwide practices and their connection to the local claim are both preserved. Nothing here decides whether an outside transaction was proved similar, lawfully punishable or merely relevant evidence.

The compensation recitation is a published characterization of the record; it is not a new independent finding concerning the components of the jury's award. The short excerpt on outrage and humiliation stops before the source's inference concerning possible overlap of compensation and punishment. That inference is not supplied as an adjudicated damages allocation. The civil-sanction excerpt retains “appears” and does not purport to reproduce a complete statute. The Texas-verdict passage does not establish a prior final punitive judgment. Descriptions of documents and employees' testimony retain their reported status.

No target disposition, alignment, target legal rule or recommended judgment is supplied. The existing approved neutral packet and entering law remain separate inputs. Later neutral validation must preserve every distinction between evidence, supported finding, party contention and judicial characterization; neither unavailable originals nor these excerpts imply litigant default.
'''
parts = [header]
for title, passage in excerpts:
    parts.append('\n## ' + title + '\n\n' + '\n'.join('> ' + line for line in passage.splitlines()) + '\n')
out = base / 'runtime/StateFarm-neutral-source-excerpts.md'
out.write_text('\n'.join(parts), encoding='utf-8')
receipt = ['# State Farm source extraction receipt', '', 'Every excerpt is an exact substring selected by this script from the complete saved primary text. No text was reconstructed as quotation.', '']
for p in [src / '01-1289.ZO.html.txt', src / '01-1289.ZD2.html.txt', out]:
    receipt.append(f'- {p.name}: SHA-256 {hashlib.sha256(p.read_bytes()).hexdigest()}')
receipt.append('\nThis receipt and extraction script remain control artifacts; only the source-only excerpts go to neutral validation. Full primary writings and footnotes were read in reconciliation. No frozen commitment was edited.\n')
(base / 'runtime/StateFarm-neutral-source-extraction-receipt.md').write_text('\n'.join(receipt), encoding='utf-8')
print(out)
print('Excerpt count:', len(excerpts))
print('Source-only words:', len(out.read_text(encoding='utf-8').split()))
print('SHA-256:', hashlib.sha256(out.read_bytes()).hexdigest())
