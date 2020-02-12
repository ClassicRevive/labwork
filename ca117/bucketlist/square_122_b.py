#!/usr/bin/env python3

''' given 3 sides of a square, find the fourth side. '''

import sys
from math import sqrt


def distance(a, b):
    [x1, y1, x2, y2] = [a[0], a[1], b[0], b[1]]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    # find distance between all points
    sides = []

    for line in sys.stdin:
        side = line.strip().split()

        for i in range(len(side)):
            side[i] = int(side[i])
        sides.append(side)

    [side1, side2, side3] = sides

    d_12 = distance(side1, side2)
    d_13 = distance(side1, side3)
    d_23 = distance(side2, side3)

    # the common distance shows which corner is the middle corner
    if d_12 > d13 and d_12 > d_23:

    # want transformation to get from middle corner to unfound opposite
    # corner, want transformation based on other two sides.


if __name__ == '__main__':
    main()
