import io
import unittest
from contextlib import redirect_stdout
from textwrap import dedent


try:
    from src.task3 import contextmanager
except ImportError as e:
    raise unittest.SkipTest("Task 3 is not complete yet")


@contextmanager
def foo():
    print("__enter__")
    try:
        yield 42
    except Exception as e:
        print(type(e))
        print(str(e))
    finally:
        print("__exit__")
    return


class Task3Tests(unittest.TestCase):
    @staticmethod
    def prepare_string(string_value):
        # remove leading empty lines
        # and dedent leading spaces in every line of multiline string
        return dedent(string_value.lstrip('\n'))

    def test_simple_case(self):
        expected = """
        __enter__
        42
        <class 'ValueError'>
        OOOPS
        __exit__
        """

        with io.StringIO() as buf, redirect_stdout(buf):
            with foo() as i:
                print(i)
                raise ValueError("OOOPS")
            res = buf.getvalue()
        self.assertEqual(self.prepare_string(expected), res)
