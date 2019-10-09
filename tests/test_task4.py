# DO NOT TOUCH THIS FILE!
import unittest

try:
    from src.task4 import lcm
except ImportError as e:
    raise unittest.SkipTest("Task 4 is not complete yet")


class Task4Tests(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(60.0, lcm(10, 20, 30))

    def test_case2(self):
        with self.assertRaises(TypeError):
            lcm()

    def test_case3(self):
        self.assertEqual(6, lcm(2, 3))