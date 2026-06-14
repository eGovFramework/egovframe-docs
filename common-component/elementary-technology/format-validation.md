---
title: "형식유효성검사"
linkTitle: "형식유효성검사"
description: "형식유효성검사"
url: /common-component/elementary-technology/system/format-validation/
menu:
  depth:
    name: "형식유효성검사"
    weight: 47
    parent: "system"
---

## 개요

문자열 데이터가 사전에 정의된 특정 형식(전화번호, 주민등록번호, 이메일 등)에 일치하는지 유효성을 검증하는 기능을 제공한다.

## 주요 기능

* **전화번호 검증**: 휴대폰 번호 및 일반 전화번호 형식을 확인한다.
* **이메일 검증**: 이메일 주소의 문자열 포맷이 올바른지 확인한다.
* **날짜 검증**: 문자열이 유효한 날짜 형식(YYYYMMDD 등)인지 확인한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `boolean` | `checkFormatEmail(String email)` | 입력된 문자열이 이메일 형식에 부합하는지 검사한다. |
| `boolean` | `checkFormatPhone(String phone)` | 입력된 문자열이 전화번호 형식에 부합하는지 검사한다. |

```java
import egovframework.com.utl.fcc.service.EgovFormatCheckUtil;

public class FormatValidationExample {
    public void validateFormat() {
        String email = "test@egovframe.go.kr";
        boolean isValidEmail = EgovFormatCheckUtil.checkFormatEmail(email);
        System.out.println("Valid Email? " + isValidEmail);
        
        String phone = "010-1234-5678";
        boolean isValidPhone = EgovFormatCheckUtil.checkFormatPhone(phone);
        System.out.println("Valid Phone? " + isValidPhone);
    }
}
```
