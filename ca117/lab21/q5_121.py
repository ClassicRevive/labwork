#!/usr/bin/env python3

''''''

import sys

def get_avg(scores):

    total = 0
    for score in scores:
        if score != "X":
            total += int(score)
    mean = total / 6

    return mean

def sort(t):
    return t[1]

def main():
    stats = {}

    for line in sys.stdin:
        # tokenize the data
        name, scores = line.rstrip().split(":")
        scores = scores.strip().split(",")
        stats[name] = get_avg(scores)

    for k, v in sorted(stats.items(), key=sort, reverse=True):
        print("{:s}: {:.1f}".format(k, v))


if __name__ == '__main__':
    main()
