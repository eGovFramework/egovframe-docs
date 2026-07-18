---
title: "프로퍼티"
linkTitle: "프로퍼티"
description: "프로퍼티"
url: /common-component/elementary-technology/system/property/
menu:
  depth:
    name: "프로퍼티"
    weight: 46
    parent: "system"
---

## 개요

애플리케이션에서 공통으로 사용할 프로퍼티 정보를 로드하여 파싱 후 메모리에 가지고 있는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

### 활용 예시

프로퍼티 기능은 다음과 같은 상황에서 활용할 수 있다.

- 애플리케이션의 공통 설정값을 외부 파일로 관리하는 경우
- 파일 저장 경로와 같은 환경별 설정값을 조회하는 경우
- 프로퍼티 파일의 여러 설정값을 일괄적으로 읽어 처리하는 경우
- 설정값을 코드와 분리하여 관리하는 경우

## 설명

프로퍼티 기능은 프로퍼티 파일에 정의된 설정정보를 로드하고, 지정한 Key를 이용하여 필요한 값을 조회하는 기능을 제공한다.
이를 통해 애플리케이션의 설정정보를 코드와 분리하여 관리하고 공통으로 활용할 수 있다.

### 기능 설명

프로퍼티에서 제공하는 기능은 다음과 같다.

1. 프로퍼티 파일을 로드하여 파싱 후 메모리에 가지고 있는 기능
2. Key값으로 프로퍼티 값을 조회하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.cmm.service.EgovProperties.java` | 프로퍼티 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovProperty.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

프로퍼티 기능은 `EgovProperties` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getProperty(String keyName)` | 프로퍼티조회 | 인자로 주어진 문자열을 Key값으로 하는 프로퍼티 값을 반환 |
| String | `getProperty(String fileName, String key)` | 프로퍼티조회 | 지정한 파일에서 인자로 주어진 문자열을 Key값으로 하는 프로퍼티 값을 반환 |
| ArrayList | `loadPropertyFile(String property)` | 프로퍼티파싱 | 주어진 프로퍼티 파일의 내용을 파싱하여 (key-value) 형태의 구조체 배열을 반환 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- Property 파일명: String 타입의 절대경로를 포함한 파일명 (예: `/user/com/test/test.properties`)
- Key: String 타입의 Key값 (예: `path`)

#### 반환값 정의 (Output)

- String 타입 Value값 또는 ArrayList 타입 (key-value) 목록

### 사용 방법

```java
import java.util.ArrayList;
import java.util.Map;

import egovframework.com.cmm.service.EgovProperties;

// 1. 프로퍼티 파일 파싱 후 Key로 조회
String file = "/user/com/test/test.properties";
String key = "path";

ArrayList list = EgovProperties.loadPropertyFile(file);

String resultStr = "";
for (int i = 0; i < list.size(); i++) {
    Map prop = (Map) list.get(i);
    String str = (String) prop.get(key);
    if (str != null && !"".equals(str)) {
        resultStr = str;
    }
}

// 2. globals.properties에서 직접 조회
String fileStorePath = EgovProperties.getProperty("Globals.fileStorePath");
```

## 환경설정

N/A

### 사용 시 주의사항

- 프로퍼티 조회 시 사용하는 Key가 프로퍼티 파일에 올바르게 정의되어 있는지 확인해야 한다.
- 프로퍼티 파일의 경로와 파일명이 실제 위치와 일치해야 한다.
- 환경별로 다른 설정값을 사용하는 경우 프로퍼티 파일의 설정 내용을 확인해야 한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
