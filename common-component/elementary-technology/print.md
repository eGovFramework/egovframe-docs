---
title: "인쇄/출력"
linkTitle: "인쇄/출력"
description: "화면 인쇄, 전자관인 출력, 프린터 상태 확인 기능을 제공하는 인쇄/출력 공통컴포넌트 가이드"
url: /common-component/elementary-technology/print/
menu:
  depth:
    weight: 4
    parent: "elementary-technology"
    identifier: "print"
---

<!-- markdownlint-disable MD025 MD013 -->

# 인쇄/출력

## 개요

인쇄/출력 공통컴포넌트는 화면 인쇄, 전자관인 출력, 프린터 상태 확인 등 인쇄와 관련된 기능을 제공하는 요소기술이다.
과거 인터넷 익스플로러(Internet Explorer) 환경의 ActiveX 기반 인쇄 제어와 웹 표준 기반의 인쇄 기능을 지원한다.

## 주요 개념

### 화면인쇄

인터넷 브라우저에서 화면을 인쇄하거나 페이지 설정을 할 수 있는 기능이다. 인쇄 미리보기, 인쇄 바로하기, 페이지 설정 기능으로 구분된다.

### 전자관인출력

기관코드와 관인구분을 입력받아 해당하는 관인 이미지를 화면에 출력하는 기능이다.

### 프린터상태확인

인터넷 웹 브라우저에서 인쇄/출력 시 프린터 상태를 확인하고 설정을 변경할 수 있는 시스템 인쇄 창을 호출하는 기능이다.

## 설명

### 1. 화면인쇄

#### 화면인쇄 관련 소스

| 유형 | 대상 소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Controller | `egovframework.com.utl.fcc.web.EgovComUtlTestController.java` | 테스트용 Controller | |
| JSP | `/WEB-INF/jsp/egovframework/cmm/utl/EgovPrint.jsp` | 화면인쇄 테스트 페이지 | |

#### 화면인쇄 사용 방법

과거 인터넷 익스플로러(Internet Explorer) 환경에서는 ActiveX(`CLSID:8856F961-340A-11D0-A96B-00C04FD705A2`)를 활용하여 인쇄 제어를 수행하였으나, 최신 브라우저 환경에서는 표준 웹 함수인 `window.print()`를 사용한다.

```javascript
function printOption(type1, type2) {
    var isIE = (navigator.appName === 'Netscape' && navigator.userAgent.search('Trident') !== -1) 
               || (navigator.userAgent.toLowerCase().indexOf("msie") !== -1);
    
    // 비 익스플로러 브라우저 및 최신 웹 표준 환경
    if (!isIE) {
        window.print();
    } else {
        // 구형 익스플로러 환경 (ActiveX 사용)
        var active = '<object id="active1" width="0" height="0" ' +
                     'classid="clsid:8856F961-340A-11D0-A96B-00C04FD705A2"></object>';
        document.body.insertAdjacentHTML('beforeend', active);
        document.getElementById('active1').ExecWB(type1, type2); 
        document.getElementById('active1').outerHTML = "";
    }
}
```

```html
<input type="button" value="인쇄 미리 보기" onclick="printOption(7, 1)" />  
<input type="button" value="인쇄 바로 하기" onclick="printOption(6, -1)" />
<input type="button" value="페이지 설정" onclick="printOption(8, 1)" />
```

### 2. 전자관인출력

#### 전자관인출력 관련 소스

| 유형 | 대상 소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Controller | `egovframework.com.utl.pao.web.EgovErncslController.java` | 전자관인 출력 Controller | |
| VO | `egovframework.com.utl.pao.service.PrntngOutptVO.java` | 전자관인 VO | |
| Controller | `egovframework.com.utl.pao.web.EgovPrntngOutptController.java` | 테스트용 Controller | |
| Service | `egovframework.com.utl.pao.service.EgovPrntngOutpt.java` | 테스트용 인터페이스 | |
| ServiceImpl | `egovframework.com.utl.pao.service.impl.EgovPrntngOutptImpl.java` | 테스트용 구현체 | |
| DAO | `egovframework.com.utl.pao.service.impl.PrntngOutptDAO.java` | 테스트용 데이터 처리 | |
| JSP | `/WEB-INF/jsp/egovframework/cmm/utl/EgovErncslOutpt.jsp` | 테스트 페이지 | |

#### 전자관인출력 사용 방법

관인 정보 확인에 필요한 기관코드(`sOrgCode`)와 관인구분(`sErncslSe`) 파라미터를 통해 해당 관인 이미지를 직접 출력한다.

```html
<img src="/utl/pao/EgovErncsl.do?sOrgCode=<%=sOrgCode%>&sErncslSe=<%=sErncslSe%>" alt="전자관인" />
```

### 3. 프린터상태확인

#### 프린터상태확인 관련 소스

| 유형 | 대상 소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Controller | `egovframework.com.utl.fcc.web.EgovComUtlTestController.java` | 테스트용 Controller | |
| JSP | `/WEB-INF/jsp/egovframework/cmm/utl/EgovPrintStatus.jsp` | 프린터상태확인 테스트 페이지 | |

#### 프린터상태확인 사용 방법

사용자가 버튼을 클릭하면 브라우저의 기본 프린터 상태 확인 및 설정 창(인쇄 대화상자)이 열린다. 이를 통해 사용자는 인쇄할 프린터의 상태를 확인하고 설정을 변경할 수 있다.

```html
<input type="button" value="프린터상태확인" onclick="window.print();" />
```

## 참고자료

- [MDN Web Docs: window.print()](https://developer.mozilla.org/en-US/docs/Web/API/Window/print)
