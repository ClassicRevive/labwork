class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def recurse_add(self, ptr, item):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr
        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        self.root = self.recurse_add(self.root, item)

    def r_count(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.r_count(ptr.left) + self.r_count(ptr.right)
            
    def count(self): return self.r_count(self.root)

    def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.r_height(ptr.left), self.r_height(ptr.right))

    def height(self): return self.r_height(self.root)

    def in_order(self):
        self.r_in_order(self.root)
        print()

    def r_in_order(self, ptr):
        if ptr is not None:
            self.r_in_order(ptr.left)
            print(ptr.item, end=" ")
            self.r_in_order(ptr.right)

    def pre_order(self):
        self.r_pre_order(self.root)
        print()

    def r_pre_order(self, ptr):
        if ptr is not None:
            print(ptr.item, end=" ")
            self.r_pre_order(ptr.left)
            self.r_pre_order(ptr.right)

    def post_order(self):
        self.r_post_order(self.root)
        print()

    def r_post_order(self, ptr):
        if ptr is not None:
            self.r_post_order(ptr.left)
            self.r_post_order(ptr.right)
            print(ptr.item, end=" ")

    def __iter__(self):
        for i in self.r_iter(self.root):
            yield i

    def r_iter(self, ptr):  # pre order iteration
        if ptr is not None:
            for x in self.r_iter(ptr.left):  # recursive left case
                yield x
            for y in self.r_iter(ptr.right):  # recursive right case
                yield y
            yield ptr.item


