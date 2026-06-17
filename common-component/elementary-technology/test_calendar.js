const https = require('https');
https.get('https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:com:v4.1:%EB%8B%AC%EB%A0%A5', (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    console.log(data.length);
  });
});
