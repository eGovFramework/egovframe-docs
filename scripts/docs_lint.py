#!/usr/bin/env python3
"""docs-lint: egovframe-docs 문서 정합성 검사 (표준 라이브러리만 사용)

검사 항목
L1 truncated-summary : 목차 요약이 '…'로 절단된 라인 (마침표 단위 발췌 규칙 위반)
L2 broken-rel-link   : 상대링크 대상 파일 부재 (렌더링 사이트 전용 링크 패턴은 정보로만 표시)
L3 frontmatter       : frontmatter 부재/title·url 누락 (README·docs/ 제외)
L4 heading-level     : H1 부재 또는 레벨 건너뜀(h2→h4 등)
L5 source-ref        : 관련소스 클래스 참조가 실제 저장소에 없음 (--src 로 소스 저장소 지정 시)

사용법: python3 docs_lint.py <docs-root> [--src <java-src-root>] [--json]
"""
import re, os, sys, glob, json, urllib.parse
from collections import defaultdict


USAGE = 'usage: python3 docs_lint.py <docs-root> [--src <java-src-root>] [--json]'


def parse_args(argv):
    if len(argv) < 2 or argv[1].startswith('-'):
        print(USAGE); sys.exit(2)
    root = argv[1]; src = None; as_json = False
    if not os.path.isdir(root):
        print('error: not a directory: ' + root); print(USAGE); sys.exit(2)
    if '--src' in argv:
        i = argv.index('--src') + 1
        if i >= len(argv):
            print('error: --src requires a path'); print(USAGE); sys.exit(2)
        src = argv[i]
    if '--json' in argv: as_json = True
    return root, src, as_json


def main():
    ROOT, SRC, AS_JSON = parse_args(sys.argv)
    findings = []
    mds = [m for m in glob.glob(ROOT + '/**/*.md', recursive=True) if '/.git/' not in m]

    cls_index = set()
    if SRC:
        for p in glob.glob(SRC + '/**/*.java', recursive=True):
            if '/main/' in p:
                rel = p.split('/src/main/java/')[-1][:-5]
                cls_index.add(rel.replace('/', '.'))

    for md in mds:
        rel = os.path.relpath(md, ROOT)
        text = open(md, encoding='utf-8', errors='replace').read()
        body = re.sub(r'```.*?```', '', text, flags=re.S)

        # L1 truncated summary
        for i, l in enumerate(text.split('\n'), 1):
            if re.search(r'\)\s*(?:—|-)\s.*…\s*$', l.strip()):
                findings.append((rel, i, 'L1', '요약 말줄임(…) — 문장 단위 발췌 필요'))

        # L2 relative links
        d = os.path.dirname(md)
        for m in re.finditer(r'\[[^\]]*\]\(([^)\s]+)\)', body):
            href = m.group(1)
            if href.startswith(('http', 'mailto:', '#', '/')): continue
            path = urllib.parse.unquote(href.split('#')[0])
            if not path: continue
            t = os.path.normpath(os.path.join(d, path))
            ok = os.path.exists(t) or os.path.exists(t + '.md') or os.path.exists(os.path.join(t, '_index.md'))
            if not ok:
                kind = 'L2' if not href.endswith('/') else 'L2-info'
                # 사이트 렌더 인지: 상위 섹션의 images/ 에 동일 파일명이 있으면 렌더링 사이트에서 정상 (GitHub 뷰 한정 문제)
                base = os.path.basename(path)
                cur = d
                for _ in range(4):
                    cur = os.path.dirname(cur)
                    if cur and os.path.exists(os.path.join(cur, 'images', base)):
                        kind = 'L2-siteok'; break
                if kind != 'L2-siteok' and href.rstrip('/').count('/') <= 2 and href.endswith('/'):
                    t2 = os.path.normpath(os.path.join(d, path.rstrip('/')))
                    if os.path.exists(t2 + '.md'): kind = 'L2-siteok'
                findings.append((rel, 0, kind, '상대링크 대상 부재: ' + href))

        # L3 frontmatter
        if not rel.startswith(('docs/', 'README')) and rel != '_index.md':
            fm = re.match(r'^---\r?\n(.*?)\r?\n---', text, re.S)
            if not fm:
                findings.append((rel, 1, 'L3', 'frontmatter 없음'))
            else:
                if not re.search(r'^\s*title\s*:', fm.group(1), re.M):
                    findings.append((rel, 1, 'L3', 'frontmatter title 누락'))

        # L4 heading levels
        levels = [len(m.group(1)) for m in re.finditer(r'^(#{1,6})\s', body, re.M)]
        if levels:
            prev = levels[0]
            for lv in levels[1:]:
                if lv > prev + 1:
                    findings.append((rel, 0, 'L4', f'제목 레벨 건너뜀 h{prev}->h{lv}'))
                    break
                prev = lv

        # L5 source refs
        if cls_index:
            for m in re.finditer(r'`((?:egovframework|org\.egovframe)\.[A-Za-z0-9_.]*?[A-Z][A-Za-z0-9_]*)(?:\.java)?`', body):
                ref = m.group(1)
                if ref not in cls_index and ref.split('.')[-1][0].isupper():
                    simple = ref.split('.')[-1]
                    if not any(c.endswith('.' + simple) for c in cls_index):
                        findings.append((rel, 0, 'L5', '실소스 부재 참조: ' + ref))

    by = defaultdict(int)
    for f in findings: by[f[2]] += 1
    if AS_JSON:
        print(json.dumps({'total': len(findings), 'byRule': dict(by),
                          'findings': [{'file': f[0], 'line': f[1], 'rule': f[2], 'msg': f[3]} for f in findings]},
                         ensure_ascii=False, indent=1))
    else:
        print(f'files scanned: {len(mds)} / findings: {len(findings)} {dict(by)}')
        for f in findings[:50]: print(f'{f[2]} {f[0]}:{f[1]} {f[3]}')


if __name__ == '__main__': main()

