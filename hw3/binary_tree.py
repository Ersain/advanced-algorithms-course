class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.value = val


class BinaryTree:
    def __init__(self):
        self.root: Node = None

    def __add_value(self, current: Node, value: int):
        if current is None:
            return Node(value)
        if value < current.value:
            current.left = self.__add_value(current.left, value)
        elif value > current.value:
            current.right = self.__add_value(current.right, value)
        else:
            return current
        return current

    def __contains_value(self, current: Node, value: int):
        if current is None:
            return False
        if value == current.value:
            return True
        return self.__contains_value(current.left, value) \
            if value < current.value \
            else self.__contains_value(current.right, value)

    def __find_smallest_value(self, root: Node):
        """Helper function for deleting"""
        return root.value if root.left is None else self.__find_smallest_value(root.left)

    def __delete_value(self, current: Node, value: int):
        if current is None:
            return None

        if value < current.value:
            current.left = self.__delete_value(current.left, value)
            return current
        if value > current.value:
            current.right = self.__delete_value(current.right, value)
            return current.right

        if current.left is None and current.right is None:
            """If a node is a leaf"""
            return None
        if current.left is None:
            """If there is no left child"""
            return current.right
        if current.right is None:
            """If there is no right child"""
            return current.left
        """If there are both"""
        smallest_value = self.__find_smallest_value(current.right)
        current.value = smallest_value
        current.right = self.__delete_value(current.right, smallest_value)
        return current

    def add(self, value: int) -> None:
        self.root = self.__add_value(self.root, value)

    def delete(self, value: int) -> None:
        self.root = self.__delete_value(self.root, value)

    def contains(self, item):
        return self.__contains_value(self.root, item)


b = BinaryTree()
b.add(24)
b.add(4)
b.add(30)
b.add(7)
b.add(3)
b.add(100)

assert b.contains(24) is True
assert b.contains(25) is False

b.delete(4)
assert b.contains(3) is True
assert b.contains(7) is True
assert b.contains(4) is False

b.delete(30)
assert b.contains(100) is True
assert b.contains(30) is False
