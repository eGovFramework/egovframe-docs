# 가이드 문서 정합성 체크

※ 해당 문서는 EricSeokgon님의 contribution 기여본(#767)을 기반으로 작성되었습니다.

## 개요
`scripts/docs_lint.py`는 가이드 Markdown 문서의 정합성을 로컬에서 검사하는 스크립트입니다.<br>
Python 표준 라이브러리만 사용하므로 별도 패키지 설치가 필요하지 않습니다.<br>
일반 마크다운 린터와 달리, frontmatter·상대링크·제목 계층·목차 요약 등 사이트 렌더링에 영향을 주는 항목을 점검합니다.<br>
PR 반영 후 가이드가 즉시 배포되므로, 배포 이후 드러나는 오류를 사전에 줄이기 위해 사용합니다.

## 방법
### 1. 파일 생성 및 수정
md 파일을 작성하거나 수정합니다.<br>
*이미 작성된 파일도 확인이 가능합니다.

### 2. 정합성 체크
Python 3가 필요하며, 별도 패키지 설치는 필요하지 않습니다.<br>
저장소 최상위(`egovframe-docs`)에서 실행하고, 인자는 검사할 폴더입니다.<br>
`python3`가 없는 환경(Windows 등)에서는 `python`으로 실행합니다.

- 전체 검사: `python3 scripts/docs_lint.py .`
- 특정 디렉토리만 검사: `python3 scripts/docs_lint.py common-component`
- 클래스 참조 검사(L5): `python3 scripts/docs_lint.py common-component --src <java-src-root>`
- 결과 전체 JSON 출력: `--json` 옵션 추가

### 3. 정합성 오류 목록
#### L1 truncated-summary
: 목차 요약이 '…'로 절단된 라인 (마침표 단위 발췌 규칙 위반)
- 목차·요약 라인의 말줄임표(`…`)를 검출합니다. 본문에 쓰인 점 세 개(`...`)는 보통 해당하지 않습니다.
- 목차 요약은 말줄임이 아닌 마침표(".") 등으로 문장을 완결해야 합니다.
- 예시)
    - 공통컴포넌트는 표준프레임워크 기반의 표준을 준수하고 … (X)
    - 공통컴포넌트는 표준프레임워크 기반의 표준을 준수하고 유연성을 확보하여 재사용성을 극대화한다. (O)

#### L2 broken-rel-link
: 상대링크 대상 파일 부재 (렌더링 사이트 전용 링크 패턴은 정보로만 표시)
- markdown의 물리 파일 경로가 작성한 경로와 올바르지 않을 때 발생합니다.
- 물리적으로 동일한 depth에 있는 파일이지만 `../component` 등 다른 경로처럼 작성하는 경우입니다.
- egovframe 가이드는 md 파일을 depth 구분 없이 한 프로젝트 내에 두고 있어, 물리 파일 경로와 url 경로를 혼동할 수 있습니다.
- 예시) login.md에서 find-id.md로 이동하는 경로를 작성할 때 (두 파일이 물리적으로 동일한 경로에 존재)
    - `[아이디 찾기](../find-id/)` 로 작성 (X)
    - `[아이디 찾기](find-id)` 로 작성 (O)
- IDE에서 작성한 경우 링크를 클릭하여 올바른 이동이 이루어지는지 확인합니다.
- 검출 코드
    - `L2`: 상대링크 대상이 없어 수정이 필요합니다.
    - `L2-info`: 끝에 `/`가 있는 디렉터리형 링크인데 대상 파일이 없을 때 정보로 표시합니다.
    - `L2-siteok`: GitHub 미리보기에서는 깨져 보일 수 있으나, 배포 사이트에서는 열릴 수 있는 정보성 알림입니다. 실패로 보지 않습니다.

#### L3 frontmatter
: frontmatter 부재 또는 `title` 누락 (README·docs/ 제외)
- 스크립트는 frontmatter 존재 여부와 `title`만 검사합니다. (`url`은 검사하지 않습니다.)
- `title` 누락 시 화면 렌더링 오류가 발생할 수 있습니다.
- README, `docs/`, `_index.md` 및 일부 목록성 파일은 검사에서 제외되거나 예외로 둡니다.
    - *egovframe-runtime/intro.md 는 참고사항을 확인합니다.

#### L4 heading-level
: 제목 레벨 건너뜀 (h2→h4 등)
- 제목은 오름차순(H1 → H2 → H3 ...)으로 작성합니다.
- H1은 가이드 제목이므로 작성하는 것을 권장하지만, 검증 스크립트의 경우 H1 부재가 아니라 레벨 건너뜀만 검출합니다.

#### L5 source-ref
: 관련소스 클래스 참조가 실제 저장소에 없음 (`--src`로 소스 저장소 지정 시)
- 문서의 백틱 클래스명(`egovframework.*`, `org.egovframe.*`)이 실제 Java 소스에 있는지 확인합니다.
- `--src`를 지정하지 않으면 L5는 동작하지 않습니다.
- 예시: `python3 scripts/docs_lint.py common-component --src ../egovframe-common-components`

## 결과
### 출력
```
files scanned: 214 / findings: 1 {'L3': 1}
L3 intro.md:1 frontmatter 없음
```
- `files scanned`: 검사한 md 파일 수 / `findings`: 검출 건수와 규칙별 건수
- 각 행은 `규칙코드 파일:라인 메시지` 형식입니다. 라인이 `0`이면 파일 단위 검출입니다.
- 기본 출력은 상위 50건만 표시합니다. 전체를 보려면 `--json`을 사용합니다.

### 수정
검증 결과에 출력된 목록 중 수정이 필요한 파일을 찾아 파일을 수정합니다.<br>
