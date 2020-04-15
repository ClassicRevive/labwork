#!/usr/bin/env python3


def maximum(a):
    # base case: list contains 1 element
    if len(a) == 1:
        return a[0]

    # recursive case
    # return a[0] if a[0] > maximum(a[1:]) else maximum(a[1:])
    head = a[0]
    maxtail = maximum(a[1:])
    return head if head > maxtail else maxtail
