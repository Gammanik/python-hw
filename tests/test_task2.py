# DO NOT TOUCH THIS FILE!
import unittest

try:
    from src.task2 import factory
except ImportError as e:
    raise unittest.SkipTest("Task 2 is not complete yet")


class Task2Tests(unittest.TestCase):
    def test_factory(self):
        res_list = factory(10)
        res_list = [func() for func in res_list]
        expected_list = [*range(10)]
        self.assertLessEqual(res_list, expected_list)
