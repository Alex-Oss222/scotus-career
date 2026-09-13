# SUPREME COURT OF THE UNITED STATES: STANDARDS AND TESTS

This Register states the recurring legal instructions that a later court must presently use. It is a current-law research source, not a case digest, historical archive, reasoning diary, or updater report.

Bracketed text is an instruction or placeholder and does not appear in the completed Register.

## 1. Scope

Include a proposition only when controlling law makes it a reusable legal instruction. The instruction may take any form the law actually adopts, including a categorical rule, element, threshold, factor inquiry, balance, scrutiny standard, presumption, burden, construction, exception, procedural sequence, standard of review, or recurring remedial rule.

Do not include:

- a case-specific holding, application, factual result, remedy, or observation;
- dicta, a separate-writing proposal without controlling force, or a reserved question;
- policy reasoning or evidence that controlling law did not make operative;
- a lower-court rule or post-divergence real-world rule not adopted in the simulation;
- a duplicate of a current instruction already stated at the proper level of generality; or
- an editor-created synthesis, burden, exception, factor, or fallback route.

Holdings records what particular decisions held. Standing State records institutional and procedural continuity. This Register contains only the consolidated reusable law now in force.

## 2. Publication header

Use:

```text
# SUPREME COURT OF THE UNITED STATES: STANDARDS AND TESTS

**Last completed October Term:** [year]
**Processed through:** [the exact common cutoff required by the Engine]
**Edition:** [date]
```

The `Last completed October Term`, `Processed through`, and `Edition` values must match Holdings and Standing State exactly. Apply the Engine's centralized term-close protocol for source freezing, chronology, same-day decisions, completeness, validation, and coordinated publication. Do not reproduce that protocol here.

## 3. Authority and derivation

Use the source hierarchy and authority determinations fixed by the Engine. A valid term-opening Standards and Tests entry is the carried current-law baseline through its opening cutoff and may remain unchanged even when the historical Holdings Register lacks a corresponding entry. Do not silently delete or reconstruct it. Later controlling law, a documented source defect, or an express rebuild may change that treatment.

A new or changed case-derived operative component is eligible only if it is entailed by:

1. an identified question-level proposition in the valid term-opening Holdings, read as originally held and constrained by its `Current force` field and material later treatment; or
2. an identified controlling proposition in a validated Canonical Decision Record for the current term, including a valid *Marks* or precedential summary-disposition determination made there, that remains operative after every later effective current-term Record.

The authority reference must identify the proposition and the component it supplies. Do not infer a component from the judgment alone, a party's argument, Stone's private position, a historical comparator, conference material, or a noncontrolling writing.

At term close, candidate Holdings and candidate Standards and Tests are parallel derivatives of the term-opening baseline, validated Canonical Decision Records, and validated Admitted Source Records. Neither new candidate document is authority for, or may bootstrap, the other. Reconcile navigation references only after each candidate's legal substance has been derived independently.

Effective constitutional text, statutes, rules, regulations, and other controlling noncase law may supply a component when the Engine preserves them in a validated Admitted Source Record. Identify the precise provision or text, the component it supplies, its effective date, and any controlling construction. If valid sources conflict about authority, scope, coalition, date, or legal effect, report the precise conflict and do not publish an invented compromise. If controlling law itself leaves an interaction unresolved, preserve that uncertainty as current law.

## 4. Admission and consolidation

Create or retain an entry only when all of these conditions are satisfied:

1. Controlling authority supplies the proposition.
2. It governs a recurring question beyond the source case's distinctive facts.
3. It tells a later court what to ask, require, presume, compare, review, construe, or do, or what legal consequence follows.
4. It remains usable when case-specific names and facts are removed.
5. No current entry already states the instruction at the correct level of generality.
6. Every operative component has identified controlling support.

Search the whole Register by governing question, trigger, and mechanics before adding an entry. One decision may change several entries, and several decisions may supply one entry. A different party, technology, factual setting, legal theory, or requested remedy does not by itself justify a separate rule.

An ordinary application, reaffirmance, citation, or case-specific distinction creates no entry or development note. Integrate a subclass, exception, safe harbor, or limiting principle into the rule it qualifies unless controlling law gives it a distinct recurring trigger and independently usable mechanics.

## 5. Preserve the law's actual form

State the analysis the controlling law adopted. Do not translate one form into another for consistency. In particular:

- A categorical rule states its trigger and commanded result without invented factors.
- An elements rule states only adopted predicates and the consequence of satisfaction or failure.
- A factor or totality inquiry distinguishes mandatory considerations from illustrative ones and identifies controlling weight only when the law does.
- A balance identifies what is compared and the rule governing the comparison.
- A scrutiny or burden-shifting rule states the governed class, stages, required showing, burden carrier, proof level, and consequence only to the extent adopted.
- A historical inquiry states the relevant period, level of generality, analogical method, and consequence only to the extent adopted.
- A procedural rule states the actor, sequence, timing, showing, and consequence supplied by law.
- A construction identifies the text construed and its controlling meaning.

Facts do not become factors. Persuasive evidence does not become a required showing. Discussion of consequences does not convert a categorical rule into balancing. Silence about one component does not authorize an editor to supply it. A change to one component does not imply a change to any other.

## 6. Organization and identity

Organize current entries under broad, familiar doctrinal areas and human-readable rule titles:

```text
## [Broad doctrinal area]

### [Human-readable rule title]
```

