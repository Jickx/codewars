from unittest import TestCase

from .deep_count import deep_count
from .find_it import find_it


class Test6Kyu(TestCase):
    def test_deep_count(self):
        self.assertEqual(deep_count([]), 0)
        self.assertEqual(deep_count([1, 2, 3]), 3)
        self.assertEqual(deep_count(["x", "y", ["z"]]), 4)
        self.assertEqual(deep_count([1, 2, [3, 4, [5]]]), 7)
        self.assertEqual(deep_count([[[[[[[[[]]]]]]]]]), 8)

    def test_find_it(self):
        self.assertEqual(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
        self.assertEqual(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1)
        self.assertEqual(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5)
        self.assertEqual(find_it([10]), 10)
        self.assertEqual(find_it([10, 10, 10]), 10)
        self.assertEqual(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10)
        self.assertEqual(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1)
