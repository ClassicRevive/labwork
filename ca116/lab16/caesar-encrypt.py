#!/usr/bin/env python


import sys

lower_case = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

encryptions = {}

# load lowercase letters into the encryption dictionary
i = 0
while i < len(lower_case):
    letter = lower_case[i]
    if letter not in encryptions:
        # load the letter and its upper case as well
        encryptions[letter] = lower_case[i + 13]
        encryptions[letter.upper()] = lower_case[i + 13].upper()

    i += 1


# for key in encryptions:
#     print  key, encryptions[key]

text = sys.stdin.read()

message = ""
i = 0
while i < len(text):
    letter = text[i]
    if letter in encryptions:
        message += encryptions[letter]
    else:
        message += letter

    i += 1

sys.stdout.write(message)
