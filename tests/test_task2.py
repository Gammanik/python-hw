# DO NOT TOUCH THIS FILE!
import unittest

try:
    from src.task2 import matrix_product, matrix_pretty_print
except ImportError as e:
    raise unittest.SkipTest("Task 1 is not complete yet")


class Task2Tests(unittest.TestCase):
    def test_matrix_product(self):
        mat1 = [[1, 3, 2], [0, 4, -1]]
        mat2 = [[2, 0, -1, 111], [3, -2, 1, 2], [0, 1, 2, 3]]
        result = matrix_product(mat1, mat2)
        expected = [[11, -4, 6, 123], [12, -9, 2, 5]]

        self.assertCountEqual(result, expected)
        for row1, row2 in zip(result, expected):
            self.assertListEqual(row1, row2)
