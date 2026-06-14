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

파일의 기밀성 보호를 위해 파일 암호화 및 복호화 기능을 제공한다. 전자정부 표준프레임워크의 암호화 라이브러리를
활용하여 ARIA 및 AES 등 블록 암호 알고리즘으로 파일 데이터를 처리한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일보안에서 제공하는 기능은 다음과 같다.

1. 파일 데이터를 암호화하는 기능
2. 암호화된 파일 데이터를 복호화하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Util | `egovframework.com.utl.sim.service.EgovFileSecuUtil.java` | 파일보안 유틸리티 클래스 | |
| Config | `context-crypto.xml` | 암호화 서비스 설정 파일 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileSecu.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일보안 기능은 `EgovFileSecuUtil` 클래스와 `EgovCryptoService`를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| byte[] | `encrypt(byte[] data)` | 파일 암호화 | 파일 데이터를 설정된 알고리즘으로 암호화한다. |
| byte[] | `decrypt(byte[] data)` | 파일 복호화 | 암호화된 파일 데이터를 복호화한다. |

### 환경 설정

`pom.xml`에 암호화 라이브러리를 추가하고, `context-crypto.xml`에 암호화 서비스를 설정한다.

#### pom.xml

```xml
<dependency>
    <groupId>org.egovframe.rte</groupId>
    <artifactId>org.egovframe.rte.fdl.crypto</artifactId>
    <version>${org.egovframe.rte.version}</version>
</dependency>
```

#### context-crypto.xml

```xml
<bean id="egovCryptoService"
    class="egovframework.rte.fdl.cryptography.impl.EgovARIACryptoServiceImpl">
    <property name="keySize" value="128"/>
    <property name="cryptoKey" value="{암호화키}"/>
</bean>
```

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileSecuUtil;

// 파일 데이터 암호화
byte[] originalData  = fileInputStream.readAllBytes();
byte[] encryptedData = EgovFileSecuUtil.encrypt(originalData);

// 파일 데이터 복호화
byte[] decryptedData = EgovFileSecuUtil.decrypt(encryptedData);
```

## 참고자료

- N/A
