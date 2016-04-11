class Tree(object):
    """Single class implementation of BST."""

    def __init__(self, data=None):
        """Initialize."""
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        self.__size = 1

    def insert(self, data):
        """Insert data into tree."""
        if not isinstance(data, int) or isinstance(data, float):
            raise TypeError('Must be int or float')
        else:
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Tree(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Tree(data)
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
