#!/usr/bin/env python3

'''module to swap keys and unique values only'''

import sys


def swap_unique_keys_values(d):
    values = []
    unique = {}
    for (k, v) in d.items():
        values.append(v)

    for value in values:
        if values.count(value) < 2:
            for (k, v) in d.items():
                if v == value:
                    unique[v] = k

    return unique


if __name__ == '__main__':
    main()
