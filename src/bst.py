from collections import deque
import random


class Tree(object):
    """Single class implementation of BST."""

    def __init__(self, data=None, parent=None):
        """Initialize."""
        self._left = None
        self._right = None
        self.parent = None
        self.data = data
        self.__size = 1

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
        if not isinstance(data, int) or isinstance(data, float):
            raise TypeError('Must be int or float')
        else:
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
        if not target:
            return None
        # leaf
        elif target.left is None and target.right is None:
            if target.parent is None:
                target.data = None
            elif target.parent.left == target:
                target.parent.left = None
            elif target.parent.right == target:
                target.parent.right = None

        # one-child
        elif target.left and not target.right:
            target.parent.left = target.left
            target.left = None
        elif target.right and not target.left:
            target.parent.right = target.right
            target.right = None

        # two-child
        elif target.left and target.right:
            if target.parent is not None:
                child = target.right
                while child.left:
                    child = child.left
                target.data = child.data
                if child.right:
                    child.right = child.parent.left
                child.parent.left = None

    def get_dot(self):
        """Return the tree with root'self' as a dot graph for visualization."""
        return "digraph G{\n%s}" % ("" if self.data is None else (
            "\t%s;\n%s\n" % (
                self.data,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """Recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.data, self.left.data)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.data, self.right.data)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)


bst = Tree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
bst.insert(75)
bst.insert(72)
bst.insert(100)
bst.insert(73)
bst.delete(70)
print(bst.get_dot())
# print(bst.in_order())
