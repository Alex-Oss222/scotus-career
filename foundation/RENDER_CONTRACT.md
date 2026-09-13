# JUDICIAL TURN OUTPUT RENDER CONTRACT

## 1. Function and input

This Contract converts the Supreme Court Term Simulator Engine's validated event Render Inputs and chunk metadata into a public-facing account of completed events plus any operator-only workflow blocker notice. It presents; it does not adjudicate, research, reconcile, classify, count votes, form coalitions, apply *Marks*, select relief, resolve chronology, repair a Canonical Decision Record, or update a tracker.

The renderer receives these eleven blocks, in this order:

1. **Event**
2. **Participation**
3. **Public Action**
4. **Judgment & Remedy**
5. **Opinion Topology**
6. **Holdings**
7. **Precedent Treatment**
8. **Law After Decision**
9. **Separate Writings**
10. **Procedure After Action**
11. **Source Notes**

| Input block | Public projection |
|---|---|
| Event | Identity, event type, chronology, posture, questions, dockets, dates, and supplied companion or consolidation facts |
| Participation | Participants, nonparticipants, and public bases or disclosure limits |
| Public Action | Exact announced action and publicly disclosed vote or basis |
| Judgment & Remedy | Judgment, components, coalitions, Stone's vote by component, mandate, remedy, transition, and remand |
| Opinion Topology | Writings, authors, joins, partial joins, relationships to judgment components, and Stone's public role and announced ground |
| Holdings | Controlling propositions, authority, application, controlling explanation, limits, reservations, and nonreach |
| Precedent Treatment | Treatment of earlier Supreme Court authority |
| Law After Decision | Effect on current simulated law and supplied public doctrinal context |
| Separate Writings | Material published separate positions, including any material Stone separate writing |
| Procedure After Action | Stage, immediate effect, next act, and controlling condition |
| Source Notes | Verified quotation and citation support, public-source limits, scheduling assumptions, and authorized corrections |

The eleven-block event inputs and validated chunk metadata are the exclusive sources for the public render and blocker notice. Do not require an inapplicable or absent field, create a new substantive field, inspect raw CDR analysis, or use an adaptive audit annex. **Source Notes** may support or qualify another block; it cannot independently create a public fact, holding, rationale, vote, or remedy.

Bracketed text below is instruction and does not print.

## 2. Projection rules

1. Preserve every supplied name, date, docket, citation, question, vote, join, disposition, proposition, limit, transition, and procedural condition exactly in substance. Choose headings, paragraphs, lists, or tables for clarity and use connective phrasing strictly entailed by the supplied fields, but add no legal or factual premise.
2. Keep the main render public. Never expose a commitment matrix, confidence assessment, source audit, comparator, provisional vote, reconciliation, counterfactual branch, conference material, private Stone instruction, or Engine reasoning.
3. Project judgment votes, opinion joins, and proposition coalitions from their own fields. None may be inferred from another.
4. State a proposition as controlling only when **Holdings** supplies both the proposition and its authority. Do not independently perform *Marks*, aggregate noncontrolling writings, or infer authority from citation or outcome.
5. Preserve authorship, partial joins, judgment-only agreement, and each writing's relationship to each judgment component. Never convert a plurality into an Opinion of the Court or a concurrence in the judgment into a join.
6. Project disposition, mandate, remedy, remand, effective transition, stage, and next condition exactly. Do not predict conduct on remand or consequences not supplied.
7. Use quotation marks for decisional language only when **Source Notes** verifies the quotation. Never invent a quotation, pin cite, parallel citation, reason for nonparticipation, or undisclosed vote.
8. Do not invent area-of-law tags, proposition codes, database keys, ideology labels, or doctrinal classifications. Include human-readable doctrinal context only when **Law After Decision** supplies it.
9. Omit an unpopulated optional section. Do not print empty headings, “None,” “N/A,” or stock sentinels.
10. Depth and form are adaptive. A routine event may use a compact conventional narrative; a standard event may use the suggested section form; a fractured, multi-question, transition-sensitive, or procedurally complex event may use the full structured form and tables. Preserve all material distinctions, but use no word, sentence, paragraph, or section-count quota.

If the input lacks or contradicts a fact needed to state the public action, judgment, authority, remedy, or next stage, identify the exact render blocker. Render an unaffected event or portion only when doing so cannot imply a resolution.

## 3. Chunk presentation

For multiple events, use:

```text
# OCTOBER TERM [year], CHUNK [identifier, only if supplied]

## Docket and Chronology

| Effective date | Case or matter | Event | Posture after event |
|---|---|---|---|
| [supplied value] | [supplied value] | [supplied value] | [supplied value] |

## Decisions and Dispositions
```

Render each event once in the effective-date order established by **Event**, preserving supplied same-day grouping or nonsequence. For one event, omit the wrapper unless requested. The table does not replace the event's full posture or post-action stage.

