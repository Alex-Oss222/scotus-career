from pathlib import Path
import hashlib

base = Path('terms/OT1998')
frozen = base / 'freeze/OT_1998CHUNK7_AGUIRRE_COMMITMENTS.md'
expected = 'bb7cb13fe974df5cfcc7682a4a0dd44aa6f244c7c3dad8e284872eb5c423d1b2'
assert hashlib.sha256(frozen.read_bytes()).hexdigest() == expected
assert frozen.read_bytes() == (base / 'runtime/OT_1998CHUNK7_AGUIRRE_COMMITMENTS.md').read_bytes()
model = frozen.read_text(encoding='utf-8')
merits = model[model.index('### A1.'):model.index('### A4.')].rstrip()

head = '''# INS v. Aguirre-Aguirre — reconciled merits, bounded procedural hold

**Docket and event:** No. 97-1754; May 3, 1999, following March 3 argument.
**Status:** A1–A3 are reconciled and ready. A4 is not certified for assembly by this artifact. The historical opinion disclosed an existing agency motion and preservation facts absent from the initial neutral packet; their treatment returns to fresh neutral review and independent modeling. No final complete case disposition or author is selected here.

## Frozen inputs and source scope

The independent [Aguirre commitments](OT_1998CHUNK7_AGUIRRE_COMMITMENTS.md), SHA256 bb7cb13fe974df5cfcc7682a4a0dd44aa6f244c7c3dad8e284872eb5c423d1b2, remain unchanged. Their original A1–A3 text is copied below; historical evidence tests it rather than replacing the independent choice. The frozen neutral Aguirre section, applicable common and supplemental materials, complete LAW_07_aguirre and actual earlier Haggar and UNUM public material supply the authorized background. Current Haggar's naming of cleaning, lubricating and painting clarifies examples already in the neutral statutory text; it changes no rule or Aguirre premise. The exact preclarification Haggar input is preserved separately for hash verification.

After the commitment freeze, the Aguirre comparator and complete Cornell opinion were read, including all of Parts II.B–C and III that the earlier source-control receipt had left unread. The opinion has no separate writing and no numbered footnotes. Its syllabus and the official report confirm that inventory. The official report was used for corroboration of the header, lineup, conditional-burden text and closing procedure; this receipt does not claim that every page of the duplicate official transcription was separately read. Research cutoff: May 3, 1999. No later doctrine enters the analysis.

Historical Kennedy authorship and the historical ninth vote provide no assignment or vote here. Only the eight Associates are reconciled. No private position, combined brief, raw Record, assembly file or top-level private directory was opened; no Git command occurred. The pending neutral repair does not reopen completed unrelated cases.

## A1–A3 retained operative commitments

'''

