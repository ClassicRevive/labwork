#!/usr/bin/env python


import sys

words = {}

with open("translation.txt") as translations:

    s = translations.readline()
    while 0 < len(s):
        trnslt_split = s.strip().split()
        key = trnslt_split[0]
        value = trnslt_split[1]
        words[key] = value

        s = translations.readline()

s = sys.stdin.readlines()

# print words

i = 0
while i < len(s):
    word = s[i].rstrip()
    if word in words:
        print words[word]

    i += 1
