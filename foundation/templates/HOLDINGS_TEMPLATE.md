# SUPREME COURT OF THE UNITED STATES: HOLDINGS REGISTER

This document defines the Holdings Register. The completed Register is the authoritative, area-organized account of what the simulated Supreme Court has decided and what force those decisions have now. It preserves controlling propositions and durable limits without reproducing opinions, deliberations, or the Standards and Tests Register.

Bracketed text is an instruction or placeholder. Remove it from the completed Register.

## 1. Function and boundary

The Register contains only:

- controlling merits holdings;
- controlling threshold holdings, including jurisdiction, justiciability, preservation, immunity, cause of action, and vehicle rulings;
- independently sufficient alternative holdings adopted by the required coalition;
- precedential summary holdings, limited to what the disposition necessarily decided;
- proposition-level authority, including a genuine controlling rule under *Marks*;
- material limits, express reservations, and questions not reached;
- a remedy or temporal instruction when it is part of the operative legal result;
- controlling treatment of earlier Supreme Court authority; and
- durable information needed to state the authority of a fractured decision accurately.

The Register excludes:

- denials, relists, holds, calls for the views of the Solicitor General, pure GVRs, DIGs, equal divisions, unexplained orders, and nonprecedential applications;
- current docket posture, pending remands, future actions, and other live procedural state;
- conference material, vote modeling, assignment, circulation, private motive, confidence, or source-audit material;
- Stone's private position or any comparison between Stone and the Court;
- historical comparators, forecasts, and research notes;
- dicta and noncontrolling separate-writing proposals, except to identify a valid *Marks* rule, an actual majority proposition across writings, or the absence of a controlling rationale; and
- copied tests, updating instructions, labels, scores, opaque identifiers, or metadata schemes.

A case-specific holding belongs here even if it creates no generally reusable test. A Standards and Tests entry is neither required for nor proof of a Holdings entry.

## 2. Publication header and cutoff

Use this header:

```text
# SUPREME COURT OF THE UNITED STATES: HOLDINGS REGISTER

**Last completed October Term:** [year]
**Processed through:** [The exact synchronized cutoff statement produced under the Engine's Centralized Term-Close Protocol.]
**Edition:** [date]
```

The `Last completed October Term`, `Processed through`, and `Edition` values must match the simultaneously published Standards and Tests and Standing State documents exactly. A reviewed event may advance the common cutoff without creating a Holdings entry. Do not divide an uncoordinated same-day decision group.

## 3. Controlling sources

At term close, use the validated Canonical Decision Records as the adjudicative source and the corresponding public renders as the required cross-check. Use validated Admitted Source Records for the effect of controlling constitutional, statutory, rule-based, regulatory, or other noncase changes. Also use the valid term-opening Holdings, Standards and Tests, and Standing State documents for the entering baseline and continuity facts.

A clerical correction may repair only an identified error in a name, citation, docket, date, tally, or transcription. Any change to adjudicated substance requires a corrected Canonical Decision Record and render or later controlling Court action.

Do not derive a holding from a case brief, Stone's approved position, a modeled vote, a historical outcome, private reasoning, or a noncontrolling writing. Do not use term close to reconstruct omitted historical law unless the user expressly requests a rebuild.

If a render differs from an otherwise complete and unambiguous Canonical Decision Record, treat the mismatch as a projection error and correct the render from the Record before publication. If the mismatch instead exposes ambiguity or a possible defect in the Record or underlying adjudication that could affect the judgment, controlling proposition, coalition, scope, remedy, or later event, stop incorporation and report the defect outside the Register. Legal indeterminacy validly established by a fractured decision is not a source conflict and must be preserved as indeterminacy.

## 4. Admission rule

Create or amend an entry's judicial holding content only when a Supreme Court event establishes at least one of the following:

1. a controlling merits proposition;
2. a controlling threshold or procedural proposition;
3. an independently sufficient alternative holding;
4. a precedential summary holding within the issue necessarily decided;
5. controlling treatment that changes the present force of an earlier Supreme Court proposition; or
6. a fractured judgment, genuine *Marks* rule, or independently majority-supported proposition whose authority must be preserved for later use.

An Admitted Source Record may amend the `Current force` and later-authority backlink of an existing holding when controlling noncase law changes that holding's present operation. It cannot create or rewrite a judicial Holding. Preserve the holding's force for former text, earlier conduct, or a transition when controlling law requires it, and preserve uncertainty when controlling law leaves the transition unresolved.

Public action alone is insufficient. Never infer a rationale from a summary disposition beyond what its form necessarily decided, and never invent a holding to complete an entry.

## 5. Area-first organization and natural authority anchors

