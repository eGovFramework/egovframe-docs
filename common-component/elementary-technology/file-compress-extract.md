---
title: "파일압축/해제"
linkTitle: "파일압축/해제"
description: "파일압축/해제"
url: /common-component/elementary-technology/system/file-compress-extract/
menu:
  depth:
    name: "파일압축/해제"
    weight: 36
    parent: "system"
---

<!-- markdownlint-disable MD025 -->
# 파일압축/해제

## 개요

비즈니스 로직을 처리하면서 필요한 파일 또는 디렉토리의 압축 및 압축 해제를 위한 공통 기능을 제공한다.
본 기능은 전자정부 표준프레임워크 공통컴포넌트 요소기술 내에 구성되어 있다.

## 설명

파일 또는 디렉토리를 `zip` 형태로 압축하거나, `zip` 형태의 압축 파일을 해제하는 기능을 제공한다.

### 관련 소스

| 유형 | 대상 소스명 | 설명 | 비고 |
| --- | --- | --- | --- |
| Service | `egovframework.com.utl.sim.service.EgovFileCmprs.java` | 파일 압축 및 해제 요소기술 클래스 | |
| JSP | `WEB-INF/jsp/egovframework/cmm/utl/EgovFileCmprs.jsp` | 테스트 페이지 | |

### 주요 메소드

| 결과값 | 메소드명 | 설명 | 내용 |
| --- | --- | --- | --- |
| `boolean` | `cmprsFile(String source, String target)` | 압축 | 대상(`source`), 압축 파일(`target`) 경로로 압축 여부 반환 |
| `boolean` | `decmprsFile(String source, String target)` | 압축 해제 | 압축 파일(`source`), 해제 경로(`target`)로 해제 여부 반환 |

#### 입출력 항목

* **Input**
    * 원본 파일: `String` 타입의 절대 경로를 포함한 파일명 (예: `/user/com/test/file1.txt` 또는 디렉토리 경로)
    * 압축 파일: `String` 타입의 절대 경로를 포함한 압축 파일명 (예: `/user/com/test/file1.zip`)
    * 해제 경로: `String` 타입의 절대 경로를 포함한 압축 해제 디렉토리 (예: `/user/com/test`)
* **Output**
    * `boolean` 타입: 성공 시 `true`, 실패 시 `false` 반환

### 환경 설정

별도의 환경 설정은 필요하지 않다.

### 사용 방법

`EgovFileCmprs` 클래스를 사용하여 파일 및 디렉토리를 압축하거나 압축을 해제할 수 있다.

```java
import egovframework.com.utl.sim.service.EgovFileCmprs;

public class Example {
    public static void main(String[] args) {
        String source = "/user/com/sample/test";
        String target = "/user/com/sample/test.zip";

        // 1. 파일 및 디렉토리 압축
        boolean isCompressed = EgovFileCmprs.cmprsFile(source, target);

        // 2. 파일 압축 해제
        if (isCompressed) {
            String src = target;
            String tar = "/user/com/sample/de_test/";
            boolean deCompressed = EgovFileCmprs.decmprsFile(src, tar);
        }
    }
}
```
