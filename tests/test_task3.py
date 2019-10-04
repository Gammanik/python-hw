# DO NOT TOUCH THIS FILE!
import unittest
import sys
import io
from contextlib import redirect_stdout

try:
    from src.task3 import main, nl_from_file, nl_from_stdin
except ImportError as e:
    raise unittest.SkipTest("Task 3 is not complete yet")


class Task3Tests(unittest.TestCase):
    @staticmethod
    def __trim_lines(lines):
        return '\n'.join([
            line.lstrip() for line in lines.split('\n')
        ])

    def test_nl_from_file(self) -> None:
        expected = """\
         1\tddd
         2\taaa
         3\t10
         4\t30
         5\taaa
         6\t
         7\t
         8\t
         9\t
        10\t
        11\t
        12\t
        13\t28
        14\t30\n"""
        expected = self.__trim_lines(expected)

        with io.StringIO() as buf, redirect_stdout(buf):
            nl_from_file("tests/task3_input")
            actual = self.__trim_lines(buf.getvalue())
            self.assertEqual(expected, actual)

    def test_nl_from_stdin(self):
        inp = """\
        2  0
        30
        asdf
        foo
        aa
        fdfadsf
        asdfasdf"""

        expected = """\
        1\t2  0
        2\t30
        3\tasdf
        4\tfoo
        5\taa
        6\tfdfadsf
        7\tasdfasdf
"""
        expected = self.__trim_lines(expected)

        s = io.StringIO(inp)
        sys.stdin = s
        with io.StringIO() as buf, redirect_stdout(buf):
            nl_from_stdin()
            actual = self.__trim_lines(buf.getvalue())
            self.assertEqual(expected, actual)

    def test_too_many_arguments(self):
        self.assertRaises(ValueError, main, ["file1.txt", "file1.txt", "file1.txt"])
