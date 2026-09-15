# SUPREME COURT OF THE UNITED STATES: STANDING STATE

This document is the Court's setting at the opening of an October Term: who sits and in what seniority, which Justice holds each circuit, the standing practices the Court has adopted, and the cases brought up to the docket beyond the term's inventory. It is not a docket history, case digest, law register, or term recap, and it carries no positions, dependencies, or narrative of past events.

Bracketed text is instruction or placeholder text and does not appear in a completed Standing State.

## 1. Boundary and authority

Standing State contains only:

- the Court currently constituted, including seniority, vacancies, and oath dates that limit participation;
- current circuit allotments;
- standing institutional practices the Court has adopted, with their effective dates; and
- the docket of cases brought up: the user's lower-court additions, and any matter the Court itself left open at the end of the prior term, one line each.

It does not contain closed-case history, procedural narratives of open matters, tracking of operative relief, dependency tables, future institutional events, noncontrolling positions of Justices, private positions, modeled conference material, ideological descriptions, scores, or copied Holdings or Standards prose. Future roster and allotment changes live in the Supreme Court Composition register and enter this document only when effective. A Justice's simulated positions from earlier terms are consulted from those terms' public renders, not recorded here.

Sources, in order:

1. The Supreme Court Composition register controls roster, seniority, oath dates, and the allotment order in force.
2. A validated Admitted Source Record establishes a roster, oath, vacancy, seniority, or allotment change effective during a term.
3. The user's instruction places a lower-court case on the docket; the final Term Workspace identifies any matter the Court itself left open.
4. A validated Canonical Decision Record establishes the stage of a matter the Court left open; the render is a cross-check only.

Public sources do not restore a historical event whose predicates were displaced in the alternate timeline. A source conflict about roster, allotment, or a docket line is stated as a conflict, not repaired by inference.

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

For each vacancy:

| Vacant seat | Vacant since | Last occupant | Successor and oath date, if fixed | Source |
|---|---|---|---|---|
| [Seat] | [Date] | [Name] | [Name and date, or none fixed] | [Natural source] |

When applicable, add:

```text
**Participation condition:** [A Justice seated after the term opens participates only in matters argued or submitted on or after the oath date unless reargued; quorum; source.]
```

State the opinion-assignment seniority in force: the Chief assigns when in the judgment majority; otherwise assignment passes through the participating Associates in seniority order. A past absence that no longer affects the current roster is omitted.

## 4. Current circuit allotments

| Circuit | Allotted Justice | Effective date | Source |
|---|---|---|---|
| [Circuit] | [Justice] | [Date] | [Natural source] |

Use the allotment order in force at the state posture, from the Composition register. Do not import an official historical allotment that depends on a displaced roster. State the allotment rule: a membership change triggers a complete reallotment; no Justice inherits a predecessor's circuits.

### Standing practices

Record each standing institutional practice the Court has adopted, one paragraph each, with its effective date and source — for example, the referral of applications on the Term's inventory to the full Court. A practice remains until the user or a Court order changes it.

## 5. Docket of cases brought up

One line per case. The case's substance lives in its brief; this table records only that it is on the docket and why.

| Case or matter | Court below and judgment | Why on the docket | Stage at opening | Source |
|---|---|---|---|---|
| [Caption; citation or docket] | [Court; disposition] | [User addition with the fourth vote / carried over from OT____ (matter the Court left open) / other supplied basis] | [Exact stage: e.g., certiorari granted, awaiting briefing; original action, injunction issued, jurisdiction retained for implementation] | [User instruction; Decision Record; Admitted Source Record] |

A carried-over matter states its stage and nothing more; its Decision Record holds the procedural detail. If no case qualifies, state that no case is brought up beyond the term's inventory.

## 6. Rollover and validation

At coordinated term close, produce the next-term Standing State by:

1. setting the roster, seniority, vacancies, and oath dates to the next term's opening under the Composition register, applying any Admitted Source Record effective during the closing term;
2. setting the allotments to the order in force at that opening;
3. carrying the standing practices forward unchanged unless changed by the user or a Court order;
4. rebuilding the docket list: the user's additions for the next term, plus every matter the closing term's final Term Workspace identifies as left open by the Court, one line each.

Before publication, verify internally:

1. every occupied seat appears once, with seniority, dates, and source;
2. every circuit has an allotted Justice valid at the state posture;
3. every open matter identified by the final workspace appears in the docket list, and nothing ended remains;
4. nothing outside Section 1 entered this document; and
5. the common publication fields match Holdings and Standards and Tests exactly.

Do not print the validation checklist or a claim that validation passed.

## 7. Return rule

Return the complete current Standing State, not a patch, event ledger, term narrative, or update report. Remove bracketed instructions and omitted optional fields. Because term-close publication is atomic, any unresolved defect that prevents one replacement tracker from validating prevents commitment of the entire new synchronized set; retain the last complete synchronized baseline.
