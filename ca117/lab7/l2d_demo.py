#!/usr/bin/env python3

'''test for l2d module'''

import sys
from l2d_041 import l2d

def main():
    d = l2d(sys.stdin)
    for (k, v) in sorted(d.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()
