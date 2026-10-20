# Thomasson resumption: check validation without Git

**Recorded UTC:** 2026-10-20T20:41:37.593952+00:00

**Status:** Non-Git deterministic checks passed; full Git reference verification remains incomplete.

**Git verification:** Not performed under the user's express no-Git instruction. No Git command was launched. Existing provenance is retained without verification; new provenance is operator-commit-pending. Git reference verification and commitment remain external operator follow-up, not a substantive stopped matter.

**Original tool:** tools/check_term.py

**Tool SHA-256:** 326c640d289d5d64df847ed573cc5999289cf691fa9a92bb814389cdb0508ca7

Original check_term.py exit code: 0. Deferred 36 reference-check calls covering 22 distinct candidate hashes. No inference about their existence is made. Holdings synchronization, runtime split freshness, and all other original checks ran unchanged. The two read-only child checks ran in-process under the process-launch guard and bytecode prohibition.

## Tool output

```text
WARNINGS
 - terms\OT1996\records\Abebe_Jira_v_Negewo_merits_1997-01-14.md: Git reference verification deferred (not checked): 1056244
 - terms\OT1996\records\Andrade_v_Mayfair_Management_Inc_merits_1997-02-26.md: Git reference verification deferred (not checked): 1278633
 - terms\OT1996\records\Atherton_v_FDIC_merits_1997-01-14.md: Git reference verification deferred (not checked): cceeded
 - terms\OT1996\records\Auer_v_Robbins_merits_1997-02-19.md: Git reference verification deferred (not checked): A40385013
 - terms\OT1996\records\Board_of_County_Commissioners_of_Bryan_County_v_Brown_reargument_1997-04-28.md: Git reference verification deferred (not checked): a2d9b20
 - terms\OT1996\records\Board_of_County_Commissioners_of_Bryan_County_v_Brown_reargument_1997-04-28.md: Git reference verification deferred (not checked): 3eb6ac3
 - terms\OT1996\records\Boggs_v_Boggs_merits_1997-06-02.md: Git reference verification deferred (not checked): bd27cdc8
 - terms\OT1996\records\Boggs_v_Boggs_merits_1997-06-02.md: Git reference verification deferred (not checked): 1ca4f0e9
 - terms\OT1996\records\California_v_Roy_summary_review_1996-11-04.md: Git reference verification deferred (not checked): A40385013
 - terms\OT1996\records\Camps_Newfound_Owatonna_v_Town_of_Harrison_merits_1997-05-19.md: Git reference verification deferred (not checked): 19970519
 - terms\OT1996\records\Department_of_State_v_Legal_Assistance_for_Vietnamese_Asylum_Seekers_post_grant_remand_1996-10-21.md: Git reference verification deferred (not checked): A40385013
 - terms\OT1996\records\Doe_v_District_of_Columbia_merits_1997-06-02.md: Git reference verification deferred (not checked): ec5106a
 - terms\OT1996\records\Edmond_v_United_States_merits_1997-05-19.md: Git reference verification deferred (not checked): 19970519
 - terms\OT1996\records\Edwards_v_Balisok_merits_1997-05-19.md: Git reference verification deferred (not checked): 19970519
 - terms\OT1996\records\Ehrlich_v_City_of_Culver_City_DIG_1997-02-18.md: Git reference verification deferred (not checked): e0abdfd
 - terms\OT1996\records\Ehrlich_v_City_of_Culver_City_DIG_1997-02-18.md: Git reference verification deferred (not checked): 88d34e4
 - terms\OT1996\records\Ehrlich_v_City_of_Culver_City_DIG_1997-02-18.md: Git reference verification deferred (not checked): 9d5688a
 - terms\OT1996\records\Hincapie_Nieto_v_INS_merits_1997-05-27.md: Git reference verification deferred (not checked): 012028153
 - terms\OT1996\records\Ingebretsen_v_Jackson_Public_School_District_merits_1997-03-19.md: Git reference verification deferred (not checked): A40386004
 - terms\OT1996\records\INS_v_Yueh_Shaio_Yang_merits_1996-11-13.md: Git reference verification deferred (not checked): A40385013
 - terms\OT1996\records\In_re_Gaydos_filing_and_writ_disposition_1996-12-02.md: Git reference verification deferred (not checked): A40385014
 - terms\OT1996\records\In_re_Vey_financial_leave_1997-04-14.md: Git reference verification deferred (not checked): A40386013
 - terms\OT1996\records\In_re_Vey_financial_leave_1997-04-14.md: Git reference verification deferred (not checked): e0abdfd
 - terms\OT1996\records\In_re_Vey_financial_leave_1997-04-14.md: Git reference verification deferred (not checked): ef97686
 - terms\OT1996\records\Lopez_v_Monterey_County_merits_1996-11-06.md: Git reference verification deferred (not checked): A40385013
 - terms\OT1996\records\Lynce_v_Mathis_threshold_1997-02-19.md: Git reference verification deferred (not checked): e0abdfd
 - terms\OT1996\records\Lynce_v_Mathis_threshold_1997-02-19.md: Git reference verification deferred (not checked): 88d34e4
 - terms\OT1996\records\Lynce_v_Mathis_threshold_1997-02-19.md: Git reference verification deferred (not checked): 9d5688a
 - terms\OT1996\records\Lynce_v_Mathis_threshold_1997-02-19.md: Git reference verification deferred (not checked): A40385013
 - terms\OT1996\records\Ohio_v_Robinette_merits_1996-11-18.md: Git reference verification deferred (not checked): A40385013
 - terms\OT1996\records\Robinson_v_City_of_Edmond_merits_1997-03-31.md: Git reference verification deferred (not checked): A40385013
 - terms\OT1996\records\Thomasson_v_Perry_merits_1997-06-09.md: Git reference verification deferred (not checked): 803cc547
 - terms\OT1996\records\Thomasson_v_Perry_merits_1997-06-09.md: Git reference verification deferred (not checked): 244a75ac
 - terms\OT1996\records\Uhlrig_v_Harder_merits_1997-02-18.md: Git reference verification deferred (not checked): A40386007
 - terms\OT1996\records\United_States_v_Brockamp_merits_1997-02-18.md: Git reference verification deferred (not checked): A40385013
 - terms\OT1996\records\Wright_v_MetroHealth_Medical_Center_merits_1997-03-03.md: Git reference verification deferred (not checked): 1301712
Non-Git deterministic checks passed: OT1996; 36 warning(s)
```
