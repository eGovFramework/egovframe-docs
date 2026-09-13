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

파일과 문자열 데이터를 Base64 방식으로 인코딩/디코딩하는 기능과 복호화가 불가능한 비밀번호 암호화 기능을 제공한다.
`encryptFile`, `decryptFile`, `encode`, `decode`는 메소드 이름과 달리 암호화 알고리즘이 아닌 Base64 인코딩/디코딩을 수행한다.
서버(Server) 및 클라이언트(Client) 응용 애플리케이션에서 파일 보안 처리 시 활용할 수 있다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일보안에서 제공하는 기능은 다음과 같다.

1. 파일을 Base64로 인코딩하는 기능
2. Base64로 인코딩된 파일을 디코딩하는 기능
3. 문자열 데이터를 Base64로 인코딩/디코딩하는 기능
4. 비밀번호를 복호화가 불가능한 방식(단방향 해시)으로 암호화하고 검증하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileScrty.java` | 파일 암호화/복호화 요소기술 클래스 | |

### 클래스 및 메소드 설명

파일보안 기능은 `EgovFileScrty` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `encryptFile(String source, String target)` | 파일 인코딩 | 원본파일(`source`)을 Base64로 인코딩하여 결과파일(`target`)로 생성한다. 성공 시 `true`, 실패 시 `false` 리턴 |
| boolean | `decryptFile(String source, String target)` | 파일 디코딩 | Base64로 인코딩된 파일(`source`)을 디코딩하여 결과파일(`target`)로 생성한다. 성공 시 `true`, 실패 시 `false` 리턴 |
| String | `encode(String data)` | 데이터 인코딩 | String 데이터를 Base64로 인코딩한다 |
| String | `decode(String data)` | 데이터 디코딩 | Base64로 인코딩된 String 데이터를 디코딩한다 |
| String | `encryptPassword(String password, String id)` | 비밀번호 암호화 | 비밀번호를 복호화가 불가능한 단방향 해시로 암호화한다 (아이디를 salt로 사용) |
| boolean | `checkPassword(String data, String encoded, byte[] salt)` | 비밀번호 검증 | 입력한 비밀번호가 암호화되어 저장된 비밀번호와 일치하는지 검증한다 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `source`: `Globals.fileStorePath` 아래의 원본 파일명 (예: `file1.txt`). 경로를 포함해도 파일명만 사용한다.
- `target`: `Globals.fileStorePath` 아래에 생성할 결과 파일명 (예: `encodeFile1.txt`)
- `data`: String 타입의 인코딩/디코딩 대상 데이터
- `password`, `id`: String 타입의 비밀번호와 salt로 사용할 아이디

#### 반환값 정의 (Output)

- boolean 타입: 처리 성공 여부 (`true` / `false`)
- String 타입: 인코딩/디코딩된 문자열

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileScrty;

// 1. 파일 인코딩
String source = "file1.txt";
String target = "encodeFile1.txt";
boolean result1 = EgovFileScrty.encryptFile(source, target);

// 2. 파일 디코딩
String decTarget = "decodeFile1.txt";
boolean result2 = EgovFileScrty.decryptFile(target, decTarget);

// 3. 비밀번호 암호화
String encrypted = EgovFileScrty.encryptPassword("password1!", "userId");
```

## 환경설정

`globals.properties`의 `Globals.fileStorePath`에 파일 저장 경로를 설정한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
