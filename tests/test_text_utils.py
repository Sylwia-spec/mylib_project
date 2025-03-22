import unittest
from mylib.text_utils import is_palindrome

class TestTextUtils(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Kajak"))
        self.assertTrue(is_palindrome("Ala ma kota, a taK om a la"))
        self.assertFalse(is_palindrome("Python"))
