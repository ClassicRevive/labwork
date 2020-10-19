#!/usr/bin/env python3



def get_odd_list():
    import sys
    lst = []
    for line in sys.stdin:
        num = int(line.rstrip())

        if num == -1:
            break
        if num % 2 == 1:
            lst.append(num)

    return lst


def main():
    # call the get_odd_list function and print the result
    odds = get_odd_list()
    print(odds)

if __name__ == "__main__":
    main()
