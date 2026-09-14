import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name('docs_lint.py')


class DocsLintInlineCodeTest(unittest.TestCase):
    def lint(self, content, files=(), source=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / 'docs'
            docs.mkdir()
            (docs / 'README.md').write_text(content, encoding='utf-8')
            for name in files:
                (docs / name).write_text('# Target\n', encoding='utf-8')
            command = [sys.executable, str(SCRIPT), str(docs), '--json']
            if source:
                java = root / 'src/main/java/example/Existing.java'
                java.parent.mkdir(parents=True)
                java.write_text('package example; class Existing {}', encoding='utf-8')
                command.extend(['--src', str(root / 'src')])
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return json.loads(result.stdout)['findings']

    def broken_links(self, content, files=()):
        return [item['msg'] for item in self.lint(content, files) if item['rule'] == 'L2']

    def test_real_links_are_still_checked(self):
        findings = self.broken_links('[정상](target.md) [누락](missing.md)', ['target.md'])
        self.assertEqual(['상대링크 대상 부재: missing.md'], findings)

    def test_inline_link_and_image_examples_are_ignored(self):
        content = '`[이름](missing.md)`와 `![이미지](missing.png)` [실제](real.md)'
        self.assertEqual(['상대링크 대상 부재: real.md'], self.broken_links(content))

    def test_matching_backtick_runs_and_unmatched_delimiters(self):
        content = '``예시 ` [이름](example.md) ``와 `닫히지 않은 [실제](real.md)'
        self.assertEqual(['상대링크 대상 부재: real.md'], self.broken_links(content))

    def test_code_in_link_label_does_not_hide_the_link(self):
        self.assertEqual(['상대링크 대상 부재: missing.md'],
                         self.broken_links('[`코드`](missing.md)'))

    def test_escaped_backticks_and_fenced_code(self):
        content = '\\`[실제](real.md)\\`\n\n```markdown\n[예시](example.md)\n```\n'
        self.assertEqual(['상대링크 대상 부재: real.md'], self.broken_links(content))

    def test_class_references_in_inline_code_are_still_checked(self):
        findings = self.lint('`egovframework.example.EgovMissing`', source=True)
        self.assertIn('L5', [item['rule'] for item in findings])


if __name__ == '__main__':
    unittest.main()
