# JUDICIAL TURN OUTPUT RENDER CONTRACT

## 1. Function and input

This Contract converts the Supreme Court Term Simulator Engine's validated generated event Render Inputs and chunk metadata into a concise, substantive public account of what the Court decided, why, who joined which propositions, the selected separate positions, and the resulting law. It does not commission full-length opinions or imitation of individual Justices' styles. The renderer receives the generated handoff only; it never opens the Canonical Decision Record, freeze artifacts, briefs, or source files. Center what the Court decided, its controlling rule and rationale, the rule's authority and limits, treatment of prior law, and the remedy or procedural effect. Keep each case entry unmistakably bounded while allowing its interior form to follow the decision's complexity. The renderer presents; it does not adjudicate, research, reconcile, classify, count votes, form coalitions, apply *Marks*, select relief, resolve chronology, repair a Canonical Decision Record, or update a tracker.

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
| Judgment & Remedy | Judgment, components, coalitions, votes by component, mandate, remedy, transition, and remand |
| Opinion Topology | Writings, authors, joins, partial joins, and relationships to judgment components |
| Holdings | Controlling propositions, authority, application, controlling explanation, limits, reservations, and nonreach |
| Precedent Treatment | Treatment of earlier Supreme Court authority |
| Law After Decision | Effect on current simulated law and supplied public doctrinal context |
| Separate Writings | Published separate positions selected by the Engine to explain the Court's authority, law, judgment, remedy, or public procedural basis |
| Procedure After Action | Stage, immediate effect, next act, and controlling condition |
| Source Notes | Verified quotation and citation support, public-source limits, and legally relevant scheduling assumptions. Never include approval history, correction lineage, modern research dates, model/tool names, or operator workflow. |

The eleven-block event inputs and validated chunk metadata are the exclusive sources for the public render. Do not require an inapplicable or absent field, create a new substantive field, inspect raw CDR analysis, or use an adaptive audit annex. **Source Notes** may support or qualify another block; it cannot independently create a public fact, holding, rationale, vote, or remedy.

The Engine selects separate-position explanations under its Render Input rules before handoff. Positions retained solely for future simulation continuity are outside the ordinary public projection. Do not independently select a different set of positions, reconstruct omitted theories, or treat their absence from the render as absence from the simulated public record. Report Stone under the same standards as every other Justice, without a dedicated section or repeated personal account.

Bracketed text below is instruction and does not print.

## 2. Projection rules

1. Preserve every supplied name, date, docket, citation, question, vote, join, disposition, proposition, limit, transition, and procedural condition in the selected public projection exactly in substance. State overlapping information once when that preserves every material distinction. Choose headings, paragraphs, lists, or tables for clarity and use connective phrasing strictly entailed by the supplied fields, but add no legal or factual premise.
2. Keep the main render public. Never expose a commitment matrix, confidence assessment, source audit, comparator, provisional vote, reconciliation, counterfactual branch, conference material, private Stone instruction, or Engine reasoning. Fidelity to the handoff does not require reproducing forbidden workflow material embedded in a legacy input. Omit claims about whether an operator inspected, extracted, verified, or certified sources and statements that no verified quotation was used. Preserve any underlying legally material uncertainty as a limitation of the evidence or record in ordinary legal prose; do not turn a source gap into an established fact or omit it merely to remove workflow wording.
3. Project judgment votes, opinion joins, and proposition coalitions from their own fields. None may be inferred from another.
4. State a proposition as controlling only when **Holdings** supplies both the proposition and its authority. Do not independently perform *Marks*, aggregate noncontrolling writings, or infer authority from citation or outcome.
5. Preserve authorship, partial joins, judgment-only agreement, and each writing's relationship to each judgment component. Never convert a plurality into an Opinion of the Court or a concurrence in the judgment into a join.
6. Project disposition, mandate, remedy, remand, effective transition, stage, and next condition exactly. Do not predict conduct on remand or consequences not supplied.
7. Use quotation marks for decisional language only when **Source Notes** verifies the quotation. Never invent a quotation, pin cite, parallel citation, reason for nonparticipation, or undisclosed vote.
8. Do not invent area-of-law tags, proposition codes, database keys, ideology labels, or doctrinal classifications. Include human-readable doctrinal context only when **Law After Decision** supplies it.
9. Omit an unpopulated optional section. Do not print empty headings, “None,” “N/A,” or stock sentinels for missing material. The entry boundaries required by Section 3 always print.
10. Depth and interior form are adaptive within the fixed entry boundaries in Section 3 and these upper limits: each ordinary controlling explanation is at most **200 words**; each user-designated extended controlling explanation is at most **750 words**; and each published separate-writing summary in a user-designated special-consideration matter is at most **500 words**. An express case-specific user instruction may set a different limit. These are ceilings for the explanation or summary body, whether labeled or integrated into prose, not minimums, targets, or a cap on the whole case entry. Use fewer words when the supplied reasoning can be stated completely in less space. Preserve the holding, authority, material reasoning and application, qualifications, and remedy; shorten repetition before substance. Do not divide one explanation or relocate its reasoning merely to evade a ceiling. If faithful condensation within the applicable limit is impossible, name the exact conflicting requirements as an operator-facing render blocker for upstream repair; do not silently exceed the limit, omit a material distinction, or invent a replacement rationale.

