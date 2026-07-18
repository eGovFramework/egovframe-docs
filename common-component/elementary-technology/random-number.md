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

### 활용 예시

랜덤 숫자 생성 기능은 다음과 같은 상황에서 활용할 수 있다.

- 테스트용 숫자 데이터를 생성하는 경우
- 지정된 범위 내에서 임의의 숫자가 필요한 경우
- 샘플 데이터나 시뮬레이션 데이터를 생성하는 경우

## 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| 유틸리티 | egovframework.com.utl.fcc.service.EgovNumberUtil.java | Number 처리 유틸리티 클래스 |

## 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `getRandomNum(int startNum, int endNum)` | `int` | 시작값과 종료값 사이의 임의의 숫자를 반환한다 |

### 입력값 (Input)

- `startNum`: 랜덤 숫자 생성 범위의 시작값
- `endNum`: 랜덤 숫자 생성 범위의 종료값

### 반환값 (Output)

- `int`: 지정한 범위 내에서 생성된 임의의 숫자

## 사용 예

```java
import egovframework.com.utl.fcc.service.EgovNumberUtil;

int startNum = 1;
int endNum = 100;

int randomNumber = EgovNumberUtil.getRandomNum(startNum, endNum);
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
