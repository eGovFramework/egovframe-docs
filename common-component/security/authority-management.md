---
title: 권한관리
linkTitle: 권한관리
description: "시스템 구축시 스프링의 보안 메카니즘을 적용하기 위해 Spring Security 에서 관리하는 권한(Authority)을 정의하는 컴포넌트이다"
url: /common-component/security/authority-management/
menu:
  depth:
    weight: 1
    parent: "security"
    identifier: "authority-management"
---



# 권한관리

## 개요

 시스템 구축시 스프링의 보안 메카니즘을 적용하기 위해 Spring Security 에서 관리하는 **권한(Authority)** 을 정의하는 컴포넌트이다. 당 컴포넌트를 이용하여 담당자는 시스템 사용자에게 부여하는 권한을 정의하여 관리할 수 있다. 표준프레임워크 3.9부터는 **Session 방식 권한처리** 기능을 추가하여 Spring Security 를 사용하지 않고도 당 컴포넌트를 이용하여 접근제어가 가능하도록 하였다.

## 설명

 **권한관리**는 사용자별 권한을 관리하기 위한 목적으로 **등록**, **수정**, **삭제**, **조회**, **목록조회**의 기능을 수반한다.

```bash
  ① 권한등록 : 시스템 담당자는 시스템 사용자에게 권한을 부여하기 위한 정의한 권한정보를 등록한다.
  ② 권한수정 : 시스템 담당자는 시스템 사용자에게 권한을 부여하기 위한 정의한 권한정보를 수정한다.
  ③ 권한삭제 : 시스템 담당자는 시스템 사용자에게 권한을 부여하기 위한 정의한 권한정보를 삭제한다.
  ④ 권한조회 : 시스템 담당자는 시스템 사용자에게 권한을 부여하기 위한 정의한 권한정보를 조회한다.
  ⑤ 권한목록 : 시스템 담당자는 시스템 사용자에게 권한을 부여하기 위한 정의한 권한정보 목록을 조회한다.
```

### 환경설정

#### 권한 기본 설정

##### * 스프링에서 제공하는 기본 권한(Authority)

| AUTHORITI | DESCRIPTION |
| --- | --- |
| ROLE\_ANONYMOUS | 모든 사용자 |
| IS\_AUTHENTICATED\_ANONYMOUSLY | 익명 사용자 |
| IS\_AUTHENTICATED\_FULLY | 인증된 사용자 |
| IS\_AUTHENTICATED\_REMEMBERED | REMEMBERED 사용자 |
| ROLE\_RESTRICTED | 제한된 사용자 |
| ROLE\_USER | 일반 사용자 |
| ROLE\_ADMIN | 관리자 |

#### 권한 추가 설정

##### * 업무적으로 필요에 의해 추가한 권한(Authority)

| AUTHORITI | DESCRIPTION |
| --- | --- |
| ROLE\_SYM | 시스템 업무 담당자 |
| ROLE\_COP | 협업 담당자 |
| ROLE\_USS | 사용자지원 담당자 |
| ROLE\_USER\_MANAGER | 업무사용자 관리자 |
| ROLE\_SEC | 보안 업무 담당자 |
| ROLE\_ENTRPRSMBER\_MANAGER | 기업회원 관리자 |
| ROLE\_MBER\_MANAGER | 일반회원 관리자 |

#### 권한(롤) 상속구조 정의(ROLES_HIERARCHY)

##### * 정의된 하위 권한의 롤을 상속하기 위해 COMTNROLES_HIERARCHY Table에 상속구조를 정의한다.

 ROLE\_ANONYMOUS → IS\_AUTHENTICATED\_ANONYMOUSLY → IS\_AUTHENTICATED\_FULLY → IS\_AUTHENTICATED\_REMEMBERED → ROLE\_USER → ROLE\_ADMIN

##### * 기초 데이터 생성

 권한관련 기초데이터를 먼저 생성한다.

- [기초데이터 생성](https://www.egovframe.go.kr/wiki/lib/exe/fetch.php?media=egovframework:com:v3.6:sec:basic_data.zip)

##### * 추가적으로 설정하는 권한은 기존에 정의된 권한 사이에 삽입한다.

- 상위 권한 정의

```sql
INSERT INTO COMTNROLES_HIERARCHY (PARENT_ROLE, CHILD_ROLE) VALUES('ROLE_COP','ROLE_ADMIN');
```

- 하위 권한 정의

```sql
INSERT INTO COMTNROLES_HIERARCHY (PARENT_ROLE, CHILD_ROLE) VALUES('ROLE_RESTRICTED','ROLE_COP');
```

- 권한의 HIERARCHY 구조

```sql
SELECT A.CHILD_ROLE CHILD, 
       A.PARENT_ROLE PARENT
  FROM COMTNROLES_HIERARCHY A LEFT JOIN COMTNROLES_HIERARCHY B ON (A.CHILD_ROLE = B.PARENT_ROLE);
```

### Spring Security Configuration

- [Spring Security](/egovframe-runtime/foundation-layer/server-security-architecture.md)

### Session 방식 접근제어 Configuration

- [Session 방식 접근제어 권한설정](/egovframe-runtime/foundation-layer/session-based-access-control-permission-settings.md)

## 관련기능

- [권한관리_기능](./authority-management-function.md)
- [권한별 롤관리](./authority-role-management.md)

## 참고자료

- [Server Security](/egovframe-runtime/foundation-layer/server-security.md)
