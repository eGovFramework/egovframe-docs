---
title: Cron Trigger Code Generation
linkTitle: Cron Trigger Code Gen
description: "CronTriggerBean을 이용한 설정"
url: /egovframe-development/implementation-tool/code-generation/template-based-code-generation/eclipse-config-generation/eclipse-config-generation-cron-trigger/
menu:
  depth:
    weight: 20
    parent: "eclipse-config-generation"
    identifier: "eclipse-config-generation-cron-trigger"
---
# Cron Trigger Code Generation

## 개요

"CronTriggerBean을 이용한 설정"을 Code Generation 기능을 사용하여 쉽게 작성할 수 있다.

## 설명

Cron Trigger Configuration 의 설명은 다음 실행환경 가이드를 참조한다.

- [실행환경 Scheduling Configuration Guide]
# Detail Bean Job Code Generation

## 개요

"JobDetailBean을 이용한 작업 생성"을 Code Generation 기능을 사용하여 쉽게 작성할 수 있다.

## 설명

Detail Bean Job Scheduling Configuration 의 설명은 다음 실행환경 가이드를 참조한다.

- [실행환경 Scheduling Configuration Guide](../../../egovframe-runtime/foundation-layer/scheduling.md)

## 사용법

1. 이클립스 Window > Show View > Other… 를 선택하여 Show View 창을 연다.

![eGovFrame Templates 메뉴](./images/config-codegen-menu.png)

2. eGovFrame > eGovFrame Templates 를 선택한다.

![eGovFrame Templates 선택](./images/config-template-menu.png)

3. 작성하고자 하는 Configuration의 템플릿을 선택한다. - eGovFrame Templates > Scheduling > New Cron Trigger 선택

![New Cron Trigger 선택](./images/config-templates-configurations.png)

4. 화면 UI 를 통해 필요한 항목을 입력한 뒤 최종적으로 Finish 버튼을 클릭한다. **XML 방식** 또는 **Java Config 방식** 모두를 지원한다.

![상세 정보 입력](./images/config-cron-trigger-input.png)

5. 생성된 Configuration 파일을 확인한다.

- **XML 방식**

![생성된 Configuration 파일 확인 (XML)](./images/config-cron-trigger-result-xml.png)

- **Java Config 방식**

![생성된 Configuration 파일 확인 (Java Config)](./images/config-cron-trigger-result-java.png)