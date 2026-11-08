# Final source verification

The core reading receipt is `CORE_RECORD_REVIEW.md`; separate complete reviews are `APPENDIX_REVIEW.md` and `BURTON_TESTIMONY_REVIEW.md`. These receipts describe actual reading boundaries and do not claim a complete reading of every underlying trial volume or omitted exhibit.

The final integrity check matched all 14 retained archive PDF/OCR files against their Internet Archive metadata MD5 values. There were no mismatches. Every page image in the 98-page bounded Miami witness PDF matched the corresponding image in the retained original trial volumes. The core excerpt script stores each copied OCR body's source offsets and SHA-256 value in the core receipt.

The content-restriction check covered 157 source, derivative, image, and task-script files within the authorized task paths. It found no prohibited content or machine-path links. The historical core sources remain in the control directory. Only the bounded neutral artifacts below were sent to the clean validator.

## Additional official statute

After completion of the core review, the clean validator requested the exact timing provision omitted in the printed appendix. The official Florida Senate 2000 version of section 102.168 was retrieved at https://www.flsenate.gov/laws/statutes/2000/102.168 . The complete section, subsections (1)-(8), history, and note were read. Its section (2) contains both the ten-day certification and five-day post-protest alternatives and the later-of-the-two qualification.

The official section's HTML body was copied mechanically; navigation and script material were excluded. Text was extracted by HTML parsing, with entities decoded and paragraph boundaries displayed as newlines. No statutory wording was retyped or supplied from memory. Retained neutral files are `gore-florida-statute-102-168-2000.html` and `gore-florida-statute-102-168-2000.txt`. The extracted body SHA-256 is `11cc2b31af2c63ae5bf30913e0f0fbd39b82a8eab10a11fc92b7774e266811c8`. This official source supplements the defective appendix printing; it does not silently alter that source.

## Neutral handoff

All files below are in `terms/OT2000/sources/chunk1-neutral/`:

- `gore-record-facts.md`: bounded factual and party-argument addendum, with evidentiary qualifications.
- `gore-main-brief-excerpts.txt`: exact selected OCR bodies; final SHA-256 `ecdfa6195ffcd62aa863ef98660683dac8c07626e23387dc64cc0b5edbb0773a`.
- `gore-miami-witnesses-2000-12-03.pdf`: complete Spencer, Spargo, and Lampkin examinations and associated cross-examinations, printed pages 460-523 and 531-564; SHA-256 `0a70046adb98f5807fd2b554ab204c315c125e7ef01533e3e6e354dc2c27ce00`.
- `gore-clarification-leave-order-2000-12-08.txt`: operative paragraph from the official state order denying leave to file clarification.
- `gore-appendix-facts.md`: the complete appendix review's bounded factual findings and limits.
- `gore-burton-testimony-2000-12-02.txt`: mechanically copied complete Burton examination.
- The two official statutory source files named above.

Independent clean validation was requested and is in progress. No factual addition from these files should bypass that validation. No adjudication, non-Stone vote, coalition, reconciliation, or assembly was performed by this source-review context.
