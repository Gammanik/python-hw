# DO NOT TOUCH THIS FILE!
import unittest

try:
    from src.task1 import remove_adjacent, linear_merge
except ImportError as e:
    raise unittest.SkipTest("Task 1 is not complete yet")


class Task1Tests(unittest.TestCase):
    def test_remove_adjacent_1(self):
        test_input = [1, 2, 2, 3]
        expected = [1, 2, 3]

        self.assertListEqual(remove_adjacent(test_input), expected)

    def test_remove_adjacent_2(self):
        test_input = [9, 9, 1, 9, 9, 2, 3, 2, 2, 3, 1]
        expected = [9, 1, 9, 2, 3, 2, 3, 1]

        self.assertListEqual(remove_adjacent(test_input), expected)

    def test_linear_merge_1(self):
        first, second = [2, 4, 6], [1, 3, 5]

        self.assertListEqual(linear_merge(first, second), [1, 2, 3, 4, 5, 6])
