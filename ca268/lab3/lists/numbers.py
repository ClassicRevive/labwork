def get_sliced_lists(lst):
    lst1 = lst[:-1]
    lst2 = lst[1:-1]
    lst3 = lst[::-1]

    return [lst1, lst2, lst3]

def get_evenodd_list():
    import sys
    even = []
    odd = []
    for line in sys.stdin:
        number = int(line.rstrip())

        if number == -1:
            break
        elif number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return (odd, even)

def get_odd_list():
    import sys
    lst = []
    for line in sys.stdin:
        num = int(line.rstrip())

        if num == -1:
            break
        if num % 2 == 1:
            lst.append(num)

    return lst

# return list of integers which are coutns of the lengths of words
# from an input list
def get_counts(lst):
    counts = [0 for i in range(10)]
    
    # get the lengths of words
    for i in lst:
        size = len(i)
        counts[size] += 1

    return counts
    