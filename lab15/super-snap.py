#!/usr/bin/env python

import sys

seen = {}

words = sys.stdin.readlines()

i = 0
snap = False
while i < len(words) and not(snap):
    word = words[i].rstrip()

    if word not in seen:
        seen[word] = True
    else:
        print "snap:", word
        snap = True

    i += 1
