# \[적용 예\] File Handling

## 개요

 [File Handling](https://www.egovframe.go.kr//wiki/doku.php?id=egovframework:rte2:fdl:file_handling) Service 를 적용해서 Excel 다운로드 하기 위한 Excel 정보를 설정한다.

 [Excel](https://www.egovframe.go.kr//wiki/doku.php?id=egovframework:rte2:fdl:excel) Service에 적용되어 있다.

## 설명

### Source

```bash
FileObject writtenFile = manager.resolveFile(baseDir, this.propertyPath);
FileContent writtenContents = writtenFile.getContent();
[InputStream](http://www.google.com/search?hl=en&q=allinurl%3Ainputstream+java.sun.com&btnI=I%27m%20Feeling%20Lucky) is = writtenContents.getInputStream();
 
[BufferedReader](http://www.google.com/search?hl=en&q=allinurl%3Abufferedreader+java.sun.com&btnI=I%27m%20Feeling%20Lucky) reader = new [BufferedReader](http://www.google.com/search?hl=en&q=allinurl%3Abufferedreader+java.sun.com&btnI=I%27m%20Feeling%20Lucky)(new [InputStreamReader](http://www.google.com/search?hl=en&q=allinurl%3Ainputstreamreader+java.sun.com&btnI=I%27m%20Feeling%20Lucky)(is));
[StringBuffer](http://www.google.com/search?hl=en&q=allinurl%3Astringbuffer+java.sun.com&btnI=I%27m%20Feeling%20Lucky) sb = new [StringBuffer](http://www.google.com/search?hl=en&q=allinurl%3Astringbuffer+java.sun.com&btnI=I%27m%20Feeling%20Lucky)();
 
for ([String](http://www.google.com/search?hl=en&q=allinurl%3Astring+java.sun.com&btnI=I%27m%20Feeling%20Lucky) line = ""; (line = reader.readLine()) != null; sb.append(line));
is.close();
```