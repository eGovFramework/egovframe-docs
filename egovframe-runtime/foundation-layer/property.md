## 개요

 Property는 시스템의 설치 환경에 관련된 정보나, 잦은 정보의 변경이 요구되는 경우 외부에서 그 정보를 관리하게 함으로써 시스템의 유연성을 높이기 위해서 제공하는 것으로 Property Service와 Property Source를 제공하고 있다.

- Property Service : 코드 상에서 key를 통해 해당 값을 가져오는 방식으로 외부 파일 변경 시 refresh가 가능하다.
- Property Source : xml 또는 코드 상에서 key를 통해 해당 값을 가져올 수 있으나 외부 파일이 변경되어도 refresh가 불가능하다.