#!/usr/bin/env python


if __name__ == "__main__":
    a = ["", "", "dog", "mountjoy", "mounty", "extra-long", "mountain"]
    s = "mount"

i = 0
while i < len(a):
    if a[i][:len(s)] == s:
        print a[i]
    i += 1
