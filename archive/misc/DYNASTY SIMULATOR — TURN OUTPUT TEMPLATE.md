## TURN [N]. [CHARACTER NAME], [AGE]

[TITLE, STYLE OR FORM OF ADDRESS, or delete] | [POSITION, RANK, OFFICE OR TRADE] | [HOUSEHOLD, UNIT, WORKSHOP, ESTATE OR EMPLOYER]

[SETTLEMENT, ESTATE, FORT, SHIP OR ROAD SEGMENT], [PROVINCE OR REGION], [JURISDICTION]

Mode: [fictional | historical_fixed | historical_soft | alternate_history] | Span: [1 month | 2 months] | Roll visibility: [visible | result_only | hidden] | This turn reports the resolution of decisions taken at the end of Turn [N-1]. Section 9 sets the decisions that resolve in Turn [N+1].

## SECTION 1: STANDING AT TURN START

Prints every turn, because every feasibility ruling in the turn is checked against it.

Name: [form used, per period, sex, freedom status, citizenship, region and family practice. Do not default to three names.]
Naming basis: [convention chosen, and the uncertainty in it]
Age: [years], [months] | Born: [date or range], [place]
Origin: [community, cultural background, first language, other languages]



The CANNOT list is the feasibility gate in readable form. Nothing in Section 9 may offer an approach that contradicts it.

Attributes: Virtus [N], Disciplina [N], Ingenium [N], Gravitas [N], Eloquentia [N], Amicitia [N], Valetudo [N], Fortuna [N]
Trained skills: [named, concrete skills, since an attribute does not confer specialist work]
Literacy: reading [level, language], writing [level], numeracy [level]
Agents who may act for the character: [name, what each is authorised to do, and the limit on it]
Standing authorizations in force: [instruction, spending cap, and what triggers it]

---

## `[THE CHRONICLER'S RECKONING]`

```
TIMELINE:
- [Year AC — named season — quarter within season]
  (e.g., 298 AC — late summer — second quarter)

CONTEXT:
- [one line on the canon beat or clock event bearing on the quarter, and what
  moves elsewhere in Westeros and Essos offstage]

EDICTS RESOLVED:
- [edict in the player's own terms]
  — verdict: [succeeds / bleeds coin or time / fails / catastrophic backfire]
  — consequence: [the brutal reality of the outcome, naming the specific house,
    market, season, sermon, or condition that delivers it]
- [next edict, same shape]
- [next edict, same shape]
[Print "none" on a turn with no player edict.]

TIER SHIFTS:
- Treasury: [prior → ±1 (named cause) → new]
- Levies: [prior → ±1 (named cause) → new]
- Granaries: [prior → ±1 (named cause) → new]
- Vassal temper, House [X]: [prior → ±1 (named cause) → new]
[Write "none" if no tier moved. Single-step shifts only. A two-step jump
(→ ±2) prints only when a named catastrophe or windfall in the Raven's Report
justifies it. A shift prints only when an event in the Raven's Report explains it.]

TRAJECTORY:
- [improving / steady / worsening]
[A "worsening" verdict must cite its cause — a failed edict, a fired clock event,
or an unaddressed dilemma resolving against the ruler. Absent a named cause, the
realm holds steady. Do not manufacture decline.]

KNOWLEDGE AUDIT:
- Confirmed this quarter: [accounts the maester, stewards, or captains have verified]
- Reported, unverified: [what arrived as rumor, sermon, hedge knight's tale, stale letter]
- Resolved rumors: [omit if none — prior KNOWN, UNCONFIRMED items now settled
  as true, exaggerated, or false]
```

---

## `[THE RAVEN'S REPORT]`

Prints every turn. This is the document's centre of gravity. 800 to 1,200 words for a one-month span, 1,100 to 1,600 for two months.

### Form

Open with a single line: Turn [N] covers [start date] to [end date].

Then four to seven dated blocks in chronological order. Each heading is a date or a date range, then a colon, then a short phrase naming what the block contains. Present tense throughout.

```text
#### [Date]: [what happens here]

#### [Date] to [date]: [what happens here]

#### [Date] and [date]: the month closes
```
---

## `[THE SPEAR AND THE SEAT]`