The upstream operator passes any applicable designated or case-specific ceiling as a private presentation instruction with the existing Render task, identifying only the affected case, holding or writing and the numeric limit. The renderer may read that instruction for length only; it supplies no substance, never prints, and is not an additional event-input block. Do not infer a designation from importance, complexity, vote margin, or a legacy "full" form. When no exception applies, use the ordinary ceiling; the user need not repeat an existing designation.

This Contract governs presentation. Vote margin alone does not require a longer form or a table. Historical differences do not determine public form and must not be supplied to or reconstructed by the renderer. A legacy "Render form" note is nonprinting editorial metadata; it does not override this Contract or authorize historical comparison. Use the existing entry structure, with compact treatment where sufficient and additional structure where the actual judgment, joins, law, or remedy requires it.

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

Every event entry, including a single event without the chunk wrapper, begins with a level-three case or matter heading and a separate event-and-date line. End the entry with a bold closing line repeating the displayed case or matter name, event, and date, followed by a horizontal divider. Use this boundary form for every merits, certiorari, procedural, and summary entry:

```text
### [Case or matter], [docket or dockets when supplied]

[Event or action], [effective date]

[The event's account, with adaptive prose, headings, or tables.]

**End of entry: [Case or matter], [event or action], [effective date].**

---
```

Use level-four or deeper headings inside an entry; reserve level-three headings in the decisions section for new case or matter entries. Keep all event-specific prose, tables, citations, and procedural conditions above its closing line. The closing line ends the displayed account only. It does not declare the case closed, terminate proceedings, or alter the stage supplied by **Procedure After Action**. A later action in the same case receives its own bounded entry in its supplied chronological position. A supplied consolidated event may share one entry with all affected dockets identified; separately decided companions remain separate entries. The closing line and divider follow the final substantive paragraph even in the shortest routine form.

If chunk metadata identifies a stopped matter, add this nonadjudicative section after all completed-event renders, or use it alone when no event was completed:

```text
## Workflow Blockers

| Case or matter | Exact blocker |
|---|---|
| [metadata identity] | [metadata blocker] |
```

This section is operator-only workflow output, not part of the Court's public action or legal record. State the supplied exact blocker without quoting or summarizing private Stone substance. Do not infer an outcome, vote, law, or procedural effect for a stopped matter. Omit the section when the metadata names none.

## 4. Merits and other precedential decisions

Every merits or other precedential decision must clearly cover chronology and posture, judgment, opinion topology, controlling propositions and authority, and mandate, remedy, and next stage. Individual positions appear through the ordinary judgment, authorship, join, and selected separate-position accounts. These are semantic duties, not a mandatory number of internal headings.

Choose the least elaborate form that preserves the decision accurately:

