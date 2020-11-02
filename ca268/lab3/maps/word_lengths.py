#!/usr/bin/env python

import sys

def get_counts_dict(lst):
    counts = {}
    for word in lst:
        if len(word) not in counts:
            counts[len(word)] = 0
        
        counts[len(word)] += 1

    return counts

def main():
    # read the list of words from stdin
    line = sys.stdin.readline()
    line = line.strip()
    words = line.split()

    # call the student's function
    counts = get_counts_dict(words)
    print(type(counts))

    lengths = counts.keys()
    for length in sorted(lengths):
        print(str(length) + ": " + str(counts[length]))

if __name__ == "__main__":
    main()