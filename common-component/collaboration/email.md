---
title: "전자우편"
linkTitle: "전자우편"
description: "전자우편"
url: /common-component/collaboration/email/
menu:
  depth:
    weight: 5
    parent: "collaboration"
    identifier: "email"
---

# 전자우편

## 개요

전자우편 컴포넌트는 시스템에서 발송하는 전자우편(발송메일)을 등록하고, 발송 내역과 상세 내용을 관리할 수 있는 협업 서비스 컴포넌트이다. 첨부파일을 포함한 메일 발송을 지원한다.

## 주요 개념

발송할 메일을 등록(수신자·제목·본문·첨부파일)하면 발송메일 내역으로 관리되며, 발송 목록과 상세 내용을 조회할 수 있다. 멀티파트 메일(EgovMultiPartEmail)로 첨부파일이 포함된 메일 발송을 처리한다.

## 관련 문서

- [협업 카테고리 개요](./_index.md) — 협업 카테고리는 조직 구성원 간의 정보 공유와 의사소통을 지원하는 공통컴포넌트 모음이다. 게시판, 커뮤니티, 일정관리, 전자우편, 주소록/명함록, 전…

## 설명

### 패키지 구조

전자우편 컴포넌트의 소스는 `egovframework.com.cop.ems` 패키지에 위치한다.

### 관련 소스

| 유형 | 대상소스 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.cop.ems.web.EgovSndngMailRegistController.java | 발송메일 등록 컨트롤러 |
| Controller | egovframework.com.cop.ems.web.EgovSndngMailDtlsController.java | 발송메일 내역 컨트롤러 |
| Controller | egovframework.com.cop.ems.web.EgovSndngMailDetailController.java | 발송메일 상세 컨트롤러 |
| Service | egovframework.com.cop.ems.service.EgovSndngMailService.java | 메일 발송 서비스 인터페이스 |
| Service | egovframework.com.cop.ems.service.EgovSndngMailRegistService.java | 발송메일 등록 서비스 인터페이스 |
| Service | egovframework.com.cop.ems.service.EgovSndngMailDtlsService.java | 발송메일 내역 서비스 인터페이스 |
| Service | egovframework.com.cop.ems.service.EgovSndngMailDetailService.java | 발송메일 상세 서비스 인터페이스 |
| Model/VO | egovframework.com.cop.ems.service.SndngMail.java, SndngMailVO.java, AtchmnFileVO.java | 발송메일·첨부파일 모델 |
| 유틸 | egovframework.com.cop.ems.service.EgovMultiPartEmail.java | 첨부파일 포함 멀티파트 메일 처리 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/ems/EgovMailRegist.jsp 외 | 메일 등록·내역·상세 화면 |
| Query XML | resources/egovframework/mapper/com/cop/ems/EgovSndngMailDetail_SQL_*.xml 외 | DB별 Query XML |

### 패키지 참조 관계

전자우편 패키지는 요소기술의 공통 패키지(cmm)에 대해서 직접적인 함수적 참조 관계를 가지며, 배포 시 패키지 간 참조 관계에 따라 관련 패키지와 함께 구성한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
