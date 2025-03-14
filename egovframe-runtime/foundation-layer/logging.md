---
title: Logging
linkTitle: Logging
url: /egovframe-runtime/foundation-layer/logging/
menu:
    depth:
        name: Logging
        weight: 4
        parent: "foundation-layer"
        identifier: "logging"
description: 전자정부 표준프레임워크 3.0부터 SLF4J를 도입하여 다양한 로깅 프레임워크와 연계하며, Log4j 2를 기본 로깅 구현체로 사용한다. 로깅 서비스는 시스템 상태를 기록하고 관리할 수 있지만, 성능 오버헤드를 줄이기 위한 메커니즘이 필요하다. System.out.println() 대신 SLF4J와 Log4j 2를 사용한 로깅이 권장된다.
---
# Logging 서비스

## 개요

 전자정부 표준프레임워크 3.0부터는 다양한 Logging Framework와 연계할 수 있도록 **SLF4J**를 도입하였고,  
Logging 구현체는 **Log4j 2**를 이용하여 Logging을 수행한다.

 Logging 서비스는 시스템의 개발이나 운용시 발생할 수 있는 사항에 대해서,  
시스템의 외부 저장소에 기록하여 시스템의 상황을 쉽게 파악할 수 있도록 도와준다.  
뿐만 아니라 테스팅 코드와 운영 코드를 동일하게 가져가면서 로깅을 선언적으로 관리할 수 있다.  
과도한 Logging은 운영시 성능 오버헤드를 발생시킬 수 있으므로, 최소화할 수 있는 메커니즘이 필요하다.

 많은 개발자가 Log을 출력하기 위해 일반적으로 사용하는 방식은 System.out.println()이다.  
하지만 이 방식은 간편한 반면, 다음과 같은 이유로 권장하지 않는다.

- 콘솔 로그를 출력 파일로 리다이렉트 할 지라도, 어플리케이션 서버가 재시작할 때 파일이 overwrite될 수도 있음
- 개발/테스팅 시점에만 System.out.println()을 사용하고 운영으로 이관하기 전에 삭제하는 것은 좋은 방법이 아님
- System.out.println() 호출은 디스크 I/O동안 동기화(synchronized)처리가 되므로 시스템의 throughput을 떨어뜨림
- 기본적으로 stack trace 결과는 콘솔에 남지만, 시스템 운영 중 콘솔을 통해 Exception을 추적하는 것은 바람직하지 못함
- 운영시의 코드가 테스트시의 코드와 다르게 동작할 수 있음

 본 페이지에서는 SLF4j와 Log4j 2에 대한 기본 사용법과 Migration에 대해 설명한다.

## 설명

- [SLF4J](./logging-slf4j.md)
- [Log4J 2](./logging-log4j2.md)

    - [프로그래밍내에서 직접 설정하는 방법](./logging-log4j2-configuration_code.md)
    - [설정 파일을 사용하는 방법](./logging-log4j2-configuration_file.md)