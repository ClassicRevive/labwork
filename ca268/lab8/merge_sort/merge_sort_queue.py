from Queue import Queue


def split(q):
    q1 = Queue()
    q2 = Queue()

    cutoff = len(q) // 2  # halfway mark
    
    for i in range(cutoff):
        q1.enqueue(q.dequeue())
    while not q.isempty():
        q2.enqueue(q.dequeue())

    return q1, q2

def merge(q1, q2, q):
    i = j = 0

    n = len(q1)
    m = len(q2)

    while (i + j) < (n + m):
        #print(q1.isempty())
        #print(len(q1))
        if (q2.isempty() and not(q1.isempty())) or (not(q1.isempty()) and (q1.first() < q2.first())):
            #print("{} added".format(q1.first()))
            q.enqueue(q1.dequeue())
            i += 1
        else:
            #print("{} added".format(q2.first()))
            q.enqueue(q2.dequeue())
            j += 1

def merge2(q1, q2, q):
    while not(q1.isempty()) and not(q2.isempty()):
        if q1.first() < q2.first():
            q.enqueue(q1.dequeue())
        else:
            q.enqueue(q2.dequeue())

    # empty the other queue
    while not(q1.isempty()):
        q.enqueue(q1.dequeue())

    while not(q2.isempty()):
        q.enqueue(q2.dequeue())


def mergesort(q):
    if len(q) < 2:
        return # Base case. No work to do for one element.

    # Split q into two smaller queues
    q1, q2 = split(q) # You will supply the split function

    # recursively sort these as well
    mergesort(q1)
    mergesort(q2)

    # Now, merge these together back into q
    merge(q1, q2, q)

def main():
    q = Queue()
    q.enqueue(2)
    q.enqueue(1)
    q.enqueue(4)
    q.enqueue(3)


    mergesort(q)

    while not q.isempty():
        print(q.dequeue())


if __name__ == '__main__':
    main()