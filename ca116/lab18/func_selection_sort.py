#!/usr/bin/env python


def selection_sort(a):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            if a[j] < a[p]:
                p = j

            j += 1

        a[i], a[p] = a[p], a[i]
        i += 1

    return a

if __name__ == "__main__":
    ls = [4, 35, 23, 211]

    print ls
    print selection_sort(ls)
