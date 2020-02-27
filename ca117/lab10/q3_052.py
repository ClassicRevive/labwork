#!/usr/bin/env python3

''' module file (functions are explanatory) '''

import sys


def build_dictionary(filename):
    d = {}

    with open(filename, "r") as f:
        for line in f:
            tokens = line.rstrip().split()
            (k, v) = (tokens[0], tokens[1])
            d[k] = int(v)

    return d


def extract_range(d, low, high):
    new_d = {}

    for (k, v) in d.items():
        if low <= v <= high:
            new_d[k] = v

    return new_d


def main():
    d = extract_range(build_dicitionary("mappings.txt"), 5, 15)
    print(d)


if __name__ == '__main__':
    main()
