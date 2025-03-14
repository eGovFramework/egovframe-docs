---
title: FTP Service
linkTitle: "FTP"
description: Apache Commons Net을 사용하여 FTP 서비스를 제공하며, FTP 클라이언트를 통해 파일 업로드, 다운로드, 삭제, 디렉토리 생성 등의 기능을 구현할 수 있다. FTP 사용 예제 및 파일 전송 설정 방법을 함께 제공한다.
url: /egovframe-runtime/foundation-layer/ftp/
menu:
    depth:
        name: FTP
        weight: 13
        parent: "foundation-layer"
---
# FTP Service

## 개요

**전자정부 표준프레임워크**는 <acronym title="File Transfer Protocol">FTP</acronym> 서비스제공을 위해 Apache Commons Net™ [단순 클라이언트측의 기본적인 Internet Protocol의 구현의 FTP기능을 편리하게 제공]을 오픈 소스로 채택하였다.

Apache Commons Net™은 Network utility collection 이다.
Apache Commons Net™은 단순 클라이언트측의 기본적인 Internet Protocol을 구현함으로서 기본적인 프로토콜 access가 목적이기 때문에 부분적으로 object-orient 규칙에 위배가 되는 사항이 있다는 것을 참고적으로 알고 있어야 한다.

### FTP정의

FTP란 FTP (File Transfer Protocol) 파일 전송 프로토콜로 FTP[에프 티 피]는 인터넷상의 컴퓨터들 간에 파일을 교환하기 위한 표준 프로토콜로서 가장 간단한 방법이기도 하다.
화면에 표시할 수 있는 웹 페이지와 관련 파일들을 전송하는 HTTP, 전자우편을 전송하는 SMTP 등과 같이, FTP 역시 인터넷의 TCP/IP 응용 프로토콜 중의 하나이다.
FTP는 웹 페이지 파일들을 인터넷상에서 모든 사람이 볼 수 있도록 하기 위해 저작자의 컴퓨터로부터 서버로 옮기는 과정에서 사용된다.
또한, 다른 서버들로부터 자신의 컴퓨터로 프로그램이나 파일들을 다운로드 하는 데에도 많이 사용된다. 
사용자 입장에서는 간단한 명령을 이용하여 FTP를 쓰거나, 또는 그래픽 사용자 인터페이스를 제공하는 상용 프로그램을 쓸 수도 있다. 
보통은 웹 브라우저도 웹 페이지로부터 선택한 프로그램을 다운로드 하는데 FTP를 사용한다. 
FTP를 사용하여 서버에 있는 파일을 지우거나 이름을 바꾸거나 옮기거나 복사하는 등 갱신작업을 할 수도 있다. 
FTP 서버에는 로그온을 해야하지만, 익명의 FTP를 사용하여 모든 사람들에게 공개된 파일들을 쉽게 접근할 수 있도록 하고 있다. 
FTP는 보통 TCP/IP에 함께 제공되는 일련의 프로그램 속에 포함되어 있다.

## 설명

### Apache Commons Net™

