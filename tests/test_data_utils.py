import unittest
from mylib.data_utils import flatten_list

class TestDataUtils(unittest.TestCase):
    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(flatten_list([[]]), [])
        self.assertEqual(flatten_list([["a"], ["b", "c"]]), ["a", "b", "c"])
