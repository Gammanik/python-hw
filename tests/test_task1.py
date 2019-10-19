import typing
import unittest

try:
    from src.task1 import typed
except ImportError as e:
    raise unittest.SkipTest("Task 1 is not complete yet")


class Task1Tests(unittest.TestCase):
    def test_one_parameter(self):
        @typed
        def foo(arg1: int) -> int:
            return arg1

        self.assertEqual(42, foo(42))
        self.assertRaises(TypeError, lambda: foo(str(42)))

    def test_few_parameters(self):
        @typed
        def foo(arg1: int, arg2: str, arg3: float) -> str:
            return str(arg1) + arg2 + str(arg3)

        self.assertEqual('33hello0.5', foo(33, 'hello', 0.5))
        self.assertRaises(TypeError, lambda: foo('33', 'hello', 0.5))

    def test_new_type(self):
        NewType = typing.NewType('NewType', int)
        NewType2 = typing.NewType('NewType2', NewType)

        @typed
        def foo(arg1: NewType2):
            return arg1

        self.assertEqual(42, foo(42))
        self.assertRaises(TypeError, lambda: foo(str(42)))

    def test_generic(self):
        @typed
        def foo(arg1: typing.List[int]):
            pass

        print("REMOVE THIS TEST IF YOU IMPLEMENTED GENERIC SUPPORT")
        self.assertRaises(NotImplementedError, lambda: foo(['aa', 0.5]))
