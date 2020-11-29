from merge_sort_queue import mergesort
from Queue import Queue
import random

#
#   Make a queue from a lst
#
def make_q(lst):
    q = Queue()
    for x in lst:
        q.enqueue(x)
    return q

def issorted(q):
    last = q.dequeue()
    while not q.isempty():
        if last > q.first():
            return False # Two elements out of order
        lst = q.dequeue()

    return True # We got here and so all elemets must have been in order.

def main():
    lst = [10 * x for x in range(101)]
    random.shuffle(lst)
    q = make_q(lst)

    mergesort(q) # This uses the student's merge function to sort q

    if issorted(q):
        print("Test passed")
    else:
        print("Your merge function didn't work.")

if __name__ == "__main__":
    main()