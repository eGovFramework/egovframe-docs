---
title: Center Cut
linkTitle: CenterCut
description: 큐(Queue)를 사용하여 대용량 데이터를 처리하는 센터 컷(Center Cut) 방식의 배치 수행 방법을 설명한다. Apache ActiveMQ를 기반으로 QueueSender가 데이터를 큐에 적재하고 QueueReceiver가 이를 소비·처리하는 구조와 설정, 예제를 다룬다.
url: /egovframe-runtime/batch-layer/batch-centercut-intro/
menu:
    depth:
        name: CenterCut
        weight: 20
        parent: "batch-layer"
---
# Center Cut

## 개요

전자정부 표준프레임워크는 **큐(Queue)를 사용하여 대용량 데이터를 처리**하기 위한 센터 컷(Center Cut) 방식의 배치 작업 수행 가이드를 제공한다. 데이터를 읽어 큐에 적재하는 단계와 큐에서 데이터를 꺼내 처리하는 단계를 분리함으로써, 대용량 데이터를 안정적으로 나누어 처리할 수 있다.

## 센터 컷 가이드 구조

센터 컷은 기본적으로 일반 배치 프로그램과 유사하나, 큐 활용이 추가된다.

- **Center-Cut Reading Step**: ItemReader로 데이터를 읽어 큐에 삽입하는 단계
- **Center-Cut Process Step**: 큐에서 데이터를 읽어 처리 모듈(Business Proc)로 데이터를 처리하는 단계

이 과정에서 추가되는 핵심 모듈은 **QueueSender**와 **QueueReceiver**이다.

## 기본 구성 요소

### Apache ActiveMQ

센터 컷은 메시지 큐로 **Apache ActiveMQ**를 활용한다. 본 가이드에서 사용하는 ActiveMQ 버전은 `apache-activemq-5.15.1`이다. ActiveMQ 관리 콘솔은 `http://localhost:8161`에서 접근할 수 있으며, 관리자 계정(`admin`/`admin`)으로 로그인한 뒤 Queue 메뉴에서 큐 상태를 확인할 수 있다.

### 배치 Job 설정 (centerCutJob.xml)

데이터를 큐에 적재하는 `stepQueueSender`와 큐에서 데이터를 꺼내 처리하는 `stepQueueProc`를 순차로 구성한다.

```xml
<job id="centerCutJob" parent="eGovBaseJob" xmlns="http://www.springframework.org/schema/batch">
	<step id="stepQueueSender" next="stepQueueProc">
		<tasklet ref="taskletQueueSender" />
	</step>
	<step id="stepQueueProc">
		<tasklet ref="taskletQueueProc" />
	</step>
</job>

<bean id="taskletQueueSender" class="egovframework.rte.bat.centercut.TaskletQueueSender" scope="step">
</bean>

<bean id="taskletQueueProc" class="egovframework.rte.bat.centercut.TaskletQueueProc" scope="step">
</bean>
```

## QueueSender (TaskletQueueSender)

10,000개의 임의 데이터를 큐로 전송하고, 마지막에 `endSender`를 통해 종료(End) 메시지를 전송한다.

```java
public RepeatStatus execute(StepContribution contribution,
		ChunkContext chunkContext) throws Exception {

	LOGGER.debug("TaskletQueueSender execute START ===");

	QueueSenderFactory qf = new QueueSenderFactory("test_queue");
	TextMessage txMessage = qf.getMessage();
	MessageProducer sender = qf.getSender();
	qf.setRemove(true);

	for(int i=0; i<10000; i++){
		LOGGER.debug("Send Value : " + i );
		txMessage.setText(String.valueOf(i));
		sender.send(txMessage);
		senderCount++;
	}

	qf.endSender(sender);
	qf.close();

	LOGGER.debug("########## Center-Cut Result ##########");
	LOGGER.debug("## Sender  Count : " + senderCount);
	LOGGER.debug("########################################");

	return RepeatStatus.FINISHED;
}
```

종료 메시지는 `"End Of QUEUE"` 문자열로 전송하며, Process 단계에서 이 메시지를 수신하면 처리를 종료한다.

```java
public void endSender(MessageProducer sender) throws Exception {
	TextMessage message = session.createTextMessage();
	setRemove(true);
	message.setText("End Of QUEUE");
	sender.send(message);
}
```

## Queue Process (TaskletQueueProc)

10,000개의 데이터를 큐에서 수신하여 처리하고, 종료 메시지(`"End Of QUEUE"`)를 수신하면 배치를 종료한다.

```java
public RepeatStatus execute(StepContribution contribution,
	ChunkContext chunkContext) throws Exception {

	LOGGER.debug("TaskletQueueProc execute START ===");

	QueueReceiverFactory qf = new QueueReceiverFactory("test_queue");
	MessageConsumer receiver = qf.getReceiver();

	LOGGER.debug("=====>>>>> Start");

	while (true){
		textMessage = (TextMessage)receiver.receive();
		if(textMessage.getText().equals("End Of QUEUE")){
			LOGGER.debug("**********Receive End Message: " + textMessage.getText());
			qf.sessionCommit();
			break;
		}
		LOGGER.debug("Receive Message: " + textMessage.getText());
		qf.sessionCommit();
		recieveCount++;
	}
	qf.close();

	LOGGER.debug("########## Center-Cut Result ##########");
	LOGGER.debug("## Recieve  Count : " + recieveCount);
	LOGGER.debug("########################################");

	return RepeatStatus.FINISHED;
}
```

## 테스트 실행

`EgovCenterCutJobRunnerTest.java`를 실행하여 센터 컷 배치의 동작(데이터 적재 → 큐 소비 → 처리 종료)을 확인할 수 있다.
