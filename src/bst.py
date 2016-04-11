from collections import deque


class Tree(object):
    """Single class implementation of BST."""

    def __init__(self, data, parent=None):
        """Initialize."""
        try:
            self.left = None
            self.right = None
            self.parent = None
            self.data = data
            self.__size = 1
        except TypeError:
            return("Please plant a root ex. 'Tree(10)'")

    @property
    def left(self):
        """Left child."""
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        if node is not None:
            node.parent = self

    @property
    def right(self):
        """Right child."""
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        if node is not None:
            node.parent = self

    def insert(self, data):
        """Insert data into tree."""
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data=data, parent=self)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data=data, parent=self)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        self.__size += 1

    def contains(self, data):
        """Check tree for data."""
        try:
            if self.data:
                if data < self.data:
                    if self.left.data and data == self.left.data:
                        print("True")
                        return True
                    else:
                        self.left.contains(data)
                elif data > self.data:
                    if self.right.data and data == self.right.data:
                        print("True")
                        return True
                    else:
                        self.right.contains(data)
                elif data == self.data:
                    print("True")
                    return True
        except AttributeError:
            print("False")
            return False

    def size(self):
        """Return size of tree."""
        print(self.__size)
        return self.__size

    def depth(self):
        """Return depth of the tree."""
        if self is None:
            return 0
        else:
            left_depth = self.left.depth() if self.left else 0
            right_depth = self.right.depth() if self.right else 0
            return max(left_depth, right_depth) + 1

    def balance(self):
        """Balance the tree."""
        if self is None:
            return 0
        else:
            balance_left = Tree.depth(self.left)
            balance_right = Tree.depth(self.right)
            return balance_left - balance_right

    def in_order(self):
        """Return generator to traverse nodes in order."""
        if self:
            if self.left:
                for node in self.left.in_order():
                    yield node
            yield self.data
            if self.right:
                for node in self.right.in_order():
                    yield node

    def pre_order(self):
        """Return generator to traverse nodes in pre-order."""
        if self.data is not None:
            yield self.data
        if self.left is not None:
            for node in self.left.pre_order():
                yield node
        if self.right is not None:
            for node in self.right.pre_order():
                yield node

    def post_order(self):
        """Return generator to traverse nodes in post-order."""
        if self.left is not None:
            for node in self.left.post_order():
                yield node
        if self.right is not None:
            for node in self.right.post_order():
                yield node
        if self.data is not None:
            yield self.data

    def breadth_first(self):
        """Return generator that runs breadth first traversal."""
        cont = deque()
        cont.append(self)
        while cont.maxlen() > 0:
            tree = cont.pop()
            if tree.data is not None:
                yield tree.data
            if tree.left is not None:
                cont.append(tree.left)
            if tree.right is not None:
                cont.append(tree.right)

    def _search(self, data):
        """Search for data in tree."""
        if self.data == data:
            return self
        left_contains = None
        right_contains = None
        if self.left is not None:
            left_contains = self.left._search(data)
        if self.right is not None:
            right_contains = self.right._search(data)
        return left_contains or right_contains

    def delete(self, data):
        """Delete data point from BST."""
        # import pdb; pdb.set_trace()
        target = self._search(data)
        # first checks if target exists, if not return None
        if not target:
            return None
        # if there is a parent check through for target, if not,'cross' out
        elif target.parent is not None:
            if target.parent.left == target:
                target.parent.left = None
            elif target.parent.right == target:
                target.parent.right = None
            target.parent = None
        # HERE: want to go through the tree (via generator) and 'recreate' tree
        # need to check results
            for data in Tree.in_order(self):
                if data != target.data:
                    self.insert(data)


# bst = Tree(10)
# bst.insert(11)
# bst.insert(1)
# bst.insert(3)
# bst.insert(4)
# bst.insert(5)
# bst.insert(2)
# bst.insert(9)
# print(bst.in_order())
# bst.delete(9)
