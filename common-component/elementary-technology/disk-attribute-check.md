---
title: "디스크속성정보체크"
linkTitle: "디스크속성정보체크"
description: "디스크속성정보체크"
url: /common-component/elementary-technology/system/disk-attribute-check/
menu:
  depth:
    name: "디스크속성정보체크"
    weight: 16
    parent: "system"
---

## 개요

특정 파일이 위치한 디스크의 마운트 경로(속성 정보)를 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

디스크 속성정보 체크에서 제공하는 기능은 다음과 같다.

1. 파일이 위치한 디스크의 마운트 경로를 확인하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDiskAttrCeck.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

디스크 속성정보 체크 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getMountLc(String file)` | 마운트 경로 조회 | 입력한 파일이 위치한 디스크의 마운트 경로를 반환한다. 성공 시 마운트 경로 문자열, 실패 시 빈 문자열 리턴 |

#### 파라미터 정의 (Input)

- `file`: String 타입의 절대경로를 포함하는 확인 대상 파일 경로
  (예: `/product/jeus/test/samples/common.xml`)

#### 반환값 정의 (Output)

- String 타입: 파일이 위치한 디스크의 마운트 경로 (예: `/product`)

### 환경 설정

`getMountLc` 메소드는 쉘 스크립트의 실행 결과를 활용하여 정보를 확인한다. 호출 시 활용되는 쉘 스크립트의 정보는
`globals.properties`에 등록한다.

#### globals.properties

```properties
# getMountLc 메소드에 해당되는 쉘 스크립트
SHELL.UNIX.getDiskAttribute = /product/jeus/egovProps/prg/getDiskAttribute.sh
```

#### getDiskAttribute.sh (유닉스용 디스크 마운트 경로 조회 스크립트)

```bash
df $1 | tail -1 | awk -F" " '{print $6}'
```

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String filePath = "/product/jeus/test/samples/common.xml";

// 파일이 위치한 디스크 마운트 경로 조회
String mountLc = EgovFileTool.getMountLc(filePath);
// 출력 예시: /product
```

## 참고자료

- N/A
