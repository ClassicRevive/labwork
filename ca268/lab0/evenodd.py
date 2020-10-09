#!/usr/bin/env python3

import sys

word = sys.argv[1]

def main():
    if len(word) % 2 == 1:
        print(word[0] + word[-1])  # odd: first and last char
    else:
        print(word[(len(word) // 2):])  # even: second half

if __name__ == '__main__':
    main()
