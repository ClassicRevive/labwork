#!/usr/bin/env python3

''' check wether a string is a palindrome '''
def is_palindrome(a):
    # base case
    if len(a) <= 1:
        return True

    x1 = a[0]
    x2 = a[-1]

    if x1 != x2:
        return False
    
    # recursive case
    return is_palindrome(a[1:-1])
