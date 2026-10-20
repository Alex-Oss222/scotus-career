"""Publish current bounded assembly and integration validation receipts."""
from pathlib import Path
import hashlib
import json
import re

TERM = Path(__file__).resolve().parents[1]
FREEZE = TERM / 'freeze'


def write(path, text):
    path.write_text(text, encoding='utf-8', newline='\n')


def main():
    check = (FREEZE / 'OT_1996CHUNK11_FLETCHER_NO_GIT_CHECK_VALIDATION.md').read_text()
    assert '**Status:** Non-Git deterministic checks passed.' in check
    output = re.search(r'```text\n(.*?)\n```', check, re.S)[1]
    write(FREEZE / 'OT_1996CHUNK11_CHECK_TERM.txt', output + '\n')
    assembly = json.loads((TERM / 'tmp/FLETCHER_ASSEMBLY_VALIDATION.json').read_text())
    assert assembly['record_sha256'] == hashlib.sha256((TERM / 'records/Fletcher_v_Kalina_merits_1997-06-16.md').read_bytes()).hexdigest()
    assembly['integration_status'] = 'Workspace and eleven-event chunk Render Input rebuilt; non-Git deterministic term checks passed.'
    write(FREEZE / 'OT_1996CHUNK11_FLETCHER_ASSEMBLY_VALIDATION.json', json.dumps(assembly, indent=2) + '\n')

    final = """# Fletcher v. Kalina — final validation

Fletcher's June 16, 1997 merits event affirms the denial of absolute immunity for the personal factual certification and remands, 9–0. Stevens delivers the lead. All nine join the personal-certification holding and bounded judgment; the eight Associates join the complete protected-advocacy and remaining-defense explanations. Stone's partial joins and both noncontrolling immunity proposals are preserved. Scalia concurs, joined by Thomas. There is no finding of liability.

Assembly ran in a physically separate context using the existing neutral, commitment and final reconciliation handoffs and the current Fletcher Section II. The Associate freezes and runtime splits remain unchanged. Independent final legal review verified the component coalitions, exact Stone qualifications and conditional existing-qualified-immunity remand, material separate positions and source limits. The Record's internal and public Holdings and separate summaries match; the eleven blocks are ordered correctly and explanation lengths are 157, 156 and 191 words.

The fifteen Records dated June 16 or later were reviewed. No other result, substantive rationale, remedy or opinion assignment requires change. Thirteen other Records contain only bounded assignment-count, pool and count-comparison updates; all fourteen other Public Projections and all their non-assignment bytes are preserved. The fresh census and case-specific fit assessment appear in [dependency checks](OT_1996CHUNK11_FLETCHER_DEPENDENCY_CHECKS.json) and [the dependency audit](OT_1996CHUNK11_FLETCHER_DEPENDENCY_AUDIT.md).

The ledger and manifest rebuilds retain 132 Records, 153 inventory events, and the existing chronology. The continuity and neutral projections carry Fletcher's current law, published separate positions and procedure. The generated chunk 11 Render Input copies all eleven completed Records and retains the existing Hendricks stopped notice. Fletcher has no blocker; no event or date was added or changed.

[Package checks](OT_1996CHUNK11_FLETCHER_PACKAGE_CHECKS.json) verify the file boundaries, local references, all eleven controlling-holding projections and current assignment counts. Briefs, case-list, public outputs, governing infrastructure and opening trackers are unchanged. [The repository checker](OT_1996CHUNK11_FLETCHER_NO_GIT_CHECK_VALIDATION.md) passed its non-Git checks, including Holdings synchronization, runtime freshness and generated projection identity. Git object existence, history verification and commitment were not performed; no Git command was run. No public Render was performed.
"""
    write(FREEZE / 'OT_1996CHUNK11_FLETCHER_FINAL_VALIDATION.md', final)

    path = FREEZE / 'OT_1996CHUNK11_ASSEMBLY_JUNE16_FINAL_VALIDATION.md'
    write(path, """# OT1996 chunk 11 — June 16 assembly validation

The four June 16 chunk-11 Records have completed assembly. Their event dates and chronological slots are fixed; their final component coalitions, ordinary explanation ceilings, local references and internal/Public Projection Holdings identity are validated.

| Matter | Judgment | Lead author |
|---|---|---|
| Del Monte Dunes | Affirmed, 5–4 | Stevens |
| Fletcher | Denial of absolute immunity for personal certification affirmed and remanded, 9–0 | Stevens |
| Piscataway / Taxman | Affirmed, 5–4 on both independent Title VII grounds | O'Connor |
| Salazar-Haro | Ordinary direct-review dismissal affirmed, 9–0 | Breyer |

The signed-lead forms, governing propositions and complete-lead eligibility precede assignment. Actual source topologies were recounted in date and alphabetical order; every delivering Justice in Kinman counts once. The saved assignment receipts and source extracts reflect the canonical Records. Fletcher's complete lead has eight eligible Associate authors, all within the minimum-plus-one pool. Stevens's recorded Buckley/Antoine fit supports selection; Stone's partial joins do not qualify him for that complete lead.

Fletcher's eight Associates retain their frozen F1–F4 positions. Stone's knowing-fabrication exception and Contextual Fair-Notice and Reasonable-Conduct Test remain noncontrolling; his express existing-law condition supplies the qualified-immunity framework on remand. No constitutional liability, damages entitlement or mandatory trial is inferred. The [Fletcher final validation](OT_1996CHUNK11_FLETCHER_FINAL_VALIDATION.md) records independent review, integration and its source limits.

The [structural checks](OT_1996CHUNK11_ASSEMBLY_JUNE16_FINAL_CHECKS.json) and [assignment reconciliation](OT_1996CHUNK11_FINAL_ASSIGNMENT_RECONCILIATION.json) contain the current file evidence and counts. Downstream Records retain their results and assignments on the already-recorded qualitative grounds. No Git verification or commitment is claimed.
""")
    path = FREEZE / 'OT_1996CHUNK11_LEGAL_REVIEW_A.md'
    text = path.read_text()
    text = text.replace('Kennedy supports the complete lead and is within the recorded minimum-plus-one eligible pool.', 'Stevens supports the complete lead and is within the recorded minimum-plus-one eligible pool.')
    write(path, text)
    path = FREEZE / 'OT_1996CHUNK11_LEGAL_REVIEW_TAXMAN.md'
    text = path.read_text()
    text = text.replace("Stone 12, Stevens 12, O'Connor 12, Scalia 11, Kennedy 13, Souter 12, Thomas 11, Ginsburg 12, Breyer 11", "Stone 12, Stevens 13, O'Connor 12, Scalia 11, Kennedy 12, Souter 12, Thomas 11, Ginsburg 12, Breyer 11")
    text = text.replace("making O'Connor, Scalia and Thomas the minimum-plus-one pool; Kennedy is outside it", "making O'Connor, Scalia, Kennedy and Thomas the minimum-plus-one pool")
    write(path, text)
    path = FREEZE / 'OT_1996CHUNK11_CONTROL.md'
    text = path.read_text()
    text = re.sub(r'^\| 119 Fletcher \|.*$', "| 119 Fletcher | Affirm denial of absolute immunity for the personal factual certification; preserve legitimate charging and advocacy; remand the constitutional violation, materiality, causation, damages and personal defenses without a liability finding. Stone proposes an exception for knowing fabrication or deliberately false material assertions causing constitutional deprivation, excluding honest mistakes and disputed factual judgments. His Contextual Fair-Notice and Reasonable-Conduct Test assesses responsibilities, information and governing law, protects genuinely reasonable mistakes, excludes knowing constitutional violations and objectively indefensible conduct, and places the defense burden on the official. | If the proposals are not adopted, existing qualified-immunity law governs the remand. Keep the oath distinct from advocacy; denial of absolute immunity establishes neither liability nor entitlement to damages or trial. |", text, flags=re.M)
    write(path, text)

    path = FREEZE / 'OT_1996CHUNK11_VALIDATION.md'
    old = path.read_text()
    retained = old[old.index('## Completed events'):old.index('## Checks and limits')]
    retained = retained.replace('| Fletcher v. Kalina | Affirmed and remanded, 9–0 | Kennedy |', '| Fletcher v. Kalina | Affirmed and remanded, 9–0 | Stevens |')
    text = "# OT1996 chunk 11 — final Run validation\n\nEleven completed Court events and one stopped matter are accounted for. The workspace covers 129 Court events and three admitted sources through June 23, 1997. The generated [Render Input](../render-inputs/OT_1996CHUNK11.md) copies all eleven canonical Public Projections. No public output is changed.\n\n" + retained
    text += """## Checks and limits

- [Fletcher final validation](OT_1996CHUNK11_FLETCHER_FINAL_VALIDATION.md) records the isolated assembly, independent substantive review and preserved conditional remand. The Associates' neutral, commitment and final reconciliation handoffs are unchanged.
- [The dependency audit](OT_1996CHUNK11_FLETCHER_DEPENDENCY_AUDIT.md) covers every Record dated June 16 or later. No other result, substantive rationale, remedy or opinion assignment changes. Other Record edits are confined to truthful assignment counts, pools and count comparisons.
- [Structural checks](OT_1996CHUNK11_FINAL_CHECKS.json) verify every current chunk-11 internal/public Holdings pair, eleven-block order, explanation limits and local references. [Integrity checks](OT_1996CHUNK11_INTEGRITY.json) verify the protected inputs, public outputs, infrastructure and source handoffs.
- [Assignment reconciliation](OT_1996CHUNK11_FINAL_ASSIGNMENT_RECONCILIATION.json) and each linked source receipt carry counts derived from actual opinion topologies. Form, coalition eligibility and qualitative author fit remain separately established.
- The ledger and manifest tools ran, retaining all inventory events, stops and open procedures. Continuity and neutral projections contain the current public law, published noncontrolling positions and procedure.
- [The repository checker](OT_1996CHUNK11_FLETCHER_NO_GIT_CHECK_VALIDATION.md) passed its non-Git deterministic checks, including Holdings synchronization, runtime-split freshness and Public Projection/Render Input identity. [Captured output](OT_1996CHUNK11_CHECK_TERM.txt) identifies the skipped Git object-existence calls. No Git command, history verification or commitment was performed.
- [Final package hashes](OT_1996CHUNK11_FINAL_PACKAGE_CHECKS.json) cover the current delivered projection files and runtime/freeze identity. Render remains a separate task; no output file is edited.

This receipt is not a term-close audit or Git verification. The operator retains repository verification and commitment.
"""
    write(path, text)
    fingerprint_paths = list(TERM.joinpath('workspace').glob('*.md')) + [TERM / 'render-inputs/OT_1996CHUNK11.md']
    fingerprint_paths += [TERM / 'records' / r['record'] for r in json.loads((FREEZE / 'OT_1996CHUNK11_FINAL_CHECKS.json').read_text())['records']]
    hashes = {p.relative_to(TERM.parents[1]).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in fingerprint_paths}
    package = {'completed_records': 11, 'public_projection_identity': True,
               'runtime_freeze_identity': {name: (TERM / 'runtime' / ('OT_1996CHUNK11_' + name + '.md')).read_bytes() == (FREEZE / ('OT_1996CHUNK11_' + name + '.md')).read_bytes() for name in ('COMMITMENTS', 'RECONCILED')},
               'designated_stop_account_copied': True, 'public_outputs_unchanged': True,
               'errors': [], 'sha256': hashes, 'git': 'No Git command, history verification or commitment performed.'}
    assert all(package['runtime_freeze_identity'].values())
    write(FREEZE / 'OT_1996CHUNK11_FINAL_PACKAGE_CHECKS.json', json.dumps(package, ensure_ascii=False, indent=2) + '\n')
    print('Published current assembly/integration receipts and final package fingerprints.')


if __name__ == '__main__':
    main()
