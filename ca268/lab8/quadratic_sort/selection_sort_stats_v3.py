def selection_sort(lst):
    compares = 0
    moves = 0

    lo = 0
    hi = len(lst) - 1

    while lo < hi:
        min_index = lo
        max_index = lo
        for j in range(lo + 1, hi + 1):
            if lst[j] < lst[min_index]:
                min_index = j
                compares += 1
            elif lst[j] > lst[max_index]: # maybe >= to get stable sort
                max_index = j
                compares += 2
            if lst[min_index] < lst[j] < lst[max_index]:
                compares += 2


        if max_index == lo:
            max_index = min_index   # We will be moving lst[lo] to min_index, so update max_index first
        #compares += 1

        # swap min index with lo ... place smallest at the first
        moves += 3
        lst[lo], lst[min_index] = lst[min_index], lst[lo]
        # swap max index with hi ... place largest at the end
        moves += 3
        lst[hi], lst[max_index] = lst[max_index], lst[hi]
        lo += 1
        hi -= 1

    return (compares, moves)