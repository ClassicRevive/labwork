#!/usr/bin/env python


n = input()

if n % 2 == 0 and n != 2 or n % 3 == 0 and n != 3:
    print "not prime"
elif n == 1:
    print "not prime"
else:
    print "prime"
