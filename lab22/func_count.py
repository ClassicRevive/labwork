#!/usr/bin/env python

import func_bsearch

def count(a, q):
    # find q
    # find where next number isnt q
    search1 = func_bsearch.bsearch(a, q)
    search2 = func_bsearch.bsearch(a, q + 1)
    count = search2 - search1

    return count

if __name__ == "__main__":
    test_list = [2, 4, 4, 7, 10, 10, 11, 20, 25, 25, 25, 25, 26]
    print count(test_list, 7)
