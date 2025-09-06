---
title: "웹에디터(공통컴포넌트 2.0 매뉴얼 참조)"
linkTitle: "웹에디터(공통컴포넌트 2.0 매뉴얼 참조)"
description: "게시판, 자료실의 메모장에서 사용자가 자유롭게 컨텐츠를 편집할 수 있는 기능의 컴포넌트을 제공한다. "
url: /common-component/elementary-technology/webeditor/
menu:
  depth:
    weight: 1
    parent: "webeditor"
    identifier: "webeditor2"
---

# 웹에디터

## 개요

게시판, 자료실의 메모장에서 사용자가 자유롭게 컨텐츠를 편집할 수 있는 기능의 컴포넌트을 제공한다. 텍스트 및 HTML 편집 기능을 지원하고, 이미지 업로드 및 이미지를 편집기에 보여주는 기능이 있어야 한다. 웹 에디터는 웹 브라우저에서 게시판, 공지사항, 자료실, 사진첩과 같이 입력기능이 있는 곳에서 사용할 수 있다.

본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

① 웹에디터 편집기능

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| HTML | /html/egovframework/cmm/utl/htmlarea3.0 | HTMLAREA3.0 웹에디터 |  |
| JS | /html/egovframework/cmm/utl/htmlarea3.0/htmlarea.js | 웹에디터 동작 스크립트 |  |
| JSP | WEB_INF/jsp/egovframework/cmm/utl/EgovWebEditor.jsp | 테스트 페이지 |  |


##### 메소드

N/A

## 환경설정

N/A

## 사용방법

자바스크립트 호출
```html
<script type="text/javascript">
_editor_url = "<c:url value='/html/egovframework/com/cmm/utl/htmlarea3.0/'/>";          -> 웹에디터 호출 전 변수값 삽입
_editor_area = "emailCn";          -> 페이지에 웹에디터가 들어갈 위치에 넣은 textarea ID
</script>
<script type="text/javascript" src="<c:url value='/html/egovframework/cmm/utl/htmlarea3.0/htmlarea.js'/>"></script>
```


submit 호출 javascript function 부분 처리
```js
function fn_egov_regist() {
    document.club.onsubmit();  // 추가 처리 부분으로 club 부분은 실제 form명으로 변경
   ...
    document.club.submit();
}
```


Body Onload 부분 처리
```html
<body onLoad="HTMLArea.init(); HTMLArea.onload = initEditor;">
```

textarea
```html
<tr> 
  <th>발신 내용<img src="/images/egovframework/ems/required.gif" width="15" height="15"></th>
  <td width="350">
    <textarea id="emailCn" name="emailCn" cols="75" rows="14"  style="width:550px; height:400px">
    </textarea> 
  </td>
</tr>
```

테스트 페이지 호출시
URL : /html/egovframework/com/cmm/utl/htmlarea3.0/examples/index.html


## 키보드 단축키

브라우져에 따라 일부 기능이 제한 될 수 있다.
```bash
  CTRL-A -- 전체 선택
  CTRL-B -- 굵게
  CTRL-I -- 기울임꼴(이탤릭체)
  CTRL-U -- 밑줄
  CTRL-S -- 취소선
  CTRL-L -- 텍스트 왼쪽 맞춤
  CTRL-E -- 텍스트 가운데 맞춤
  CTRL-R -- 텍스트 오른쪽 맞춤
  CTRL-J -- 텍스트 양쪽 맞춤
  CTRL-1 ~ CTRL-6 -- headings (<h1> ~ <h6>)
```

## 에디터 설정 변경

기본으로 제공되는 에디터 설정 이외에 툴바의 설정, 글쓰는 영역 지정, 글쓰는 영역의 색상 등도 지정할 수 있다.
```javascript
  예제> htmlarea.js
 
  var config = new HTMLArea.Config(); // 새로운 설정 객체를 생성하고, 해당 객체에 기본 값을 지정한다.
  config.width = '90%';      //에디터 넓이 90%
  config.height = '200px';  //에디터 높이 200px
 
  //에디터 페이지의 스타일을 지정한다. 
  config.pageStyle =
  'body { background-color: yellow; color: black; font-family: verdana,sans-serif } ' +
  'p { font-width: bold; } ';
 
  // id의 textarea를 설정한 HTMLArea로 교체한다.
  HTMLArea.replace('id', config);
```

## 툴바 설정 변경

```js
예제> htmlarea.js
 
var config = new HTMLArea.Config();
 
  //toolbar내의 내용을 변경하여 에디터의 toolbar설정을 수정할 수 있다.
  config.toolbar = [
[ "fontname", "space",
  "fontsize", "space",
  "formatblock", "space", ㅡㅏ
  "bold", "italic", "underline", "separator",
  "strikethrough", "subscript", "superscript", "separator",
  "copy", "cut", "paste", "space", "undo", "redo" ],
 
[ "justifyleft", "justifycenter", "justifyright", "justifyfull", "separator",
  "insertorderedlist", "insertunorderedlist", "outdent", "indent", "separator",
  "forecolor", "hilitecolor", "textindicator", "separator",
  "inserthorizontalrule", "createlink", "insertimage", "inserttable", "htmlmode", "separator",
  "popupeditor", "separator", "showhelp", "about" ]
];
 
HTMLArea.replace('id', config);
```

위의 예제에서 아래의 세개의 문자열을 제외하고 툴바 내의 모든 객체(예시>“fontname” )들은 config.btnList에 정의 되어있다.
```bash
'space' — 현재 툴바의 위치에 5pixel 공백 입력
'separator' — 구분선 입력
'linebreak' — 이후의 버튼들은 새로운 라인으로 이동
```

## 참고자료

- [참고자료](https://htmlarea.sourceforge.net/reference.html)