'''
BUGS:
1. I had the code getting midpoints of the enitre list rather than the current partition
i.e. lst[len(lst)//2] instead of lst[hi//2]
2. I was getting the wrong sorts when midpoints were as midpoint is hi//2
   this was fixed when i put hi+1//2 as midpoint
3. (lo+hi)//2 now is my midpoint calculation!

'''
def partition(lst, lo, hi):
    global compares, moves


    lst[lo], lst[(lo + hi)//2] = lst[(lo + hi)//2], lst[lo] 
    moves += 3
    part = lo
    # print(lst, lo, hi)
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
            # print("lo and hi swap happened")
            moves += 3
        # print(lst)
    # Swap part into position
    compares += 1
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        # print("partition hi swap happenes", lst[part], lst[hi])
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