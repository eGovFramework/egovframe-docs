const fs = require('fs');
let content = fs.readFileSync('common-component/elementary-technology/calendar.md', 'utf8');
content = content.replace(/\|([^|\n]+)\|/g, (match) => {
    return match; // Actually, maybe prettier is better
});
