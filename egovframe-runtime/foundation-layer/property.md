---
title: Property
linkTitle: "Property"
description: Property는 시스템 설정 정보를 외부에서 관리하여 유연성과 확장성을 높이는 기능으로, 동적 갱신이 가능한 Property Service와 정적 설정인 Property Source를 제공한다.
url: /egovframe-runtime/foundation-layer/property/
menu:
    depth:
        name: Property
        weight: 6
        parent: "foundation-layer"
        identifier: "Property"
---
# Property
        
Property는 시스템의 설치 환경에 관련된 정보나, 잦은 정보의 변경이 요구되는 경우 외부에서 그 정보를 관리하게 함으로써 시스템의 유연성을 높이기 위해서 제공하는 것으로 Property Service와 Property Source를 제공하고 있다.
Property Service와 Property Source는 각각의 특성과 용도에 따라 시스템의 설정 정보를 관리한다.
이와 같은 기능을 통해 전자정부프레임워크는 시스템의 유연성과 확장성을 높여준다. 
- Property Service
 - 특징: 코드 상에서 key를 통해 해당 값을 가져오는 방식으로, 외부 파일이 변경될 경우 이를 반영하여 값을 갱신할 수 있다.
 - 장점: 시스템 운영 중에도 설정 값을 동적으로 변경할 수 있어 유연성이 높다.
 - 사용 예시: 데이터베이스 연결 정보, API 키 등 자주 변경될 수 있는 설정 값 관리.
- Property Source
 - 특징: XML 또는 코드 상에서 key를 통해 값을 가져올 수 있지만, 외부 파일이 변경되어도 즉시 반영되지 않는다.
 - 단점: 설정 값 변경 시 시스템을 재시작해야 변경 사항이 반영됩니다.
 - 사용 예시: 상대적으로 변경이 적은 설정 값 관리, 예를 들어 애플리케이션의 기본 설정 값.
- Property 파일 사용 방법:
 - 별도의 Property 파일을 만들어 Spring Bean 설정 파일에 파일의 위치를 입력하여 사용할 수 있다.
 - 외부 설정 파일에 기재된 프로퍼티 내용은 어플리케이션 운영 중에 추가 및 변경이 가능하다.
