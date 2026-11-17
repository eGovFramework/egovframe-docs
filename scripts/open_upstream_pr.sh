#!/usr/bin/env bash
set -euo pipefail

# 소스 브랜치(기본 트랙 통합 브랜치 work 또는 work-hugo-project)에서
# fork 전용 인프라 파일을 제거한 임시 브랜치를 만들어 push하고, 그 브랜치로
# 업스트림(eGovFramework/egovframe-docs)의 지정한 base 브랜치에 PR을 연다.
# 원본 소스 브랜치는 그대로 남아있다.
#
# 반드시 소스/base 브랜치 쌍을 직접 지정한다(자동 추측하지 않음):
#   work              -> main          (문서/콘텐츠 트랙)
#   work-hugo-project -> hugo-project  (Hugo 테마 트랙)
#
# 추가 인수는 gh pr create에 전달한다. 생략하면 대화형으로 제목/본문을 묻는다.
#
# 사용법: scripts/open_upstream_pr.sh <source-branch> <upstream-base-branch> [gh-pr-create-options...]
# 예시:   scripts/open_upstream_pr.sh work main
#         scripts/open_upstream_pr.sh work-hugo-project hugo-project
#         scripts/open_upstream_pr.sh work main --title "..." --body-file /tmp/pr-body.md

if [ $# -lt 2 ]; then
  echo "usage: $0 <source-branch> <upstream-base-branch> [gh-pr-create-options...]" >&2
  echo "  예: $0 work main" >&2
  echo "      $0 work-hugo-project hugo-project" >&2
  exit 1
fi

SRC="$1"
BASE="$2"
shift 2
UPSTREAM_REPO="eGovFramework/egovframe-docs"
CLEAN_BRANCH="upstream-submit/$(date +%Y%m%d%H%M%S)"

# 업스트림으로 절대 보내면 안 되는 fork 전용 인프라 파일 목록.
# 두 트랙(work, work-hugo-project) 전체를 아우르는 superset이다 —
# 각 파일은 해당하는 트랙에만 존재하므로 다른 트랙에서는 "없으면 건너뜀"으로 처리된다.
DENYLIST=(
  "AGENTS.md"
  ".github/FORK_PREVIEW.md"
  ".github/workflows/fork-preview.yml"
  ".github/workflows/sync-upstream-mirrors.yml"
  ".github/workflows/close-resolved-issues.yml"
  ".github/workflows/check-upstream-pr-hygiene.yml"
  "scripts/prepare_fork_site.py"
  "scripts/preview_fork.sh"
  "scripts/open_upstream_pr.sh"
  "scripts/close_resolved_issues.py"
  ".specify"
  ".omp"
)

# 이번 제출에서만 제외할 경로(공백으로 구분). 예: 업스트림에 이미 열린 PR과 겹치는 파일.
# 업스트림 base에 있는 파일은 base의 내용으로 되돌리고(삭제가 아님), 없는 파일은 제거한다.
# 영구 제외 대상이면 위 DENYLIST에 추가한다.
#   EXTRA_DENY=".github/workflows/deploy-on-merge.yaml" scripts/open_upstream_pr.sh work main
EXTRA=()
if [ -n "${EXTRA_DENY:-}" ]; then
  # shellcheck disable=SC2206
  EXTRA=($EXTRA_DENY)
fi

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

git fetch origin "$SRC" "$BASE"
git checkout -B "$CLEAN_BRANCH" "origin/$SRC"

removed=()
for f in "${DENYLIST[@]}"; do
  if [ -e "$f" ]; then
    git rm -rq "$f"
    removed+=("$f")
  fi
done

reverted=()
for f in ${EXTRA[@]+"${EXTRA[@]}"}; do
  if git cat-file -e "origin/$BASE:$f" 2>/dev/null; then
    git checkout "origin/$BASE" -- "$f"
    reverted+=("$f")
  elif [ -e "$f" ]; then
    git rm -rq "$f"
    removed+=("$f")
  fi
done
if [ ${#reverted[@]} -gt 0 ]; then
  printf '이번 제출에서 업스트림 %s 버전으로 되돌린 파일:\n' "$BASE"
  printf '  - %s\n' "${reverted[@]}"
fi

if [ ${#removed[@]} -gt 0 ] || [ ${#reverted[@]} -gt 0 ]; then
  [ ${#removed[@]} -gt 0 ] && { printf '다음 fork 전용 파일을 제거했습니다:\n'; printf '  - %s\n' "${removed[@]}"; }
  git commit -m "chore: strip fork-only tooling before upstream submission"
else
  echo "제거할 fork 전용 파일이 없습니다 (이미 없음)."
fi

git push -u origin "$CLEAN_BRANCH"

gh pr create --repo "$UPSTREAM_REPO" --base "$BASE" --head "leejongyoung:$CLEAN_BRANCH" "$@"

echo
echo "원본 브랜치($SRC)는 그대로 유지됩니다. 임시 제출 브랜치: $CLEAN_BRANCH"
