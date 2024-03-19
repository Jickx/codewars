from unittest import TestCase
from .set_reducer import set_reducer
from .sum_nested import sum_nested
from .rice_and_chessboard import squares_needed


class Test7Kyu(TestCase):
    def test_set_reducer(self):
        sample_test_cases = [
            (2, [0, 4, 6, 8, 8, 8, 5, 5, 7]),
            (3, [8, 1, 6, 1, 2, 7, 7, 7, 7, 6, 5, 3, 2, 1, 8]),
            (2, [0, 0, 8, 6, 6, 7, 8, 6, 6, 4, 7, 6, 4, 0, 1, 1, 2, 1, 2, 9, 9, 0, 3, 3, 0, 4]),
            (3, [6, 3, 5, 7, 4, 2, 0, 0, 1, 6, 9, 6, 1, 3, 9, 3, 2]),
            (5, [1, 4, 0, 1, 2, 6, 6, 0, 8, 4, 7, 9, 9, 4, 3, 7, 2, 6, 7, 5, 0, 9, 8]),
            (23, [4, 6, 8, 1, 9, 3, 8, 4, 1, 4, 0, 8, 3, 7, 1, 5, 6, 3, 2, 1, 8, 4, 9]),
            (3, [8, 3, 2, 6, 2, 7, 9, 9, 6, 8, 2, 4, 3, 6, 9, 5, 2, 4, 9]),
            (3, [7, 2, 0, 6, 5, 7, 3, 9, 1, 8, 4, 5, 5, 5, 8, 9, 8, 1, 9, 1, 2, 7, 2, 6, 0, 8, 0, 2]),
            (5, [8, 5, 1, 1, 1, 5, 9, 7, 4, 8, 8, 8, 2, 4, 3, 1, 2, 1, 3, 5, 6, 4]),
            (3, [2, 4, 4, 6, 2, 1, 1, 5, 6, 7, 8, 8, 8, 8, 9, 0, 1, 1, 5, 4, 4]),
        ]

        for expected, inp in sample_test_cases:
            msg = f'set_reducer({inp})'
            self.assertEqual(set_reducer(inp), expected, msg)

    def test_sum_nested(self):
        self.assertEqual(sum_nested([1]), 1)
        self.assertEqual(sum_nested([1, 2, 3, 4]), 10)
        self.assertEqual(sum_nested(list(range(11))), 55)

        self.assertEqual(sum_nested([]), 0)

        self.assertEqual(sum_nested([[1], []]), 1)
        self.assertEqual(sum_nested([[1, 2, 3, 4]]), 10)

        self.assertEqual(sum_nested([[], []]), 0)

        self.assertEqual(sum_nested([1, [1], [[1]], [[[1]]]]), 4)
        self.assertEqual(sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]), 8)

        self.assertEqual(sum_nested([[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []]), 0)

    def test_rice_and_chessboard(self):
        self.assertEqual(squares_needed(0), 0)
        self.assertEqual(squares_needed(1), 1)
        self.assertEqual(squares_needed(2), 2)
        self.assertEqual(squares_needed(3), 2)
        self.assertEqual(squares_needed(4), 3)
        self.assertEqual(squares_needed(349793859), 29)
