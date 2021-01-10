#
#   Create a method which will return the height of the Binary Search Tree (BST)
#
#
class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
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

    def count_right_only(self):
        return self.recurse_count_right(self.root)  # recursive call

    def recurse_count_right(self, ptr):
        if ptr is None:  # base case
            return 0
        if ptr.left is None and ptr.right is not None:  # right case
            return 1 + self.recurse_count_right(ptr.right)
        else:  # general case, keep searching
            return sum([self.recurse_count_right(ptr.left), self.recurse_count_right(ptr.right)])


def who_searched(val, bst):
    visited = []
    if bst.root is not None:
        
        ptr = bst.root
        while ptr is not None:
            visited.append(ptr.item)
            # search instructions
            if val < ptr.item:
                ptr = ptr.left
            elif ptr.item < val:
                ptr = ptr.right
            elif val == ptr.item:
                return visited

import random

def test(lst):
    bst = BST()

    # Add each element in the lst to the tree
    for n in lst:
        bst.add(n)

    index = random.randint(0, len(lst) - 1)
    element = lst[index]

    elements = who_searched(element, bst)
    # Print the list and the result of calling the function
    print("search(" + str(element) + ", " + str(lst) +") is " + str(elements))


def main():
   random.seed(0)
   test([4])
   test([4, 5, 6, 7, 1, 2, 3])
   test([40, 20, 30, 50, 10, 13, 14, 5, 18])

main()
