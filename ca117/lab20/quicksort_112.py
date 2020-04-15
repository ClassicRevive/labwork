#!/usr/bin/env python3

''' quicksort module '''
def partition(A, p, r):
    # j and q start off at p
    j = q = p

    while j < r:
        # if element at j is less or equal to the pivot
        if A[j] <= A[r]:
            # assign element at j to pivot position
            A[q], A[j] = A[j], A[q]

            q += 1

        j += 1

    # assign pivot to pivot position
    A[r], A[q], = A[q], A[r]
    # return pivot position
    return q

def quicksort(A, p, r):
    # finished once there is nothing to sort
    if r <= p:
        return

    # recursively partition the left and right of the pivot until sorted:
    q = partition(A, p, r)
    quicksort(A, p, q - 1)
    quicksort(A, q + 1, r)


def main():
    a = [32, 24, 12, 38]
    quicksort(a, 0, len(a) - 1)
    print(a)

if __name__ == '__main__':
    main()
