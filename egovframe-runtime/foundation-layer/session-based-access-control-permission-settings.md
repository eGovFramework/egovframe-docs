---
title: Session 방식 접근제어 권한설정
linkTitle: "Session 방식 접근제어"
description: 표준프레임워크 3.9부터 Session 방식의 접근제어 권한관리를 설정할 수 있으며, 이를 위해 XML 선언 및 SQL 쿼리를 포함한 기본 설정이 필요하다. 롤 권한 변경 시 서버 재기동 없이 `AuthorityResourceMetadata`의 `reload()` 메소드를 호출하여 설정을 적용할 수 있다.
url: /egovframe-runtime/foundation-layer/session-based-access-control-permission-settings/
menu:
    depth:
        name: Session 방식 접근제어
        weight: 2
        parent: "foundation-layer"
---
# Session 방식 접근제어 권한설정

## 개요

표준프레임워크 3.9부터 Session 방식으로 접근제어 권한관리를 설정 할 수 있는 방법을 제공한다.
내부적으로 필요한 설정을 가지고 있고, XML Schema를 통해 필요한 설정만을 추가할 수 있도록 제공한다.
이 기능을 사용하기 위해서는 globals.properties 파일에서 Globals.Auth = session 로 설정한다.

## 환경설정

### pom.xml (dependency추가)

Session 방식의 접근제어 권한관리를 사용하기 위해서는 표준프레임워크 실행환경 구성요소중 org.egovframe.rte.fdl.access 라이브러리가 설치되어야 한다.

```xml
<dependency>
	<groupId>org.egovframe.rte</groupId>
	<artifactId>org.egovframe.rte.fdl.access</artifactId>
	<version>${org.egovframe.rte.version}</version>
</dependency>
```

### XML namespace 및 schema 설정

접근제어를 설정하기 위해서는 다음과 같은 xml 선언이 필요하다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:egov-access="http://maven.egovframe.go.kr/schema/egov-access"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://maven.egovframe.go.kr/schema/egov-access http://maven.egovframe.go.kr/schema/egov-access/egov-access-4.2.0.xsd">
```

## Session 접근제어 설정

Session 방식 접근제어 권한관리에 대한 기본 설정 정보를 제공한다.

```xml
<egov-access:config id="egovAccessConfig"
	globalAuthen="session"
	mappingPath="/**/*.do"
	dataSource="egov.dataSource"
	loginUrl="/uat/uia/egovLoginUsr.do"
	accessDeniedUrl="/uat/uia/egovLoginUsr.do?auth_error=1"
	sqlAuthorityUser="SELECT CONCAT(B.USER_SE, B.USER_ID) USERID, A.AUTHOR_CODE AUTHORITY
		FROM COMTNEMPLYRSCRTYESTBS A, COMVNUSERMASTER B
		WHERE A.SCRTY_DTRMN_TRGET_ID = B.ESNTL_ID"
	sqlRoleAndUrl="SELECT A.ROLE_PTTRN URL, B.AUTHOR_CODE AUTHORITY
		FROM COMTNROLEINFO A, COMTNAUTHORROLERELATE B
		WHERE A.ROLE_CODE = B.ROLE_CODE
		AND A.ROLE_TY = 'url'
		ORDER BY A.ROLE_SORT"
	requestMatcherType="regex"
	excludeList="/uat/uia/**, /index.do, /EgovLeft.do, /EgovContent.do, /EgovTop.do, /EgovBottom.do, /validator.do, /uss/umt/**, /sec/rnc/EgovRlnmCnfirm.do, /EgovModal.do"
/>
```

### 속성 설명

|    속성                    |     설명                                                                                                         |     필수여부      |     비고            |
|--------------------------|----------------------------------------------------------------------------------------------------------------|---------------|-------------------|
|    globalAuthen          |  globals.properties 설정과 동일하게 적용 (Globals.Auth = session 설정 사용시 globalAuthen = “session”으로 값을 동일하게 일치하여 설정 필요)  |   필수          |                   |
|    dataSource            |  DBMS 설정 dataSource                                                                                            |   필수          |                   |
|    loginUrl              |  로그인 페이지 URL                                                                                                   |   필수          |                   |
|    accessDeniedUrl       |  권한이 없는 경우 호출되는 페이지 URL                                                                                        |   필수          |                   |
|    sqlAuthorityUser      |  인증된 사용자의 권한(authority) 조회 query                                                                               |   필수          |                   |
|    sqlRoleAndUrl         |  Role 및 URL 패턴                                                                                                 |   필수          |                   |
|    requestMatcherType    |  패턴 매칭 방식(regex, ant, ciRegex: case-insensitive regex)                                                         |   필수          |  default : regex  |
|    excludeList           |  접근제한 예외처리 URL(구분자: ,)                                                                                         |   필수          |                   |

- excludeList(접근제한 예외 목록 URL) 예시 값
  - 회원관리 : /uat/uia/**
  - 실명확인 : /sec/rnc/**
  - 우편번호 : /sym/ccm/zip/**
  - 로그인이미지관리 : /uss/ion/lsi/**
  - 약관확인 : /uss/umt/**
  - 포털예제배너 : /uss/ion/bnr/getBannerImage.do
  - 처음화면 : /index.do
  - 로그인화면이미지 : /cmm/fms/getImage.do
  - 좌측메뉴 : /EgovLeft.do
  - 초기화면 : /EgovContent.do
  - 상단메뉴 : /EgovTop.do
  - 하단메뉴 : /EgovBottom.do
  - 모달팝업 : /EgovModal.do
  - 만족도조사 : /cop/stf/selectSatisfactionList.do
  - 만족도조사 선택 : /cop/stf/selectSingleSatisfaction.do
  - 댓글 : /cop/cmt/selectArticleCommentList.do
  - 댓글 선택 : /cop/cmt/updateArticleCommentView.do
- 동적 include 방식 - JSP 에서 `<c:import>` 혹은 `<jsp:include>` 사용시 호출대상 URL이 .do 인 경우
  - 호출대상.do 뿐만 아니라 .do URL이 호출하는 JSP파일도 권한관리에 등록해야 함

## Session 접근제어 재설정

Session 접근제어에서 사용자의 롤권한변경 후 서버 재기동 없이 적용하는 방법을 제공한다.

```java
import org.egovframe.rte.fdl.access.bean.AuthorityResourceMetadata;
 
@Resource(name="authorityResource")
private AuthorityResourceMetadata sessionResourceMetadata;
 
@RequestMapping(value="/insertAuthorGroupInsert.do")
public String insertAuthorGroup() {
...
    sessionResourceMetadata.reload();
...
}
```