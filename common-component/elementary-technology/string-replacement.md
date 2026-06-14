---
title: "문자열치환"
linkTitle: "문자열치환"
description: "문자열치환"
url: /common-component/elementary-technology/system/string-replacement/
menu:
  depth:
    name: "문자열치환"
    weight: 68
    parent: "system"
---

## 개요

문자열 내에 포함된 특정 단어나 패턴을 찾아 다른 단어나 문자로 일괄 교체(Replace)하는 기능을 제공한다. 데이터 정제 및 마스킹 시 활용할 수 있다.

## 주요 기능

* **단순 치환**: 원본 문자열에서 변경 대상 문자열을 찾아 일괄적으로 새 문자열로 바꾼다.
* **정규식 치환**: 정규 표현식을 지원하여 패턴에 일치하는 모든 문자열을 치환한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `replace(String source, String subject, String object)` | source 내의 subject를 object로 치환하여 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovStringUtil;

public class StringReplacementExample {
    public void replaceString() {
        String original = "Hello egovframe, egovframe is great.";
        String target = "egovframe";
        String replacement = "eGovFramework";
        
        // 문자열 치환 수행
        String result = EgovStringUtil.replace(original, target, replacement);
        System.out.println("Result: " + result);
    }
}
```
