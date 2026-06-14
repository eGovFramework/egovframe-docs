---
title: "파일시스템모니터링"
linkTitle: "파일시스템모니터링"
description: "파일시스템모니터링"
url: /common-component/elementary-technology/system/file-system-monitoring/
menu:
  depth:
    name: "파일시스템모니터링"
    weight: 48
    parent: "system"
---

## 개요

시스템의 안정적인 운영을 위해 파일시스템의 상태를 모니터링하고 관련 정보를 관리하는 기능을 제공한다.
모니터링 항목 관리, 로그 조회 및 시스템 정상 서비스 여부 확인 기능을 포함한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일시스템모니터링에서 제공하는 기능은 다음과 같다.

1. 파일시스템 모니터링 정보(속성)를 조회하는 기능
2. 파일시스템 모니터링 항목을 등록·수정·삭제하는 기능
3. 모니터링 로그를 조회하는 기능
4. 시스템의 정상 서비스 여부를 확인하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Controller | `egovframework.com.utl.sys.fsm.web.EgovFileSysMntrController.java` | 파일시스템모니터링 컨트롤러 | |
| Service | `egovframework.com.utl.sys.fsm.service.EgovFileSysMntrService.java` | 파일시스템모니터링 서비스 인터페이스 | |
| ServiceImpl | `egovframework.com.utl.sys.fsm.service.impl.EgovFileSysMntrServiceImpl.java` | 파일시스템모니터링 서비스 구현체 | |

### 화면 구성

| 화면명 | 설명 |
| --- | --- |
| 파일시스템모니터링 목록 | 등록된 모니터링 항목 목록 및 상태 조회 |
| 파일시스템모니터링 상세 | 특정 모니터링 항목 상세 정보 확인 |
| 파일시스템모니터링 등록 | 신규 모니터링 항목 등록 |
| 모니터링 로그 목록 | 파일시스템 상태 변경 이력 로그 조회 |

### 사용 방법

```java
import egovframework.com.utl.sys.fsm.service.EgovFileSysMntrService;
import egovframework.com.utl.sys.fsm.service.FileSysMntrVO;

// 파일시스템 모니터링 목록 조회
List<FileSysMntrVO> mntrList = egovFileSysMntrService.selectFileSysMntrList(searchVO);

// 파일시스템 모니터링 항목 등록
FileSysMntrVO mntrVO = new FileSysMntrVO();
mntrVO.setFilePath("/product/jeus/upload");
mntrVO.setMntrCycle("10"); // 모니터링 주기(분)
egovFileSysMntrService.insertFileSysMntr(mntrVO);
```

## 참고자료

- N/A