Area headings are navigation aids, not a closed ontology or source of law. Add, divide, combine, rename, or retire them when ordinary legal retrieval warrants it. Give each rule one canonical home, ordinarily under the doctrine supplying its trigger and operative mechanics. Use cross-references for material interactions rather than duplicating the rule.

Titles must be stable, descriptive, and understandable to a legal reader. A conventional case-linked or doctrinal name may be paired with a descriptive title when it materially improves legal retrieval, but the familiar name supplies no independent legal content. Do not use opaque identifiers, numbered codes, taxonomy labels, scores, confidence fields, or invented doctrinal branding.

When scale impairs retrieval, divide the Register into doctrinal volumes. Every volume must use the same publication cutoff and edition, define its ordinary-language scope, and preserve one canonical home for each rule across the complete set. Volumes do not alter authority or create doctrinal boundaries.

## 7. Entry form

Use the following core fields for every current rule:

```text
### [Human-readable rule title]

**Governing question:** [The recurring question, trigger, class, or stage governed.]

**Current rule:** [The complete controlling instruction in its actual legal form.]

**Authority by component:**
- [Component]: [For case-derived law, give the question-level natural authority anchor and original Holding as constrained by its `Current force` field, or the operative Canonical Decision Record proposition, with decision date. For noncase law, give the precise controlling text or provision, component supplied, effective date, and material controlling construction.]

**Present operation effective:** [Authority and date of the most recent operative change.]
```

Add only fields that materially improve accurate application. Omit inapplicable fields without placeholders:

```text
[**Burdens and proof:** [Controlling allocation or proof requirement.]]

[**Sequence or decisionmaker:** [Controlling stage, order, timing, or actor.]]

[**Presumption or rebuttal:** [Starting rule, rebuttal showing, burden carrier, and consequence.]]

[**Controlling construction:** [Text construed and adopted meaning.]]

[**Consequence or recurring remedy:** [Reusable controlling consequence.]]

[**Exceptions and limits:** [Controlling exception, safe harbor, exclusion, qualification, or boundary.]]

[**Open question:** [Precisely what controlling law leaves unresolved and which authority leaves it open.]]

[**Unresolved interaction:** [The rules or authorities involved, what each controls, and the exact unresolved boundary.]]

[**Effective transition:** [Prospective, delayed, stayed, or transitional operation expressly supplied by controlling law.]]

[**Related current rules:** [Exact titles and a concise statement of the legally supported interaction, without restating either rule.]]

[**Material development:** [Only the compact before-and-after change needed to understand present operation, transition, or surviving force.]]
```

Do not repeat mechanics across the core rule and optional fields. When authorities supply different components, map each one separately. Do not attribute the entire rule to the latest decision merely because it applied or restated the rule.

`Present operation effective` identifies the latest change in legal operation, not a later application or wording change. If later authority materially clarifies the current wording without changing operation, identify it in `Authority by component` or, if needed, add `Current wording authority`. Same-day decisions that were not sequentially coordinated use the common start-of-day baseline required by the Engine; cite every decision necessary to support the combined post-day rule.

## 8. Limits, interactions, and transitions

State limits at the level controlling law establishes. Do not broaden a reservation into an exception or narrow an exception into a factual example.

A safe harbor states its conditions, the protection inside it, and the legal position outside it if controlling law resolves that point. Failure to enter a safe harbor does not itself establish liability or invalidity unless controlling law says so. A presumption states the initial conclusion, rebuttal showing, burden carrier, and consequence. A recurring remedy enters the Register only when controlling law makes it reusable; case-specific relief remains in Holdings.

Use `Open question` when silence would otherwise overstate the rule. Use `Unresolved interaction` when valid authorities retain force but do not establish their hierarchy or combined operation. Do not resolve either through editorial synthesis.

State an effective transition only when controlling law supplies one. Preserve the prior rule for events governed by it, but do not maintain a general inactive archive.

## 9. Former-rule notes

Omit displaced rules unless their surviving force, transition, later treatment, or possible restoration makes a compact note necessary. Place any necessary note immediately after the current successor or under the former rule's doctrinal area:

```text
**Former-rule note:** [Former rule in the minimum detail needed]; ceased to govern [authority and date]; [successor, transition, or exact surviving force].
```

Do not reproduce obsolete mechanics beyond what the surviving issue requires. A former rule remains applicable to decisions and conduct governed while it was in force, but its note does not make it current law.

## 10. Quality controls

Before publication, confirm that:

- every entry is a reusable current instruction, not a case summary;
- every new or changed operative component is entailed by an identified currently operative controlling proposition or admitted noncase source, and every unchanged carried component remains supported by a valid term-opening entry;
- the rule preserves the controlling law's form, scope, burdens, sequence, limits, consequence, and transition without supplementation;
- case-specific applications and routine reaffirmances did not create entries or development notes;
- each rule appears once under one canonical title, including across volumes;
- cross-references state only supported interactions and do not reproduce rules;
- unresolved questions and authority boundaries remain unresolved;
- former-rule notes are retained only for material surviving force or transition; and
- the cutoff and edition match Holdings and Standing State.

Do not print this checklist or a validation claim.

## 11. Return rule

Return the complete continuous Register, or the complete coordinated set of doctrinal volumes, not a patch, change log, classification report, or updater packet. Preserve unrelated valid entries. Remove bracketed instructions and omitted optional fields.

If a missing source or authority conflict prevents a safe update, identify the exact blocker outside the Register and do not advance the common cutoff.
