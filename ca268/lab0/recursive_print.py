#!/usr/bin/env python3

''' Write a recursive function called rprint to print 
    a range of integers from a to b. 
'''

import sys

def rprint(a, b):
    # base case:
    if a == b - 1:
        print(a)
        return a

    # recursive case:
    print(a)
    rprint(a + 1, b)

def main():
    rprint(-2, 5)

if __name__ == '__main__':
    main()