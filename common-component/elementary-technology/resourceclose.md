---
  title: Resource close 처리
  linkTitle: Resource close 처리
  description: "자원(Stream, DB 관련 Object, Socket 관련 Object)에 대한 해제 처리 기능을 제공한다."
  url: /common-component/elementary-technology/new-components-v3.2/resourceclose/
  menu:
    depth:
      name: Resource close 처리
      weight: 9
      parent: "new-components-v3.2"
      identifier: "resourceclose"
---



# 요소기술 - Resource close 처리

## 개요

Resource close 처리는 Stream, DB 및 Socket 관련 객체 등 사용이 완료된 자원을 안전하게 해제하기 위한 기능을 제공한다.

여러 개의 자원을 한 번에 전달하여 종료할 수 있으며, 자원의 유형에 따라 적절한 close 메소드를 사용할 수 있다.

## 설명

`EgovResourceCloseHelper`는 한 개 또는 여러 개의 자원을 유형별로 종료할 수 있는 메소드를 제공한다.
종료할 자원을 메소드의 파라미터로 전달하여 Stream, JDBC 및 Socket 관련 자원을 해제할 수 있다.

### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Util | egovframework.com.cmm.util.EgovResourceCloseHelper.java | Resource close 처리 관련 유틸리티 |  |

## 사용방법

 EgovResourceCloseHelper는 다음과 같은 메소드를 제공한다.

| 결과값 | 메소드명 | 설명 |
| --- | --- | --- |
| `void` | `close(Closeable … resources)` | 하나 이상의 `Closeable` 자원을 종료한다. |
| `void` | `closeDBObjects(Wrapper … objects)` | JDBC 관련 자원 객체를 종료한다. |
| `void` | `closeSocketObjects(Socket socket, ServerSocket server)` | `Socket`과 `ServerSocket` 객체를 종료한다. |
| `void` | `closeSockets(Socket … sockets)` | 하나 이상의 `Socket` 객체를 종료한다. |

 close()메소드를 이용하여 다수의 io 관련 resource를 닫는 방법이다.

```java
import egovframework.com.cmm.util.EgovResourceCloseHelper;
 
...
// 사용하고자 하는 resource
BufferedReader buffResInput = new BufferedReader(new InputStreamReader(..., "utf-8"));
BufferedReader buffResOld = new BufferedReader(new InputStreamReader(..., "utf-8"));
 
...
 
// 사용 완료된 resource close하기
EgovResourceCloseHelper.close(buffResInput, buffResOld);
```

## 참고자료

 **해당없음**
