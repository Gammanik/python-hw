# DO NOT TOUCH THIS FILE!
import unittest
import sys
import io
from contextlib import redirect_stdout
from utils import trim_lines

try:
    from src.task4 import main, tail_from_files, tail_from_stdin
except ImportError as e:
    raise unittest.SkipTest("Task 4 is not complete yet")


class Task3Tests(unittest.TestCase):
    def test_nl_from_file(self):
        expected = """VIWeIb
        K4Xbwa
        4Brlss
        Ll1h2v
        ckpVC5
        jVMgDk
        TLzWDc
        CH5p2W
        ZbPuk4
        yuTRNf
        """
        expected = trim_lines(expected)

        with io.StringIO() as buf, redirect_stdout(buf):
            tail_from_files(['tests/task4_input1'])
            actual = buf.getvalue()
            self.assertEqual(expected, actual)

    def tests_nl_from_many_files1(self):
        expected = """==> tests/task4_input1 <==
        VIWeIb
        K4Xbwa
        4Brlss
        Ll1h2v
        ckpVC5
        jVMgDk
        TLzWDc
        CH5p2W
        ZbPuk4
        yuTRNf
        ==> tests/task4_input3 <==
        Q8X
        Gv8
        8Rj
        KXq
        Mo0
        ARW
        4hb
        qmf
        zJe
        MXl
        ==> tests/task4_input2 <==
        r3cQ2P
        uCRueP
        zmtsWo
        PfiUQn
        ExeZjD
        GJRsyF
        jzkDNx
        P7tmcM
        4N5gCx
        olmFGM
        """
        expected = trim_lines(expected)

        with io.StringIO() as buf, redirect_stdout(buf):
            tail_from_files(['tests/task4_input1', 'tests/task4_input3', 'tests/task4_input2'])
            actual = buf.getvalue()
            self.assertEqual(expected, actual)

    def test_tail_from_stdin(self) -> None:
        inpt = """Jri6Ib
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

        expected = """\
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
        expected = trim_lines(expected)

        s = io.StringIO(inpt)
        sys.stdin = s
        with io.StringIO() as buf, redirect_stdout(buf):
            tail_from_stdin()
            self.assertEqual(expected, buf.getvalue())
        sys.stdin = sys.__stdin__
