import unittest

try:
    from src.task3 import n_times
except ImportError as e:
    raise unittest.SkipTest("Task 3 is not complete yet")


class Task2Tests(unittest.TestCase):
    def test_foo(self):
        res = -1
        pow = 0

        @n_times(4)
        def foo():
            nonlocal res
            nonlocal pow
            pow += 1
            res = 3 ** pow

        foo()
        self.assertEqual(pow, 4)
        self.assertEqual(res, 81)