tail = '''

## Complete historical comparison of the merits

The historical opinion supports the eight Associates' same result on each identified circuit error. It recognizes actual statutory and adjudicative delegation, accepts the Board's political-versus-criminal comparison, rejects a mandatory additional persecution-risk balance, rejects atrociousness as a necessary condition, and rejects mandatory further necessity/success findings on this agency explanation. The stronger historical executive/foreign-relations discussion is not needed for A1 and does not enlarge it. Historical agreement is evidence, not the source of an automatic vote.

The precise factor distinctions are preserved:

- Prospective persecution remains the paragraph (1) eligibility inquiry. A2 allows the Board to decide the paragraph (2) exception on the assumption that the applicant could establish persecution; it does not find no threat or convert otherwise mandatory withholding into free discretion. No additional risk-versus-crime balance is required; this is not a prohibition on considering every relevant circumstance.
- Gross disproportion and atrocious conduct can demonstrate predominating criminal character. Atrocious means can defeat the political characterization under the Board's approach, but atrocity is not necessary to every serious nonpolitical crime. This case requires no new finding that these particular acts were atrocious.
- The Ninth Circuit's suggested comparison with McMullen concerned the meaning of atrociousness. Because this Board determination rests on the political/criminal comparison and disproportion, absence of a separate comparison to McMullen's atrocious acts does not itself require reversal. This does not prohibit relevant comparisons or excuse unexplained inconsistency in another case.
- The Board actually addressed the political objectives and the disproportionate property destruction and assaults on civilians. The rejection of obligatory necessity/success findings does not make political purpose immaterial or substitute a judicial factual account. A clear causal connection would not necessarily defeat an otherwise supported disproportion determination. Any independent causal-link requirement in a different case remains open; A3 supplies no comprehensive code of political offenses.

The Ninth Circuit's reliance on Handbook paragraphs 156 and 152 strengthens the already considered contrary arguments for humanitarian balancing and political-context evaluation. The source-only repair now identifies those passages. It does not introduce a new adjudicative fact on which A1–A3 depends. The historical opinion also evaluated the Handbook's legal status, but this handoff adds no separate treaty or Handbook-binding-status holding beyond the frozen model. Interpretive relevance and weight remain distinct from a mandatory additional statutory condition. No broader conclusion is inferred from a quoted fragment or from a guidance label.

## Justice-specific reconciliation and exact join scope

Every row retains a direct join in all of A1–A3, including their bounded applications. The frozen preference to reverse the circuit's identified legal grounds remains supported; complete A4 procedural implementation awaits the separate repaired handoff. These are not judgment-only joins.

| Justice | Strongest contrary consideration and own eligible premise | Reconciliation |
|---|---|---|
| Stevens | His Elias-Zacarias dissent requires serious attention to political context. His NationsBank and Haggar framework joins recognize actual interpretive delegation, and his Haggar separate position permits resolution of an adequately supported application. | The Board acknowledged the protest aims and compared them with the destruction and civilian assaults. The Handbook argument reinforces humanitarian stakes without supplying an enacted balancing override. His historical full join confirms the independently supported A1–A3; no changed merits premise warrants departure. |
| O'Connor | Her Elias-Zacarias position resists erasing politics; her NFFE Part II objection insists on an actual agency explanation. NationsBank, Yang and Haggar support bounded evaluative authority. | The Board's own comparison, rather than counsel's invented rationale or mere executive status, answers her explanation concern. No unexplained compelled-policy premise resembling NFFE appears. Historical full agreement confirms A1–A3 at this scope. |
| Scalia | His MCI/NCUA and Haggar positions require enacted limits before deference; Elias-Zacarias separates legal elements from supported factual review. | Sections 1103 and 1253 supply actual authority while every territorial, temporal and substantive exception condition survives. Mandatory additional humanitarian or atrocity elements lack that textual basis. His historical agreement confirms all three bounded rules, not automatic foreign-affairs deference. |
| Kennedy | His AT&T position distinguishes authority from a particular rule's validity, while NationsBank, NFFE and Haggar recognize reasoned delegated choice. | The actual Board standard and its stated application are separately tested, satisfying the distinction. Historical authorship supports his known grounds but creates no assignment or broader language requirement here. He joins A1–A3 without a new factual or removal ruling. |
| Souter | NationsBank and his Yang opinion require reasoned administration; his NFFE join remands when correction leaves a material agency choice unmade. | Here the Board already chose and applied the relevant political/criminal comparison, independent of a mistaken compulsion premise. Elias-Zacarias and Haggar preserve distinct fact/law review. Historical full agreement corroborates all three merits joins without a categorical no-remand principle. |
| Thomas | His MCI/NCUA and NFFE positions enforce specific statutory assignments; NationsBank and Haggar permit construction within an actual delegation. | The Attorney General's task and the Board's adjudicative assignment are established, unlike a disputed transfer of a specifically assigned function. The exception retains each enacted condition and adds no conviction prerequisite. Historical agreement supports all three merits joins. |
| Ginsburg | MCI/NCUA preserve statutory predicates; NationsBank, NFFE and Haggar support bounded implementation. Her Haggar separate join distinguishes a supported application from one requiring further agency work. | Humanitarian consequences and political purpose are preserved, and the Board's existing comparison supplies the pertinent reason. Neither later statutes nor an automatic asylum bar is imported. Historical full agreement confirms A1–A3 rather than requiring new inquiry by category. |
| Breyer | His AT&T separate position requires explanation under the actual lawful standard; NationsBank, Yang, NFFE and Haggar recognize evaluative administration. | The Board's actual comparative explanation satisfies the present legal objection. A judicial mandatory factor list would displace that choice, but the selected rule still requires actual political-context analysis. Historical agreement supports all A1–A3, with any record-error procedure separately reserved. |

No material merits departure from the historical positions is established. The actual prior simulated administrative-law holdings sharpen the explanation and limits but do not supply a changed premise supporting a different Associate vote. No author or ninth vote is inferred.

## Conditional burden and nonfiling: no change to A1–A3

The regulatory passage applies only if evidence indicates that one or more denial grounds apply; on that trigger the applicant bears a preponderance burden to prove that those grounds do not apply. The historical syllabus's broad shorthand is not substituted for that condition. The published recitation that respondent did not file a Board brief after an extension supplies neither a default nor an adverse factual inference.

A1 concerns the source and limits of interpretive authority; neither the burden nor nonfiling changes that legal allocation. A2 concerns whether the exception requires an additional persecution-risk balance; neither changes the separation of the statutory inquiries. A3 rests on the announced comparison and the actual supported Board explanation already in the frozen neutral packet. It does not depend on respondent losing by silence or on a new finding that he failed the regulatory burden. These independent sufficient grounds preserve all eight merits joins. A future correction of the testimony could change the agency application, which is exactly why the existing motion belongs in the separate A4 review; no frozen merits rule prevents lawful reconsideration of a corrected record.

## Exact A4 hold and permitted next step

The initial packet did not identify respondent's alleged translation/transcription errors, first presentation in his opposition to certiorari rather than before the Board or circuit, or the already filed Board motion for a new hearing. The [mechanical procedural extract](../entering-law/OT_1998CHUNK7_AGUIRRE_PROCEDURE_SOURCE_EXTRACT.md) supplies those published recitations, the regulatory condition and the lower-court Handbook argument for clean validation. It states allegations as allegations and creates no missing-document default.

Fresh neutral review must classify those facts and independent modeling must determine the resulting A4 treatment: the existing motion's proper channel; whether and how record modification may call for further withholding consideration; the late claim's preservation treatment; and the exact relationship to reversal and appellate remand. No historical disposition of the late claim is imported into that new independent choice. The initial frozen A4 text is preserved but is not certified as the complete final remedy. No new hearing, grant or denial of the motion, finding that errors occurred, stay, immediate removal instruction or new burden finding is supplied here.

This is a component hold only. A1–A3 may be copied from this artifact after the fresh context confirms that the corrected facts do not change a sufficient merits premise. The complete case awaits an additive reconciled A4 handoff; no other case is blocked by this repair.

## Source and validation limits

Primary full-opinion source: [Cornell, No. 97-1754, opinion](https://www.law.cornell.edu/supct/html/97-1754.ZO.html). Official corroboration: [526 U.S. 415–433](https://tile.loc.gov/storage-services/service/ll/usrep/usrep526/usrep526415/usrep526415.pdf). No separate historical writing exists. The historical full-opinion read is complete; original briefs and the hearing transcript have not been independently certified complete in this reconciliation. Published recitations support the bounded facts; the alleged accuracy defect remains unresolved.

This internal handoff supplies no assignment, final Court arithmetic, Record, public render, or term validation. A sibling receipt verifies original commitment identity, handoff identity and source hashes. Deterministic validation verifies bytes, not judicial judgment.
'''
text = head + merits + tail
name = 'OT_1998CHUNK7_AGUIRRE_MERITS_RECONCILED.md'
for directory in ('freeze', 'runtime'):
    dest = base / directory / name
    assert not dest.exists(), str(dest)
    dest.write_text(text, encoding='utf-8', newline='\n')
