#!/usr/bin/env python


n = input()
p = input()

# trim number down so last digit is the target
num = n / 10 ** p

# print the last digit of th number
print num % 10
