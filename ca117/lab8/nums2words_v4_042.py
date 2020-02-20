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
                   "10": "ten",
                   "11": "eleven",
                   "12": "twelve",
                   "13": "thirteen",
                   "14": "fourteen",
                   "15": "fifteen",
                   "16": "sixteen",
                   "17": "seventeen",
                   "18": "eighteen",
                   "19": "nineteen",
                   "20": "twenty",
                   "30": "thirty",
                   "40": "forty",
                   "50": "fifty",
                   "60": "sixty",
                   "70": "seventy",
                   "80": "eighty",
                   "90": "ninety",
                   "100": "one hundred"}

    try:
        return num_to_word[s]
    except:
        num_build = []
        special = ["2", "3", "4", "5", "8"]
        for i in range(len(s)):
            if i == 0:
                num_build.append(num_to_word[s[i] + "0"])
            else:
                num_build.append(num_to_word[s[i]])

        return "-".join(num_build)


def main():
    for line in sys.stdin:
        nums = line.rstrip().split()
        word_line = []

        for number in nums:
            word_line.append(word(number))

        print(" ".join(word_line))


if __name__ == '__main__':
    main()
