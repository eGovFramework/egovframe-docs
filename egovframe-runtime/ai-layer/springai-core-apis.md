---
title: "핵심 API"
linkTitle: "핵심 API"
description: "Spring AI의 ChatModel, ChatClient, Prompt Engineering, Structured Output, Embedding Model 등 핵심 API 사용법을 설명한다."
url: /egovframe-runtime/ai-layer/springai-layer/springai-core-apis/
menu:
    depth:
        name: "핵심 API"
        weight: 1
        parent: "springai-layer"
        identifier: "springai-core-apis"
---
# 핵심 API

## 개요

Spring AI는 다양한 AI 모델과 상호작용하기 위한 핵심 API를 제공한다. 이 문서에서는 ChatModel, ChatClient, Prompt Engineering, Structured Output, Embedding Model 등의 사용법을 설명한다.

---

## ChatModel과 ChatClient

**ChatModel**은 Spring AI에서 LLM(Large Language Model)과 상호작용하는 핵심 인터페이스이다.

```java
public interface ChatModel extends Model<Prompt, ChatResponse>, StreamingChatModel {

    default String call(String message) {...}

    @Override
    ChatResponse call(Prompt prompt);
}
```

**다양한 AI 모델 간 일관된 인터페이스 제공:**
- Spring Boot의 Auto Configuration 활용
- 제공자 변경 시 코드 수정 최소화

<br/>

**동기식 및 스트리밍 응답 지원**
- 간단한 문자열 호출
- 복잡한 Prompt 객체 기반 호출
- 실시간 스트리밍 응답

<br/>

**세밀한 요청/응답 제어**
- ChatOptions를 통한 모델 파라미터 제어
- 메타데이터를 포함한 상세 응답 정보

---

### 핵심 클래스

**Prompt:** 요청을 구성하는 핵심 클래스로 messages(메시지 리스트)와 modelOptions(모델 옵션)를 포함한다.

**MessageType:** UserMessage(사용자 질의), AssistantMessage(AI 응답), SystemMessage(AI 동작 방식 정의), ToolResponseMessage(함수 호출 결과)

**ChatOptions:** 모델 이름, Temperature(창의성 0.0~1.0), MaxTokens(응답 길이 제한), TopK(상위 반환 문서) 등 AI 모델 옵션을 정의한다.

**ChatResponse:** AI 모델의 응답을 담는 클래스로 generations(응답 결과)와 metadata(토큰 사용량 등)를 포함한다.

---

### 기본 사용법

**간단한 호출:**

```java
@RestController
@RequiredArgsConstructor
public class ChatController {

    private final OllamaChatModel chatModel;

    // 간단한 호출
    @GetMapping("/simple")
    public String simpleCall() {
        return chatModel.call("Tell me a joke");
    }
}
```

**Prompt 기반 호출:**
```java
@GetMapping("/advanced")
public String advancedCall() {

    Prompt prompt = new Prompt(new UserMessage("Explain Spring Boot"));

    // 실제 애플리케이션에서는 Prompt를 받아 호출하는 것이 일반적
    ChatResponse response = chatModel.call(prompt);
    
    return response.getResult().getOutput().getContent();
}
```

**스트리밍 응답:**
```java
@GetMapping("/stream")
public Flux<ChatResponse> streamCall() {

    Prompt prompt = new Prompt(new UserMessage("Tell me a story"));
    
    return chatModel.stream(prompt);
}
```

---

### ChatOptions 활용

Prompt와 Options를 조합하여 세밀한 제어가 가능하다.

```java
ChatResponse response = chatModel.call(
    new Prompt(
        "Tell me a joke about Spring",
        ChatOptions.builder()
            .withModel("gpt-4")
            .withTemperature(0.7)    // 창의성
            .withMaxTokens(100)      // 최대 길이
            .build()
    )
);

String content = response.getResult().getOutput().getContent();
```

**주요 옵션:**
- `Model`: 사용할 모델 지정
- `Temperature`: 0.0~1.0 (창의성 조절)
- `MaxTokens`: 최대 토큰 수

---

### ChatClient

**ChatClient**는 고수준(High-level) Fluent API를 제공하는 인터페이스이다. 메서드 체이닝으로 직관적인 코드 작성이 가능하고, Advisor 패턴을 통해 RAG, Memory 등 고급 기능을 통합할 수 있다.

가장 간단한 방법은 Spring Boot 자동 구성으로 생성된 `ChatClient.Builder` 빈을 주입받는 것이다.

```java
@RestController
class MyController {
    private final ChatClient chatClient;

    public MyController(ChatClient.Builder chatClientBuilder) {
        this.chatClient = chatClientBuilder.build();
    }

    @GetMapping("/ai")
    String generation(String userInput) {
        return this.chatClient.prompt()
            .user(userInput)
            .call()
            .content();
    }
}
```

**주요 메서드:**
- `prompt()`: 프롬프트 시작
- `user()`: 사용자 메시지 설정
- `call()`: 모델 호출
- `content()`: 응답을 문자열로 변환

---

### 복수 ChatClient 사용

서로 다른 구성의 여러 ChatClient 인스턴스를 생성할 수 있다.

