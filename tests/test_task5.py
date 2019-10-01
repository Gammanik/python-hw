# DO NOT TOUCH THIS FILE!
import unittest
import sys
import io
from contextlib import redirect_stdout
from utils import trim_lines


try:
    from src.task5 import main
except ImportError as e:
    raise unittest.SkipTest("Task 5 is not complete yet")


class Task3Tests(unittest.TestCase):
    def test_wc_from_file(self):
        expected = """40 40 280 tests/task4_input1\n"""
        with io.StringIO() as buf, redirect_stdout(buf):
            main(['tests/task4_input1'])
            actual = trim_lines(buf.getvalue())
            self.assertEqual(expected, actual)

    def test_wc_from_files(self):
        expected = """\
        40 40 280 tests/task4_input1
        35 35 140 tests/task4_input3
        40 40 280 tests/task4_input2
        115 115 700 total\n"""
        expected = trim_lines(expected)

        with io.StringIO() as buf, redirect_stdout(buf):
            main(['tests/task4_input1', 'tests/task4_input3', 'tests/task4_input2'])
            actual = trim_lines(buf.getvalue())
            self.assertEqual(expected, actual)

    def test_wc_from_stdin(self):
        inpt = """\
        Jri6Ib
        9taElV
        G2bwD8
        uRWZBk
        PcF7ty
        C0EX6V
        bqmMgG
        262oJd
        QSpBep
        BD8FMv
        HsGR2C
        2Rash5
        No8CYE
        8E4g2t
        yQDbAT
        7lgl5L
        b7wFdJ
        2s4sfj
        mQfQrt
        cvbaUE
        gDF4cQ
        Z5Ly8Z
        73aW7Y
        r3cQ2P
        """
        inpt = trim_lines(inpt)

        expected = """      24      24     168\n"""

        s = io.StringIO(inpt)
        sys.stdin = s
        with io.StringIO() as buf, redirect_stdout(buf):
            main([])
            self.assertEqual(expected, buf.getvalue())
        sys.stdin = sys.__stdin__
