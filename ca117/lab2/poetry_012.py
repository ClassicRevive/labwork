#!/usr/bin/env python3

''' center the text from stdin and print '''

import sys


def main():
    lines = sys.stdin.readlines()
    longest = 0
    for line in lines:
        line = line.rstrip()
        if longest < len(line):
            longest = len(line)

    for line in lines:
        line = line.rstrip()
        print('{:^{}s}'.format(line, longest))


if __name__ == '__main__':
    main()
