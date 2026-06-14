---
title: "문자열검색"
linkTitle: "문자열검색"
description: "문자열검색"
url: /common-component/elementary-technology/system/string-search/
menu:
  depth:
    name: "문자열검색"
    weight: 69
    parent: "system"
---

## 개요

전체 문자열 내에서 특정 문자 또는 서브 스트링(Substring)이 존재하는 위치(Index)를 찾거나, 해당 패턴이 몇 번 등장하는지 카운트하는 기능을 제공한다.

## 주요 기능

* **위치 인덱스 검색**: 문자열 내에서 찾고자 하는 문자가 처음 또는 마지막으로 등장하는 위치를 확인한다.
* **등장 횟수 계산**: 전체 문자열 안에서 특정 문자열 패턴이 몇 번 반복되는지 셈한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `int` | `indexOf(String source, String str)` | source 문자열 내에서 str이 처음 시작되는 인덱스를 반환한다. |
| `int` | `getEncdCmt(String source, String str)` | source 문자열 내에 str 패턴이 몇 번 포함되어 있는지 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovStringUtil;

public class StringSearchExample {
    public void searchString() {
        String text = "abc def abc ghi";
        
        // 검색 대상 위치 찾기
        int index = EgovStringUtil.indexOf(text, "def");
        System.out.println("Index of 'def': " + index);
    }
}
```
