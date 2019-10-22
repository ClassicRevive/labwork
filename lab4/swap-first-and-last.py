#!/usr/bin/env python


s = raw_input()

# print s with reversed first and last characters
print s[len(s) - 1] + s[1: len(s) - 1] + s[0]
