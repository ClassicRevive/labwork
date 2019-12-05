#!/usr/bin/env python


pi = 3.141

def circumference(r):
    if type(r) == float or type(r) == int:
        return 2 * pi * float(r)

def area(r):
    if type(r) == float or type(r) == int:
        return pi * float(r) * float(r)

if __name__ == "__main__":
    print circumference(5)
    print area(4)
    print area(50)
