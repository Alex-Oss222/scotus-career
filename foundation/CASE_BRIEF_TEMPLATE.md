# STONE PRE-VOTE CASE BRIEF

## PURPOSE

One canonical case module prepares one Supreme Court matter for the Simulator Engine.

The brief prepares inputs. It does not adjudicate the Court.

Each case has three physically separable parts:

1. Section I: Neutral Modeling Packet
2. Section II: Stone Position Supplement
3. Section III: Historical Comparator Supplement

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
* **Companion or Related Matters:** [if material]
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
* **Other Governing Law:** [constitutional, statutory, surviving, or effective noncase law]
* **Material Other Authority:** [only authority that performs work]
* **Open Point:** [what entering law leaves unresolved, if anything]

If Holdings and Standards & Tests materially conflict, state the conflict and stop that issue rather than synthesizing them.

## C. DECISION-MATERIAL LITIGATION POSITIONS

For each material issue state compactly:

* controlling reasoning below;
* material alternative or unreached grounds;
* petitioner's or appellant's strongest supported position;
* respondent's or appellee's strongest supported position;
* necessary concessions or limiting principles;
* Solicitor General or amicus position only when it could affect analysis.

Do not manufacture symmetry where one side lacks a credible answer.

## D. LAWFUL PATHS AND UNCERTAINTY

Identify only materially plausible:

* threshold paths;
* merits paths;
* judgment consequences;
* remedial or remand consequences.

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

* **Version:** [version]
* **Approval Status:** [approved / proposed and unapproved]
* **Approval Date or Turn:** [only if actually approved]
* **Current-Through Baseline:** [baseline]
* **Conditions:** [if any]

Do not claim that a newly drafted Stone position was previously approved.

## B. JUDGMENT AND REMEDY

For each docket or separable judgment component:

* **Stone's Controlled Judgment or Disposition:** [exact disposition]
* **Stone's Remedy and Remand Position:** [exact consequence]

## C. ISSUE POSITIONS

Repeat for each issue Stone lawfully reaches:

### Issue [number]: [short description]

* **Threshold and Merits Reach:** [whether and why Stone reaches the issue]
* **Question Stone Resolves:** [only if narrowing is required]
* **Stone's Legal Position:** [apply current law, apply it differently, or propose changing it]
* **Stone's Proposed Holding:** [legal proposition plus necessary case application]
* **Essential Reasoning and Record Application:** [compact but complete]
* **Boundary or Reserved Question:** [when material]
* **Approved Conditional Position or Fallback:** [only if one actually exists]

If Stone proposes changing current law, identify what current law is, what he would change, the replacement proposition, and what remains unchanged.

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
