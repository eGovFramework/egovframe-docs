---
title: "XML데이터파싱"
linkTitle: "XML데이터파싱"
description: "XML데이터파싱"
url: /common-component/elementary-technology/system/xml-data-parsing/
menu:
  depth:
    name: "XML데이터파싱"
    weight: 76
    parent: "system"
---

## 개요

문자열이나 파일 형태로 제공되는 XML(eXtensible Markup Language) 데이터를 읽어들여 DOM 구조로 파싱하고, 특정 태그명이나 속성에 해당하는 데이터를 추출하는 기능을 제공한다.

## 주요 기능

* **XML 문서 파싱**: 입력된 XML 문자열을 파싱하여 메모리 상의 `Document` 객체로 변환한다.
* **노드 데이터 추출**: 변환된 XML `Document`에서 특정 엘리먼트(태그)명에 해당하는 텍스트 값들을 추출한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `String` | `getXMLData(String xmlStr, String nodeName)` | 주어진 XML 문자열에서 특정 노드명에 해당하는 첫 번째 값을 파싱하여 반환한다. |

```java
import egovframework.com.utl.fcc.service.EgovXMLDoc;

public class XmlDataParsingExample {
    public void parseXml() throws Exception {
        String xmlStr = "<users><user>Hong</user><user>Kim</user></users>";
        String nodeName = "user";
        
        // XML 데이터 파싱 및 첫 번째 노드 값 추출
        String data = EgovXMLDoc.getXMLData(xmlStr, nodeName);
        System.out.println("Parsed Data for <" + nodeName + ">: " + data);
    }
}
```
