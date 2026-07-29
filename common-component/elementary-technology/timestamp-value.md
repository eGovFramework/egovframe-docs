---
title: "TIMESTAMP값구하기"
linkTitle: "TIMESTAMP값구하기"
description: "TIMESTAMP값구하기"
url: /common-component/elementary-technology/formatter-util/timestamp-value/
menu:
  depth:
    name: "TIMESTAMP값구하기"
    weight: 24
    parent: "formatter-util"
---

# TIMESTAMP값구하기

## 개요

TIMESTAMP값은 응용 프로그램에서 고유한 식별값이 필요할 때 시스템 시각을 기반으로 17자리 TIMESTAMP 문자열을 생성하는 기능을 제공한다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovStringUtil.java | String 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getTimeStamp()` | `String` | 시스템 시각을 기반으로 17자리 TIMESTAMP 문자열을 생성하여 반환한다. |

## 사용 예

```java
String ts = EgovStringUtil.getTimeStamp(); // 예시: 20260711153021123 (17자리)
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
