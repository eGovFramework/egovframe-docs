import re

with open("common-component/elementary-technology/print.md", "r") as f:
    content = f.read()

# Fix headings newlines
content = re.sub(r'([^\n])\n(#+ .*)', r'\1\n\n\2', content)

# Fix lists newlines
content = re.sub(r'([^\n])\n(- .*)', r'\1\n\n\2', content)

# Fix trailing newline
if not content.endswith('\n'):
    content += '\n'

with open("common-component/elementary-technology/print.md", "w") as f:
    f.write(content)
