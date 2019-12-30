#!/usr/bin/env python


import sys

s = sys.stdin.read()
words = s.split()
# print words

i = 0
ans = ""
while i < len(words):
    if words[i][-1] == "." or words[i][-1] == "?" or words[i][-1] == "!":
        ans += words[i] + "\n"
    else:
        ans += words[i] + " "

    i += 1
sys.stdout.write(ans)
