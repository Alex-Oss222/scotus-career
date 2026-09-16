# OT1992 chronology and dependency review

This is an audit of the source packets before reorganization, not an Engine record. It records no votes, holdings, outcomes, or effective simulated law. Source paths in the companion JSON identify provenance under the former numbering and are not runtime load instructions.

## Inventory and date findings

The source case indexes identify 51 original matters and 72 additional matters: 123 distinct intended modules. The stable combined order is the original 51-case list followed by the additional 72-case list, sorted by historical event date while preserving each list's same-date sequence. All listed event dates survive this review; no substitute docket or different matter is needed.

The review compared the dated inventory against the [Cornell Project Hermes OT1992 opinion index](https://www.law.cornell.edu/supct/party.php?begin=19920830&end=19930630&party=1) and the Government Publishing Office's volume-context listings for [506 U.S.](https://www.govinfo.gov/app/details/USREPORTS-506/USREPORTS-506-BackMatter/context), [508 U.S.](https://www.govinfo.gov/app/details/USREPORTS-508/USREPORTS-508-BackMatter/context), and [509 U.S.](https://www.govinfo.gov/app/details/USREPORTS-509/USREPORTS-509-BackMatter/context). The published judicial texts and individual decree metadata resolve unusual dispositions and metadata conflicts. The five A-docket matters receive a separate application audit.

**Resolved metadata conflict:** GPO's 508-volume context lists Smith v. United States, 508 U.S. 223, as May 24. The actual Court opinion's dateline is **June 1, 1993**, matching the existing packet and Cornell's term index. Retain June 1 and docket 91-8674. This is distinct from the Antarctica FTCA case, 91-1538, 507 U.S. 197, March 8. [Smith opinion](https://www.law.cornell.edu/supct/html/91-8674.ZO.html).

| Matter | Docket | Retained event date | Historical action/source check |
|---|---|---|---|
| Martin v. District of Columbia Court of Appeals | 92-5584 | 1992-11-02 | IFP filing motion and prospective filing restriction; [GPO](https://www.govinfo.gov/app/details/USREPORTS-506/USREPORTS-506-1) |
| Montana v. Imlay | 91-687 | 1992-11-03 | Per curiam writ disposition; [GPO](https://www.govinfo.gov/app/details/USREPORTS-506/USREPORTS-506-5) |
| Hadley v. United States | 91-6646 | 1992-11-16 | Per curiam writ disposition; [Court text](https://www.law.cornell.edu/supct/html/91-6646.ZPC.html) |
| Dobbs v. Zant | 92-5579 | 1993-01-19 | Summary per curiam; [Court text](https://www.law.cornell.edu/supct/html/92-5579.ZPC.html) |
| United States v. Nachtigal | 92-609 | 1993-02-22 | Summary per curiam; [GPO](https://www.govinfo.gov/app/details/USREPORTS-507/USREPORTS-507-1) |
| United States v. Louisiana, supplemental decree | 9, Original | 1993-02-22 | Supplemental decree action, not one of the earlier underlying boundary opinions; [GPO](https://www.govinfo.gov/app/details/USREPORTS-507/USREPORTS-507-7) |
| Delo v. Lashley | 92-409 | 1993-03-08 | Summary per curiam; [Court writing dateline](https://www.law.cornell.edu/supct/html/92-409.ZA.html) |
| Demos v. Storrie | 92-6846 | 1993-03-08 | IFP filing motion and filing restriction; [GPO](https://www.govinfo.gov/app/details/USREPORTS-507/USREPORTS-507-290) |
| United States v. McDermott | 91-1229 | 1993-03-24 | Signed opinion; [Court text](https://www.law.cornell.edu/supct/html/91-1229.ZO.html) |
| Delaware v. New York | 111, Original | 1993-03-30 | Opinion on original-action exceptions; [GPO](https://www.govinfo.gov/app/details/USREPORTS-507/USREPORTS-507-490) |
| Conroy v. Aniskoff | 91-1353 | 1993-03-31 | Signed opinion; [Court text](https://www.law.cornell.edu/supct/html/91-1353.ZO.html) |
| United States v. Green | 91-1521 | 1993-04-05 | Mootness/writ disposition; dated in [Project Hermes index](https://www.law.cornell.edu/supct/party.php?begin=19920830&end=19930630&party=1) |
| Nebraska v. Wyoming | 108, Original | 1993-04-20 | Opinion on original-action decree proceedings; dated in [Project Hermes index](https://www.law.cornell.edu/supct/party.php?begin=19920830&end=19930630&party=1) |
| United States v. Padilla | 92-207 | 1993-05-03 | Argued case with per curiam action; [Court text](https://www.law.cornell.edu/supct/html/92-207.ZPC.html) |
| El Vocero de Puerto Rico v. Puerto Rico | 92-949 | 1993-05-17 | Summary per curiam; [Court text](https://www.law.cornell.edu/supct/html/92-949.ZPC.html) |

The original-jurisdiction category applies to the three expressly Original dockets above. Mississippi v. Louisiana, 91-1158, remains appellate review of the district court's jurisdiction; a boundary subject does not change its docket into an original action. United States v. California, 91-2003, is similarly not an Original docket. Martin and Demos must retain their filing-application posture rather than the obsolete index's generic MERITS label.

## Dependency review

All 123 modules were scanned through Sections I and II for named same-term references, date language, source-law qualifications, and dependency fields. The 39 non-generic dependency fields are preserved in `chronology_dependency_rows.json`; they include temporal prohibitions and record conditions as well as forward references. Candidate short-name matches were individually reviewed to exclude unrelated older authorities: Graham v. Connor, Shaw v. Delta Air Lines, Johnson v. Zerbst, Martin v. Ohio, Withrow v. Larkin, and the earlier Montana decisions are not citations to similarly named OT1992 matters.

No operative backward import of later OT1992 law was identified in the existing Sections I or II. Express future references are correctly framed as exclusions or later downstream effects: Hadley excludes Daubert; Growe excludes Voinovich and Shaw; Voinovich excludes Shaw; Graham excludes Johnson as entering law; Antoine excludes Buckley; and Shaw does not treat same-date Daubert as earlier effective law. These restrictions should remain intact.

### Necessary organizational updates

1. Shaw's dependency field still names old CHUNK3 for Growe/Voinovich and old CHUNK7 for Northeastern Florida. Replace these numerical locators with the unchanged event dates or the validated new chunk locators. Do not revise the corrected doctrinal, standing, remedial, or Stone-position text.
2. Add a forward dependency check from **FCC v. Beach Communications (June 1)** to **Heller v. Doe (June 24)**. Heller's old placeholder says no case-specific earlier matter, but the merged inventory now includes the related rational-basis case. Load only an actual earlier effective simulated rule, preserving its economic-classification context and Heller's distinct liberty, participation, burden, and preservation questions. This relationship is confirmed by the [historical Heller opinion](https://www.law.cornell.edu/supct/html/92-351.ZO.html); that historical outcome itself supplies no simulation authority.
3. Add a forward dependency check from **Antoine v. Byers & Anderson (June 7)** to **Buckley v. Fitzsimmons (June 24)** for the functional approach to absolute immunity and burden of justification. Preserve the distinction between court reporting and prosecutorial functions. The [historical Buckley opinion](https://www.law.cornell.edu/supct/html/91-7849.ZO.html) confirms the relationship; its historical reasoning remains quarantined.
4. Retain all existing case-specific gates, including Herrera before Blair, Graham/Fretwell/Brecht before Gilmore, Nobelman before Rake, Martin before Demos, Mertens before Demisay, and McNeil/Lincoln before Darby. Adding the second inventory does not itself make any proposal or comparator effective law.

### Material relationships across the combined run

The arrows below indicate dates and conditional relevance, not a determination that the earlier case adopted a particular rule.

| Earlier eligible event(s) | Later event | Subject and scope limit |
|---|---|---|
| Soldal, Dec 8 | Farrar, Dec 14; Leatherman, Mar 3; Padilla, May 3; Dickerson, Jun 7 | Respect any actually adopted relevant holding; Fourth Amendment coverage does not supply fees, a pleading rule, vicarious privacy rights, or expanded frisk authority. |
| Martin, Nov 2 | Rowland, Jan 12; Demos, Mar 8 | Filing abuse and restrictions; association eligibility under §1915 is a distinct question. |
| Farrar, Dec 14 | Bray, Jan 13 | Fees only within the earlier holding's actual scope. |
| Growe, Feb 23 | Voinovich, Mar 2; Shaw, Jun 28 | Redistricting responsibility and applicable §2 predicates; no assumed historical disposition. |
| Voinovich, Mar 2; Northeastern Florida, Jun 14 | Shaw, Jun 28 | Preserve distinct dilution, racial-classification, and competitive-injury inquiries. |
| Puerto Rico Aqueduct, Jan 12 | Saudi Arabia, Mar 23; United States v. California, Apr 26 | Distinct sovereign-immunity and substantive statutory sources. |
| Greater Washington Board of Trade, Dec 14; Boston Harbor, Mar 8 | CSX, Apr 21 | Preemption remains statute-specific. |
| Itel, Feb 23 | United States v. California, Apr 26 | Foreign-commerce limits do not create a federal refund claim. |
| Herrera and Graham, Jan 25 | Lashley, Mar 8 | Apply only actually adopted capital/habeas propositions. |
| Cincinnati, Mar 24 | Edenfield, Apr 26; Edge Broadcasting, Jun 25 | Commercial-speech review; actual Edenfield holdings also require screening at Edge. |
| Brecht, Apr 21; Zafiro, Jan 25 | Olano, Apr 26 | Collateral harmless error and instruction principles do not replace Rule52(b). |
| Brecht, Apr 21 | Sullivan, Jun 1; Gilmore, Jun 7 | Preserve direct/collateral review and Teague sequencing. |
| Graham and Fretwell, Jan 25 | Gilmore, Jun 7 | Retroactivity and prejudice questions remain distinct. |
| Graham, Jan 25 | Johnson, Jun 24 | Actual mitigation/retroactivity holding, if any. |
| Negonsott, Feb 24 | Sac and Fox Nation, May 17 | Kansas criminal-jurisdiction statute does not establish state taxing power. |
| Greater Washington Board of Trade, Dec 14 | Mertens, Jun 1 | ERISA preemption does not create monetary remedies or defendants. |
| Lincoln, May 24; Stinson, May 3 | Good Samaritan, Jun 7 | Statutory and administrative contexts remain separate. |
| Nobelman, Jun 1 | Rake, Jun 7 | Home-mortgage rights versus interest/present-value rules. |
| Lamb's Chapel, Jun 7; Lukumi, Jun 11 | Zobrest, Jun 18 | Forum equal access and targeting do not decide public funding or restore unpresented claims. |
| Spectrum Sports, Jan 25 | Brooke Group, Jun 21 | Attempted-monopolization elements do not automatically become Robinson-Patman elements. |
| Mertens, Jun 1 | Demisay, Jun 14 | ERISA remedies do not create LMRA §302(e) authority. |
| McNeil, May 17; Lincoln, May 24 | Darby, Jun 21 | FTCA exhaustion does not add an APA exhaustion requirement. |
| FCC v. Beach, Jun 1 | Heller, Jun 24 | Actual rational-basis propositions; distinct liberty and procedural questions remain. |
| Antoine, Jun 7 | Buckley, Jun 24 | Actual functional-immunity rule; distinct functions and preserved scope remain. |
| Hazen Paper, Apr 20 | Hicks, Jun 25 | An unlawful criterion versus another motive does not settle TitleVII burden allocation. |
| TXO, Jun 25 | Austin, Jun 28 | Private punitive damages and government forfeiture have distinct constitutional sources. |
| Fabe, Jun 11; Leatherman, Mar 3 | Hartford Fire, Jun 28 | Separate McCarran-Ferguson clauses and pleading scope must remain distinct. |
| Herrera, Jan 25 | Blair, Jul 21 | Actual innocence/habeas doctrine is material to review of the lower-court stay. |

### Same-date sequences

Brecht precedes Withrow on April 21 under the preexisting list sequence. Withrow may use a Brecht rule only if the simulation establishes that the completed decision became effective before Withrow's event; otherwise use independent entering law. Their cognizability and harmless-error questions remain separate. The stable combined order also places Austin before Alexander on June 28. Alexander's existing same-day gate remains essential: calendar order, pagination, prepared briefs, and chunk position alone are not an actual effective decision record. No change in the ordering of either pair is required, and neither relationship warrants a smaller chunk by itself.

## Baseline and records limitation

The original packet describes an adopted historical baseline entering OT1992. The later additional packet describes a linked repository frozen at the OT1991 opening and expressly requires authorization or actual records for post-divergence Supreme Court law. This is a source-state difference, not a reason to delete corrected brief material or adjudicate missing cases. A consolidated runtime manifest should state the distinction, require the actual authorized term-opening state, and prevent a later packet's file location from silently changing the legal baseline of any matter. There are no local foundation, state, or completed Engine record files in the supplied workspace inventory. Remote registers are cited in the prior manifest; this audit does not certify their present contents or merge their chronology into an invented completed Term.

## Reorganization checks to apply after generation

For every new chunk boundary, verify the last event date does not exceed the next first event date. All chunks normally contain twelve matters and the final chunk contains three. Evaluate dependencies at each individual event, including a same-day boundary if one occurs. Index order and file membership do not establish legal effectiveness. Regenerated NEUTRAL, STONE, and COMPARATOR exports must reproduce only the corresponding sections of the new assigned modules, and obsolete manifests must not remain live routing documents.
