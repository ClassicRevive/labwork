#!/usr/bin/env python3


import sys

def crazy_cap(s):
    return s[:-1] + s[-1].upper()

def main():
    for line in sys.stdin:
        words = line.strip().split()
        for i in range(len(words)):
            words[i] = crazy_cap(words[i])

        print(" ".join(words))

if __name__ == '__main__':
    main()
