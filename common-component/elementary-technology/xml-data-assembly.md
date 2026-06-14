---
title: "XML데이터조합"
linkTitle: "XML데이터조합"
description: "XML데이터조합"
url: /common-component/elementary-technology/system/xml-data-assembly/
menu:
  depth:
    name: "XML데이터조합"
    weight: 75
    parent: "system"
---

## 개요

시스템 간의 데이터 연계나 설정 파일 생성을 위해 Java 객체나 Map 형식의 데이터를 기반으로 XML 형식의 문자열(String) 또는 문서를 동적으로 생성(조합)하는 기능을 제공한다.

## 주요 기능

* **XML 엘리먼트 생성**: 사용자 정의 태그와 속성을 가진 XML 노드를 동적으로 추가하고 구조를 구성한다.
* **Document 빌드**: DOM 기반으로 문서를 작성하고 최종적으로 XML 문자열 형태로 변환하여 반환한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `makeXMLString(Map<String, String> data)` | 주어진 맵 데이터를 XML 포맷의 문자열로 조합하여 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovXMLDoc;

public class XmlDataAssemblyExample {
    public void createXml() {
        // XML 데이터 생성 예시
        // 내부 구현에 따라 DocumentBuilder 등을 활용
        String rootElement = "users";
        String childElement = "user";
        String value = "Hong Gil Dong";
        
        // 간단한 문자열 조합 방식
        StringBuilder xmlBuilder = new StringBuilder();
        xmlBuilder.append("<").append(rootElement).append(">");
        xmlBuilder.append("<").append(childElement).append(">").append(value).append("</").append(childElement).append(">");
        xmlBuilder.append("</").append(rootElement).append(">");
        
        System.out.println("Generated XML: \n" + xmlBuilder.toString());
    }
}
```
