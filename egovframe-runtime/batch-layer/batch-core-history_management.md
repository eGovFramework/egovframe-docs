---
title: History Management
linkTitle: HistoryManagement
description: 배치작업 처리 중의 정보는 JobRepository의 JobInstance, JobParams, JobExecution, StepExecution, key-value 쌍으로 값을 보관할 수 있는 공간인 ExecutionContext에 저장 및 갱신되어 history를 관리한다.
url: /egovframe-runtime/batch-layer/batch-core-history_management/
menu:
    depth:
        name: History Management
        weight: 15
        parent: "batch-layer"
---
# History Management

## 개요

 배치작업 처리 중의 정보는 JobRepository의 JobInstance, JobParams, JobExecution, StepExecution, key-value 쌍으로 값을 보관할 수 있는 공간인 ExecutionContext에 저장 및 갱신되어 history를 관리한다.

## 설명

 JobInstance, JobParams, JobExecution, StepExecution, ExecutionContext 의 각각의 속성에 대해서 정리하였다.

### BATCH_JOB_INSTANCE

| JobInstance 속성 | 설명 |
| --- | --- |
| jobInstanceId | JobInstance를 식별하는 ID |
| version | JobInstance 의 수정 횟수 |
| jobName | Job의 이름 |
| jobKey | JobInstance를 구분 짓는 JobParameters의 serialization |

### BATCH_JOB_EXECUTION

| JobExecution 속성 | 설명 |
| --- | --- |
| status | BatchStatus는 실행 상태를 나타내는 객체이다, 실행하는 동안에는 BatchStatus,STARTED, 실행이 실패한 경우 BatchStatus.FAILED, 실행이 성공적으로 종료됐을 경우 BatchStatus.COMPLETED가 된다. |
| startTime | Execution이 시작되는 현재 시스템 시간을 java.Util.Data로 저장 |
| endTime | Execution의 성공/실패 여부와 관계없이 종료되는 현재 시스템 시간을 java.Util.Data로 저장 |
| exitStatus | ExitStatus는 실행의 결과를 나타낸다. 호출자에게 반환될 exit code를 포함한다. |
| createTime | JobExecution이 최초 생성 된 현재 시스템 시간을 java.Util.Data로 저장 |
| lastUpdated | JobExecution이 마지막으로 생성 된 현재 시스템 시간을 java.Util.Data로 저장 |
| executionContext | execution간 지속돼야 할 모든 데이터를 포함하는 '프로퍼티 백' |
| failureExceptions | Job이 실행되는 동안 발생한 익셉션 리스트 |

### BATCH_JOB_PARAMS

| JobParams 속성 | 설명 |
| --- | --- |
| jobInstanceId | BATCH\_JOB\_INSTANCE 테이블의 jobInstanceId를 외래키로 지정 |
| typeCd | 파라마터의 형식을 String으로 저장,null일 될 수 없음 |
| keyName | 파라미터의 키 |
| stringVal | String타입의 파마미터 값 |
| dateVal | Date타입의 파마미터 값 |
| longVal | Long타입의 파마미터 값 |
| doubleVal | Double타입의 파마미터의 값 |

### BATCH_STEP_EXECUTION

| StepExecution 속성 | 설명 |
| --- | --- |
| status | BatchStatus는 실행 상태를 나타내는 객체이다, 실행하는 동안에는 BatchStatus,STARTED, 실행이 실패한 경우 BatchStatus.FAILED, 실행이 성공적으로 종료됐을 경우 BatchStatus.COMPLETED가 된다. |
| startTime | Execution이 시작되는 현재 시스템 시간을 java.Util.Data로 저장 |
| endTime | Execution의 성공/실패 여부와 관계없이 종료되는 현재 시스템 시간을 java.Util.Data로 저장 |
| exitStatus | ExitStatus는 실행의 결과를 나타낸다. 호출자에게 반환될 exit code를 포함한다. |
| executionContext | execution간 지속돼야 할 모든 데이터를 포함하는 '프로퍼티 백' |
| readCount | 성공적으로 읽은 item 갯수 |
| writeCount | 성공적으로 쓰인 item 갯수 |
| commitCount | 해당 execution에서 커밋된 트랜젝션 횟수 |
| rollbackCount | 롤백된 Step에 의해서 제어된 비즈니스 트랜젝션의 갯수 |
| readSkipCount | 읽기 과정에서 실패 후, 스킵된 item 갯수 |
| processSkipCount | 프로세스 과정에서 실패 후, 스킵된 item 갯수 |
| filterCount | ItemProcessor에 의해 필터링 된 item 갯수 |
| writeSkipCount | 쓰기 과정에서 실패 후, 스킵된 item 갯수 |

### BATCH_JOB_EXECUTION_CONTEXT

| JobExecutionContext 속성 | 설명 |
| --- | --- |
| jobExecutionId | BATCH\_JOB\_EXECUTION 테이블의 jobExecutionId를 외래키로 지정 |
| shortContext | SERIALIZED\_CONTEXT의 문자열 버전 |
| serializedContext | 전체 Context |

### BATCH_STEP_EXECUTION_CONTEXT

| StepExecutionContext 속성 | 설명 |
| --- | --- |
| stepExecutionId | BATCH\_STEP\_EXECUTION 테이블의 stepExecutionId를 외래키로 지정 |
| shortContext | SERIALIZED\_CONTEXT의 문자열 버전 |
| serializedContext | 전체 Context |

## 참고자료

- Meta-Data Schema :[http://static.springsource.org/spring-batch/reference/html/metaDataSchema.html](http://static.springsource.org/spring-batch/reference/html/metaDataSchema.html)