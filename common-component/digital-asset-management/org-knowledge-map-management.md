---
title: "조직지식맵관리"
linkTitle: "조직지식맵관리"
description: "조직지식맵관리"
url: /common-component/digital-asset-management/knowledge-map/org-knowledge-map-management/
menu:
  depth:
    name: "조직지식맵관리"
    weight: 1
    parent: "knowledge-map"
---

## 개요

전사 조직도(본부-실-팀 등)를 기반으로 하여, 각 부서별로 어떤 지식 자산을 얼마나 보유하고 있는지 조직 단위로 지식을 매핑하고 탐색할 수 있도록 시각화하는 컴포넌트입니다.

## 주요 기능

* **조직 기반 지식 탐색**: 좌측의 조직도 트리를 클릭하면 해당 부서의 소속원들이 생산하고 등록한 지식 문서의 목록이 필터링되어 나타납니다.
* **부서별 지식 통계**: 각 조직별 지식 등록 건수, 평균 조회수, 우수 지식 보유 현황 등을 통계 내어 조직 간의 지식 공유 활동을 비교 분석합니다.

## 데이터 구조 (테이블)

* `COMTNORGNZTINFO` (조직 테이블) + `COMTNKNOWLEDGEINFO` (지식 테이블): 등록자의 소속 조직 ID를 기준으로 지식 데이터를 그루핑(Grouping)하여 뷰를 생성합니다.

## 활용 방안

인사 이동이 발생했을 때 전임자의 부서 지식을 후임자가 쉽게 승계받을 수 있으며, 조직 단위의 지식 마일리지 포상이나 성과 평가(KPI)에 활용하여 부서 차원의 지식 경영 참여를 독려합니다.
