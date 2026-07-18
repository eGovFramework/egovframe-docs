---
title: "서버정보확인"
linkTitle: "서버정보확인"
description: "서버정보확인"
url: /common-component/elementary-technology/system/server-info-check/
menu:
  depth:
    name: "서버정보확인"
    weight: 19
    parent: "system"
---

## 개요

서버정보확인은 시스템에 설치된 웹 서버, WAS, 메일 서버 등의 정보를 조회하는 기능을 제공한다.

등록된 서버의 제품명과 버전, 사용 포트 및 실행 상태를 확인할 수 있으며,
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

서버정보확인에서 제공하는 주요 기능은 다음과 같다.

1. 시스템에 등록된 서버의 제품명과 버전 정보를 조회한다.
2. 서버가 사용하는 포트 번호를 조회한다.
3. 서버의 사용 포트를 기반으로 실행 상태를 확인한다.

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovSysInfo.java` | 시스템 정보 확인 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovSysInfo.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

서버정보확인 기능은 `EgovSysInfo` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getPrductVersion(String server)` | 제품명·버전 조회 | 서버명(`server`)으로 제품명과 제품버전을 리턴 |
| String | `getPrductPort(String server)` | 포트 조회 | 서버명(`server`)으로 사용포트번호를 리턴 |
| String | `getPrductStatus(String port)` | 실행상태 조회 | 사용포트번호(`port`)로 실행상태를 리턴 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `server`: 정보를 조회할 서버명
- `port`: 실행 상태를 확인할 서버의 포트 번호

#### 반환값 정의 (Output)

- `String`: 서버의 제품명·버전, 사용 포트 또는 실행 상태 정보

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovSysInfo;

// 1. 서버 목록 조회
String strlist = EgovProperties.getProperty(Globals.ServerConfPath, "SERVER_LIST");
String[] list = strlist.split("\\$");

for (int i = 0; i < list.length; i++) {
    String name = list[i];                                   // 제품명
    String version = EgovSysInfo.getPrductVersion(list[i]);  // 제품버전
    String port = EgovSysInfo.getPrductPort(list[i]);        // 사용포트번호
    String status = EgovSysInfo.getPrductStatus(port);       // 실행상태
}
```

## 환경설정

서버 목록·버전·포트 및 실행상태 조회 스크립트는 `server.properties`에 정의한다.

```properties
#1. 목록(구분자 $)
SERVER_LIST = WEBLOGIC$JEUS$JBOSS
#2. 버전
WEBLOGIC.VERSION = 9.2 MP3
JEUS.VERSION = 6.0
JBOSS.VERSION = 3.1
#3. 사용포트
WEBLOGIC.PORT = 7001
JEUS.PORT = 9736
JBOSS.PORT = 8080
#4. 실행상태 확인 쉘 스크립트
SHELL.WINDOWS.getPrductStatus = C:/egovProps/prg/getPrductStatus.bat
SHELL.UNIX.getPrductStatus = /product/jeus/egovProps/prg/getPrductStatus.sh
```

실행상태 조회 스크립트 예시는 다음과 같다.

```shell
# getPrductStatus.sh (유닉스용)
netstat -na | grep -w "LISTEN" | grep -c $1
```

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
