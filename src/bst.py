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
        self._size = 1

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
                self._size += 1
                if data < self.data:
                    if self.left is None:
                        self.left = Tree(data=data, parent=self)
                        self._crawl_tree()
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Tree(data=data, parent=self)
                        self._crawl_tree()
                    else:
                        self.right.insert(data)
                else:
                    raise TypeError('This value already exists')
            else:
                self.data = data

    def _crawl_tree(self):
        """move up the tree and balance branches that are too heavy"""
        if self.data:
            if self.balance() > 1:
                if self.left.balance() < 0 and self.left.depth() > 1:
                    self.left._rotate_left()
                    self._rotate_right()
                else:
                    self._rotate_right()
            elif self.balance() < -1:
                if self.right.balance() > 0 and self.right.depth() > 1:
                    self.right._rotate_right()
                    self._rotate_left()
                else:
                    self._rotate_left()
        if self.parent:
            self.parent._crawl_tree()

    def _rotate_right(self):
        """Rotate right from parent node."""
        new_root = self.left
        new_root.data, self.data = self.data, new_root.data
        if new_root.left:
            self.left = new_root.left
            new_root.left = None
        if new_root.right:
            new_root.left = new_root.right
            new_root.right = None
        if self.right:
            new_root.right = self.right
            self.right = None
        self.right = new_root
        if self.left == new_root.left:
            new_root.left = None

    def _rotate_left(self):
        """Rotate left from parent node."""
        new_root = self.right
        new_root.data, self.data = self.data, new_root.data
        if new_root.right:
            self.right = new_root.right
            new_root.right = None
        if new_root.left:
            new_root.right = new_root.left
            new_root.left = None
        else:
            new_root.right = None
        if self.left:
            new_root.left = self.left
            self.left = None
        if self.right == new_root.right:
            new_root.right = None
        self.left = new_root

    def contains(self, data):
        """Check tree for data."""
        if data == self.data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.contains(data)
            else:
                return False
        elif data > self.data:
            if self.right:
                return self.right.contains(data)
            else:
                return False

    def size(self):
        """Return size of tree."""
        if self.data:
            return self._size
        else:
            return 0

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
            balance_left = balance_right = 0
            if self.left:
                balance_left = Tree.depth(self.left)
            if self.right:
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
        target = self._search(data)
        if not target:
            return None
        # leaf
        if not target.left and not target.right:
            if not target.parent:
                target.data = None
            elif target.parent.left == target:
                target.parent.left = None
            elif target.parent.right == target:
                target.parent.right = None
        # one-child
        elif target.left and not target.right:
            if target == target.parent.right:
                target.parent.right = target.left
            else:
                target.parent.left = target.left
            target.left = None
        elif target.right and not target.left:
            if target == target.parent.right:
                target.parent.right = target.right
            else:
                target.parent.left = target.right
            target.right = None
        # two-child
        elif target.left and target.right:
            child = target.right
            while child.left:
                child = child.left
            target.data = child.data
            if child is child.parent.right:
                if child.right:
                    child.parent.right = child.right
                else:
                    child.parent.right = None
            else:
                if child.right:
                    child.parent.left = child.right
                else:
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
