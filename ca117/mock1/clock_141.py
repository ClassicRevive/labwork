#!/usr/bin/env python3

''' return minimum moves to get from A to B on a clock
    - clock is 12 hour
'''

import sys

def solve():
    t1 = int(sys.stdin.readline().rstrip())
    t2 = int(sys.stdin.readline().rstrip())

    if (t2 < t1):
        clockwise = 12 - (t1 - t2)
        anticlockwise = t2 - t1
    else:
        clockwise = t2 - t1
        anticlockwise = -(12 + (t1 - t2))

    # print("clockwise:", clockwise, "anticlockwise:", anticlockwise)
    print(min([clockwise, anticlockwise], key=abs))


if __name__ == '__main__':
    solve()
