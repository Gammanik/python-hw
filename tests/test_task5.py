import unittest

try:
    from src.task5 import register, depends_on
except ImportError as e:
    raise unittest.SkipTest("Task 5 is not complete yet")


class Task5Tests(unittest.TestCase):
    def test_only_register(self):
        @register
        def foo():
            return 50

        self.assertEqual(foo(), 50)

    def test_flat_dependencies(self):
        var1 = 0
        var2 = 0
        var3 = 0

        @register
        def foo1():
            nonlocal var1
            var1 += 10
            print("foo1 ", var1)

        @depends_on(["foo1"])
        def foo2():
            nonlocal var2
            nonlocal var1
            var2 = var1 * 5
            print("foo2 ", var2)

        @depends_on(['foo1', 'foo2'])
        def foo3():
            nonlocal var3
            var3 = 1
            print("foo3 ", var3)

        foo3()
        self.assertEqual(var1, 20)
        self.assertEqual(var2, 100)
        self.assertEqual(var3, 1)

    def test_cycle_dependencies(self):
        @register
        def foo1():
            return 42

        @depends_on(["foo4"])
        def foo2():
            return 43

        @depends_on(["foo2"])
        def foo3():
            return 44

        @depends_on(["foo1", "foo3"])
        def foo4():
            return 45

        with self.assertRaises(Exception) as context:
            foo4()
