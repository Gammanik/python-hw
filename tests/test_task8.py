# DO NOT TOUCH THIS FILE!
import unittest

try:
    from src.task8 import primes
except ImportError as e:
    raise unittest.SkipTest("Task 8 is not complete yet")


class Task8Tests(unittest.TestCase):
    def test_primes1(self):
        self.assertListEqual([], primes(0))

    def test_primes2(self):
        self.assertListEqual([2, 3, 5, 7], primes(10))

    def test_primes3(self):
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37],
                            primes(40))
