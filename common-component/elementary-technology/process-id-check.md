---
title: "프로세스ID확인"
linkTitle: "프로세스ID확인"
description: "프로세스ID확인"
url: /common-component/elementary-technology/system/process-id-check/
menu:
  depth:
    name: "프로세스ID확인"
    weight: 45
    parent: "system"
---

## 개요

시스템에서 동작하는 프로세스에 대한 정보를 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

프로세스ID확인에서 제공하는 기능은 다음과 같다.

1. 전체 프로세스 아이디 정보를 확인하는 기능
2. 특정 프로세스명에 해당하는 아이디 정보를 확인하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovSysInfo.java` | 시스템 정보 확인 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovProcsInfo.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

프로세스ID확인 기능은 `EgovSysInfo` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| ArrayList | `getProcessId()` | 프로세스아이디 정보 조회 | 전체 프로세스의 아이디·그룹정보·사용계정정보·실행명령·실행명령위치 정보를 문자열로 LIST에 담아 리턴 |
| ArrayList | `getProcessId(String processName)` | 프로세스아이디 정보 조회 (프로세스명 조건) | `processName`에 해당하는 프로세스의 아이디·그룹정보·사용계정정보·실행명령·실행명령위치 정보를 LIST에 담아 리턴 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `processName`: String 타입의 프로세스명 (예: `java`)

#### 반환값 정의 (Output)

- ArrayList 타입: 프로세스정보 목록 (예: `{"javaw", "user", "jeus", "java", "/usr/java5_64/bin/java"}`)

### 사용 방법

```java
import java.util.ArrayList;

import egovframework.com.utl.sim.service.EgovSysInfo;

// 프로세스아이디, 그룹정보, 사용계정정보, 실행명령, 실행명령위치 항목이 순차적으로 등록됨
ArrayList result1 = EgovSysInfo.getProcessId();

String strProcessName = "oracle";
ArrayList result2 = EgovSysInfo.getProcessId(strProcessName);
```

## 환경설정

`getProcessId` 메소드는 쉘 스크립트 실행 결과를 활용하여 정보를 확인하며, 스크립트 경로를 `globals.properties`에 등록한다.

```properties
# getProcInfo 메소드에 해당되는 쉘 스크립트
SHELL.UNIX.getProcInfo = /product/jeus/egovProps/prg/getProcInfo.sh
```

```shell
# getProcInfo.sh (유닉스용 프로세스정보 조회 스크립트)
if [ $1 == "-all" ]
then
    ps -eo "%p %G %U %c %a" | awk -F" " '{print $1,$2,$3,$4,$5}'
else
    ps -eo "%p %G %U %c %a" | awk -F" " '{print $1,$2,$3,$4,$5}' | grep $1
fi
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
