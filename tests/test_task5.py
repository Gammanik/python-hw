import unittest

try:
    from src.task5 import context_decorator
except ImportError as e:
    raise unittest.SkipTest("Task 5 is not complete yet")


class Task5Tests(unittest.TestCase):
    def test_simple_case(self):
        a = 0
        b = 0
        c = 0

        @context_decorator
        class CounterContext:
            def __enter__(self):
                nonlocal a
                a += 1

            def __exit__(self, exc_type, exc_val, exc_tb):
                nonlocal c
                c += 1
                return True

        @CounterContext()
        def foo():
            nonlocal b
            b += 1

        self.assertEqual((a, b, c), (0, 0, 0))
        foo()
        self.assertEqual((a, b, c), (1, 1, 1))

        with CounterContext():
            pass

        self.assertEqual((a, b, c), (2, 1, 2))

        with CounterContext():
            foo()

        self.assertEqual((a, b, c), (4, 2, 4))

    def test_with_return(self):
        @context_decorator
        class CounterContext:
            def __enter__(self):
                pass

            def __exit__(self, exc_type, exc_val, exc_tb):
                pass

        a = 0

        @CounterContext()
        def returnee():
            nonlocal a
            a += 5
            return a

        self.assertEqual(returnee(), 5)
        self.assertEqual(returnee(), 10)
