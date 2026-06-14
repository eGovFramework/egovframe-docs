---
title: "타임스탬프생성"
linkTitle: "타임스탬프생성"
description: "타임스탬프생성"
url: /common-component/elementary-technology/system/timestamp-value/
menu:
  depth:
    name: "타임스탬프생성"
    weight: 72
    parent: "system"
---

## 개요

현재 시간이나 특정 날짜를 기준으로 시스템 고유의 타임스탬프(Timestamp) 값을 생성하여 반환하는 기능을 제공한다. 주로 고유 파일명 생성이나 거래 식별 키 생성에 사용된다.

## 주요 기능

* **현재 타임스탬프**: 밀리초(millisecond) 또는 지정된 형식(yyyyMMddHHmmssSSS 등)으로 현재 시간을 추출한다.
* **시간 포맷팅**: 날짜 및 시간을 조합하여 사람이 읽기 쉬운 형태의 고유 시간 문자열을 만든다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `getTimeStamp()` | 현재 시스템 시간을 기반으로 yyyyMMddHHmmssSSS 형식의 타임스탬프 문자열을 생성한다. |

```java
import egovframework.com.utl.fcc.service.EgovDateUtil;

public class TimestampValueExample {
    public void generateTimestamp() {
        // 현재 시간에 대한 타임스탬프 조회
        // 실제 유틸리티의 메서드명은 다를 수 있습니다.
        String timestamp = EgovDateUtil.getCurrentDateTime(); 
        System.out.println("Generated Timestamp: " + timestamp);
    }
}
```
