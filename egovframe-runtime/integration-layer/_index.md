---
title: 연계통합
linkTitle: 연계통합
description: 연계통합 레이어는 타 시스템과의 연동기능을 지원한다.
url: /egovframe-runtime/integration-layer/
menu:
    depth:
        weight: 7
        parent: "egovframe-runtime"
        identifier: "integration-layer"
---
# 연계통합
연계통합 레이어는 타 시스템과의 연동기능을 지원한다.

## 개요

연계통합 계층은 표준프레임워크 기반 시스템이 타 시스템과 연계하기 위한 인터페이스 표준과 지원 기능을 제공한다. 연계 서비스 표준과 메타데이터 정의를 중심으로 WebService, RESTful, Naming 서비스, Cloud Data Stream 등 다양한 연계 방식을 지원한다.

## 주요 개념

Integration 서비스는 시스템 간 연계 인터페이스의 표준을 정의하며, 연계등록정보와 기관·시스템·서비스 등의 메타데이터를 기반으로 동작한다. 연계 방식은 WebService, RESTful(HTTP 메소드 기반), 메시징(Cloud Data Stream) 등으로 나뉘고, 자원의 등록·검색에는 JNDI 기반 Naming 서비스를 사용한다.

## 관련 문서

- [Integration 서비스](./integration-service.md) — 타 시스템 연계를 위한 인터페이스 표준 정의
- [Integration 서비스 Metadata](./integration-service-metadata.md) — 연계등록정보와 기관·시스템·서비스 메타데이터
- [연계 서비스 API](./integration-service-api.md) — 연계 서비스 사용·제공을 위한 인터페이스
- [WebService](./webservice.md) — Integration 표준에 따른 WebService 요청·제공 라이브러리
- [Restful](./restful.md) — Spring MVC 기반 REST 리소스 접근(PUT·GET·POST·DELETE)
- [Swagger](./swagger.md) — RESTful 서비스 문서화 자동 지원
- [Naming 서비스](./naming-service.md) — JNDI API 기반 자원 등록·검색
- [Cloud Data Stream](./cloud-data-stream.md) — Spring Cloud Stream 기반 이벤트 마이크로서비스 바인딩

## 참고자료

- [표준프레임워크 실행환경 소개](../intro/overview.md)
