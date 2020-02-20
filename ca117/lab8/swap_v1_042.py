#!/usr/bin/env python3

'''module to swao keys and values'''

import sys


def swap_keys_values(d):
    new_dict = {}
    for (k, v) in d.items():
        new_dict[v] = k

    return new_dict


if __name__ == '__main__':
    main()
