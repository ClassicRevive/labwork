#!/usr/bin/env python3

''' create diamond using asterix
    use complex expressions of:
    1) numbers of asteriks per line in terms of k and n
    2) number of spaces per line in terms of k and n
    3) number of lines in terms of n
    '''

import sys
n = int(sys.argv[1])

def main():
    k = 1
    while k < ((n - 1) * 2) + 2:
        space = " " * abs(n - k)
        build = []

        if k <= n:
            for i in range(k):
                build.append("*")

        else:
            for i in range(n - abs(n - k)):
                build.append("*")

        print(space, end="")
        print(" ".join(build))

        k += 1


if __name__ == '__main__':
    main()
