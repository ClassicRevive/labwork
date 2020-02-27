#!/usr/bin/env python3

'''Demonstrate use of extract_range function.'''

import q3_052

def main():
    d = q3_052.build_dictionary('mappings.txt')

    nd = q3_052.extract_range(d, 5, 15)

    for (k, v) in sorted(nd.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()
