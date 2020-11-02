#!/usr/bin/env python3

import sys
from LinkedList import LinkedList

def even_count(ll):
    ptr = ll.head
    count = 0
    while ptr != None:
        if ptr.item % 2 == 0:
            count += 1
        ptr = ptr.next

    return count



def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    ll = LinkedList()
    
    for num in nums:
        ll.add(num)
    
    print(even_count(ll))


if __name__ == '__main__':
    main()