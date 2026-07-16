---
title: Generate with Custom Templates
linkTitle: "Custom Templates"
description: "eGovFrame Initializr in VSCode (VS Code Extension)의 CRUD Code Generation 내 기능들 중 Generate with Custom Templates 기능을 안내한다."
url: /egovframe-development/vscode-implementation-tool/vscode-code-generation/vscode-custom-templates-generation/
menu:
  depth:
    weight: 2
    parent: "vscode-code-generation"
    identifier: "vscode-custom-templates-generation"
---
# Generate with Custom Templates

## 개요

본 문서는 eGovFrame Initializr in VSCode 확장의 CRUD Code Generation 기능 중 **Generate with Custom Templates** 기능을 안내한다.

**Generate with Custom Templates**는 사용자가 직접 작성한 Handlebars(`.hbs`) 템플릿 파일을 업로드하여 DDL 기반 코드를 원하는 형식으로 생성하는 기능이다. 기본 제공 템플릿 대신 프로젝트 규약에 맞는 커스텀 코드 구조를 정의할 수 있다.

## 사용 방법

1. [DDL 입력 및 설정](./vscode-code-generation.md) 과정을 먼저 완료한다. 유효한 DDL이 입력되면 버튼이 활성화된다.
2. **Generate with Custom Templates** 버튼을 클릭한다.
3. 파일 탐색기에서 커스텀 Handlebars 템플릿 파일(`.hbs`)을 선택한다.
4. 선택한 템플릿을 기반으로 코드가 생성된다.

> 커스텀 템플릿 파일 작성 시 [Download Template Context](./vscode-code-generation-template-context.md) 기능으로 다운로드한 JSON 파일을 참고하면 사용 가능한 변수 목록을 쉽게 파악할 수 있다.

## 커스텀 템플릿 파일 형식

커스텀 템플릿은 **Handlebars**(`.hbs`) 형식으로 작성한다. 기본 제공 템플릿 파일들은 Extension 소스코드의 `templates/code/` 디렉터리에서 확인할 수 있으며, 이를 참고하여 커스텀 템플릿을 작성하면 된다.

### 기본 제공 템플릿 파일 목록

| 파일명 | 설명 |
|---|---|
| `sample-vo-template.hbs` | VO 클래스 템플릿 |
| `sample-default-vo-template.hbs` | Default VO 클래스 템플릿 |
| `sample-service-template.hbs` | Service 인터페이스 템플릿 |
| `sample-service-impl-template.hbs` | ServiceImpl 클래스 템플릿 |
| `sample-controller-template.hbs` | Controller 클래스 템플릿 |
| `sample-mapper-interface-template.hbs` | Mapper 인터페이스 템플릿 |
| `sample-mapper-template.hbs` | MyBatis Mapper XML 템플릿 |
| `sample-thymeleaf-list.hbs` | Thymeleaf 목록 페이지 템플릿 |
| `sample-thymeleaf-register.hbs` | Thymeleaf 등록/수정 페이지 템플릿 |
| `sample-jsp-list.hbs` | JSP 목록 페이지 템플릿 |
| `sample-jsp-register.hbs` | JSP 등록/수정 페이지 템플릿 |

## 템플릿 컨텍스트 변수

템플릿 내에서 사용할 수 있는 변수는 다음과 같다. 전체 구조는 [Download Template Context](./vscode-code-generation-template-context.md) 기능으로 다운로드한 JSON 파일에서 확인할 수 있다.

### 최상위 변수