If chunk metadata identifies a stopped matter, add this nonadjudicative section after all completed-event renders, or use it alone when no event was completed:

```text
## Simulation Workflow Blockers

| Case or matter | Exact blocker |
|---|---|
| [metadata identity] | [metadata blocker] |
```

This section is operator-only workflow output, not part of the Court's public action or legal record. State the supplied exact blocker without quoting or summarizing private Stone substance. Do not infer an outcome, vote, law, or procedural effect for a stopped matter. Omit the section when the metadata names none.

## 4. Merits and other precedential decisions

Every merits or other precedential decision must clearly cover chronology and posture, judgment, opinion topology, Stone's public position, controlling propositions and authority, and mandate, remedy, and next stage. These are semantic duties, not a mandatory number of headings.

Choose the least elaborate form that preserves the decision accurately:

- **Routine form:** a conventional narrative under the case heading, with Stone's position and the controlling proposition stated distinctly.
- **Standard form:** the suggested core below, combining adjacent sections when no distinction is lost.
- **Complex form:** the full core, component tables, question-level proposition blocks, and conditional sections needed for mixed judgments, partial joins, fractures, multiple remedies, or transitions.

The standard form is:

```text
### [Case and dockets]

#### Chronology and Posture
[Supplied decisional dates, route to the Court, decision below, questions,
participation, and consolidation or companion facts.]

#### Judgment
[Exact disposition, vote, coalitions, nonparticipants, remedy, and any
effective transition.]

#### Opinion Topology
[Writing table.]

#### Justice Stone's Public Position
[Participation or established nonparticipation; vote by component; public
role; exact join scope; and announced ground or absence of an additional
ground.]

#### Controlling Propositions and Authority
[Separate question, threshold, component, and alternative-holding blocks.]

[Populated conditional public sections from Section 4.6.]

#### Mandate, Remedy, and Stage
[Exact mandate or order, relief, remand, transition, post-action stage, and
next controlling condition.]
```

### 4.1 Chronology and Posture

Use natural Supreme Court phrasing supported by **Event**, such as Argued, Submitted, Reargued, On writ of certiorari to, On appeal from, On certification from, or the supplied original-jurisdiction stage. State accepted questions exactly in substance, including limitations and reformulations. State that a question was not reached only from **Holdings**.

For consolidated matters, identify every docket and docket-specific question or result. Render separately decided companion cases separately, adding a cross-reference only if supplied. Include participation when it differs from the ordinary sitting or affects the vote, authority, or public record.

### 4.2 Judgment

Do not simplify a mixed disposition. Name every supporting and opposing Justice and any supplied nonparticipant. When dockets, claims, components, or remedies have different coalitions, use:

| Judgment component | Disposition and vote | Supporting Justices | Opposing Justices | Remedy or remand |
|---|---|---|---|---|
| [supplied value] | [supplied value] | [supplied value] | [supplied value] | [supplied value] |

Do not reconstruct this table from opinion joins.

### 4.3 Opinion Topology

Use the table when there are multiple writings, partial joins, fractures, judgment-only relationships, or other topology that prose could blur. For a single uncomplicated opinion and any straightforward dissent or concurrence, a precise narrative statement is sufficient. The table form is:

| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| [supplied value] | [supplied value] | [supplied value] | [supplied value] | [supplied value] |

Identify partial joins by supplied sections or issue propositions; invent no section number. The table describes structure, not authority. If **Opinion Topology** says no opinion commands a majority, state that. Project a controlling *Marks* rationale, *Marks* indeterminacy, or no controlling rationale only from **Holdings**.

### 4.4 Justice Stone's Public Position

State Stone's public position distinctly for every merits or other precedential decision, either under this heading or in a clearly identified sentence in the routine form. Use **Participation** for participation or established nonparticipation, **Judgment & Remedy** for Stone's vote by component, **Opinion Topology** for his authorship, public role, exact joins, and announced ground, and **Separate Writings** for any material separate writing. When Stone joins without a separate writing or additional ground, identify the opinion and scope joined and state that he announces no additional ground. When he did not participate, state only that he took no part in the consideration or decision. Never compare the public position with private instructions or describe Stone's influence.

### 4.5 Controlling Propositions and Authority

For multiple questions, threshold paths, distinct authority coalitions, independent alternative holdings, or a fracture, create a block for each supplied component. For one straightforward proposition, state the same proposition, authority, controlling explanation, and material application in conventional prose without duplicating them. The structured block is:

```text
##### [Question or issue]

**Controlling proposition:** [Exact proposition and necessary operative
qualification.]

**Authority:** [Source writing or instrument, supporting Justices at the
same level of generality, and supplied basis of controlling force.]

[**Controlling explanation:** [Only explanation adopted by that coalition.]]

[**Application:** [Only supplied material application.]]
```

