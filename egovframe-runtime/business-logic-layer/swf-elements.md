---
title: SWF Elements
linkTitle: "SWF Elements"
url: /egovframe-runtime/business-logic-layer/spring-web-flow/swf-elements/
menu:
    depth:
        name: SWF Elements
        weight: 3
        parent: "spring-web-flow"
        identifier: "swf-elements"
---

## 개요

Spring Web Flow(SWF)에서 제공하는 핵심 요소(Elements)들에 대해 설명한다. 웹 애플리케이션의 네비게이션 흐름을 정의하는 다양한 XML 태그와 컴포넌트들을 포함한다.

## 주요 요소

* **Flow (`<flow>`)**: 하나의 업무 흐름을 정의하는 최상위 요소
* **State (`<view-state>`, `<action-state>`, `<decision-state>`, `<end-state>`)**: 흐름 내에서 특정 단계(상태)를 표현
* **Transition (`<transition>`)**: 상태 간의 이동(이벤트 기반 라우팅)을 정의
* **Action (`<evaluate>`, `<set>`)**: 상태 진입/진출 시 수행할 비즈니스 로직(메서드 호출, 변수 할당 등)

이러한 요소들을 조합하여 복잡한 페이지 간의 상태와 데이터를 안전하게 유지하며 화면 흐름을 제어할 수 있다.
