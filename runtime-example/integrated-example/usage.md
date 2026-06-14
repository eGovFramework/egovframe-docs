---
title: "사용법"
linkTitle: "사용법"
description: "실행환경 통합 예제를 개발 환경에서 임포트하고 실행하는 방법을 안내합니다."
url: /runtime-example/integrated-example/usage/
menu:
  depth:
    name: "사용법"
    weight: 2
    parent: "integrated-example"
---

## 통합 예제 실행 방법

1. **프로젝트 임포트**: Eclipse(eGovFrame IDE) 또는 IntelliJ에서 메이븐(Maven) 프로젝트로 임포트합니다.
2. **DB 설정**: 내장형 HSQL 또는 로컬 MySQL 등에 맞게 `context-datasource.xml`을 수정합니다.
3. **서버 기동**: Tomcat 등의 웹 WAS 서버를 구성하여 프로젝트를 배포하고 기동합니다.
4. **기능 테스트**: 제공되는 로그인 화면이나 게시판 목록 화면 등에 접근하여 트랜잭션이 정상적으로 처리되는지 확인합니다.