| 변수 | 타입 | 설명 |
|---|---|---|
| `{{tableName}}` | `string` | 테이블명 (PascalCase 변환). 클래스명으로 사용된다. |
| `{{packageName}}` | `string` | 패키지 이름 |
| `{{className}}` | `string` | 클래스명 (`tableName`과 동일) |
| `{{classNameFirstCharLower}}` | `string` | 클래스명의 첫 글자를 소문자로 변환한 값. 빈 이름, 변수명 등으로 사용된다. |
| `{{author}}` | `string` | 작성자 (`author` 고정값) |
| `{{date}}` | `string` | 생성 날짜 (`YYYY-MM-DD` 형식) |
| `{{version}}` | `string` | 버전 (`1.0.0` 고정값) |
| `{{attributes}}` | `Column[]` | 전체 컬럼 배열 |
| `{{pkAttributes}}` | `Column[]` | PK 컬럼 배열 |

### Column 객체 필드

`attributes`와 `pkAttributes` 배열의 각 항목에서 사용할 수 있는 필드이다.

| 필드 | 타입 | 설명 |
|---|---|---|
| `{{columnName}}` | `string` | 원본 컬럼명 (SQL 대문자 유지). 예) `REGIST_DATE` |
| `{{ccName}}` | `string` | camelCase 변환된 컬럼명. 예) `registDate` |
| `{{pcName}}` | `string` | PascalCase 변환된 컬럼명. 예) `RegistDate` |
| `{{dataType}}` | `string` | SQL 데이터 타입. 예) `VARCHAR` |
| `{{javaType}}` | `string` | 매핑된 Java 타입. 예) `String` |
| `{{isPrimaryKey}}` | `boolean` | PK 여부 |

## 지원 Handlebars 헬퍼

커스텀 템플릿에서 사용할 수 있는 헬퍼 목록이다.

| 헬퍼 | 사용 예 | 설명 |
|---|---|---|
| `eq` | `{{#if (eq pkAttributes.length 1)}}` | 두 값이 같은지 비교 |
| `concat` | `{{concat "#{" ccName "}"}}` | 문자열 연결. Handlebars 표현식 내에 `{{}}`를 삽입할 때 유용하다. |
| `lowercase` | `{{lowercase className}}` | 문자열을 소문자로 변환 |
| `unless` | `{{#unless isPrimaryKey}}` | 조건이 거짓일 때 블록 실행 |
| `setVar` | `{{~setVar "foundFirst" false~}}` | 템플릿 내 변수 설정. `#each` 반복문에서 첫 번째 항목 추적 등에 활용한다. |

### 헬퍼 사용 예시

#### `concat` — MyBatis `#{}` 표현식 삽입

MyBatis XML 내에서 `#{ccName}` 형태의 문자열을 생성해야 할 때, Handlebars `{{}}`와 충돌하므로 `concat` 헬퍼를 사용한다.

```handlebars
{{concat "#{" ccName "}"}}
{{!-- 출력 결과: #{registDate} --}}
```

#### `setVar` + `unless` — 첫 번째 비PK 컬럼 찾기

```handlebars
{{~setVar "foundFirst" false~}}
{{#each attributes}}
  {{#unless isPrimaryKey}}{{#unless @root.foundFirst}}
    AND {{columnName}} LIKE '%' || #{searchKeyword} || '%'
    {{~setVar "foundFirst" true~}}
  {{/unless}}{{/unless}}
{{/each}}
```

#### `eq` — PK 개수에 따른 분기 처리

```handlebars
{{#if (eq pkAttributes.length 1)}}
  vo.set{{pkAttributes.[0].pcName}}(id);
{{else}}
  {{!-- 복수 PK 처리 --}}
{{/if}}
```

## 템플릿 작성 예시

아래는 간단한 커스텀 VO 클래스 템플릿 예시이다.

```handlebars
package {{packageName}}.service;

/**
 * {{className}} Value Object
 */
public class {{className}}VO {

{{#each attributes}}
    /** {{columnName}} */
    private {{javaType}} {{ccName}};

{{/each}}
{{#each attributes}}
    public {{javaType}} get{{pcName}}() { return {{ccName}}; }
    public void set{{pcName}}({{javaType}} {{ccName}}) { this.{{ccName}} = {{ccName}}; }

{{/each}}
}
```
