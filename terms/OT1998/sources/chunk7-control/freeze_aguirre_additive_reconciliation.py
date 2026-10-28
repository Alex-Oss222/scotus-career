from pathlib import Path
import hashlib
import re

base = Path('terms/OT1998')
hashes = {
    'freeze/OT_1998CHUNK7_AGUIRRE_COMMITMENTS.md': 'bb7cb13fe974df5cfcc7682a4a0dd44aa6f244c7c3dad8e284872eb5c423d1b2',
    'freeze/OT_1998CHUNK7_AGUIRRE_ADDITIVE_COMMITMENTS.md': '19bde2b2cc9533c4f0e3d7a41eefe3cb1816f4b190a9135b67163b6930087ea7',
    'freeze/OT_1998CHUNK7_AGUIRRE_MERITS_RECONCILED.md': '2e0166579c2679d01a8ccdcc7ce71fdc65416543a4b68f44527f61ff94c4fe4c',
    'freeze/OT_1998CHUNK7_AGUIRRE_PROCEDURE_NEUTRAL.md': '36e1cd9cd6a7b2ec1af3465e01e708ccef28ad37d426c1d9c10a6fc40b057af3',
    'freeze/OT_1998CHUNK7_AGUIRRE_HANDBOOK_NEUTRAL.md': 'efe1aceab19a27b2cb16b0686ff5847ca22c2b3d9b4f0a5a73cd34d31ec939cc',
}
for rel, expected in hashes.items():
    assert hashlib.sha256((base / rel).read_bytes()).hexdigest() == expected, rel
for stem in ('AGUIRRE_COMMITMENTS', 'AGUIRRE_ADDITIVE_COMMITMENTS', 'AGUIRRE_MERITS_RECONCILED'):
    name = 'OT_1998CHUNK7_' + stem + '.md'
    assert (base / 'freeze' / name).read_bytes() == (base / 'runtime' / name).read_bytes(), name
model = (base / 'freeze/OT_1998CHUNK7_AGUIRRE_ADDITIVE_COMMITMENTS.md').read_text(encoding='utf-8')
copied = model[model.index('## A2 —'):model.index('## Justice-specific affected comparison and joins')].rstrip()

head = '''# INS v. Aguirre-Aguirre — final additive reconciliation

**Docket and event:** No. 97-1754; May 3, 1999; argued March 3, 1999.
**Ready scope:** Complete eight-Associate reconciliation. All eight retain reversal of the Ninth Circuit and a bounded judicial remand, with direct joins in A1–A4 as defined below. No author, ninth vote, final Court count or assignment is selected.

## Authority, lineage and released hold

Read this file with [the initial merits reconciliation](OT_1998CHUNK7_AGUIRRE_MERITS_RECONCILED.md). That earlier handoff remains authoritative for unchanged A1–A3 and its individual historical testing. This additive handoff controls the refined A2–A3 attribution, the complete A4 procedure and the express record-modification condition. It supersedes the earlier handoff's A4 hold and any shorthand that could attribute a universal atrocity prerequisite to the Ninth Circuit. No old frozen bytes are rewritten.

The [additive independent commitments](OT_1998CHUNK7_AGUIRRE_ADDITIVE_COMMITMENTS.md), SHA256 19bde2b2cc9533c4f0e3d7a41eefe3cb1816f4b190a9135b67163b6930087ea7, were received only after independent freezing. Both clean neutral additions and their receipts were read completely. The new model independently retains all eight votes after evaluating the actual agency motion, claim-specific preservation, evidence-triggered burden, Handbook arguments and McMullen comparison. This reconciliation does not supply a new choice through historical attribution.

Research cutoff is May 3, 1999. Complete LAW07 and the actual earlier Haggar and UNUM public law were read in the initial reconciliation; no same-day LaSalle or Neztsosie decision is used as entering law. Haggar's later naming of cleaning, lubricating and painting is editorial and changes no administrative-law premise. Its former exact public bytes remain preserved for the original source receipt.

The complete historical Cornell opinion, including Parts II.B–C and III, was read in the initial reconciliation; its sole writing and absence of numbered notes were verified. The official report corroborates inventory, dates, burden and closing procedure. No historical authorship or assignment follows. No private position, combined brief, raw Record or assembly material was read, and no Git command occurred.

## Retained A1 and exact final A2–A4

A1 remains unchanged: actual authority under sections 1103(a)(1), 1253(h) and the Board's adjudicative assignment precedes deference to a permissible construction within genuine ambiguity. Statutory boundaries, supported factual review and the actual agency explanation remain separate. An executive label, foreign-relations concern or the absence of notice-and-comment procedure does not replace that analysis.

The following A2–A4 text is mechanically copied from the additive independent freeze. The condition and historical comparison following it clarify its already selected procedural limits; they do not add a compulsory new agency undertaking.

'''

