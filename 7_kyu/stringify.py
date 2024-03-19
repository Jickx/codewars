class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    return 'None' if node is None else str(node.data) + ' -> ' + stringify(node.next)


print(stringify(Node(0, Node(1, Node(2, Node(3))))))  # '0 -> 1 -> 2 -> 3 -> None'
print(stringify(None))  # 'None'
print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))
print(stringify(Node(0)))
