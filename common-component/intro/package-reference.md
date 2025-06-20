---
title: "패키지 간 참조 관계"
linkTitle: "패키지 참조"
description: "공통컴포넌트 간의 의존성 관계에 대해 설명합니다."
url: /common-component/common-intro/package-reference/
menu:
  depth:
    name: "패키지 간 참조 관계"
    weight: 5
    parent: "common-intro"
    identifier: "package-reference"
---

# 패키지 간 참조 관계

## 개요

컴포넌트를 구성하는 패키지 간의 참조관계를 아래 그림과 같이 도식화하였다. 경량화를 통해 상호 참조관계 및 이행 참조를 통한 순환 참조 관계를 모두 제거하였음을 도식적으로 확인할 수 있다. 함수적 참조관계와 UI 또는 업무적 참조관계를 구분하여 참조관계의 종류를 파악할 수 있도록 하였다. 전체 패키지를 함께 표현하는 것은 판독성이 떨어지므로 컴포넌트 분류 단위별로 표현하였다. 패키지에 부여된 색을 통해 서로 다른 분류에 속하는 패키지들을 구분하도록 구성하였다.

> **참고**: 아래 그림의 유효 공통컴포넌트는 [공통컴포넌트 배포 파일의 구성](/common-component/intro/deployment-structure.md) 내역의 공통컴포넌트 및 패키지를 참조하시기 바랍니다.

## 주요 특징

### 경량화된 참조 구조
- **순환 참조 제거**: 상호 참조관계 및 이행 참조를 통한 순환 참조 관계를 모두 제거
- **명확한 의존성**: 함수적 참조관계와 UI 또는 업무적 참조관계를 구분하여 표현
- **분류별 구성**: 컴포넌트 분류 단위별로 표현하여 판독성 향상

### 참조 관계 유형
- **함수적 참조**: 기능적으로 필요한 의존성 관계
- **UI 참조**: 사용자 인터페이스 관련 의존성
- **업무적 참조**: 비즈니스 로직 관련 의존성

## 컴포넌트별 참조 관계

### 사용자디렉토리/통합인증

사용자디렉토리/통합인증 컴포넌트는 시스템의 기본 인증 및 사용자 관리 기능을 제공한다.
![사용자디렉토리/통합인증 참조 관계](./images/user-auth-dependency.jpg)

### 보안

보안 컴포넌트는 시스템의 권한 관리 및 보안 정책을 담당한다.
![보안 참조 관계](./images/security-dependency.jpg)


### 통계/리포팅

통계/리포팅 컴포넌트는 시스템 사용 현황 및 각종 통계 정보를 제공한다.
![통계/리포팅 참조 관계](./images/statistics-dependency.jpg)


### 협업

협업 컴포넌트는 조직 내 협업을 지원하는 다양한 기능을 제공하며, 크게 두 그룹으로 나뉜다.

#### 게시판, 커뮤니티(동호회), 블로그
![협업 - 게시판/커뮤니티/블로그 참조 관계](./images/collaboration-board-dependency.jpg)


#### 일정관리, 문자메시지, 주소록 외
![협업 - 일정관리/문자메시지/주소록 참조 관계](./images/collaboration-schedule-dependency.jpg)


### 사용자지원

사용자지원 컴포넌트는 시스템 사용자를 위한 다양한 지원 기능을 제공한다.
![사용자지원 참조 관계 1](./images/user-support-dependency01.jpg)
![사용자지원 참조 관계 2](./images/user-support-dependency02.jpg)
![사용자지원 참조 관계 3](./images/user-support-dependency03.jpg)


### 시스템관리

시스템관리 컴포넌트는 시스템 운영 및 관리를 위한 기능을 제공한다.
![시스템관리 참조 관계 1](./images/system-management-dependency01.jpg)
![시스템관리 참조 관계 2](./images/system-management-dependency02.jpg)