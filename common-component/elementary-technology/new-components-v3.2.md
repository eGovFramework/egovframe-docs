---
title: "신규 컴포넌트(v3.2)"
linkTitle: "신규 컴포넌트(v3.2)"
description: "신규 컴포넌트(v3.2)"
url: /common-component/elementary-technology/new-components-v3.2/
menu:
  depth:
    weight: 1
    parent: "elementary-technology"
    identifier: "new-components-v3.2"
---

# 신규 컴포넌트(v3.2)

## 개요

표준프레임워크 3.2에서 추가된 요소기술 신규 컴포넌트 묶음이다. HTTP 요청 정보 취득, 자원(Resource) 해제 처리, 날짜 지역화, 로그 처리 등 개발 시 빈번히 필요한 기능을 제공한다.

## 관련 문서

- [Basic 로그](./basiclog.md) — JDK에서 제공하는 Logger 클래스를 이용하여 3가지 레벨로 로그를 남길 수 있는 기능을 제공한다.
- [HTTPS UrlRewrite filter](./urlrewrite.md) — 서버내의 특정 URL의 경우 HTTP로 호출 되더라도 HTTPS로 전환 하여 Redirect 하고, 그 외의 URL의 경우는 HTTP로 연결한다.
- [Http Request 정보 취득](./httprequesthelper.md) — Http Request(HttpServletRequest) 정보를 서비스 코드나 DAO 코드 상에서 취득할 수 있는 기능을 제공한다.
- [Resource close 처리](./resourceclose.md) — 자원(Stream, DB 관련 Object, Socket 관련 Object)에 대한 해제 처리 기능을 제공한다.
- [showModalDialog 대체 기능](./showmodaldialog.md) — JavaScript의 Modal 방식의 dialog를 지원하는 windows.showModalDialog의 기능이 chrome 37 버전부터 지원하지 않음에 따라 대체 기능을 제공한다.
- [날짜 지역화 처리](./dateformat.md) — 다국어 지원을 위한 국가간 날짜 표시 변환 기능을 제공한다.
- [숫자 지역화 처리](./numberformat.md) — 다국어 지원을 위한 국가간 숫자 표시 변환 기능을 제공한다.
- [이중등록(Double Submit) 방지](./doublesubmit.md) — 새로고침 등의 중복 request 호출 시 등록 처리 등에 대한 이중 등록을 방지하는 기능을 제공한다.
- [중복 로그인 방지 기능](./multilogin.md) — spring security 없이 중복 로그인을 방지하기 위한 기능이다.
- [출퇴근 관리](./cmtmanage.md) — **출퇴근 관리**는 출근, 퇴근 정보를 관리하는 기능을 제공한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
