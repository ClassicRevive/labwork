#!/usr/bin/env python3

import sys

def main():
    # read integers into two lists
    l1 = [int(c) for c in sys.stdin.readline().strip().split()]
    l2 = [int(c) for c in sys.stdin.readline().strip().split()]

    # compare indices
    matches = []
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            matches.append(i)

    print(matches)


if __name__ == '__main__':
    main()
