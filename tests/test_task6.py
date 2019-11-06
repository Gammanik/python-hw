import unittest

try:
    from src.task6 import Storage
except ImportError as e:
    raise unittest.SkipTest("Task 6 is not complete yet")


class Task6Tests(unittest.TestCase):

    def test_commit(self):
        s = Storage()
        with s.edit() as se:
            se['s'] = 283

        self.assertEqual(s['s'], 283)

    def test_rollback(self):
        s = Storage()
        try:
            with s.edit() as se:
                se['a'] = 1
                raise Exception("Transaction rollback")
        except Exception:
            pass

        self.assertRaises(KeyError, lambda: s['a'])

    def test_delete_commit(self):
        s = Storage()
        with s.edit() as se:
            se['a'] = 1
            se['b'] = 2
            se['c'] = 3
        with s.edit() as se:
            del se['a']
            del se['b']
            del se['c']

        self.assertRaises(KeyError, lambda: s['a'])
        self.assertRaises(KeyError, lambda: s['b'])
        self.assertRaises(KeyError, lambda: s['c'])

    def test_delete_rollback(self):
        s = Storage()
        with s.edit() as se:
            se['a'] = 1
            se['b'] = 2
            se['c'] = 3
        try:
            with s.edit() as se:
                del se['a']
                del se['b']
                raise RuntimeWarning("Transaction rollback")
        except RuntimeWarning:
            pass

        self.assertEqual(s['a'], 1)
        self.assertEqual(s['b'], 2)
        self.assertEqual(s['c'], 3)

    def test_security(self):
        s = Storage()
        with s.edit() as se:
            se['not'] = 200

        self.assertEqual(s['not'], 200)

        def assign():
            s['bad'] = 200

        def delete():
            del s['not']

        self.assertRaises(TypeError, assign)
        self.assertRaises(TypeError, delete)
