class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    return 'None' if node is None else str(node.data) + ' -> ' + stringify(node.next)
