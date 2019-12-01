#!/usr/bin/env python


import sys

word_count = {}

words = sys.stdin.readlines()

i = 0
while i < len(words):
    word = words[i].rstrip()
    if word not in word_count:
        word_count[word] = 0

    word_count[word] += 1

    i += 1

for word in word_count:
    if word_count[word] == 1:
        print word
