#!/usr/bin/env python

import sys

''' count the tokens in given input (usually a file) '''
def main():
    tokens = sys.stdin.read().split()
    print(len(tokens))


if __name__ == '__main__':
    main()
