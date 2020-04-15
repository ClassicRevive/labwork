#!/usr/bin/env python3

from priority_queue_112 import PQ
import sys
m = int(sys.argv[1])

def desc(t):
    return t[1]

def main():
    queue = PQ()
    # read first m elements into the queue
    i = 0
    while i < m:
        num = int(sys.stdin.readline().rstrip())
        queue.insert(num)

        i += 1

    # get the minimum M numbers from stdin
    for element in sys.stdin:
        element = int(element.rstrip())
        if element < queue.getMax():
            queue.insert(element)
            queue.delMax()

    while not(queue.is_empty()):
        # print(queue.d, queue.N)
        print(queue.delMax())


if __name__ == '__main__':
    main()
