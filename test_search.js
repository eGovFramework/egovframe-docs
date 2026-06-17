const https = require('https');
https.get('https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:com:v4.1', (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    const lines = data.split('\n');
    lines.forEach(line => {
      if (line.includes('인터페이스') || line.includes('interface')) {
        console.log(line);
      }
    });
  });
});
