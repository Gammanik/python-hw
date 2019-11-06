import unittest

try:
    from src.task3 import implicit_int
except ImportError as e:
    raise unittest.SkipTest("Task 3 is not complete yet")


class Task3Tests(unittest.TestCase):
    def test_simple_case(self):
        @implicit_int
        class A:
            k = -9

        a = A()
        self.assertEqual(a.e + a.k + 589, 580)
