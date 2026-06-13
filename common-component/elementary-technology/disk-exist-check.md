---
title: "디스크존재체크"
linkTitle: "디스크존재체크"
description: "디스크존재체크"
url: /common-component/elementary-technology/system/disk-exist-check/
menu:
  depth:
    name: "디스크존재체크"
    weight: 18
    parent: "system"
---

## 개요

시스템에 존재하는 디스크(DISK), CD, USB 등에 대한 존재를 확인하는 기능이다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 디스크 존재 확인 기능

### 관련 소스

| 유형 | 대상 소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.service.EgovSysInfo.java` | 시스템 정보 확인 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDiskExst.jsp` | 테스트 페이지 | |

### 메서드

| 결과값 | 메서드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| `ArrayList` | `getExistDisk(String diskName)` | 디스크 존재 조회 | DISK, CD, USB 존재 정보를 조회해 개수를 확인하여 반환한다. |

- **Input**
    - `diskName` : 디스크 종류 (예: `"disk"`)
- **Output**
    - `ArrayList` 타입 : 디스크 개수 정보 목록 (예: `{"4"}`)

## 환경설정

`getExistDisk` 메서드는 쉘 스크립트의 실행 결과를 활용하여 정보를 확인한다.
호출 시 활용되는 쉘 스크립트의 정보는 `globals.properties`에 등록한다.

- **`globals.properties`**

  ```properties
  # getDiskAttribute 메서드에 해당되는 쉘 스크립트
  SHELL.UNIX.getDiskExst = /product/jeus/egovProps/prg/getDiskExst.sh
  ```

- **`getDiskExst.sh` (유닉스용 디스크 존재 조회 스크립트)**

  ```bash
  lsdev -Cc $1 | wc -l
  ```

## 사용방법

```java
import egovframework.com.utl.sim.service.EgovSysInfo;

// 디스크 개수가 등록됨
ArrayList result = EgovSysInfo.getDiskExst();
String diskCnt = (String)result.get(0);
```

## 참고자료

- 해당 사항 없음
