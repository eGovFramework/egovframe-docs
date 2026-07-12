---
title: "네트워크정보확인"
linkTitle: "네트워크정보확인"
description: "네트워크정보확인"
url: /common-component/elementary-technology/system/network-info-check/
menu:
  depth:
    name: "네트워크정보확인"
    weight: 2
    parent: "system"
---

## 개요

네트워크 정보인 IP ADDRESS, MAC ADDRESS, PortScan 리스트를 확인하는 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

네트워크정보확인에서 제공하는 기능은 다음과 같다.

1. 시스템의 IP ADDRESS를 가져오는 기능
2. 시스템의 MAC ADDRESS를 가져오는 기능
3. 시스템의 PortScan(포트 사용) 정보를 가져오는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovNetworkState.java` | 네트워크정보 확인 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovNetworkInfo.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

네트워크정보확인 기능은 `EgovNetworkState` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `getMyIPaddress()` | IP ADDRESS 검색 | 시스템의 IP ADDRESS를 리턴 |
| String | `getMyMACAddress(String ipAddress)` | MAC ADDRESS 검색 | 시스템의 MAC ADDRESS를 리턴 |
| List | `getMyPortScan()` | Port 사용정보 | Port 사용내역을 리턴 |
<!-- markdownlint-restore -->

### 사용 방법

```java
import java.util.Iterator;
import java.util.List;

import egovframework.com.utl.sim.service.EgovNetworkState;

// 1. IP 주소 조회
String myIPAddress = EgovNetworkState.getMyIPaddress();

// 2. MAC 주소 조회
String myMACAddress = EgovNetworkState.getMyMACAddress(myIPAddress);

// 3. Port 사용정보 조회
List<String> list = EgovNetworkState.getMyPortScan();
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    String text = it.next();
}
```

## 환경설정

윈도우 환경은 `nbtstat -A <IP>`(MAC 주소)·`netstat -an`(포트 사용정보) 명령을 사용하며,
유닉스 환경은 네트워크정보 조회 쉘 스크립트 경로를 프로퍼티에 등록하여 사용한다.

```properties
# 네트워크 정보 쉘 스크립트
SHELL.UNIX.getNetWorkInfo = /product/jeus/egovProps/prg/getNetWorkInfo.sh
```

유닉스용 스크립트는 `netstat`·`prtconf`·`hostname`·`host` 명령 조합으로 MAC·IP·서브넷 마스크·게이트웨이·DNS·포트스캔 정보를 조회한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
