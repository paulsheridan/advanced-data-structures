class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self, itbl=None):
        self.root = None
        self.count = 0
        try:
            for item in itbl:
                self.insert(item)
                print(item)
        except TypeError:
            print('That is not an iterable')

    def insert(self, val):
        self.count += 1
        new = Node(val)
        if self.root is None:
            self.root = new
        else:
            pass

    def size(self):
        print('size')
        return self.count
