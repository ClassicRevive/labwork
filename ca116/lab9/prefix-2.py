#!/usr/bin/env python


if __name__ == "__main__":
    a = ["", "", "dog", "mountjoy", "mounty", "extra-long", "mountain"]
    s = "mount"

i = 0
while i < len(a) and s not in a[i]:
    i += 1

if i < len(a):
    print a[i]
