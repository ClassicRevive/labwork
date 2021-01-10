#!/usr/bin/env python3

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

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)

    def height(self):
        return self.recurse_height(self.root)

    def recurse_height(self, ptr):
        if ptr is None:  # base case
            return 0
        else:  # recursive case, get the max of height of left and right subtree
            return 1 + max(self.recurse_height(ptr.left), self.recurse_height(ptr.right))

    def count_non_leaves(self):
        return self.recurse_non_leaves(self.root)

    def recurse_non_leaves(self, ptr):
        if ptr is None:  # base case
            return 0
        if ptr.left is None and ptr.right is None:  # leaf case
            return 0
        return 1 + sum([self.recurse_non_leaves(ptr.left), self.recurse_non_leaves(ptr.right)])


def how_many_searched(element, bst):
    ptr = bst.root
    searched = 0
    while ptr is not None:
        searched += 1
        if ptr.item == element:  # found it!
            return searched
        elif element < ptr.item:  # go left
            ptr = ptr.left
        elif element > ptr.item:  # go right
            ptr = ptr.right



import random

def test(lst):
    bst = BST()

    # Add each element in the lst to the tree
    for n in lst:
        bst.add(n)

    index = random.randint(0, len(lst) - 1)
    element = lst[index]

    count = how_many_searched(element, bst)
    # Print the list and the result of calling the function
    print("how_many_searched(" + str(element) + ", " + str(lst) +") is " + str(count))

def main():
   random.seed(0)
   test([4])
   test([4, 5, 6, 7, 1, 2, 3])
   test([40, 20, 30, 50, 10, 13, 14, 5, 18])

main()