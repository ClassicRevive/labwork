# another interesting insertion sort implementation

def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    comparisons = 0
    swaps = 0
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        
        comparisons +=1
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            swaps += 1
            if i != 1:
                comparisons += 1
            i -= 1

    return (comparisons, swaps)
