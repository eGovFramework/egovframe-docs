---
title: "공통코드관리"
linkTitle: "공통코드관리"
description: "공통코드관리"
url: /common-component/system-management/common-code-manage/
menu:
  depth:
    weight: 1
    parent: "system-management"
    identifier: "common-code-manage"
---

# 공통코드관리

## 개요

공통코드관리는 시스템관리 영역에서 공통으로 사용하는 코드 정보를 관리하는 기능이다.
이 문서는 공통코드관리 하위 기능의 위치와 역할을 안내한다.

공통코드 관련 기능은 공통분류코드, 공통코드, 공통상세코드 문서로 나뉘어 제공된다.
각 문서에서는 코드 체계의 구성 단위별 관리 기능을 설명한다.

## 하위 기능

### 공통분류코드

공통분류코드는 코드 체계의 상위 분류를 관리하는 기능이다. 공통코드와 공통상세코드를
구분하기 위한 분류 기준을 정의한다.

### 공통코드

공통코드는 공통분류코드 아래에서 코드 그룹을 관리하는 기능이다. 업무 기능에서 사용할
코드 단위를 등록하고 관리한다.

### 공통상세코드

공통상세코드는 공통코드에 속한 상세 코드 값을 관리하는 기능이다. 화면 표시나 업무 처리
시 참조되는 세부 코드 정보를 등록하고 관리한다.

## 관련 기능

공통코드관리 영역에는 공통코드 체계 외에도 우편번호관리, 행정코드관리, 기관코드수신,
기관코드, 법정동코드, 도로명주소연계 문서가 함께 구성되어 있다. 각 기능의 상세 설명은
해당 하위 문서에서 확인한다.

## 관련 문서

- [공통분류코드](./common-class-code.md) — 공통분류코드는 공통코드관리에서 코드 체계를 구분하기 위한 상위 분류 정보를 관리하는 기능이다. 여러 업무 기능에서 사용하는 코드를 성격이나 업무 영역…
- [공통코드](./common-code.md) — 공통코드 관리는 공통코드를 등록, 수정, 목록조회, 상세조회를 제공한다.
- [공통상세코드](./common-detail-code.md) — 공통상세코드 관리는 공통상세코드를 등록, 수정, 목록조회, 상세조회를 제공한다.
- [우편번호관리](./zipcode-management.md) — 도로명주소 안내시스템(https://www.juso.go.kr/) 연계를 통해 우편번호와 주소를 관리하고 도로명 찾기 기능을 팝업창으로 제공하여 우편…
- [행정코드관리](./admin-code-management.md) — 행정코드 관리는 법정동, 행정동을 등록, 수정, 목록조회, 상세조회를 제공한다.
- [기관코드수신](./org-code-receive.md) — 기관코드수신은 EDI 모듈을 통하여 기관코드 및 법정동코드를 수신하여 운영시스템에 반영하고 연계내역을 관리한다.
- [기관코드](./org-code.md) — 기관코드수신은 기관코드의 변경정보를 시스템에서 주기적으로 수신 반영하고 변경사항을 관리하는 기능으로 구성되어 있다.
- [법정동코드](./legal-dong-code.md) — 법정동코드수신은 법정동코드의 변경정보를 시스템에서 주기적으로 수신 반영하고 변경사항을 관리하는 기능으로 구성되어 있다.
- [도로명주소연계](./road-name-address.md) — 도로명주소연계는 도로명주소 기반 우편번호 정보를 등록(엑셀 일괄 등록 포함)·조회·수정·삭제하는 기능이다. 소스는 공통코드관리(`egovframewo…
- [공통컴포넌트 배포 파일의 구성](../intro/deployment-structure.md)
- [공통컴포넌트 테이블 구성 정보](../intro/table-structure.md)

## 참고자료

- [eGovFramework/egovframe-docs - 공통컴포넌트 배포 파일의 구성](https://github.com/eGovFramework/egovframe-docs/blob/main/common-component/intro/deployment-structure.md)
- [eGovFramework/egovframe-docs - 공통컴포넌트 테이블 구성 정보](https://github.com/eGovFramework/egovframe-docs/blob/main/common-component/intro/table-structure.md)
