---
title: "에러애플리케이션"
linkTitle: "에러애플리케이션"
description: "에러애플리케이션"
url: /common-component/system-management/error-manage/error-application/
menu:
  depth:
    name: "에러애플리케이션"
    weight: 1
    parent: "error-manage"
---

## 개요

시스템 내의 여러 애플리케이션(모듈)이나 화면에서 에러가 발생했을 때, 해당 에러를 캐치(Catch)하고 중앙 집중적으로 로깅/기록할 수 있도록 인터페이스를 제공하는 컴포넌트입니다.

## 주요 기능

* **예외(Exception) 수집**: AOP(Aspect Oriented Programming)나 ControllerAdvice 등을 통해 발생하는 런타임 에러나 비즈니스 익셉션을 공통으로 낚아채어 수집합니다.
* **에러 로그 등록**: 에러가 발생한 클래스명, 메서드명, 에러 메시지(Stack Trace) 및 발생 시간을 에러 이력 테이블에 기록합니다.

## 데이터 구조 (테이블)

* `COMTNERRORINFO`: 에러 발생 시간, 시스템명, 발생 URL, 예외 클래스, 스택 트레이스 등을 기록하는 테이블 (에러결과관리와 공유)

## 활용 방안

사용자에게 "시스템 오류가 발생했습니다"라는 정제된 메시지를 보여주면서, 이면에서는 개발자가 오류를 분석할 수 있는 상세한 원천 데이터를 DB나 파일에 안정적으로 적재하는 데 사용됩니다.