Two to three dilemmas active this quarter, each materially different, each carrying feudal, fiscal, dynastic, or martial risk. No option is clean — only agonizing choices of what to sacrifice: coin, blood, honor, or loyalty. Format each as:

**[Title of the matter]** — [two to four sentences naming the houses or factions involved, the immediate crisis, the material resources required to intervene, what is risked by acceding, and the cost of inaction. Mark distant or third-hand reports as *unconfirmed* where the ruler could not have verified them.]

**[Title of the matter]** — [same shape]

**[Title of the matter]** — [same shape; optional third only if the quarter warrants it]

A dilemma ignored, under-resourced, or unaddressed in the player's `<ROYAL_EDICT>` resolves itself without the ruler's guidance, by the Triad, to the realm's detriment.

After the dilemmas, the status block:

```
=== PLAYER'S KNOWLEDGE === (in-character; what the keep knows)
```text
STATUS, ON SEPARATE AXES
Freedom:              [enslaved | freed | freeborn]
Citizenship:          [Roman | Latin | peregrine | local | none | disputed]
Civic status:         [municipal or local standing, or none]
Family status:        [sui iuris | under potestas of [WHOM]]
Order or census rank: [senatorial | equestrian | decurional | none | disputed]
Formal infamia:       [yes, with the disability named | no]
Other disabilities:   [legal bars, oaths, guardianship, occupation-linked bars]
Occupation:           [main role] | Duty now: [current assignment]
```

```text
AUTHORITY
Practical power: [narrow | limited | substantial | commanding] in [this jurisdiction]
├─ Property title:      [owns | holds peculium | manages for another | none]
├─ Contract capacity:   [full | limited by status | requires authorisation | none]
├─ Household authority: [head | delegated manager | dependent | none]
├─ Command authority:   [over whom, in what circumstance | none]
├─ Legal standing:      [may sue and be sued | requires a representative | barred]
├─ Marriage capacity:   [restrictions by status, rank or service]
├─ Office eligibility:  [what is open by law, age and census, and what is not]
└─ Movement:            [free | requires leave, pass or order | confined]

CANNOT, THIS INTERVAL
- [Structural bar, with the reason: law, status, distance, season, money, authority]
- [Second bar]
- [Third bar]

MUST, THIS INTERVAL
- [Non-negotiable duty, with its date and the penalty for default]
- [Second obligation]
```

Cap each list at five entries. Drop entries that no longer affect future quarters. Tempers, tiers, and rumors in Ruler's Knowledge must match the Reckoning's *TIER SHIFTS* and *KNOWLEDGE AUDIT* — the status block is a snapshot, not a recalculation.

Close the entire turn with this line on its own, no embellishment:

*Custom edicts accepted.*

### Primary undertaking

Carryover issue: [the one known problem or aim, with the constraints that make it non-trivial: what is not known, what cannot be reached in time, who else holds the authority, what it competes with for the same days and the same money.] 100 to 150 words.

Deadline inside the next interval: [date and the consequence of missing it, or none]

Approaches, two to four, no more:

1. [Approach.] Cost: [ ]. Time: [days]. Delay: [ ]. Legal exposure: [ ]. Obligation created or spent: [ ]. Physical risk: [ ]. Information gained: [ ]. Duties it displaces: [ ].
2. [Approach.] Cost: [ ]. Time: [days]. Delay: [ ]. Legal exposure: [ ]. Obligation: [ ]. Risk: [ ]. Information: [ ]. Displaces: [ ].
3. [Approach, or delete.] [same fields]
4. [Approach, or delete.] [same fields]

Free action: any other approach, tested against the CANNOT list in Section 1 before it is rolled.

No approach is marked as the sound one. No hidden outcome is signposted in the wording. An impossible approach is not offered; the blocker is stated instead.

### Secondary actions

Three to five, each costing a named number of discretionary days, totalling no more than the discretionary remainder in Section 2.

1. [Errand, visit, purchase, letter, offering, inspection or contact.] Days: [N]. [Option A | Option B | skip]
2. [ ] Days: [N]. [ ]
3. [ ] Days: [N]. [ ]
4. [ ] Days: [N]. [ ]
5. [ ] Days: [N]. [ ]

Discretionary days committed: [N] of [N] available.