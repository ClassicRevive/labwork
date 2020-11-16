#!/usr/bin/env python3

from BST import BST

bst = BST()
bst.add(1)
bst.add(2)
bst.add(4)
bst.add(-1)
bst.add(-2)
print(bst.is_present(0))