#!/usr/bin/env python


import sys
# this program will read standard input as an entire file and print its
# contents one word per line

s = sys.stdin.read()
yes = "\n".join(s.split())
print yes
