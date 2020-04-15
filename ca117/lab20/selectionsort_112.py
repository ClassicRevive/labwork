#!/usr/bin/env python3

''' module for selection sort algorithm '''

def selectionsort(a):
    i = 0
    while i < len(a):
        p = i
        # find smallest element in a[i:N]
        j = i + 1
        while j < len(a):
            if a[j] < a[p]:
                p = j

            j += 1

        # swap smallest element in a[i:N] with element at a[i]
        a[i], a[p] = a[p], a[i]
        i += 1

    return a


def main():
    a = [53, 32, 44, 28, 12, 1]
    selectionsort(a)
    print(a)

if __name__ == '__main__':
    main()
