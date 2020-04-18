#!/usr/bin/env python3

''' return word with the most double vowels eg. foo '''

from copy import deepcopy
import sys


def main():
    vowels = "aeiou"
    highest = 0

    for line in sys.stdin:
        word = line.rstrip()

        count = 0
        i = 0
        while i < len(word) - 1:

            if word[i] in vowels and word[i + 1] == word[i]:
                count += 1
                if highest < count:
                    highest = count
                    winner = word

                i += 1  # prevent cross counting

            i += 1

    print(winner)


if __name__ == '__main__':
    main()
