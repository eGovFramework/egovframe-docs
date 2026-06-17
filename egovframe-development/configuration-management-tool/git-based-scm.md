---
title: Git 기반 소스관리도구 운영
linkTitle: "Git 기반 SCM"
description: "Git 기반 소스관리도구의 운영 방식과 GitLab, Gitea, GitHub Enterprise 등 Git 서버 활용 방법을 설명한다."
url: /egovframe-development/configuration-management-tool/configuration-management/git-based-scm/
menu:
  depth:
    weight: 4
    parent: "configuration-management"
    identifier: "git-based-scm"
---

# Git 기반 소스관리도구 운영

## 개요

Git은 분산 버전 관리 시스템(Distributed Version Control System)으로, 개발자 PC의 로컬 저장소와 기관 내부 또는 외부의 원격 저장소를 함께 사용한다. 개발자는 로컬 저장소에서 브랜치를 만들고 커밋한 뒤 원격 저장소로 push하며, 원격 저장소에서는 merge request 또는 pull request를 통해 코드리뷰와 병합 절차를 운영할 수 있다.

이 문서는 기존 SVN 기반 운영 문서를 대체하지 않는다. SVN 운영이 필요한 사업은 [소스관리도구 서버환경 운영](./server-environment.md)과 [소스관리도구 클라이언트환경 사용](./client-environment.md)을 참고하고, Git 기반 운영이 필요한 사업은 본 문서를 기준으로 기관 환경에 맞게 구성한다.

## 적용 범위

Git 기반 소스관리도구는 다음과 같은 경우에 적합하다.

* 신규 개발 사업에서 브랜치 기반 협업과 코드리뷰를 기본 절차로 운영하는 경우
* GitLab, Gitea, GitHub Enterprise 등 Git 기반 서버를 기관 내부망 또는 전용망에 구축하는 경우
* Jenkins, Maven, Gradle, Nexus 등 빌드·배포 도구와 저장소 이벤트를 연계하는 경우
* SVN 저장소를 유지하면서 일부 신규 저장소부터 Git으로 단계적으로 전환하는 경우

## Git 기반 서버 예시

Git 기반 서버는 특정 제품을 의무적으로 채택하는 방식이 아니라 기관의 보안 정책, 운영 역량, 기존 인프라와의 연계성을 기준으로 선택한다.

| 구분 | 주요 특징 | 적용 시 고려사항 |
| --- | --- | --- |
| GitLab | 저장소, merge request, 이슈, CI/CD, 보호 브랜치, 감사 기능을 통합 제공한다. | 내부망 설치, 그룹·프로젝트 권한, Runner 운영, 백업 정책을 함께 설계한다. |
| Gitea | 비교적 가벼운 자체 호스팅 Git 서비스이며 저장소, pull request, 이슈, 조직 기능을 제공한다. | 소규모 기관 또는 독립망 환경에서 운영 부담을 낮추고자 할 때 검토할 수 있다. |
| GitHub Enterprise | GitHub의 협업 모델을 기관 전용 환경에서 사용할 수 있는 엔터프라이즈 제품군이다. | 조직 정책, 외부 협업, 감사 로그, SSO, 네트워크 경계를 함께 검토한다. |

## 기본 운영 흐름

저장소는 사업 또는 서비스 단위로 생성하고, 필요한 경우 공통 모듈과 응용 시스템을 별도 저장소로 분리한다. 저장소 생성 이후 개발자는 원격 저장소를 로컬 PC로 clone한다.

```bash
git clone https://git.example.go.kr/group/project.git
cd project
```

기능 개발은 기본 브랜치에서 직접 수행하지 않고 작업 브랜치를 만들어 진행한다.

```bash
git switch -c feature/login-policy
git add .
git commit -m "feat: add login policy validation"
git push -u origin feature/login-policy
```

원격 서버에서는 merge request 또는 pull request를 생성하여 코드리뷰, 자동 빌드, 보안 점검을 수행한다. 검토가 끝난 변경사항은 보호 브랜치 정책에 따라 승인 후 병합한다. 배포 기준점은 태그와 릴리스로 표시할 수 있다.

```bash
git tag v1.0.0
git push origin v1.0.0
```

## 권한 및 보안 운영

공공·기관 내부망 환경에서는 다음 항목을 기본 운영 정책으로 검토한다.