assert (base / 'freeze' / name).read_bytes() == (base / 'runtime' / name).read_bytes()
digest = hashlib.sha256((base / 'freeze' / name).read_bytes()).hexdigest()
inputs = [
    'freeze/OT_1998CHUNK7_AGUIRRE_COMMITMENTS.md',
    'freeze/OT_1998CHUNK7_AGUIRRE_MODEL_VALIDATION.md',
    'entering-law/OT_1998CHUNK7_LAW_07_aguirre.md',
    'freeze/OT_1998CHUNK7_HAGGAR_PUBLIC_BEFORE_EDITORIAL_CLARIFICATION.md',
    'entering-law/OT_1998CHUNK7_HAGGAR_PUBLIC.md',
    'entering-law/OT_1998CHUNK7_UNUM_PUBLIC.md',
    'entering-law/OT_1998CHUNK7_AGUIRRE_PROCEDURE_SOURCE_EXTRACT.md',
    'sources/chunk7-control/aguirre-ZO.txt',
    'sources/chunk7-control/aguirre-ZS.txt',
    'sources/chunk7-control/aguirre-official.txt',
]
rows = []
for rel in inputs:
    p = base / rel
    rows.append('| ' + rel + ' | ' + hashlib.sha256(p.read_bytes()).hexdigest() + ' |')
receipt = '''# Aguirre merits reconciliation validation

Scope: reconciled A1–A3 only; A4 held for the fresh neutral/procedural model. This is an additive freeze, preserving the original eight-Associate commitments and their original receipt. No completed adjudication is modified.

Both freeze and runtime handoffs are byte-identical. SHA256: ''' + digest + '''.

Original commitment hash matches the supplied authorized hash and runtime matches it. The copied A1–A3 block is mechanically selected from that frozen input. Every Associate retains a direct join in the three merits rules; no missing brief supplies default or an adverse inference. A4 requires a separate successor handoff. Historical sole-opinion reading is complete, including all previously unread sections; no numbered footnote or separate writing is omitted. Official duplicate corroboration is scoped, not falsely certified as another complete read.

No Git command, assignment, private-position read, assembly, Record modification or check_term occurred. Writes are confined to this term. The script checks identity and hashes; the accompanying natural-language handoff supplies the qualitative legal reconciliation.

| Input | SHA256 |
|---|---|
''' + '\n'.join(rows) + '\n'
receipt_path = base / 'freeze/OT_1998CHUNK7_AGUIRRE_MERITS_RECONCILIATION_VALIDATION.md'
assert not receipt_path.exists()
receipt_path.write_text(receipt, encoding='utf-8', newline='\n')
print(name)
print(digest)
print('Original commitments unchanged; runtime identity confirmed; A4 hold explicit.')
