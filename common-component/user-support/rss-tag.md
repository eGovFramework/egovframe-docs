---
title: "RSS태그관리"
linkTitle: "RSS태그관리"
description: "RSS태그관리"
url: /common-component/user-support/information-provided/rss-tag/
menu:
  depth:
    name: "RSS태그관리"
    weight: 36
    parent: "information-provided"
---

## 개요

시스템 내의 게시판, 뉴스, 공지사항 등의 업데이트된 콘텐츠 정보를 RSS(Rich Site Summary) XML 피드 형식으로 생성하여 외부 사용자나 다른 시스템에 제공하는 컴포넌트입니다.

## 주요 기능

* **RSS 피드 생성**: 특정 게시판의 최신 글 목록을 표준 RSS 2.0 규칙에 맞는 XML 포맷으로 동적 생성합니다.
* **구독 URL 제공**: 사용자가 RSS 리더기를 통해 새 글 알림을 받을 수 있도록 고유한 RSS 접근 URL을 제공합니다.
* **대상 대상 관리**: RSS로 제공할 대상 게시판(게시물)의 범위와 항목 수를 관리자가 설정할 수 있습니다.

## 데이터 구조 (테이블)

(보통 게시판 마스터 테이블 `COMTNBBSMASTER` 및 게시물 테이블 `COMTNBBS`의 데이터를 실시간으로 읽어와 XML로 변환하므로 별도 저장 테이블은 필요하지 않습니다.)

## 활용 방안

자사 홈페이지의 주요 새소식을 블로그, 포털 사이트 검색엔진, 뉴스 피드 수집기 등에 빠르게 배포하고 노출시켜 웹 접근성 및 홍보 효과를 높이는 데 사용됩니다.
