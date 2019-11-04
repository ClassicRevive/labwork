#!/usr/bin/env python

if __name__ == "__main__":
    a = ["dog", "cat", "mouse", ""]

# And the rest of your fragment goes here.

i = 0
non_empty = 0
while i < len(a):
    if a[i] != "":
        non_empty += 1

    i += 1

print non_empty
