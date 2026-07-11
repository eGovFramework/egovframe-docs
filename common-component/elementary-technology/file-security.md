---
title: "파일보안"
linkTitle: "파일보안"
description: "파일보안"
url: /common-component/elementary-technology/system/file-security/
menu:
  depth:
    name: "파일보안"
    weight: 29
    parent: "system"
---

## 개요

암호화 알고리즘을 사용하여 파일을 암호화하거나 역으로 복호화하는 기능을 제공한다. 다양한 파일 포맷의 암호화/복호화를 지원하며,
문자열 데이터의 인코딩/디코딩과 복호화가 불가능한 비밀번호 암호화 기능도 함께 제공한다.
서버(Server) 및 클라이언트(Client) 응용 애플리케이션에서 파일 보안 처리 시 활용할 수 있다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일보안에서 제공하는 기능은 다음과 같다.

1. 암호화 알고리즘에 의해 파일을 암호화하는 기능
2. 복호화 알고리즘을 사용하여 파일을 복호화하는 기능
3. 문자열 데이터를 암호화(인코딩)/복호화(디코딩)하는 기능
4. 비밀번호를 복호화가 불가능한 방식(단방향 해시)으로 암호화하고 검증하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileScrty.java` | 파일 암호화/복호화 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileScrty.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일보안 기능은 `EgovFileScrty` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `encryptFile(String source, String target)` | 파일 암호화 | 원본파일(`source`)을 암호화하여 결과파일(`target`)로 생성한다. 성공 시 `true`, 실패 시 `false` 리턴 |
| boolean | `decryptFile(String source, String target)` | 파일 복호화 | 암호화된 파일(`source`)을 복호화하여 결과파일(`target`)로 생성한다. 성공 시 `true`, 실패 시 `false` 리턴 |
| String | `encode(String data)` | 데이터 암호화 | String 데이터를 암호화(인코딩) 처리한다 |
| String | `decode(String data)` | 데이터 복호화 | 암호화(인코딩)된 String 데이터를 복호화(디코딩) 처리한다 |
| String | `encryptPassword(String password, String id)` | 비밀번호 암호화 | 비밀번호를 복호화가 불가능한 단방향 해시로 암호화한다 (아이디를 salt로 사용) |
| boolean | `checkPassword(String data, String encoded, byte[] salt)` | 비밀번호 검증 | 입력한 비밀번호가 암호화되어 저장된 비밀번호와 일치하는지 검증한다 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `source`: String 타입의 절대경로를 포함한 원본 파일명 (예: `/user/com/test/file1.txt`)
- `target`: String 타입의 절대경로를 포함한 결과 파일명 (예: `/user/com/test/encodeFile1.txt`)
- `data`: String 타입의 암호화/복호화 대상 데이터
- `password`, `id`: String 타입의 비밀번호와 salt로 사용할 아이디

#### 반환값 정의 (Output)

- boolean 타입: 처리 성공 여부 (`true` / `false`)
- String 타입: 암호화/복호화된 문자열

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileScrty;

// 1. 파일 암호화
String source = "/user/com/test/file1.txt";
String target = "/user/com/test/encodeFile1.txt";
boolean result1 = EgovFileScrty.encryptFile(source, target);

// 2. 파일 복호화
String decTarget = "/user/com/test/decodeFile1.txt";
boolean result2 = EgovFileScrty.decryptFile(target, decTarget);

// 3. 비밀번호 암호화
String encrypted = EgovFileScrty.encryptPassword("password1!", "userId");
```

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
