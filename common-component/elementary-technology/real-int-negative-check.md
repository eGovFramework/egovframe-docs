---
title: "실수정수음수체크"
linkTitle: "실수정수음수체크"
description: "실수정수음수체크"
url: /common-component/elementary-technology/system/real-int-negative-check/
menu:
  depth:
    name: "실수정수음수체크"
    weight: 63
    parent: "system"
---

## 개요

문자열 형태의 데이터가 나타내는 숫자의 특성(실수, 정수, 음수 여부 등)을 정확하게 판별하고 검증하는 기능을 제공한다.

## 주요 기능

* **실수 확인**: 소수점을 포함하는 실수 형태인지 확인한다.
* **정수 확인**: 소수점이 없는 양의 정수인지 확인한다.
* **음수 확인**: 마이너스(-) 부호가 포함된 음수인지 여부를 검사한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `boolean` | `checkFormatReal(String source)` | 지정된 문자열이 실수 형식인지 확인한다. |
| `boolean` | `checkFormatInteger(String source)` | 지정된 문자열이 정수 형식인지 확인한다. |
| `boolean` | `checkFormatNegative(String source)` | 지정된 문자열이 음수 형식인지 확인한다. |

```java
import egovframework.com.utl.fcc.service.EgovFormatCheckUtil;

public class RealIntNegativeCheckExample {
    public void checkNumberType() {
        String num1 = "-10";
        String num2 = "3.14";
        
        System.out.println("Is '-10' Negative? " + EgovFormatCheckUtil.checkFormatNegative(num1));
        System.out.println("Is '3.14' Real? " + EgovFormatCheckUtil.checkFormatReal(num2));
    }
}
```
