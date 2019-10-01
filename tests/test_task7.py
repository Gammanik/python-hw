# DO NOT TOUCH THIS FILE!
import unittest

try:
    from src.task7 import verbing, not_bad
except ImportError as e:
    raise unittest.SkipTest("Task 7 is not complete yet")


class Task3Tests(unittest.TestCase):
    def test_verbing(self):
        self.assertEqual("splitly", verbing("spliting"))
        self.assertEqual("verbing", verbing("verb"))
        self.assertEqual("do noting", verbing("do not"))

    def test_not_bad(self):
        self.assertEqual("This is good!", not_bad("This is not that bad!"))