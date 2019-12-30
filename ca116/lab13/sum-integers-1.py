#!/usr/bin/env python


import sys

total = 0

s = sys.stdin.readline()
while 0 < len(s):
    total += int(s)
    s = sys.stdin.readline()

print total
