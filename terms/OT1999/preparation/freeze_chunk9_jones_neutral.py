from pathlib import Path
import hashlib

root = Path(__file__).resolve().parents[3]
term = root / 'terms' / 'OT1999'
paths = {
    'runtime': term / 'runtime' / 'OT_1999CHUNK9_NEUTRAL.md',
    'facts': term / 'preparation' / 'OT_1999CHUNK9_JONES_CONTROL_FACTS.md',
    'law': term / 'entering-law' / 'OT_1999CHUNK9_JONES.md',
    'projection': term / 'workspace' / 'neutral-projection.md',
}
texts = {key: path.read_text(encoding='utf-8-sig') for key, path in paths.items()}
projection = texts['projection']
start = projection.index('### Reform Party of Allegheny County v. Allegheny County Department of Elections — 2000-04-10')
end = projection.index('\n### ', start + 4)
reform = projection[start:end].rstrip()
facts = texts['facts'][texts['facts'].index('## Event and exact judgment below'):].rstrip()
opening = projection[:projection.index('## Completed public events and admitted sources')].rstrip()
packet = '''# Frozen neutral packet — California Democratic Party v. Jones

Fresh neutral validation completed November 3, 2026. This packet supplies no vote, commitment, target historical Supreme Court result or Stone position. It supersedes the generic and stale framing of this case's runtime Section I for independent modeling; the approved runtime source remains unchanged. Sources are copied below without retyping their substantive passages.

## Event, scope and participation

No. 99-401; merits review of the Ninth Circuit on June 26, 2000, following April 24, 2000 argument. The question is whether California may compel political parties to select their official nominees through the described blanket primary. The nine seated Justices are Chief Justice Stone-Zsela and Justices Stevens, O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg and Breyer. No case-specific nonparticipation is identified in the authorized materials. Independent modeling addresses only the eight Associates.

The opening law is the OT1998-close set, supplemented by effective current-term law. The chronology cursor is June 26, 2000. Uncoordinated June 26 decisions share entering law and do not govern one another. No supplied dependency makes this case a coordinated sequel. The current projection records no institutional change.

## Fresh framing and completeness determinations

The State's law selects an official nominee for each party; party-committee voting remains limited to that party's registrants. The surviving private party functions, electoral access interests and empirical findings must all be considered without turning the lower court's constitutional characterization of the burden into an established fact. Outsider influence, sincere crossover voting, strategic voting and organized raiding are distinct. Popular support is not party consent. The four parties' opposing bylaws are part of the record. The packet preserves the qualified predictive nature of crossover and participation evidence and does not invent California totals.

Both the parties' claim of compelled control over a standard bearer and the State's claim of authority over a public nominating process receive substantive treatment in the copied source extraction. A decision may sustain the law on actual burden and proportionate interests, apply strict scrutiny to a severe burden, or find inadequate fit even without declaring the burden severe. Neither the classification nor the outcome is predetermined. Party-authorized participation, a conventional open primary, nonpartisan candidate winnowing and an official party nomination are separate arrangements; this case need not adjudicate them all.

The focused entering-law slice requires one addition: Reform Party of Allegheny County, decided April 10, 2000. Its exact sanitized public projection is copied below. Its common rule concerns unequal access to a timely pre-primary cross-nomination opportunity, not a free-standing right to every nomination mechanism. Its explanation that endorsement does not replace the legal nomination opportunity is relevant to the parties' claimed burden here, while its equality premise, timing and confined relief limit the analogy. It neither predetermines Jones nor changes Anderson–Burdick scrutiny. Any source-map statement that no relevant current-term nomination decision exists is superseded by this explicit addition.

The controlling law and source extraction preserve statutory party-committee limits; state and congressional scope; the changed presidential reporting issue; absence of a granted Elections Clause initiative question; and the difference between prospective relief, reopening completed elections and judicial creation of a new ballot system. No damages award, automatic redesign, or adjudication of unpresented presidential-delegate rules is supported.

## Source limitations and model readiness

Ready for independent modeling of the bounded question described above. No material fact gap remains for that question on the supported lower-court recitations and qualified factual account. This is not certification that every page of the underlying archive or joint appendix has been reviewed. An exact transcript concession, additional empirical number, amicus position, independent Elections Clause claim, or application of later presidential reporting amendments would require a targeted sanitized source check before it could perform decisional work. Those matters are not supplied as facts or preserved claims. Missing research is not litigant default.

The event's legal cutoff is June 26, 2000; historical source facts are limited to the date-eligible record and permitted scheduling material. The lower-court findings and arguments are historical support, while the alternative decisional paths are analytical possibilities under entering law. No reconstruction premise beyond the supplied scheduling placement is adopted. The separate model must perform the Engine's Justice-specific alternative-path analysis and preserve the full distinction between public prior positions and binding holdings.

## Validated objective source extraction

'''
packet += facts + '\n\n## Exact focused entering-law copy\n\n' + texts['law'].rstrip()
packet += '\n\n## Exact current-term institutional and chronology extract\n\n' + opening
packet += '\n\n## Exact additional effective current-term law\n\n' + reform + '\n'
out = term / 'freeze' / 'OT_1999CHUNK9_JONES_NEUTRAL.md'
out.parent.mkdir(parents=True, exist_ok=True)
if out.exists():
    raise RuntimeError('Refusing to replace an existing freeze')
