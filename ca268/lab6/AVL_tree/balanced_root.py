#!/usr/bin/env python3

from BST import BST

def is_avl(bst):
    return r_is_avl(bst, bst.root)

def r_is_avl(bst, ptr):
    return abs(bst.r_height(ptr.left) - bst.r_height(ptr.right)) <= 1