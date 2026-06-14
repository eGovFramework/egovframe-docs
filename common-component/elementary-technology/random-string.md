---
title: "랜덤문자열생성"
linkTitle: "랜덤문자열생성"
description: "랜덤문자열생성"
url: /common-component/elementary-technology/system/random-string/
menu:
  depth:
    name: "랜덤문자열생성"
    weight: 62
    parent: "system"
---

## 개요

지정된 길이의 무작위 문자열(알파벳 대소문자, 숫자 포함 등)을 생성하는 기능을 제공한다. 비밀번호 초기화, 고유 식별자 생성 등 다양한 목적으로 활용된다.

## 주요 기능

* **임의 길이의 문자열 조합**: 사용자가 원하는 자릿수만큼의 랜덤 영문/숫자 조합 문자열을 생성한다.
* **식별 키 생성**: 세션 또는 일회성 비밀번호 발급 등에 사용될 수 있는 안전한 랜덤 값을 부여한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `getRandomStr(char type, int length)` | 문자, 숫자 등 지정한 타입과 길이에 맞추어 무작위 문자열을 생성하여 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovStringUtil;

public class RandomStringExample {
    public void generateRandomString() {
        // 영숫자 조합 10자리 난수 생성 등
        String randomStr = EgovStringUtil.getRandomStr('A', 10);
        System.out.println("Random String: " + randomStr);
    }
}
```
