---
  title: Resource close 처리
  linkTitle: Resource close 처리
  description: "자원(Stream, DB 관련 Object, Socket 관련 Object)에 대한 해제 처리 기능을 제공한다."
  url: /common-component/elementary-technology/resourceclose/
  menu:
    depth:
      name: Resource close 처리
      weight: 9
      parent: "new-components-v3.2"
      identifier: "resourceclose"
---



# 요소기술 - Resource close 처리

## 개요

 자원(Stream, DB 관련 Object, Socket 관련 Object)에 대한 해제 처리 기능을 제공한다.

## 설명

 한 개 또는 다수의 resource를 타입별로 동시에 close할 수 있도록 메소드를 제공한다.

 close 할 resource를 파라미터로 넘기면 해당 자원을 close해 준다.

##### 관련소스

| 유형 | 대상소스 | 설명 | 비고 |
| --- | --- | --- | --- |
| Util | egovframework.com.cmm.util.EgovResourceCloseHelper.java | Resource close 처리 관련 유틸리티 |  |

## 사용방법

 EgovResourceCloseHelper는 다음과 같은 메소드를 제공한다.

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| void | close(Closeable … resources) | Resource close 처리 |  |
| void | closeDBObjects(Wrapper … objects) | JDBC 관련 resource 객체 close 처리 |  |
| void | closeSocketObjects(Socket socket, ServerSocket server) | Socket 관련 resource 객체 close 처리 |  |
| void | closeSockets(Socket … sockets) | Socket 관련 resource 객체 close 처리 |  |

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
...
 
// 사용 완료된 resource close하기
EgovResourceCloseHelper.close(buffResInput, buffResOld);
```

## 참고자료

 **해당없음**