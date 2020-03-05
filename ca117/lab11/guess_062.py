#!/usr/bin/env python3

''' with the use of guess function, find random variable z '''

from random import randint

top = 1000000
bottom = 0
z = randint(bottom, top)
# print(z)  # test

def guess(g):
    if g == z:
        return 0
    elif g < z:
        return -1
    else:
        return 1

# Find z *efficiently* by calling guess() (and without peeking at z!)
def find():
    bottom = 0
    top = 1000000
    g = (bottom + top) // 2

    while bottom < top:
        if guess(g) == -1:
            bottom = g + 1
        else:
            top = g

        g = (bottom + top) // 2

    return bottom


def main():
    a = find()
    if a == z:
        print('Correct!')
    else:
        print('Incorrect!')
    print('You said {:d} and answer is {:d}'.format(a, z))

if __name__ == '__main__':
    main()
