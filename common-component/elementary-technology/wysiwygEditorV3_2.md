---
title: "WYSIWYG Editor(v3.2 신규)"
linkTitle: "WYSIWYG Editor(v3.2 신규)"
description: "게시판, 자료실의 메모장에서 사용자가 자유롭게 컨텐츠를 편집할 수 있는 기능의 컴포넌트을 제공한다."
url: /common-component/elementary-technology/webeditor/
menu:
  depth:
    weight: 1 ???
    parent: "webeditor"
    identifier: "wysiwygEditor"  ???
---

# 요소기술 - 위지윅 에디터(WYSIWYG Editor) 방지

## 개요

게시판, 자료실의 메모장에서 사용자가 자유롭게 컨텐츠를 편집할 수 있는 기능의 컴포넌트을 제공한다. 텍스트 및 HTML 편집 기능을 지원하고, 이미지 업로드 및 이미지를 편집기에 보여주는 기능이 있어야 한다. 웹 에디터는 웹 브라우저에서 게시판, 공지사항, 자료실, 사진첩과 같이 입력기능이 있는 곳에서 사용할 수 있다.

본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 중 **개인정보보호정책**의 등록 화면에 구성되어 있다.

## 설명

기존 사용하던 htmlarea를 ckeditor로 변경한다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| JS | webapp/html/egovframework/com/cmm/utl/ckeditor | 에디터 소스 |  |



## 환경설정

pom.xml 선언
```xml
    <dependency>
        <groupId>com.ckeditor</groupId>
        <artifactId>ckeditor-java-core</artifactId>
        <version>3.5.3</version>
    </dependency>
```

## 사용방법

taglib 선언
```jsp
<%@ taglib prefix="ckeditor" uri="http://ckeditor.com" %>
```

ckeditor:replace 선언(body 태그안에 선언해야 함)
```html
   <form:textarea path="indvdlInfoDc" rows="75" cols="14" cssClass="txaClass2"/>
...
<ckeditor:replace replace="indvdlInfoDc" basePath="${pageContext.request.contextPath}/html/egovframework/com/cmm/utl/ckeditor/" />
```



## 에디터 설정 변경

**인터페이스 색상**
에디터 인터페이스의 색상을 'uiColor' property를 이용하여 변경할 수 있다.
```javascript
<code html>
CKEDITOR.replace( 'textarea_id', {
    uiColor: '#14B8C4'
});
</code>
```

**엔터키 설정**
에디터에서 엔터나 쉬프트+엔터를 눌렀을 때 입력되는 내용을 변경할 수 있다.
    property : enterMode(엔터), shiftEnterMode(쉬프트+엔터)
    option : ENTER_P (<p>), ENTER_BR (<br>), ENTER_DIV (<div>)
```javascript
  CKEDITOR.replace( 'textarea_id', {
     enterMode: CKEDITOR.ENTER_DIV
  });
```

**엔터키 설정**
에디터 인터페이스의 언어를 'language' property를 이용하여 변경할 수 있다. 각 언어별 설정은 /ckeditor/lang 디렉토리 안에 존재한다.
```javascript
<code html>
CKEDITOR.replace( 'textarea_id', {
   // Load the Korean interface.
   language: 'ko'
});
</code>
```

**툴바 설정**
에디터의 도구모음을 원하는 것만 설정해서 사용할 수 있다. 설정 방법은 두가지 방법을 제공하고 있다.

config.toolbar
```javascript
   CKEDITOR.replace( 'textarea_id', {
     toolbar: [
		{ name: 'document', items: [ 'Source', '-', 'NewPage', 'Preview', '-', 'Templates' ] },//이름과 도구모음그룹을 정의
		[ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ],	// 이름없이 도구모음그룹을 정의
		'/',										// 줄바꿈 - 다음 그룹이 새로운 라인에 배치 됨
		{ name: 'basicstyles', items: [ 'Bold', 'Italic' ] }
	      ]
    });
```

config.toolbarGroups
```javascript
   CKEDITOR.replace( 'textarea_id', {
	toolbarGroups: [
		{ name: 'document',	   groups: [ 'mode', 'document' ] },	// 이름과 두 개의 하위 그룹으로 구성
 		{ name: 'clipboard',   groups: [ 'clipboard', 'undo' ] },
 		'/',								// 줄바꿈 - 다음 그룹이 새로운 라인에 배치 됨
 		{ name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
 		{ name: 'links' }
	     ]
   });
```

※ 설정관련 샘플페이지 호출 URL : /html/egovframework/com/cmm/utl/ckeditor/samples/index.html



## 참고자료

- [ckeditor](https://ckeditor.com/)
- [https://docs-old.ckeditor.com/Main_Page](https://docs-old.ckeditor.com/Main_Page)
