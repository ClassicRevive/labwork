#!/usr/bin/env python3

''' return whether a number is perfect or not (sum of factors) '''

import sys

def sumFac(n):
    # find all factors of n
    factors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)

    return sum(factors)


def isPerfect(n):
    return n == sumFac(n)

def main():

    for line in sys.stdin:
        n = int(line.rstrip())
        print(isPerfect(n))


if __name__ == '__main__':
    main()
