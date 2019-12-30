#!/usr/bin/env python


import sys

s = sys.stdin.readline()
while 0 < len(s):
    s_split = s.split("/")
    sys.stdout.write(s_split[-1])

    s = sys.stdin.readline()
