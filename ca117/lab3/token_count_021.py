#!/usr/bin/env python3

import sys

''' count the tokens in given input (usually a file) '''
def main():
    tokens = sys.stdin.read().split()
    print(len(tokens))


if __name__ == '__main__':
    main()
