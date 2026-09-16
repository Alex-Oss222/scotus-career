$ErrorActionPreference = 'Stop'
$workspaceDir = Split-Path -Parent $PSScriptRoot
function Read-Packet([string]$name) { return [IO.File]::ReadAllText((Join-Path $workspaceDir $name)).Replace("`r`n", "`n") }
function Replace-Once([string]$text, [string]$old, [string]$new) {
    $count = [regex]::Matches($text, [regex]::Escape($old)).Count
    if ($count -ne 1) { throw "Expected one occurrence ($count): $($old.Substring(0,[Math]::Min(90,$old.Length)))" }
    return $text.Replace($old, $new)
}
function Replace-CaseBody([string]$text, [string]$caption, [string]$body) {
    $pattern = '(?ms)(^## ' + [regex]::Escape($caption) + '\n.*?)(^#### B\. JUDGMENT AND REMEDY\n.*?)(?=\n---\n\n## |\z)'
    $match = [regex]::Match($text, $pattern)
    if (-not $match.Success) { throw "Missing case body: $caption" }
    return $text.Substring(0,$match.Index) + $match.Groups[1].Value + $body.Trim() + "`n" + $text.Substring($match.Index+$match.Length)
}
$s10 = Read-Packet 'OT_1992CHUNK10_STONE.md'
$s11 = Read-Packet 'OT_1992CHUNK11_STONE.md'

