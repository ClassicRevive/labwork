#!/usr/bin/env python


total = 0

num = input()
while num != 0:
    if num < 0:
        total += (num * -1)
    else:
        total += num

    num = input()

print total
