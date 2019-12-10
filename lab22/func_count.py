#!/usr/bin/env python

import func_bsearch

def count(a, q):
    search = func_bsearch.bsearch(a, q)
    if search == len(a) or a[search] != q:
        return 0
    else:
        return a.count(q)

if __name__ == "__main__":
    test_list = [2, 4, 4, 7, 10, 10, 11, 20, 25, 25, 25, 25, 26]
    print count(test_list, 7)
