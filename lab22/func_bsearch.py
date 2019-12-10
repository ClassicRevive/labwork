#!/usr/bin/env python


def bsearch(a, q):
    low = 0
    high = len(a)
    mid = (low + high) / 2

    while low < high:
        if a[mid] < q:
            low = mid + 1
        else:
            high = mid

        mid = (low + high) / 2

    return low

if __name__ == "__main__":
    a = [5, 6, 7, 7, 7, 8, 10, 10, 12, 12]
    print bsearch(a, 10)
