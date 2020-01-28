#!/usr/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        line = line.rstrip()
        words = line.split()

        for i in range(len(words)):
            words[i] = words[i].capitalize()

        print(" ".join(words))

if __name__ == '__main__':
    main()
