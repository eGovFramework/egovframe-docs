---
title: SWF Getting Started
linkTitle: "SWF Getting Started"
url: /egovframe-runtime/business-logic-layer/spring-web-flow/swf-getting-started/
menu:
    depth:
        name: SWF Getting Started
        weight: 1
        parent: "spring-web-flow"
        identifier: "swf-getting-started"
---

## 개요

Spring Web Flow(SWF)를 프로젝트에 처음 도입하고 설정하는 기초적인 방법을 설명한다.

## 1. 의존성 추가

프로젝트의 `pom.xml`에 Spring Web Flow 라이브러리 의존성을 추가한다.

## 2. Web Flow 설정 파일 작성

`DispatcherServlet` 컨텍스트 설정에 `FlowRegistry`, `FlowExecutor` 빈을 등록하고, URL 맵핑을 통해 Flow Controller가 동작하도록 구성한다.

## 3. 첫 번째 Flow XML 작성

가장 기본적인 화면 이동이 포함된 `flow.xml` 파일을 생성하여 `<view-state>`와 `<transition>`을 정의해 본다.
