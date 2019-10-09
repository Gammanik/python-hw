# DO NOT TOUCH THIS FILE!
import unittest

try:
    from src.task6 import *
except ImportError as e:
    raise unittest.SkipTest("Task 6 is not complete yet")


class Tas6Tests(unittest.TestCase):
    def test_null(self):
        self.assertTrue(null(Nil()))
        self.assertFalse(null(Cons(0, Nil())))

    def test_fromseq(self):
        self.assertEqual(Nil(), fromseq([]))
        self.assertEqual(Nil(), fromseq(tuple()))
        self.assertEqual(Cons(car=1, cdr=Cons(car=2, cdr=Cons(car=3, cdr=Nil()))), fromseq([1, 2, 3]))

    def test_head(self):
        self.assertEqual(1, head(fromseq([1, 2, 3])))
        with self.assertRaises(AttributeError):
            head(Nil())

    def test_tail(self):
        self.assertEqual(Cons(car=2, cdr=Cons(car=3, cdr=Nil())),
                         tail(fromseq([1, 2, 3])))

        with self.assertRaises(AttributeError):
            tail(fromseq([]))

    def test_foldr(self):
        self.assertEqual(0, foldr(lambda x, y: x + y, 0, Nil()))
        self.assertEqual(8, foldr(lambda x, y: x + y, 2, fromseq([1, 2, 3])))
        self.assertEqual(1, foldr(lambda x, y: x - y, 1, fromseq([3, 2, 1])))

    def test_foldl(self):
        self.assertEqual(0, foldl(lambda x, y: x + y, 0, Nil()))
        self.assertEqual(8, foldl(lambda x, y: x + y, 2, fromseq([1, 2, 3])))
        self.assertEqual(-5, foldl(lambda x, y: x - y, 1, fromseq([3, 2, 1])))

    def test_length(self):
        self.assertEqual(0, length(Nil()))
        self.assertEqual(2, length(fromseq((1, 2))))

    def test_to_list(self):
        self.assertListEqual([], tolist(Nil()))
        self.assertListEqual([1], tolist(Cons(1, Nil())))
        self.assertListEqual([1, 2, 3], tolist(fromseq([1, 2, 3])))

    def test_map_(self):
        self.assertListEqual([], tolist(map_(lambda x: x, Nil())))
        self.assertListEqual([1, 2, 3], tolist(map_(lambda x: x, fromseq([1, 2, 3]))))
        self.assertListEqual(['10', '20', '30'], tolist(map_(lambda x: str(x) + '0', fromseq([1, 2, 3]))))

    def test_append(self):
        self.assertEqual(Nil(), append(Nil(), fromseq([])))
        self.assertEqual(Cons(car=0, cdr=Cons(car=1, cdr=Nil())), append(Nil(), Cons(0, Cons(1, Nil()))))
        self.assertEqual(Cons(car=1, cdr=Nil()), append(fromseq([1]), Nil()))
        self.assertEqual(Cons(car=1, cdr=Cons(car=2, cdr=Cons(car=3, cdr=Nil()))),
                         append(fromseq([1, 2]), fromseq([3])))

    def test_filter(self):
        self.assertEqual(filter_(lambda x: True, Nil()), Nil())
        self.assertEqual([1, 2], tolist(filter_(lambda x: True, fromseq([1, 2]))))
        self.assertEqual([], tolist(filter_(lambda x: False, fromseq([1, 2]))))
        self.assertEqual([0, 2, 4], tolist(filter_(lambda x: x % 2 == 0, fromseq(range(5)))))

    def test_reverse(self):
        self.assertEqual(reverse(Nil()), Nil())
        self.assertEqual(tolist(reverse(fromseq(range(2)))), [1, 0])
        self.assertEqual(tolist(reverse(fromseq(range(3)))), [2, 1, 0])

    def test_elem(self):
        self.assertFalse(elem(10, Nil()))
        self.assertFalse(elem(5, fromseq(range(5))))
        self.assertTrue(elem(5, fromseq(range(10))))