Apache Commons Net™ 프로젝트([http://commons.apache.org/net/](http://commons.apache.org/net/))에서 지원하는 프로토콜은 다음과 같다.

- <acronym title="File Transfer Protocol">FTP</acronym>/FTPS
- <acronym title="File Transfer Protocol">FTP</acronym> over <acronym title="Hyper Text Transfer Protocol">HTTP</acronym> (experimental)
- NNTP
- <acronym title="Simple Mail Transfer Protocol">SMTP</acronym>(S)
- <acronym title="Post Office Protocol 3">POP3</acronym>(S)
- <acronym title="Internet Message Access Protocol">IMAP</acronym>(S)
- Telnet
- TFTP
- Finger
- Whois
- rexec/rcmd/rlogin
- Time (rdate) and Daytime
- Echo
- Discard
- NTP/SNTP

Apache Commons Net - org.apache.commons.net.ftp 의 동작흐름에 대하여 간략히 설명한다.

논리적 흐름도는 아래와 같다.

```
1. FTP Client를 생성
2. FTP Server에 Connect 서버에 연결한다
3. 응답이 정상적인지 확인한다.
4. FTP Server 로그인한다
5. 접속하여 여러가지 작업(list, get, put....등등)
6. FTP Server 로그아웃한다
7. FTP Server disconnect
```

다음은 사용예제는 FTP에 접속하여 리스트를 볼수 있는 예제이다.

#### 사용예제

```java
private static FileInputStream inputStream;
 
public static void main(String[] args) {
 
	FTPClient client = null;
 
	// 계정 로그인
	try {
		client = new FTPClient();
 
		// 한글파일명 때문에 디폴트 인코딩을 euc-kr로 한다.
		client.setControlEncoding("euc-kr");
 
		// Test 서버 정보
		logger.info("Commons NET FTP Client Test Program");
		logger.info("Start GO");
 
		// Novell TEST서버에 접속
		client.connect("ftp.novell.com");
		logger.info("Connected to ...........");
 
		// 응답코드가 비정상일 경우 종료함
		int reply = client.getReplyCode();
		if (!FTPReply.isPositiveCompletion(reply)) {
			client.disconnect();
			logger.info("FTP server refused connection");
 
		} else {
			logger.info(client.getReplyString());
 
			// timeout을 설정
			client.setSoTimeout(10000);
			// 로그인
			client.login("anonymous", "anonymous");
			logger.info("anonymous login success...");
 
 
			// 각종 정보를 처리 (Put / Get / Append등)
 
 
			client.logout();
		}
 
	} catch (Exception e) {
		logger.info("해당 ftp 로그인 실패하였습니다.");
		e.printStackTrace();
		System.exit(-1);
	} finally {
		if(client != null && client.isConnected()){
			try {
				client.disconnect();
			}catch(IOException ioe) {
				ioe.printStackTrace();
			}
		}
	}
}
```

#### 파일 리스트 보기

```java
FTPFile[] ftpfiles = client.listFiles("/");
 
if (ftpfiles != null ) {
	for (int i = 0; i < ftpfiles.length; i++) {
		FTPFile file = ftpfiles[i];
		logger.info(file.toString()); // 파일정보
		logger.info(file.getName()); // 파일명 
		logger.info(file.getSize()); // 파일사이즈
	}
}
```

#### 파일 다운로드 (get)

```java
File get_file = new File("c:\\temp\\test.jpg");
FileOutputStream outputstream = new FileOutputStream(get_file);
boolean result = client.retrieveFile("/public/test.jpg", outputstream);
 
outputstream.close();
```

#### 파일 업로드 (put)

```java
File put_file = new File("c:\\temp\\test.jpg");
inputStream = new FileInputStream(put_file);
boolean result = client.storeFile("/public/test.jpg", inputStream);
 
inputStream.close();
```

#### 파일 업로드 (append)

```java
File append_file = new File("c:\\temp\\test.jpg");
inputStream = new FileInputStream(append_file);
boolean result = client.appendFile("/public/test.jpg", inputStream);
 
inputStream.close();
```

#### 파일 이름변경 (rename)

```java
boolean result = client.rename("/public/바꾸기전.jpg", "/public/바꾼후.jpg");
```

#### 파일 삭제 (delete)

```java
boolean result = client.deleteFile("/public/삭제할.jpg");
```

#### Dircetory 생성

```java
boolean result = client.makeDirectory("/public/test");
```

#### OS 커맨드 입력하기

```java
client.sendCommand(FTPCommand.MAKE_DIRECTORY,"/public/test");
```

#### 파일 및 전송상태 설정

- 파일 타입 : <acronym title="File Transfer Protocol">FTP</acronym>.BINARY_FILE_TYPE, <acronym title="File Transfer Protocol">FTP</acronym>.ASCII_FILE_TYPE, 등 설정 - 파일 전송 형태 : <acronym title="File Transfer Protocol">FTP</acronym>.STREAM_TRANSFER_MODE, COMPRESSED_TRANSFER_MODE 등 설정

```java
/* 파일 타입*/
client.setFileType(FTP.BINARY_FILE_TYPE);
```

```java
/* 파일 전송 형태 */
client.setFileTransferMode(FTP.COMPRESSED_TRANSFER_MODE);
```

```java
/* Mail - IMAP[S] Client 사용 */
public final class IMAPMail {
  public static void main(String[] args) {
      if (args.length < 3) {
          System.err.println(
              "Usage: IMAPMail <imap server hostname> <username> <password> [TLS]");
          System.exit(1);
      }
      String server = args[0];
      String username = args[1];
      String password = args[2];
      String proto = (args.length > 3) ? args[3] : null;
      IMAPClient imap;
      if (proto != null) {
          System.out.println("Using secure protocol: " + proto);
          imap = new IMAPSClient(proto, true); // implicit
        
      } else {
          imap = new IMAPClient();
      }
      System.out.println("Connecting to server " + server + " on " + imap.getDefaultPort());
      imap.setDefaultTimeout(60000);
      // suppress login details
      imap.addProtocolCommandListener(new PrintCommandListener(System.out, true));
      try {
          imap.connect(server);
      } catch (IOException e) {
          throw new RuntimeException("Could not connect to server.", e);
      }
      try {
          if (!imap.login(username, password)) {
              System.err.println("Could not login to server. Check password.");
              imap.disconnect();
              System.exit(3);
          }
          imap.setSoTimeout(6000);
          imap.capability();
          imap.select("inbox");
          imap.examine("inbox");
          imap.status("inbox", new String[]{"MESSAGES"});
          imap.logout();
          imap.disconnect();
      } catch (IOException e) {
          System.out.println(imap.getReplyString());
          e.printStackTrace();
          System.exit(10);
          return;
      }
  }
}
```

## Commons Net 2.x to Commons Net 3.0

Version 3.0의 binary는 호환이 보장 되지만 소스코드는 아래와 같은 내용이 변경되었다.

사용되지 않는 여러 상수들이 제거되었으며, binary 호환성에 영향을 주지않는 exception, public methods 들은 더이상 IOException 을 throw 하지 않도록 보완/수정되었다.

- TelnetClient#addOptionHandler(TelnetOptionHandler)
- TelnetClient#deleteOptionHandler(int)

## 참고자료

[Jakarta Commons Net](http://commons.apache.org/net/)