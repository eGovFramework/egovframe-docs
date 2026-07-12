---
title: "메일솔루션 연동 인터페이스"
linkTitle: "메일솔루션 연동 인터페이스"
description: "메일솔루션 연동 인터페이스"
url: /common-component/collaboration/email/mail-solution-interface/
menu:
  depth:
    name: "메일솔루션 연동 인터페이스"
    weight: 1
    parent: "email"
---

# 메일솔루션 연동 인터페이스

## 개요

메일솔루션 연동 인터페이스는 메일 솔루션과 연동하여 발송메일을 등록하고, 발송 요청을 XML 파일로 생성·전달하며, 발송결과 XML을 수신해 결과코드를 갱신하는 기능이다. 발송메일 내역·상세 조회와 첨부파일 관리도 제공한다. 본 기능은 전자정부 표준프레임워크 공통컴포넌트 협업(전자우편) 내에 구성되어 있다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.cop.ems.web.EgovSndngMailRegistController.java | 발송메일 등록 Controller Class |
| Controller | egovframework.com.cop.ems.web.EgovSndngMailDtlsController.java | 발송메일 내역 Controller Class |
| Controller | egovframework.com.cop.ems.web.EgovSndngMailDetailController.java | 발송메일 상세 Controller Class |
| Service | egovframework.com.cop.ems.service.EgovSndngMailService.java | 메일 발송(솔루션 연동) Service Interface |
| Service | egovframework.com.cop.ems.service.EgovSndngMailRegistService.java | 발송메일 등록·XML 생성 Service Interface |
| Service | egovframework.com.cop.ems.service.EgovSndngMailDtlsService.java | 발송메일 내역 Service Interface |
| Service | egovframework.com.cop.ems.service.EgovSndngMailDetailService.java | 발송메일 상세 Service Interface |
| ServiceImpl | egovframework.com.cop.ems.service.impl.EgovSndngMail*ServiceImpl.java | 각 Service 구현 Class |
| Util | egovframework.com.cop.ems.service.EgovMultiPartEmail.java | 첨부 포함 메일 발송 지원 Class |
| VO | egovframework.com.cop.ems.service.SndngMail.java / SndngMailVO.java / AtchmnFileVO.java | 발송메일·첨부파일 VO Class |
| DAO | egovframework.com.cop.ems.service.impl.SndngMailRegistDAO.java, SndngMailDtlsDAO.java, SndngMailDetailDAO.java | 발송메일 DAO Class |
| JSP | /WEB-INF/jsp/egovframework/com/cop/ems/EgovMailRegist.jsp | 발송메일 등록 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/ems/EgovMailDtls.jsp | 발송메일 내역 페이지 |
| JSP | /WEB-INF/jsp/egovframework/com/cop/ems/EgovMailDetail.jsp | 발송메일 상세 페이지 |
| Query XML | resources/egovframework/mapper/com/cop/ems/EgovSndngMailDtls_SQL_*.xml, EgovSndngMailDetail_SQL_*.xml | DB별 Query XML |

### 주요 메서드

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `EgovSndngMailService.sndngMail(SndngMailVO)` | `boolean` | 메일 솔루션과 연동하여 메일을 발송한다 |
| `EgovSndngMailRegistService.insertSndngMail(SndngMailVO)` | `boolean` | 발송메일을 등록하고 발송요청 XML 파일을 생성한다 |
| `EgovSndngMailRegistService.trnsmitXmlData(SndngMailVO)` | `boolean` | 발송할 메일을 XML 파일로 만들어 저장한다 |
| `EgovSndngMailRegistService.recptnXmlData(String)` | `boolean` | 발송결과 XML 파일을 읽어 발송결과코드를 수정한다 |
| `EgovSndngMailDtlsService.selectSndngMailList(ComDefaultVO)` | `List<SndngMailVO>` | 발송메일 내역을 조회한다 |
| `EgovSndngMailDtlsService.selectSndngMailListTotCnt(ComDefaultVO)` | `int` | 발송메일 총건수를 조회한다 |
| `EgovSndngMailDetailService.selectSndngMail(SndngMailVO)` | `SndngMailVO` | 발송메일을 상세 조회한다 |
| `EgovSndngMailDetailService.deleteSndngMail(SndngMailVO)` | `void` | 발송메일을 삭제한다 |
| `EgovSndngMailDetailService.deleteAtchmnFile(SndngMailVO)` | `void` | 첨부파일을 삭제한다 |

메일 발송에는 연동 대상 메일 솔루션(또는 SMTP 서버)에 대한 설정이 필요하다. 자세한 사용 방법은 [전자우편](./email.md) 문서를 참조한다.

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