- **Routine form:** a visible Judgment block followed by a conventional narrative within the entry boundaries, stating the controlling proposition, authority, and material procedural effect without repetitive personal accounts.
- **Standard form:** the suggested core below, combining adjacent sections when no distinction is lost.
- **Complex form:** the full core, component tables, question-level proposition blocks, and conditional sections needed for mixed judgments, partial joins, fractures, multiple remedies, or transitions.

Keep a visible **Judgment** heading after the brief chronology and posture and before the opinion and reasoning account in every merits form. The remaining standard sections are a suggested interior arrangement. Combine or reorder them when clarity improves and no material distinction is lost; retain the entry boundaries in every form:

```text
### [Case or matter], [docket or dockets when supplied]

[Event or action], [effective date]

#### Chronology and Posture
[Supplied decisional dates, route to the Court, decision below, questions,
participation, and consolidation or companion facts.]

#### Judgment
[Single-disposition block or component table from Section 4.2; preserve
the exact remedy and any effective transition.]

#### Opinion Topology
[Precise authorship-and-joins account or writing table from Section 4.3.]

#### Controlling Propositions and Authority
[Separate question, threshold, component, and alternative-holding blocks.]

[Populated conditional public sections from Section 4.6.]

#### Mandate, Remedy, and Stage
[Exact mandate or order, relief, remand, transition, post-action stage, and
next controlling condition.]

**End of entry: [Case or matter], [event or action], [effective date].**

---
```

### 4.1 Chronology and Posture

Use natural Supreme Court phrasing supported by **Event**, such as Argued, Submitted, Reargued, On writ of certiorari to, On appeal from, On certification from, or the supplied original-jurisdiction stage. State accepted questions exactly in substance, including limitations and reformulations. State that a question was not reached only from **Holdings**.

For consolidated matters, identify every docket and docket-specific question or result. Render separately decided companion cases separately, adding a cross-reference only if supplied. Include participation when it differs from the ordinary sitting or affects the vote, authority, or public record.

### 4.2 Judgment

For one disposition with one coalition, use this compact block. Supply only the disposition, tally, names, and disclosure limits established by the public handoff:

```text
#### Judgment

**[Disposition], [supplied vote].**

**Supporting:** [Supplied supporting Justices].
**Opposing:** [Supplied opposing Justices].
[**Not participating:** [Supplied nonparticipants].]
```

Name each supporting and opposing Justice once in this account. Omit the Opposing line for a supplied unanimous judgment and omit Not participating when inapplicable; do not print empty lines or "None." Preserve any supplied distinction between supporting the disposition and supporting its reasoning. Follow the block with any necessary qualification, remedy, or transition that is not already stated accurately elsewhere in the entry. Do not repeat the same judgment lineup in an additional table and paragraph.

Do not simplify a mixed disposition, including one whose several components share a coalition. When dockets, claims, components, or remedies differ, use the component table below, naming the supporting and opposing Justices for each component and any supplied nonparticipant. Keep exact component outcomes and relief even when the vote is identical:

| Judgment component | Disposition and vote | Supporting Justices | Opposing Justices | Remedy or remand |
|---|---|---|---|---|
| [supplied value] | [supplied value] | [supplied value] | [supplied value] | [supplied value] |

Do not reconstruct either form from opinion joins or a vote count. If individual votes or a tally are not publicly disclosed, preserve the supplied disclosure limit and omit unsupported lines; never complete a lineup by inference. A missing or contradictory input needed to state the judgment remains a render blocker under Section 2. These forms do not authorize publication of modeled certiorari polls or undisclosed application votes.

### 4.3 Opinion Topology

Use the table when overlapping writings, partial joins, fractures, or judgment-only relationships would be unclear in a concise narrative. Preserve every distinct join and relationship in either form. For one uncomplicated Court opinion and any straightforward dissent or concurrence, a precise authorship-and-joins statement is sufficient. The table form is:

| Writing | Author | Joined by | Relationship to judgment | Scope joined |
|---|---|---|---|---|
| [supplied value] | [supplied value] | [supplied value] | [supplied value] | [supplied value] |

Identify partial joins by supplied sections or issue propositions; invent no section number. The table describes structure, not authority. If **Opinion Topology** says no opinion commands a majority, state that. Project a controlling *Marks* rationale, *Marks* indeterminacy, or no controlling rationale only from **Holdings**.

