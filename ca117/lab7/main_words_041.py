#!/usr/bin/env python3

''' make dictionary of unique word count from input '''

import sys
from string import punctuation

def main():
    words = {}
    desired_width = 0
    desired_numw = 0

    for line in sys.stdin:
        line = line.rstrip().split()

        for element in line:
            element = element.lower().strip(punctuation)
            if 3 < len(element):
                if element not in words:
                    words[element] = 0

                words[element] += 1

    for (k, v) in words.items():
        if 2 < v:
            if desired_width < len(k):
                desired_width = len(k)
            elif desired_numw < len(str(v)):
                desired_numw = len(str(v))

    for (k, v) in sorted(words.items()):
        if 2 < v:
            print("{:>{:d}s} : {:>{:d}d}".format(k, desired_width, v, desired_numw))

if __name__ == '__main__':
    main()
