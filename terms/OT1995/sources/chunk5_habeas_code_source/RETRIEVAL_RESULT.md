# Bounded official 1994 Code recovery attempt

**Result:** Neither complete 1994 28 U.S.C. §2253 nor §1651 was recovered. No operative statutory text, transition note or current-law substitute was extracted. This result concerns the two bounded routes attempted; it is not a finding that the sources do not exist elsewhere.

## Route 1: GovInfo complete Title 28 package

- Requested `https://www.govinfo.gov/content/pkg/USCODE-1994-title28/pdf/USCODE-1994-title28.pdf`.
- The response was HTTP 200, `text/html`, 44,172 bytes, titled **“Page Not Found | GovInfo”**. Its bytes did not begin with `%PDF`.
- Checked the same package's official metadata locator, `https://www.govinfo.gov/metadata/pkg/USCODE-1994-title28/mods.xml`.
- That request returned the identical soft-404 HTML, not package metadata or an authenticated volume locator.
- Both actual responses were retained as `GOVINFO_FULL_TITLE_RESPONSE.html` and `GOVINFO_TITLE28_MODS_RESPONSE.txt`. Each has SHA-256 `ab214ce9f7a706cc4ee93703502f950222090c2547e47fafd75a299545919743`.

No section-specific GovInfo locator from the prior failed search was repeated.

## Route 2: Library of Congress catalog alternative

- Requested the constructed complete-title catalog locator `https://www.loc.gov/item/uscode1994-028000000/?fo=json`; response: HTTP 403 Forbidden.
- Checked the same item's ordinary HTML representation, `https://www.loc.gov/item/uscode1994-028000000/`; response: HTTP 404 Not Found.
- This locator was not authenticated as an existing catalog item, and no official volume or section content was obtained. No PDF was inferred from its naming pattern.

## Receipt and scope

`RETRIEVAL_RECEIPT.json` records all four exact requests and observed responses. The retained HTML files are failure evidence, not legal sources. The attempt stopped after these two alternate source routes. No OLRC request was repeated, no neutral packet or current-case position was read or written, and no Git operation was performed.

The exact 1994 sections and any date-relevant transition-note coverage therefore remain unverified by this task. No statement about April 9, 1996 effective-law freshness follows from these failures.

## Precisely directed full-HTML follow-up

After the bounded attempt, the operator supplied the successful complete-Title-42 HTML pattern and directed one exact analogous request: `https://www.govinfo.gov/content/pkg/USCODE-1994-title28/html/USCODE-1994-title28.htm`.

That exact request also returned HTTP 200, `text/html`, 44,172 bytes, titled **“Page Not Found | GovInfo”**, with the same SHA-256 `ab214ce9f7a706cc4ee93703502f950222090c2547e47fafd75a299545919743`. No §2253 or §1651 heading candidate appeared. The response is retained as `USCODE-1994-title28.htm` solely as failure evidence; despite that filename, it is not Code text.

The receipt now records five requests. No section extraction was made, and the follow-up stopped at this failure as directed.
