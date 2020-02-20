#!/usr/bin/env python3

'''assign words to numbers from stdin'''

import sys

def word(s):
    num_to_word = {"0": "zero",
                   "1": "one",
                   "2": "two",
                   "3": "three",
                   "4": "four",
                   "5": "five",
                   "6": "six",
                   "7": "seven",
                   "8": "eight",
                   "9": "nine",
                   "10": "ten"}

    try:
        return num_to_word[s]
    except:
        return "unknown"


def main():
    for line in sys.stdin:
        nums = line.rstrip().split()
        word_line = []

        for number in nums:
            word_line.append(word(number))

        print(" ".join(word_line))


if __name__ == '__main__':
    main()
