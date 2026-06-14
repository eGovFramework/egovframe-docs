---
title: "디스크유효용량체크"
linkTitle: "디스크유효용량체크"
description: "디스크유효용량체크"
url: /common-component/elementary-technology/system/disk-capacity-check/
menu:
  depth:
    name: "디스크유효용량체크"
    weight: 17
    parent: "system"
---

## 개요

시스템 내 디스크의 전체 용량, 사용 가능한 용량, 사용률 및 마운트 위치 정보를 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

디스크 유효용량 체크에서 제공하는 기능은 다음과 같다.

1. 디스크 전체 용량을 확인하는 기능
2. 디스크 사용 가능 용량을 확인하는 기능
3. 디스크 사용률(%)을 확인하는 기능
4. 디스크 마운트 위치를 확인하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovSysInfo.java` | 시스템 정보 확인 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDiskCpcty.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

디스크 유효용량 체크 기능은 `EgovSysInfo` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| ArrayList | `getDiskCapacity()` | 디스크 용량 조회 | 시스템 내 디스크의 전체 사이즈, 사용 가능 사이즈, 사용률(%), 마운트 위치 정보를 ArrayList 형태로 반환한다. |

#### 반환값 정의 (Output)

- `ArrayList` 타입: 디스크 용량 정보 목록
    - 항목[0]: 전체 용량 (KB 단위)
    - 항목[1]: 사용 가능 용량 (KB 단위)
    - 항목[2]: 사용률 (%)
    - 항목[3]: 마운트 위치

### 환경 설정

`getDiskCapacity` 메소드는 쉘 스크립트의 실행 결과를 활용하여 정보를 확인한다. 호출 시 활용되는 쉘 스크립트의 정보는
`globals.properties`에 등록한다.

#### globals.properties

```properties
# getDiskCapacity 메소드에 해당되는 쉘 스크립트
SHELL.UNIX.getDiskCpcty = /product/jeus/egovProps/prg/getDiskCpcty.sh
```

#### getDiskCpcty.sh (유닉스용 디스크 용량 조회 스크립트)

```bash
df -k | grep -v Filesystem | awk -F" " '{print $2, $4, $5, $6}'
```

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovSysInfo;

// 디스크 용량 정보 조회
ArrayList result = EgovSysInfo.getDiskCapacity();

// 결과 활용 예시
String totalSize      = (String) result.get(0); // 전체 용량
String availableSize  = (String) result.get(1); // 사용 가능 용량
String usageRate      = (String) result.get(2); // 사용률
String mountLocation  = (String) result.get(3); // 마운트 위치
```

## 참고자료

- N/A
