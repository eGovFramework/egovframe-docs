---
title: "시스템정보확인"
linkTitle: "시스템정보확인"
description: "시스템정보확인"
url: /common-component/elementary-technology/system/system-info-check/
menu:
  depth:
    name: "시스템정보확인"
    weight: 20
    parent: "system"
---

## 개요

시스템 고유의 속성정보인 프로세서 ID, 호스트, 운영체제(OS), 메모리(Memory), 디스크(HDD) 정보를 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

시스템정보확인에서 제공하는 기능은 다음과 같다.

1. 시스템의 프로세서(Processor) ID(CPU ID)를 가져오는 기능
2. 시스템의 운영체제 정보를 가져오는 기능
3. 시스템의 메모리 용량 정보를 가져오는 기능
4. 시스템의 디스크 정보를 가져오는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovSysInfo.java` | 시스템정보 확인 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovSysInfo.jsp` | 테스트 페이지 | |

> ※ 해당 파일은 보안상의 이유로 배포되지 않는다. 필요시 표준프레임워크 지원 이메일(egovframesupport@gmail.com)로 요청하면 관련 파일을 전달받을 수 있다.

### 클래스 및 메소드 설명

시스템정보확인 기능은 `EgovSysInfo` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getProcessorID()` | 프로세서ID 조회 | 시스템의 프로세서ID를 리턴 |
| String | `getHostName()` | 호스트명 조회 | 시스템의 호스트명을 리턴 |
| String | `getOSName()` | OS이름 조회 | 시스템의 OS 이름을 리턴 |
| String | `getOSVersion()` | OS버전 조회 | 시스템의 OS 버전을 리턴 |
| String | `getOSPrductor()` | OS제조사 조회 | 시스템의 OS 제조사를 리턴 |
| float | `getMoryFullCpcty()` | 메모리 전체용량 조회 | 시스템의 메모리 전체용량 리턴 |
| float | `getMoryUsedCpcty()` | 메모리 사용용량 조회 | 시스템의 메모리 사용용량 리턴 |
| float | `getMoryFreeCpcty()` | 메모리 유효용량 조회 | 시스템의 메모리 유효용량 리턴 |
| ArrayList | `getDiskName()` | 디스크 목록 조회 | 시스템의 디스크목록 리턴 |
| float | `getDiskFullCpcty()` | 디스크 전체용량 조회 | 시스템의 디스크 전체용량 리턴 |
| float | `getDiskUsedCpcty()` | 디스크 사용용량 조회 | 시스템의 디스크 사용용량 리턴 |
| float | `getDiskFreeCpcty()` | 디스크 유효용량 조회 | 시스템의 디스크 유효용량 리턴 |
<!-- markdownlint-restore -->

#### 반환값 정의 (Output)

- String 타입: 호스트명 (예: `WAS`), OS이름 (예: `AIX`), OS버전 (예: `5.3.0.0`), OS제조사 (예: `IBM,8204-E8A`), 프로세서ID (예: `0B0AA2`)
- float 타입: 메모리·디스크 전체/사용/유효 용량 (MB 단위)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovSysInfo;

// 1. 호스트명, OS명, OS버전, OS제조사, 프로세서
String hostname = EgovSysInfo.getHostName();
String osname = EgovSysInfo.getOSName();
String osversion = EgovSysInfo.getOSVersion();
String osprductor = EgovSysInfo.getOSPrductor();
String processor = EgovSysInfo.getProcessorID();

// 2. 메모리 용량
float moryFull = EgovSysInfo.getMoryFullCpcty();
float moryUsed = EgovSysInfo.getMoryUsedCpcty();
float moryFree = EgovSysInfo.getMoryFreeCpcty();

// 3. 디스크 용량
ArrayList list = EgovSysInfo.getDiskName();
for (int i = 0; i < list.size(); i++) {
    String diskName = (String) list.get(i);
}
```

## 환경설정

프로세서ID·OS·메모리·디스크 정보 조회는 OS별 쉘 스크립트 실행 결과를 활용하며, 스크립트 경로를 `server.properties`에 정의한다.

```properties
#1. 프로세서ID, OS정보 조회 쉘 스크립트
SHELL.WINDOWS.getOSInfo = C:/egovProps/prg/getOSInfo.bat
SHELL.UNIX.getOSInfo = /product/jeus/egovProps/prg/getOSInfo.sh
#2. 메모리정보 조회 쉘 스크립트
SHELL.WINDOWS.getMoryInfo = C:/egovProps/prg/getMoryInfo.bat
SHELL.UNIX.getMoryInfo = /product/jeus/egovProps/prg/getMoryInfo.sh
#3. 디스크정보 조회 쉘 스크립트
SHELL.WINDOWS.getDiskInfo = C:/egovProps/prg/getDiskInfo.bat
SHELL.UNIX.getDiskInfo = /product/jeus/egovProps/prg/getDiskInfo.sh
```

윈도우 환경은 `systeminfo` 명령을, 유닉스 환경은 `uname`·`oslevel`·`vmstat`·`lspv` 등의 명령 조합 스크립트를 사용한다.
윈도우 환경에서는 디스크정보 조회를 지원하지 않는다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
