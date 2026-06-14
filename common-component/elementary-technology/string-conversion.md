---
title: "문자열변환"
linkTitle: "문자열변환"
description: "문자열변환"
url: /common-component/elementary-technology/system/string-conversion/
menu:
  depth:
    name: "문자열변환"
    weight: 67
    parent: "system"
---

## 개요

데이터 포맷팅이나 화면 출력을 위해 문자열의 대소문자를 변경하거나 특정 포맷(날짜 문자열, 금액 표시 등)으로 변환하는 기능을 제공한다.

## 주요 기능

* **대소문자 변환**: 영문자열을 일괄적으로 대문자 또는 소문자로 변환한다.
* **포맷 기반 변환**: 구분자가 없는 날짜 문자열에 기호("-")를 삽입하거나, 금액 표기를 위해 콤마(",")를 추가한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `upperCase(String source)` | 문자열을 모두 대문자로 변환한다. |
| `String` | `lowerCase(String source)` | 문자열을 모두 소문자로 변환한다. |

```java
import egovframework.com.utl.fcc.service.EgovStringUtil;

public class StringConversionExample {
    public void convertString() {
        String data = "eGovFrame";
        
        System.out.println("UPPER: " + EgovStringUtil.upperCase(data));
        System.out.println("LOWER: " + EgovStringUtil.lowerCase(data));
    }
}
```
