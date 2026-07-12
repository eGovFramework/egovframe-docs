---
title: "도로명주소연계"
linkTitle: "도로명주소연계"
description: "도로명주소연계"
url: /common-component/system-management/common-code-manage/road-name-address/
menu:
  depth:
    name: "도로명주소연계"
    weight: 9
    parent: "common-code-manage"
---

# 도로명주소연계

## 개요

도로명주소연계는 도로명주소 기반 우편번호 정보를 등록(엑셀 일괄 등록 포함)·조회·수정·삭제하는 기능이다. 소스는 공통코드관리(`egovframework.com.sym.ccm.zip`) 패키지에 위치하며, 도로명주소 우편번호 데이터를 시스템에 적재해 주소 검색에 활용한다.

## 설명

### 관련소스

| 유형 | 대상소스명 | 비고 |
| --- | --- | --- |
| Controller | egovframework.com.sym.ccm.zip.web.EgovCcmZipManageController.java | EgovCcmZipManageController Class |
| Service | egovframework.com.sym.ccm.zip.service.EgovCcmRdnmadZipManageService.java | Service Interface |
| Service | egovframework.com.sym.ccm.zip.service.EgovCcmZipManageService.java | Service Interface |
| ServiceImpl | egovframework.com.sym.ccm.zip.service.impl.EgovCcmRdnmadZipServiceImpl.java |  |
| ServiceImpl | egovframework.com.sym.ccm.zip.service.impl.EgovCcmZipManageServiceImpl.java |  |
| VO | egovframework.com.sym.ccm.zip.service.ZipVO.java |  |
| Class | egovframework.com.sym.ccm.zip.service.Zip.java |  |
| Class | egovframework.com.sym.ccm.zip.service.impl.EgovCcmExcelRdnmadZipMapping.java |  |
| Class | egovframework.com.sym.ccm.zip.service.impl.EgovCcmExcelZipMapping.java |  |
| DAO | egovframework.com.sym.ccm.zip.service.impl.RdnmadZipDAO.java |  |
| DAO | egovframework.com.sym.ccm.zip.service.impl.ZipManageDAO.java |  |
| JSP | /WEB-INF/jsp/egovframework/com/sym/ccm/zip/EgovAdressPop.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/sym/ccm/zip/EgovCcmExcelZipRegist.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/sym/ccm/zip/EgovCcmZipDetail.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/sym/ccm/zip/EgovCcmZipList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/sym/ccm/zip/EgovCcmZipModify.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/sym/ccm/zip/EgovCcmZipRegist.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/sym/ccm/zip/EgovCcmZipSearchList.jsp |  |
| JSP | /WEB-INF/jsp/egovframework/com/sym/ccm/zip/EgovCcmZipSearchPopup.jsp |  |
| Query XML | resources/egovframework/mapper/com/sym/ccm/zip/EgovRdnmadZip_SQL_*.xml | DB별 Query XML |
| Query XML | resources/egovframework/mapper/com/sym/ccm/zip/EgovZipManage_SQL_*.xml | DB별 Query XML |

### 주요 메서드 (EgovCcmRdnmadZipManageService)

| 메서드 | 반환형 | 설명 |
| --- | --- | --- |
| `deleteZip(Zip)` | `void` | 우편번호에 관한 서비스 인터페이스 클래스를 정의한다 |
| `deleteAllZip()` | `void` | 우편번호 전체를 삭제한다. |
| `insertZip(Zip)` | `void` | 우편번호를 등록한다. |
| `insertExcelZip(InputStream)` | `void` | 우편번호 엑셀파일을 등록한다. |
| `selectZipDetail(Zip)` | `Zip` | 우편번호 상세항목을 조회한다. |
| `selectZipList(ZipVO)` | `List<EgovMap>` | 우편번호 목록을 조회한다. |
| `selectZipListTotCnt(ZipVO)` | `int` | 우편번호 총 개수를 조회한다. |
| `updateZip(Zip)` | `void` | 우편번호를 수정한다. |

## 참고자료

- [공통컴포넌트 소스 저장소 (egovframe-common-components)](https://github.com/eGovFramework/egovframe-common-components)
