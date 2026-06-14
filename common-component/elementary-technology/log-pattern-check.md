---
title: "로그패턴검사"
linkTitle: "로그패턴검사"
description: "로그패턴검사"
url: /common-component/elementary-technology/system/log-pattern-check/
menu:
  depth:
    name: "로그패턴검사"
    weight: 50
    parent: "system"
---

## 개요

시스템 로그 파일의 내용 중에서 특정 문자열이나 정규표현식 패턴과 일치하는 로그 항목을 추출하여 분석할 수 있는 기능을 제공한다.

## 주요 기능

* **로그 파일 분석**: 지정된 로그 파일을 라인 단위로 읽어 패턴을 검사한다.
* **에러 감지**: NullPointerException, OOM 등 시스템의 치명적인 에러 로그를 특정 패턴으로 스캔하여 확인한다.

## 사용법

| 리턴타입 | 메서드명 | 기능 설명 |
| -------- | -------- | --------- |
| `List<String>` | `checkLogPattern(String filePath, String pattern)` | 지정된 로그 파일에서 주어진 정규표현식 패턴과 일치하는 라인들을 반환한다. |

```java
import egovframework.com.utl.sys.log.service.EgovLogPatternUtil;
import java.util.List;

public class LogPatternCheckExample {
    public void checkLog() throws Exception {
        String logFilePath = "/logs/system/catalina.out";
        String searchPattern = ".*NullPointerException.*";
        
        // 로그 패턴 검사
        List<String> matchedLogs = EgovLogPatternUtil.checkLogPattern(logFilePath, searchPattern);
        
        for (String logLine : matchedLogs) {
            System.out.println("Detected Error Log: " + logLine);
        }
    }
}
```
