#!/usr/bin/env python


import sys

for line in sys.stdin:
    line = line.rstrip()
    words = line.split()

    print(words[0].lower() in words[1].lower())
