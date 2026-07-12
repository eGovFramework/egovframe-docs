---
title: "랜덤숫자구하기"
linkTitle: "랜덤숫자구하기"
description: "랜덤숫자구하기"
url: /common-component/elementary-technology/formatter-util/random-number/
menu:
  depth:
    name: "랜덤숫자구하기"
    weight: 7
    parent: "formatter-util"
---

# 랜덤 숫자

## 개요

랜덤 숫자는 시작값과 종료값 사이의 임의의 숫자를 생성하는 요소기술이다.

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovNumberUtil.java | Number 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getRandomNum(int startNum, int endNum)` | `int` | 시작값과 종료값 사이의 임의의 숫자를 반환한다 |

## 사용 예

```java
int n = EgovNumberUtil.getRandomNum(1, 100); // 1~100 사이 임의 숫자
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
