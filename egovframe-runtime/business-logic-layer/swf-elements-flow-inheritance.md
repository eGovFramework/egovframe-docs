---
title: Flow 상속
linkTitle: "Flow 상속"
description: Flow 상속은 상위 Flow의 설정을 하위 Flow에서 사용할 수 있도록 하며, 주로 global transition과 예외 핸들러를 상속받는 데 사용된다. 자바 상속과 유사하지만, 하위 Flow는 상위 Flow의 요소를 재정의할 수 없으며, 여러 상위 Flow를 상속받을 수 있다.
url: /egovframe-runtime/business-logic-layer/spring-web-flow/swf-elements/swf-elements-flow-inheritance/
menu:
  depth:
    name: Flow 상속
    weight: 5
    parent: "swf-elements"
---
# Flow 상속

## 개요

Flow 상속은 한 Flow가 다른 Flow 설정을 상속할 수 있게 되어 있다. 상속은 Flow와 State 레벨에서 모두 발생할 수 있다.
가장 흔한 유즈케이스는 상위 Flow로 global transition과 예외 핸들러를 정의하고 하위 Flow로 그 설정을 상속받는 것이다.
상위 Flow를 찾으려면 다른 Flow들처럼 flow-registry에 추가해야 된다.

## 설명

### Flow 상속은 자바 상속과 비슷한가?

상위에 정의한 요소를 하위에서 접근할 수 있다는 측면에서는 자바 상속과 Flow 상속이 비슷하다.
하지만 몇 가지 차이점을 가지고 있다.

하위 Flow는 상위 Flow의 요소를 재정의할 수 없다. 상위와 하위 Flow에 있는 동일한 요소는 병합된다.
상위 Flow에만 있는 요소는 하위 Flow에 추가된다.

**하위 Flow는 여러 상위 Flow를 상속**받을 수 있다. 그러나, 자바 상속은 단일 클래스로 제한된다.

### Flow 상속 타입

#### Flow 수준 상속

Flow 수준 상속은 flow 내에 parent 속성을 이용하여 정의한다. 이 속성은 콤마로 구분하여 상속받을 Flow를 표현한다.
하위 flow는 목록에 명시된 순서대로 각각의 상위 Flow를 상속받는다.
첫 번째 상속으로 상위 Flow에 있는 요소와 내용을 추가하고 나면 그것을 다시 하위 Flow로 간주하고 그 다음 상위 flow를 상속 받는다.
아래 예를 보면 common-transitions를 먼저 상속 받고 다음에 common-states를 상속 받는다.

```xml
<flow parent="common-transitions, common-states">
```

#### State 수준 상속

State 수준 상속은 Flow 수준 상속과 비슷하다. 유일한 차이점은 Flow 전체가 아니라 오직 해당 **State 하나만 상위로부터 상속**받는다.
Flow 상속과 달리 오직 하나의 상위만 허용한다. 또한 상속받을 Flow State의 식별자가 반드시 정의되어 있어야 한다.
Flow와 State 식별자는 #로 구분한다.
**상위와 하위 State는 반드시 같은 타입이어야 한다.** 예를 들어 view-state는 ent-state를 상속받을 수 없다. 오직 view-state만 상속받을 수 있다


```xml
<view-state id="child-state" parent="parent-flow#parent-view-state">
```

### 추상 Flow

종종 상위 Flow는 직접 호출하지 않도록 설계한다. 그런 Flow를 실행하지 못하도록 abstract로 설정할 수 있다.
만약 추상 Flow를 실행하려고 하면 FlowBuilderException가 발생한다.

```xml
<flow abstract="true">
```

### 상속 알고리즘

하위 Flow가 상위 Flow를 상속할 때 발생하는 기본적인 일은 상위와 하위 Flow를 병합하여 새로운 Flow를 만드는 것이다.
웹 Flow 정의 언어에는 각각의 엘리먼트에 대해 어떻게 병합할 것인가에 대한 규칙이 있다.
엘리먼트에는 두 종류가 있다. 병합 가능한 것(mergeable)과 병합이 가능하지 않은 것(non-mergeable)이 있다.
병합 가능(mergeable)한 엘리먼트는 만약 엘리먼트가 같다면 병합을 시도한다. 병합이 가능하지 않은(non-mergeable) 엘리먼트는 항상 최종 Flow에 직접 포함된다.
병합 과정 중에 수정하지 않는다.

#### 주의 

- 상위 Flow에 있는 외부 리소스 경로는 절대 경로여야 한다. ** 상대 경로는 두 Flow를 병합할 때 상위 Flow와 하위 Flow가 위치한 디렉토리가 다르면 깨질 수 있다. 일반 병합하면, 상위 Flow에 있던 모든 상대 경로는 하위 Flow 기준으로 바뀐다.

#### 병합 가능한(mergeable) 엘리먼트

만약 같은 타입의 엘리먼트고 입력한 속성이 같다면 상위 엘리먼트의 내용을 하위 엘리먼트로 병합한다.
병합 알고리즘은 계속해서 병합하는 상위와 하위의 서브 엘리먼트를 각각 병합한다.
그렇지 않으면 상위 Flow의 엘리먼트를 하위 Flow에 새로운 엘리먼트로 추가한다.

대부분의 경우 상위 flow의 엘리먼트가 하위 Flow 엘리먼트에 추가된다.
이 규칙에 예외로는 시작할 때 추가될 action 엘리먼트(evaluate, render, set)가 있다. 상위 action의 결과를 하위 action 결과로 사용하게 한다.

병합이 가능한 엘리먼트는 다음과 같다.

- action-state: id
- attribute: name
- decision-state: id
- end-state: id
- flow: 항상 병합
- if: test
- on-end: 항상 병합
- on-entry: 항상 병합
- on-exit: 항상 병합
- on-render: 항상 병합
- on-start: 항상 병합
- input: name
- output: name
- secured: attributes
- subflow-state: id
- transition: on and on-exception
- view-state: id

#### 병합할 수 없는 엘리먼트

병합할 수 없는 엘리먼트는 다음과 같다

- bean-import
- evaluate
- exception-handler
- persistence-context
- render
- set
- var

## 참고자료

- [Spring Web Flow reference 2.0.x](http://static.springframework.org/spring-webflow/docs/2.0.x/reference/html/index.html) (링크 만료)
- Spring Web-Flow Framework Reference beta with Korean (by 박찬욱)
- [Whiteship's Note](http://whiteship.me/2146) (링크 만료)