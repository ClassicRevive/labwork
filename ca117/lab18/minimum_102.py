#!/usr/bin/env python3


''' get the mimimum of a list of numbers'''
def minimum(a):
    # base case
    if len(a) <= 1:
        return a[0]

    # recursive case
    head = a[0]
    min_tail = minimum(a[1:])
    return head if head < min_tail else min_tail
