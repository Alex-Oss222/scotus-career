from pathlib import Path

term = Path(__file__).resolve().parent.parent
original = (term / 'freeze/OT_2002CHUNK8_C_COMMITMENTS.md').read_text(encoding='utf-8')
body = original.split('## 101. ', 1)[1].split('## Handoff validation', 1)[0]
body = '## 101. ' + body

notes = {
    "## 101. Women's Medical Center of Northwest Houston v. Bell — April 22, 2003": """### Historical reconciliation determination

**Retain all eight frozen component commitments and their stated join limits.** The comparator is the Fifth Circuit's April 13, 2001 judgment, not a Supreme Court merits vote. The complete issuing-court opinion, including all notes, confirms the split preliminary relief, unappealed access ruling, significant civil sanctions, lack of an objective compliance measure and unchallenged severability. No factual supplement or new premise is necessary. The frozen result matches that split disposition, but its legal explanation must follow the current entering law.

The source's linkage of rational review to the absence of anti-abortion animus cannot become a complete rule for protected access. The distinct provider-classification claim is governed by ordinary rationality; a properly presented access claim retains Casey's complete standard, including residual meaningful interference, the applicable State justification burden and fitted relief. The frozen commitments preserve that distinction without reopening an unappealed preliminary ruling. This is a limitation on the source rationale's reuse, not a new grant, a source-possession condition or a historical Supreme Court vote departure.

The individual comparisons remain operative: Stevens's concrete public-end inquiry in his Beach/Craigmiles positions is satisfied by inspection, infection control and oversight of the very medical activity being regulated; no new general endorsement of every conceivable-purpose formulation is inferred. O'Connor and Souter preserve their complete Casey framework joins. Ginsburg and Breyer preserve the meaningful access inquiry reflected in Owens and Newman. Kennedy preserves protected choice and necessary care without adopting the residual lesser-burden rule he withheld in those cases. Scalia and Thomas need not adopt the asserted substantive abortion right to recognize ordinary civil-sanction vagueness. Consequently all eight can join the specific classification, ordinary-vagueness and procedural-preservation grounds below; none is deemed to retract a prior separate position.

**Remedy and completeness check:** Affirm the appellate judgment: the volume-threshold injunction remains dissolved; preliminary restraint remains against precisely §§139.51(1), 139.51(2) and 139.2(43). Likelihood of success does not alone sustain an injunction: the established irreparable-injury, comparative-harm and public-interest findings also support the three-provision restraint. The mandate returns ordinary merits proceedings; it neither awards final relief against the whole licensing system nor resolves the availability or adequacy of alternative care. A future actual limiting construction can be assessed if presented; its hypothetical availability is no current cure.

""",
    '## 102. Franchise Tax Board of California v. Hyatt — April 23, 2003': """### Historical reconciliation determination

**Retain all eight frozen commitments.** The primary syllabus identifies the single historical Court writing and unanimous result; that complete writing, with its notes and qualifications, has been read. Every Associate's proposed affirmance matches the historical judgment on the actually presented full-faith-and-credit question. The comparator's opinion assignment supplies no assignment instruction for this Court.

Historical agreement is independently supported despite the changed Alden premise. The present Alden permits an expressly enacted federal FLSA remedy in a competent state court; it does not decide interstate tort amenability or require Nevada to export California immunity. Conversely, O'Connor, Scalia, Kennedy and Thomas retain their Alden immunity position without transforming it into an answer to a statutory conflicts question that Hall still governs. Stevens, Souter, Ginsburg and Breyer can rely on Hall's legislative-immunity holding without extending their Alden ground beyond the valid federal remedy there. Baker's unanimous lawful-recognition rule remains distinct from the divided additional-forum-control issue; neither side of that division treats an immunity statute as an adjudicated judgment.

The strongest contrary route protects tax administration as a sovereign function. Neither that function's importance nor ordinary litigation expense establishes a constitutional distinction requiring a special export rule. The supplied Nevada connection and evenhanded use of Nevada's own intentional-tort policy suffice; there is no supported hostile rule to correct. The historical opinion's discussion of competing sovereign interests confirms, rather than displaces, that ground. The Court need not devise a comparative-ranking test for State functions or adjudicate Hall's general constitutional amenability holding, which lies outside the supplied question.

**Remedy and completeness check:** Affirm Nevada's refusal of compelled California statutory immunity on the alleged intentional torts. Ordinary proceedings on those claims remain available; the negligence dismissal under comity remains effective. No allegation is established as fact, no damages follow, and the validity of the tax assessments is not determined. No material historical departure or later-matter predicate displacement is identified on this supplied question.

""",
    '## 103. Gorski v. New Hampshire Department of Corrections — May 27, 2003': """### Historical reconciliation determination

**Retain all eight frozen commitments on both components.** The First Circuit's May 24, 2002 opinion is the comparator, not a historical Supreme Court merits decision. Its complete text and footnotes confirm the pleaded harassment theory, district-court substitution of a transfer theory, discovery limited to that latter theory, lack of a supported refusal or futility showing, unresolved resignation-date inconsistency and limited remand. The present Court reviews the supplied two components under the authorized presentation premise. No invented petition wording or cross-petition is needed to preserve the transfer judgment against Gorski.

The First Circuit's result remains supportable under the actual simulated authorities, not by importing every doctrine associated with the historical cases it cites. O'Connor's Harris rule, Thomas's Oncale rule and Scalia's Swierkiewicz rule each have the stated complete coalition in the entering slice. Stevens, Kennedy, Souter and Ginsburg joined those relevant rules. Breyer's Faragher and all eight Associates' Ellerth commitments preserve proof of actual authority materially aiding harassment, while rejecting automatic attribution from title and automatic complete immunity from a known policy or nonreporting. The present pleading record does not establish any of those ultimate agency facts. The different factual completeness of Faragher's bench findings explains why its conclusive remedy is not transplanted.

Stout is effective before this May 27 event but not the April cases in this group. Scalia, Kennedy and Thomas's Stout evidence objection addresses the required comparative effect in an impact case; it does not negate their own fair-notice pleading commitments or the enacted pregnancy coverage here. No impact theory or new comparative-proof element enters this harassment suit. This is an actual doctrinal distinction supporting their result, not an unexplained vote change. The other five Associates likewise preserve substantive proof and ordinary evidentiary review after a sufficient complaint.

**Remedy and completeness check:** Affirm reinstatement of the hostile-environment theory and preservation of the separate transfer summary judgment. Ordinary further proceedings must distinguish allegation sufficiency, ultimate severe-or-pervasive conditions, sex causation and employer attribution. A lawful later evidentiary disposition remains available; the mandate guarantees neither trial nor recovery. The transfer comments may be relevant harassment evidence despite their insufficiency to establish a denied transfer. Constructive discharge, damages and the rejected administrative-timeliness defense are not newly decided. No historical Supreme Court vote departure or necessary later-matter predicate displacement is identified.

""",
}
for heading, note in notes.items():
    assert body.count(heading) == 1
    body = body.replace(heading + '\n\n', heading + '\n\n' + note, 1)

