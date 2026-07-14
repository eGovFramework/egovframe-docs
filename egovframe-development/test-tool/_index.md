---
title: 테스트 도구
linkTitle: 테스트 도구
description: "테스트 도구"
url: /egovframe-development/test-tool/
menu:
  depth:
    weight: 5
    parent: "egovframe-development"
    identifier: "test-tool"
---

# 테스트 도구

## 개요

테스트 도구는 단위 테스트 작성부터 실행, 커버리지 측정, 결과 리포팅, 테스트 자동화까지 테스트 전 과정을 지원한다. JUnit 기반 Unit Test와 Mock·DB·MVC 테스트 지원, EMMA 커버리지, Ant·Maven·Excel 리포팅을 제공한다.

## 주요 개념

테스트는 Test Case 작성 → TestSuite 구성·실행 → 커버리지 측정 → 결과 리포팅 순으로 진행하며, 통합빌드와 연계해 자동화할 수 있다. 외부 의존성은 Mock Support로 대체하고, DB·MVC 계층은 전용 지원 기능으로 테스트한다.

## 관련 문서

### Unit Test

- [Unit Test](./unit-test.md) — 단위 테스트 개요
- [Test Case](./test-case.md) — 테스트 케이스 작성
- [Write TestSuite](./write-testsuite.md) · [Run TestSuite](./run-testsuite.md) — 테스트 스위트 작성·실행
- [Unit Test 작성을 위한 pom.xml dependency 설정](./pom-dependency-for-write-unittest.md)

### 테스트 지원

- [Mock Support](./mock-support.md) — 의존 객체 대체
- [DB Support](./db-support.md) — 데이터베이스 테스트 지원
- [MVC Test](./mvc-test.md) — MVC 계층 테스트
- [Batch Job Test Wizard](./batch-job-test-wizard.md) — 배치 작업 테스트

### Test Coverage

- [Test Coverage](./test-coverage.md) — 커버리지 측정 개요
- [EMMA에서 생성한 HTML 리포트 샘플](./emma-test-report.md)
- [EMMA 실행을 위한 build.xml 설정 샘플](./build-example-for-run-emma.md) · [pom.xml 설정 샘플](./pom-example-for-run-emma.md)

### Test Reporting

- [Test Reporting](./test-reporting.md) — 리포팅 개요
- [Ant에서 생성한 테스트 결과 HTML 리포트](./ant-test-report.md) · [Maven에서 생성한 테스트 결과 HTML 리포트](./maven-test-report.md)
- [테스트 결과 Excel 리포트](./excel-test-report.md) · [상세](./excel-test-report-detail.md) · [엑셀 리포팅 사용을 위한 setting.xml 설정](./setting-for-excel-reporting.md)

### Test Automation

- [Test Automation](./test-automation.md) — 테스트 자동화
- [이클립스에서 Ant 실행하기](./run-ant-on-eclipse.md) · [이클립스에서 Maven 실행하기](./run-maven-on-eclipse.md)

### 정적분석

- [SpotBugs](./spotbugs.md) — 정적분석 도구

### 소스·참조

- [egovframework-dev-tst 프로젝트 소스 코드](./egovframework-dev-tst-source.md) · [egovframework-dev-tst-ant 프로젝트 소스 코드](./egovframework-dev-tst-ant-source.md)
- [참조 문서 목록](./test-tool-ref.md)

## 참고자료

- [배포 도구](../deployment-tool/_index.md)
- [구현 도구](../implementation-tool/_index.md)
