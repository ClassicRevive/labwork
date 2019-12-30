#!/usr/bin/env python


import sys

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

candidates = sys.stdin.readlines()

i = 0
while i < len(candidates):
    if candidates[i].rstrip() in fruit:
        sys.stdout.write(candidates[i])

    i += 1
