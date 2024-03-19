class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def find_max(root):
    result = root.value
    if root.right:
        result = max(result, find_max(root.right))
    if root.left:
        result = max(result, find_max(root.left))
    return result


perfect_tree = TreeNode(11, TreeNode(4, TreeNode(100), TreeNode(1)),
                        TreeNode(-2, TreeNode(99), TreeNode(-101)))
print(find_max(perfect_tree))  # 100
