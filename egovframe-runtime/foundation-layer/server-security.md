---
title: Server Security
linkTitle: Server Security
description: Server Security Service는 Spring Security를 확장하여 사용자 인증과 권한 관리를 DB 기반으로 처리하며, 세션 관리도 지원한다. Spring Security는 인증, 권한 처리, 웹 및 서비스 레이어 보안을 제공하는 강력한 솔루션이지만 사용자 관리와 역할 관리에서 일부 취약점을 가진다. 표준프레임워크 3.0에서는 설정 간소화 기능과 Map 기반 UserDetails로 손쉬운 사용자 정보 관리가 가능해졌으며, 업그레이드 가이드를 통해 최신 보안 기능을 적용할 수 있다.
url: /egovframe-runtime/foundation-layer/server-security/
menu:
    depth:
        name: Server Security
        weight: 1
        parent: "foundation-layer"
        identifier: "serverSecurity"
---
# Server Security Service

## 개요

 웹을 통해 데이터를 주고받는 업무를 진행할 경우, 보안상의 문제가 발생하기 쉽다.  
Security Service는 웹을 통한 서비스 이용 시 발생할 수 있는 다양한 보안상의 취약점들을 사전에 인지하고 대응함으로써, 서비스의 안정성을 확보한다.  
Security Service는 사용자 정보를 DB에서 관리하여 인증을 거쳐야만 접근할 수 있는 **Authentication**과 사용자 권한 정보를 계층화시켜서 화면 및 페이지, 또는 메소드에 접근할 수 있는 **Authorization**이 포함된다.  

## 설명

 Server Security Service는 Spring Framework의 Spring Security를 확장하여 구현하였으며, 사용자 인증정보 및 권한정보를 DB에서 관리하고, Spring Security의 UserDetails 인터페이스를 확장하여 세션정보를 담을 수 있다.  
Server Security의 주요기능은 다음과 같다.

- 자원(url, method 등) 접근 제한
- 사용자 인증 확인
- 미인증시 인증확인 요청
- 계층적 권한 설정 및 사용자 권한 확인

### Spring Security 강점

- Spring Security 는 엔터프라이즈 어플리케이션을 위한 인증(Authentication), 권한 처리(Authorization) 서비스를 제공하는 강력하고 유연한 보안 솔루션이다.
- Servlet Filter 와 Java AOP 를 통하여 보안을 강제하며 Spring의 IoC 의 lifecycle 기반으로 동작한다.
- authentication, Web URL authorization, Method 호출 authorization, 도메인 객체 기반의 security 처리, 채널 보안(https 강제) 등의 주요 기능을 제공한다.
- Web request 보안에 더하여 Service Layer 및 인스턴스 수준의 보안 제공으로 Layering issue 해결 및 웹 클라이언트 외의 다양한 rich 클라이언트/웹서비스에 대한 보안 제어를 지원한다.
- 재사용성, 이식성, 코드 품질, 레퍼런스 (정부,은행,대학,기업 등 많은 business field), 다양한 타 프레임워크를 지원하며 community가 활성화 되어있다.

### Spring Security 기능 취약 부분

- 사용자관리 기능
- 역할 관리 기능
- XML 기반(설정 어려움)의 권한 체크

### SI 프로젝트의 보안.인증/권한처리의 일반적인 요구사항

- RDB 기반의 인증 또는 상용 SSO 연계
- 사용자 정보의 쉽고 빠른 참조를 위한 session 사용
- 부서, 사용자 및 메뉴/화면/권한 관리 - 개발자가 아닌 최종 사용자가 GUI 기반 관리 기능을 통해 작업하기를 원함
- 계층 구조의 부서관리, 사용자 관리, 권한 복제, 권한 상속, 프로젝트 업무 규모에 따른 방대한 사용자/역할 데이터의 관리 필요
- Portal solution / X-internet 도입 등 - 사용자관리/메뉴-권한 처리에 대한 유연한 통합(integration) 필요
- 부서/사용자/메뉴/화면/권한처리 등 각 프로젝트별 요구사항이 유사하면서도 달라 중복개발의 위험성 - 일반 업무보다 난이도가 높은 공통 업무 성격. 표준화, 손쉬운 customizing, 유연한 확장이 필요

### 기대효과

- 전자정부개발프레임워크의 Server Security에서 Spring Security 강점과 SI 프로젝트 활용성을 두루 갖춘 유연하고 강력한 Security 프레임워크를 확보할 수 있다.

### 표준프레임워크 3.0 변경사항

- 설정간소화 기능(XML Schema 기반)을 통하여 기존 복잡한 설정을 단순화할 수 있다.
- Map 기반의 UserDetails 사용을 통해 손쉬운 사용자정보 관리가 가능하다.

### Server Security

- [architecture](./server-security-architecture.md/)
- [Authentication](./server-security-authentication.md/)
- [Authorization](./server-security-authorization.md/)
- [설정 간소화](./server-security-simplifying-settings.md/)

### Server Security 업그레이드 가이드

- [업그레이드](./server-security-upgrade.md/)

## 참고자료

- [Spring Framework-Spring Security](https://spring.io/projects/spring-security)
- [Spring Framework-Spring Security Reference Documentation](https://docs.spring.io/spring-security/reference/5.8/index.html)