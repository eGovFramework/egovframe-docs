---
title: Cache Code Generation
linkTitle: Cache Code Gen
description: "기본 Cache, Custom Cache 설정"
url: /egovframe-development/implementation-tool/code-generation/template-based-code-generation/eclipse-config-generation/eclipse-config-generation-cache/
menu:
  depth:
    weight: 6
    parent: "eclipse-config-generation"
    identifier: "eclipse-config-generation-cache"
---
# Cache Code Generation

## 개요

"기본 Cache 및 Custom Cache 설정"을 Code Generation 기능을 사용하여 쉽게 작성할 수 있다.

## 설명

eGovFrame Cache Configuration 의 설명은 다음 실행환경 가이드를 참조한다.

* [실행환경 Cache Configuration Guide](../../../egovframe-runtime/foundation-layer/cache.md)

## 사용법

1. 이클립스 Window > Show View > Other… 를 선택하여 Show View 창을 연다.

   ![Show View 메뉴](./images/config-codegen-menu.png)

2. eGovFrame > eGovFrame Templates 를 선택한다.

   ![eGovFrame Templates 메뉴](./images/config-template-menu.png)

3. 작성하고자 하는 Configuration의 템플릿을 선택한다. - eGovFrame Templates > Cache > New Cache 선택

   ![New DataSource 선택](./images/config-templates-configurations.png)

4. 화면 UI 를 통해 필요한 항목을 입력한 뒤 최종적으로 Finish 버튼을 클릭한다.

   ![상세 정보 입력](./images/config-cache-1.png)

   ![세부 정보 입력](./images/config-cache-2.png)

5. 생성된 Configuration 파일을 확인한다.

   ![생성된 Configuration 파일 확인](./images/config-cache-result.png)