Organize the Register by broad doctrinal area, not by term or decision chronology. Use stable, ordinary legal headings such as Constitutional Structure, Federal Courts, Criminal Procedure, Civil Rights, Administrative Law, or Statutory Interpretation. Create narrower subheadings only when they materially improve retrieval. Do not force a case into an artificial taxonomy. When a case answers questions in distinct broad areas, place each question-level holding in the appropriate area and use compact cross-references rather than duplicate text.

Within an area, order entries for useful legal retrieval, normally by subject and then case. Chronology may break ties but is not the governing structure.

The natural authority anchor is:

```text
[Case name], [official citation when available]; [docket or dockets]; decided [date]; exact question decided
```

Do not create proposition codes, holding IDs, database keys, or mandatory tags.

Use this structure:

```text
## [Broad doctrinal area]

[### [Narrow subject, only if useful]]

#### [Case], [official citation when available]

**Docket or dockets:** [Every docket.]
**Decided:** [Date.]
[**Companion or consolidated matters:** [Identity and relevant relationship.]]

##### [Exact question decided]

**Holding:** [Exact controlling proposition, including any qualification necessary to state it accurately.]

**Proposition-level authority:** [Controlling opinion or instrument; every Justice supporting this exact proposition at the same operative level of generality; nature of its controlling force.]

**Current force:** [One canonical statement of the proposition's present controlling scope. If unchanged, say that it remains controlling as stated. If modified, state only the surviving scope and cite the later controlling case or noncase authority.]

[**Material application:** [Only the case-specific application needed to understand scope.]]

[**Limits and questions not reached:** [Only controlling limits, express reservations, and issues the Court did not reach.]]

[**Operative remedy or transition:** [Only a remedy, remand instruction, or effective transition that is legally operative or necessary to use the holding correctly.]]

[**Material judgment:** [Exact disposition and coalition only when needed to understand authority, fracture, remedy, or the scope of the holding.]]

[**Treatment of earlier authority:** [Earlier case and proposition; what this Court did to it; scope of that treatment. Use ordinary legal prose.]]

[**Later-authority backlinks:** [Later controlling case or noncase source, date or effective date, and exact affected question, proposition, or component, stated compactly without repeating the current-force analysis.]]
```

For multiple questions, repeat the question block under the same case identity. For consolidated matters sharing one opinion and proposition, use one entry and identify every docket. If dispositions differ materially, preserve the distinctions in Material Judgment or Operative Remedy. Use separate entries for companion cases that supply independently usable holdings.

If the same case appears in more than one doctrinal area, one location holds the complete question block. Other locations contain only a natural-language cross-reference giving the case, date, docket, exact question, and primary location.

## 6. Field discipline

### Holding

A holding is a proposition necessary to the judgment or an alternative ground expressly adopted as independently sufficient by the required coalition. Separate the holding from explanation, application, remedy, and nonreach. Include a qualification in the Holding field only when omitting it would overstate the controlling proposition.

Do not record persuasive evidence, policy reasoning, factual narrative, dicta, or a separate writing's gloss as a holding.

### Proposition-level authority

Identify authority for each proposition separately. Opinion joins do not establish a proposition-level coalition when joins are partial or the writings diverge. Name the supporting Justices when the source discloses them. If the public instrument does not disclose a vote or participation, state the disclosure limit rather than infer either.

`Required coalition` means the participating support that governing law requires to make the exact proposition controlling in that event. It is determined proposition by proposition, not inferred from the judgment tally.

Do not reproduce full opinion topology. Include authorship, joins, partial joins, or judgment alignments only to the extent necessary to establish the proposition's authority, a fracture, or an operative remedy.

### Current force and backlinks

Each recorded proposition has exactly one canonical present-force statement: its `Current force` field. Later controlling authority that alters the proposition's present operation requires amendment of that field. Preserve the originally announced Holding and add a compact later-authority backlink to the modifying case or noncase source.

The later case records its own holding and its treatment of the earlier authority. Do not duplicate the earlier proposition's full current-force analysis there. Routine applications and citations do not warrant backlinks.

### Limits, nonreach, remedy, and judgment

Record only limits and nonreach established by the controlling disposition or necessary to avoid overreading it. Do not turn cautionary language into law.

Record a remedy, mandate, remand instruction, or temporal transition only when operative or materially necessary to use the holding. Record the exact judgment, vote, and coalition only when they determine authority, expose a fracture, distinguish docket-level results, or define the remedy. Otherwise omit them.

### Treatment of precedent

Record material controlling treatment proposition by proposition. State what earlier law supplied and the scope of what the later Court changed, preserved, or distinguished. Put the earlier proposition's single complete present-force statement only in that earlier entry's `Current force` field; the later entry supplies treatment, not a duplicate current-law restatement. Do not reduce a compound treatment to one categorical label and do not silently rewrite an earlier holding.

