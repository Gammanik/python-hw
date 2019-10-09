# DO NOT TOUCH THIS FILE!
import unittest
import sys
import io
from contextlib import redirect_stdout

try:
    from src.task3 import union
except ImportError as e:
    raise unittest.SkipTest("Task 3 is not complete yet")


class Task3Tests(unittest.TestCase):
    def test_union(self):
        self.assertSetEqual(union({1, 2, 10}, set(), {3, 5}), {1, 2, 3, 5, 10})