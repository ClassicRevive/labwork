#!/usr/bin/env python


postotal = 0
negtotal = 0

n = input()
while n != 0:
    if n < 0:
        negtotal += n
    else:
        postotal += n
    n = input()

print negtotal, postotal
