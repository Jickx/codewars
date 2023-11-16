from permutations import permutations
import unittest


class TestPermutations(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sorted(permutations('a')), ['a']);
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
