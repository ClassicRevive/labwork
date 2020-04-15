#!/usr/bin/env python3

def count_letters(s):
    # base case: s is empty string
    if s == '':
        return 0

    # recursive case
    return 1 + count_letters(s[1:])