* 계정 관리: 기관 계정, SSO, LDAP, 2단계 인증 등 인증 정책과 연계한다.
* 권한 관리: 조직, 그룹, 프로젝트, 저장소 단위 권한을 정의하고 최소 권한 원칙을 적용한다.
* 보호 브랜치: `main`, `master`, `develop`, 릴리스 브랜치에는 직접 push를 제한하고 리뷰 또는 승인 절차를 요구한다.
* 코드리뷰: merge request 또는 pull request에 최소 승인 인원, 리뷰어 지정, 변경 요청 절차를 적용한다.
* 감사 로그: 저장소 생성, 권한 변경, push, 병합, 태그 생성, 설정 변경 이력을 보존한다.
* 백업 및 복구: 저장소 데이터, 이슈, merge request 또는 pull request, 첨부파일, 설정 정보를 주기적으로 백업한다.
* 미러링: 재해복구 또는 망 분리 연계를 위해 읽기 전용 미러 저장소를 구성할 수 있다.
* 비밀정보 관리: 소스 저장소에 비밀번호, API 키, 인증서 개인키가 포함되지 않도록 사전 점검 절차를 둔다.

## Jenkins 및 배포 도구 연계

Git 기반 서버는 저장소 이벤트를 활용해 빌드·배포 도구와 연계할 수 있다.

* Jenkins의 Git 플러그인을 사용하여 저장소와 브랜치를 checkout한다.
* push, tag, merge request 또는 pull request 이벤트를 webhook으로 전달하여 빌드를 자동 실행한다.
* Maven 또는 Gradle 빌드 결과물은 Nexus와 같은 저장소 관리 도구에 배포한다.
* 보호 브랜치 병합 전에는 단위 테스트, 정적 분석, 보안 점검을 필수 단계로 둘 수 있다.
* 운영 배포용 태그는 승인된 릴리스 절차를 통해 생성하고, 태그 기준으로 배포 이력을 추적한다.

## SVN에서 Git으로 전환

SVN에서 Git으로 전환할 때는 단순히 저장소만 변환하지 않고 이력, 권한, 브랜치 전략, 빌드 절차를 함께 재설계한다.

| SVN 구조 | Git 전환 예시 |
| --- | --- |
| `trunk` | `main` 또는 `master` 기본 브랜치 |
| `branches/*` | Git 원격 브랜치 또는 보존용 브랜치 |
| `tags/*` | Git tag |
| 디렉터리 단위 권한 | 저장소 분리, 그룹 권한, 보호 브랜치 정책 |

전환 절차는 다음 순서로 진행할 수 있다.

1. SVN 저장소 목록, 용량, 이력 기간, 권한 정책, 외부 참조를 조사한다.
2. `trunk`, `branches`, `tags` 구조가 일관적인지 확인하고 전환 대상 범위를 정한다.
3. 작성자 정보를 Git 계정 또는 이메일과 매핑한다.
4. `git svn` 또는 별도 마이그레이션 도구로 이력을 변환하고 태그·브랜치가 정상 매핑되었는지 검증한다.
5. 파일·디렉터리 단위 권한은 Git 저장소 분리 또는 보호 브랜치 정책으로 재설계한다.
6. Jenkins, Nexus, 배포 스크립트 등 기존 자동화 절차를 Git checkout 방식으로 수정한다.
7. 시범 저장소를 먼저 운영하고, 필요한 기간 동안 SVN과 Git을 병행 운영한다.
8. 최종 전환 시점에는 SVN 쓰기 작업을 중지하고 Git 저장소를 기준 저장소로 공지한다.

SVN의 파일 또는 디렉터리 단위 접근 제어는 Git의 기본 권한 모델과 일대일로 대응되지 않는다. 권한이 중요한 프로젝트는 저장소를 업무 단위로 분리하거나 보호 브랜치와 코드리뷰 정책을 결합하여 운영한다.

## 참고자료

* [Configuration Management](./configuration-management.md)
* [소스관리도구 서버환경 운영](./server-environment.md)
* [소스관리도구 클라이언트환경 사용](./client-environment.md)
* [Git 공식 문서](https://git-scm.com/book/en/v2)
* [GitLab 문서](https://docs.gitlab.com/)
* [Gitea 문서](https://docs.gitea.com/)
* [GitHub Enterprise 문서](https://docs.github.com/en/enterprise-server)