State a common whole-opinion coalition once. Where the same coalition supplies authority for several propositions, refer to that unambiguous common account rather than repeat every name. Identify each different proposition-level coalition and partial join precisely. Judgment supporters are never a substitute for this authorship-and-joins account.

### 4.4 Individual positions and attribution

Apply one reporting standard to all Justices, including Stone. Use **Participation** for participation, **Judgment & Remedy** for votes by component, **Opinion Topology** for authorship and exact joins, and **Separate Writings** for the Engine's selected position explanations. An ordinary vote or join needs no second personal summary, and an absence of an additional ground needs no separate statement. When a Justice authors an opinion for the Court, attribute the opinion normally and explain its adopted propositions as the Court's law.

Preserve each supplied partial join, judgment-only relationship, distinct ground, and operative qualification where it belongs in the account. Do not collapse component-specific agreement into a misleading whole-opinion label. Give a separate position only the treatment supplied to explain the Court's authority or its absence, law, judgment, remedy, or public procedural basis. Do not create a dedicated Stone section, compare any public position with private instructions, or discuss his influence or personal performance.

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

For a controlling fractured-decision rationale, project the supplied governing rule, sources, coalition, authority basis, and limit without new synthesis. Preserve a logical-subset basis or *Marks* designation only when **Holdings** supplies it. Never present a plurality rationale as law merely because it explains the judgment.

This section explains the operative rule and why the Court adopts and applies it, within Section 2's explanation ceilings. Give each material qualification beside the proposition it limits. Retain the supplied answer to a material contrary argument; do not substitute a bare conclusion for the reasoning. The precedent and resulting-law account in Section 4.6 performs a different job and need not repeat the complete holding or explanation.

### 4.6 Conditional public sections

Include only populated material. Use these headings and order when the distinctions require separate treatment; in a routine form, integrate the same supplied material into the surrounding narrative without changing its source or force.

#### Limits and Questions Not Reached

State supplied reservations, exclusions, unanswered questions, and grounds not reached. Keep a qualification needed to state a proposition accurately with that proposition.

#### Precedent Treatment and Current-Law Effect

Present **Precedent Treatment** and **Law After Decision** in ordinary legal prose, using this combined heading or separate Precedent Treatment and Current Law headings when their distinct work is clearer. Precedent treatment explains how earlier authority is applied, distinguished, limited, extended, or displaced. The resulting-law account states the operative consequence, surviving boundaries, and any effective transition supplied by **Law After Decision**. Do not copy the full holding and explanation into both accounts; integrate overlap while preserving each source's legal work. No closed treatment vocabulary applies. Omit a separate section for an ordinary application with no supplied material change, retaining any material treatment in the explanation; silence or citation alone is not reaffirmance.

#### Doctrinal Context

Include only public explanatory context supplied by **Law After Decision**. It creates no tag, tracker key, holding, or implication beyond that block.

#### Separate Positions Relevant to the Decision

State the selected position summaries supplied in **Separate Writings**, preserving author, joiners, relationship to judgment, and the supplied proposition, limit, or remedial position. Explain the competing legal ground, the material objection to the Court's reasoning, the points of agreement, and any different disposition or remedy to the extent supplied; a bare statement that a Justice dissents is not a substitute for a supplied substantive summary. Preserve material differences between separate writings even when they support the same result. Integrate a summary into the authority, judgment, or remedy discussion when a separate section would repeat it. The existence of a writing in **Opinion Topology** does not require a separate discussion of its theory. Do not invent a separate opinion from a vote or partial join, expand a supplied summary into a survey of the Justice's views, or call a proposition controlling unless **Holdings** independently establishes that force for the exact proposition.

### 4.7 Mandate, Remedy, and Stage

Conclude the substantive account with the exact mandate or operative order, party-specific relief, remand instructions, transition or expiration, post-action stage, and next established act or condition, then add the entry closing line and divider required by Section 3. Do not invent relief for nonparties, convert probable consequences into a command, or predict the result below.

