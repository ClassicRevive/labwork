class Node:
    ''' A node in a Binary Search Tree. It may have left and right subtrees '''
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    ''' An implementation of a Binary Search Tree '''
    def __init__(self):
        self.root = None

    def recurse_add(self, ptr, item):
        if ptr is None:  # base case
            return Node(item)
        elif item < ptr.item:  # traverse left
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:  # traverse right
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr  # item is a duplicate

    def add(self, item):
        ''' Add this item to its correct position on the tree '''
        self.root = self.recurse_add(self.root, item)

    def r_contains(self, ptr, item):
        if ptr is None:
            return None
        elif item == ptr.item:
            return ptr
        elif item < ptr.item:
            return self.r_contains(ptr.left, item)
        else:
            return self.r_contains(ptr.right, item)

    def contains(self, item):
        return self.r_contains(self.root, item)

    def in_order(self, ptr):
        if ptr is not None:
            # recursively traverses to the furthest left leaf
            self.in_order(ptr.left)
            # prints the leaf
            print(ptr.item)
            # tries to traverse right at every node, printing its
            # left most nodes, hence printing in ascending order
            self.in_order(ptr.right)

    def recursive_count(self, ptr):
        if ptr is None:
            return 0
        else:
            return 1 + sum([self.recursive_count(ptr.left), self.recursive_count(ptr.right)])


    def count(self):
        return self.recursive_count(self.root)

    def recurs_height(self, ptr):
        if ptr is None:
            return 0
        else:
            return 1 + max(self.recurs_height(ptr.left), self.recurs_height(ptr.right))

    def height(self):
        return self.recurs_height(self.root)

    def total(self):
        return self.recursive_total(self.root)

    def recursive_total(self, ptr):
        if ptr is None:
            return 0
        else:
            return ptr.item + sum([self.recursive_total(ptr.left), self.recursive_total(ptr.right)])

    def is_present(self, item):
        return self.recurs_present(self.root, item)

    def recurs_present(self, ptr, item):
        if ptr is None:  # base case (failure)
            return False
        elif ptr.item == item:  # success case
            return True
        else:  # recursive case, check left and right branches, if any match is found then True
            return any([self.recurs_present(ptr.left, item), self.recurs_present(ptr.right, item)])

    def count_leaves(self):
        return self.recursive_leaves(self.root)

    def recursive_leaves(self, ptr):
        if ptr is None:  # base (empty) case
            return 0
        elif ptr.left is None and ptr.right is None: # leaf case
            return 1
        elif ptr.left is not None or ptr.right is not None:  # recursive case
            return sum([self.recursive_leaves(ptr.left), self.recursive_leaves(ptr.right)])




        