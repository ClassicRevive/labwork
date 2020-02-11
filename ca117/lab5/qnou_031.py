#!/usr/bin/env python3

''' displays words which contain q with no following u (non case sensitive) '''

import sys

def q_check(word):
    if not word.lower().count("q"):
        return False

    return word.lower().count("qu") < word.lower().count("q")

def main():
    a = []
    for i in sys.stdin:
        a.append(i.rstrip())

    print("Words with q but no u: {}".format([x for x in a if q_check(x)]))


if __name__ == '__main__':
    main()
