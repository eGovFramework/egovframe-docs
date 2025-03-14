---
title: 압축 파일의 종류
linkTitle: "압축 파일의 종류"
description: 다양한 압축 파일 형식과 그 사용 방식에 대해 설명하며, 각 형식의 특징과 관련 프로그램을 안내한다.
url: /egovframe-runtime/foundation-layer/compression-file-types/
menu:
    depth:
        name: 압축 파일의 종류
        weight: 1
        parent: "compress-decompress"
---
# 압축 파일의 종류
| 압축 파일  | 설명                                                                                         |
|------------|----------------------------------------------------------------------------------------------|
| .alz       | 이스트소프트에서 개발한 압축 형식입니다. 분할 압축을 할 경우 확장자는 (ALZip 으로 생성) alz, a00, a01…형식으로 생성됨. |
| .ace       | ACE, WinAce에서 이용하는 압축 형식입니다. 분할 압축을 할 경우 확장자는 ace, c00, c01, … 형식으로 생성됨.          |
| .arc       | DOS용 프로그램 pkarc.com, pkxarc.com에서 사용되는 압축 형식.                                        |
| .arj       | DOS용 프로그램 arj.exe, 윈도우용 프로그램 WinArj에서 이용하는 압축 형식. 분할 압축을 할 경우 확장자는 arj, a01, a02,… 형식으로 생기게 됨. |
| .b64       | 인터넷에서 문서를 주고 받을 때 사용하는 형식으로 BASE64MIME 형식으로 인코딩된 파일임.                     |
| .bh        | BinHex Format. E-Mail로 이진(binary) 형태의 파일을 보내기 위해 사용하는 형식임.                         |
| .bhx       | 인터넷에서 문서를 주고 받을 때 사용하는 형식으로 BASE64MIME 형식으로 인코딩된 파일임.                     |
| .bin       | Macintosh용이며, MacBinary Format. Aladdin StuffIt Expander에서 지원함.                               |
| .bz2       | UNIX용의 bzip2에서 사용하는 압축 형식입니다. 파일 하나만 압축할 수 있으므로 주로 .tar와 함께 사용되며 이 경우 .tar.bz2의 확장자를 갖음. (bzip2로 생성) |
| .cab       | Microsoft Cabinet 파일. 마이크로소프트에서 사용하는 압축 형식임.                                     |
| .ear       | 내부적으로 zip 압축 알고리즘을 사용하는 파일 형식임.                                            |
| .enc       | E-Mail로 이진(binary) 형태의 파일을 보내기 위해 사용하는 형식임.                                   |
| .gz        | UNIX용의 gzip에서 사용하는 압축 형식. 파일 하나만 압축할 수 있으므로 주로 .tar와 함께 사용되며 이 경우 .tar.gz의 확장자를 갖고 줄여서 .tgz 확장자를 사용하기도 함. |
| .ha        | PPMC를 개선한 압축 파일 형식.                                                               |
| .hqx       | 맥에서 제작된 파일을 인터넷에서 문서를 주고 받을 때 사용하는 형식임. (BinHex로 생성)                   |
| .ice       | DOS용 프로그램 ice.exe에서 사용하는 압축 형식임. 실제 파일 내용은 lha와 동일함.                          |
| .img       | Disk image를 저장해둔 파일로, Falk Huth에 의해 만들어진 img.exe라는 프로그램을 이용하여 파일들을 추출해 낼 수 있음. |
| .jar       | 자바의 jar.exe에서 사용하는 압축 형식. 내부적으로 zip 압축 알고리즘을 사용함.                          |
| .lha, .lzh | DOS용 프로그램 lha.exe, lharc.exe에서 사용하던 압축 형식. Lempel-Ziv 알고리즘을 사용함.                   |
| .mim       | 인터넷에서 문서를 주고 받을 때 사용하는 형식.                                                  |
| .pak       | DOS용 프로그램 pak.exe에서 사용하던 압축 형식.                                                  |
| .rar       | DOS용 프로그램 rar.exe와 윈도우용 프로그램 winrar.exe에서 사용하는 압축 형식. 분할 압축을 할 경우 확장자는 rar, r00, r01,… 형식으로 생기게 됨. |
| .sit       | Macintosh에서 이용되는 압축 Format. WinArj, Aladdin StuffIt Expander, WinPack 등의 윈도우용 압축 프로그램에서 이를 지원함. |
| .tar       | UNIX 명령 tar를 이용해 생성되는 파일 형식으로 실제로는 압축은 되지 않고 여러 파일을 하나로 묶어주기만 함. 보통 tar로 묶은 후 gz으로 압축하며 이 경우 .tar.gz의 확장자를 갖고 줄여서 .tgz 확장자를 사용하기도 함. |
| .tgz       | UNIX에서 tar로 묶은 파일을 gzip으로 압축한 파일 형식.                                          |
| .uue       | UU Encoded Format. E-Mail로 이진(binary) 형태의 파일을 보내기 위해 사용하는 형식.                   |
| .war       | 내부적으로 zip 압축 알고리즘을 사용하는 파일 형식.                                            |
| .xxe       | XXEncode Format. E-Mail로 이진(binary) 형태의 파일을 보내기 위해 사용하는 형식.                   |
| .z         | UNIX용의 compress, uncompress에서 사용하는 파일 형식.                                           |
| .zip       | 도스용 프로그램 pkzip.exe, pkunzip.exe에서 사용하는 파일 형식.                                   |
| .zoo       | DOS용 프로그램 zoo.exe에서 사용되는 파일 형식.                                                 |
| .001       | rzjoin으로 분할된 파일 형식. 압축이 아닌 단순히 001, 002…… 순서로만 분할된 파일.                   |
