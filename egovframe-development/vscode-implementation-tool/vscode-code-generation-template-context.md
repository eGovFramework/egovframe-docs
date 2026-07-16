---
title: Download Template Context
linkTitle: "Template Context"
description: "eGovFrame Initializr in VSCode (VS Code Extension)의 CRUD Code Generation 내 기능들 중 Download Template Context 기능을 안내한다."
url: /egovframe-development/vscode-implementation-tool/vscode-code-generation/template-context/
menu:
  depth:
    weight: 3
    parent: "vscode-code-generation"
    identifier: "template-context"
---
# Download Template Context

## 개요

본 문서는 eGovFrame Initializr in VSCode 확장의 CRUD Code Generation 기능 중 **Download Template Context** 기능을 안내한다.

**Download Template Context**는 코드 생성에 사용되는 템플릿 컨텍스트 데이터를 JSON 파일로 다운로드하는 기능이다. 커스텀 Handlebars 템플릿을 작성할 때 어떤 변수를 사용할 수 있는지 확인하기 위한 참조 자료로 활용한다.

## 사용 방법

1. [DDL 입력](./vscode-code-generation.md) 과정에서 유효한 `CREATE TABLE` 문을 입력한다. 유효한 DDL이 입력되면 버튼이 활성화된다.
2. **Download Template Context** 버튼을 클릭한다.
3. 파일 저장 대화상자가 열리면 저장 위치를 선택하고 파일을 저장한다.
4. 다운로드된 JSON 파일을 열어 커스텀 템플릿 작성 시 사용할 수 있는 변수 구조를 확인한다.

## Template Context JSON 구조

다운로드되는 JSON 파일의 최상위 구조는 다음과 같다.

```json
{
  "tableName": "Board",
  "packageName": "egovframework.example.sample",
  "className": "Board",
  "classNameFirstCharLower": "board",
  "author": "author",
  "date": "2026-02-26",
  "version": "1.0.0",
  "attributes": [ ... ],
  "pkAttributes": [ ... ]
}
```

### 최상위 필드

| 필드 | 타입 | 설명 |
|---|---|---|
| `tableName` | `string` | DDL에서 파싱한 테이블명 (PascalCase). 클래스명으로 사용된다. |
| `packageName` | `string` | Code Generator 탭의 Package Name 입력값 |
| `className` | `string` | 클래스명 (`tableName`과 동일) |
| `classNameFirstCharLower` | `string` | 클래스명의 첫 글자를 소문자로 변환한 값. 빈 이름, 변수명, URL 경로 등에 활용된다. |
| `author` | `string` | 작성자 (`author` 고정값) |
| `date` | `string` | 파일 생성 날짜 (`YYYY-MM-DD` 형식) |
| `version` | `string` | 버전 (`1.0.0` 고정값) |
| `attributes` | `Column[]` | 전체 컬럼 배열 |
| `pkAttributes` | `Column[]` | PK 컬럼만 필터링한 배열 |

### Column 객체 구조

`attributes`와 `pkAttributes` 배열의 각 항목 구조이다.

```json
{
  "columnName": "BOARD_ID",
  "ccName": "boardId",
  "pcName": "BoardId",
  "dataType": "VARCHAR",
  "javaType": "String",
  "isPrimaryKey": true
}
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `columnName` | `string` | 원본 컬럼명 (SQL 원문 그대로). 예) `BOARD_ID`, `REGIST_DATE` |
| `ccName` | `string` | camelCase로 변환된 컬럼명. Java 필드명, MyBatis 파라미터명으로 사용된다. 예) `boardId` |
| `pcName` | `string` | PascalCase로 변환된 컬럼명. getter/setter 메서드명 생성에 사용된다. 예) `BoardId` |
| `dataType` | `string` | SQL 데이터 타입. 예) `VARCHAR`, `INT`, `DATETIME` |
| `javaType` | `string` | 매핑된 Java 타입. 예) `String`, `int`, `java.util.Date` |
| `isPrimaryKey` | `boolean` | `PRIMARY KEY` 여부 |

## 활용 예시

아래 DDL을 입력하고 Package Name을 `egovframework.example.sample`로 설정한 뒤 다운로드하면 다음과 같은 JSON이 생성된다.

### 입력 DDL

```sql
CREATE TABLE BOARD (
  BOARD_ID   VARCHAR(20)  NOT NULL,
  TITLE      VARCHAR(200) NOT NULL,
  CONTENT    TEXT,
  REGIST_DT  DATETIME,
  PRIMARY KEY (BOARD_ID)
);
```

### 다운로드되는 JSON

```json
{
  "tableName": "Board",
  "packageName": "egovframework.example.sample",
  "className": "Board",
  "classNameFirstCharLower": "board",
  "author": "author",
  "date": "2026-02-26",
  "version": "1.0.0",
  "attributes": [
    {
      "columnName": "BOARD_ID",
      "ccName": "boardId",
      "pcName": "BoardId",
      "dataType": "VARCHAR",
      "javaType": "String",
      "isPrimaryKey": true
    },
    {
      "columnName": "TITLE",
      "ccName": "title",
      "pcName": "Title",
      "dataType": "VARCHAR",
      "javaType": "String",
      "isPrimaryKey": false
    },
    {
      "columnName": "CONTENT",
      "ccName": "content",
      "pcName": "Content",
      "dataType": "TEXT",
      "javaType": "String",
      "isPrimaryKey": false
    },
    {
      "columnName": "REGIST_DT",
      "ccName": "registDt",
      "pcName": "RegistDt",
      "dataType": "DATETIME",
      "javaType": "java.util.Date",
      "isPrimaryKey": false
    }
  ],
  "pkAttributes": [
    {
      "columnName": "BOARD_ID",
      "ccName": "boardId",
      "pcName": "BoardId",
      "dataType": "VARCHAR",
      "javaType": "String",
      "isPrimaryKey": true
    }
  ]
}
```

이 JSON을 참고하여 커스텀 Handlebars 템플릿에서 `{{tableName}}`, `{{#each attributes}}`, `{{ccName}}` 등의 변수를 활용할 수 있다. 자세한 내용은 [Generate with Custom Templates](./vscode-code-generation-custom-templates.md)를 참고한다.
