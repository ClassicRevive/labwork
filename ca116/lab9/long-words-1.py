#!/usr/bin/env python


if __name__ == "__main__":
    a = ["", "", "dog", "cat", "hello", "extra-long", "thisissolongbrooo"]


i = 0
while i < len(a):
    if 6 <= len(a[i]):
        print a[i]
    i += 1
