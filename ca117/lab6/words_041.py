#!/usr/bin/env python3

''' make dictionary of unique word count from input '''

import sys
from string import punctuation

def main():
    words = {}

    for line in sys.stdin:
        line = line.rstrip().split()

        for element in line:
            element = element.lower().strip(punctuation)

            if element not in words:
                words[element] = 0

            words[element] += 1

    for (k, v) in sorted(words.items()):
        print("{} : {}".format(k, v))

if __name__ == '__main__':
    main()
