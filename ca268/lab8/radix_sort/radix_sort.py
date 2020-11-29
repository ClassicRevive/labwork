def radix_sort(lst, passnum):
   # for each power of two (starting at lowest) sort based on that power
    """ this function will sort lst using radixsort up to the required number of passes.
    Note that the first pass we will sort on the least significant bit.
    """

    i = 0
    while i < passnum:
        for p in range(32):  # Assume 6 bits
            # Split list in two
            lo = [x for x in lst if x & (1 << p) == 0] # lo where the bit is zero
            hi = [x for x in lst if x & (1 << p) != 0] # hi where the bit is one
            lst = lo + hi # combine the two into one list.
            
            # You need to work out when to stop and also you have to return the lst.
            
            i += 1
            if i >= passnum:
                break

    return lst