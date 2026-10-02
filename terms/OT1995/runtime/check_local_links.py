"""Bounded, read-only Markdown target/anchor consistency check for OT1995.

No Git, network, recursive tree walk, or automatic source edit. Target files are
opened only to extract headings/explicit anchors, never to interpret their text.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[3]
TERM = ROOT / 'terms' / 'OT1995'
LOCKED = ROOT / 'stone'
WORKSPACE_NAMES = ('manifest.md', 'ledger.md', 'continuity.md', 'neutral-projection.md')
RENDER_NAME = 'OT_1995CHUNK1.md'


def path_key(path: Path) -> str:
    return str(path).replace('\\', '/').rstrip('/').casefold()


def within(path: Path, parent: Path) -> bool:
    a, b = path_key(path), path_key(parent)
    return a == b or a.startswith(b + '/')


def label(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def mask_code(text: str, inline: bool = True) -> str:
    """Preserve offsets/newlines while ignoring fenced blocks and inline code."""
    rows = text.splitlines(keepends=True)
    marker = None
    length = 0
    masked = []
    for row in rows:
        opening = re.match(r'^ {0,3}(`{3,}|~{3,})', row)
        if marker is not None:
            closing = re.match(r'^ {0,3}' + re.escape(marker) + r'{' + str(length) + r',}\s*$', row.rstrip('\r\n'))
            masked.append(re.sub(r'[^\r\n]', ' ', row))
            if closing:
                marker = None
            continue
        if opening:
            marker, length = opening[1][0], len(opening[1])
            masked.append(re.sub(r'[^\r\n]', ' ', row))
        else:
            masked.append(row)
    value = ''.join(masked)
    if inline:
        value = re.sub(r'(`+)(?!`)(.*?)(?<!`)\1(?!`)',
                       lambda m: re.sub(r'[^\r\n]', ' ', m[0]), value, flags=re.S)
    return value


def closing_index(text: str, start: int, opening: str, closing: str) -> int | None:
    depth = 0
    escaped = False
    for i in range(start, len(text)):
        c = text[i]
        if escaped:
            escaped = False
            continue
        if c == '\\':
            escaped = True
        elif c == opening:
            depth += 1
        elif c == closing:
            depth -= 1
            if depth == 0:
                return i
    return None


def destination(value: str) -> str | None:
    value = value.strip()
    if value.startswith('<'):
        end = value.find('>')
        return value[1:end] if end >= 0 else None
    # Bare destination ends at unescaped whitespace; the remainder is a title.
    hit = re.match(r'(?:\\.|[^\s])+', value)
    return hit[0] if hit else ''


def normalize_ref(value: str) -> str:
    return ' '.join(value.split()).casefold()


def extract_links(text: str) -> tuple[list[dict], list[dict]]:
    visible = mask_code(text)
    links, warnings = [], []
    definitions = {}
    spans = []
    for m in re.finditer(r'^ {0,3}\[([^\]\n]+)\]:[ \t]*(.*)$', visible, re.M):
        if m[1].startswith('^'):
            continue
        href = destination(m[2])
        if href is not None:
            definitions[normalize_ref(m[1])] = href
            spans.append((m.start(), m.end()))
            links.append(dict(target=href, line=visible.count('\n',0,m.start())+1, kind='reference-definition'))
    i = 0
    while i < len(visible):
        if visible[i] != '[' or (i and visible[i-1] == '\\'):
            i += 1
            continue
        skip = next((b for a,b in spans if a <= i < b), None)
        if skip is not None:
            i = skip
            continue
        end = closing_index(visible, i, '[', ']')
        if end is None:
            i += 1
            continue
        line = visible.count('\n',0,i)+1
        after = end+1
        if after < len(visible) and visible[after] == '(':
            finish = closing_index(visible, after, '(', ')')
            if finish is None:
                warnings.append(dict(line=line,kind='unclosed-inline-destination'))
                i = after+1
                continue
            href = destination(visible[after+1:finish])
            if href is not None:
                links.append(dict(target=href,line=line,kind='image' if i and visible[i-1]=='!' else 'inline'))
            else:
                warnings.append(dict(line=line,kind='unclosed-angle-destination'))
            i = finish+1
            continue
        # Definitions are checked once. Reference usages need not duplicate them.
        if after < len(visible) and visible[after] == '[':
            finish = closing_index(visible,after,'[',']')
            if finish is not None:
                ref = normalize_ref(visible[after+1:finish] or visible[i+1:end])
                if ref and ref not in definitions:
                    warnings.append(dict(line=line,kind='undefined-reference',reference=ref))
                i=finish+1
                continue
        i=end+1
    for m in re.finditer(r'<((?:https?://|mailto:)[^<>\s]+)>',visible,re.I):
        links.append(dict(target=m[1],line=visible.count('\n',0,m.start())+1,kind='autolink'))
    for m in re.finditer(r'<(?:a|img)\b[^>]*?\b(?:href|src)\s*=\s*([\"\'])(.*?)\1',visible,re.I|re.S):
        links.append(dict(target=m[2],line=visible.count('\n',0,m.start())+1,kind='html'))
    return links,warnings


def heading_text(value: str) -> str:
    value = re.sub(r'!?\[([^\]]*)\]\([^\n]*?\)',r'\1',value)
    value = re.sub(r'<[^>]+>','',value)
    value = re.sub(r'`+([^`]*?)`+',r'\1',value)
    value = re.sub(r'(?<!\w)_([^_]+)_(?!\w)',r'\1',value)
    value = re.sub(r'\\([!"#$%&\'()*+,\-./:;<=>?@\[\]\\^_`{|}~])',r'\1',value)
    return html.unescape(value).strip()


def slug(value: str) -> str:
    value = heading_text(value).lower()
    return ''.join('-' if c.isspace() else c for c in value
                   if c.isspace() or c in '-_' or unicodedata.category(c)[0] in 'LN')


def anchors(text: str) -> set[str]:
    visible = mask_code(text,inline=False)
    result = set()
    for m in re.finditer(r'<[^>]+\b(?:id|name)\s*=\s*([\"\'])(.*?)\1',visible,re.I|re.S):
        result.add(html.unescape(m[2]))
    used = set()
    rows = visible.splitlines()
    for index,row in enumerate(rows):
        atx = re.match(r'^ {0,3}#{1,6}[ \t]+(.*)$',row)
        heading = None
        if atx:
            heading = re.sub(r'[ \t]+#+[ \t]*$','',atx[1])
        elif index and re.match(r'^ {0,3}(?:=+|-+)[ \t]*$',row) and rows[index-1].strip():
            previous=rows[index-1]
            if not re.match(r'^\s*(?:#|[-*+]\s|\d+\.\s|[>|])',previous):
                heading=previous
        if heading is None:
            continue
        base = slug(heading)
        candidate, number = base, 0
        while candidate in used:
            number += 1
            candidate = base+'-'+str(number)
        used.add(candidate)
        result.add(candidate)
    return result


def resolve_target(source: Path, raw: str) -> tuple[str, Path | None, str]:
    value = html.unescape(raw.strip())
    value = re.sub(r'\\([() ])',r'\1',value)
    # A drive prefix is local, not a URI scheme. Network/UNC targets are not probed.
    if value.startswith(('//','\\\\')):
        return 'external-network-not-fetched',None,''
    if not re.match(r'^[A-Za-z]:[\\/]',value):
        scheme=urlsplit(value).scheme
        if scheme:
            return 'external-url-not-fetched',None,''
    pathpart, sep, fragment = value.partition('#')
    fragment=unquote(fragment) if sep else ''
    pathpart=unquote(pathpart.split('?',1)[0]).replace('\\','/')
    if not pathpart:
        candidate=source
    elif pathpart.startswith('/') and not re.match(r'^/[A-Za-z]:/',pathpart):
        candidate=ROOT/pathpart.lstrip('/')
    elif re.match(r'^/[A-Za-z]:/',pathpart):
        candidate=Path(pathpart[1:])
    elif re.match(r'^[A-Za-z]:/',pathpart):
        candidate=Path(pathpart)
    else:
        candidate=source.parent/pathpart
    # Lexical normalization rejects a directly named locked target before resolve.
    import os
    lexical=Path(os.path.abspath(candidate))
    if within(lexical,LOCKED):
        return 'locked-target-rejected',lexical,fragment
    resolved=lexical.resolve(strict=False)
    if within(resolved,LOCKED):
        return 'locked-target-rejected',resolved,fragment
    if not within(resolved,ROOT):
        return 'outside-workspace-not-inspected',resolved,fragment
    if within(resolved,TERM):
        return 'current-term-local',resolved,fragment
    if within(resolved,ROOT/'foundation') or within(resolved,ROOT/'state') or within(resolved,ROOT/'terms'):
        return 'legacy-baseline-local',resolved,fragment
    return 'repository-local',resolved,fragment


def self_test() -> None:
    sample='''# Plain title
## [Case name](https://example.test/path) — § 3
## Plain title
## Plain title
<a id="kept"></a>
```
## hidden
[ignored](missing.md)
```
[ok](../record.md#plain-title)
[space](<my file.md#title> "title")
[nested](asset_(old).pdf)
[r]: target.md#anchor
[use][r]
`[ignored](again.md)`
'''
    found,warnings=extract_links(sample)
    assert [x['target'] for x in found]==['target.md#anchor','https://example.test/path','../record.md#plain-title','my file.md#title','asset_(old).pdf']
    assert not warnings
    a=anchors(sample)
    assert {'plain-title','plain-title-1','plain-title-2','case-name---3','kept'} <= a
    assert 'hidden' not in a
    kind,_,_=resolve_target(TERM/'records/test.md','../../../stone/never-open.md')
    assert kind=='locked-target-rejected'


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report-name',default='OT_1995CHUNK1_LINK_CHECK',help='Simple basename under freeze; no path separators.')
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]+',args.report_name):
        parser.error('Report name must be a simple safe basename.')
    if args.self_test:
        self_test()
    sources=sorted((TERM/'records').glob('*.md'))  # Only this one explicit, nonrecursive directory.
    required=[TERM/'workspace'/name for name in WORKSPACE_NAMES]
    sources += [p for p in required if p.is_file()]
    render=TERM/'render-inputs'/RENDER_NAME
    if render.is_file():
        sources.append(render)
    report=dict(scope='Canonical OT1995 Records, four named workspace projections, and current chunk1 Render Input if present; no recursive enumeration',generated_utc=datetime.now(timezone.utc).isoformat(),network_used=False,git_used=False,source_edits=False,locked_targets_inspected=False,inputs=[],missing_required_inputs=[label(p) for p in required if not p.is_file()],optional_render_input=dict(path=label(render),present=render.is_file()),links=[],parse_warnings=[],anchor_method='GitHub-style rendered heading slugs with duplicate suffixes plus explicit HTML id/name; Markdown heading extraction only',limitations=['External URLs and network paths are catalogued without fetching.','Fragments of non-Markdown targets are reported as not checked, not missing headings.','Outside-workspace targets are not inspected.','Generated-heading slugs are a local consistency approximation; unusual inline HTML or Markdown extensions may require manual anchor review.'])
    cache={}
    for source in sources:
        raw=source.read_bytes()
        content=raw.decode('utf-8-sig')
        report['inputs'].append(dict(path=label(source),sha256=hashlib.sha256(raw).hexdigest()))
        extracted,warnings=extract_links(content)
        report['parse_warnings'] += [dict(source=label(source),**w) for w in warnings]
        for item in extracted:
            kind,target,fragment=resolve_target(source,item['target'])
            row=dict(source=label(source),**item,category=kind,fragment=fragment)
            if target is not None:
                row['resolved_target']=label(target)
            if kind.startswith('external-'):
                row['status']='not-fetched'
                row['legacy_baseline_url']=bool(re.search(r'github\.com/[^/]+/[^/]+/blob/[^/]+/(?:state|foundation|terms/OT(?!1995/)[0-9]{4})/',item['target']))
            elif kind in ('locked-target-rejected','outside-workspace-not-inspected'):
                row['status']='rejected-without-content-inspection'
            elif not target.exists():
                row['status']='missing-target'
            elif not fragment:
                row['status']='target-exists'
            elif target.suffix.lower() not in ('.md','.markdown'):
                row['status']='target-exists-nonmarkdown-fragment-not-checked'
            elif not target.is_file():
                row['status']='fragment-target-not-file'
            else:
                try:
                    if target not in cache:
                        cache[target]=anchors(target.read_text(encoding='utf-8-sig'))
                    row['status']='anchor-exists' if fragment in cache[target] else 'missing-anchor'
                except (OSError,UnicodeError) as exc:
                    row['status']='anchor-read-error'
                    row['error']=type(exc).__name__
            report['links'].append(row)
    counts=Counter((r['category'],r['status']) for r in report['links'])
    report['counts']=[dict(category=c,status=s,count=n) for (c,s),n in sorted(counts.items())]
    failures={'missing-target','missing-anchor','fragment-target-not-file','anchor-read-error','rejected-without-content-inspection'}
    report['issues']=[r for r in report['links'] if r['status'] in failures]
    report['current_term_issues']=[r for r in report['issues'] if r['category']=='current-term-local']
    report['legacy_baseline_issues']=[r for r in report['issues'] if r['category']=='legacy-baseline-local']
    report['external_urls_not_fetched']=len([r for r in report['links'] if r['category'].startswith('external-')])
    report['passed']=not report['issues'] and not report['missing_required_inputs']
    dest=TERM/'freeze'/args.report_name
    dest.with_suffix('.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    lines=['# OT1995 chunk1 — bounded local link and anchor check','',f"Status: {'PASS' if report['passed'] else 'ISSUES FOUND'} for the inputs present.",'',f"Inputs checked: {len(sources)}. Links catalogued: {len(report['links'])}. External URLs/network targets not fetched: {report['external_urls_not_fetched']}.",f"Current Render Input present: {report['optional_render_input']['present']}; absence before generation is pending scope, not a missing link.",'','No Git, network, source edits, recursive directory walk or locked-target content inspection.','', '## Counts','', '| Category | Status | Count |','|---|---|---|']
    lines += [f"| {c['category']} | {c['status']} | {c['count']} |" for c in report['counts']]
    for heading,subset in [('Current-term local issues',report['current_term_issues']),('Legacy baseline local issues',report['legacy_baseline_issues']),('Other rejected or repository issues',[r for r in report['issues'] if r['category'] not in ('current-term-local','legacy-baseline-local')])]:
        lines += ['', '## '+heading,'']
        if not subset:
            lines.append('No issues in this category.')
        for r in subset:
            lines.append(f"- `{r['source']}:{r['line']}` — {r['status']}: `{r['target']}` → `{r.get('resolved_target','')}`")
    lines += ['','## Scope and limits','']+[ '- '+s for s in report['limitations']]
    lines += ['','Missing required workspace inputs: '+(', '.join(report['missing_required_inputs']) or 'none')+'.',f"Parser warnings: {len(report['parse_warnings'])}; see JSON for exact locations.",'','The JSON keeps target failures, heading failures, legacy baseline links and unfetched external URLs separate. Re-run after final workspace and Render Input generation. This report tests consistency only and supplies no legal conclusion.','']
    dest.with_suffix('.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps(dict(passed=report['passed'],inputs=len(sources),links=len(report['links']),issues=len(report['issues']),current_term_issues=len(report['current_term_issues']),legacy_baseline_issues=len(report['legacy_baseline_issues']),external_not_fetched=report['external_urls_not_fetched'],render_present=render.is_file(),parse_warnings=len(report['parse_warnings']),report=label(dest.with_suffix('.json')))))
    return 0 if report['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
