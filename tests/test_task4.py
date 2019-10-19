import io
import unittest
from contextlib import redirect_stdout

try:
    from src.task4 import trace_if
except ImportError as e:
    raise unittest.SkipTest("Task 4 is not complete yet")


class Task4Tests(unittest.TestCase):
    def test_div(self):
        @trace_if(lambda x, y, **kwargs: kwargs.get("integral"))
        def div(x, y, integral=False):
            return x // y if integral else x / y

        with io.StringIO() as buf, redirect_stdout(buf):
            div(4, 2)
            div(4, 2, integral=True)
            self.assertEqual("div (4, 2) {'integral': True}\n", buf.getvalue())
