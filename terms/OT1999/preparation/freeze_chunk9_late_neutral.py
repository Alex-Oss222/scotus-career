from pathlib import Path
import hashlib
import sys

term=Path(__file__).resolve().parents[1]
case=sys.argv[1].upper()
front={
'HILL': '''The challenge concerns Colorado section 18-9-122(3), considered June 28, 2000 after January 19 argument, on review of the Colorado Supreme Court. It is a facial preenforcement challenge seeking declaratory and injunctive relief, not review of a conviction or an injunction aimed only at particular wrongdoers.

The statute's precise trigger is a knowing speaker-initiated approach within eight feet without the approached person's consent, for the listed leaflet, sign or oral communicative purposes, on a public way or sidewalk within one hundred feet of an entrance door to a lawfully authorized health-care facility. Colorado's binding no-retreat construction matters: a stationary speaker need not leave because another person approaches. A knowledge element does not itself decide all clarity or overbreadth objections, and consent limits approach rather than every word, sign or presence in the area. Subsection (2)'s obstruction offense, (5)'s local-law permission and (6)'s civil-liability cross-reference are separate. Nothing here adjudicates every civil remedy or local law.

The State's actual access and treatment interests and petitioners' actual peaceful initiation, leafleting and conversational burdens receive substantive consideration. Legislative testimony about misconduct is not proof that these petitioners committed it. The state court's characterization of adequate alternative communication remains reviewable constitutional reasoning, not a conclusive empirical finding. A benign objective does not settle content classification, and a communicative-purpose category does not mechanically resolve the analysis without examining operation and justification.

Madsen and Schenck preserve the protection of initial peaceful contact and distinct scrutiny of moving restraints, but apply a heightened injunction test and specific remedial records. They do not establish a universal forbidden distance or automatically invalidate generally applicable legislation. Ward supplies the neutral legislative route. The model must separately consider classification, the appropriate scrutiny, actual fit/channels, vagueness and overbreadth and match relief to the adopted ground. A valid no-retreat reading cannot be replaced by a hypothetical duty to flee; neither can statutory knowledge be treated as an answer to every protected-activity burden.

The lower opinion's account of a neutrality concession and the complaint's content-discrimination allegation are both preserved. The state court passed on neutrality. No new waiver is inferred without a source showing its actual scope and the ordinary treatment of an issue decided below. If forfeiture itself would determine the result, current petition/briefing verification is required. The merits alternatives may be considered without inventing a forfeiture. A ruling must retain ordinary remedies and the independent subsection boundaries; no substitute distance, damages or conviction disposition is assumed.

Ready for independent modeling at this bounded scope. Exact current preservation, any unreported enforcement construction and actual elements of an unpresented civil claim remain targeted source conditions only if relied on. No other missing material blocks the identified facial merits paths. All eight Associates have their own prior writings/joins in the copied Madsen/Schenck history, with Breyer's clarification-before-invalidation position and Stevens's distinct equity analysis preserved. Prior public views are not present votes.''',
'MITCHELL': '''The question concerns the federal Chapter 2 equipment/materials program, considered June 28, 2000 after December 1, 1999 argument, on review of the Fifth Circuit. The lower Part III disposition is categorical as to equipment and library-book loans to sectarian schools in Jefferson Parish; it is not merely a quantified judgment about a proved devotional item. Textbooks and the separate programs within the larger litigation retain their actual scope. The federal grant does not automatically bring every Louisiana program or unrelated docket before the Court.

The exact approved operational premise is copied unchanged below. It establishes actual financed religious instruction or demonstrated religious use under recipient control for this application. It is not inferred from religious identity, classroom control, fungibility or savings; it is not a recovered historical finding, and supplies no specific school, number, incident, nationwide prevalence or chosen remedy. A model may not reduce it to a mere hypothetical risk or enlarge it to all materials at all schools. Its constitutional significance, proper application and remedy remain for independent adjudication.

Public title, public administration, secular/neutral/nonideological services, independent providers and supplement-not-supplant requirements are statutory commands. The described classroom control, actual monitoring practices, recalled titles and assurances are separate facts or judicial recitations. Neither nominal public title nor neutral eligibility conclusively establishes lawful use. Conversely, a religious provider and a possible institutional saving alone cannot establish a forbidden financed function under the current law.

Agostini's unified Lemon inquiry and the actual Jackson and Strout funded-function holdings govern. The independent old Lemon prongs do not return. The exact relationship and controls in Rosenberger, Southworth and safeguarded secular instruction retain their lawful protection; a label of private expression does not alone resolve what this expenditure buys. The Court must address both the categorical premise below and the adopted actual-use premise. Rejecting a categorical equipment rule does not approve every administered use, while identifying a genuine defect does not justify exclusion of every religious provider or independently lawful loan.

Competing paths include confined invalidity/remedial correction under the actual funded-function rule, or a narrower disposition correcting the categorical lower rationale while preserving adjudication of the established financed-use application. A departure from binding doctrine requires the ordinary precedent analysis rather than recharacterizing the adopted fact. No route is selected. Relief must explain treatment of the actual lower declaration, any genuinely dependent state provision and lawful severable applications. No new administrative audit system, school closure, across-the-board exclusion, recoupment or damages is presumed.

Ready for independent modeling. Source-specific quantity, particular financed activities beyond the premise, exact reach of a distinct state program and the final remedial implementation are not supplied by inference. If one becomes essential to a proposed broader remedy, obtain that source or confine the holding/remand to established scope. No nonexistent simulated filing is required to re-prove the approved premise. The copied prior public writings preserve the different Agostini, Jackson and Strout grounds of each Associate, including Breyer's limited Agostini joins; they do not generate a present commitment.'''
}
names={'HILL':'Hill v. Colorado','MITCHELL':'Mitchell v. Helms'}
if case not in front: raise SystemExit('Unsupported not-yet-validated case')
facts_path=term/'preparation'/'OT_1999CHUNK9_LATE_CONTROL_FACTS.md'
extracts_path=term/'preparation'/'OT_1999CHUNK9_LATE_SOURCE_EXTRACTS.md'
law_path=term/'entering-law'/f'OT_1999CHUNK9_{case}.md'
facts_all=facts_path.read_text(encoding='utf-8-sig')
extracts_all=extracts_path.read_text(encoding='utf-8-sig')
def section(text,heading):
    start=text.index(heading)
    end=text.find('\n## ',start+4)
    return text[start:end if end!=-1 else len(text)].rstrip()
