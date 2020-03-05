#!/usr/bin/env python3

''' return quadratic roots of a quadratic equation '''

import sys
from math import sqrt

def quad(a, b, c):
    r1 = (-b + sqrt((b * b) - (4 * a * c))) / (2 * a)
    r2 = (-b - sqrt((b * b) - (4 * a * c))) / (2 * a)

    return (r1, r2)


def main():
    for line in sys.stdin:
        try:
            (a, b, c) = line.rstrip().split()
            (a, b, c) = (int(a), int(b), int(c))
            (r1, r2) = quad(a, b, c)
            print("r1 = {}, r2 = {}".format(r1, r2))
        except:
            print(None)


if __name__ == '__main__':
    main()
