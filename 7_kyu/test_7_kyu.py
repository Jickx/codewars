from unittest import TestCase
from .sum_nested import sum_nested
from .rice_and_chessboard import squares_needed
from .find_max_tree_node import TreeNode, find_max
from .stringify import Node, stringify


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

    def test_max_tree_node(self):
        tree_is_leaf = TreeNode(-3)
        self.assertEqual(find_max(tree_is_leaf), -3)

        tree_with_left = TreeNode(2, TreeNode(1))
        self.assertEqual(find_max(tree_with_left), 2)

        tree_with_right = TreeNode(5, None, TreeNode(0))
        self.assertEqual(find_max(tree_with_right), 5)

        tree_with_duplicates = TreeNode(1010, TreeNode(-2, TreeNode(100), TreeNode(1010, None, TreeNode(-101))),
                                        TreeNode(-2, TreeNode(99)))
        self.assertEqual(find_max(tree_with_duplicates), 1010)

        all_duplicates = TreeNode(-3, TreeNode(-3, TreeNode(-3, None), TreeNode(-3)),
                                  TreeNode(-3, None, TreeNode(-3, TreeNode(-3))))
        self.assertEqual(find_max(all_duplicates), -3)

        perfect_tree = TreeNode(11, TreeNode(4, TreeNode(100), TreeNode(1)),
                                TreeNode(-2, TreeNode(99), TreeNode(-101)))
        self.assertEqual(find_max(perfect_tree), 100)

        unbalanced_tree = TreeNode(54, TreeNode(4, TreeNode(-10, TreeNode(2, None, TreeNode(9)), TreeNode(45)),
                                                TreeNode(1)))
        self.assertEqual(find_max(unbalanced_tree), 54)  # Max at root

        all_negatives = TreeNode(-5, TreeNode(-4, TreeNode(-6), TreeNode(-2)),
                                 TreeNode(-9, TreeNode(-45, None, TreeNode(-1))))
        self.assertEqual(find_max(all_negatives), -1)  # Max at last node

    def test_stringify(self):
        self.assertEqual(stringify(Node(0, Node(1, Node(2, Node(3))))), '0 -> 1 -> 2 -> 3 -> None')
        self.assertEqual(stringify(None), 'None')
        self.assertEqual(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))),
                         '0 -> 1 -> 4 -> 9 -> 16 -> None')
