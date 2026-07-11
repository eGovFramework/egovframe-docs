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

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovNumberUtil.java | Number 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `checkRlnoInteger(double srcNumber)` | `int` | 특정숫자가 실수인지, 정수인지, 음수인지 체크하는 기능 123이 실수인지, 정수인지, 음수인지 체크하는 기능을 제공함 |

## 사용 예

```java
int type = EgovNumberUtil.checkRlnoInteger("123"); // 실수/정수/음수 판별
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
