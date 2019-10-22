#!/usr/bin/env python


# any number divisible by 3 will be replaced with fizz
# any number divisible by 5 will be replaced with buzz
# any number divisible by 3 and 5 will be replaced with fizz-buzz

n = input()
m = 1

i = 0
while i < n:
    if m % 3 == 0 and m % 5 == 0:
        print "fizz-buzz"
    elif m % 3 == 0:
        print "fizz"
    elif m % 5 == 0:
        print "buzz"
    else:
        print m
    m += 1
    i += 1
