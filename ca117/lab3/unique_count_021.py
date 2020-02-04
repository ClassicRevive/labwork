#!/usr/bin/env python3

''' take input and display number of unique words'''

import sys
import string

def main():
    seen = {}
    tokens = sys.stdin.read().split()

    # remove all punctuation
    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip(string.punctuation)

    for token in tokens:
        if token.lower() not in seen and token != "":
            seen[token.lower()] = True

    # print(seen)
    print(len(seen))


if __name__ == '__main__':
    main()
