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

> **5.0 적용 범위:** `EgovSysInfo`는
> [공통컴포넌트 3.9.x](https://github.com/eGovFramework/egovframe-common-components/blob/3.9.x/src/main/java/egovframework/com/utl/sim/service/EgovSysInfo.java)까지
> 제공되던 클래스로, [v3.10.0 beta 커밋](https://github.com/eGovFramework/egovframe-common-components/commit/c78c52ffb3b3e384d62a545aa76ffdfc6fec3f7c)에서
> 삭제되어 4.x와 [5.0](https://github.com/eGovFramework/egovframe-common-components/tree/v5.0.6/src/main/java/egovframework/com/utl/sim/service) 소스 저장소에는 없다.
> 아래의 클래스·메서드·JSP 테스트 페이지는 5.0에서 그대로 사용할 수 없고, 같은 기능의 대체 클래스도 5.0 소스에서 확인되지 않는다.
> 기존 설명과 예제는 구버전 참고용으로 유지한다.

## 개요

시스템에 존재하는 디스크(DISK), CD, USB 등에 대한 존재를 확인하는 기능이다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 디스크 존재 확인 기능

### 관련 소스

| 유형 | 대상 소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovSysInfo.java` | 시스템 정보 확인 요소기술 클래스 | |
| JSP | `WEB-INF/jsp/egovframework/cmm/utl/EgovDiskExst.jsp` | 테스트 페이지 | |

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

// 디스크 개수 조회
ArrayList result = EgovSysInfo.getExistDisk("disk");
String diskCnt = (String)result.get(0);
```

## 참고자료

- 해당 사항 없음
