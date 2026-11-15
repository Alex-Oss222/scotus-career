"""Copy bounded authoritative readings for the clean OT2003 chunk 1 stages."""
from pathlib import Path
import importlib.util
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('entering_builder', ROOT / 'tools/build_entering_law.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

DEMORE_STANDARDS = [
    'Immigration review channels and protection of former waiver eligibility',
    'Removal-linked duration of post-removal-period detention',
    'Juvenile release avenues and facial custody review',
    'Unauthorized-employment conditions on immigration release',
    'Initial employment suspension and continuing procedural protection',
    'Interim review of prolonged forfeiture retention',
    'Continued psychiatric confinement after an insanity-acquittal predicate ends',
    'Functional impairment required for sexually violent predator commitment',
    "Defendant's preponderance burden and equivalent competence presumption",
    'Hearings for risk-based and conviction-based notification',
    'Remand for an initial determination assigned to an agency',
]
DEMORE_HOLDINGS = [
    ('immigration', "INS v. National Center for Immigrants' Rights, Inc., 502 U.S. 183 (1991)"),
    ('immigration', 'Reno v. Flores, 507 U.S. 292 (1993)'),
    ('immigration', 'Zadvydas v. Davis; Ashcroft v. Ma'),
    ('federal-courts-habeas', 'Kolster v. INS'),
    ('federal-courts-habeas', 'Reno v. Goncalves'),
    ('federal-courts-habeas', 'Calcano-Martinez v. INS'),
    ('federal-courts-habeas', 'INS v. St. Cyr'),
    ('federal-courts-habeas', 'Zadvydas v. Davis; Ashcroft v. Ma'),
    ('civil-rights', 'Foucha v. Louisiana, 504 U.S. 71 (1992)'),
    ('civil-rights', 'Gilbert v. Homar'),
    ('civil-rights', 'Connecticut Department of Public Safety v. Doe, 538 U.S. 1'),
    ('civil-rights', 'Fairley v. Luman'),
    ('property-and-economic-rights', 'Krimstock v. Kelly'),
    ('administrative-law', 'INS v. Ventura, 537 U.S. 12'),
]
DEMORE_PUBLIC = [
    ('terms/OT2000/output/OT_2000CHUNK8.md', 'Zadvydas v. Davis and Ashcroft v. Ma, Nos. 99-7791 and 00-38'),
    ('terms/OT1992/output/OT_1992CHUNK4.md', 'Reno v. Flores, No. 91-905'),
    ('terms/OT2002/output/OT_2002CHUNK13.md', 'Krimstock v. Kelly, lower docket 00-9488'),
    ('terms/OT2002/output/OT_2002CHUNK13.md', 'Fairley v. Luman'),
]

HOLSTON_STANDARDS = ['Commerce connection, mechanism, and class-wide effects']
HOLSTON_HOLDINGS = [
    ('constitutional-structure', 'United States v. Lopez'),
    ('constitutional-structure', 'United States v. Hale, judgment below 978 F.2d 1016'),
    ('constitutional-structure', 'National Association of Home Builders v. Babbitt'),
    ('constitutional-structure', 'United States v. Kirk'),
    ('constitutional-structure', 'Hiley v. Barrett'),
    ('constitutional-structure', 'United States v. Franklyn / United States v. Gonzalez'),
    ('constitutional-structure', 'United States v. Griffin / United States v. Langley'),
]
HOLSTON_PUBLIC = [
    ('terms/OT1994/output/OT_1994CHUNK5.md', 'United States v. Lopez, No. 93-1260'),
    ('terms/OT1995/output/OT_1995CHUNK3.md', 'United States v. Hale, Eighth Circuit No. 91-3830'),
    ('terms/OT1997/output/OT_1997CHUNK10.md', 'National Association of Home Builders v. Babbitt, D.C. Circuit No. 96-5354'),
]

def make(name, standards, holdings, public):
    output = ROOT / ('terms/OT2003/entering-law/OT_2003CHUNK1_' + name + '.md')
    args = [sys.executable, '-B', str(ROOT / 'tools/build_entering_law.py'), str(output)]
    for title in standards:
        args.extend(['--standard-heading', title])
    args.extend(['--standing-heading', '1. Current Court'])
    subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True)
    parts = [output.read_text(encoding='utf-8')]
    for volume, title in holdings:
        source = 'state/holdings/' + volume + '.md'
        copied = builder.take_heading((ROOT / source).read_text(encoding='utf-8'), title)
        parts.extend(['\n## Verbatim Holdings selection\n\nSource: `' + source + '`; heading: ' + title + '\n\n', copied, '\n'])
    for source, title in public:
        case = builder.take_heading((ROOT / source).read_text(encoding='utf-8'), title)
        parts.append('\n## Prior public positions\n\nSource: `' + source + '`; case: ' + title + '\n\n')
        for section in ['Opinion Topology', 'Separate Writings', 'Selected Separate Positions', 'Selected Separate Writings', 'Separate Positions Relevant to the Decision']:
            try:
                copied = builder.take_heading(case, section)
            except ValueError:
                continue
            parts.extend([copied, '\n'])
    output.write_text('\n'.join(parts).rstrip() + '\n', encoding='utf-8')
    print(str(output.relative_to(ROOT)) + ': ' + str(len(output.read_text(encoding='utf-8').split())) + ' words')
    return output

if __name__ == '__main__':
    make('DEMORE', DEMORE_STANDARDS, DEMORE_HOLDINGS, DEMORE_PUBLIC)
    make('HOLSTON', HOLSTON_STANDARDS, HOLSTON_HOLDINGS, HOLSTON_PUBLIC)