header = """# OT2002 chunk 8 group C — partial reconciled commitments

## Scope, boundaries and source receipt

This historical-reconciliation handoff is complete for inventory 101 Bell, 102 Hyatt and 103 Gorski only. It preserves the frozen independent commitments and adds the comparison determinations below. It makes no final Clackamas commitment. Clackamas requires a separately validated neutral factual supplement and fresh affected modeling before its final reconciliation; its independent frozen commitments have not been rewritten.

Authorized inputs were AGENTS.md; Engine sections 3, 7 and 14; the group C frozen neutral packet, preflight receipt and commitments; the group C comparator; and the relevant sections of the group C entering-law slice and public neutral projection. The saved primary Hyatt syllabus and complete Court opinion were read, as were the complete Bell and Gorski issuing-court opinions including footnotes. Clackamas's saved primary syllabus and all writings were read solely for its separate comparison and factual-referral work; they supply no law for these independent same-group events. No private current Stone material, combined brief, raw Decision Record or top-level private directory was accessed. Earlier public positions contained in authorized entering law do not supply the current Stone vote. No author or final nine-Justice coalition is assigned here.

All eight Associates participate on the supplied record. Proper presentation and assigned review dates are settled premises. Bell uses law effective before April 22, 2003; Hyatt before April 23; Gorski before May 27. Stout's May 19 holding is eligible only for Gorski in this group. Same-day processing order creates no law. The cutoffs exclude later historical developments. General knowledge is not claimed erased; the physically withheld current Stone material was not supplied.

The three matters below have no unresolved material source, arrival or approval blocker. The shared rules state actual common grounds; individual limits remain controlling compatibility boundaries for assembly. No historical authorship is imported, and the lower-court comparators create no imaginary Supreme Court voting history.

"""
footer = """## Partial-handoff validation

- Eight named Associates retain each judgment commitment for Bell, Hyatt and Gorski. Bell has two injunction components; Gorski has separate pleading and transfer components. No Stone vote is inferred.
- Each retained component identifies its sufficient ground, qualifications, authorities, alternative route, operative remedy and individual join limits. The copied commitment text is preserved below each added reconciliation determination.
- Bell remains preliminary; Hyatt retains the statute/judgment, comity and constitutional-amenability distinctions; Gorski retains the Rule 12/Rule 56, harassment/transfer and liability/attribution distinctions.
- No controlling ruling, workspace projection, tracker or public output is changed. The partial runtime and freeze files are identical. Final group C reconciliation still requires the separate Clackamas process.

Sources: Women's Medical Center v. Bell, 248 F.3d 411 (5th Cir. 2001), complete issuing-court text at https://www.ca5.uscourts.gov/opinions/pub/00/00-20037.cv0.wpd.pdf; Franchise Tax Board v. Hyatt, 538 U.S. 488 (2003), complete primary writing at https://www.law.cornell.edu/supct/html/02-42.ZO.html and syllabus at https://www.law.cornell.edu/supct/html/02-42.ZS.html; Gorski v. New Hampshire Department of Corrections, 290 F.3d 466 (1st Cir. 2002), complete issuing-court text at https://media.ca1.uscourts.gov/pdf.opinions/01-1995-01A.pdf. Saved full texts were read; no underlying filing not possessed is represented as read. The entering-law slice supplies the current simulated holdings at their actual scope.
"""
result = header + body + footer
for directory in ('runtime', 'freeze'):
    (term / directory / 'OT_2002CHUNK8_C_PARTIAL_RECONCILED.md').write_text(result, encoding='utf-8')
assert (term / 'runtime/OT_2002CHUNK8_C_PARTIAL_RECONCILED.md').read_bytes() == (term / 'freeze/OT_2002CHUNK8_C_PARTIAL_RECONCILED.md').read_bytes()
print('Partial reconciliation saved and identical; Bell, Hyatt and Gorski ready for assembly.')
