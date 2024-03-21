from unittest import TestCase

from .deep_count import deep_count


class Test6Kyu(TestCase):
    def test_deep_count(self):
        self.assertEqual(deep_count([]), 0)
        self.assertEqual(deep_count([1, 2, 3]), 3)
        self.assertEqual(deep_count(["x", "y", ["z"]]), 4)
        self.assertEqual(deep_count([1, 2, [3, 4, [5]]]), 7)
        self.assertEqual(deep_count([[[[[[[[[]]]]]]]]]), 8)
