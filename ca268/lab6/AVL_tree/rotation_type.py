#!/usr/bin/env python3

from BST import BST

def rotation_type(bst):
    # identifying node directions for classifying rotation type
    top = bst.root
    if top.left is not None:
        mid = top.left
    else:
        mid = top.right
    if mid.left is not None:
        bot = mid.left
    else:
        bot = mid.right

    if top.item < mid.item < bot.item:
        return "rr"
    elif bot.item < mid.item < top.item:
        return "ll"
    elif mid.item < bot.item < top.item:
        return "lr"
    else:
        # top item < bot.item < mid.item
        return "rl"
