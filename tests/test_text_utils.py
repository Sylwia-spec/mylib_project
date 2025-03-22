import unittest
from mylib.text_utils import count_words, reverse_text

class TestTextUtils(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words("To jest test"), 3)
        self.assertEqual(count_words("   Python   jest wredny   "), 3)
        self.assertEqual(count_words(""), 0)

    def test_reverse_text(self):
        self.assertEqual(reverse_text("abc"), "cba")
        self.assertEqual(reverse_text(""), "")
