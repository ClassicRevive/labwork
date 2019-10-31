#!/usr/bin/env python


s = raw_input()


j = 0
number = 0
while number < 2:
    i = j
    while i < len(s) and (s[i] < "0" or "9" < s[i]):
        i += 1

    
    j = i
    while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
        j += 1

     
    number += 1
    

print s[i:j]
