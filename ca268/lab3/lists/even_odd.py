#!/usr/bin/env python3

import sys

def get_evenodd_list():
    import sys
    even = []
    odd = []
    for line in sys.stdin:
        number = int(line.rstrip())

        if number == -1:
            break
        elif number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return (odd, even)

def main():
    # call the get_odd_list function and print the result
    odds, evens = get_evenodd_list()
    print(odds)
    print(evens)

if __name__ == "__main__":
    main()