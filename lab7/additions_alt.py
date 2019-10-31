#!/usr/bin/env python


s = raw_input()

i = 0
while i < len(s) and s[i] != "+":
    i += 1
term_1 = s[:i]

total = int(term_1)
term_counter = 0
j = 0
while term_counter < 4:
    j = i + 1
    while j < len(s) and s[j] != "+":
        j += 1
    
    term_n = s[i+1:j] 
    
    i = j
    total += int(term_n)
    term_counter += 1

print total
