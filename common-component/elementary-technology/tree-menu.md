---
title: "트리메뉴"
linkTitle: "트리메뉴"
description: "트리메뉴"
url: /common-component/elementary-technology/interface/tree-menu/
menu:
  depth:
    name: "트리메뉴"
    weight: 2
    parent: "interface"
---

## 개요

클라이언트(Client)에서 서버(Server)의 데이터를 받아 트리 형태로 메뉴를 구성하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

트리메뉴에서 제공하는 기능은 다음과 같다.

1. 서버의 메뉴 데이터(DAT 파일)를 파싱하여 트리 형태로 화면에 표현하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovMenuGov.java` | 메인메뉴 요소기술 클래스 | 메뉴파일 생성 |
| JS | `/js/egovframework/cmm/utl/EgovMenuGov.js` | 트리생성 JavaScript | |
| JSP | `WEB_INF/jsp/egovframework/cmm/EgovTreeMenu.jsp` | 테스트 페이지 | 직접 생성 (사용방법 참고) |

### 클래스 및 메소드 설명

트리메뉴 기능은 `EgovMenuGov` 클래스의 메소드와 트리생성 JavaScript를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| Vector | `parsFileByMenuChar(String parFile, String parChar, int parField)` | 메뉴테이블형태 파싱 | 데이터를 받아 구분값·필드수에 맞추어 메뉴필드 형태로 나눈다 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `parFile`: String 타입의 절대경로를 포함한 메뉴변환파일 (예: `/user/com/test/file1.dat`)

### 사용 방법

메인메뉴로 생성한 DAT 파일(라인별 `nodeId|parentNodeId|nodeName|nodeUrl`)을 파싱하여 트리메뉴를 표현한다.

```jsp
<%
import egovframework.com.utl.sim.service.EgovMenuGov;
Vector result1 = EgovMenuGov.parsFileByMenuChar(parFile, parChar, parField);
%>

<div class="tree">
<script type="text/javascript">
    var Tree = new Array;
<%  // nodeId | parentNodeId | nodeName | nodeUrl
    String temp = "";
    for (int j = 0; j < result1.size() - 1; j++) {
        ArrayList arr = (ArrayList) result1.elementAt(j);
        temp = (String) arr.get(0) + "|" + (String) arr.get(1) + "|"
             + (String) arr.get(2) + "|" + (String) arr.get(3);
%>  Tree[<%=j%>] = "<%=temp%>"; <%
    }
%>
    createTree(Tree);
</script>
</div>
```

## 환경설정

N/A

## 참고자료

- [메인메뉴](../main-menu/) — 트리메뉴에서 사용하는 DAT 파일의 생성·관리
- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
