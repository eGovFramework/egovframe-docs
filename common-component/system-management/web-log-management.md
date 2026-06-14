---
title: "웹로그관리"
linkTitle: "웹로그관리"
description: "웹로그관리"
url: /common-component/system-management/log-manage/web-log-management/
menu:
  depth:
    name: "웹로그관리"
    weight: 7
    parent: "log-manage"
---

## 개요

웹 서버 또는 WAS 앞단에서 발생하는 모든 HTTP Request(요청)에 대한 접근 URL, 요청자의 IP 주소, 요청 시간 등을 인터셉터나 필터를 통해 포괄적으로 로깅하는 컴포넌트입니다.

## 주요 기능

* **모든 웹 요청 기록**: 시스템에 들어오는 모든 페이지 요청에 대해 URL Path, 클라이언트 IP 등을 남깁니다.
* **비정상 접근 모니터링**: 짧은 시간에 과도한 요청이 들어오거나 인가되지 않은 비정상적인 URL 요청 패턴(예: 보안 스캔)을 파악하는 데 도움을 줍니다.

## 데이터 구조 (테이블)

* `COMTNWEBLOG`: HTTP 요청 일시, 요청 URL, 클라이언트 IP 주소, 브라우저 User-Agent 정보 등을 저장하는 테이블

## 활용 방안

`사용로그`가 비즈니스 기능(메뉴 단위) 중심의 분석이라면, `웹로그`는 인프라 및 트래픽 분석(Traffic Analysis)
관점에서 웹사이트 방문자 수 추이 산정, 페이지 뷰(PV) 분석, 공격 IP 차단을 위한 기초 자료로 사용됩니다.
