---
title: "랜덤문자열구하기"
linkTitle: "랜덤문자열구하기"
description: "랜덤문자열구하기"
url: /common-component/elementary-technology/formatter-util/random-string/
menu:
  depth:
    name: "랜덤문자열구하기"
    weight: 6
    parent: "formatter-util"
---

# 랜덤 문자열

## 개요

랜덤 문자열은 시작 문자와 종료 문자 사이의 임의의 문자열을 생성하는 요소기술이다.

### 활용 예시

랜덤 문자열 생성 기능은 다음과 같은 상황에서 활용할 수 있다.

- 테스트용 문자 데이터를 생성하는 경우
- 지정된 문자 범위 내에서 임의의 문자가 필요한 경우
- 샘플 데이터나 임시 식별값을 생성하는 경우

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovStringUtil.java | String 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getRandomStr(char startChr, char endChr)` | `String` | 문자열 A에서 Z사이의 랜덤 문자열을 구하는 기능을 제공 시작문자열과 종료문자열 사이의 랜덤 문자열을 구하는 기능 |

### 입력값 (Input)

- `startChr`: 랜덤 값 생성 범위의 시작 문자
- `endChr`: 랜덤 값 생성 범위의 종료 문자

### 반환값 (Output)

- `String`: 지정한 문자 범위에서 생성된 임의의 문자열

## 사용 예

```java
import egovframework.com.utl.fcc.service.EgovStringUtil;

char startChr = 'A';
char endChr = 'Z';

String randomString = EgovStringUtil.getRandomStr(startChr, endChr);
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
