#!/usr/bin/env python3

''' produce list of words whose reverse is in the list '''

import sys

def reverse(s):
    reverse = ""
    for i in range(len(s)):
        reverse += s[- 1 - i]

    return reverse

def bsearch(a, q):
    low = 0
    high = len(a)
    mid = (low + high) // 2

    while low < high:
        if a[mid] < q:
            low = mid + 1
        else:
            high = mid
        mid = (high + low) // 2

    return low


def main():
    a = []
    al = []
    for i in sys.stdin:
        a.append(i.rstrip())
        al.append(i.rstrip().lower())
    # al.append("zyzy")
    # a.append("zyzy")

    print([x for x in a if 4 < len(x) and reverse(x).lower() == al[bsearch(al, reverse(x).lower())]])


if __name__ == '__main__':
    main()