If **Holdings** supplies no controlling rationale, do not fabricate a rule. State instead:

```text
**Judgment without controlling rationale:** [Exact result and authority
conclusion.]

[**Independently majority-supported proposition:** [Exact proposition.]]
[**Authority:** [Exact coalition and force.]]
```

For a valid *Marks* rule, project the supplied logical subset, sources, coalition, and limit without new synthesis. Never present a plurality rationale as law merely because it explains the judgment.

### 4.6 Conditional public sections

Include only populated material. Use these headings and order when the distinctions require separate treatment; in a routine form, integrate the same supplied material into the surrounding narrative without changing its source or force.

#### Limits and Questions Not Reached

State supplied reservations, exclusions, unanswered questions, and grounds not reached. Keep a qualification needed to state a proposition accurately with that proposition.

#### Precedent Treatment and Current-Law Effect

Combine **Precedent Treatment** and **Law After Decision** in ordinary legal prose. Identify the affected prior proposition, its resulting present force, and any effective transition. No closed treatment vocabulary applies. Omit this section for an ordinary application with no supplied material change; silence or citation alone is not reaffirmance.

#### Doctrinal Context

Include only public explanatory context supplied by **Law After Decision**. It creates no tag, tracker key, holding, or implication beyond that block.

#### Material Published Separate Positions

State each separate writing marked material in **Separate Writings**, including author, joiners, relationship to judgment, and supplied proposition, limit, or remedial position. Use the depth its content requires. Do not call it controlling unless **Holdings** independently establishes that force for the exact proposition.

### 4.7 Mandate, Remedy, and Stage

Conclude with the exact mandate or operative order, party-specific relief, remand instructions, transition or expiration, post-action stage, and next established act or condition. Do not invent relief for nonparties, convert probable consequences into a command, or predict the result below.

## 5. Public certiorari actions

Keep the public action separate from any optional simulation audit:

```text
### Certiorari: [Case or matter], [citation or docket], [date]

#### Chronology and Posture
[Petition question, decision below, relevant petition posture, participation,
and consolidation.]

#### Public Action
[Exact grant, limited grant, denial, relist, hold, CVSG, or other action;
question granted or limitation; and publicly disclosed vote or basis.]

[#### Material Published Separate Positions]

#### Mandate, Remedy, and Stage
[Effect, stage, and supplied next act, carry condition, or release condition.]
```

Do not print modeled certiorari votes, conference positions, or merits predictions here. Denial creates no merits holding. Project the validated result without independently testing the Rule of Four.

## 6. Other procedural and summary actions

For a DIG, GVR, equal division, summary disposition, reargument or rehearing order, stay, application, in-chambers action, or comparable event, use:

```text
### [Action]: [Case or matter], [citation or docket], [date]

#### Chronology and Posture
[Decisionmaker, prior stage, participation, referral or renewal path, and
other supplied posture.]

#### Public Action
[Exact action, publicly stated basis or disclosure limit, and public vote.]

[#### Controlling Propositions and Authority]
[#### Limits and Questions Not Reached]
[#### Precedent Treatment and Current-Law Effect]
[#### Material Published Separate Positions]

#### Mandate, Remedy, and Stage
[Consequence below, relief, expiration or return condition, stage, and next
controlling condition.]
```

Include controlling propositions only when **Holdings** supplies them. Never infer Court law from an unexplained order, disclosed vote, single-Justice action, or separate writing.

## 7. Optional Simulation Audit Appendix

The ordinary renderer never receives the CDR's adaptive audit annex. Include an appendix only when the user separately requests it and the Engine supplies a distinct validated **Public Audit Projection** authorized for disclosure. This exceptional input is not a twelfth Render Input block.

Place the appendix after the complete public render and label it **Simulation Audit Appendix**. State that it is nonpublic simulation metadata, not part of the Court's action and not legal authority. Display only fields in the Public Audit Projection. Any modeled certiorari table must label positions nonpublic and reproduce its validated tally and result exactly. Never interleave audit material with a public event or allow it to supply a tracker with law or public procedure.

## 8. Projection check

Before return, verify that:

1. every event appears once in supplied effective order;
2. chronology, posture, participation, public action, judgment components, coalitions, opinions, partial joins, and Stone's public vote, role, join scope, and announced ground match their designated blocks;
3. every controlling proposition, authority statement, and *Marks* result reproduces **Holdings** without synthesis;
4. limits, nonreach, precedent treatment, current-law effect, separate positions, mandate, remedy, transition, and next stage use only their designated blocks;
5. no public/private boundary, quotation rule, no-invented-tag rule, or optional-section rule was violated; and
6. every stopped matter and blocker in chunk metadata appears once without an implied adjudication; and
7. compression lost no material distinction and elaboration added no fact or conclusion.

Return no certification on success. If the Render Input fails a projection check, state the exact blocker and do not adjudicate it.
