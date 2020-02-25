#!/usr/bin/env python3

''' find mean and median of numbers in stdin '''

import sys

def median(a):
    mid = len(a) // 2
    if len(a) % 2 == 0:
        med = (a[mid] + a[mid - 1]) / 2
    else:
        med = a[mid]

    return med


def main():
    numbers = sys.stdin.readlines()  # read in all numbers into an array

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i].rstrip())

    numbers = sorted(numbers)
    # print(numbers)

    my_mean = sum(numbers) / len(numbers)
    my_median = median(numbers)

    print("Mean: {:.1f}\nMedian: {:.1f}".format(my_mean, my_median))

if __name__ == '__main__':
    main()
