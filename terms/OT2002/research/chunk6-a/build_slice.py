from pathlib import Path
import importlib.util
import subprocess
import sys
import re

root = Path(__file__).resolve().parents[4]
spec = importlib.util.spec_from_file_location('entering', root / 'tools/build_entering_law.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
out = root / 'terms/OT2002/entering-law/OT_2002CHUNK6_A.md'
standards = [
    'Forfeited error and discretionary correction under Rule 52(b)',
    'Jury determination of elements and qualified omitted-element review',
    'Present-offense facts changing binding punishment ranges',
    'Omitted aggravating allegations and criminal jurisdiction',
    'Contemporaneous retrieval of numerical pager messages incident to arrest',
    'Nonassisting media observers during a home search',
    'Privacy in confidential account administration records',
    'Informant reports of gun possession and individualized suspicion',
    'Independent appellate review of suspicion and nonwarrant probable cause',
    'Traffic-stop completion, search consent and prior illegality',
    'Punitive purpose or effect in nominally civil commitment',
    'Official dissemination of compiled nonpublic residential information',
]
args = [sys.executable, str(root / 'tools/build_entering_law.py'), str(out)]
for title in standards:
    args += ['--standard-heading', title]
subprocess.run(args, check=True)
holdings = {
    'criminal-procedure-investigations': [
        'United States v. Ortiz; United States v. Hurtado', 'Ayeni v. Mottola',
        'Guest v. Leis', 'Illinois v. Wardlow, 528 U.S. 119 (2000)',
        'Florida v. J. L., 529 U.S. 266 (2000)', 'United States v. Arvizu, 534 U.S. 266',
        'United States v. Valentine',
    ],
    'criminal-procedure-sentencing-and-capital': [
        'United States v. Watts / United States v. Putra', 'Jones v. United States',
        'Apprendi v. New Jersey, 530 U.S. 466 (2000)',
        'United States v. Cotton, 535 U.S. 625',
        'United States v. Angle, 254 F.3d 514 (judgment below)',
        'Harris v. United States, 536 U.S. 545',
    ],
    'criminal-procedure': [
        'United States v. Olano, 507 U.S. 725 (1993)', 'Johnson v. United States',
        'Kansas v. Hendricks; Hendricks v. Kansas', 'Hudson v. United States',
        'W.P. v. Verniero', 'Almendarez-Torres v. United States',
        'Neder v. United States', 'Castillo v. United States, 530 U.S. 120 (2000)',
        'Seling v. Young, 531 U.S. 250',
    ],
    'civil-rights': ['Paul P. v. Verniero'],
}
parts = [out.read_text(encoding='utf-8')]
for volume, titles in holdings.items():
    rel = f'state/holdings/{volume}.md'
    src = (root / rel).read_text(encoding='utf-8')
    for title in titles:
        parts += [f'## Verbatim Holdings selection: {title}\n\nSource: `{rel}`.\n', module.take_heading(src, title), '']

# Current-term excerpts are selected only from supplied bounded public handoffs.
current = root / 'terms/OT2002/entering-law/OT_2002CHUNK6_PUBLIC_BEFORE_2003-03-05.md'
blocks = re.split(r'(?=^## Source: )', current.read_text(encoding='utf-8'), flags=re.M)
names = ['Konop-v-Hawaiian-Airlines-Inc', 'Sattazahn-v-Pennsylvania']
for name in names:
    matched = [b for b in blocks if b.startswith('## Source: ') and name in b.splitlines()[0]]
    assert len(matched) == 1, name
    parts += [f'## Date-eligible current-term public selection: {name}\n\nCopied from `{current.relative_to(root).as_posix()}`.\n', matched[0].strip(), '']
parts += ['## Date and source restrictions\n\nBach, Smith, and Wheat use only completed law effective before March 5, 2003. Buckland uses only completed law effective before March 10, 2003. Unrelated March 5 decisions are excluded from the first three matters. The two current-term excerpts above precede both cutoffs. No new holding in this group supplies entering law to another unrelated same-date matter. Buckland requires a final date check after the March 5 events are committed; none of those events presently poses a sentencing-quantity dependency.\n']
out.write_text('\n\n'.join(parts), encoding='utf-8')
print(f'{len(standards)} standards; {sum(map(len, holdings.values()))} Holdings entries; {len(names)} current-term public entries; {out.stat().st_size} bytes')
