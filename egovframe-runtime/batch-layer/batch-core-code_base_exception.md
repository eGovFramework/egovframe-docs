---
title: Code Base Exception
linkTitle: CodeBaseException
description: 배치 처리 시 EgovBatchException을 통해 Code 기반으로 에러를 처리할 수 있으며, 이를 사용하려면 먼저 데이터베이스 에러 코드 관리 테이블과 에러 코드 데이터를 등록해야 한다. 이 서비스를 통해 에러 처리의 효율성을 높일 수 있다.
url: /egovframe-runtime/batch-layer/batch-core-code_base_exception/
menu:
    depth:
        name: CodeBaseException
        weight: 19
        parent: "batch-layer"
---
# Code Base Exception

## 개요

배치 처리시 Code 기반으로 에러를 처리 할 수 있도록 EgovBatchException를 통해서 지원한다.
데이터베이스 에러코드관리 테이블을 등록과 에러코드 데이터를 등록이 선행 되야지만 해당 서비스를 사용가능하다.

## 설명

### Code Base Exception 데이터베이스 설정

```bash
C REATE TABLE BATCH_EXCEPTION_MESSAGE  (
	EX_ID BIGINT NOT NULL PRIMARY KEY,
	EX_KEY VARCHAR(255) NOT NULL,
	EX_MESSAGE VARCHAR(2500) NOT NULL
);
I NSERT INTO BATCH_EXCEPTION_MESSAGE VALUES(1,'EGOVBATCH000001','배치실행 중 업무 관련 에러가 발생 하였습니다.');
I NSERT INTO BATCH_EXCEPTION_MESSAGE VALUES(2,'EGOVBATCH000002','배치실행 중 알수 없는 오류가 발생 하였습니다.');
```

- 방화벽 정책상 [C REATE] 문자를 space 처리 하였습니다. space 문자를 제거 하시면 됩니다.
- 방화벽 정책상 [I NSERT] 문자를 space 처리 하였습니다. space 문자를 제거 하시면 됩니다.
- 방화벽 정책상 [I NTO] 문자를 space 처리 하였습니다. space 문자를 제거 하시면 됩니다.

### Code Base Exception 사용

에러처리 생성자 생성자 파리미터 데이터베이스소스, 에러코드를 사용하여 에러처리를 할 수 있습니다.

```bash

try{
	...
}catch(Exception e){
	throw new EgovBatchException(dataSource,"EGOVBATCH000001");
        //Sql 설정시 EgovBatchException 생성자 파리미터 추가
        //throw new EgovBatchException(dataSource,"EGOVBATCH000001","SELECT EX_MESSAGE FROM BATCH_EXCEPTION_MESSAGE WHERE EX_KEY = ?");
}

```