```java
import org.springframework.ai.chat.ChatClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ChatClientConfig {

    @Bean
    public ChatClient openAiChatClient(OpenAiChatModel chatModel) {
        return ChatClient.create(chatModel);
    }

    @Bean
    public ChatClient anthropicChatClient(AnthropicChatModel chatModel) {
        return ChatClient.create(chatModel);
    }
}
```

**@Qualifier를 통한 주입:**
```java
@Configuration
public class ChatClientExample {

    @Bean
    CommandLineRunner cli(
            @Qualifier("openAiChatClient") ChatClient openAiChatClient,
            @Qualifier("anthropicChatClient") ChatClient anthropicChatClient) {

        return args -> {
            var scanner = new Scanner(System.in);
            ChatClient chat;

            String choice = scanner.nextLine().trim();

            if (choice.equals("1")) {
                chat = openAiChatClient;
                System.out.println("Using OpenAI model");
            } else {
                chat = anthropicChatClient;
                System.out.println("Using Anthropic model");
            }

            System.out.print("\nEnter your question: ");
            String input = scanner.nextLine();
            String response = chat.prompt(input).call().content();
            System.out.println("ASSISTANT: " + response);

            scanner.close();
        };
    }
}
```

---

### ChatClient with Advisor

샘플 프로젝트에서는 ChatClient에 Advisor 체인을 적용하여 RAG와 Chat Memory를 통합한다.

```java
public Flux<ChatResponse> streamRagResponse(String query, String model) {
    String sessionId = SessionContext.getCurrentSessionId();

    // 동적 모델 선택 지원
    ChatClientRequestSpec requestSpec = createRequestSpec(query, model);

    // RAG 어드바이저 동적 생성 (질문 압축 설정에 따라)
    Advisor ragAdvisor = EgovRagConfig.createRagAdvisor(
            sessionId, compressionTransformer,
            vectorStoreDocumentRetriever, enableQueryCompression);

    // ChatMemory + RAG Advisor 체인 적용
    return requestSpec
            .advisors(messageChatMemoryAdvisor, ragAdvisor)
            .advisors(a -> a.param(ChatMemory.CONVERSATION_ID, sessionId))
            .stream()
            .chatResponse();
}
```

**주요 메서드:**
- `advisors(Advisor...)`: Advisor 객체 등록
- `advisors(Consumer<AdvisorSpec>)`: Advisor에게 파라미터 전달
- `stream()`: 스트리밍 모드로 전환
- `chatResponse()`: Flux\<ChatResponse\> 반환

---

### 스트리밍 응답 처리

Controller에서 `Flux<ChatResponse>`를 반환하면 Spring MVC가 SSE(Server-Sent Events)로 처리한다.

```java
@GetMapping("/ai/rag/stream")
public Flux<ChatResponse> streamRagResponse(
        @RequestParam(value = "message") String message,
        @RequestParam(value = "model", required = false) String model,
        @RequestParam(value = "sessionId", required = false) String sessionId) {

    // 세션 컨텍스트 설정 및 검증
    SessionContext.setCurrentSessionId(sessionId);

    return sessionAwareChatService.streamRagResponse(message, model)
            .doFinally(signalType -> SessionContext.clear());
}
```

**Frontend 예시 (JavaScript):**
```javascript
function sendMessage(message, sessionId) {
    const eventSource = new EventSource(
        `/ai/rag/stream?message=${encodeURIComponent(message)}&sessionId=${sessionId}`
    );

    eventSource.onmessage = function(event) {
        const data = JSON.parse(event.data);
        if (data.result && data.result.output) {
            appendToChat(data.result.output.content);
        }
    };

    eventSource.onerror = function() {
        eventSource.close();
    };
}
```

---

## Prompt Engineering

Spring AI에서는 `PromptTemplate` 클래스를 사용하여 구조화된 프롬프트를 생성할 수 있다. 템플릿 변수는 `{}` 구문으로 식별된다.

```java
// 템플릿 정의
PromptTemplate promptTemplate = new PromptTemplate(
    "Tell me a {adjective} joke about {topic}"
);

// 변수 바인딩
Prompt prompt = promptTemplate.create(
    Map.of("adjective", "funny", "topic", "programming")
);

// 실행
ChatResponse response = chatModel.call(prompt);
```

**구분자 변경:** JSON과의 충돌을 방지하기 위해 구분자를 변경할 수 있다.

```java
PromptTemplate promptTemplate = PromptTemplate.builder()
    .renderer(StTemplateRenderer.builder()
        .startDelimiterToken('<')
        .endDelimiterToken('>')
        .build())
    .template("""
        Tell me the names of 5 movies whose soundtrack was composed by <composer>.
        """)
    .build();

String prompt = promptTemplate.render(Map.of("composer", "John Williams"));
```

---

**SystemPromptTemplate:** 시스템 역할의 메시지를 생성할 수 있다.

