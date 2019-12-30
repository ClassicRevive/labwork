#!/usr/bin/env python


n = input()


i = 0
prev = 0
current = 1

while i < n:
    print prev

    tmp = current
    current = prev + current
    prev = tmp

    i += 1
