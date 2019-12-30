#!/usr/bin/env python


s = raw_input()


total = 0
term_counter = 0
i = 0
j = 0
while term_counter < 5:
    j = i + 1
    while j < len(s) and s[j] != "+":
        j += 1

    term_n = s[i:j]

    i = j + 1
    total += int(term_n)
    term_counter += 1

print total
