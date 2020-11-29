def partition(lst, lo, hi):
    global compares, moves

    part = lo
    while lo < hi:
        compares += 1
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
            compares += 1
        compares += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1
            compares += 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]
            moves += 3
        print(lst)
    # Swap part into position
    compares += 1
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        moves += 3
    
    return hi

def rec_qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    global compares, moves
    compares = 0
    moves = 0

    rec_qsort(lst, 0, len(lst) - 1)
    return compares, moves