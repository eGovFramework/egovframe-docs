---
title: "실수/정수/음수체크"
linkTitle: "실수/정수/음수체크"
description: "실수/정수/음수체크"
url: /common-component/elementary-technology/formatter-util/real-int-negative-check/
menu:
  depth:
    name: "실수/정수/음수체크"
    weight: 19
    parent: "formatter-util"
---

# 실수/정수/음수 체크

## 개요

실수/정수/음수 체크는 특정 숫자가 실수인지, 정수인지, 음수인지 판별하는 요소기술이다.

### 활용 예시

실수/정수/음수 체크 기능은 다음과 같은 상황에서 활용할 수 있다.

- 입력된 숫자의 유형을 판별하는 경우
- 숫자 데이터의 특성에 따라 처리 로직을 구분하는 경우
- 수치 데이터를 검증하거나 분류하는 경우

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovNumberUtil.java | Number 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `checkRlnoInteger(double srcNumber)` | `int` | 입력된 숫자가 실수, 정수 또는 음수인지 판별하는 기능을 제공한다. |

### 입력값 (Input)

- `srcNumber`: 실수, 정수 또는 음수 여부를 판별할 숫자

### 반환값 (Output)

- `int`: 입력된 숫자의 유형을 판별한 결과값

## 사용 예

```java
import egovframework.com.utl.fcc.service.EgovNumberUtil;

double srcNumber = 123;
int type = EgovNumberUtil.checkRlnoInteger(srcNumber);
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
