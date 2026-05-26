---
title: "샘플 프로젝트"
linkTitle: "샘플 프로젝트"
description: "전자정부 표준프레임워크 기반 LangChain4j RAG 샘플 프로젝트의 개요, 기술 스택, 프로젝트 구조, 환경 설정을 설명한다."
url: /egovframe-runtime/ai-layer/langchain4j-layer/langchain4j-sample-project/
menu:
    depth:
        name: "샘플 프로젝트"
        weight: 1
        parent: "langchain4j-layer"
        identifier: "langchain4j-sample-project"
---
# 샘플 프로젝트

## 개요

전자정부 표준프레임워크 기반의 **문서 기반 질의응답 시스템**을 LangChain4j로 구현한 실습 프로젝트이다.

**채팅 애플리케이션:**
- 일반 채팅 / 컨텍스트 기반 대화
- 세션 관리를 통한 멀티턴 대화
- 동적 LLM 모델 선택

<br/>

**RAG (Retrieval-Augmented Generation):** 문서 기반 질의 응답, 벡터 검색을 통한 관련 문서 검색으로 환각 감소

**문서 처리:** PDF, Markdown 등 다양한 형식 지원, 문서 분할 및 정규화, Embedding 생성 및 벡터 저장

**스트리밍 응답:** langchain4j-reactor 기반 Flux 네이티브 스트리밍, 실시간 응답 생성

---

## 기술 스택

| 항목 | 기술 | 버전 및 비고 |
|------|------|-------------|
| **Framework** | Spring Boot + eGovFrame | 3.x + 5.0.0 |
| **AI Framework** | LangChain4j | 1.8.0 / 1.8.0-beta15 |
| **LLM** | Ollama | qwen3-4b:Q4_K_M |
| **Embedding** | ONNX Runtime | ko-sroberta-multitask |
| **Vector Store** | PostgreSQL + PGVector | 14+ |
| **Chat Memory** | PostgreSQL (JPA) | 영구 저장 |
| **Streaming** | langchain4j-reactor | Flux 네이티브 |
| **Build** | Maven | 3.8.4+ |

---

## 의존성 관리

본 프로젝트는 `egovframe-boot-starter-parent` 5.0.0을 parent로 사용한다. eGovFrame 5.0.0에서 LangChain4j 의존성 버전을 공식 관리하므로, 별도의 BOM 선언이나 버전 명시 없이 간결하게 사용할 수 있다.

```xml
<parent>
    <groupId>org.egovframe.boot</groupId>
    <artifactId>egovframe-boot-starter-parent</artifactId>
    <version>5.0.0</version>
    <relativePath/>
</parent>

<dependencies>
    <!-- 버전 명시 불필요 - egovframe-boot-starter-parent가 관리 -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j</artifactId>
    </dependency>
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-ollama</artifactId>
    </dependency>
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-pgvector</artifactId>
    </dependency>
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-embeddings</artifactId>
    </dependency>
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-reactor</artifactId>
    </dependency>
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-document-parser-apache-pdfbox</artifactId>
    </dependency>
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-easy-rag</artifactId>
    </dependency>
</dependencies>
```

egovframe-boot-starter-parent 5.0.0이 관리하는 LangChain4j 버전:

| 구분 | artifactId | 버전 |
|------|-----------|------|
| **정식** | langchain4j, langchain4j-ollama, langchain4j-redis, langchain4j-spring-boot-starter | 1.8.0 |
| **Beta** | langchain4j-pgvector, langchain4j-embeddings, langchain4j-reactor, langchain4j-easy-rag, langchain4j-document-parser-apache-pdfbox | 1.8.0-beta15 |

> **참고**: 일반적인 LangChain4j 프로젝트에서는 `langchain4j-bom`을 사용하여 버전을 관리하지만, 표준프레임워크 프로젝트에서는 parent POM이 이를 대신한다.

---

## 프로젝트 구조

