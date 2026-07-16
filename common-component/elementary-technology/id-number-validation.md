---
title: "번호유효성체크"
linkTitle: "번호유효성체크"
description: "번호유효성체크"
url: /common-component/elementary-technology/formatter-util/id-number-validation/
menu:
  depth:
    name: "번호유효성체크"
    weight: 12
    parent: "formatter-util"
---

## 개요

주어진 주민등록번호, 법인번호, 사업자등록번호, 외국인등록번호의 유효성을 체크하여 `true`, `false`를 반환한다.

## 설명

입력에 주민등록번호, 법인번호, 사업자등록번호, 외국인등록번호를 입력받는다. 각 번호마다 하이픈(`-`)이 포함된 구분 입력과, 하이픈이 배제된 하나의 입력 등 두 가지 방식을 지원한다.

### 관련 소스

| 유형 | 대상 소스 | 설명 |
| --- | --- | --- |
| Service | `egovframework.com.utl.fcc.service.EgovNumberCheckUtil.java` | 번호 유효성 처리 관련 유틸리티 |
| JSP | `/WEB-INF/jsp/egovframework/cmm/utl/EgovNumberCheck.jsp` | 테스트 페이지 |

### 메소드

| 결과값 | 메소드 | 설명 | 내용 |
| --- | --- | --- | --- |
| `boolean` | `checkJuminNumber(String jumin1, String jumin2)` | 주민등록번호 유효성체크 | 주민등록번호 앞, 뒤 문자열을 입력받아 유효성 체크 |
| `boolean` | `checkJuminNumber(String jumin)` | 주민등록번호 유효성체크 | 주민등록번호(`-` 제외) 문자열을 입력받아 유효성 체크 |
| `boolean` | `checkBubinNumber(String bubin1, String bubin2)` | 법인번호 유효성체크 | 법인번호 앞, 뒤 문자열을 입력받아 유효성 체크 |
| `boolean` | `checkBubinNumber(String bubin)` | 법인번호 유효성체크 | 법인번호(`-` 제외) 문자열을 입력받아 유효성 체크 |
| `boolean` | `checkCompNumber(String c1, String c2, String c3)` | 사업자번호 유효성체크 | 사업자번호 앞, 중간, 뒤 문자열을 입력받아 유효성 체크 |
| `boolean` | `checkCompNumber(String comp)` | 사업자번호 유효성체크 | 사업자번호(`-` 제외) 문자열을 입력받아 유효성 체크 |
| `boolean` | `checkforeignNumber(String for1, String for2)` | 외국인번호 유효성체크 | 외국인등록번호 앞, 뒤 문자열을 입력받아 유효성 체크 |
| `boolean` | `checkforeignNumber(String foreign)` | 외국인번호 유효성체크 | 외국인등록번호(`-` 제외) 문자열을 입력받아 유효성 체크 |

- **Input**: 해당하는 입력란의 `String` 형태의 번호
- **Output**: `boolean` (유효 여부)

## 사용방법

다음은 번호의 종류에 따라 유효성을 검증하는 예제 코드이다.

```java
import egovframework.com.utl.fcc.service.EgovNumberCheckUtil;

// ...

// 1. 주민등록번호 체크
String jumin1 = "831231";
String jumin2 = "265948";
String jumin  = "831231265948";

boolean isJuminValid1 = EgovNumberCheckUtil.checkJuminNumber(jumin1, jumin2);
boolean isJuminValid2 = EgovNumberCheckUtil.checkJuminNumber(jumin);

// 2. 법인번호 체크
String bubin1 = "134153";
String bubin2 = "4433453";
String bubin  = "1341534433453";

boolean isBubinValid1 = EgovNumberCheckUtil.checkBubinNumber(bubin1, bubin2);
boolean isBubinValid2 = EgovNumberCheckUtil.checkBubinNumber(bubin);

// 3. 사업자등록번호 체크
String comp1 = "324";
String comp2 = "12";
String comp3 = "43222";
String comp  = "3241243222";

boolean isCompValid1 = EgovNumberCheckUtil.checkCompNumber(comp1, comp2, comp3);
boolean isCompValid2 = EgovNumberCheckUtil.checkCompNumber(comp);

// 4. 외국인등록번호 체크
String foreign1 = "831231";
String foreign2 = "576545";
String foreign  = "831231576545";

boolean isForeignValid1 = EgovNumberCheckUtil.checkforeignNumber(foreign1, foreign2);
boolean isForeignValid2 = EgovNumberCheckUtil.checkforeignNumber(foreign);

// ...
```
