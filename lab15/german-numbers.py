#!/usr/bin/env python

import sys

eng_to_gr = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn"
}

numbers = sys.stdin.readlines()

i = 0
while i < len(numbers):
    # replace english key with german value
    key = numbers[i].rstrip()
    if key in eng_to_gr:

        sys.stdout.write(eng_to_gr[key] + "\n")

    i += 1