## 5. Public certiorari actions

Keep the public action separate from any optional simulation audit. Use the common entry boundaries and adapt the interior as needed; the following form is suggested:

```text
### [Case or matter], [docket or dockets when supplied]

[Certiorari action], [effective date]

#### Chronology and Posture
[Petition question, decision below, relevant petition posture, participation,
and consolidation.]

#### Public Action
[Exact grant, limited grant, denial, relist, hold, CVSG, or other action;
question granted or limitation; and publicly disclosed vote or basis.]

[#### Separate Positions Relevant to the Decision]

#### Mandate, Remedy, and Stage
[Effect, stage, and supplied next act, carry condition, or release condition.]

**End of entry: [Case or matter], [certiorari action], [effective date].**

---
```

Do not print modeled certiorari votes, conference positions, or merits predictions here. Denial creates no merits holding. Project the validated result without independently testing the Rule of Four.

## 6. Other procedural and summary actions

For a DIG, GVR, equal division, summary disposition, reargument or rehearing order, stay, application, in-chambers action, or comparable event, use the common entry boundaries and adapt the interior as needed. The suggested form is:

```text
### [Case or matter], [docket or dockets when supplied]

[Action], [effective date]

#### Chronology and Posture
[Decisionmaker, prior stage, participation, referral or renewal path, and
other supplied posture.]

#### Public Action
[Exact action, publicly stated basis or disclosure limit, and public vote.]

[#### Controlling Propositions and Authority]
[#### Limits and Questions Not Reached]
[#### Precedent Treatment and Current-Law Effect]
[#### Separate Positions Relevant to the Decision]

#### Mandate, Remedy, and Stage
[Consequence below, relief, expiration or return condition, stage, and next
controlling condition.]

**End of entry: [Case or matter], [action], [effective date].**

---
```

Include controlling propositions only when **Holdings** supplies them. Never infer Court law from an unexplained order, disclosed vote, single-Justice action, or separate writing.

## 7. Optional Simulation Audit Appendix

The ordinary renderer never receives the CDR's adaptive audit annex. Include an appendix only when the user separately requests it and the Engine supplies a distinct validated **Public Audit Projection** authorized for disclosure. This exceptional input is not a twelfth Render Input block.

Place the appendix after the complete public render and label it **Simulation Audit Appendix**. State that it is nonpublic simulation metadata, not part of the Court's action and not legal authority. Display only fields in the Public Audit Projection. Any modeled certiorari table must label positions nonpublic and reproduce its validated tally and result exactly. Never interleave audit material with a public event or allow it to supply a tracker with law or public procedure.

## 8. Projection check

Before return, verify that:

1. every event appears once in supplied effective order, with the required case heading, event-and-date line, matching closing line, and divider; each boundary encloses only its own event and does not imply a terminal procedural status;
2. chronology, posture, participation, public action, judgment components, coalitions, opinions, partial joins, and selected individual positions match their designated blocks;
3. every controlling proposition, authority statement, and *Marks* result reproduces **Holdings** without synthesis;
4. limits, nonreach, precedent treatment, current-law effect, separate positions, mandate, remedy, transition, and next stage use only their designated blocks;
5. no public/private boundary, quotation rule, no-invented-tag rule, or optional-section rule was violated;
6. every stopped matter and blocker in chunk metadata appears once without an implied adjudication;
7. the account centers the Court's action and law, treats all Justices by the same standard, and contains no dedicated Stone section or repetitive personal account;
8. compression lost no material distinction in the selected public projection and elaboration added no fact or conclusion; and
9. each merits entry has the visible Judgment block or necessary component table, judgment votes remain distinct from opinion joins, and each explanation and designated summary respects Section 2's applicable ceiling without padding or relocation to evade it.

Return no certification on success. From OT1993 forward, when no blocker remains, omit the Workflow Blockers section entirely. If the Render Input fails a projection check, state the exact blocker in operator-facing text and do not adjudicate it. Public entries must never mention that a holding, vote, or Court action is "simulated," "user-directed," "approved," corrected by version, or generated by a model; they speak in the Court's ordinary institutional voice.
