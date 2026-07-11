---
title: "파일속성정보체크"
linkTitle: "파일속성정보체크"
description: "파일속성정보체크"
url: /common-component/elementary-technology/system/file-attribute-check/
menu:
  depth:
    name: "파일속성정보체크"
    weight: 34
    parent: "system"
---

## 개요

파일 속성정보인 파일명, 최종수정일자, 소유계정, 읽기권한, 쓰기권한, 접근권한, 마운트 경로 정보를 확인하는
기능을 제공한다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

### 활용 예시

파일 속성정보 체크 기능은 다음과 같은 상황에서 활용할 수 있다.

- 파일의 존재 여부와 상태를 확인하는 경우
- 파일의 읽기 및 쓰기 권한을 점검하는 경우
- 파일의 최종 수정일자와 소유자를 확인하는 경우
- 파일이 저장된 디스크의 마운트 경로를 확인하는 경우

## 설명

지정한 파일의 이름, 최종 수정일자, 소유자, 접근 권한 및 마운트 경로 등의 속성정보를 조회하는 기능을 제공한다.
이를 통해 파일의 상태와 접근 가능 여부를 확인하고 운영 환경을 점검할 수 있다.

### 기능 설명

파일 속성정보 체크에서 제공하는 기능은 다음과 같다.

1. 파일명을 확인하는 기능
2. 파일 최종수정일자를 확인하는 기능
3. 파일의 소유계정을 확인하는 기능
4. 파일의 읽기권한을 확인하는 기능
5. 파일의 쓰기권한을 확인하는 기능
6. 파일의 접근권한을 확인하는 기능
7. 파일이 위치한 디스크의 마운트 경로를 확인하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileAttrCeck.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일 속성정보 체크 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getFileName(path)` | 파일명 조회 | 성공 시 파일명, 실패 시 빈 문자열 리턴 |
| String | `getUpdtDate(path)` | 수정일자 조회 | 최종 수정일자를 조회한다. 성공 시 8자리 날짜, 실패 시 빈 문자열 리턴 |
| String | `getOwner(path)` | 소유자 조회 | 소유자 계정명을 조회한다. 성공 시 소유계정명, 실패 시 빈 문자열 리턴 |
| boolean | `checkReadAuth(path)` | 읽기권한 조회 | 파일의 읽기 권한 여부를 확인한다. 권한이 있으면 true, 없으면 false 리턴 |
| boolean | `checkWriteAuth(path)` | 쓰기권한 조회 | 파일의 쓰기 권한 여부를 확인한다. 권한이 있으면 true, 없으면 false 리턴 |
| String | `getAccess(path)` | 접근권한 조회 | 접근권한을 조회한다. 성공 시 권한 문자열, 실패 시 빈 문자열 리턴 |
| String | `getMountLc(path)` | 마운트 경로 조회 | 파일이 위치한 디스크의 마운트 경로를 조회한다. |

#### 파라미터 정의 (Input)

- `path`: String 타입의 절대경로를 포함하는 확인 대상 파일 경로
  (예: `/product/jeus/test/samples/common.xml`)

#### 반환값 정의 (Output)

- String 타입: 항목별로 확인된 속성정보
- boolean 타입: 권한 유무 (`true` / `false`)

### 환경 설정

`getOwner`, `getAccess` 메소드는 쉘 스크립트의 실행 결과를 활용하여 정보를 확인한다. 호출 시 활용되는 쉘 스크립트의 정보는
`globals.properties`에 등록한다.

### 사용 시 주의사항

- 조회 대상 파일이 존재해야 한다.
- 운영체제와 실행 계정의 권한에 따라 일부 속성정보를 조회하지 못할 수 있다.
- `getOwner`, `getAccess` 메소드는 유닉스 계열 운영체제의 쉘 스크립트를 사용하므로 실행 권한과 경로 설정을 확인해야 한다.
- 마운트 경로 조회 결과는 운영체제 및 파일 시스템 환경에 따라 달라질 수 있다.

#### globals.properties

```properties
# getOwner 메소드에 해당되는 쉘 스크립트
SHELL.UNIX.getFileOwner = /product/jeus/egovProps/prg/getFileOwner.sh
# getAccess 메소드에 해당되는 쉘 스크립트
SHELL.UNIX.getFileAccess = /product/jeus/egovProps/prg/getFileAccess.sh
```

#### getFileOwner.sh (유닉스용 파일 소유자 조회 스크립트)

```bash
ls -alF $1 | grep $2 | awk -F" " '{print $3}'
```

#### getFileAccess.sh (유닉스용 파일 접근권한 조회 스크립트)

```bash
ls -alF $1 | grep $2 | awk -F" " '{print $1}'
```

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String targetFilePath = "/product/jeus/test/samples/common.xml";

String fileName       = EgovFileTool.getFileName(targetFilePath);
String updtDate       = EgovFileTool.getUpdtDate(targetFilePath);
String owner          = EgovFileTool.getOwner(targetFilePath);
boolean canRead       = EgovFileTool.checkReadAuth(targetFilePath);
boolean canWrite      = EgovFileTool.checkWriteAuth(targetFilePath);
String accessStr      = EgovFileTool.getAccess(targetFilePath);
String mountLc        = EgovFileTool.getMountLc(targetFilePath);
```

## 참고자료

- N/A
