class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree(object):
    def __init__(self, itbl=None):
        self.root = None
        self.__size = 0
        if itbl is not None:
            try:
                for item in itbl:
                    self.insert(item)
                    print(item)
            except TypeError:
                print('That is not an iterable')

    def insert(self, val):
        parent = None
        current = self.root
        self.__size += 1
        new = Node(val)
        current = new
        print('root', self.root.val)
        current.parent = parent

    def size(self):
        return self.__size


        # while current:
        #     if new.val > current.val:
        #         parent = current
        #         current = current.right
        #     elif new.val < current.val:
        #         parent = current
        #         current = current.left
        #     else:
        #         print('That value already exists in this tree')
