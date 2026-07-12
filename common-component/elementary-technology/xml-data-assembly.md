---
title: "XML 데이터조립"
linkTitle: "XML 데이터조립"
description: "XML 데이터조립"
url: /common-component/elementary-technology/system/xml-data-assembly/
menu:
  depth:
    name: "XML 데이터조립"
    weight: 47
    parent: "system"
---

## 개요

일반 구조적 형태의 데이터를 XML 데이터로 조립하여 파일로 저장하는 기능을 제공한다.
웹서비스(Web Service), 전자문서, 데이터교환과 같은 응용 애플리케이션에서 사용할 수 있다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

XML 데이터조립에서 제공하는 기능은 다음과 같다.

1. 일반 구조적 형태의 데이터(자바 객체)를 XML 데이터로 조립하여 파일로 저장하는 기능
2. Document 객체 기반으로 Element·Text 노드를 생성·조작하여 XML 파일로 저장하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovXMLDoc.java` | XML파싱/조립 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovXMLDoc.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

XML 데이터조립 기능은 `EgovXMLDoc` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `getClassToXML(SndngMailDocument mailDoc, String file)` | XML조립 | 객체(예제: 메일발송 클래스)의 데이터를 XML파일로 저장 |
| boolean | `getXMLFile(Document document, String file)` | XML조립 | Document 객체를 XML파일로 저장 |
| Document | `getXMLDocument(String xml)` | XML파싱 | XML 파일을 파싱하여 조작 가능한 Document 객체를 반환 |
| Element | `getRootElement(Document document)` | ROOT이동 | Document의 최상위 Element로 이동 |
| Element | `insertElement(Document document, Element rt, String id)` | 노드생성 | 하위에 새로운 Element를 생성 |
| Element | `insertElement(Document document, Element rt, String id, String text)` | 문자열노드생성 | 하위에 문자열을 가지는 새로운 Element를 생성 |
| Text | `insertText(Document document, Element rt, String text)` | 문자열추가 | 하위에 문자열을 추가 |
| Element | `getParentNode(Element current)` | 상위노드반환 | 마지막으로 입력·참조된 XML Node의 상위 Element를 리턴 |
<!-- markdownlint-restore -->

#### 반환값 정의 (Output)

- boolean 타입: 조립(저장) 성공 여부 (`true` / `false`)

### 사용 방법

예제는 XML 스키마로 생성한 메일정보 클래스(`SndngMailDocument`)에 데이터를 담아 XML 파일로 조립하는 방식이다.

```java
import egovframework.com.utl.sim.service.EgovXMLDoc;

SndngMailDocument mailDoc = SndngMailDocument.Factory.newInstance();
SndngMailDocument.SndngMail mailElement = mailDoc.addNewSndngMail();
mailElement.setDsptchPerson("example1@example.com");
mailElement.setRecptnPerson("example2@example.com");
mailElement.setSj("test mail");
mailElement.setEmailCn("This is test mail.");
mailElement.setSndngResultCode("R");

boolean result = EgovXMLDoc.getClassToXML(mailDoc, "/user/com/test/mail_result.xml");
```

## 환경설정

XML 스키마 기반 클래스 생성을 위해 Apache XMLBeans 라이브러리를 사용한다. 자세한 스키마 컴파일 절차는
[XML 데이터파싱](../xml-data-parsing/) 문서의 환경설정을 참조한다.

## 참고자료

- [XML 데이터파싱](../xml-data-parsing/)
- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
