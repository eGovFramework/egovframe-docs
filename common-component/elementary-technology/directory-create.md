---
title: "디렉토리생성"
linkTitle: "디렉토리생성"
description: "비즈니스 로직을 처리하면서 필요에 따라 시스템상에 디렉토리를 생성할 수 있는 공통 기능을 제공한다."
url: /common-component/elementary-technology/system/directory-create/
menu:
  depth:
    name: "디렉토리생성"
    weight: 7
    parent: "system"
---

<!-- markdownlint-disable MD025 -->

# 디렉토리생성

## 개요

디렉토리생성(Directory Create) 기능은 공통컴포넌트의 요소기술 중 하나로, 비즈니스 로직을 처리하면서 필요에 따라
시스템상에 지정된 경로로 디렉토리를 생성할 수 있는 공통 기능을 제공한다.

본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

### 활용 예시

디렉토리 생성 기능은 다음과 같은 상황에서 활용할 수 있다.

- 파일 업로드를 위한 저장 경로를 생성하는 경우
- 로그 또는 백업 디렉토리를 자동으로 생성하는 경우
- 애플리케이션 실행 시 필요한 작업 디렉토리를 초기화하는 경우
- 사용자별 디렉토리를 동적으로 생성하는 경우

## 주요 개념

지정한 절대 경로를 기반으로 새로운 디렉토리(폴더)를 생성할 수 있다.

- 디렉토리를 생성하고자 하는 상위 디렉토리가 존재하지 않는 경우에도 상위 디렉토리를 포함하여 하위 디렉토리까지 전체 경로를 생성할 수 있다.
- 디렉토리 생성에 성공하면 생성된 디렉토리의 절대 경로가 반환되며, 이미 디렉토리가 존재하거나 생성에 실패하는 경우에는 빈 문자열(`""`)이 반환된다.

## 설명

지정한 경로에 새로운 디렉토리를 생성하는 기능을 제공한다.
필요한 경우 존재하지 않는 상위 디렉토리까지 함께 생성하여 전체 경로를 구성할 수 있다.

디렉토리 생성 기능은 `egovframework.com.utl.sim.service.EgovFileTool` 클래스의 `createNewDirectory` 메서드를 사용하여 처리한다.

### 관련 소스

| 유형 | 대상 소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileTool.java` | 파일관리 툴 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovDrctryCreate.jsp` | 테스트 페이지 | |

### 메소드

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| String | `createNewDirectory(String dirCreationPath)` | 디렉토리 생성 | 생성 대상 디렉토리 경로(`dirCreationPath`)를 입력받아 생성한다. 성공 시 생성된 절대 경로, 실패 시 빈 문자열(`""`)을 반환한다. |
<!-- markdownlint-restore -->

### Input

- **dirCreationPath**: String 타입의 절대 경로를 포함하는 생성 대상 디렉토리 경로 (예: `/product/jeus/egovProps/tmp/dir1`)

### Output

- **String** 타입: 생성된 디렉토리의 절대 경로 (성공 시 생성 경로, 실패 시 빈 문자열 `""`)

## 환경설정

해당사항 없음

### 사용 시 주의사항

- 생성 대상 경로에 대한 쓰기 권한이 필요하다.
- 동일한 경로에 디렉토리가 이미 존재하는 경우 빈 문자열(`""`)이 반환될 수 있다.
- 운영체제의 파일 시스템 권한에 따라 디렉토리 생성이 실패할 수 있다.

## 사용방법

```java
import egovframework.com.utl.sim.service.EgovFileTool;

// 생성할 디렉토리의 절대경로 지정
String dirCreationPath = "/user/com/dir1";

// 디렉토리 생성 메소드 호출
String result = EgovFileTool.createNewDirectory(dirCreationPath);

if (!"".equals(result)) {
    // 생성 성공 시 처리 로직
    System.out.println("디렉토리 생성 성공: " + result);
} else {
    // 생성 실패 시 처리 로직
    System.out.println("디렉토리 생성 실패");
}
```

## 참고자료

- [EgovFileTool JavaDoc](https://github.com/eGovFramework/egovframe-common-components/blob/main/src/main/java/egovframework/com/utl/sim/service/EgovFileTool.java)
