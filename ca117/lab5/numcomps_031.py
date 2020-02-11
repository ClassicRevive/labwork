#!/usr/bin/env python3

import sys
n = int(sys.argv[1])

def isPrime(x):
    prime = True
    if x == 1:
        return not prime

    for i in range(2, x):
        if x % i == 0:
            return not(prime)

    return prime


def main():
    a = [x + 1 for x in range(n)]
    print("Multiples of 3: {}".format([x for x in a if not x % 3]))
    print("Multiples of 3 squared: {}".format([x * x for x in a if not x % 3]))
    print("Multiples of 4 doubled: {}".format([x * 2 for x in a if not x % 4]))
    print("Multiples of 3 or 4: {}".format([x for x in a if not x % 3 or not x % 4]))
    print("Multiples of 3 and 4: {}".format([x for x in a if not x % 3 and not x % 4]))
    print("Multiples of 3 replaced: {}".format(["X" if not x % 3 else x for x in a]))
    print("Primes: {}".format([x for x in a if isPrime(x)]))


if __name__ == '__main__':
    main()
