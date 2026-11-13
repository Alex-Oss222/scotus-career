# STONE PRE-VOTE CASE BRIEF

## PURPOSE

One canonical case module prepares one Supreme Court matter for the Simulator Engine.

The brief prepares inputs. It does not adjudicate the Court.

Each case has exactly three live physically separable parts:

1. Section I: Neutral Modeling Packet
2. Section II: Stone Position Supplement
3. Section III: Historical Comparator Supplement

A case block must contain exactly one live Section I, one live Section II, and one live Section III, in that order. A revised approved position replaces the prior Section II text in the brief; do not append a second Section II, a trailing supplement, or a correction addendum. Git history preserves the superseded text. The runtime splitter fails rather than guessing which duplicate section controls.

Use adaptive depth. Routine cases should remain compact. Expand only when a material issue involving law, record, threshold, competing paths, remedy, participation, source uncertainty, or chronology requires it.

The brief does not model non-Stone Justices, predict votes, form coalitions, assign opinions, create a Canonical Decision Record, render the decision, or update trackers.

# SECTION I: NEUTRAL MODELING PACKET

Section I must permit independent modeling without revealing Stone's position or the same matter's historical Supreme Court result.

## A. CASE, RECORD, AND POSTURE

* **Case Name:** [CASE LIST caption]
* **Canonical Matter / Alias:** [Standing State caption or docket if different; otherwise omit]
* **Citation or Docket:** [identifiers]
* **October Term:** [year]
* **Entry Stage and Event:** [precise stage]
* **Simulated Event Date:** [date or scheduling basis]
* **Question Presented:** [exact question]
* **Question Granted:** [if applicable]
* **Court and Judgment Under Review:** [court and disposition]
* **Relief Requested:** [requested Supreme Court judgment and relief]
* **Material Record:** [only decision-material facts, disputes, assumptions, and missing findings]
* **Threshold, Preservation, and Vehicle Matters:** [material matters or none identified]
* **Relevant Dates:** [only chronology-material dates]
* **Companion or Related Matters:** [if material; when a companion or same-term case raises the same doctrine, state the factual, statutory, or procedural differences between the two records, without predicting either outcome or borrowing a historical opinion's framing]
* **Participation Matter:** [recusal, vacancy, nonparticipation, or none identified]

Do not invent a finding the record does not contain.

## B. LAW ENTERING THE CASE

* **Current Through:** [baseline]
* **Earlier Same-Term Decisions:** [only effective decisions that matter]
* **Unresolved Same-Term Dependencies:** [only material pending dependencies]
* **Institutional or Procedural Law:** [only when material]

Repeat for each genuinely distinct issue:

### Issue [number]: [short description]

* **Controlling Simulated Law:** [Holdings proposition and authority]
* **Current Reusable Doctrine:** [operative Standards & Tests provisions]
* **Other Governing Law:** [constitutional, statutory, surviving, or effective noncase law; flag any statute or amendment history enacted to abrogate, codify, or modify a Supreme Court decision this timeline decided differently or never decided]
* **Material Other Authority:** [only authority that performs work]
* **Existing Rule's Reach:** [the questions and applications entering law already governs; distinguish a genuinely unresolved legal question from an ordinary future application that needs only fact-finding under a settled rule]
* **Open Point:** [the legal question entering law actually leaves unresolved, if any]

If Holdings and Standards & Tests materially conflict, state the conflict and stop that issue rather than synthesizing them.

## C. DECISION-MATERIAL LITIGATION POSITIONS

For each material issue state compactly:

* controlling reasoning below;
* material alternative or unreached grounds;
* petitioner's or appellant's strongest supported position, including the general rule it asks the Court to adopt;
* respondent's or appellee's strongest supported position, including the general rule it asks the Court to adopt;
* necessary concessions or limiting principles, including any made by counsel at oral argument and verified from the transcript, never from the opinion;
* Solicitor General or amicus position when it could affect analysis; when the United States or a principal amicus proposes a rule, construction, or remand different from both parties, state that rule and its judgment consequence.

Do not manufacture symmetry where one side lacks a credible answer.

## D. LAWFUL PATHS AND UNCERTAINTY

Identify only materially plausible:

* threshold paths;
* merits paths;
* judgment consequences;
* remedial or remand consequences, including the relief the parties would receive on each path.

**Plausible Holding Scope:** For each materially plausible merits path, identify the legal rule it could establish, the breadth the question presented and the record reasonably support, and its consequences for analogous cases. Include a broader or narrower formulation only when the law genuinely supports it. Do not recommend a formulation or predict the Court's choice.

State any record, source, posture, or legal uncertainty that could change the analysis.

This is a neutral decisional map, not a prediction.

## E. SOURCES

Provide compact source support sufficient to verify material facts, proceedings, arguments, and nonsimulated legal propositions.

Prefer primary and official sources.

## F. CERTIORARI ADDENDUM

Complete only for a designated petition.

* **Petition Question and Posture**
* **Split and Percolation**
* **Vehicle, Finality, and Preservation**
* **Record and Timing**
* **Recurrence or Objective Importance**
* **Related Matters**
* **Solicitor General Role**
* **Participation or Institutional Matter**
* **Term Treatment if Granted**
* **Sources**

Do not include Stone's merits position, Stone's certiorari vote, historical petition treatment, historical grant or denial, or a merits recommendation.

# SECTION II: STONE POSITION SUPPLEMENT

Section II contains Stone's case-specific position. Keep current simulated law distinct from Stone's personal view.

## A. STATUS

* **Approval Status:** [approved / proposed and unapproved]
* **Approval Date or Turn:** [only if actually approved]
* **Current-Through Baseline:** [baseline]
* **Conditions:** [if any]
* **Discretion Envelope:** [only if approved: nonmaterial wording, compatible joins or partial joins, or an authorized narrower formulation the Engine may use without renewed approval]

Do not claim that a newly drafted Stone position was previously approved.

## B. JUDGMENT AND REMEDY

For each docket or separable judgment component:

* **Stone's Controlled Judgment or Disposition:** [exact disposition]
* **Stone's Remedy and Remand Position:** [exact consequence, including the relief the parties receive (damages, injunction, declaration, fees, reinstatement, or other) and, if remanding, the governing standard the lower court applies]
* **Remedial Reach:** [who the relief covers (the named parties, a class, or everyone the challenged policy or practice governs) and why. When a policy, pattern, or practice is proved unlawful, relief reaches the policy and those it governs unless the record shows a narrower remedy fully cures the violation; the party that committed the violation bears that showing. When no proved policy, pattern, or practice and no live claim for relief against it are before the Court, state only whom this judgment's relief covers and give no conditional remedial proposal.]
* **Practical Relief:** [what actually changes: who must do what, by when, how compliance is shown, and what follows if it is not. Relief must work in practice. A declaration or remand that leaves a proved violation in place without a path to cure it is not enough unless the record cannot support more; then say exactly what the lower court must do to get there.]

## C. ISSUE POSITIONS

Answer each question Stone reaches as a whole: whether the right, power, or cause of action exists, its reach within the question, and the remedy. Do not leave reach or remedy for a later case unless a Boundary ground below applies.

Breadth is calibrated, not defaulted. Neither narrowness nor breadth is a virtue in itself. The reach is the one Stone's commitments and the case's needs call for, anywhere from confined to this record to a rule that reshapes the area. It rests on what Stone has actually held and written in this area, the method he uses, the breadth a Justice with his record would realistically write here, and what is needed to resolve this dispute and the recurring problem it represents. Do not narrow to avoid controversy or to anticipate colleagues' votes; do not broaden past what Stone's reasoning supports.

Prefer one administrable test to layered definitions. Add a distinction only if it changes the result in this case or a lower court needs it to apply the rule.

Repeat for each issue Stone lawfully reaches:

### Issue [number]: [short description]

* **Threshold and Merits Reach:** [whether and why Stone reaches the issue, resting on the record rather than on Section I's summary]
* **Question Stone Resolves:** [the question as presented; narrow it only if the Court must]
* **Stone's Legal Position:** [apply current law, apply it differently, or propose changing it; say which]
* **Reach Calibration:** [one of: confined to this record / narrow / intermediate / broad / sweeping (reshapes the area, may overrule). State its basis in Stone's prior positions or method and in what the case needs. Then give one sentence on why not one step broader and one on why not one step narrower.]
* **Stone's Proposed Holding:** [the complete answer, leading with Stone's whole position. Open with one sentence stating the rule that a lower court can quote as written. Then give the controlling rule at the level of generality Stone's reasoning supports, its elements, who bears each burden and at what standard, the material applications it governs, and its application to this case; do not narrow or expand it merely to limit future consequences]
* **Reach Within the Question:** [the persons, conduct, claims, or statutes the rule covers and any it excludes]
* **Next-Case Guidance:** [how the rule applies to the nearest fact patterns its reasoning reaches, stated as part of the rule's scope and not as a decision of a case not before the Court; and for each question left open on a Boundary ground, an interim instruction in the form "Until this Court decides [X], courts apply [Y]," where Y is existing law or the rule this holding states. If the rule's reach is plain and no question is left open, "None."]
* **Transition:** [only when the holding changes law and Stone would depart from the entering-law rule for pending cases, cases on direct review, final judgments, or collateral review, or the parties actually contest that application: state Stone's position, including any departure, and why. Where the entering-law rule applies and no party contests it, "Not applicable." Put any remedial consequence of the change, such as which terms or judgments survive, in Remedial Reach or Practical Relief.]
* **Essential Reasoning and Record Application:** [compact but complete. Draw only on the precedents that do work for Stone's point; this is an argument, not a survey of related cases. For each precedent used, state what it held, as entering law states it in this timeline, and how that holding applies here, is extended, or is distinguished. A list of case names never substitutes for that explanation.]
* **Precedent Treatment:** [each precedent the holding overrules, limits, extends, or reaffirms, by name, with one line on what changes for it. Otherwise "None."]
* **Boundary or Reserved Question:** [only a question that lies outside the question presented, was not raised or preserved, or needs facts the record lacks; name which ground applies. Otherwise "None."]
* **Approved Conditional Position or Fallback:** [only if one actually exists, for example an alternative judgment vote if five votes do not support Stone's own disposition. A fallback is narrower and labeled as such; the lead position above is never pre-narrowed to match it]

If Stone proposes changing current law, identify what current law is, what he would change, the replacement proposition, and what remains unchanged. If Stone treats a rule as existing law, confirm that entering law actually adopted it rather than reserved it; otherwise state it as a new holding.

When three or more bounded rules in entering law govern the same question, say so and state whether Stone would restate them as one test, naming each rule he would fold in or overrule.

## D. CERTIORARI POSITION

Complete only if Stone has an expressly approved petition-stage position.

* **Approved Certiorari Position:** [grant, deny, limited grant, relist, hold, CVSG, or other action]
* **Case-Specific Institutional Ground:** [ground]
* **Status:** [final or interim]

Otherwise omit this subsection. The Engine will simulate Stone's petition-stage vote neutrally.

# SECTION III: HISTORICAL COMPARATOR SUPPLEMENT

Section III is comparison material only. It is not simulated law and does not control Stone.

## A. MERITS COMPARATOR

When a historical Supreme Court merits comparator exists:

* **Historical Outcome and Vote**
* **Historical Opinion Structure**
* **Historical Holding**
* **Historical Authority**
* **Historical Sources**

If no Supreme Court merits comparator exists, state the relevant historical anchor without inventing one.

## B. PETITION COMPARATOR

For a petition:

* **Historical Petition Treatment**
* **Date and Material Procedural Detail**
* **Sources**

Do not place this information in Section I.

# RUNTIME SEPARATION

Before simulation, export the completed chunk without substantive revision into:

* `OT_[YEAR]CHUNK[N]_NEUTRAL.md`, containing only Section I;
* `OT_[YEAR]CHUNK[N]_STONE.md`, containing only Section II;
* `OT_[YEAR]CHUNK[N]_COMPARATOR.md`, containing only Section III.

The Neutral file is used first.

The Comparator file is introduced only after provisional non-Stone commitments are frozen.

The Stone file is introduced only after historical reconciliation.

For certiorari, the neutral petition-stage file goes first and contains neither Stone merits material nor historical petition treatment.

A defect in one case stops only that case unless chronology makes later matters dependent on it.
