#!/usr/bin/env python

from BST import BST

def main():
    bst = BST()
    bst.add(5)
    bst.add(4)
    bst.add(6)
    bst.add(1)
    print(bst.total())


if __name__ == '__main__':
    main()


