from pathlib import Path
import hashlib

base = Path('terms/OT1997')
source = base / 'freeze/OT_1997CHUNK12_COMMITMENTS_JUNE25_HISTORICAL.md'
raw = source.read_bytes()
s = raw.decode('utf-8')
start = s.index('## National Endowment for the Arts v. Finley')
end = s.index('## United States v. Balsys', start)
original = s[start:end]
target = base / 'freeze/OT_1997CHUNK12_RECONCILED_FINLEY.md'
assert not target.exists(), 'Never revise a completed handoff.'
header = '''# OT1997 chunk 12 — reconciled non-Stone commitments: National Endowment for the Arts v. Finley

Status: completed historical reconciliation; filesystem-durable handoff. Cutoff: June 25, 1998. No Stone position or author assignment. The original frozen model remains unchanged. This document adopts its F1–F4 and Justice-specific grounds except for the express Souter vagueness correction and join clarifications below; the final matrix, not the superseded phrases in the appended original, governs assembly.

## Sources and scope

Authorized inputs are the frozen neutral, original commitments and entering-law slice for June 25, the Finley section of the clean comparator, and the Finley control verification. No raw runtime comparator, original briefs, private position, private Decision Record audit or control receipt was opened. This is not a neutral modeling context. The earlier disclosed bounded Monge comparator overshoot during Diamondstone supplies no premise here and was not passed to any modeler. No Git command was used.

- Frozen neutral `OT_1997CHUNK12_NEUTRAL_JUNE25_HISTORICAL.md`: the live NAAO representative challenge, settlement of the original individual claims, later grant restrictions and their limits, exact §954(d)(1) consideration language and separate §954(d)(2) obscenity prohibition. This review does not adjudicate every 1998 appropriations exception.
- Frozen entering law `OT_1997CHUNK12_ENTERING_LAW_JUNE25.md`: actual Rosenberger, Denver Area and Forbes holdings and separate positions. Rosenberger concerns the opened private-publication benefit, not every expenditure. Forbes's selective debate remains a nonpublic forum subject to reasonableness and viewpoint neutrality; it supplies no categorical government-editor immunity. Denver Area preserves the distinctions among private-editor permission, compulsory burdens and governmental access arrangements. None of these actual rules newly changes the pertinent historical premise enough to support a new join in unrestricted subsidy selection or a refusal to resolve vagueness.
- [Official United States Reports, 524 U.S. 569–623](https://www.govinfo.gov/content/pkg/USREPORTS-524/pdf/USREPORTS-524-569.pdf), saved as `research/chunk12_control/USREPORTS-524-569.pdf` and mechanically extracted `.txt`. Control verified the complete opinion set, including notes. This context read the material merits, overbreadth, spending-priority and vagueness discussions, Scalia's separate rationale and Souter's full substantive dissent including note 17. Particular controls are 580–587 (narrow facial rationale and application limits), 587–588 (Part II-B spending discussion), 588–590 (vagueness), 590–600 (broader rationale), and 600–623 (dissent).

## Material reconciliation corrections

**Souter's vagueness component is corrected.** The original says to refrain from an independent vagueness decision. His historical dissent expressly rejects that claim in note 17, 524 U.S. 622: imprecision inherent in comparative artistic merit is permissible in scarce prizes; the constitutional objection is the separate demand for viewpoint conformity. The actual simulated Forbes dissent and Denver Area positions do not displace that distinction. There is no changed factual, legal, procedural or remedial premise supporting the provisional omission. The corrected commitment rejects facial vagueness but still affirms the injunction on his independent First Amendment overbreadth ground. This does not narrow his concern about chilling from mandatory viewpoint criteria; it distinguishes that concern from unavoidable uncertainty in assessing art.

**Scalia and Thomas agree with the rejection of vagueness on their broader method, not by a complete join in F2's limited balancing explanation.** Their historical writing rejects applying the speech-related vagueness doctrine to a grant program as such, distinguishing its allocation of funds from coercive regulation. The frozen F3 and their own date-eligible positions support that ground. The final commitment preserves their outcome and broader subsidy reasoning but does not manufacture a formal join in the five Justices' narrower opinion simply because its result follows from their approach. Six Associates (the five F1 Justices plus Souter) accept the specific F2 rationale about permissible imprecision in artistic judgments; all eight reject this facial vagueness claim on their stated grounds.

**Ginsburg's withheld scope is the spending-priority discussion, not vagueness.** The historical join excludes Part II-B at 587–588, which invokes broad spending discretion and Rust/Maher; it includes Part III's vagueness rationale. Her F1/F2 position remains, with no join in a broad proposition that government may select favored ideas throughout private arts patronage. The frozen actual Forbes and Denver Area positions do not supply a reason to erase that historical reservation. Her narrow facial-validity vote does not deem the arts program wholly governmental speech.

**F1 preserves review of actual applications without deciding every future case.** The five Justices reject facial invalidation on the limited statutory construction and selective arts context. The consideration command is meaningful, but supplies neither automatic disqualification nor fixed weight. It does not create a categorical viewpoint veto. A proved invidious viewpoint denial, a use of subsidy power to punish independently financed expression, or coercive suppression presents a different claim. Reviewability is not a present holding that every disputed consideration is unconstitutional, and scarcity is not blanket immunity. Scalia and Thomas do not join those limitations as a universal viewpoint-neutral grant-allocation rule; their broader F3 permits the government to disfavor indecent or disrespectful proposed work when choosing what to fund.

## Final commitments by component and Justice

Components: F1 is the narrow First Amendment facial-validity ground; F2 rejects facial vagueness in this comparative artistic-selection setting; F3 is the broader subsidy ground; F4 is Souter's First Amendment facial-invalidity ground. All eight accept reachability of the surviving NAAO controversy on this record. Settled individual denials are not revived or judged under a later-enacted provision.

| Justice | Judgment | Complete grounds and join limits | Source test |
|---|---|---|---|
| Stevens | Reverse facial invalidation and remand for implementation. | F1 and F2. Meaningful contextual consideration without automatic viewpoint exclusion is facially permissible; invidious applications remain reviewable. Artistic comparative judgment differs from the political-candidate selection objections in his Forbes dissent. No F3 join or broad viewpoint-conformity permission. | Historical narrow-opinion join remains consistent with actual Forbes/Denver Area; no material departure. |
| O'Connor | Reverse and remand. | F1 and F2. Selective arts funding can use contextual consideration; the words remain mandatory but not conclusive. The facial challenge fails, while concrete coercion or invidious suppression remains open. Program-specific allocation can differ from direct prohibitions, subject to other constitutional rights; that limited observation does not authorize a viewpoint veto or replace F1 with F3. | Historical rationale and actual Rosenberger/Forbes confirm the bounded construction; no new forum immunity. |
| Scalia | Reverse and remand, on separate grounds. | F3; rejects the vagueness claim because the speech-related vagueness rule does not govern ordinary grant selection as such. Government may prefer decent/respectful art in its appropriations without abridging a rejected artist's ability to create independently. Does not join F1 or F2's full limited explanation. No approval of independent-speech penalties, a disguised regulation or every possible unconstitutional condition. | Historical separate rationale confirms the broader method. Actual forum cases concern opportunities government actually opened and do not compel a new join here. |
| Kennedy | Reverse and remand. | F1 and F2. Mandatory consideration is not on its face compulsory viewpoint suppression; genuine program judgments can coexist with continuing review for invidious discrimination. Does not join F3's broad preference rationale or relabel private art as government speech. | Historical narrow-opinion join is consistent with actual Rosenberger, Denver Area and Forbes; no changed premise. |
| Souter | Affirm facial relief on the First Amendment ground; reject the distinct facial vagueness claim. | F4: decency/respect directs adverse attention to disfavored viewpoints; meaningful consideration cannot be erased by panel diversity or called harmless because nonconclusive. Private arts patronage is not the government's message. Genuine artistic merit remains permissible, but the challenged mandatory criterion has substantial unconstitutional applications and chills expression. F2's permissible-imprecision principle is accepted, without joining F1 or F3. No invalidation of the separate obscenity provision. | Historical note 17 requires the correction from the provisional refusal to reach vagueness; actual entering law provides no Justice-specific changed premise supporting that refusal. |
| Thomas | Reverse and remand, on separate grounds. | F3 and the same broader rejection of vagueness as Scalia. No complete F1/F2 rationale join. A discretionary subsidy preference is distinct from legally suppressing independently financed speech; government need not finance all expression, and opened forums remain separately governed. | Historical separate join confirms these barriers; no material departure. |
| Ginsburg | Reverse and remand. | F1 and F2, with strict reservation of concrete invidious/coercive application claims. Withholds the broader spending-priority/Rust-Maher rationale associated with Part II-B, and does not join F3. No governmental-message fiction or authoritative panel-diversity cure. | Historical exclusion of Part II-B does not exclude Part III. Actual Forbes/Denver Area give no changed premise for either broader funding join or vagueness dissent. |
| Breyer | Reverse and remand. | F1 and F2. Contextual artistic selection and audience suitability need not be mechanical; compulsory viewpoint suppression would remain a different case. No new balancing checklist, panel safe harbor or universal subsidy exemption. | Historical narrow-opinion join and actual contextual Denver Area/Forbes positions support the same limited ground. |

## Result, remedy and reconciliation conclusion

Seven Associates reverse the facial constitutional judgment and corresponding injunction: Stevens, O'Connor, Scalia, Kennedy, Thomas, Ginsburg and Breyer. Souter affirms that relief on F4. Five share F1 (Stevens, O'Connor, Kennedy, Ginsburg and Breyer). Scalia and Thomas support reversal through F3. All eight reject facial vagueness; six support the narrow permissible-imprecision rationale (Stevens, O'Connor, Kennedy, Souter, Ginsburg and Breyer), and two rely on the broader inapplicability ground. Souter's agreement on vagueness does not convert his judgment into reversal.

No grant is awarded or withdrawn; no settled claim, particular denial or individual appropriations eligibility is adjudicated. The case returns for implementation of the facial disposition. The original statute's separate obscenity prohibition is not rewritten, and neither panel diversity nor an unpromulgated agency position eliminates the challenged consideration duty.

This handoff corrects unsupported provisional scope, rather than recording a simulated material departure from history. There is no unresolved blocker for the bounded case. Assembly must respect the final component matrix, test Stone compatibility independently and assign only after determining actual joins. It may not claim eight joins in one rationale, seven joins in F1, or a Ginsburg join in the broader spending discussion.

## Original provisional case section — mechanically copied for audit

The original is preserved below as evidence of the pre-comparator model and its full two-path reasoning, Justice-specific authorities, objections and limits. The original Souter nondecision and any language implying Scalia/Thomas directly join the entire F2 rationale are superseded by the express final commitments above. Other F1–F4 definitions and limits are adopted as clarified.

'''
target.write_text(header + original, encoding='utf-8', newline='\n')
assert source.read_bytes() == raw
assert target.read_text(encoding='utf-8').endswith(original)
print(str(target), len(target.read_bytes()), hashlib.sha256(target.read_bytes()).hexdigest())
print('original unchanged', hashlib.sha256(raw).hexdigest())
