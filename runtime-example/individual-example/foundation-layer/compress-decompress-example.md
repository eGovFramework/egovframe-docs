---
title: 압축/압축해제 예제(Compress/Decompress Example)
linkTitle: "압축/압축해제 예제"
description: 전자정부 표준프레임워크에서 서버에 있는 파일을 압축 및 해제하는 기능을 제공하는 컨트롤러 예제를 다룬다.
url: /runtime-example/individual-example/foundation-layer/compress-decompress-example/
menu:
    depth:
        name: 압축/압축해제 예제
        weight: 4
        parent: "foundationLayer"
---
# 압축/압축해제 예제(Compress/Decompress Example)

## 개요
전자정부 표준프레임워크 상에서 서버상에 존재하는 특정 파일을 압축하거나 압축 해제하는 기능에 대한 예제를 제공한다. 서버상에서 지정된 파일을 zip 파일로 압축하고, 이를 다시 압축 해제하는 기능을 controller 상에서 수행하는 기능을 제공한다.

## 설명
1. 해당 예제를 실행하고 성공메세지를 확인한다.

![compress-1.png](./images/compress-1.png)

2. 실행에 성공하면 테스트파일을 압축해 C:\egovCompressSample.zip 형태로 압축된다.

![compress-2.png](./images/compress-2.png)

3. [압축해제]를 누르고 성공메세지를 확인한다.

![compress-3.png](./images/compress-3.png)

4. 압축해제가 성공하면 C:\egovCompressSample폴더에 압축해제된 파일이 생성되어 있다.

![compress-4.png](./images/compress-4.png)

## 참고자료
- [Compress/Decompress 서비스](../../../egovframe-runtime/foundation-layer/compress-decompress.md)