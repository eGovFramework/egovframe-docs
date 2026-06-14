---
title: "랜덤날짜생성"
linkTitle: "랜덤날짜생성"
description: "랜덤날짜생성"
url: /common-component/elementary-technology/system/random-date/
menu:
  depth:
    name: "랜덤날짜생성"
    weight: 60
    parent: "system"
---

## 개요

지정된 두 날짜(시작일과 종료일) 사이의 구간에서 무작위로 날짜를 생성하여 반환하는 기능을 제공한다. 더미 데이터 생성이나 테스트 목적으로 주로 활용된다.

## 주요 기능

* **기간 내 무작위 날짜 추출**: 입력받은 시작일자 문자열과 종료일자 문자열 범위 내에 존재하는 임의의 날짜를 계산한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `getRandomDate(String startDate, String endDate)` | 시작일과 종료일 사이의 무작위 일자를 지정된 포맷(YYYYMMDD)으로 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovDateUtil;

public class RandomDateExample {
    public void generateRandomDate() throws Exception {
        String startDate = "20260101";
        String endDate = "20261231";
        
        // 2026년 중 임의의 날짜 생성
        String randomDate = EgovDateUtil.getRandomDate(startDate, endDate);
        System.out.println("Random Date between " + startDate + " and " + endDate + ": " + randomDate);
    }
}
```