tail = '''

## Express condition for possible agency reconsideration

The pending BIA motion remains available for lawful determination. **If the BIA determines that modification of the record is necessary, it may determine whether the modified record warrants further consideration of withholding.** The judgment neither finds the alleged errors nor requires record modification, a new hearing or further withholding consideration merely because the applicant filed the motion. Nor does it foreclose reconsideration that the Board finds appropriate under the lawful motion process.

This condition implements the independent A4 choice to decide the presented statutory questions while preserving the existing motion and refusing to preordain it. It does not declare that record modification is the only legally possible basis for any future agency action or promise that any particular motion satisfies its governing requirements. The allegation's late presentation does not become a universal forfeiture rule. There is no order to file another motion, no new deadline, no stay, no immediate-removal instruction and no retained Supreme Court proceeding.

## Historical reconciliation of the affected components

The historical Court unanimously reversed and remanded. That result and the reasoning supply strong evidence for the frozen Associate choices, but the present handoff adopts only the grounds and qualifications independently supported here. Historical Kennedy authorship is not an assignment. No historical ninth vote is imported.

**A2 and paragraph 156.** The historical opinion actually addressed the Ninth Circuit's Handbook-based offense/persecution argument. The repaired model now attributes that argument accurately and rejects the extra statutory requirement on its own textual and structural ground. The quoted guidance can inform interpretation without supplying an enacted mandatory balance. This narrower formulation reaches the same supported result without requiring a general holding about every use of the Handbook or treaty enforceability. There is no changed premise requiring any Associate to abandon A2.

**A3 and paragraph 152.** The historical opinion separately addressed gross disproportion, atrociousness and the proposed comparison with McMullen. The circuit's reported request for attention to those matters must not be rewritten as a necessarily universal atrocity element. The additive model gives the consistency argument its strongest supported form: considerably less severe conduct may require scrutiny of the agency's reason. The Board's actual political/criminal comparison and disproportionate-conduct explanation answer that legal objection; McMullen's greater atrocity supplies no minimum threshold for the alternative ground. A separate atrocity finding and atrocity-specific case comparison are not required to sustain that explanation. Actual political purpose, relevant consistency objections and supported-fact review remain available at their proper scope.

The original A3 limits on mandatory additional political-necessity/success findings remain. They do not eliminate political context, announce an exhaustive offense definition or decide the independent relevance of a causal-link inquiry in another case. Even a causal connection would not necessarily defeat a supported disproportion determination. No new finding characterizes these acts as atrocious or resolves the translation allegation.

**A4, preservation and the pending motion.** The historical closing section declines to resolve the newly presented translation/transcription argument and identifies the already filed agency motion, with further withholding attention dependent on the Board's record-modification determination. The clean model independently selected the same division: resolve the presented legal errors, leave the late factual claim undecided, preserve lawful agency consideration and compel no hearing. The express condition above supplies that procedural precision without importing a decision on the motion. The Court's reversal does not transform the new allegation into a claim previously decided by the circuit.

**Conditional burden.** The historical opinion quotes the evidence-triggered regulation and mentions the absent Board brief. The additive model's more precise account is supported: the repeated reported bus burnings, civilian assaults and actual agency comparison indicate the particular exclusion on the unrevised record; the ensuing burden concerns whether that exclusion applies. Missing briefing is not the substantive evidence, does not erase testimony and supplies no default. The model preserves the statutory serious-reasons standard, regulatory preponderance allocation, persecution showing and judicial review standard as distinct. Nothing in history requires a contrary vote or a categorical finding that nonfiling itself defeats the application.

The initial A1–A3 grounds remain sufficient without a default premise. The new burden application concerns the existing agency account and is subject to the lawful record-error process; it is not a new credibility determination. Reversal and remand correct the circuit's review, not an unpresented motion result or an award of asylum/withholding. The separate discretionary asylum determination retains its independent character under the applicable former law.

## Eight-Associate affected-premise and join audit

All eight directly join A1, A2, A3 and the completed A4, including the express condition above. Each retains the corresponding reversal and judicial remand. No partial join, judgment-only position or separate writing is required by these commitments. The following comparison preserves the clean model's individual bases and tests the strongest historical contrary implication rather than treating the historical unanimity as a vote generator.

| Justice | Individual premise and strongest affected alternative | Reconciled choice and limit |
|---|---|---|
| Stevens | His Elias-Zacarias dissent makes political context and the McMullen difference substantial; his NationsBank and Haggar framework joins recognize reasoned delegated choice, and his Haggar separate position permits deciding a supported application now. A real translation error could alter that application. | The existing Board comparison answers the identified legal objection; the unproved error claim remains with the existing motion. Historical full agreement corroborates this division. Joins all four and the conditional reconsideration language, with no disregard of political evidence or missing-brief default. |
| O'Connor | Her Elias-Zacarias position and NFFE Part II objection require context and the agency's own adequate explanation; Yang and Haggar do not validate every agency action automatically. A materially inconsistent classification would warrant further review. | The actual disproportionate-conduct explanation distinguishes McMullen's greater atrocity without making it a threshold. The new motion is neither decided nor futile by decree. Full joins remain historically supported, conditioned on actual evidence before the regulatory burden and no universal late-claim forfeiture. |
| Scalia | His Elias-Zacarias opinion separates elements and factual review; MCI/NCUA, NationsBank and Haggar preserve enacted boundaries and actual delegation. The humanitarian argument cannot silently add an exclusion override. | Historical agreement supports A1–A4 on these grounds. The conditional burden retains its evidence trigger and differs from serious reasons and persecution proof. Joins the ordinary remand and leaves the late allegation unresolved, without new motion adjudication or removal command. |
| Kennedy | His AT&T position distinguishes authority from validity; NationsBank, NFFE and Haggar demand the actual agency reason. The stronger comparative objection requires examining that reason rather than invoking abstract deference. | The Board actually explained political/criminal disproportion. The known motion and preservation facts justify the independent procedural division. Historical reasoning corroborates full joins and conditional reconsideration; historical authorship supplies no role here. |
| Souter | His NationsBank and Yang opinions require reasoned consistency; his NFFE join returns an unmade choice after a material premise changes. The Handbook and McMullen material sharpen the explanation objection. | No invalid compulsion premise undermines this Board explanation. The alleged record error remains a separate unproved question for the actual motion process. Historical full agreement supports all four joins with no categorical guidance irrelevance, automatic hearing or default. |
| Thomas | His MCI/NCUA, Elias-Zacarias, NationsBank and Haggar positions enforce each assigned statutory condition. No filed brief is not itself conduct evidence; a new allegation is not an established record correction. | Actual delegation and the evidence-indicated exclusion support the legal result and triggered burden. All four joins remain historically supported; further withholding attention may follow a necessary record correction through lawful agency process, with no conviction requirement, later-law substitution or compelled reopening. |
| Ginsburg | Her NationsBank, NFFE and Haggar joins require genuine authority and reasoned application; her Haggar separate join permits present resolution of an adequately supported issue. Possible record error and the legal comparison are distinct. | The comparative reason supports correction of the circuit's legal requirements, while the pending motion can address any established record defect. Historical full agreement confirms all four joins with the exact evidence trigger, political context and no finding that the allegation is false. |
| Breyer | His AT&T separate position requires actual explanation; NationsBank, Yang, NFFE and Haggar recognize evaluative judgment. Handbook guidance and comparative severity can test that explanation without becoming an exhaustive judicial checklist. | The Board's actual comparative reason supports the selected rules. A possible translation defect receives its existing lawful channel, not an automatic hearing. Historical agreement confirms all four joins and conditional reconsideration, without automatic agency acceptance or a nonfiling concession. |

**Changed-premise conclusion:** The new procedural facts refine the remedy and explain why the late allegation is not resolved here. The corroborated Handbook passages correct argument attribution and strengthen the opposing path. Neither supplies a Justice-specific reason to change the frozen result or any direct join. The actual prior simulated administrative-law holdings support the same bounded rules, and no material departure from the historical Associate positions is established. More precise explanation and narrower reservation of unneeded Handbook-status questions do not create a conflicting vote.

## Assembly-ready scope and validation limits

The whole matter is ready for the next authorized stage using the initial merits handoff together with this additive handoff. Copy the unchanged A1 and initial A1–A3 limits, apply the precise A2–A3 clarifications above, and use this complete A4 and its express condition. The earlier A4 hold is closed. The original independent freezes, both neutral freezes and prior reconciliation remain unchanged; their chronological statements continue to describe their earlier scope.

The source-extract chronology limitation remains internal: the first derived extract's exact former bytes were not recovered, although its original hash and frozen neutral copies survive. The current expanded extract and its separate neutral validation are identified by their actual hashes. No prior derived file is falsely represented as byte-recovered, and no litigant procedural consequence follows from that operator-source limitation.

Primary sources: [Cornell opinion, No. 97-1754](https://www.law.cornell.edu/supct/html/97-1754.ZO.html), read completely with its sole-writing inventory; [official 526 U.S. 415–433](https://tile.loc.gov/storage-services/service/ll/usrep/usrep526/usrep526415/usrep526415.pdf), used for the scoped corroboration recorded in the initial receipt. Original motion contents, verified transcript corrections and a motion disposition have not been independently supplied. No selected rule depends on inventing them.

This is an internal non-Stone reconciliation only. No Record, final Court count, assignment, public output or term-wide validation is created or certified. The companion receipt verifies the supplied input hashes, unchanged originals, exact copied model block and identical runtime/freeze output. Mechanical checks do not decide legal sufficiency.
'''

