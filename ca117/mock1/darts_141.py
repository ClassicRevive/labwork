#!/usr/bin/env python3

''' output total darts score based on coordinates of darts '''
import sys
from math import sqrt

def main():
    score = 0
    circles = [20 * c for c in range(1, 11)]

    for line in sys.stdin:
        line = line.rstrip().split()
        x, y = int(line[0]), int(line[1])

        # calculate euclidean distance from the origin
        dist = sqrt(x ** 2 + y ** 2)

        # now find smallest circle which encloses the coord
        # using linear search
        p = 0
        while p < len(circles) and (20 * (11 - p) >= dist):
            p += 1

        # special case caturing;
        # 1.the dart is in the smallest circle 2. the dart is out of bounds
        if 20 * (11 - p) >= dist:
            score += p
        elif p != 0:
            score += p - 1

    print(score)


if __name__ == '__main__':
    main()
