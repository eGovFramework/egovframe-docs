---
title: "공통분류코드"
linkTitle: "공통분류코드"
description: "공통분류코드"
url: /common-component/system-management/common-code-manage/common-class-code/
menu:
  depth:
    name: "공통분류코드"
    weight: 1
    parent: "common-code-manage"
---

# 공통분류코드

## 개요

공통분류코드는 공통코드관리에서 코드 체계를 구분하기 위한 상위 분류 정보를 관리하는
기능이다. 여러 업무 기능에서 사용하는 코드를 성격이나 업무 영역에 따라 묶을 때 기준으로
사용된다.

공통분류코드는 공통코드와 공통상세코드를 관리하기 위한 기준 정보이므로, 코드 체계를
구성할 때 먼저 정의한다. 공통코드와 공통상세코드는 공통분류코드에 연결되어 관리된다.

## 관리 대상

공통분류코드는 코드 체계의 최상위 구분 정보를 관리한다. 분류를 식별하고 설명하는
정보를 기준으로 코드 그룹을 구성한다.

공통분류코드를 등록한 후에는 해당 분류에 속하는 공통코드를 등록하고, 공통코드 아래에
공통상세코드를 등록하여 실제 업무 화면이나 기능에서 사용할 코드 값을 구성한다.

## 관련 구조

공통분류코드는 공통코드관리 영역의 하위 기능 중 하나이며, 공통코드와 공통상세코드보다
상위 단계의 분류 정보를 담당한다.

공통컴포넌트 테이블 구성 정보에서는 공통분류코드와 관련된 테이블로
`COMTCCMMNCLCODE`를 제공한다. 공통코드와 공통상세코드는 각각 `COMTCCMMNCODE`,
`COMTCCMMNDETAILCODE` 테이블과 연결된다.

## 관련 문서

- [공통코드관리](./common-code-manage.md)
- [공통코드](./common-code.md)
- [공통상세코드](./common-detail-code.md)
- [공통컴포넌트 배포 파일의 구성](../intro/deployment-structure.md)
- [공통컴포넌트 테이블 구성 정보](../intro/table-structure.md)

## 참고자료

- [eGovFramework/egovframe-docs - 공통컴포넌트 배포 파일의 구성](https://github.com/eGovFramework/egovframe-docs/blob/main/common-component/intro/deployment-structure.md)
- [eGovFramework/egovframe-docs - 공통컴포넌트 테이블 구성 정보](https://github.com/eGovFramework/egovframe-docs/blob/main/common-component/intro/table-structure.md)
