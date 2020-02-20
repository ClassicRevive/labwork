#!/usr/bin/env python3

''' count each vowel in input and display nicely '''

import sys
from string import punctuation

def value(o):
    return o[1]

def main():
    v_length = 0
    vowels = {"a": 0,
              "e": 0,
              "i": 0,
              "o": 0,
              "u": 0}

    for line in sys.stdin:
        line = line.rstrip().lower().strip(punctuation).split()

        for word in line:
            for (k, v) in vowels.items():
                vowels[k] += word.count(k)

    for k, v in vowels.items():
        if v_length < len(str(v)):
            v_length = len(str(v))

    for k, v in sorted(vowels.items(), key=value, reverse=True):
        print("{:s} : {:>{:d}d}".format(k, v, v_length))


if __name__ == '__main__':
    main()
