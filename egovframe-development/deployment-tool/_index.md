---
title: 배포 도구
linkTitle: 배포 도구
description: "배포 도구"
url: /egovframe-development/deployment-tool/
menu:
  depth:
    weight: 6
    parent: "egovframe-development"
    identifier: "deployment-tool"
---

# 배포 도구

## 개요

배포 도구는 소스코드를 빌드하고 배포하는 데 필요한 기능을 제공한다. 개인빌드(Maven·Gradle)와 통합빌드, 빌드 레퍼지토리(Nexus), 컨테이너 가상화(Docker) 빌드, 서버 이관을 지원한다.

## 주요 개념

빌드는 개발자 PC에서 수행하는 개인빌드와 서버에서 수행하는 통합빌드로 구분되며, 빌드 산출물과 라이브러리는 빌드 레퍼지토리(Nexus)를 통해 관리한다. 빌드 도구는 Maven과 Gradle을 지원하며, 구현 도구 플러그인(m2eclipse·Buildship)으로 연동해 사용할 수 있다.

## 관련 문서

### 빌드 도구

- [Build Tool](./build-tool.md) — 빌드 도구 개요
- [빌드 Lifecycle](./build-lifecycle.md) — 빌드 생명주기
- [빌드 레퍼지토리](./build-repository.md) · [Nexus](./nexus.md) — 산출물·라이브러리 관리

### 개인빌드

- [개인빌드(Maven)](./maven.md) · [구현도구 플러그인(m2eclipse)](./build-m2eclipse.md)
- [개인빌드(Gradle)](./gradle.md) · [구현도구 플러그인(Buildship)](./gradle-buildship.md)

### Gradle 빌드환경 전환

- [표준프레임워크 Sample 프로젝트를 Gradle로 전환](./to-gradle.md)
- [표준프레임워크 Boot Sample 프로젝트를 Gradle로 전환](./boot-to-gradle.md)

### 통합빌드·이관

- [통합빌드](./integration-build.md) — 서버 통합빌드
- [서버 이관](./server-migration.md) — 배포 대상 서버 이관

### 컨테이너

- [컨테이너 가상화(Docker) 빌드](./docker.md) · [Docker Tooling](./docker-tooling.md)

## 참고자료

- [형상 관리 도구](../configuration-management-tool/_index.md)
