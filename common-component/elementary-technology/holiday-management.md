---
title: "휴일관리"
linkTitle: "휴일관리"
description: "휴일관리"
url: /common-component/elementary-technology/system/holiday-management/
menu:
  depth:
    name: "휴일관리"
    weight: 48
    parent: "system"
---

## 개요

특정 날짜가 법정 공휴일이나 휴일로 지정된 날인지 확인하고, 시스템에 등록된 휴일 정보를 기준으로 날짜 계산을 수행하는 기능을 제공한다.

## 주요 기능

* **휴일 여부 확인**: 입력된 날짜가 휴일인지 여부를 boolean 값으로 리턴한다.
* **공휴일 정보 제공**: 설날, 추석, 국경일 등 법정 공휴일에 대한 정보를 체크한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `boolean` | `isHoliday(String date)` | 지정된 날짜(YYYYMMDD)가 휴일인지 확인한다. |

```java
import egovframework.com.utl.fcc.service.EgovDateUtil;

public class HolidayManagementExample {
    public void checkHoliday() throws Exception {
        // 2026년 3월 1일 (삼일절)
        String date = "20260301";
        
        // 해당 일자가 휴일인지 확인
        boolean isHoliday = EgovDateUtil.isHoliday(date);
        System.out.println("Is " + date + " a holiday? " + isHoliday);
    }
}
```
