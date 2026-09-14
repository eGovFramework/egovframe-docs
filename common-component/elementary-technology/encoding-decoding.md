---
title: "인코딩/디코딩"
linkTitle: "인코딩/디코딩"
description: "인코딩/디코딩"
url: /common-component/elementary-technology/formatter-util/encoding-decoding/
menu:
  depth:
    name: "인코딩/디코딩"
    weight: 21
    parent: "formatter-util"
---

## 개요

특정 문자열의 문자셋(Charset)을 인코딩 또는 디코딩하여 변환하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

인코딩/디코딩에서 제공하는 기능은 다음과 같다.

1. 문자열을 지정한 문자셋으로 인코딩하는 기능
2. 문자열을 지정한 문자셋으로 디코딩하는 기능

이 메소드는 `new String(srcString.getBytes(srcCharsetNm), cnvrCharsetNm)`을 수행하므로, 서로 다른 문자셋을 지정하면
글자가 깨질 수 있으며 인자를 반대로 지정해 다시 호출해도 원문이 복원되지 않을 수 있다.

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.fcc.service.EgovStringUtil.java` | 문자열 처리 요소기술 클래스 | |

### 클래스 및 메소드 설명

인코딩/디코딩 기능은 `EgovStringUtil` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getEncdDcd(src, srcCharset, destCharset)` | 문자셋 변환 | 원본 문자열을 지정 문자셋으로 변환하여 반환한다. 성공 시 변환된 문자열, 원본이 `null`이거나 지원하지 않는 문자셋이면 `null` |

#### 파라미터 정의 (Input)

- `srcString`: 변환할 원본 문자열 (String 타입)
- `srcCharsetNm`: 문자열을 바이트 배열로 변환할 때 사용할 문자셋명 (예: `"UTF-8"`, `"EUC-KR"`)
- `cnvrCharsetNm`: 바이트 배열을 문자열로 변환할 때 사용할 문자셋명 (예: `"EUC-KR"`, `"UTF-8"`)

#### 반환값 정의 (Output)

- String 타입: 지정한 문자셋으로 변환된 문자열 (원본이 `null`이거나 지원하지 않는 문자셋이면 `null`)

### 사용 방법

```java
import egovframework.com.utl.fcc.service.EgovStringUtil;

String srcString    = "변환할문자열";
String srcCharset   = "UTF-8";
String destCharset  = "EUC-KR";

// UTF-8로 얻은 바이트를 EUC-KR로 해석 (서로 다른 문자셋이면 글자가 깨질 수 있다)
String encoded = EgovStringUtil.getEncdDcd(srcString, srcCharset, destCharset);
```

## 참고자료

- N/A
