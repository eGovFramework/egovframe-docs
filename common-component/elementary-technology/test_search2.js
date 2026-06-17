const https = require('https');
const url = 'https://www.egovframe.go.kr/wiki/doku.php?do=search&id=' + encodeURIComponent('인터페이스');
https.get(url, (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => {
    const matches = data.match(/egovframework:com:[^"]+/g);
    if(matches) {
       console.log(Array.from(new Set(matches)).join('\n'));
    } else {
       console.log("no matches");
    }
  });
});
