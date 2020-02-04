#!/usr/bin/env python3

''' return boolean for whether two words are anagrams or not'''

import sys

def anagram(left, right):
    if len(left) == len(right):
        for char in left:
            i = 0
            matched = False
            while i < len(right) and not(matched):
                if char == right[i]:
                    right = right.replace(char, "", 1)
                    matched = True

                i += 1

        return 0 == len(right)
    else:
        return False


def main():

    for line in sys.stdin:
        [left, right] = line.rstrip().split()
        print(anagram(left, right))


if __name__ == '__main__':
    main()
