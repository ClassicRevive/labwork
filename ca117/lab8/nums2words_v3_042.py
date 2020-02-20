#!/usr/bin/env python3

'''assign words to numbers from stdin but now map to a key from file'''

import sys

filename = sys.argv[1]

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
    map_dict = {}

    with open(filename) as mapp:
      for line in mapp:
        (k, v) = line.rstrip().split()
        map_dict[k] = v

    try:
      return map_dict[num_to_word[s]]
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
