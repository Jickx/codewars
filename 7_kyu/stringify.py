class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    if node is None:
        return 'None'
    s = []

    def inner(node, s):
        s.append(str(node.data))
        if node.next is None:
            s.append('None')
        else:
            inner(node.next, s)
        return ' -> '.join(s)
    return inner(node, s)


print(stringify(Node(0, Node(1, Node(2, Node(3))))))  # '0 -> 1 -> 2 -> 3 -> None'
print(stringify(None))  # 'None'
print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))
print(stringify(Node(0)))
