#!/usr/bin/env python3

'''print the longest instance of contigious upper case letters in each line of stdin'''

import sys

def upper_case(s):
    a = "".join(['0' if c.islower() else c for c in s])
    a = a.split("0")
    return a


def main():
    for line in sys.stdin:
        line = line.rstrip()

        print(max(upper_case(line), key=len))


if __name__ == '__main__':
    main()
