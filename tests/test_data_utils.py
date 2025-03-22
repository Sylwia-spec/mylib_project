import unittest
from mylib.data_utils import filter_even, average_list, count_words

class TestDataUtils(unittest.TestCase):

    def test_filter_even(self):
        self.assertEqual(filter_even([1, 2, 3, 4]), [2, 4])
        self.assertEqual(filter_even([1, 3, 5]), [])

    def test_average_list(self):
        self.assertAlmostEqual(average_list([1, 2, 3]), 2.0)
        with self.assertRaises(ValueError):
            average_list([])

    def test_count_words(self):
        self.assertEqual(count_words("Ala ma kota"), 3)
        self.assertEqual(count_words(""), 0)
