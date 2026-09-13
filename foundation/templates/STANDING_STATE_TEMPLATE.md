# SUPREME COURT OF THE UNITED STATES: STANDING STATE

This document is the current institutional, procedural, and limited jurisprudential transition state from which the next simulated Supreme Court event begins. It carries only information that remains live or is necessary to model a sitting Justice consistently. It is not a docket history, case digest, law register, or term recap.

Bracketed text is instruction or placeholder text and does not appear in a completed Standing State.

## 1. Boundary and authority

Standing State contains only:

- the Court currently constituted, including seniority and vacancies;
- current circuit allotments;
- Supreme Court matters and applications that remain open;
- still-operative Supreme Court relief and its ending condition;
- current procedural or institutional dependencies;
- supplied future-effective institutional events whose predicates remain valid; and
- material published noncontrolling positions of sitting Justices that remain relevant to later modeling and are not adequately preserved by current controlling law.

It does not contain closed-case history, routine postjudgment clocks, lower-court remands over which the Supreme Court retains no role, predicted filings or roster changes, private positions, modeled conference material, ideological descriptions, scores, copied Holdings or Standards prose, or superseded state.

The Engine's shared source-precedence, conflict, chronology, same-day, correction, and coordinated term-close rules control preparation of this document. For Standing State specifically:

1. The opening Standing State establishes the preterm institutional and procedural baseline.
2. A validated Canonical Decision Record establishes the simulated effect of its event. Its `stage before and after`, `next nonroutine act or condition`, public-action, and Continuity fields control current stage and next act.
3. The corresponding render verifies the public form but does not supplement a missing state fact.
4. A validated Admitted Source Record may establish an objective nonadjudicative filing or administrative docket fact, roster, oath, vacancy, seniority, allotment, or other expressly supplied institutional event. A Court action requires a Canonical Decision Record.
5. Public sources do not restore a historical event whose predicates were displaced in the alternate timeline.

A source conflict quarantines only the affected state and any later event that depends on it. Genuine procedural uncertainty created by valid sources is carried as uncertainty rather than repaired by inference.

## 2. Publication header

Use:

```text
# SUPREME COURT OF THE UNITED STATES: STANDING STATE

**Opening October Term:** [year]
**Last completed October Term:** [year]
**Processed through:** [Exact common cutoff used by Holdings and Standards and Tests.]
**Edition:** [date]
**State posture:** [Exact point represented, ordinarily the opening of the stated October Term before its first supplied event.]
**Controlled Justice:** Stone, [office and seat]
```

The last completed term, processed-through statement, and edition must match the coordinated Holdings and Standards and Tests publications exactly. The opening term and state posture explain the prospective baseline and do not create a second synchronization cursor.

## 3. Current Court

List every occupied seat once in institutional seniority order.

| Seniority | Justice | Office | Seat | Supreme Court service began | Current office began | Source and effective date |
|---:|---|---|---|---|---|---|
| 1 | [Name] | Chief Justice | [Seat] | [Date] | [Date] | [Natural source] |
| 2 | [Name] | Associate Justice | [Seat] | [Date] | [Date] | [Natural source] |

When applicable, add:

```text
**Institution-wide participation condition:** [Condition, legal effect, effective period, and source.]
```

For each vacancy:

| Vacant seat | Vacant since | Last occupant | Source |
|---|---|---|---|
| [Seat] | [Date] | [Name] | [Natural source] |

Case-specific participation belongs with the affected live matter. A past absence that no longer affects current state is omitted.

## 4. Current circuit allotments

| Circuit | Allotted Justice | Effective date | Source |
|---|---|---|---|
| [Circuit] | [Justice] | [Date] | [Natural source] |

Use the allotment valid at the state posture. Do not import an official historical allotment that depends on a displaced roster. If a missing allotment affects an active application or established next-term event, it is a blocker. Otherwise state the narrow source limitation without inventing a successor.

## 5. Open certiorari, merits, and original matters

Include one entry for each supplied Supreme Court matter that remains procedurally open.

### [Case or matter], [citation or every docket]

**Current stage:** [Exact posture.]

**Operative grant or order:** [Exact order, date, scope, and natural source, when one continues to govern.]

**Question before the Court:** [Exact petition, granted, limited, certified, reargument, or original-action question, when a question remains pending.]

**Last material Supreme Court action:** [Action, date, and source.]

**Next nonroutine act or controlling condition:** [Established act or condition, or a statement that none is presently supplied.]

[**Scheduled event:** [Actually set argument, submission, briefing, return, or other date.]]

[**Court below and judgment:** [Only when needed to identify the live posture.]]

[**Companion or consolidated matters:** [Captions, dockets, and current procedural relationship.]]

[**Participation and quorum:** [Established case-specific limitation and its present consequence.]]

[**Active dependency:** [Related matter or institutional event and its present procedural effect.]]

[**Procedural uncertainty or source limitation:** [Exact unresolved point, source, and what remains authorized or unavailable.]]

