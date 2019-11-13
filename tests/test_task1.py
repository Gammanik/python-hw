import io
import unittest
from contextlib import redirect_stdout
from textwrap import dedent

try:
    from src.task1 import heapify, empty, heap_sort, print_heap, build_heap, extract_last, extract_min
except ImportError as e:
    raise unittest.SkipTest("Task 1 is not complete yet")


class Task1Tests(unittest.TestCase):
    def test_heapify(self):
        self.assertTupleEqual((1, 1, 1), list(heapify(1, empty(), empty()))[0])
        self.assertTupleEqual((1, 2, 2), list(heapify(2, heapify(1, empty(), empty()), empty()))[0])

        heap1 = heapify(3, empty(), empty())
        heap2 = heapify(1, empty(), empty())
        self.assertTupleEqual((2, 1, 1), list(list(heapify(2, heap1, heap2))[2])[0])

    def test_empty(self):
        self.assertListEqual([], list(empty()))

    def test_heap_sort(self):
        self.assertListEqual([], list(heap_sort([])))
        self.assertListEqual([1], list(heap_sort(iter([1]))))
        self.assertListEqual([1, 2], list(heap_sort([2, 1])))
        self.assertListEqual([1, 2, 3], list(heap_sort(iter([2, 1, 3]))))
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7], list(heap_sort(range(7, 0, -1))))

    def test_build_heap(self):
        self.assertEqual("", self.run_print(lambda: print_heap(build_heap([]))))
        self.assertEqual("[1, 1]: 1\n",
                         self.run_print(lambda: print_heap(build_heap([1]))))

        expected = """
        [2, 2]: 1
            [1, 1]: 2
        """

        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(build_heap([2, 1]))))

        expected = """
        [3, 2]: 1
            [1, 1]: 3
            [1, 1]: 2
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(build_heap([3, 1, 2])))
        )

        expected = """
        [3, 2]: 1
            [1, 1]: 2
            [1, 1]: 3
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(build_heap(range(1, 4))))
        )

        expected = """
        [4, 3]: 1
            [2, 2]: 3
                [1, 1]: 4
            [1, 1]: 2
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(build_heap([2, 4, 1, 3])))
        )

        expected = """
        [5, 3]: 1
            [3, 2]: 3
                [1, 1]: 4
                [1, 1]: 5
            [1, 1]: 2
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(build_heap([2, 4, 1, 3, 5])))
        )

    def test_print_heap(self):
        self.assertEqual("", self.run_print(lambda: print_heap(empty())))
        expected = """
        [1, 1]: 1
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(heapify(1, empty(), empty())))
        )

        expected = """
        [2, 2]: 1
            [1, 1]: 2
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(heapify(2, heapify(1, empty(), empty()), empty())))
        )

    def test_extract_last(self):
        last, heap = extract_last(build_heap([]))
        self.assertIsNone(last)
        self.assertEqual("", self.run_print(lambda: print_heap(heap)))

        last, heap = extract_last(build_heap([1]))
        self.assertEqual(1, last)
        self.assertEqual("", self.run_print(lambda: print_heap(heap)))

        last, heap = extract_last(build_heap([2, 1]))
        self.assertEqual(2, last)

        expected = """
        [1, 1]: 1
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(heap))
        )

        last, heap = extract_last(build_heap([3, 1, 2]))
        self.assertEqual(2, last)

        expected = """
        [2, 2]: 1
            [1, 1]: 3
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(heap))
        )

        last, heap = extract_last(build_heap([2, 4, 1, 3, 5]))
        self.assertEqual(5, last)

        expected = """
        [4, 3]: 1
            [2, 2]: 3
                [1, 1]: 4
            [1, 1]: 2
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(heap))
        )

    def test_extract_min(self):
        min_value, heap = extract_min(build_heap([]))
        self.assertIsNone(min_value)
        self.assertEqual("", self.run_print(lambda: print_heap(heap)))

        min_value, heap = extract_min(build_heap([1]))
        self.assertEqual(1, min_value)
        self.assertEqual("", self.run_print(lambda: print_heap(heap)))

        min_value, heap = extract_min(build_heap([2, 1]))
        self.assertEqual(1, min_value)

        expected = """
        [1, 1]: 2
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(heap))
        )

        min_value, heap = extract_min(build_heap([3, 1, 2]))
        self.assertEqual(min_value, 1)

        expected = """
        [2, 2]: 2
            [1, 1]: 3
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(heap))
        )

        min_value, heap = extract_min(build_heap([2, 4, 1, 3, 5]))
        self.assertEqual(1, min_value)
        expected = """
        [4, 3]: 2
            [2, 2]: 3
                [1, 1]: 4
            [1, 1]: 5
        """
        self.assertEqual(
            self.prepare_string(expected),
            self.run_print(lambda: print_heap(heap))
        )

    @staticmethod
    def prepare_string(string_value):
        # remove leading empty lines
        # and dedent leading spaces in every line of multiline string
        return dedent(string_value.lstrip('\n'))

    @staticmethod
    def run_print(call):
        with io.StringIO() as buf, redirect_stdout(buf):
            call()
            return buf.getvalue()
