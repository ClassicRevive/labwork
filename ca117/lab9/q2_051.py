#!/usr/bin/env python3

''' The program should print all words in the list that contain a single
instance of each of the characters “e”, “v”, “i”, “l”, in that order '''

import sys


def evil(s):
    return "".join([c for c in s if c.lower() in 'evil'])


def main():
    for word in sys.stdin:
        word = word.rstrip()

        if evil(word).lower() == "evil":
            print(word)


if __name__ == '__main__':
    main()
