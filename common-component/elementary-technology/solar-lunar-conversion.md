---
title: "음력양력변환"
linkTitle: "음력양력변환"
description: "음력양력변환"
url: /common-component/elementary-technology/system/solar-lunar-conversion/
menu:
  depth:
    name: "음력양력변환"
    weight: 65
    parent: "system"
---

## 개요

입력된 양력(Solar) 날짜를 음력(Lunar) 날짜로 변환하거나, 반대로 음력 날짜를 양력 날짜로 상호 변환하는 기능을 제공한다.

## 주요 기능

* **양력 -> 음력 변환**: 양력 기준의 날짜(YYYYMMDD)를 입력 받아 해당하는 음력 날짜와 윤달 여부를 반환한다.
* **음력 -> 양력 변환**: 음력 기준의 날짜(윤달 포함)를 입력 받아 정확한 양력 날짜로 계산해 반환한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `toLunar(String solarDate)` | 지정된 양력 날짜를 음력 날짜 문자열로 변환하여 반환한다. |
| `String` | `toSolar(String lunarDate, int leapMonth)` | 지정된 음력 날짜를 양력 날짜 문자열로 변환하여 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovDateUtil;

public class SolarLunarConversionExample {
    public void convertDate() throws Exception {
        String solarDate = "20260101";
        
        // 양력을 음력으로 변환 (윤달 여부 등에 따라 구현 파라미터가 다를 수 있음)
        String lunarDate = EgovDateUtil.toLunar(solarDate);
        System.out.println("Solar " + solarDate + " is Lunar " + lunarDate);
    }
}
```
