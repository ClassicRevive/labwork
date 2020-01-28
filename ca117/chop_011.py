#!/usr/bin/env python3

'''removes first and last characters from a string'''

import sys

def chop(s):
    return s[1:-1]


def main():
    for line in sys.stdin:
        chopped = chop(line.strip())
        
        if 0 < len(chopped):
            print(chopped)

if __name__ == '__main__':
    main()
