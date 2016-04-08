class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.__size = 0

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                    print(self.left.data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                    print(self.right.data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        self.__size += 1

    def contains(self, data):
        try:
            if self.data:
                # import pdb; pdb.set_trace()
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
        print(self.__size)
        return self.__size


bst = Tree(10)
bst.insert(5)
bst.insert(200)
bst.insert(45)
bst.insert(1)
bst.insert(22)
bst.insert(25)
bst.insert(2000)
bst.insert(2)
bst.insert(3)
print("***********************")
bst.contains(1)
bst.contains(5)
bst.contains(200)
bst.contains(45)
bst.contains(1)
bst.contains(3)
bst.contains(22)
bst.contains(2)
bst.contains(25)
bst.contains(33333)
bst.contains(2000)

bst.size()
