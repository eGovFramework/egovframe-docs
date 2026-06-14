---
title: "특수문자처리"
linkTitle: "특수문자처리"
description: "특수문자처리"
url: /common-component/elementary-technology/system/special-string-processing/
menu:
  depth:
    name: "특수문자처리"
    weight: 66
    parent: "system"
---

## 개요

웹 환경에서 보안 취약점(XSS 등)을 방지하거나 데이터의 원형을 보존하기 위해 HTML 태그나 특수문자를 적절한 형태(Entity 등)로 치환하고 복원하는 기능을 제공한다.

## 주요 기능

* **HTML 태그 제거**: 입력된 문자열에서 모든 HTML 태그를 식별하여 제거한다.
* **XSS 방지 처리**: `<` 나 `>` 와 같은 특수 기호를 `&lt;`, `&gt;` 로 치환하여 스크립트 실행을 차단한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `getHtmlStrCnvr(String source)` | 문자열 내의 특수 기호를 HTML Entity 표기로 변환하여 반환한다. |
| `String` | `removeHtml(String source)` | 문자열에 포함된 HTML 태그를 모두 제거하고 순수 텍스트만 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovStringUtil;

public class SpecialStringExample {
    public void processString() {
        String input = "<script>alert('XSS');</script>";
        
        // 태그 제거
        String noHtml = EgovStringUtil.removeHtml(input);
        System.out.println("Removed HTML: " + noHtml);
        
        // 치환 (XSS 방어)
        String safeHtml = EgovStringUtil.getHtmlStrCnvr(input);
        System.out.println("Safe HTML: " + safeHtml);
    }
}
```
