''' More efficeint insertion sort with stats'''

def insertion_sort(lst):
    # No swap version
    comparisons = 0
    moves = 0

    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        moves += 1
        i = todo

        comparisons += 1
        while i > 0 and tobeinserted < lst[i-1]:
            moves += 1
            lst[i] = lst[i-1] # Make space for the item
            if i != 1:  # more comparisons if not at start of list
                comparisons += 1

            i -= 1
        lst[i] = tobeinserted  # Found the place for this item, plonk it in
        moves += 1
    
    return (comparisons, moves)