```
langchain4j-ai-rag-postgre/
|-- src/main/java/com/example/chat/
|   |-- config/                              # 설정 클래스
|   |   |-- LangChain4jConfig.java           # LLM, 임베딩, PGVector 설정
|   |   +-- RagConfig.java                   # ContentRetriever 설정
|   |
|   |-- service/                             # 서비스 계층
|   |   |-- RagChatbot.java                  # RAG 챗봇 인터페이스 (AiServices)
|   |   |-- SimpleChatbot.java               # 일반 챗봇 인터페이스 (AiServices)
|   |   |-- ChatbotFactory.java              # 챗봇 팩토리 (동적 모델 선택)
|   |   |-- ChatService.java                 # 채팅 서비스 인터페이스
|   |   +-- impl/
|   |       |-- ChatServiceImpl.java         # 채팅 서비스 구현체
|   |       +-- DocumentServiceImpl.java     # 문서 서비스 구현체
|   |
|   |-- repository/                          # 데이터 접근 계층
|   |   |-- PersistentChatMemoryStore.java   # ChatMemoryStore 구현
|   |   |-- ChatMemoryRepository.java        # JPA Repository
|   |   +-- ChatSessionRepository.java       # 세션 Repository
|   |
|   |-- entity/                              # JPA 엔티티
|   |   |-- ChatMemoryEntity.java            # 채팅 메모리 엔티티
|   |   +-- ChatSessionEntity.java           # 세션 엔티티
|   |
|   |-- controller/                          # REST 컨트롤러
|   |   |-- ChatController.java              # 채팅 API
|   |   |-- ChatSessionController.java       # 세션 API
|   |   +-- DocumentController.java          # 문서 API
|   |
|   |-- context/
|   |   +-- SessionContext.java              # ThreadLocal 세션 관리
|   |
|   +-- util/
|       +-- ConfigUtils.java                 # 외부 설정 로드 유틸
|
|-- src/main/resources/
|   |-- application.yml                      # 애플리케이션 설정
|   +-- templates/
|       +-- chat.html                        # 채팅 UI
|
|-- docker-compose.yml                       # PostgreSQL 설정
+-- pom.xml
```

---

## 환경 설정

**LLM 설정:**
```yaml
langchain4j:
  ollama:
    base-url: http://localhost:11434
    chat-model:
      model-name: qwen3-4b:Q4_K_M
      temperature: 0.4
      timeout: 60s
```

**ONNX 임베딩 모델 설정:**
```yaml
app:
  embedding-config-path: ${user.home}/EgovSearch-Config/Config/searchConfig.json
```

외부 설정 파일(searchConfig.json)에서 modelPath와 tokenizerPath를 지정한다.

```json
// searchConfig.json
{
  "modelPath": "C:/Users/username/model/model.onnx",
  "tokenizerPath": "C:/Users/username/model/tokenizer.json"
}
```

**PostgreSQL + PGVector 설정:**
```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/ragdb
    username: postgres
    password: postgres

pgvector:
  host: localhost
  port: 5432
  database: ragdb
  table-name: document_embeddings
  dimension: 768
  create-table: true
  distance-type: cosine
```

**RAG 설정:**
```yaml
rag:
  similarity:
    threshold: 0.20
  top-k: 3

chat:
  memory:
    max-messages: 20
    table-name: chat_memory
```

---

## 실행 방법

```bash
# PostgreSQL + PGVector 실행
docker-compose up -d

# Ollama 모델 다운로드
ollama pull qwen3-4b:Q4_K_M

# 애플리케이션 실행
mvn spring-boot:run
```

| 서비스 | URL |
|--------|-----|
| 채팅 UI | http://localhost:8080 |
| PostgreSQL | localhost:5432 (ragdb) |
| Ollama API | http://localhost:11434 |

---

## 상세 가이드

- [핵심 구현](./langchain4j-sample-implementation.md)
AiServices 패턴, ChatbotFactory, PersistentChatMemoryStore, ContentRetriever 구현을 설명한다.

## 참고자료

* https://docs.langchain4j.dev/
* https://github.com/langchain4j/langchain4j
* https://docs.langchain4j.dev/tutorials/ai-services
