#!/usr/bin/env python

import func_bsearch

def sum_range(a, low, high):
    beginning = func_bsearch.bsearch(a, low)

    total = 0
    j = beginning
    while j < len(a) and a[j] < high:
        total += a[j]
        j += 1

    return total

if __name__ == "__main__":
    a = [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9]
