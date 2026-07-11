---
title: "파일송/수신"
linkTitle: "파일송/수신"
description: "파일송/수신"
url: /common-component/elementary-technology/system/file-send-receive/
menu:
  depth:
    name: "파일송/수신"
    weight: 35
    parent: "system"
---

## 개요

FTP 프로토콜을 사용하여 파일을 송수신하는 기능을 제공한다. 서버(Server) 간 파일 송수신 및 서버(Server)와
클라이언트(Client) 간 파일 송수신 시 사용할 수 있다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

### 기능 설명

파일송/수신에서 제공하는 기능은 다음과 같다.

1. FTP 클라이언트(Client)에서 서버(Server)로 파일을 전송하는 기능
2. FTP 서버(Server)에서 로컬로 파일을 전송받는 기능

### 관련 소스

| 유형 | 대상소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFtpTool.java` | 파일송수신 요소기술 클래스 | |
| JSP | `WEB_INF/jsp/egovframework/cmm/utl/EgovFtpTool.jsp` | 테스트 페이지 | |

### 클래스 및 메소드 설명

파일송/수신 기능은 `EgovFtpTool` 클래스의 메소드를 활용하여 제공한다.

<!-- markdownlint-disable MD013 -->
| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| boolean | `getFile(String ftp_ip, int ftp_port, String ftp_id, String ftp_pw, String remote)` | 파일수신 | FTP 서버로부터 파일을 다운로드한다 |
| boolean | `getFile(String ftp_ip, int ftp_port, String ftp_id, String ftp_pw, int ftp_mode, String remote)` | 파일수신 | FTP 서버로부터 파일을 다운로드한다 (전송모드 지정) |
| boolean | `getFile(String ftp_ip, int ftp_port, String ftp_id, String ftp_pw, int ftp_mode, String remote, String local)` | 파일수신 | FTP 서버로부터 파일을 지정한 로컬 경로로 다운로드한다 |
| byte[] | `getFileAsByte(String ftp_ip, int ftp_port, String ftp_id, String ftp_pw, int ftp_mode, String remote, String local)` | 파일읽기 | FTP 서버로부터 파일을 읽어 byte[]로 반환한다 |
| boolean | `sendFile(String ftp_ip, int ftp_port, String ftp_id, String ftp_pw, String local)` | 파일송신 | FTP 서버로 파일을 업로드한다 |
| boolean | `sendFile(String ftp_ip, int ftp_port, String ftp_id, String ftp_pw, int ftp_mode, String local)` | 파일송신 | FTP 서버로 파일을 업로드한다 (전송모드 지정) |
| boolean | `sendFile(String ftp_ip, int ftp_port, String ftp_id, String ftp_pw, int ftp_mode, InputStream data, String remote)` | 파일쓰기 | FTP 서버로 데이터(InputStream)를 업로드한다 |
| boolean | `connect(FTPClient ftpClient, String ftp_ip, int ftp_port, String ftp_id, String ftp_pw, int ftp_mode)` | FTP연결 | FTP 클라이언트를 연결한다 |
| void | `disconnect(FTPClient ftpClient)` | FTP연결종료 | FTP 클라이언트 연결을 종료한다 |
| boolean | `changeRemoteDrctry(FTPClient ftpClient, String remote_drctry)` | 디렉토리이동 | FTP 서버의 디렉토리로 이동한다 |
| String[] | `splitPathAndName(String path, String fileSep)` | 파일명분리 | 파일명이 포함된 전체경로를 파일경로와 파일명으로 분리한다 |
<!-- markdownlint-restore -->

#### 파라미터 정의 (Input)

- `ftp_ip`: String 타입의 FTP 접속 아이피 (예: `192.168.200.21`)
- `ftp_port`: int 타입의 FTP 접속 포트 (예: `21`)
- `ftp_id` / `ftp_pw`: String 타입의 FTP 접속 계정 정보
- `ftp_mode`: int 타입의 FTP 전송모드
- `remote`: String 타입의 절대경로를 포함한 원격 파일명 (예: `/user/com/test/file1.txt`)
- `local`: String 타입의 절대경로를 포함한 로컬 파일명 (예: `/user/com/test/ftp/downFile1.txt`)

#### 반환값 정의 (Output)

- boolean 타입: 송수신 성공 여부 (`true` / `false`)

### 사용 방법

```java
import egovframework.com.utl.sim.service.EgovFtpTool;

String ip = "192.168.200.21";
int port = 21;
String id = "com";
String pw = "com01";
int mode = 0;

// 1. FTP 파일 수신
String remote = "/user/com/test/file1.txt";
String local = "/user/com/test/ftp/downFile1.txt";
boolean result1 = EgovFtpTool.getFile(ip, port, id, pw, mode, remote, local);

// 2. FTP 파일 송신
boolean result2 = EgovFtpTool.sendFile(ip, port, id, pw, mode, local);
```

## 환경설정

N/A

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
