import unittest
from functools import lru_cache

try:
    from src.task2 import cached
except ImportError as e:
    raise unittest.SkipTest("Task 2 is not complete yet")


class Task2Tests(unittest.TestCase):
    def test_case1(self):
        count_calls = 0

        @cached
        def foo(default_val=42):
            nonlocal count_calls
            count_calls += 1
            return default_val

        foo()
        foo(42)
        foo()
        self.assertEqual(1, count_calls)

    def test_cache_size_10(self):
        var1 = 5

        @cached(cache_size=10)
        def foo1(arg1, arg2=42):
            nonlocal var1
            var1 *= arg1

        var2 = 5

        @lru_cache(maxsize=10)
        def foo2(arg1, arg2=42):
            nonlocal var2
            var2 *= arg1

        for i in range(0, 13, 2):
            foo1(i)
            foo2(i)

        for i in range(13, 0, -2):
            foo1(i)
            foo2(i)

        self.assertEqual(var2, var1)

    def test_cache_size_zero(self):
        var = 0

        @cached(cache_size=0)
        def foo():
            nonlocal var
            var += 1

        foo()
        foo()
        foo()
        foo()
        foo()
        self.assertEqual(5, var)

    def test_no_arguments(self):
        calls_count = 0

        @cached(cache_size=1)
        def f():
            nonlocal calls_count
            calls_count += 1

        f()
        f()
        f()
        f()
        f()
        self.assertEqual(1, calls_count)
