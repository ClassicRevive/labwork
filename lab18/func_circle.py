#!/usr/bin/env python


def circumference(r):
    if type(r) == float or type(r) == int:
        return 2 * 3.141 * float(r)

def area(r):
    if type(r) == float or type(r) == int:
        return 3.141 * float(r) * float(r)

if __name__ == "__main__":
    print circumference(5)
    print area(4)
    print area(50)
