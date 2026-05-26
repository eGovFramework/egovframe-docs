---
title: 배치처리
linkTitle: 배치처리
description: 배치처리 서비스는 일괄처리 업무 구현에 필요한 기능을 제공한다. Spring Batch 5.2.3 기반의 Job, Step, ItemReader/Writer, 트랜잭션·재시작·병렬 처리 등 핵심 개념을 다룬다.
url: /egovframe-runtime/batch-layer/
menu:
    depth:
        name: 배치처리
        weight: 8
        parent: "egovframe-runtime"
        identifier: "batch-layer"
---
# 배치 실행환경

배치처리 서비스는 일괄처리 업무 구현에 필요한 기능을 제공한다. 전자정부 표준프레임워크 배치 실행환경은 **Spring Batch**를 기반으로 하며, 본 문서는 [Spring Batch 5.2 Reference](https://docs.spring.io/spring-batch/reference/5.2/index.html)(5.2.3 호환)를 참고하여 구성하였다.

## 문서 구성

- **배치 실행환경 소개**: 배치 개요, 사용 시나리오, 3-Tier(Run/Job/Application) 구조
- **도메인 언어**: Job, Step, JobInstance, JobParameters, JobExecution, StepExecution, ExecutionContext, JobRepository, JobLauncher, ItemReader, ItemWriter, ItemProcessor
- **Job 설정 및 실행**: Job 설정, JobRepository, JobLauncher, Job 실행
- **Step 설정**: Step 유형, Chunk 기반 처리, TaskletStep, 흐름 제어
- **Item 읽기/쓰기**: ItemReader, ItemWriter 구현체 및 사용법
- **Item 처리**: ItemProcessor 인터페이스 및 사용법
- **확장 및 병렬 처리**: 다중 스레드 Step, 병렬 Step, 원격 청크, 파티셔닝
- **Repeat·Retry**: 반복 완료 정책, 예외 처리, 재시도·백오프