out.write_text(packet, encoding='utf-8', newline='\n')
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
receipt = '''# Jones — fresh neutral validation receipt

Status: READY for a fresh independent non-Stone modeling context on the bounded compulsory-blanket-primary question. No commitments were produced in this validation context.

## Authorized sources actually read

- `AGENTS.md`: governing source boundaries, completeness, chronology and neutral-stage rules.
- `foundation/ENGINE.md`: governing rules, particularly §§1–3, 5–6 and 14.
- `runtime/OT_1999CHUNK9_NEUTRAL.md`: all eight Section I packets for intake completeness; only the Jones section supplies this freeze's event input.
- `preparation/OT_1999CHUNK9_JONES_CONTROL_FACTS.md`: sanitized objective facts, lower-court reasoning, competing arguments, source and scope limits.
- `entering-law/OT_1999CHUNK9_JONES.md`: focused current-law and prior public-position handoff.
- `workspace/neutral-projection.md`: opening institutional/chronology paragraphs, text searches for election/nomination authorities, and the complete Reform Party of Allegheny County public section. A broad initial heading/name search returned additional already-public projection excerpts; no raw Records or private material was opened.

No target Supreme Court opinion, target comparator, Stone supplement, raw Record, control exposure receipt, private Stone material, or excluded source was read. No Git command was run. No external research was performed in this fresh validation context. Source provenance is accepted only within the sanitized handoff's expressly stated scope, not enlarged into a claim to have inspected unrecovered or unread originals.

## Independent findings and corrections

1. The approved Section I's generic State argument, generic remedy paths and stale baseline are insufficient alone; the sanitized extraction supplies the trial findings, actual lower judgment, State interests, procedural scope and material limits.
2. The focused entering-law handoff omitted the effective April 10, 2000 Reform Party decision. The validator found it in the sanitized projection and mechanically copied its complete public section into the freeze. The packet explains both its relevance and its equality/timing limits without predicting a result.
3. The freeze separates constitutional characterizations from underlying findings; predictions from actual California counts; sincere/strategic crossover from organized raiding; popular support from party consent; and party-committee selection from official nominee selection.
4. All-eight-Associate date-eligible source grounding is available through the actual Timmons and Hurley joins, with the Timmons public dissents and surviving pre-divergence sources identified. Those positions are evidence for modeling, not commitments in this case.
5. The packet preserves lawful competing paths and remedy limits. The code copies exact saved source text; no long source passage was manually retyped.

## Exact gaps and consequences

- Full joint-appendix and transcript review is not certified. An exact concession, new empirical statistic or additional preserved factual contention cannot be used without targeted source verification. The framed question does not require such an assertion.
- The scope and operation of amended presidential reporting rules are not fully established for a separate merits decision. National-delegate treatment remains outside this packet's adjudicable question.
- No independent Elections Clause initiative claim or omitted amicus ground is established as granted/preserved. Do not decide or attribute it without a new sanitized source showing.
- No additional same-term nomination authority was found in the scoped search beyond Reform Party. Ordinary chronology freshness must be checked if intervening effective sources are added before modeling.

These are bounded source and scope limits, not a blocker to the supported state/congressional compulsory-nomination issue. A later decision to rely on one of the unsupplied propositions creates a targeted research condition; it cannot be inferred away.

## Snapshot integrity

'''
for key, path in paths.items():
    receipt += f'- `{path.relative_to(term).as_posix()}`: SHA-256 `{digest(path)}`.\n'
receipt += f'- `freeze/{out.name}`: SHA-256 `{digest(out)}`.\n'
receipt += '\nThe frozen packet is a durable neutral handoff, not a Court action or a revision of any completed adjudication. It contains no opinion assignment or modeled vote.\n'
rec = term / 'freeze' / 'OT_1999CHUNK9_JONES_NEUTRAL_VALIDATION.md'
if rec.exists():
    raise RuntimeError('Refusing to replace an existing validation receipt')
rec.write_text(receipt, encoding='utf-8', newline='\n')
assert facts in out.read_text(encoding='utf-8')
assert texts['law'].rstrip() in out.read_text(encoding='utf-8')
assert reform in out.read_text(encoding='utf-8')
print(f'Created {out.relative_to(root)} ({len(packet)} characters)')
print(f'Created {rec.relative_to(root)}')
print('Exact saved facts, focused law and Reform Party projection copies verified.')
