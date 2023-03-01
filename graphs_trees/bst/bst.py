class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)


class Bst(object):

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if self.root is not None:
            return self._insert(self.root, data)
        self.root = Node(data)
        return self.root

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is not None:
                return self._insert(node.left, data)
            node.left = self._insert(node.left, data)
            node.left.parent = node
            return node.left
        elif node.right is None:
            node.right = self._insert(node.right, data)
            node.right.parent = node
            return node.right
        else:
            return self._insert(node.right, data)
