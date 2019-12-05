#!/usr/bin/env python


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

    return a

def reverse(a):
    i = 0
    while i < len(a) / 2:
        tmp = a[i]
        a[i] = a[-i - 1]
        a[-i - 1] = tmp

        i += 1

    return a

if __name__ == "__main__":
    import random

    test_list = []
    i = 0
    while i < 10:
        test_list.append(random.randrange(50))

        i += 1

    print test_list
    # swap(test_list, 1, 2)
    # print test_list
    reverse(test_list)
    print test_list
