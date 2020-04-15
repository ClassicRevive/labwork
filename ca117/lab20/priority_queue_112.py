#!/usr/bin/env python3


class PQ(object):

    def __init__(self):
        self.d = {}
        self.N = 0

    # insert an element into priority queue
    def insert(self, v):
        self.N += 1
        self.d[self.N] = v
        self.swim(self.N)

    # swap elements at 2 nodes based on key
    def exch(self, i, j):
        self.d[i], self.d[j] = self.d[j], self.d[i]

    # move element up the tree into position
    def swim(self, k):
        # while k is not root and k > parent
        while k > 1 and self.d[k // 2] < self.d[k]:
            self.exch(k, k // 2)
            # reassign k's position
            k = k // 2

    # remove the maximum element from the tree and return it
    def delMax(self):
        v = self.d[1]
        # swap elements at 1 and N
        self.exch(1, self.N)
        del(self.d[self.N])
        self.N -= 1
        # sink the curret first element into its position
        self.sink(1)
        return v

    def bigger(self, i, j):
        try:
            return max([i, j], key=self.d.__getitem__)
        except KeyError:  # if no right branch exists, return the left branch
            return i

    def sink(self, k):
        # while there are still children
        while (k * 2 <= self.N):
            j = 2 * k  # child position
            j = self.bigger(j, j + 1)
            # if the element at k is greater than children nodes
            if self.d[k] > self.d[j]:
                break

            self.exch(k, j)
            k = j

    def getMax(self):
        return self.d[1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.N

def main():
    pq = PQ()
    pq.insert(5)
    pq.insert(6)
    pq.insert(12)
    pq.insert(3)
    pq.insert(15)
    pq.insert(9)
    print(pq.d)

if __name__ == '__main__':
    main()