**State source:** [Unchanged term-opening Standing State entry, a validated Decision Record with its render used only as a cross-check, or a validated Admitted Source Record identifying the natural procedural source.]

A grant remains open until a dated terminal event. An ordinary rehearing period, transmission period, or lower-court remand does not keep a matter open unless an actual filing, order, retained role, or return channel does so. Preserve argument or submission history only when it affects later participation.

If no matter qualifies, state that no supplied certiorari, merits, or original matter remains open.

## 6. Active applications and in-chambers matters

Include an application or in-chambers matter while it remains pending or while relief issued through it remains operative.

### [Application or matter], [application docket or natural matter identity]

**Underlying matter:** [Case, court, and citation or docket.]

**Filed:** [Date.]

**Current stage:** [Pending before named Justice, referred, renewed, relief in force, or other exact posture.]

**Relief requested:** [Exact relief.]

**Circuit and allotted Justice at filing:** [Circuit, Justice, and effective allotment.]

**Routing and last action:** [Recipient, referral or renewal path, public action, decisionmaker, date, and source.]

**Present effect and ending condition:** [Immediate legal effect and exact expiration, return, or dissolution condition.]

**Next nonroutine act or controlling condition:** [Exact act or condition, or a statement that none is presently supplied.]

[**Participation, uncertainty, or source limitation:** [Only when material to the current posture.]]

**State source:** [Unchanged term-opening Standing State entry, a validated Decision Record with its render used only as a cross-check, or a validated Admitted Source Record identifying the natural procedural source.]

Do not infer a full-Court referral, vote, renewal, or future filing. Keep an independently live underlying Supreme Court docket separate and cross-reference it without merging stages.

Omit this section when nothing qualifies.

## 7. Active dependencies and supplied future institutional events

Include only relationships that presently affect an open matter.

| Open matter | Related matter, order, or institutional event | Present procedural consequence | Ends when | Source |
|---|---|---|---|---|
| [Case or docket] | [Related event] | [Current effect] | [Exact condition] | [Natural source] |

Include a future institutional event only when it has been expressly supplied or validly carried forward, its institutional effect is fixed, and its alternate-timeline predicates remain intact.

| Established future event | Effective date or condition | Institutional effect | Source |
|---|---|---|---|
| [Event] | [Date or condition] | [Effect when effective] | [Natural source] |

Remove a dependency when its condition ends. Apply and remove a future event when it becomes effective. Omit either table when empty.

## 8. Material Published Noncontrolling Positions of Sitting Justices

This section preserves behavioral continuity, not law. Include a position only when all of the following are true:

1. A sitting Justice publicly authored or expressly joined it in a simulated opinion or separate writing.
2. The proposition is noncontrolling, or its materially distinctive content is not fully represented by current controlling law.
3. It supplies a concrete jurisprudential commitment, reservation, or change that could materially affect that Justice's analysis in a later supplied case.
4. The proposition can be stated precisely and traced to its source writing.

Do not include ideology, inferred motive, personality, a private brief, a silent vote, a generic case summary, or every separate opinion. A position is evidence, not a binding prediction. Later law, facts, procedure, argument, or a later public writing may affect its weight.

### Justice [name]

- **[Case], [date], [writing]:** [Exact material proposition and its scope.] **Present status:** [Unchanged, qualified, or displaced by identified later public position or controlling law.]

Combine related propositions from one writing when accuracy permits. Preserve a later qualification with the earlier proposition only when the relationship remains material. Remove the entry when it no longer affects a sitting Justice's future modeling; the archived decision remains the historical source.

If no position qualifies, state that no material noncontrolling simulated position requires carryforward.

## 9. Rollover and validation

At coordinated term close, apply the Engine's Term-Close Dossier and shared update protocol. Carry forward only current roster and allotments, still-operative institution-wide participation conditions, genuinely open matters and applications, active dependencies, not-yet-effective institutional events, narrow unresolved source limitations, and qualifying Section 8 positions. Do not preserve completed stages as history.

Before publication, verify internally:

1. all source events were processed once and in the correct effective-date groups;
2. roster, seniority, vacancies, and allotments are complete and sourced;
3. every retained matter or application is genuinely open and states its exact next act or condition;
4. no ended matter, expired relief, or completed dependency remains;
5. every uncertainty is genuine and every documentary conflict is quarantined under the Engine;
6. every jurisprudential continuity entry is public, source-linked, material, nonbinding, and limited to a sitting Justice;
7. no holding, reusable rule, private position, modeled conference material, forecast, or copied tracker prose entered this document; and
8. the common publication fields match Holdings and Standards and Tests exactly.

Do not print the validation checklist or a claim that validation passed.

## 10. Return rule

Return the complete current Standing State, not a patch, event ledger, term narrative, or update report. Remove bracketed instructions and omitted optional fields. During preparation, quarantine a source defect only to the extent established by the Engine's shared conflict protocol. Because term-close publication is atomic, any unresolved defect that prevents one replacement tracker from validating prevents commitment of the entire new synchronized set; retain the last complete synchronized baseline.
