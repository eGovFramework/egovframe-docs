import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name('docs_lint.py')


class DocsLintInlineCodeTest(unittest.TestCase):
    def lint(self, content, files=(), source=False, test_classes=()):
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
                for name in test_classes:
                    sample = root / 'src/test/java/egovframework/example' / (name + '.java')
                    sample.parent.mkdir(parents=True, exist_ok=True)
                    sample.write_text('package egovframework.example; class %s {}' % name, encoding='utf-8')
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

    def source_rules(self, content, test_classes=()):
        return [(item['rule'], item['msg']) for item in self.lint(content, source=True, test_classes=test_classes)
                if item['rule'].startswith('L5')]

    def test_class_only_in_test_sources_is_informational_not_missing(self):
        rules = self.source_rules('`egovframework.example.SampleVO`', test_classes=['SampleVO'])
        self.assertEqual([('L5-test', '테스트 소스(src/test/java)에만 있는 클래스: egovframework.example.SampleVO')], rules)

    def test_class_nowhere_is_still_reported_as_missing(self):
        rules = self.source_rules('`egovframework.example.NoSuchClass`', test_classes=['SampleVO'])
        self.assertEqual([('L5', '실소스 부재 참조: egovframework.example.NoSuchClass')], rules)

    def test_class_in_main_sources_is_clean(self):
        self.assertEqual([], self.source_rules('`egovframework.example.Existing`', test_classes=['SampleVO']))

    def test_test_only_class_does_not_hide_a_main_lookup_without_main_sources(self):
        # --src 가 test 소스만 가진 경우에도 테스트 전용 클래스는 L5-test 로 구분된다
        rules = self.source_rules('`egovframework.example.OnlyTest`', test_classes=['OnlyTest'])
        self.assertEqual(['L5-test'], [rule for rule, _ in rules])


if __name__ == '__main__':
    unittest.main()
