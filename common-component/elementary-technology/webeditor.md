---
title: "웹에디터"
linkTitle: "웹에디터"
description: "웹 브라우저상의 입력 폼에서 텍스트 및 HTML 콘텐츠를 자유롭게 편집할 수 있도록 지원하는 위지윅(WYSIWYG) 에디터 컴포넌트"
url: /common-component/elementary-technology/webeditor/
menu:
  depth:
    weight: 8
    parent: "elementary-technology"
    identifier: "webeditor"
---

## 개요

웹에디터(WYSIWYG Editor) 컴포넌트는 게시판, 자료실, 공지사항 등 웹 브라우저상의 입력 폼에서 사용자가 자유롭게 콘텐츠를 편집할 수 있도록 지원하는 요소기술 컴포넌트이다.
텍스트 및 HTML 편집 기능을 제공하며, 이미지 업로드 및 편집기 내 이미지 표시 기능을 지원한다. 기존의 `HTMLArea`를 대체하여 현재는 오픈소스인 **CKEditor**를 기본 제공한다.

## 주요 개념

### 위지윅(WYSIWYG)

What You See Is What You Get의 약자로, 사용자가 화면에서 편집하고 있는 형태 그대로 출력되는 방식을 의미한다. 사용자는 HTML 태그를 직접 작성하지 않고도 서식이 적용된 문서를 작성할 수 있다.

### CKEditor

전자정부 표준프레임워크에서 기본으로 제공하는 오픈소스 웹 에디터이다. 다양한 브라우저 호환성을 제공하며, 플러그인 구조를 통해 기능을 확장할 수 있다.

## 설명

### 1. 라이브러리 설정

CKEditor를 사용하기 위해서는 프로젝트의 `pom.xml`에 관련 의존성을 추가해야 한다.

```xml
<dependency>
    <groupId>com.ckeditor</groupId>
    <artifactId>ckeditor-java-core</artifactId>
    <version>3.5.3</version>
</dependency>
```

### 2. JSP 페이지 적용

웹 페이지에 에디터를 적용하려면 JSP 상단에 태그 라이브러리를 선언하고, `<ckeditor:replace>` 태그를 사용하여 기존의 `<textarea>`를 에디터로 대체한다.

```jsp
<%@ taglib prefix="ckeditor" uri="http://ckeditor.com" %>

<!-- 텍스트 영역 폼 선언 -->
<form:textarea path="indvdlInfoDc" rows="10" cols="100" />

<!-- 에디터로 대체 -->
<ckeditor:replace replace="indvdlInfoDc" 
                  basePath="${pageContext.request.contextPath}/html/egovframework/com/cmm/utl/ckeditor/" />
```

### 3. 주요 설정 옵션

CKEditor는 속성 설정을 통해 다양한 커스터마이징이 가능하다.

- **인터페이스 색상 (`uiColor`)**: 에디터 툴바 및 테두리의 색상을 변경할 수 있다.
- **언어 설정 (`language`)**: 사용자 인터페이스의 언어를 지정한다. (예: `ko`)
- **엔터키 동작 (`enterMode` 및 `shiftEnterMode`)**: 사용자가 엔터(Enter)나 쉬프트+엔터(Shift+Enter)를 입력했을 때
  적용되는 태그(`ENTER_P`, `ENTER_BR`, `ENTER_DIV`)를 지정할 수 있다.
- **툴바 설정 (`config.toolbar`)**: 에디터 상단에 표시되는 도구 모음을 사용자가 원하는 기능만 노출되도록 재구성할 수 있다.

## 참고자료

- [CKEditor 공식 가이드](https://ckeditor.com/)
