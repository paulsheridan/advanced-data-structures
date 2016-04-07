class Node(object):
    def __init__(self, val):
        self.val = val
        self._left = None
        self._right = None
        self.parent = None

        @property
        def left(self):
            return self._left

        @left.setter
        def left(self, left):
            self._left = left

        @property
        def right(self):
            return self._right

        @right.setter
        def right(self, right):
            self._right = right


class BinarySearchTree(object):
    def __init__(self, itbl=None):
        self.root = None
        self._size = 0
        if itbl is not None:
            try:
                for item in itbl:
                    self.insert(item)
            except TypeError:
                print('That is not an iterable')

    def insert(self, val):
        self._size += 1
        parent = None
        current = self.root
        new = Node(val)
        while current:
            if new.val > current.val:
                parent = current
                current = current.right
            elif new.val < current.val:
                parent = current
                current = current.left
            else:
                print('That value already exists in this tree')
        if current == self.root:
            self.root = new
        else:
            current = new
            new.parent = parent

    def size(self):
        return self._size
