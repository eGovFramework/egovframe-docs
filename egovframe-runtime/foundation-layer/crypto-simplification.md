---
title: Crypto 간소화 서비스
linkTitle: "Crypto 간소화"
description: 전자정부 표준프레임워크의 Crypto 간소화서비스를 사용한 ARIA 블록암호 기반 암/복호화 설정 및 사용법을 제공한다.
url: /egovframe-runtime/foundation-layer/crypto/crypto-simplification/
menu:
    depth:
        name: Crypto 간소화 서비스
        weight: 2
        parent: "crypto"
---
# Crypto 간소화서비스 설정

전자정부 표준프레임워크 실행환경 구성요소인 Crypto 간소화서비스를 사용한 암호화 설정 및 사용법을 정리한 문서입니다.

## 개요

Crypto 간소화서비스는 ARIA 블록암호 알고리즘 기반 암/복호화 기능을 제공합니다. globals.properties의 DB 연결 정보(Url, UserName, Password) 및 기타 민감 정보를 암호화하여 보호할 수 있습니다.

## 라이브러리 적용

### pom.xml 의존성 추가

```xml
<dependency>
    <groupId>org.egovframe.rte</groupId>
    <artifactId>egovframe-rte-fdl-crypto</artifactId>
</dependency>
```

- 전자정부 Maven 저장소(`https://maven.egovframe.go.kr/maven/`)에서 의존성 해결
- parent POM의 `egovframe.rte.version`에 따라 버전 관리

## 설정 방법

### 1. globals.properties

**경로:** `src/main/resources/egovframework/egovProps/globals.properties`

```properties
# 접근제어 설정 파일 경로 (egov-crypto 모듈이 참조)
Globals.CryptoConfigPath = egovframework/egovProps/conf/egov-crypto-config.properties

# File ID 암호화 키 (반드시 기본값 "egovframe"을 다른 값으로 변경하여 사용)
Globals.File.algorithmKey = egovframe
```

### 2. egov-crypto-config.properties

**경로:** `src/main/resources/egovframework/egovProps/conf/egov-crypto-config.properties`

| 항목 | 필수 | 설명 |
|------|------|------|
| `id` | O | 암호화 설정 빈 식별자 |
| `initial` | O | globals.properties의 Url, UserName, Password 로드 여부 (`true`, `false`) |
| `crypto` | O | 계정 암호화 여부 (`true`: 암호화 사용, `false`: 평문 사용) |
| `algorithm` | O | 계정 암호화 알고리즘 (MD5, SHA-1, SHA-256) |
| `algorithmKey` | O | 계정 암호화 키 |
| `algorithmKeyHash` | O | algorithmKey의 해시값 |
| `cryptoBlockSize` | O | 계정 암호화 블록 사이즈 |
| `cryptoPropertyLocation` | O | 암복호화 대상 설정 파일 경로 |
| `plainDigest` | O | 평문 다이제스트 사용 여부 (`true`, `false`) |

**예시 설정:**

```properties
id = egovCryptoConfig
initial = true
crypto = true
algorithm = SHA-256
algorithmKey = egovframe
algorithmKeyHash = gdyYs/IZqY86VcWhT8emCYfqY1ahw2vtLG+/FzNqtrQ=
cryptoBlockSize = 1024
cryptoPropertyLocation = classpath:/egovframework/egovProps/globals.properties
plainDigest = false
```

> **보안 주의:** `algorithmKey`, `algorithmKeyHash` 값은 반드시 기본값에서 변경하여 사용하세요. 노출을 피하려면 `egov-crypto-config.properties`에서 해당 항목을 삭제하고 WAS VM arguments에 `-Degov.crypto.algorithmKey="(사용자정의 값)"`, `-Degov.crypto.algorithmKeyHash="(생성값)"`으로 등록할 수 있습니다.

## Spring 설정

### context-crypto.xml

**경로:** `src/main/resources/egovframework/spring/com/context-crypto.xml`

egovframe-rte-fdl-crypto의 `@Configuration` 클래스를 스캔하여 `egovEnvCryptoService`, `egovEnvPasswordEncoderService` 등 빈을 자동 등록합니다.

```xml
<context:component-scan base-package="org.egovframe.rte.fdl.crypto">
    <context:include-filter type="annotation" expression="org.springframework.context.annotation.Configuration"/>
    <context:include-filter type="annotation" expression="org.springframework.stereotype.Component"/>
    <context:include-filter type="annotation" expression="org.springframework.stereotype.Service"/>
</context:component-scan>
```

### context-datasource.xml - DB 암호화 복호화

DataSource의 password는 `egovPasswordResolver.resolvePassword()`로 복호화합니다.

```xml
<property name="password" value="#{egovPasswordResolver.resolvePassword('Globals.mysql.Password')}"/>
```

