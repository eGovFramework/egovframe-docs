---
title: "요소기술"
linkTitle: "요소기술"
description: "요소기술"
url: /common-component/elementary-technology/
menu:
  depth:
    weight: 10
    parent: "common-component"
    identifier: "elementary-technology"
---

# 요소기술

## 개요

요소기술 카테고리는 업무 화면을 갖는 서비스 컴포넌트가 아니라, 애플리케이션 전반에서 재사용되는 유틸리티성 공통 기능을 제공한다. 소스는 주로 `egovframework.com.utl.*`, `egovframework.com.cmm` 패키지에 위치한다.

## 주요 영역

- **문자열·숫자 처리** — 문자열 검색·변환·치환·유효성 체크, 숫자 검색·유효성, 특수문자 처리
- **날짜·시간 처리** — 날짜/시간/요일 계산·변환·포맷·유효성, 양음력 변환, 랜덤 날짜, 타임스탬프, 달력·휴일 관리
- **파일·디렉터리 처리** — 파일 생성·복사·이동·삭제·압축·비교·파싱·송수신·동기화, 업로드, 디렉터리 권한·이동
- **시스템 점검·모니터링** — 서버·시스템·네트워크 정보 확인, 프로세스·HTTP·DB서비스·파일시스템 모니터링, 메모리 점검
- **웹·기타** — 메인/트리 메뉴, 로그인 세션 체크, 쿠키/세션, 프로퍼티, XML 조립·파싱, 로그 패턴 점검

각 기능의 상세 내용은 좌측 메뉴의 개별 문서를 참조한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
