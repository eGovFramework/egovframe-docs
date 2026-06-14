---
title: "파일송수신"
linkTitle: "파일송수신"
description: "파일송수신"
url: /common-component/elementary-technology/system/file-send-receive/
menu:
  depth:
    name: "파일송수신"
    weight: 45
    parent: "system"
---

## 개요

FTP(File Transfer Protocol) 또는 SFTP(Secure File Transfer Protocol)를 이용하여 서버 간
파일을 송수신하는 기능을 제공한다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에
구성되어 있다.

## 설명

### 기능 설명

파일송수신에서 제공하는 기능은 다음과 같다.

1. FTP를 이용하여 원격 서버에 파일을 전송(Upload)하는 기능
2. FTP를 이용하여 원격 서버에서 파일을 수신(Download)하는 기능
3. SFTP를 이용하여 SSH 기반 보안 파일을 전송/수신하는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileSndRcv.java` | 파일송수신 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFileSndRcv.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일송수신 기능은 `EgovFileSndRcv` 클래스의 메소드를 활용하여 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `ftpSend(host, port, user, pwd, localPath, remotePath)` | FTP 파일 전송 | FTP로 로컬 파일을 원격 서버에 전송한다. |
| boolean | `ftpReceive(host, port, user, pwd, remotePath, localPath)` | FTP 파일 수신 | FTP로 원격 서버에서 파일을 수신한다. |
| boolean | `sftpSend(host, port, user, pwd, localPath, remotePath)` | SFTP 파일 전송 | SFTP로 로컬 파일을 원격 서버에 전송한다. |
| boolean | `sftpReceive(host, port, user, pwd, remotePath, localPath)` | SFTP 파일 수신 | SFTP로 원격 서버에서 파일을 수신한다. |

#### 파라미터 정의 (Input)

- `host`: 원격 서버 호스트명 또는 IP (String 타입)
- `port`: 접속 포트 번호 (int 타입, FTP: 21, SFTP: 22)
- `user`: 접속 계정 (String 타입)
- `pwd`: 접속 비밀번호 (String 타입)
- `localPath`: 로컬 파일 절대경로 (String 타입)
- `remotePath`: 원격 파일 절대경로 (String 타입)

#### 반환값 정의 (Output)

- boolean 타입: 송수신 성공 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFileSndRcv;

String host       = "ftp.example.go.kr";
int    port       = 21;
String user       = "ftpuser";
String pwd        = "ftppassword";
String localPath  = "/product/jeus/files/report.pdf";
String remotePath = "/upload/report.pdf";

// FTP 파일 전송
boolean sendResult = EgovFileSndRcv.ftpSend(host, port, user, pwd,
    localPath, remotePath);

// SFTP 파일 수신
boolean receiveResult = EgovFileSndRcv.sftpReceive(host, 22, user, pwd,
    remotePath, localPath);
```

## 참고자료

- N/A
