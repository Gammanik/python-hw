# DO NOT TOUCH THIS FILE!
import unittest

try:
    from src.task5 import compose
except ImportError as e:
    raise unittest.SkipTest("Task 5 is not complete yet")


class Task5Tests(unittest.TestCase):
    def test_task5(self):
        f = compose(lambda x: 2 * x, lambda x: x + 1, lambda x: x % 9)
        self.assertEqual(14, f(42))