---
title: "XML 데이터파싱"
linkTitle: "XML 데이터파싱"
description: "XML 데이터파싱"
url: /common-component/elementary-technology/system/xml-data-parsing/
menu:
  depth:
    name: "XML 데이터파싱"
    weight: 48
    parent: "system"
---

## 개요

XML 파일을 로드한 후 XML 데이터를 파싱하여 구조적인 데이터 형태로 변환하는 기능을 제공한다.
웹서비스(Web Service), 전자문서, 데이터교환과 같은 응용 애플리케이션에서 사용할 수 있다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

XML 데이터파싱에서 제공하는 기능은 다음과 같다.

1. XML 스키마 구조를 읽어 이에 맞는 자바클래스(JAR)를 생성하는 기능
2. XML 데이터를 파싱하여 구조적인 데이터 형태(자바 객체·Document)로 변환하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovXMLDoc.java` | XML파싱/조립 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovXMLDoc.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

XML 데이터파싱 기능은 `EgovXMLDoc` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `creatSchemaToClass(String xml, String ja)` | 클래스생성 | XML스키마 구조를 읽어 이에 맞는 자바클래스(JAR)를 생성 |
| SndngMailDocument | `getXMLToClass(String file)` | XML파싱 | XML파일을 파싱하여 객체(예제: 메일발송 클래스)에 내용을 담아 반환 |
| Document | `getXMLDocument(String xml)` | XML파싱 | XML 파일을 파싱하여 조작 가능한 Document 객체를 반환 |
| Element | `getRootElement(Document document)` | ROOT이동 | Document의 최상위 Element로 이동 |
| Element | `getParentNode(Element current)` | 상위노드반환 | 마지막으로 입력·참조된 XML Node의 상위 Element를 리턴 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- XML스키마 파일: String 타입의 절대경로 (예: `/user/com/test/mail.xsd`)
- 생성 JAR 경로: String 타입의 절대경로 (예: `/user/com/test/mail.jar`)
- XML데이터 파일: String 타입의 절대경로 (예: `/user/com/test/mail_data.xml`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovXMLDoc;

// 1. 스키마 파일을 읽어 자바 클래스(JAR) 생성
boolean result = EgovXMLDoc.creatSchemaToClass("/user/com/test/mail.xsd", "/user/com/test/mail.jar");

// 2. XML 파일의 데이터를 읽어 객체로 파싱
SndngMailDocument mailDoc = EgovXMLDoc.getXMLToClass("/user/com/test/mail_data.xml");
SndngMailDocument.SndngMail mailElement = mailDoc.getSndngMail();

String dsptchPerson = mailElement.getDsptchPerson();  // 발신자
String recptnPerson = mailElement.getRecptnPerson();  // 수신자
String sj = mailElement.getSj();                      // 제목
```

## 환경설정

XML 스키마 컴파일을 위해 [Apache XMLBeans](https://xmlbeans.apache.org/) 라이브러리를 사용한다.

```text
# 시스템변수 및 PATH 설정 (윈도우 예시)
set XMLBEANS_HOME=C:\xmlbeans-2.0.0
set PATH=%XMLBEANS_HOME%\bin;%JAVA_HOME%\bin;

# 스키마 파일 컴파일 (JAR 생성: -out, 소스 생성: -src)
scomp -out target.jar source.xsd
```

XML 스키마(`.xsd`)로 생성된 JAR를 시스템에 추가한 뒤, 해당 클래스로 XML 데이터를 파싱·조립한다.

## 참고자료

- [XML 데이터조립](../xml-data-assembly/)
- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
