---
title: "AI 통합"
linkTitle: "AI 통합"
description: "AI 통합 서비스는 Spring 기반 애플리케이션에서 AI 기능을 쉽게 통합할 수 있도록 지원한다."
url: /egovframe-runtime/ai-layer/
menu:
    depth:
        name: "AI 통합"
        weight: 9
        parent: "egovframe-runtime"
        identifier: "ai-layer"
---

# AI 통합

## 개요

AI 통합 서비스는 Spring 기반 애플리케이션에서 LLM(대규모 언어 모델) 기능을 쉽게 통합할 수 있도록 지원한다. 실행환경은 Spring AI와 LangChain4j 두 가지 프레임워크를 제공하며, 각 프레임워크의 개념과 API, 그리고 RAG(Retrieval Augmented Generation) 샘플 프로젝트를 함께 안내한다.

## 주요 개념

AI 통합의 기본 요소는 LLM, Embedding, Vector Store이며, 이를 조합해 보유 문서를 근거로 답변하는 방식이 RAG이다. 문서를 읽어 분할·저장하는 ETL Pipeline(DocumentReader → DocumentTransformer → DocumentWriter), 대화 맥락을 유지하는 Chat Memory, 질의를 정제하는 Query Compression 등이 핵심 개념으로 사용된다.

## 관련 문서

### 개념

- [AI 개요](./ai-intro.md) — LLM·Embedding·Vector Store 등 기본 개념과 핵심 용어
- [RAG 및 고급 개념](./ai-rag-concepts.md) — RAG·ETL Pipeline·Chunking·Chat Memory·Query Compression·GGUF 포맷

### Spring AI

- [Spring AI](./springai-intro.md) — Spring 생태계에 포함되어 AI 기능 통합을 지원하는 프레임워크
- [핵심 API](./springai-core-apis.md) — ChatModel·ChatClient·Prompt Engineering·Structured Output·Embedding Model
- [RAG 아키텍처](./springai-rag-architecture.md) — Vector Store와 RAG 3단계 프로세스
- [Advisor 패턴](./springai-advisor-guide.md) — QuestionAnswerAdvisor·RetrievalAugmentationAdvisor·Query Transformer
- [ETL Pipeline](./springai-etl-guide.md) — DocumentReader·DocumentTransformer·DocumentWriter
- [환경 설정](./springai-setup-guide.md) — Ollama·Embedding 모델·Redis Stack 설치 및 실행 방법

### Spring AI 샘플

- [샘플 프로젝트](./springai-sample-project.md) — 개요·아키텍처·프로젝트 구조
- [RAG 구현](./springai-sample-rag.md) — Advisor Chain·Query Compression·VectorStoreDocumentRetriever
- [ETL 구현](./springai-sample-etl.md) — 문서 적재 파이프라인 구현
- [세션 관리](./springai-sample-session.md) — Chat Memory·Redis 저장·세션 생명주기

### LangChain4j

- [LangChain4j](./langchain4j-intro.md) — AiServices 프록시 패턴 기반 Java LLM 개발 프레임워크
- [샘플 프로젝트](./langchain4j-sample-project.md) — 개요·기술 스택·프로젝트 구조·환경 설정
- [핵심 구현](./langchain4j-sample-implementation.md) — AiServices·ChatbotFactory·PersistentChatMemoryStore

## 참고자료

- [AI RAG 샘플 저장소 (egovframe-ai-rag)](https://github.com/eGovFramework/egovframe-ai-rag)
- [표준프레임워크 실행환경 소개](../intro/overview.md)
