# DO NOT TOUCH THIS FILE!
import unittest
import io
from collections import OrderedDict
from contextlib import redirect_stdout
from utils import trim_lines

try:
    from src.task6 import main, parse_dictionary, print_dictionary, reverse_dictionary
except ImportError as e:
    raise unittest.SkipTest("Task 6 is not complete yet")


class Task3Tests(unittest.TestCase):
    def test_print_dict(self):
        input_dict = OrderedDict([
            ('apple', ['malum', 'pomum', 'popula']),
            ('fruit', ['baca', 'bacca', 'popum']),
            ('punishment', ['malum', 'multa'])
        ])

        expected = """\
        apple - malum, pomum, popula
        fruit - baca, bacca, popum
        punishment - malum, multa\n"""
        expected = trim_lines(expected)

        with io.StringIO() as buf, redirect_stdout(buf):
            print_dictionary(input_dict)
            self.assertEqual(expected, buf.getvalue())

    def test_parse_dictionary(self):
        input_text = """\
        apple - malum, pomum, popula
        fruit - baca, bacca, popum
        punishment - malum, multa\n"""
        input_text = trim_lines(input_text)

        expected = {
            'apple': ['malum', 'pomum', 'popula'],
            'fruit': ['baca', 'bacca', 'popum'],
            'punishment': ['malum', 'multa']
        }
        result = parse_dictionary(input_text)

        self.assertDictEqual(result, expected)
        for key, value in expected.items():
            self.assertTrue(key in result)
            self.assertSetEqual(set(expected[key]), set(result[key]))

    def test_reverse_dictionary1(self):
        input_dict = {
            'apple': ['malum', 'pomum', 'popula'],
            'fruit': ['baca', 'bacca', 'popum'],
            'punishment': ['malum', 'multa']
        }

        output_dict = {
            'baca': ['fruit'],
            'bacca': ['fruit'],
            'malum': ['apple', 'punishment'],
            'multa': ['punishment'],
            'pomum': ['apple'],
            'popula': ['apple'],
            'popum': ['fruit']
        }
        result = reverse_dictionary(input_dict)

        self.assertDictEqual(output_dict, result)
        for key, value in output_dict.items():
            self.assertTrue(key in result)
            self.assertSetEqual(set(output_dict[key]), set(result[key]))