# 109. Common capacity is a proposed resolution; actual capacity and waiver remain separate.
$s10 = Replace-Once $s10 (@'
revive the death sentence already reduced on direct review
'@) (@'
revive the death sentence for the ex-wife's murder already reduced to life without parole on direct review (the other two death sentences remained)
'@)
$s10 = Replace-Once $s10 (@'
Apply Dusky and the received waiver cases, rejecting a separate higher competence threshold while preserving the independent waiver requirements.
'@) (@'
Resolve the open common-capacity question through Dusky and the received waiver cases, rejecting a separate higher competence threshold while preserving the independent waiver requirements. The equivalence of standards is the resolution proposed here, not a previously settled same-case rule.
'@)
$s10 = Replace-Once $s10 (@'
The constitutional capacity standard is Dusky for standing trial, pleading guilty, and waiving counsel.
'@) (@'
The constitutional capacity standard Stone adopts is Dusky for standing trial, pleading guilty, and waiving counsel: sufficient present ability to consult with counsel with rational understanding, and rational as well as factual understanding of the proceedings.
'@)
$s10 = Replace-Once $s10 (@'
The trial judge made express findings, but the medication and other circumstances must be evaluated for the work the distinct doctrines assign them.
'@) (@'
The trial judge made express findings, but the medication and other circumstances must be evaluated for the work the distinct doctrines assign them. On remand determine whether contemporaneous circumstances required further inquiry, whether any retrospective determination can still be reliable, and whether each actual relinquishment was informed and voluntary. Earlier reports cannot conclusively answer a materially changed condition. Apply pre-AEDPA habeas treatment of the state findings before selecting relief.
'@)

# 110. Implement the review's source-specific equality analysis, separately from family participation.
$heller = @'
#### B. JUDGMENT AND REMEDY

**Stone's Proposed Judgment or Disposition:** AFFIRM the invalidation of the unequal proof burdens, REVERSE the categorical invalidation of family or guardian participation, and REMAND for a limited remedy and unresolved matters.

**Stone's Remedy and Remand Position:** Address severability and the State's lawful choices for equalizing safeguards. This judgment does not establish a national beyond-reasonable-doubt commitment standard or require immediate release of every class member. Each continuing confinement needs its own lawful basis. Family participation remains subject to counsel, effective contest, and independent adjudication.

#### C. ISSUE POSITIONS

##### Issue 1: The preserved equality claim and allocation of error risk

**Threshold and Merits Reach:** Do not reach the heightened-scrutiny theory first advanced at this stage. Decide the preserved rational-basis challenge under Cleburne and the separate due-process question under its own sources.

**Stone's Legal Position:** Apply received rational-basis review to the particular procedural disadvantage. Stone's preferred disability tier is not the governing rule in this appeal. This conclusion is his application of an available framework, not a result compelled by it.

**Stone's Proposed Holding:** Kentucky's reasons for treating the two conditions differently do not rationally explain the lower overall protection against erroneous institutional confinement imposed on this class. Satisfaction of Addington's federal minimum does not independently answer the equality objection to unequal safeguards. [Cleburne, 473 U.S. 432 (1985)](https://supreme.justia.com/cases/federal/us/473/432/); [Addington, 441 U.S. 418 (1979)](https://supreme.justia.com/cases/federal/us/441/418/).

**Essential Reasoning and Record Application:** The State's diagnostic argument concerns the identification of a condition, while commitment also requires judgments about dangerousness, treatment benefit, and institutional placement. Stone accepts that a longer behavioral history may improve some predictions and that reasonable legislative generalizations are permissible. His disagreement is that those differences sufficiently explain assigning the individual a greater risk of erroneous confinement across the scheme as a whole. A categorical claim that one group's treatment is less intrusive also does not adequately account for the comparable loss of physical liberty. This reasoning addresses all of the State's explanations rather than requiring a separate empirical demonstration for each predicate. It does not require formal legislative findings, a scientific study, or governmental proof under an unstated higher tier.

**Contrary application:** Different diagnostic histories, prediction risks, and treatment may be understood to permit different safeguards. Stone acknowledges that rational-basis argument. His conclusion concerns its connection to the actual disadvantage—allocation of the risk of mistaken confinement—and does not declare every distinction between the conditions irrational. [Record and contemporaneous analyses, 509 U.S. 312 (1993)](https://supreme.justia.com/cases/federal/us/509/312/).

**Boundary:** Equal protection requires a rational relationship to the particular procedural difference, not identical procedures in every setting. Addington's minimum and the substantive predicates of commitment remain independent. No new scrutiny tier or categorical liberty discount for disability is adopted.

##### Issue 2: Differential family-party status and fair adjudication

**Threshold and Merits Reach:** Decide the equality challenge to family-party status separately from its Mathews procedural consequences.

**Stone's Proposed Holding:** A lifelong developmental condition and continuing family involvement plausibly make relatives' participation especially informative, supplying a rational basis for the participation distinction. Under Mathews, party status does not by itself violate due process where the subject can effectively contest the evidence with counsel before an independent decisionmaker.

**Essential Reasoning and Record Application:** Gathering relevant information differs from assigning a person's liberty less weight. Relatives' knowledge can be tested in the proceeding; their preferences, conflicts, or convenience establish no commitment predicate. Stone does not presume that a family member and the adult share interests. A neutral adjudicator must apply the lawful burden to the statutory grounds, and the adult must have an effective opportunity to answer adverse evidence. [Mathews v. Eldridge, 424 U.S. 319 (1976)](https://supreme.justia.com/cases/federal/us/424/319/).

**Boundary:** A proceeding in which relatives control the outcome, suppress the adult's position, or defeat effective contest remains challengeable. Neither ruling establishes that every individual hearing was fair.
'@
$s10 = Replace-CaseBody $s10 'Heller v. Doe' $heller

# 111. Reserve the master's falsification exception without silently changing Imbler.
$s10 = Replace-Once $s10 (@'
The ruling does not award damages or remove absolute immunity from testimony or actual prosecutorial advocacy not resolved here.
'@) (@'
The ruling does not award damages. It reserves Stone's proposed exception for knowing material falsification in otherwise protected advocacy or testimony; that broader departure from received immunity law is unnecessary to resolve these investigative acts and press statements. Existing Harlow/Anderson qualified immunity remains a separate question.
'@)

# 114. Preserve review without demanding access to juror deliberations or ignoring default.
$s10 = Replace-Once $s10 (@'
Stone treats the instructional arguments as elaboration of the preserved federal due-process challenge under Yee, rather than a new claim. He reaches the adequacy of guidance and review but does not fix a constitutional maximum.
'@) (@'
Identify the specific instructional objections preserved below. Yee permits an additional argument supporting a preserved federal claim; it does not defeat an independent state procedural default. Reach instructional matters to that extent, and otherwise confine the holding to the preserved adequacy-of-review and excessiveness challenge. No constitutional maximum is fixed.
'@)
$s10 = Replace-Once $s10 (@'
But relevance is not a finding that the jury valued that harm in the manner later suggested.
'@) (@'
A court may uphold a general verdict on supported evidence, lawful instructions, and meaningful review without reconstructing what jurors privately calculated. The inquiry is whether those objective safeguards adequately support and constrain the amount, not whether the jury supplied an explanation or special verdict.
'@)

# 115. Preserve the defendant/remedy distinction in the circumstantial-inference ruling.
$s10 = Replace-Once $s10 (@'
Later employment-discrimination decisions supply neither the rule nor the factual assessment in this 1993 case.
'@) (@'
Later employment-discrimination decisions supply neither the rule nor the factual assessment in this 1993 case. Keep Title VII and §1983 defendants and remedies separate; the unchallenged common intentional-discrimination analysis is accepted only for this case.
'@)

# 116. The user's new baseline supersedes the obsolete assignment injury and two lanes.
$shaw = Read-Packet 'review/SHAW_REVISED_POSITION.md'
$shawSection = $shaw.Substring($shaw.IndexOf('### SECTION II')).Trim()
$shawPattern = '(?ms)(^## Shaw v\. Reno\n\n)### SECTION II.*?(?=\n---\n\n## United States v\. Dixon)'
if ([regex]::Matches($s10,$shawPattern).Count -ne 1) { throw 'Shaw replacement target mismatch.' }
$s10 = [regex]::Replace($s10,$shawPattern,{param($m) $m.Groups[1].Value + $shawSection + "`n"})

# 117–120. Tighten the native rules without importing later law.
$s10 = Replace-Once $s10 (@'
Where the subsequent prosecution necessarily proves the criminal act already tried as an essential part of the earlier contempt charge, the successive prosecution is barred.
'@) (@'
Under the retained Grady rule, a subsequent prosecution is barred when establishing an essential element would require proving conduct constituting an offense for which the defendant has already been prosecuted.
'@)
$s10 = Replace-Once $s10 (@'
Under Rules 104(a) and 702, the proponent must establish the preliminary foundation for reliable scientific knowledge
'@) (@'
Under Rules 104(a) and 702, the proponent must establish by a preponderance of the evidence the preliminary foundation for reliable scientific knowledge
'@)
$s10 = Replace-Once $s10 (@'
The preliminary foundation is assessed under the inherited Rule 104(a) framework;
'@) (@'
The preliminary foundation is assessed under the inherited Rule 104(a) framework and Bourjaily v. United States, 483 U.S. 171, 175–176 (1987);
'@)
$s10 = Replace-Once $s10 (@'
The absence of relevant valuation and proportionality findings calls for remand, not an appellate assumption in either party’s favor.
'@) (@'
The absence of relevant valuation and proportionality findings calls for remand, not an appellate assumption in either party's favor. Examine the property interest and supported value taken, seriousness and extent of the wrongdoing, the owner's relevant culpability, and the property's actual role. These are Stone's proposed nonexclusive considerations derived from the Clause, not settled 1993 guideposts or a comprehensive formula.
'@)
$s10 = Replace-Once $s10 (@'
Congress’s § 6a boundaries remain controlling where applicable; these allegations describe direct, substantial, foreseeable American effects, so Stone need not decide whether that enactment altered every aspect of prior law.
'@) (@'
Congress’s § 6a boundaries remain controlling where applicable, including both the required direct, substantial, reasonably foreseeable domestic effect and the requirement that the qualifying effect give rise to the asserted claim. The alleged changes in American coverage supply the connection asserted here. Stone does not resolve the provision’s reach beyond what is necessary on these allegations or omit its claim-connection requirement.
'@)

# 121. First Amendment scrutiny has an express trigger and standard, distinct from excessiveness.
$alexander = @'
#### B. JUDGMENT AND REMEDY

**Stone's Proposed Judgment or Disposition:** VACATE the judgment insofar as it sustains the challenged forfeiture without the necessary Excessive Fines and distinct First Amendment inquiries, and REMAND. Reject the categorical prior-restraint objection to postconviction forfeiture that forbids no future publication.

**Stone's Remedy and Remand Position:** Leave the independently sustained convictions undisturbed. Determine the forfeiture's statutory nexus, punitive extent, and burden on lawful expression. Distinguish the judicial order from the Government's later administrative destruction of inventory, the injury attributable to the judgment, the matters reviewable here, and the correction still available. This appeal creates no damages cause of action and cannot order return of destroyed stock. No dollar cap or ultimate proportionality finding is entered.

#### C. ISSUE POSITIONS

##### Issue 1: Prior restraint and the separate burden on lawful expression

**Threshold and Merits Reach:** Decide the preserved challenge to the postconviction sanction. A prior-restraint label does not exhaust the constitutional inquiry.

**Stone's Legal Position and Treatment of Precedent:** Apply Arcara's distinction between sanctions for ordinary nonexpressive conduct and sanctions triggered by expression or targeting expressive activity. Applying that distinction to this enterprise forfeiture is Stone's proposed constitutional application; Fort Wayne Books did not settle every postconviction forfeiture of lawful stock. [Arcara, 478 U.S. 697, 706–707 (1986)](https://supreme.justia.com/cases/federal/us/478/697/); [Fort Wayne Books, 489 U.S. 46, 60–67 (1989)](https://supreme.justia.com/cases/federal/us/489/46/).

**Stone's Proposed Holding:** An ordinary sanction for nonexpressive misconduct does not trigger special scrutiny merely because a publisher loses assets. Here expressive predicates drew the sanction and removal of lawful inventory presents a distinct expressive burden. For a genuinely content-neutral incidental restriction within that trigger, apply O'Brien: lawful authority, an important or substantial interest unrelated to suppressing expression, and an incidental restriction no greater than essential to that interest. A measure suppressing works because of their protected content instead requires compelling justification and narrow tailoring. [O'Brien, 391 U.S. 367, 377 (1968)](https://supreme.justia.com/cases/federal/us/391/367/).

**Essential Reasoning and Record Application:** A valid obscenity conviction permits authorized punishment, but does not itself establish that eliminating lawful expressive inventory is permissible. The counterargument is that neutral RICO asset forfeiture fully accounts for the burden. Stone answers it through the sanction's particular operation: distinguish transfer of forfeitable economic interests from suppression of protected works, and examine whether lawful asset realization can accomplish the authorized punishment without gratuitously eliminating expression. The reported destruction makes scope and causation concrete. The judicial forfeiture and the Government's administrative choices must nevertheless be analyzed separately. [Reported order and destruction, 509 U.S. 544, 548 n.1 (1993)](https://supreme.justia.com/cases/federal/us/509/544/).

**Boundary:** No universal least-restrictive-means requirement for ordinary asset forfeiture, no categorical immunity for lawful expressive inventory, no authority to seize protected stock before adjudication on this rationale, and no future-publication ban. Available relief must respond to the reviewable injury actually caused.

##### Issue 2: Punitive criminal forfeiture and excessiveness

**Stone's Proposed Holding:** This punitive criminal forfeiture is subject to the Excessive Fines Clause. The court must separately examine the extent of the exaction in relation to the offenses supporting it.

**Essential Reasoning and Record Application:** Valid predicates and statutory nexus do not resolve constitutional excessiveness. Examine the interests and supported value taken, the extent and seriousness of wrongdoing, culpability, and the property's role as relevant to a reasoned comparison. These are nonexclusive proposed implementation considerations, not an inherited numerical formula. Correction is limited to the forfeiture that exceeds lawful authority or constitutional bounds.

**Boundary:** No automatic finding of excessiveness, no later Bajakajian formula, and no assumption that the prepared or same-date Austin position is already effective law. The First and Eighth Amendment inquiries remain independent.
'@
$s11 = Replace-CaseBody $s11 'Alexander v. United States' $alexander

# 122. The missing record creates a real condition, not an automatic five-week entitlement.
$s11 = Replace-Once $s11 (@'
DENY the State’s application to vacate the temporary stay.
'@) (@'
Conditionally DENY the State’s application to vacate the temporary stay, if the actual affidavits and effective habeas law establish the substantial grounds and procedural availability described below.
'@)
$s11 = Replace-Once $s11 (@'
Leave the appellate court’s limited stay in place for the review it was entered to permit. Do not order habeas relief, an evidentiary hearing, or a permanent stay through this application. Revalidation against an actual earlier simulated Herrera holding is required before this proposed position is approved for runtime.
'@) (@'
Sustain the approximately five-week interval only on a demonstrated legally substantial and procedurally available basis. If the necessary materials cannot yet be assessed, preserve only an interval genuinely necessary for prompt examination and reconsideration; a missing record does not establish entitlement to the full stay. This application orders neither a writ nor an automatic evidentiary hearing. Check any actual effective simulated Herrera ruling rather than its prepared position or historical comparator.
'@)
$s11 = Replace-Once $s11 (@'
A State does not establish clear abuse merely by identifying a successive petition when a nonfrivolous innocence contention and its procedural availability require examination; this limited appellate review period should not be displaced on the abbreviated presentation.
'@) (@'
A successive capital petition requires substantial grounds under Barefoot and Delo v. Stokes, with procedural availability assessed under McCleskey and the actual effective law. Nonfrivolousness alone is insufficient to sustain the stay. Clear-abuse formulations in separate writings do not replace those requirements or become an unqualified controlling rule.
'@)
$s11 = Replace-Once $s11 (@'
Stone distinguishes permitting a court to examine a claim from accepting the claim. The affidavits are not adjudicated facts, but the State’s analogy and insistence on finality do not by themselves establish that the lower court acted outside its discretion. He would preserve the limited opportunity to determine whether the claim is legally available and factually substantial. An actual controlling simulated holding that eliminates the asserted basis would require a renewed case-specific position, not an Engine-invented exception.
'@) (@'
Identify which assertions in the seven affidavits supply admissible or potentially testable evidence capable of satisfying the applicable merits or gateway rule, why the third petition is not clearly foreclosed, and why the time allowed is necessary for that review. Number of affidavits is not probative sufficiency. Neither finality alone nor a desire to investigate answers the governing standard. The currently supplied packet does not establish those conditions; the disposition remains expressly conditional until the affidavit record and effective law can be evaluated.
'@)

# 123. Standing requires affirmative next-friend predicates.
$s11 = Replace-Once $s11 (@'
He accepts next-friend presentation for this narrow application in the absence of an established representation defect, rather than treating counsel’s assertion as proof of a separate substantive right.
'@) (@'
Under Whitmore, next-friend presentation requires the child’s inability to litigate personally and a representative adequately dedicated to her interests, including a sufficient relationship where required. The child’s age supplies the inability predicate; evaluate the representative’s dedication and authority affirmatively rather than infer standing merely from the absence of a proved defect. Representation does not itself establish the claimed substantive right.
'@)

# Status accurately records this editing authorization without entering simulated outcomes.
function Update-Status([string]$text) {
    $text = [regex]::Replace($text, '(?m)^\*\*Version:\*\*[^\n]*', '**Version:** OT1992 reviewed revision, v1.2.  ')
    $text = [regex]::Replace($text, '(?m)^\*\*Approval Status:\*\*[^\n]*', "**Approval Status:** USER-DIRECTED REVISION. The user authorized implementation of the jurisprudence review; Shaw additionally follows the expressly supplied replacement baseline. This is a proposed Stone position, not a rendered simulated decision.  ")
    $text = [regex]::Replace($text, '(?m)^\*\*Approval Date or Turn:\*\*[^\n]*', '**Revision Authority:** The current user request to make the necessary changes.  ')
    $text = [regex]::Replace($text, '(?m)^\*\*Conditions:\*\*[^\n]*(?:No approved alternative|No separately approved|corrected supplement|No approved alternative)[^\n]*', '**Conditions:** Revalidate material changes in effective simulated law, record, or review scope. This authoring revision enters no simulated judgment.  ')
    $text = $text.Replace('Only the case-specific position below is tendered for approval.', 'The case-specific position below implements the authorized review.')
    $text = [regex]::Replace($text, ' ?filecite[^]+', '')
    return $text
}
$s10 = Update-Status $s10
$s11 = Update-Status $s11

# Synchronize each exact Section II while preserving the combined packet's other sections.
function Sync-Stone([string]$combined,[string]$stone) {
    $caseMatches = [regex]::Matches($stone,'(?ms)^## (?<caption>[^\n]+)\n(?<body>.*?)(?=^## |\z)')
    foreach ($case in $caseMatches) {
        $caption = $case.Groups['caption'].Value
        $body = $case.Groups['body'].Value
        $section = $body.Substring($body.IndexOf('### SECTION II')).Trim()
        $section = [regex]::Replace($section,'\n+---\s*\z','').Trim()
        $pattern = '(?ms)(^## ' + [regex]::Escape($caption) + '\n.*?)^### SECTION II.*?(?=^### SECTION III)'
        if ([regex]::Matches($combined,$pattern).Count -ne 1) { throw "Combined mismatch: $caption" }
        $combined = [regex]::Replace($combined,$pattern,{param($m) $m.Groups[1].Value + $section + "`n`n"})
    }
    return $combined
}
$c10 = Sync-Stone (Read-Packet 'OT_1992CHUNK10.md') $s10
$c11 = Sync-Stone (Read-Packet 'OT_1992CHUNK11.md') $s11
$n10 = Read-Packet 'OT_1992CHUNK10_NEUTRAL.md'
$oldFact = 'Direct review had already reduced one of three death sentences to life without parole.'
$newFact = "Direct review had already reduced the death sentence for the ex-wife's murder to life without parole; the other two death sentences remained."
$n10 = Replace-Once $n10 $oldFact $newFact
$c10 = Replace-Once $c10 $oldFact $newFact
$outputs = @{'OT_1992CHUNK10_STONE.md'=$s10;'OT_1992CHUNK11_STONE.md'=$s11;'OT_1992CHUNK10.md'=$c10;'OT_1992CHUNK11.md'=$c11;'OT_1992CHUNK10_NEUTRAL.md'=$n10}
foreach ($entry in $outputs.GetEnumerator()) {
    [IO.File]::WriteAllText((Join-Path $workspaceDir $entry.Key),$entry.Value.TrimEnd()+"`n",[Text.UTF8Encoding]::new($false))
}
[pscustomobject]@{Cases=15;Files=$outputs.Keys;ComparatorEdits=0}
