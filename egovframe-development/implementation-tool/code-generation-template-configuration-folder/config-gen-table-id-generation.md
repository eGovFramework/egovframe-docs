---
title: Table ID Code Generation
linkTitle: Table ID Code Gen
description: "별도의 테이블을 이용한 ID 생성 서비스 설정"
url: /egovframe-development/implementation-tool/code-generation/template-based-code-generation/eclipse-config-generation/eclipse-config-generation-table-id-generation/
menu:
  depth:
    weight: 9
    parent: "eclipse-config-generation"
    identifier: "eclipse-config-generation-table-id-generation"
---
# Table ID Code Generation

## 개요

"별도의 테이블을 이용한 ID 생성 서비스 설정"을 Code Generation 기능을 사용하여 쉽게 작성할 수 있다.

## 설명

Table ID Generation Configuration 의 설명은 다음 실행환경 가이드를 참조한다.

* [실행환경 ID Generation Configuration Guide](../../../egovframe-runtime/foundation-layer/id-generation.md)

## 사용법

1. 이클립스 Window > Show View > Other… 를 선택하여 Show View 창을 연다.

   ![Show View 메뉴](./images/config-codegen-menu.png)

2. eGovFrame > eGovFrame Templates 를 선택한다.

   ![eGovFrame Templates 메뉴](./images/config-template-menu.png)

3. 작성하고자 하는 Configuration의 템플릿을 선택한다. - eGovFrame Templates > ID Generation > New Table ID Generation 선택

   ![New DataSource 선택](./images/config-templates-configurations.png)

4. 화면 UI 를 통해 필요한 항목을 입력한 뒤 최종적으로 Finish 버튼을 클릭한다. **XML 방식** 또는 **Java Config 방식** 모두를 지원한다.

   ![상세 정보 입력](./images/config-table-idgen-input.png)

5. 생성된 Configuration 파일을 확인한다.

   * **XML 방식**

     ![생성된 Configuration 파일 확인 (XML)](./images/config-table-idgen-result-xml.png)

   * **Java Config 방식**

     ![생성된 Configuration 파일 확인 (Java Config)](./images/config-table-idgen-result-java.png)