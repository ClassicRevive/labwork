#!/usr/bin/env python

import func_bsearch


def contains(a, q):
    search = func_bsearch.bsearch(a, q)
    if search == len(a):
        return 1 == 0

    return a[func_bsearch.bsearch(a, q)] == q

if __name__ == "__main__":
    a = [5, 6, 7, 7, 7, 8, 10, 10, 12, 12]
    print contains(a, 13)
