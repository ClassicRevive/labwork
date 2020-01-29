#!/usr/bin/env python3

'''print true if each char in first string is also in the second string'''

import sys

def match(chars, word):
    matched = True
    for i in range(len(chars)):
            if chars[i].lower() in word.lower():
                word = word.replace(chars[i], "*")
            else:
                matched = False
    
    return matched


def main():
    lines = sys.stdin.readlines()
    for line in lines:
        [chars, word] = [line.rstrip().split()]
        print(match(chars, word))


if __name__ == '__main__':
    main()
