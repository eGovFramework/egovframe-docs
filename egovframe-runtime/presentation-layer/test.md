# Customizing the nature of a bean

## 개요
컨테이너의 빈 라이프사이클 관리와 상호 작용하기 위해 Spring InitializingBean 및 DisposableBean 인터페이스를 구현할 수 있는데, 컨테이너는 전자의 경우 afterPropertiesSet()을 호출하고 후자의 경우 destroy()를 호출하여 빈이 초기화 및 소멸될 때 특정 작업을 수행하도록 한다.