```java
String userText = """
    Tell me about three famous pirates from the Golden Age of Piracy and why they did.
    Write at least a sentence for each pirate.
    """;

Message userMessage = new UserMessage(userText);

String systemText = """
  You are a helpful AI assistant that helps people find information.
  Your name is {name}
  You should reply to the user's request with your name and also in the style of a {voice}.
  """;

SystemPromptTemplate systemPromptTemplate = new SystemPromptTemplate(systemText);
Message systemMessage = systemPromptTemplate.createMessage(
    Map.of("name", "Claude", "voice", "pirate")
);

Prompt prompt = new Prompt(List.of(userMessage, systemMessage));
List<Generation> response = chatModel.call(prompt).getResults();
```

**활용 시나리오:**
- AI의 역할 및 톤 정의
- 도메인 특화 지식 주입
- 응답 형식 가이드라인 제공

---

## Structured Output

AI 모델의 응답을 자연어가 아닌 Java 객체로 변환할 수 있다.

**ChatClient 활용:**

```java
// 반환될 객체 정의
record ActorsFilms(String actor, List<String> movies) { }

// 응답을 ActorsFilms로 반환하도록 AI 모델에 요청
ActorsFilms actorsFilms = ChatClient.create(chatModel).prompt()
    .user(u -> u.text("Generate the filmography of 5 movies for {actor}.")
                .param("actor", "Tom Hanks"))
    .call()
    .entity(ActorsFilms.class);
```

**장점:**
- 타입 안전성 확보
- 자동 역직렬화
- 코드 가독성 향상

<br/>

---

**ChatModel 직접 활용:** `BeanOutputConverter`를 사용하여 구조화된 출력을 생성할 수 있다.

```java
// BeanOutputConverter 생성
BeanOutputConverter<ActorsFilms> beanOutputConverter =
    new BeanOutputConverter<>(ActorsFilms.class);

String format = beanOutputConverter.getFormat();
String actor = "Tom Hanks";

String template = """
    Generate the filmography of 5 movies for {actor}.
    {format}
    """;

// Prompt 생성 및 호출
Generation generation = chatModel.call(
    PromptTemplate.builder()
        .template(template)
        .variables(Map.of("actor", actor, "format", format))
        .build()
        .create()
).getResult();

// 응답을 객체로 변환
ActorsFilms actorsFilms = beanOutputConverter.convert(
    generation.getOutput().getText()
);
```

**활용 사례:**
- JSON API 응답 생성
- 데이터베이스 엔티티 자동 생성
- 구조화된 보고서 생성

---

## Embedding Model

Spring AI는 다양한 EmbeddingModel 구현체를 제공한다.

**지원 제공자:**

| 제공자 | 의존성 |
|--------|--------|
| OpenAI | spring-ai-starter-model-openai |
| Azure's OpenAI | spring-ai-starter-model-azure-openai |
| Ollama | spring-ai-starter-model-ollama |
| Transformers (ONNX) | spring-ai-starter-model-transformers |
| PostgresML | spring-ai-starter-model-postgresml-embedding |
| Amazon Bedrock (Cohere) | spring-ai-starter-model-bedrock |
| Amazon Bedrock (Titan) | spring-ai-starter-model-bedrock |
| Google VertexAI | spring-ai-starter-model-vertex-ai-embedding |
| Mistral AI | spring-ai-starter-model-mistral-ai |
| OCI GenAI | spring-ai-starter-model-oci-genai |

---

<br/>

**Embedding이란?** 자연어를 기계가 이해할 수 있는 숫자의 나열(Vector)로 변환하는 과정이다. 텍스트를 Vector로 변환 후 Vector 간 거리를 계산하여 가장 유사한 문서를 찾는다.

**ONNX (Open Neural Network Exchange):** 기계학습 모델을 다른 딥러닝 프레임워크 환경에서 서로 호환되게 사용할 수 있도록 만든 공유 플랫폼이다. 로컬 환경에서 Embedding 수행이 가능하다.

---

**EmbeddingModel 사용 예시:** Onnx 모델을 사용한 수동 Embedding 요청 방법이다.

```java
TransformersEmbeddingModel embeddingModel = new TransformersEmbeddingModel();

// (optional) tokenizer 리소스 설정
embeddingModel.setTokenizerResource(
    "classpath:/onnx/all-MiniLM-L6-v2/tokenizer.json"
);

// (optional) 모델 리소스 설정
embeddingModel.setModelResource(
    "classpath:/onnx/all-MiniLM-L6-v2/model.onnx"
);

// (optional) 캐시 디렉토리 설정
embeddingModel.setResourceCacheDirectory("/tmp/onnx-zoo");

// (optional) tokenizer 패딩 설정
embeddingModel.setTokenizerOptions(Map.of("padding", "true"));

embeddingModel.afterPropertiesSet();

// Embedding 수행
List<List<Double>> embeddings = embeddingModel.embed(
    List.of("Hello world", "World is big")
);
```

**참고:**
- 공식 문서에서 각 제공자별 설정 방법 확인 가능
- https://docs.spring.io/spring-ai/reference/api/embeddings.html

## 참고자료
* https://docs.spring.io/spring-ai/reference/api/chatmodel.html
* https://docs.spring.io/spring-ai/reference/api/chatclient.html
* https://docs.spring.io/spring-ai/reference/api/embeddings.html
