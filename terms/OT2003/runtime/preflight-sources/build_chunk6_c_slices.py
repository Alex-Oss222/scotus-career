from pathlib import Path
import importlib.util
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
spec = importlib.util.spec_from_file_location('entering_builder', ROOT / 'tools/build_entering_law.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

CASES = {
    83: {
        'date': '2004-05-17',
        'standards': ['Federal-program bribery without traced federal-funds effect', 'Commerce connection, mechanism, and class-wide effects', 'Genuine choice under conditional federal funding'],
        'holdings': {
            'criminal-procedure': ['Salinas v. United States', 'Fischer v. United States, 529 U.S. 667 (2000)'],
            'constitutional-structure': ['United States v. Lopez', 'United States v. Morrison / Brzonkala v. Morrison, 529 U.S. 598 (2000)', 'Kansas v. United States', 'National Association of Home Builders v. Babbitt'],
        },
        'public': ['runtime/current-public-law/united_states_v_ho_merits_2003-11-20.md', 'runtime/current-public-law/rancho_viejo_llc_v_norton_merits_2004-02-05.md', 'runtime/OT_2003CHUNK4_united_states_v_mcfarland_merits_2004-02-19_PUBLIC.md'],
    },
    84: {
        'date': '2004-05-20',
        'standards': ['Prison-conditions prospective relief', 'Serious risks in prison conditions and deliberate indifference'],
        'holdings': {
            'federal-courts-immunities-and-remedies': ['Benjamin v. Jacobson'],
            'civil-rights': ['Farmer v. Brennan, 511 U.S. 825', 'County of Sacramento v. Lewis'],
            'criminal-procedure': ['Helling v. McKinney, 509 U.S. 25 (1993)'],
        },
        'public': ['runtime/OT_2003CHUNK6_RULE53_PUBLIC.md'],
    },
    85: {
        'date': '2004-05-24',
        'standards': ['Traffic citations and the custodial-arrest search exception'],
        'holdings': {
            'criminal-procedure-investigations': ['Knowles v. Iowa, 525 U.S. 113'],
            'federal-courts': ['Florida v. Thomas, 532 U.S. 774'],
        },
        'public': [],
    },
    86: {
        'date': '2004-05-24',
        'standards': ['Conviction-negating damages claims and favorable invalidation', 'Equitable delay independently of a habeas procedural bar', 'Prison-conditions prospective relief'],
        'holdings': {
            'civil-rights': ['Heck v. Humphrey, 512 U.S. 477', 'Edwards v. Balisok', 'Randell v. Johnson'],
            'federal-courts-habeas': ['Gomez v. United States District Court for the Northern District of California, 503 U.S. 653 (1992)'],
        },
        'public': ['runtime/OT_2003CHUNK4_Muhammad_v_Close_merits_2004-02-25_PUBLIC.md'],
    },
    87: {
        'date': '2004-06-01',
        'standards': ['Communicated circumstances and Miranda custody', 'Independent Miranda custody review under the former habeas statute', 'State-court merits decisions and factual development under amended'],
        'holdings': {
            'criminal-procedure-investigations': ['Stansbury v. California, 511 U.S. 318', 'Thompson v. Keohane, 516 U.S. 99'],
            'federal-courts-habeas': ['Williams v. Taylor (Terry Williams), 529 U.S. 362 (2000)', 'Woodford v. Visciotti, 537 U.S. 19', 'Lockyer v. Andrade, 538 U.S. 63'],
        },
        'public': ['runtime/current-public-law/mitchell_v_esparza_merits_2003-11-03.md'],
    },
}

for number, config in CASES.items():
    output = ROOT / f'terms/OT2003/entering-law/OT_2003CHUNK6_CASE{number}.md'
    command = [sys.executable, '-B', str(ROOT / 'tools/build_entering_law.py'), str(output)]
    for heading in config['standards']:
        command.extend(['--standard-heading', heading])
    subprocess.run(command, cwd=ROOT, check=True)
    parts = [output.read_text(encoding='utf-8').rstrip(), '', '## Event-specific scope', '',
             f'Case {number}; decision-date cutoff {config["date"]}. Only law effective before that date enters. Uncoordinated same-date decisions share the pre-date baseline.', '',
             'The following prior-authority sections are copied without substantive alteration by the heading selector in tools/build_entering_law.py. Current-term additions are copied only from public handoffs identified in workspace/neutral-projection.md. These are reading copies, not independent authority.', '']
    for volume, headings in config['holdings'].items():
        source = ROOT / f'state/holdings/{volume}.md'
        body = source.read_text(encoding='utf-8')
        for heading in headings:
            selected = builder.take_heading(body, heading)
            parts.extend([f'## Selected authority from state/holdings/{volume}.md', '', selected, ''])
    for relative in config['public']:
        source = ROOT / 'terms/OT2003' / relative
        parts.extend([f'## Effective current-term public authority: {relative}', '', source.read_text(encoding='utf-8').strip(), ''])
    output.write_text('\n'.join(parts).rstrip() + '\n', encoding='utf-8')
    print(f'Case {number}: {output.stat().st_size} bytes')
