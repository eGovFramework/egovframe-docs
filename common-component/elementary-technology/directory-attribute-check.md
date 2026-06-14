---
title: "디렉토리속성정보체크"
linkTitle: "디렉토리속성정보체크"
description: "디렉토리속성정보체크"
url: /common-component/elementary-technology/system/directory-attribute-check/
menu:
  depth:
    name: "디렉토리속성정보체크"
    weight: 8
    parent: "system"
---

## 개요

디렉토리 속성정보인 디렉토리명, 생성일자(최종수정일자), 소유계정, 읽기권한, 쓰기권한, 접근권한, 사이즈 정보를 확인하는
기능을 제공한다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

디렉토리 속성정보 체크에서 제공하는 기능은 다음과 같다.

1. 디렉토리명을 확인하는 기능
2. 디렉토리 최종수정일자를 확인하는 기능
3. 디렉토리의 소유계정을 확인하는 기능
4. 디렉토리의 읽기권한을 확인하는 기능
5. 디렉토리의 쓰기권한을 확인하는 기능
6. 디렉토리의 접근권한을 확인하는 기능
7. 디렉토리의 사이즈를 확인하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | egovframework.com.utl.service.EgovFileTool.java | 파일관리 요소기술 클래스 | |
| JSP | WEB_INF/jsp/egovframework/cmm/utl/EgovDrctryInfoCeck.jsp | 테스트 페이지 | |

### 클래스 및 메소드 설명

디렉토리 속성정보 체크 기능은 `EgovFileTool` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | getName(path) | 디렉토리명 조회 | 성공 시 디렉토리명, 실패 시 빈 문자열 리턴 |
| String | getLastModifiedDateFromFile(path) | 수정일자 조회 | 최종 수정일자를 조회한다. 성공 시 8자리 날짜, 실패 시 빈 문자열 리턴 |
| String | getOwner(path) | 소유자 조회 | 소유자 계정명을 조회한다. 성공 시 소유계정명, 실패 시 빈 문자열 리턴 |
| boolean | canRead(path) | 읽기권한 조회 | 디렉토리의 읽기 권한 여부를 확인한다. 권한이 있으면 true, 없으면 false 리턴 |
| boolean | canWrite(path) | 쓰기권한 조회 | 디렉토리의 쓰기 권한 여부를 확인한다. 권한이 있으면 true, 없으면 false 리턴 |
| String | getAccess(path) | 접근권한 조회 | 접근권한을 조회한다. 성공 시 권한 문자열, 실패 시 빈 문자열 리턴 |
| long | getDirectorySize(path) | 용량 조회 | 디렉토리 내 모든 파일과 하위 크기 합계를 조회한다. (byte 단위 리턴) |

#### 파라미터 정의 (Input)

- `targetDirPath` (또는 `path`): String 타입의 절대경로를 포함하는 확인대상 디렉토리 경로
  (예: `/product/jeus/egovProps/tmp/dir1`)

#### 반환값 정의 (Output)

- String 타입: 항목별로 확인된 속성정보
- boolean 타입: 권한 유무 (`true` / `false`)
- long 타입: 사이즈 정보 (byte 단위)

### 환경 설정

`getOwner`, `getAccess` 메소드는 쉘 스크립트의 실행 결과를 활용하여 정보를 확인한다. 호출 시 활용되는 쉘 스크립트의 정보는
`globals.properties`에 등록한다.

#### globals.properties

```properties
#1. getOwner 메소드에 해당되는 쉘 스크립트
SHELL.UNIX.getDrctryOwner = /product/jeus/egovProps/prg/getDrctryOwner.sh
#2. getAccess 메소드에 해당되는 쉘 스크립트
SHELL.UNIX.getMoryInfo = /product/jeus/egovProps/prg/getDrctryAccess.sh
```

#### getDrctryOwner.sh (유닉스용 디렉토리 소유자 조회 스크립트)

```bash
ls -alF $1 | grep $2  | awk -F" " '{print $3}'
```

#### getDrctryAccess.sh (유닉스용 디렉토리 접근권한 조회 스크립트)

```bash
ls -alF $1 | grep $2 | awk -F" " '{print $1}'
```

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

String targetDirPath1    = "user/com/jeus";
String directoryName1    = EgovFileTool.getName(targetDirPath1);
String lastModifiedDate1 = EgovFileTool.getLastModifiedDateFromFile(targetDirPath1);
String owner1            = EgovFileTool.getOwner(targetDirPath1);
boolean canRead1         = EgovFileTool.canRead(targetDirPath1);
boolean canWrite1        = EgovFileTool.canWrite(targetDirPath1);
String roleStr           = EgovFileTool.getAccess(targetDirPath1);
long dirSize1            = EgovFileTool.getDirectorySize(targetDirPath1);
```

## 참고자료

- N/A