facts=section(facts_all,'## '+names[case]+' -')
extracts=[]
for part in extracts_all.split('\n## ')[1:]:
    if part.startswith(case.title()+' -'):
        extracts.append('## '+part.rstrip())
law=law_path.read_text(encoding='utf-8-sig').rstrip()
intro=f'''# Frozen neutral packet — {names[case]}

Fresh neutral validation completed November 3, 2026. This packet supplies no modeled vote, assignment, Stone position or target historical Supreme Court outcome. It corrects the generic/stale framing of the approved runtime Section I without changing that input. Exact saved substantive handoffs follow.

The nine seated Justices are Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No case-specific nonparticipation is identified. Independent modeling concerns the eight Associates. The law cutoff is immediately before June 28, 2000. The four uncoordinated June 28 cases share entering law and do not govern one another. No unfinished June 26 position is law. If a completed earlier event adds materially relevant law before modeling, provide a sanitized update; the specifically identified Jones/Dale dependency does not predetermine another case.

## Independent framing, qualifications and readiness

{front[case]}

## Validated objective source extraction

'''
packet=intro+facts+'\n\n## Exact case-specific source terms\n\n'+'\n\n'.join(extracts)+'\n\n## Exact focused entering-law handoff\n\n'+law+'\n'
out=term/'freeze'/f'OT_1999CHUNK9_{case}_NEUTRAL.md'
rec=term/'freeze'/f'OT_1999CHUNK9_{case}_NEUTRAL_VALIDATION.md'
if out.exists() or rec.exists(): raise RuntimeError('Refusing to replace frozen packet')
out.write_text(packet,encoding='utf-8',newline='\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt=f'''# {names[case]} — fresh neutral validation receipt

Status: READY for independent non-Stone modeling at the bounded scope and source conditions stated in the packet. No modeled votes or assignments produced.

Authorized sources used: AGENTS.md; governing neutral Engine rules; this case's Section I in `runtime/OT_1999CHUNK9_NEUTRAL.md`; case-specific portions of the shared late control-facts and source-extract files; the focused law handoff below; relevant current neutral-projection chronology and public-law material already contained in the scoped handoffs. The continuing neutral context has read other current-chunk neutral handoffs but no target comparator, current Stone supplement, commitment, raw Record or target historical Supreme Court source.

The validator independently checked framing, record characterizations, both sides' strongest supported paths, alternative lower grounds, statutory qualifications, controlling versus noncontrolling law, chronology and remedy limits. The packet's independent assessment states the exact remaining conditional source needs. There is no certification of exhaustive reading of the raw case archive; source-extractor claims are preserved without expanding them into a personal reading claim. Source absence establishes no litigant default, waiver or failure of proof.

Case-specific facts, terms and law are mechanically copied from saved handoffs. No long source text is manually retyped. Only a target-dependent source gap used by a proposed ground requires further verification; the packet neither invents the missing fact nor stops all supported alternatives. Earlier effective law must receive the ordinary final freshness check before modeling.

Snapshot integrity:

'''
for p in [facts_path,extracts_path,law_path,out]: receipt+=f'- `{p.relative_to(term).as_posix()}`: SHA-256 `{sha(p)}`.\n'
rec.write_text(receipt,encoding='utf-8',newline='\n')
assert facts in packet and law in packet and all(e in packet for e in extracts)
if case=='MITCHELL':
    runtime=(term/'runtime'/'OT_1999CHUNK9_NEUTRAL.md').read_text(encoding='utf-8-sig')
    premise=next(line for line in runtime.splitlines() if line.startswith('* **Simulation Premise'))
    assert premise in packet
print(f'{case}: neutral freeze/receipt created; exact case extracts and law verified.')
