#!/usr/bin/env python3

'''prints pi to n decimal places where n is sys.argv[1]'''

from math import pi
import sys
n = int(sys.argv[1])

def main():
    print("{:.{}f}".format(pi, n))

if __name__ == '__main__':
    main()
