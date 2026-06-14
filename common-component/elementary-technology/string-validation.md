---
title: "문자열유효성검사"
linkTitle: "문자열유효성검사"
description: "문자열유효성검사"
url: /common-component/elementary-technology/system/string-validation/
menu:
  depth:
    name: "문자열유효성검사"
    weight: 70
    parent: "system"
---

## 개요

전달받은 문자열이 Null이거나 비어 있는지(Empty), 또는 특정 길이 조건을 만족하는지 여부를 판단하여 데이터의 유효성을 검사하는 기능을 제공한다.

## 주요 기능

* **Null 및 공백 확인**: 문자열이 null 객체이거나, 양쪽 공백을 제거했을 때 길이가 0인지 점검한다.
* **길이 제한 검사**: 문자열의 바이트 수 혹은 문자 개수가 허용 범위 내에 있는지 판단한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `boolean` | `isEmpty(String source)` | 파라미터로 넘어온 문자열이 null 이거나 공백 문자열("")인지 확인한다. |
| `boolean` | `isNumeric(String source)` | 파라미터가 숫자로만 구성되어 있는지 확인한다. |

```java
import egovframework.com.utl.fcc.service.EgovStringUtil;

public class StringValidationExample {
    public void checkValidity() {
        String str1 = "";
        String str2 = "  ";
        
        System.out.println("str1 is Empty? " + EgovStringUtil.isEmpty(str1)); // true
        // 구현에 따라 스페이스만 있는 경우의 처리 방식이 다를 수 있습니다.
        System.out.println("str2 is Empty? " + EgovStringUtil.isEmpty(str2.trim())); // true
    }
}
```
