#!/usr/bin/env python3

def get_sliced_lists(lst):
    lst1 = lst[:-1]
    lst2 = lst[1:-1]
    lst3 = lst[::-1]

    return [lst1, lst2, lst3]

def main():
    # read the list from stdin
    nums = []
    num = int(input())
    while num != -1:
        nums.append(num)
        num = int(input())
        
    # call the student's function with the list of numbers and ...
    lists = get_sliced_lists(nums)
    # ... print the result
    for lst in lists:
        print(lst)

if __name__ == "__main__":
    main()