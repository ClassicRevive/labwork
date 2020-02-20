#!/usr/bin/env python3

''' module which reads file and corresponds keys to values'''

import sys

def l2d(file):
    d = {}
    f1 = file.readline()
    keys = f1.rstrip().split()

    f2 = file.readline()
    values = f2.rstrip().split()

    for i in range(len(keys)):
        d[keys[i]] = values[i]

    return d

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as fin:
        print(l2d(fin))
