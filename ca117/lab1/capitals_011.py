#!/usr/bin/env python3


''' for each line in stdin, print with first character and last character capitalized'''

import sys

def cap(s):
    result_string = s[0].capitalize() + s[1:-1] + s[-1].capitalize()
    return result_string


def main():
    lines = sys.stdin.readlines()

    for line in lines:
        line = line.rstrip()

        if 1 < len(line):
            print(cap(line))

if __name__ == '__main__':
    # print(cap("hello"))
    main()
