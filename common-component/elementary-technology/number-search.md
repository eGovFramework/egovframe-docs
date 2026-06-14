---
title: "숫자치환"
linkTitle: "숫자치환"
description: "숫자치환"
url: /common-component/elementary-technology/system/number-search/
menu:
  depth:
    name: "숫자치환"
    weight: 55
    parent: "system"
---

## 개요

문자열 또는 데이터 내에서 지정된 숫자(패턴)를 찾아내거나 이를 다른 숫자로 치환(Replace) 및 조작하는 기능을 제공한다.

## 주요 기능

* **숫자 검색**: 문자열 내에서 특정 숫자 문자가 존재하는지 찾는다.
* **문자열 내 숫자 치환**: 지정한 숫자 패턴을 찾아 새로운 숫자로 일괄 변경한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `replaceNumber(String source, int targetStr, int replaceStr)` | 원본 문자열에서 대상 숫자를 찾아 변경할 숫자로 치환하여 반환한다. |
| `int` | `checkNumber(String source, int searchNum)` | 문자열 안에서 특정 숫자가 처음 나타나는 위치 인덱스를 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovNumberCheckUtil;

public class NumberSearchExample {
    public void searchAndReplace() {
        String data = "Hello123World123";
        
        // 숫자 치환 (123 -> 999)
        // 실제 유틸리티의 파라미터 타입이나 이름에 따라 구현 방식은 달라질 수 있습니다.
        String replaced = EgovNumberCheckUtil.replaceNumber(data, 123, 999);
        System.out.println("Replaced Data: " + replaced);
    }
}
```
