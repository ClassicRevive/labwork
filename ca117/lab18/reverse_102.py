#!/usr/bin/env python3

''' write recursive function to reverse a list '''

def reverse_list(a):
    # base case
    if a == []:
        return []

    # recursive case: list[1:] + head
    element = [a[0]]
    return reverse_list(a[1:]) + element
