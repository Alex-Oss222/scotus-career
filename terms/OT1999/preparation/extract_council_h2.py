from pathlib import Path
import hashlib

base = Path(__file__).resolve().parent
source = base / 'usc-1999-42-1395cc.txt'
text = source.read_text(encoding='utf-8')
start = text.index('(h) Dissatisfaction with determination of Sec-')
end = text.index('(i) Intermediate sanctions for psychiatric hos-', start)
excerpt = text[start:end].rstrip()
assert '(2) An institution or agency is not entitled to' in excerpt
assert 'same underlying facts' in excerpt
url = 'https://www.govinfo.gov/content/pkg/USCODE-1999-title42/pdf/USCODE-1999-title42-chap7-subchapXVIII-partD-sec1395cc.pdf'
pdfhash = hashlib.sha256((base / 'usc-1999-42-1395cc.pdf').read_bytes()).hexdigest()
out = '''# Illinois Council — exact preexisting statutory extract

Extraction date: October 31, 2026. Source-only artifact; fresh neutral validation is required before adding readiness. No legal application, current-matter result, rationale, lineup or commitment is supplied here.

The following is copied mechanically from the official 1999 United States Code, Title 42, section 1395cc(h), printed pages 2104–2105. The source's line wrapping, print hyphenation and intervening page header are preserved. Both paragraphs are included so the reference in paragraph (1) and the text of paragraph (2) can be read together.

Source: [1999 United States Code, section 1395cc](URL).

Downloaded official PDF SHA-256: `HASH`.

```text
EXCERPT
```

The complete downloaded statute is retained as `usc-1999-42-1395cc.pdf` with its extracted text `usc-1999-42-1395cc.txt` in this preparation directory. No current-matter opinion or search result is included in this artifact. The initially attempted current Part E path returned an error page and was replaced by the correct historical Part D source; no error-page content supplies authority.
'''.replace('URL', url).replace('HASH', pdfhash).replace('EXCERPT', excerpt)
(base / 'OT_1999CHUNK3_COUNCIL_STATUTORY_EXTRACT.md').write_text(out, encoding='utf-8')
print(pdfhash)
print('Exact section 1395cc(h)(1)-(2) copied; no legal application supplied.')
