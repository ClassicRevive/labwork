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


ans_list = ans.split("\n")

# for each line in list
# split the line
# take first word from split
# capitalize
# append to sentence
# append to rest
# UGLY CODE

i = 0
while i < len(ans_list) - 1:
    sentence = ""
    ans_words = ans_list[i].split()
    # print  ans_words[0]

    j = 0
    if ans_words[0] > "A" and ans_words[0] < "Z":
        sentence += ans_words[j] + " "
        j += 1
    else:
        sentence += ans_words[0].capitalize() + " "
        j += 1

    while j < len(ans_words) - 1:
        sentence += ans_words[j] + " "
        j += 1

    sentence += ans_words[j]

    print sentence
    i += 1