- `EgovPasswordResolver`: `EgovEnvCryptoService`의 `crypto` 설정에 따라 암호화된 값 복호화 또는 평문 반환

## algorithmKey, algorithmKeyHash 생성

`egov-crypto-config.properties`에 사용할 `algorithmKeyHash` 생성 방법:

```java
import org.egovframe.rte.fdl.crypto.EgovPasswordEncoder;

EgovPasswordEncoder egovPasswordEncoder = new EgovPasswordEncoder();
egovPasswordEncoder.setAlgorithm("SHA-256");

String algorithmKey = "(사용자정의 값)";
String algorithmKeyHash = egovPasswordEncoder.encryptPassword(algorithmKey);

// algorithmKeyHash 출력 후 egov-crypto-config.properties에 설정
```

## globals.properties DB 암호화 값 생성

DB 연결 정보(Url, UserName, Password)를 암호화하는 방법:

```java
import org.egovframe.rte.fdl.crypto.EgovEnvCryptoService;

EgovEnvCryptoService cryptoService = context.getBean(EgovEnvCryptoService.class);
String plainText = "데이터베이스_접속_비밀번호";
String encrypted = cryptoService.encrypt(plainText);

// encrypted 값을 globals.properties의 Globals.mysql.Password 등에 설정
```

## 평문 사용 (crypto=false)

개발/테스트 시 평문을 사용하려면:

1. **egov-crypto-config.properties** 수정:
   ```properties
   initial = false
   crypto = false
   ```

2. **context-datasource.xml**에서 `egovPasswordResolver.resolvePassword()`로 조회 시 평문 그대로 반환됨

## 사용법

### EgovEnvCryptoService - 암호화/복호화

```java
import org.egovframe.rte.fdl.crypto.EgovEnvCryptoService;

@Resource(name = "egovEnvCryptoService")
EgovEnvCryptoService cryptoService;

// 암호화 (URL 인코딩 처리)
String encrypted = cryptoService.encrypt(plainText);

// 암호화 (URL 인코딩 미처리)
String encrypted = cryptoService.encryptNone(plainText);

// 복호화 (URL 디코딩 처리)
String decrypted = cryptoService.decrypt(encrypted);

// 복호화 (URL 디코딩 미처리)
String decrypted = cryptoService.decryptNone(encrypted);
```

### EgovPasswordEncoder - 비밀번호 해시

```java
import org.egovframe.rte.fdl.crypto.EgovPasswordEncoder;

@Resource(name = "egovEnvPasswordEncoderService")
EgovPasswordEncoder egovPasswordEncoder;

// 비밀번호 해시 생성
String hashedPassword = egovPasswordEncoder.encryptPassword(plainPassword);

// 비밀번호 검증
boolean matches = egovPasswordEncoder.checkPassword(plainPassword, hashedPassword);
```

### EgovComUtlController - ID 암호화/복호화

```java
// 문자열 암호화 (Base64, URL 인코딩)
String encrypted = EgovComUtlController.encryptId(plainText);

// 암호화 문자열 복호화
String decrypted = EgovComUtlController.decryptId(encrypted);
```

### EgovFileMngController - 파일 ID 암호화

```java
// 파일 ID 암호화
String encrypted = EgovFileMngController.encrypt(atchFileId);

// 세션 ID 포함 파일 ID 암호화 (URL 노출 시 세션 검증용)
String encrypted = EgovFileMngController.encryptSession(atchFileId, sessionId);

// 암호화된 파일 ID 복호화
String decrypted = EgovFileMngController.decrypt(base64CipherId);
```

### JSP에서 사용 (egovc TLD)

```jsp
<%@ taglib prefix="egovc" uri="/WEB-INF/tlds/egovc.tld" %>

<!-- 문자열 암호화 -->
${egovc:encrypt(atchFileId)}

<!-- 세션 ID 포함 암호화 (파일 다운로드 링크 등) -->
${egovc:encryptSession(fileVO.atchFileId, pageContext.session.id)}

<!-- ID 암호화 (URL 인코딩 미처리) -->
${egovc:encryptId(plainId)}
```

## 적용 사례

| 용도 | 사용처 |
|------|--------|
| DB 연결 비밀번호 | context-datasource.xml, EgovPasswordResolver |
| 첨부파일 ID | EgovFileMngController, EgovFileDownloadController, getImage.do |
| 파일 다운로드 URL | egovc:encryptSession (세션 검증 포함) |
| ID 파라미터 암호화 | EgovComUtlController.encryptId/decryptId, EgovCipherIdPropertyEditor |
| 암호화/복호화 테스트 UI | EgovCryptoController (/sec/pki/EgovCryptoInfo.do) |
