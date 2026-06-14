---
title: "공통코드"
linkTitle: "공통코드"
description: "공통코드"
url: /common-component/system-management/common-code-manage/common-code/
menu:
  depth:
    name: "공통코드"
    weight: 2
    parent: "common-code-manage"
---

## 개요

특정 `분류코드` 하위에 속하며, 실제 데이터를 담고 있는 `상세코드`들의 그룹 명칭(중분류) 역할을 하는 공통코드(Common Code) 마스터 정보를 관리하는 컴포넌트입니다.

## 주요 기능

* **공통코드 등록/수정**: 특정 데이터 항목 그룹(예: 'COM014: 성별', 'COM022: 회원상태')을 나타내는 마스터 코드를 생성하고 관리합니다.
* **분류코드 매핑**: 해당 공통코드가 속하는 상위 분류코드(Class Code)를 선택하여 계층 관계를 맺어줍니다.

## 데이터 구조 (테이블)

* `COMTNCCMMNCODE`: 상위 분류코드 ID, 공통코드 ID, 공통코드명, 설명, 사용 여부를 저장하는 테이블

## 활용 방안

각종 셀렉트 박스나 라디오 버튼에 매핑되는 하위 '상세코드'들을 묶는 컨테이너 역할을 하며, 애플리케이션 내에서 "성별 코드를 가져와라(COM014)"라고 호출할 때의 기준 식별자로 활용됩니다.
