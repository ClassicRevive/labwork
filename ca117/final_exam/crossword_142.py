#!/usr/bin/env python3

import sys

def main():
    a, b = sys.stdin.readline().strip().split()

    width = len(a)
    length = len(b)

    # find common first occurene of letter
    i = 0
    while i < len(a):
        if a[i] in b:
            cross, cross_index = a[i], i
            i = len(a)

        i += 1

    # length x width matrix processeed line by line
    for i in range(length):
        line = []
        for j in range(width):
            if j == cross_index:  # connditions to print b
                line.append(b[i])
            elif i == cross_index:  # conditions to print a
                line.append(a)
                break
            else:
                line.append(".")

        print("".join(line))

if __name__ == '__main__':
    main()
