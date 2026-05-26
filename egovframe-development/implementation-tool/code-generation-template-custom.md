---
title: Custom Templates Generation
linkTitle: Custom Templates Gen
description: "사용자 정의 템플릿 추가 기능"
url: /egovframe-development/implementation-tool/code-generation/template-based-code-generation/eclipse-custom-templates-generation/
menu:
  depth:
    weight: 3
    parent: "template-based-code-generation"
    identifier: "eclipse-custom-templates-generation"
---

# Custom Templates Generation

## 개요

전자정부 프레임워크에서 제공하는 기본 템플릿 외에도 사용자가 필요한 템플릿을 작성하여 추가할 수 있는 기능을 제공한다. 전자정부 프레임워크 템플릿 Code Gen.은 플러그인 방식으로 개발되었기 때문에 사용자가 전자정부 프레임워크 템플릿 Code Gen의 플러그인을 확장하여 다양한 템플릿을 작성할 수 있고, 프로젝트에서 이를 활용할 수 있다.

## 설명

전자정부 프레임워크에서 제공하는 템플릿 Code Gen은 기본적으로 Velocity Template Engine을 사용한다. 사용자 정의 템플릿을 추가하기 위해서는 다음과 같은 구성요소가 필요하다.

* Template : 사용자는 Velocity Template 문법에 따라 Template을 제작한다.
* Wizard XML File : Wizard 화면 UI를 생성하기 위한 XML 파일이다.
* Wizard 목록 XML File : Template의 목록 정보 XML 파일이다.
* 플러그인 프로젝트 : 전자정부 프레임워크 템플릿 Code Gen.의 확장점을 이용하여 작성하며, 주요구성요소는 Template, Wizard XML, Wizard 목록 XML이다.
* 피처, 업데이트 사이트 프로젝트 : 위의 플러그인 프로젝트를 하나의 단위로 묶어 업데이트할 수 있도록 돕는다.

### 템플릿 작성 방법

Velocity Template 기본 작성방법은 다음 사이트를 참조한다.

