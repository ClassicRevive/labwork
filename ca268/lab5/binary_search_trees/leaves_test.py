#!/usr/bin/env python3

from BST import BST

def main():
    bst = BST()
    bst.add(1)
    bst.add(2)
    bst.add(-1)
    bst.add(4)
    bst.add(3)
    print(bst.count_leaves())

if __name__ == '__main__':
    main()