A noncase source changes present force by its own legal operation, not by creating a fictional Court treatment. Record that effect in `Current force` and the later-authority backlink, with any applicable transition.

## 7. Independent alternative holdings

Within the affected question block, use:

```text
**Independent alternative holding:** [Exact independently sufficient proposition.]
**Proposition-level authority for alternative holding:** [Source and exact controlling coalition.]
**Current force of alternative holding:** [One canonical present-force statement.]
[**Limits, remedy, transition, or precedent treatment:** [Only applicable material.]]
```

Repeat only for a genuinely independent ground expressly adopted as sufficient. Discussion unnecessary to the judgment is not an alternative holding.

## 8. Fractured decisions and *Marks*

Analyze authority separately for each question and proposition. Apply the fractured-decision rule currently governing the simulated timeline. Unless controlling simulated authority changes that rule, use the following convention:

1. First preserve any proposition supported by an actual participating majority at the same operative level of generality.
2. If no rationale supporting the judgment has a majority, recognize a *Marks* rule only when a narrower judgment-supporting rule is a true logical subset of one or more broader judgment-supporting rationales, would produce the same result whenever the narrower rule applies as those broader rationales would produce, and the relevant writers together supply the required participating majority.
3. If no such subset exists, state that no controlling rationale exists. Preserve the material judgment and any separately identifiable majority proposition, but do not synthesize a compromise rule.

Use this structure when no controlling rationale exists:

```text
##### [Exact question implicated]

**Authority of the judgment:** [Material judgment; coalition if publicly established; statement that no controlling rationale exists under Marks.]

[If an independently majority-supported proposition exists, repeat this complete three-field group for each such proposition:]
**Independently majority-supported proposition:** [Exact proposition.]
**Proposition-level authority:** [Source writings and every Justice supporting that exact proposition.]
**Current force:** [Canonical present-force statement for that proposition only.]

[**Limits and questions not reached:** [What the judgment and any actual majority proposition establish, without attributing plurality reasoning to the Court.]]
```

For a valid *Marks* rule, identify the source writings, supporting Justices, exact logical subset, and its limit in Proposition-Level Authority. A narrower concurrence does not displace an independent proposition already supported by an actual majority. Agreement in result alone is not a controlling rationale.

## 9. Relationship to Standards and Tests

Holdings and Standards and Tests are parallel outputs derived from the same validated Records and source set. Holdings states what the Court held and its present force. Standards and Tests states the current reusable decision rule. Neither candidate document is authority for the other during preparation.

Do not couple a Holdings entry to an exact Standards heading or reproduce a Standards rule merely for navigation. If a cross-reference is indispensable, describe the reusable doctrine in ordinary legal language so that a later title change does not break the Holdings Register.

## 10. Term-close maintenance

Follow the Engine's Centralized Term-Close Protocol. Do not replicate its source-freeze, chronology, completeness, same-day grouping, reconciliation, atomic-publication, or blocker procedures here.

For Holdings specifically:

- consume every validated Canonical Decision Record and cross-check its render;
- consume every validated Admitted Source Record that affects an existing holding's present operation;
- admit only events satisfying Section 4;
- insert each new question-level proposition under its broad doctrinal area;
- update an older `Current force` field only when later controlling case or noncase authority materially changes it, and add the compact backlink;
- reconcile cross-area references and prevent duplicate holdings; and
- publish the complete current Register, preserving unaffected valid entries.

When size materially impairs reliable use, divide the Register into nonoverlapping doctrinal volumes and provide a short master index. Every volume must carry the identical publication header and common cutoff. A question-level proposition has one primary location across the volume set; cross-volume references remain compact natural anchors. Publication still returns the complete current set, not only changed volumes.

## 11. Validation and return rule

Before publication, verify internally that:

- every admitted proposition has proposition-level controlling authority;
- case name, citation, docket, date, participation, material judgment, and remedy are accurate where included;
- each proposition has one and only one `Current force` statement;
- later treatment updates present force without rewriting the original holding;
- *Marks* is used only for a true logical subset and fractures remain unresolved when they are legally unresolved;
- limits, nonreach, application, remedy, and precedent treatment have not been converted into unsupported holdings;
- cross-area and cross-volume references do not duplicate substantive entries;
- no source conflict has been concealed; and
- the synchronized header matches the other term-close documents.

Do not print a validation receipt.

Return the complete continuous Holdings Register, or the complete master index and all doctrinal volumes when volume splitting is used. Do not return a patch, change log, updater packet, or summary. Remove bracketed instructions and omitted optional fields from the completed Register. If a material source conflict prevents safe publication, identify the precise blocker outside the Register and retain the last complete synchronized baseline.