[https://velocity.apache.org/](https://velocity.apache.org/)

### Wizard 생성 방법

Wizard는 XML 문법에 따라 작성하며 사용법은 다음과 같다.

#### Wizard의 구성

사용자 정의 템플릿 마법사 페이지는 model-page와 component-page가 있으며, 하나 이상의 페이지를 생성 또는 추가할 수 있다.

* model-page : 데이터베이스 테이블 선택 페이지
* component-page : 각각의 입력항목을 통하여 필요한 정보를 입력받는 페이지.
* output : 템플릿 파일 매핑 정보를 기술

#### 모델 페이지의 생성

```xml
<model-page type="table" required="true">
    <!-- SelectSomeTable 테이블 선택 -->
    <description>Select some Table</description>
</model-page>
```

#### 컴포넌트 페이지의 생성 예시

```xml
<component-page>
    <description>Input resource information</description>
    <group label="" required="true">
        <textfield name="author" label="Author :" required="true" value="" />
        <container name="voPackage" label="VO Package: " required="true" type="package" />
    </group>
</component-page>
```

(설명)

* component-page : 생성되는 위저드 페이지 수만큼 하나 이상의 `<component-page>` XML Code를 작성한다.
* label : 위저드 화면에 보여지는 제목
* name : 내부적으로 사용되는 컴포넌트명
* required : 필수 입력값 여부 (true|false)
* value : default 값을 선언할 때 사용한다.

#### UI 입력 컴포넌트 생성 및 추가

group : 하나 이상의 UI 컴포넌트를 그룹화한다.

```xml
<group name="" label="" checkbox="" >
    ...
</group>
```

(설명)

* label : 위저드 화면에 보여지는 제목
* checkbox : 그룹내 컴포넌트 항목들에 대한 checkbox 옵션을 적용한다.

Container : 패키지 또는 폴더를 선택하기 위한 것이다.

```xml
<container name="actionPackage"
           label="Package:"
           required="true"
           type="package|folder"
           value="" />
```

(type 설명)

* package : 현재 프로젝트의 자바 패키지 목록을 선택할 수 있는 기능을 제공한다.
* folder : 현재 프로젝트의 리소스 폴더를 선택할 수 있는 기능을 제공한다.

textField : 텍스트 입력박스

```xml
<textfield name=""
           label=""
           required="true/false"
           extension="" />
```

checkbox :

```xml
<checkbox name="createValidation"
          label="Create the Action-validation.xml ?"
          value="false" />
```

radio :

```xml
<combo name="radio" label="View:" value="FreeMarker">
    <elements>
        <option value="freemarker">FreeMarker</option>
        <option value="velocity">Velocity</option>
        <option value="dispatcher">JSP</option>
        <option value="xslt">XSLT</option>
    </elements>
</combo>
```

combo :

```xml
<combo name="radio" label="View:" value="FreeMarker">
    <elements>
        <option value="freemarker">FreeMarker</option>
        <option value="velocity">Velocity</option>
        <option value="dispatcher">JSP</option>
        <option value="xslt">XSLT</option>
    </elements>
</combo>
```

#### Output 작성 예시

코드 생성을 하기 위해서는 위저드에서 입력받은 내용을 어떤 템플릿 파일과 매핑시켜서 코드를 생성할 것인지 `<output>`에 지정해주어야 한다.

```xml
<output>
    <template component="txtFileName" velocity="sequenceId.vm"
        extension="xml" container="txtPath">
    </template>
    <condition variable="checkService" value="true" />
</output>
```

(설명)

* template : 생성되는 파일의 수만큼 하나 이상의 `<template>` XML Code를 작성한다.
* component : 파일이름을 입력받은 컴포넌트명
* velocity : 코드 생성에 사용할 velocity template을 지정한다.
* extension : 파일 기본 확장자를 지정한다.
* container : 파일이 저장될 경로를 입력한다.
* condition : 조건을 적용하여 코드 생성 여부를 결정할 때 사용한다. (variable : 조건에 사용할 컴포넌트명, value = 컴포넌트가 이 값과 동일할 경우 코드를 생성한다.)

### 위저드/템플릿에서 데이터베이스 테이블 정보를 사용하는 방법

데이터베이스 테이블을 선택하여 코드를 생성할 때 해당 테이블 정보를 활용하는 방법은 다음과 같다.

* `${model.vender}` : 테이블의 데이터베이스 벤더 정보
* `${model.entity.name}` : 테이블명
* `${model.entity.pcName}` : 테이블명을 파스칼 방식을 따라 변환한다. (EGOV_SAMPLE → EgovSample)
* `${model.entity.ccName}` : 테이블명을 Camel 방식을 따라 변환한다. (EGOV_SAMPLE → egovSample)
* `${model.entity.ucName}` : 테이블명을 모두 대문자로 변환한다.
* `${model.entity.lcName}` : 테이블명을 모두 소문자로 변환한다.
* `${model.attributes}` : 테이블 내에 있는 컬럼 목록
* `${model.primaryKeys}` : 테이블 내에 있는 Primary Key 목록
* `${model.attributes.get(0)}` : 테이블의 첫번째 컬럼
* `${model.attributes.get(0).name}` : 테이블의 첫번째 컬럼의 컬럼명 가져올 때
* `${model.attributes.get(0).javaType}` : 테이블의 첫번째 컬럼의 자바 타입 가져올 때

#### 테이블 명칭을 이용한 파일 생성 예시

파일을 생성할 테이블 정보를 활용할 수 있고, 예시는 다음과 같다.

```xml
<output>
    <template component="dao" expression="${model.entity.pcName}DAO"
        velocity="java/pkg/service/impl/Sample2DAO.vm" extension="java"
        container="daoPackage">
        <condition variable="checkDataAccess" value="true" />
    </template>
</output>
```

#### 템플릿에서 테이블 및 컬럼 정보를 이용한 데이터베이스 쿼리 생성 예시

```velocity
SELECT
#set($i=0)
#foreach($attribute in $model.attributes)
#if($i == 0)
    ${attribute.name}
#else
    , ${attribute.name}
#end
#set($i=$i+1)
#end
    FROM ${model.entity.name}
    ORDER BY
#set($i=0)
#foreach($attribute in $model.primaryKeys)
#if($i == 0)
    ${attribute.name} DESC
#else
    , ${attribute.name} DESC
#end
#set($i=$i+1)
#end
```

#### 템플릿에서 데이터베이스 벤더 정보를 이용한 다른 쿼리문 생성 예시

```velocity
#set($vender="$model.vender")
#if($vender == "HSQLDB")
.....
#elseif($vender == "Oracle")
.....
#end
```

### Wizard 목록 작성 방법

Category 별로 작성한 wizard 목록을 기술하며, template 경로는 wizard 목록 xml 파일의 상대경로를 기술하면 된다.

예시

```xml
<?xml version="1.0" encoding="UTF-8"?>
<templates>
    <category name="CRUD">
        <wizards>
            <wizard-def description="CRUD Program" template="crud/wizard.xml"/>
        </wizards>
    </category>
</templates>
```

### 사용자 템플릿 플러그인 프로젝트 제작 방법

1. 개발환경에서 플러그인 프로젝트를 생성하고, 위 설명을 참조하여 Template과 Wizard, Wizard 목록 파일을 생성한다.
2. MANIFEST.MF를 Plug-in Manifest Editor로 열고, Extensions 탭을 클릭한다.
3. Add… 버튼을 클릭하고, `egovframework.dev.imp.codegen.template.templateWizards`를 더블클릭하여 Extensions에 추가한다.
4. Extensions 세부 항목을 입력한다. 임의의 ID와 이름, 마법사 목록 XML 경로를 입력한다.

수정된 plugin.xml의 내용:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.4"?>
<plugin>
   <extension
         point="egovframework.dev.imp.codegen.template.templateWizards">
      <wizards
            id="CustomTemplates.wizards"
            name="Custom Templates"
            wizardsFile="templates/wizards.xml">
      </wizards>
   </extension>
</plugin>
```

5. Feature와 update site 프로젝트를 만들고 제작한 템플릿 플러그인을 패키징한다.
6. 제작한 템플릿 플러그인을 개발환경에 업데이트한다. (Help > Software Updates > Add Site… > "업데이트 사이트 주소 또는 파일 선택")
7. Template 목록 조회 : **Window** > **Show View** > **eGovFrame Templates**를 선택한다.
8. 사용자 정의 템플릿이 추가되어 정상작동하는 것을 확인한다.

## 사용법

사용자 정의 템플릿 예제 - 아래 소스는 사용자 템플릿 예제 프로젝트이다.

매뉴얼을 참조하셔서 원하는 템플릿을 추가 또는 수정하셔서 사용하시면 됩니다.

### 사용자정의 템플릿 프로젝트 소스

* 파일 다운로드 : [CustomTemplateSample.zip](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:dev2:imp:codegen:template:customtemplatesample.zip) (사용자정의 템플릿 소스)

(파일 설명)

사용자 정의 샘플 프로젝트는 다음의 3개 프로젝트로 구성되어 있다.

* CustomTemplates : 사용자 정의 템플릿 프로젝트
* CustomTemplates.feature : 사용자 정의 템플릿 피처 프로젝트
* CustomTemplates.update : 사용자 정의 템플릿 업데이트 사이트 프로젝트

실제 사용자정의 템플릿은 CustomTemplates 프로젝트 내에 있고, feature 프로젝트와 update site 프로젝트는 CustomTemplates 플러그인을 하나의 단위 플러그인으로 묶고 로딩하여 업데이트할 수 있도록 하기 위한 것이다.

### 사용자정의 템플릿 업데이트 파일

* 파일 다운로드 : [CustomTemplate.update.zip](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:dev2:imp:codegen:template:customtemplates.update.zip) (사용자정의 템플릿 업데이트 파일)

(파일 설명)

위의 파일은 사용자정의 템플릿을 업데이트할 수 있도록 최종적으로 빌드한 업데이트 예제 파일이다. 사용법은 다음과 같다.

1. 위의 파일을 다운로드받은 후 개발환경 메뉴에서 **Help** > **Software Updates**를 선택한다.
2. Available Software 탭에서 우측 중앙에 있는 **Add Site…** 버튼을 클릭한다.
3. "Add Site" 팝업 화면에서 우측에 있는 **Archive…** 버튼을 클릭한다.
4. 다운로드 받은 파일을 선택하고, **OK** 버튼을 클릭한다.
5. Available Software 목록에 추가된 "Custom Template"을 선택하고, **Install** 버튼을 클릭한다.
6. Install이 완료되면 안내에 따라 플러그인을 재시작하고, Template 목록 조회을 조회하여 사용자 템플릿이 추가된 것을 확인한다.

### 사용자 정의 템플릿 추가에 대한 사용자 팁

사용자 정의 템플릿을 추가하기를 원하지만, 플러그인 프로젝트에 익숙하지 않는 경우 다음과 같은 방법으로 사용자 정의 템플릿을 추가할 수 있다.

1. 사용하고자 하는 Velocity Template과 Wizard 파일을 작성한다.
2. plugin 폴더에 해당 파일을 저장한다.
   * 저장위치 : `\plugins\egovframework.dev.imp.codegen.template.templates_<버전정보>\eGovFrameTemplates\`
3. wizards.xml (Wizard 목록 파일)을 편집하여 사용자 정의 템플릿에 대한 내용을 추가한다. (수정방법은 위의 템플릿 목록 XML 설명 참조)
4. Template 목록 조회 : 개발환경에서 **Window** > **Show View** > **eGovFrame Templates**를 선택한다.
5. 사용자 정의 템플릿이 추가되어 정상작동하는 것을 확인한다.
6. 단, 버전이 업데이트될 때에는 파일이 초기화되므로, 재작업을 해야 한다.