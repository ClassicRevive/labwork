#!/usr/bin/env python3

def power(n, m):
    # base case
    if m == 0:
        return 1

    # recursive case
    return n * power(n, m - 1)
