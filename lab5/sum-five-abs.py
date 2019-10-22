#!/usr/bin/env python

total = 0

i = 0
while i < 5:
    num = input()
    if num < 0:
        total += (num * -1)
    else:
        total += num

    i += 1

print total
