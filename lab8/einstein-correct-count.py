#!/usr/bin/env python


correct_count = 0

s = raw_input()
while s != "end":
    i = len(s) - 1
    while i != 0 and s[i] != "y":
        i -= 1

    if s[i + 2:] == "correct":
        correct_count += 1

    s = raw_input()

print correct_count
