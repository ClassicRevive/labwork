#!/usr/bin/env python


if __name__ == "__main__":
    a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]


i = 0
j = a[0]
t = 0
while i < len(a):
    if a[i] < j:
        j = a[i]
        t = i
    i += 1

print t
