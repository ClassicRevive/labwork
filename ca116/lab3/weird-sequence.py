#!/usr/bin/env python


n = input()

i = 0
m = 1
while i < n:
    if m % 2 == 0:
        print i * -1
    else:
        print i

    m += 1
    i += 1
