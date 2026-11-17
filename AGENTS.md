# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, Copilot, etc.) working in
**leejongyoung/egovframe-docs**, a personal fork of
[eGovFramework/egovframe-docs](https://github.com/eGovFramework/egovframe-docs)
used to prepare clean contributions back to that upstream repo.

As of 2026-10-05, upstream PRs #1150 and #1151 are closed and their
consolidated replacements are open: [#1152](https://github.com/eGovFramework/egovframe-docs/pull/1152)
targets `main` and [#1153](https://github.com/eGovFramework/egovframe-docs/pull/1153)
targets `hugo-project`. Merge #1152 first: #1153's locale templates require
Hugo 0.167.0. PR state can change; check GitHub before relying on this note.

This file is fork-only tooling: it must never be sent upstream (see
"Submitting to upstream" below). If you are reading this while checked out on
`main` or `hugo-project`, something is wrong — those branches must stay
byte-identical to upstream.

## Mental model: two tracks, four branch roles

Upstream has two unrelated histories: `main` (Markdown content) and
`hugo-project` (an orphan branch holding the Hugo site generator + the
`krds-theme` theme). This fork mirrors that split and adds one integration
branch per track:

| Branch              | Role                                                             | Who commits here |
|----------------------|-------------------------------------------------------------------|-------------------|
| `main`               | Byte-identical mirror of upstream `main`                          | Bot only (fast-forward) |
| `work`               | **Default branch.** Content-track dev/integration + fork tooling  | You |
| `hugo-project`       | Byte-identical mirror of upstream `hugo-project`                  | Bot only (fast-forward) |
| `work-hugo-project`  | Theme-track dev/integration branch, branched from `hugo-project`  | You |
| `gh-pages`           | Generated build output                                            | Nobody — never hand-edit |

**Why `main`/`hugo-project` must stay pure:** GitHub Actions `schedule`
(cron) triggers are only evaluated from the workflow file as it exists on the
repository's **default branch**. The default branch was moved to `work` for
exactly this reason — it lets `main` and `hugo-project` stay untouched
mirrors while the daily sync automation (`.github/workflows/sync-upstream-mirrors.yml`,
cron `0 15 * * *` UTC + manual `workflow_dispatch`) lives on `work` and
fast-forwards both mirrors from upstream. The merge is `--ff-only`: if either
mirror ever diverges (e.g. someone commits to it directly), the sync job
fails loudly instead of silently force-pushing. **Never commit directly to
`main` or `hugo-project`.**

## The fork-first PR workflow

Always land changes on this fork before they go upstream — never open a PR
against `eGovFramework/egovframe-docs` directly from a throwaway branch.

1. For upstream-bound changes, branch from the relevant mirror:
   - Content/docs change → branch from `main`.
   - Theme/Hugo change → branch from `hugo-project`.
   - Fork-only tooling or `AGENTS.md` → branch from the corresponding
     integration branch; keep it out of upstream submission heads.
2. Open a PR **against this fork's own integration branch** (`work` or
   `work-hugo-project`). This is the review checkpoint — CI (`fork-preview.yml`)
   builds the site and uploads a downloadable HTML preview artifact on every
   push/PR to either integration branch. Use this step for agent review,
   human review, or both, before anything goes near upstream.
3. **Default cadence: batch, don't submit after every single fork PR.** Let
   several fork-side PRs land on `work`/`work-hugo-project` first, then cut
   *one* upstream submission covering all of them. Submitting upstream
   immediately after each individual fork PR merge (as was done once for
   PRs [#1151](https://github.com/eGovFramework/egovframe-docs/pull/1151)
   and [#1150](https://github.com/eGovFramework/egovframe-docs/pull/1150))
   is the exception, not the rule — upstream reviewers deal with one
   consolidated PR per batch, not a stream of small ones. Either way, the
   script below only runs when a human chooses to run it — nothing in this
   repo opens PRs against the upstream repo automatically.
4. When more work appears while an upstream PR is open, land it through a
   separate fork topic PR into the appropriate integration branch. Decide
   deliberately whether to refresh the existing disposable submission head
   and update its description, or close it and submit a new consolidated
   snapshot. Do not develop on the upstream PR head. If replacing a PR,
   explain the replacement on the old PR and update fork issue/PR links.

### Submitting to upstream

```sh
scripts/open_upstream_pr.sh work main                    # content track
scripts/open_upstream_pr.sh work-hugo-project hugo-project # theme track
```

This creates a disposable `upstream-submit/<timestamp>` branch from the given
source, **strips the fork-only tooling denylist** (see `DENYLIST` in the
script), pushes it, and opens a PR against `eGovFramework/egovframe-docs`.
It accepts additional `gh pr create` options such as `--title`, `--body-file`,
and `--draft`. The source branch is left untouched. Paths that must be left out of one submission only (for example files already covered by an open upstream PR) go in the `EXTRA_DENY` environment variable, space-separated (files that exist upstream are reverted to the upstream base content, not deleted); `.specify/` and `.omp/` are always stripped. **If you add new
fork-only files, add them to `DENYLIST` first.** Before submission, compare
the exact proposed diff against the current upstream base and inspect the
file list for accidental fork tooling or unrelated changes.

**Always use this script to get the PR head branch — never open an
upstream PR directly from `work`, `work-hugo-project`, or any other branch
you intend to keep developing on.** An open PR's diff is live: GitHub
recomputes it from the current head branch on every push, not from a
snapshot taken when the PR was opened. PR #1150 did this correctly (head
is a disposable `upstream-submit/20261005121218`, so later commits to
`work` never touched it). PR #1151 didn't — it was opened directly from
`fix/hugo-project-maintenance`, which was still being pushed to
afterwards (a mermaid-header date fix, then the dead-template removal),
so those commits appeared in the already-open PR automatically. The
*content* happened to be fine both times (everything pushed there was
meant for that PR anyway), but it was only safe by luck, not by design -
don't rely on that. Once a PR like #1151 exists from a branch you're still
using for development, stop pushing to that branch; do further work
through a fresh topic branch and a new `open_upstream_pr.sh` snapshot
instead.

**`.github/workflows/check-upstream-pr-hygiene.yml` is the backstop.** Its
daily schedule (and manual dispatch) lists open upstream PRs authored by
`leejongyoung` and fails if any head branch does not start with
`upstream-submit/`. It runs from default branch `work` so it catches topic
branches that lack the workflow file. A failed run stays a meaningful alert
until the unsafe PR is closed or resubmitted; do not silence it merely to
make Actions green. GitHub's failure notification alerts the fork owner.

## Upstream rules you must not break

- **Never touch the frontmatter of an existing `.md` file** on the content
  track. Upstream's `merge-on-pr.yaml` bot diffs frontmatter blocks (the
  first `---`…`---`) on every PR touching `main`; if it detects a change on
  a *modified* file (new files are exempt), it blocks auto-merge and comments
  on the PR asking for maintainer review. Add new files without frontmatter
  and describe their menu placement in the PR template's "추가 참고 사항" field
  instead.
- **2026 contribution scope is `common-component/` (primary), plus
  `egovframe-development/` and `egovframe-runtime/`.** New top-level menus
  are explicitly not accepted upstream.
- `hugo-project` has **no `.github/workflows/` directory of its own** — all
  CI for building/deploying the site lives in `main`'s workflows
  (`deploy-on-merge.yaml`, `deploy-on-push.yaml`, `deploy-on-schedule.yaml`)
  and this fork's `fork-preview.yml`. A fix that only touches a workflow
  YAML's settings (e.g. the pinned Hugo version) belongs on the content
  track (`main`/`work`), not a `hugo-project` PR, even if it's about
  building the Hugo site.
- `hugo-project` commit history so far is maintainer-only accounts
  (`hjlee1107`, `eGovFrameSupport`). Treat changes there as proposals, not
  assumed-acceptable PRs.

## Local preview

```sh
./scripts/preview_fork.sh
```

Renders the current checkout (including uncommitted changes) at
`http://127.0.0.1:8888/`, using the Hugo layout from `origin/hugo-project`
and the pinned Hugo **0.167.0** (extended) binary — match this version
exactly when testing locally; a different Hugo version is not a valid test
of what CI will do. `scripts/prepare_fork_site.py` is what rewrites
`hugo.toml`'s baseURL/repo links from the upstream site to
`leejongyoung.github.io` for both the local script and CI; look there before
changing any URL-rewriting logic.

The live fork preview is published from `work-hugo-project` pushes, using
that branch's Hugo theme and the `main` documentation, at
<https://leejongyoung.github.io/egovframe-docs/>. The `work` content track
still produces downloadable HTML artifacts for PRs and pushes.

## Verifying a change before opening any PR

Fork CI builds the full site with real content, but does not compare its
output page by page against a baseline — do that for changes to the site:

```sh
# Linux/CI-matching binary: download the exact pinned version, don't use
# whatever `hugo` happens to be on PATH.
gh release download v0.167.0 --repo gohugoio/hugo \
  --pattern "hugo_extended_0.167.0_Linux-64bit.tar.gz"

# macOS: Homebrew's formula tracks the latest version; only trust its build
# when `hugo version` confirms the exact pinned version.
brew install hugo && hugo version
```

Then build with real `main` content copied into `hugo-project`'s `content/`
(mirroring what CI's "Copy markdown files to content" step does), and diff
the output `public/` tree against a baseline build from before your change.
A change that touches the theme should produce a **page-by-page diff you can
fully explain** — if pages differ in ways you didn't intend, stop and
investigate before opening a PR. This is how the `hugo-project` fixes in PR
[#1151](https://github.com/eGovFramework/egovframe-docs/pull/1151) were
verified (708/708 pages matched except the specific intended lines).

### Check cross-PR version dependencies, not just conflicts

Two PRs touching different branches can't git-conflict, but one can still
*require* the other. Before shipping a fix, ask whether it depends on a
specific tool/Hugo/library version being live yet — not just whether it
clashes with another open PR's files. This bit us for real: switching
`hugo-project` to `.Language.Locale`/`.Language.Direction` (for issue #11)
builds fine under Hugo 0.167.0 but is a **hard build failure** under the
0.139.0 still pinned upstream (`can't evaluate field Locale in type
*langs.Language`). Main-track PR #1152 must merge before theme-track PR
#1153. The two PRs can be open concurrently; PR creation, draft/ready state,
and merge order are separate decisions. GitHub does not automatically change
draft/ready state when a prerequisite merges, and a visible merge button
does not prove a cross-branch version dependency is satisfied. Only an
upstream maintainer with write access can merge. The unrelated dead
`td-render-heading.html` template was verified under both Hugo versions.
When in doubt, build with *both* the old and new pinned versions.

## Known gotchas (so you don't rediscover them)

- **`krds-theme` is not really a git submodule.** `.gitmodules` used to
  declare it as one, but the tree entry was always a plain directory (mode
  `040000`, not a commit gitlink `160000`) on both the fork and upstream —
  `git submodule update --init` was a silent no-op. The stale `.gitmodules`
  was removed in PR #1151; the theme is just a vendored directory.
- **The merged `custom.js`'s SRI `integrity` attribute is empty** (see
  `themes/krds-theme/layouts/partials/head/js.html`, the `resources.Concat`
  output). This is a pre-existing upstream bug unrelated to anything this
  fork has changed — don't assume you broke it if you see it, and don't try
  to "fix" it incidentally as part of an unrelated change.
- **`mermaid.min.js` is vendored from the official npm distribution.**
  `themes/krds-theme/package.json` pins Mermaid 12.1.0 and records the
  vendoring date; `npm ci && npm run build:vendor` reproduces the committed
  browser bundle byte for byte. The fork preview checks this on the theme
  track. When updating Mermaid, change the pin and date together, then
  re-verify browser rendering as PR #1151 did (Playwright + real Chrome
  against every diagram type used in `main`'s content). Hugo builds alone
  cannot validate client-side diagram rendering.
- **The Hugo version pin was bumped `0.139.0` → `0.167.0`** (fork issue
  [#6](https://github.com/leejongyoung/egovframe-docs/issues/6), current
  upstream PR [#1152](https://github.com/eGovFramework/egovframe-docs/pull/1152)). Don't
  bump it again casually; it needs the same before/after full-site-diff
  verification described above. 0.167.0 also surfaces three new deprecation
  warnings that only matter for `hugo-project` (its `hugo.toml`'s
  `languageCode` key, and `.Language.LanguageCode`/`.Language.LanguageDirection`
  in templates, plus an "unrecognized render hook template" warning for an
  already-dead template) — tracked separately as a `hugo-project`/
  `work-hugo-project` fix, not a content-track one.
- **`markdown-lint.yml` and `link-check.yml` on `main` are entirely commented
  out** — they do nothing. `scripts/docs_lint.py` exists but is not wired
  into any CI workflow either. Don't assume either one is actually linting
  anything right now.
- **`deploy-on-*.yaml` on `main` install Node.js 18** (EOL since 2025-04)
  even though the Hugo build itself needs no Node tooling that's visible in
  this repo. Not yet filed as an issue — if you investigate and find it's
  genuinely dead weight, file one.

## Issue/label/milestone conventions on this fork

Labels use a two-axis scheme, `type:*` (what kind of change) × `area:*`
(which part of the repo) — e.g. `type:docs`, `type:update`,
`type:maintenance`, `type:research`, `area:common-component`,
`area:development`, `area:runtime`, `area:infra`, `area:hugo-theme`. Default
GitHub labels (`bug`, `enhancement`, `good first issue`, ...) were
deliberately deleted in favor of this scheme — don't recreate them.

Milestones group issues by concrete, verified gaps (not aspirational
roadmap items) — e.g. "공통컴포넌트 공백 보완", "5.x 버전 정합성 점검",
"hugo-project 유지보수 점검". When filing a new issue, attach it to an
existing milestone if it fits, and add it to the GitHub Project
("egovframe-docs 기여 로드맵", project number 3, owner `leejongyoung`) with:

```sh
gh project item-add 3 --owner leejongyoung --url <issue-url>
```

Every issue should describe a finding you've actually verified (grep output,
a build log, a diff) — not a suspicion. If investigation shows an issue
can't actually be fixed in the PR scope you assumed (as happened with issue
#6 above), say so in the issue/PR rather than forcing it in anyway.

### Checkbox hygiene and auto-closing

Only check a `- [ ]` box in an issue body when a specific commit actually
resolved it — not when you've merely investigated it. An issue's checklist
is a completion record, not a scratchpad. When a fix lands, comment on the
issue with the **full URL** of the upstream PR (e.g.
`https://github.com/eGovFramework/egovframe-docs/pull/1151`) — not a bare
`#1151` — and check the boxes it actually resolves, leaving any unresolved
ones unchecked. Closed or superseded upstream PRs must be identified as such
in issue comments, with links updated to their current replacements.

`.github/workflows/close-resolved-issues.yml` (daily + `workflow_dispatch`,
runs `scripts/close_resolved_issues.py`) auto-closes an issue once **both**
hold: every checkbox in its body is checked (or it has none at all), and
every upstream PR URL mentioned in its body/comments is `MERGED` (a PR
that's merely `CLOSED` — e.g. #1149, superseded by #1151 — is ignored
rather than blocking the issue forever). This only writes to this fork's
own issues, so the default `GITHUB_TOKEN` is enough — there's no cross-repo
permission problem here, unlike the "does merging an upstream PR auto-close
a fork issue via `Closes #N`" question this was built to answer (no: GitHub
keyword auto-close only works within a single repo, and even the
`owner/repo#N` cross-repo syntax requires the person merging the PR to have
write access to the *other* repo, which an upstream maintainer doesn't have
to this fork).

## Spec-driven workflow (lightweight, no extra tooling)

This fork doesn't install [github/spec-kit](https://github.com/github/spec-kit)
or any `.specify/` scaffolding — just follow its shape manually for any
nontrivial change:

1. **Specify** — before touching files, write (or confirm) a GitHub issue
   with a concrete, falsifiable problem statement, not a vague "improve X".
2. **Plan** — note how you'll verify the fix *before* implementing it (which
   command, which diff, which build). Decide this before writing code so you
   don't rationalize a weak verification after the fact.
3. **Implement** — make the smallest change that satisfies the plan.
4. **Verify & record** — actually run the verification from step 2, and put
   the result in the PR description (see PR #1151's "검증" section for the
   expected level of detail: exact command, exact before/after comparison).

If a step reveals the original plan doesn't work (e.g. "this needs a
different base branch," "this file doesn't exist where I assumed"), stop and
re-specify rather than forcing the original plan through.

## Applying this collaboration pattern to another eGovFrame fork

Inspect that repository's upstream, branch histories, workflows, permissions,
existing issues, and Project before changing its setup. Record the actual
branch roles and contribution rules in *its own* `AGENTS.md`; do not assume
every eGovFrame repository has this repo's orphan `hugo-project` track.

- Keep upstream mirror branches byte-identical and move them only by verified
  fast-forward. Use a separate default `work` integration branch and fork
  topic PRs with CI as the review checkpoint. Add another integration track
  only when the upstream repository truly has a separate history.
- Batch reviewed fork work into an upstream submission. Use a disposable PR
  head such as `upstream-submit/*`, strip fork-only tooling, inspect the exact
  diff, and leave the integration branch free for continuing work. Run a
  scheduled check of open upstream PR heads from the fork's default branch.
- Track verified findings in fork issues, using consistent labels,
  milestones, and a Project. Check a task off only after implementation;
  link the full upstream PR URL and keep superseded PR references current.
  Close an issue after its checklist is complete and its linked upstream
  submissions are merged.
- Verify cross-branch build dependencies and the actual deployed preview.
  Opening a PR, marking it ready, passing CI, and merging are distinct
  events. State required merge order in dependent PRs and do not infer it
  from GitHub's merge button.
