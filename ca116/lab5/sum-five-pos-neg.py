#!/usr/bin/env python


i = 0
postotal = 0
negtotal = 0

while i < 5:
    n = input()
    if n < 0:
        negtotal += n
    else:
        postotal += n

    i += 1
print negtotal, postotal
