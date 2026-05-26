---
title: Property Code Generation
linkTitle: Property Appender Code Gen
description: "Property Service 설정"
url: /egovframe-development/implementation-tool/code-generation/template-based-code-generation/eclipse-config-generation/eclipse-config-generation-property/
menu:
  depth:
    weight: 16
    parent: "eclipse-config-generation"
    identifier: "eclipse-config-generation-property"
---
# Property Code Generation

## 개요

"Property Service 설정"을 Code Generation 기능을 사용하여 쉽게 작성할 수 있다.

## 설명

Property Configuration 의 설명은 다음 실행환경 가이드를 참조한다.

- [실행환경 Property Configuration Guide](../../../egovframe-runtime/foundation-layer/property.md)

## 사용법

1. 이클립스 Window > Show View > Other… 를 선택하여 Show View 창을 연다.

![eGovFrame Templates 메뉴](./images/config-codegen-menu.png)

2. eGovFrame > eGovFrame Templates 를 선택한다.

![eGovFrame Templates 선택](./images/config-template-menu.png)

3. 작성하고자 하는 Configuration의 템플릿을 선택한다. - eGovFrame Templates > Property > New Property 선택

![New Property 선택](./images/config-templates-configurations.png)

4. 화면 UI 를 통해 필요한 항목을 입력한 뒤 최종적으로 Finish 버튼을 클릭한다. **XML 방식** 또는 **Java Config 방식** 모두를 지원한다.

![상세 정보 입력](./images/config-property-input.png)

5. 생성된 Configuration 파일을 확인한다.

- **XML 방식**

![생성된 Configuration 파일 확인 (XML)](./images/config-property-result-xml.png)

- **Java Config 방식**

![생성된 Configuration 파일 확인 (Java Config)](./images/config-property-result-java.png)