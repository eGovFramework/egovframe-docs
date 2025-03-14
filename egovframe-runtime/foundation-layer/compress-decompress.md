---
title: Compress/Decompress Service
linkTitle: "Compress/Decompress"
description: 전자정부 표준프레임워크는 Jakarta Commons Compress를 통해 다양한 압축 방식(tar, zip, bzip2 등)을 지원하는 편리한 API를 제공한다.
url: /egovframe-runtime/foundation-layer/compress-decompress/
menu:
    depth:
        name: Compress/Decompress
        weight: 15
        parent: "foundation-layer"
        identifier: "compress-decompress"
---
# Compress/Decompress Service

## 개요

**전자정부 프레임워크**에서는 다양한 압축방식을 개발자들에게 편리한 API를 제공하는 Jakarta Commons의 Compress를 오픈소스로 채택하였다.

Jakarta Commons의 Compress에서 지원하는 tar, zip and bzip2 파일등을 지원한다.

현재 Commons Compress API 에서는 아래의 Packages를 제공하고 있다.

- org.apache.commons.compress.archivers   
- org.apache.commons.compress.archivers.ar   
- org.apache.commons.compress.archivers.cpio   
- org.apache.commons.compress.archivers.jar   
- org.apache.commons.compress.archivers.tar   
- org.apache.commons.compress.archivers.zip   
- org.apache.commons.compress.changes   
- org.apache.commons.compress.compressors   
- org.apache.commons.compress.compressors.bzip2   
- org.apache.commons.compress.compressors.gzip   
- org.apache.commons.compress.utils

보다 자세한 사항은 [Commons Compress API](http://commons.apache.org/compress/apidocs/index.html)를 참고하기 바란다.

## 설명

**압축**이란 파일에 저장되어 있는 정보를 압축하여 보다 적은 기억 공간에 동일한 정보를 저장하는 기술이다.

```
일반적으로 정보에 포함되어 있는 중복된 내용을 삭제하거나 보다 적은 길이의 코드를 사용하여 정보를 표현하는 방법을 사용하여 저장에 필요한 공간의 크기를 줄인다. 
이런 과정을 압축이라고 하며, 압축된 정보를 사용하기 위해서 다시 원래의 상태로 복원하는 과정을 압축해제라고 한다.
압축 방법에는 손실이 없는 압축 방법과 손실이 있는 압축 방법이 있다.
먼저 프로그램과 데이터 등과 같은 정보는 반드시 손실이 없는 압축 방법을 사용하여야 한다.
손실이 없는 압축 방법이라고 하는 것은 압축된 정보를 다시 복원한 경우에 압축되기 이전의 상태와 동일한 내용과 크기를 가지게 되는 압축 방법을 말한다.
하지만 이미지나 음성 등과 같은 경우에는 손실이 있는 압축 방법을 사용할 수 있다.
이미지나 음성에는 방대한 양의 정보가 존재하고 이들 정보 중에 일부가 사라진다 하더라도 사람이 눈이나 귀로 그 차이를 구별할 수 없기 때문이다.
손실이 있는 압축 방법이라고 하는 것은 압축된 정보를 다시 복원하더라도 압축되기 이전의 상태 혹은 크기와 동일하지 않은 내용을 가질 수 있는 압축 방법을 뜻한다.
```
간단히 여기서는 자주 사용하는 압축파일의 종류는 아래의 참조 링크를 참고한다.

- [압축파일의 종류](./compression-file-types.md)

## 사용 예제

다음은 테스트코드 EgovZipTestCase의 testZipArchiveCreation() 메소드로 org.apache.commons.compress.archivers 패키지에 속한 ArchiveInputStream 클래스를 사용하여 compress/decompress로 구성되어 있다.

```java
public final class EgovZipTestCase extends EgovAbstractTestCase {
 
	/*
	 * Zip을 사용한 압축(Archive) TEST
	 * 두개의 파일(test1.xml, test2.xml)을 사용하여  압축하여 bla.zip으로 압축함
	 */
	public void testZipArchiveCreation() throws Exception {
        // Archive
        final File output = new File(dir, "bla.zip");
        final File file1 = getFile("test1.xml");
        final File file2 = getFile("test2.xml");
 
        {
            final OutputStream out = new FileOutputStream(output);
            final ArchiveOutputStream os = new ArchiveStreamFactory().createArchiveOutputStream("zip", out);
 
            os.putArchiveEntry(new ZipArchiveEntry("testdata/test1.xml"));
            IOUtils.copy(new FileInputStream(file1), os);
            os.closeArchiveEntry();
 
            os.putArchiveEntry(new ZipArchiveEntry("testdata/test2.xml"));
            IOUtils.copy(new FileInputStream(file2), os);
            os.closeArchiveEntry();
            os.close();
        }
 
        // Unarchive the same
        List results = new ArrayList();
 
        {
            final InputStream is = new FileInputStream(output);
            final ArchiveInputStream in = new ArchiveStreamFactory().createArchiveInputStream("zip", is);
 
            File result = File.createTempFile("dir-result", "");
            result.delete();
            result.mkdir();
 
            ZipArchiveEntry entry = null;
            while((entry = (ZipArchiveEntry)in.getNextEntry()) != null) {
                File outfile = new File(result.getCanonicalPath() + "/result/" + entry.getName());
                outfile.getParentFile().mkdirs();
                OutputStream out = new FileOutputStream(outfile);
                IOUtils.copy(in, out);
                out.close();
                results.add(outfile);
            }
            in.close();
        }
 
        assertEquals(results.size(), 2);
        File result = (File)results.get(0);
        assertEquals(file1.length(), result.length());
        result = (File)results.get(1);
        assertEquals(file2.length(), result.length());
    }
}
```

다음은 위에서 압축한 파일을 압축해제(Unarchive)하는 테스트 코드이다.

```java
public void testZipUnarchive() throws Exception {
    final File input = getFile("bla.zip");
    final InputStream is = new FileInputStream(input);
    final ArchiveInputStream in = new ArchiveStreamFactory().createArchiveInputStream("zip", is);
    final ZipArchiveEntry entry = (ZipArchiveEntry)in.getNextEntry();
    final OutputStream out = new FileOutputStream(new File(dir, entry.getName()));
    IOUtils.copy(in, out);
    out.close();
    in.close();
}
```

## 참고자료

- [Apache Commons Compress](http://commons.apache.org/compress/index.html)
- [Commons Compress API](http://commons.apache.org/compress/apidocs/index.html)

## 예제

- [Compress/Decompress 예제](../../runtime-example/individual-example/foundation-layer/compress-decompress-example.md)