text = head + copied + tail
assert copied in text
assert '## Exact A4 hold' not in text
assert 'All eight directly join A1, A2, A3' in text
assert not re.search(r'(?:https?://(?:github|[^/]*onedrive)|file://|[A-Z]:\\)', text, re.I)
name = 'OT_1998CHUNK7_AGUIRRE_ADDITIVE_RECONCILED.md'
for directory in ('freeze', 'runtime'):
    dest = base / directory / name
    assert not dest.exists(), str(dest)
    dest.write_text(text, encoding='utf-8', newline='\n')
assert (base / 'freeze' / name).read_bytes() == (base / 'runtime' / name).read_bytes()
digest = hashlib.sha256((base / 'freeze' / name).read_bytes()).hexdigest()
for rel, expected in hashes.items():
    assert hashlib.sha256((base / rel).read_bytes()).hexdigest() == expected, rel

inputs = list(hashes) + [
    'freeze/OT_1998CHUNK7_AGUIRRE_ADDITIVE_VALIDATION.md',
    'freeze/OT_1998CHUNK7_AGUIRRE_PROCEDURE_NEUTRAL_VALIDATION.md',
    'freeze/OT_1998CHUNK7_AGUIRRE_HANDBOOK_NEUTRAL_VALIDATION.md',
    'entering-law/OT_1998CHUNK7_AGUIRRE_PROCEDURE_SOURCE_EXTRACT.md',
    'entering-law/OT_1998CHUNK7_LAW_07_aguirre.md',
    'sources/chunk7-control/aguirre-ZO.txt',
    'sources/chunk7-control/aguirre-ZS.txt',
    'sources/chunk7-control/aguirre-official.txt',
]
rows = ['| ' + rel + ' | ' + hashlib.sha256((base / rel).read_bytes()).hexdigest() + ' |' for rel in inputs]
receipt = '''# Aguirre final additive reconciliation validation

**Result:** Ready. The additive handoff closes the earlier A4 hold. All eight Associates retain reversal and bounded judicial remand with direct joins in A1–A4 as clarified. Initial merits reconciliation remains authoritative for unchanged rules; this addition controls exact Handbook attribution, complete procedure, burden and the record-modification condition. No new writing, author, ninth vote or Court count is assigned.

Output: `freeze/OT_1998CHUNK7_AGUIRRE_ADDITIVE_RECONCILED.md`, with identical runtime copy.

SHA256: ''' + digest + '''.

## Checks actually completed

- Read both neutral additions and receipts, complete additive commitments and receipt. Prior full lawful inputs and complete historical sole-opinion read remain the foundation. No numbered historical note or separate writing is omitted; official duplicate corroboration is accurately limited.
- Verified the supplied original, additive, neutral and prior merits hashes before writing and again afterward. The original commitment, additive commitment and initial merits runtime copies match their authoritative freezes.
- Mechanically copied the complete additive A2–A4 block. Tested all eight individual changed-premise paths against their own eligible bases and the historical evidence. No changed vote or material historical departure is established.
- Preserved paragraph 156's persecution/offense argument separately from paragraph 152 and McMullen's consistency argument. The prior shorthand does not become a universal atrocity condition attributed to the Ninth Circuit. No universal Handbook-status or treaty holding is added.
- Preserved the actual evidence trigger and conditional preponderance allocation independently of serious reasons, persecution proof and judicial fact review. The missing brief supplies no default, concession or adverse inference.
- Precisely preserved the already pending motion and late claim. If the Board finds record modification necessary, it may determine whether further withholding consideration is warranted; neither follows automatically from the allegation or filing. No motion result, new hearing, stay, deadline, removal command or new factual finding is imported.
- Verified identical freeze/runtime output, exact copied block, relative local references and absence of prohibited absolute-local, GitHub or OneDrive links. Wrote only new files within this term; no Git command or top-level private-directory access occurred.
- The predecessor extract's exact byte-recovery limitation remains disclosed; no reconstructed artifact is falsely certified as that earlier source. Frozen neutral content and actual hashes remain intact.

This receipt certifies only this reconciliation and the checks above. No assembly, Record, public render or check_term is claimed. Deterministic checks verify bytes; the handoff states the qualitative legal judgment.

## Input hashes at final reconciliation

| Input | SHA256 |
|---|---|
''' + '\n'.join(rows) + '\n'
receipt_path = base / 'freeze/OT_1998CHUNK7_AGUIRRE_ADDITIVE_RECONCILIATION_VALIDATION.md'
assert not receipt_path.exists()
receipt_path.write_text(receipt, encoding='utf-8', newline='\n')
print(name)
print(digest)
print('Input hashes preserved; output identity verified; all eight A1-A4 joins retained; prior A4 hold released.')
