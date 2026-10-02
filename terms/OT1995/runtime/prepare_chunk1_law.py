"""Mechanical copies of operator-selected opening authority; no adjudication."""
from pathlib import Path
import importlib.util
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('entering', ROOT / 'tools/build_entering_law.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
groups = {
 'A': (
  ['Collective Brady materiality and investigating-team responsibility', 'Relevant precedent in appellate qualified-immunity review', 'Qualified-immunity legal appeals and factual sufficiency', 'Individual-capacity liability for official conduct under §1983', 'Preserved protected-silence and personal-intent errors on federal habeas review', 'Parole ineligibility as an answer to future-danger evidence', 'Invalid aggravators in capital weighing and correction of sentencing error'],
  {'criminal-procedure': ['Collective disclosure materiality and prosecution responsibility', 'Protected silence and habeas harmless-error review', 'Constitutional trial error on habeas', 'Capital sentencing responsibility and rebuttal', 'Capital sentencing and correction of weighing error'], 'civil-rights': ['Qualified-immunity review', 'Constitutional torts and fractured authority', 'Prison officials’ duty to protect', 'Individual-capacity liability'], 'federal-courts': ['Collateral appeals from municipal liability defenses']}),
 'B': (
  ['Interim restraint and orderly review in related bankruptcy proceedings', 'Exclusive interstate jurisdiction and private boundary-related claims', 'Jury determination of criminal materiality', 'Capacity to plead or waive counsel and independent valid waiver', 'Punitive forfeiture and Excessive Fines review', 'Required commercial connection and distinct economic-class regulation', 'RFRA review of prospective enforcement', 'Speech burdens in a content-neutral injunction'],
  {'bankruptcy': ['Liens and claim valuation', 'Bond execution and bankruptcy restraints'], 'federal-courts': ['Exclusive original jurisdiction and private title litigation'], 'criminal-procedure': ['Jury determination of criminal elements', 'Competence and informed waiver', 'Excessive fines and criminal RICO forfeiture'], 'constitutional-structure': ['Commerce power and school-zone firearm possession', 'Commerce power and armed vehicle taking'], 'first-amendment': ['Religious exercise and statutory protection', 'Speech injunctions and remedial scope'], 'civil-rights': ['Private conspiracies and clinic obstruction']}),
 'C': (
  ['Continued psychiatric confinement after an insanity-acquittal predicate ends', 'Equal protection of commitment proof and family participation', 'Limited modification authority and mandatory tariff filing', 'Professional direction and genuine NLRA supervisory authority', 'Communicated circumstances and Miranda custody', 'Miranda habeas review and fair litigation of independent coercion claims', 'ERISA employee status under general common-law agency', 'Nonemployee organizers\' access under a nondiscriminatory exclusion policy'],
  {'civil-rights': ['Psychiatric confinement', 'Equality and procedure in civil commitment'], 'administrative-law': ['Tariff-filing modification authority'], 'labor-and-employment': ['Skilled employees and supervisory status', 'ERISA employee classification', 'Nonemployee organizing access'], 'criminal-procedure': ['Custodial interrogation'], 'federal-courts': ['Miranda habeas review and unpleaded coercion']})
}
for group, (standards, holdings) in groups.items():
    if group == 'A':
        standards.append('Late assertion of Teague nonretroactivity')
        holdings['criminal-procedure'] += ['Stringer v. Black, 503 U.S. 222 (1992)', 'Caspari v. Bohlen', 'Romano v. Oklahoma']
        holdings['federal-courts'] += ['Johnson v. Jones']
    if group == 'B':
        standards.append('Advance plea-statement waivers for impeachment')
        holdings['criminal-procedure'] += ['Plea-discussion impeachment waivers']
        standards.append('Direct enterprise engagement in interstate commerce')
    if group == 'C':
        holdings['criminal-procedure'] += ['Wright v. West, 505 U.S. 277 (1992)']
    output = ROOT / f'terms/OT1995/entering-law/OT_1995CHUNK1_{group}.md'
    args = [sys.executable, '-B', str(ROOT / 'tools/build_entering_law.py'), str(output)]
    for heading in standards:
        args += ['--standard-heading', heading]
    args += ['--standing-heading', '1. Current Court', '--standing-heading', '2. Current Circuit Allotments', '--standing-heading', '3. Standing Practices']
    subprocess.run(args, check=True)
    with output.open('a', encoding='utf-8') as out:
        for slug, headings in holdings.items():
            path = ROOT / f'state/holdings/{slug}.md'
            source = path.read_text(encoding='utf-8')
            for heading in headings:
                out.write(f'\n\n## Verbatim Holdings selection: {slug} / {heading}\n\nSource: state/holdings/{slug}.md\n\n')
                out.write(module.take_heading(source, heading) + '\n')
    print(f'{group}: {len(output.read_text(encoding="utf-8"))} characters')
