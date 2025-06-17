---
title: "Maven에서 생성한 테스트 결과 HTML 리포트"
linkTitle: "Maven에서 생성한 테스트 결과 HTML 리포트"
description: "Maven에서 생성한 테스트 결과 HTML 리포트다."
url: /egovframe-development/test-tool/ref/maven-test-report
menu:
  depth:
    weight: 5
    parent: "ref"
---
# Maven에서 생성한 테스트 결과 HTML 리포트

Maven을 통해 테스트를 실행하면 다음과 같은 항목들이 포함된 HTML 리포트가 생성됩니다.

| 항목         | 설명                                                              |
| ------------ | ----------------------------------------------------------------- |
| Tests        | 전체 TestCase 수                                                  |
| Errors       | 전체 에러가 발생한 TestCase 수                                    |
| Failures     | 전체 실패한 TestCase 수                                           |
| Skipped      | 전체 테스트를 수행하지 않은 TestCase 수 (@Ignore 설정된 TestCase) |
| Success Rate | 전체 성공한 TestCase 백분율                                       |
| Time         | TestCase가 수행되는 걸린 초단위 시간                              |
