#!/usr/bin/env python3

''' check wether a string is a palindrome '''
def is_palindrome(a):
    # base case
    if len(a) <= 1:
        return True

    # recursive case
    return a[0] == a[-1] and is_palindrome(a[1:-1])
