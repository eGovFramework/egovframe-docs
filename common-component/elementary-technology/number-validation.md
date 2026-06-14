---
title: "숫자유효성검사"
linkTitle: "숫자유효성검사"
description: "숫자유효성검사"
url: /common-component/elementary-technology/system/number-validation/
menu:
  depth:
    name: "숫자유효성검사"
    weight: 56
    parent: "system"
---

## 개요

문자열 데이터가 올바른 숫자(정수, 실수 등) 형식을 갖추고 있는지 유효성을 검사하는 기능을 제공한다.

## 주요 기능

* **숫자 여부 확인**: 문자열이 숫자로만 구성되어 있는지 판별한다.
* **형식 유효성 검증**: 음수, 양수, 실수 등의 구체적인 숫자 형식을 만족하는지 확인한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `boolean` | `checkNumber(String source)` | 지정된 문자열이 숫자로 구성되어 있는지 유효성을 검증한다. |

```java
import egovframework.com.utl.fcc.service.EgovNumberCheckUtil;

public class NumberValidationExample {
    public void validateNumber() {
        String numStr1 = "12345";
        String numStr2 = "123A5";
        
        System.out.println("numStr1 is number? " + EgovNumberCheckUtil.checkNumber(numStr1)); // true
        System.out.println("numStr2 is number? " + EgovNumberCheckUtil.checkNumber(numStr2)); // false
    }
}
```
