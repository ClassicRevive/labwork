import sys
from LinkedList import LinkedList

def main():
    # Create a list for the tests
    tests = []
    
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items] # Create an array of nums from the strings
    
    ll = LinkedList()

    # Add each number to the list
    for num in nums:
        ll.add(num)
    
    # call the students function
    print(ll.largest(), max(nums))
    tests.append(ll.largest() == max(nums)) # First test ... compare students function to max
    
    # Keep reducing the list, comparing the largest of the reduced list to the remiaining numbers.
    count = 1
    while count == len(nums):
        ll.remove() # Remove one element from the list
        # Compare the largest of this list with the remaining numbers
        tests.append(ll.largest() == max(nums[count:]))
        count += 1
        
    if all(tests):
        print("All tests passed!")
    else:
        for i in range(len(tests)):
            if not tests[i]:
                print("test " + str(i) + " failed.")

    # my own side test
    import random

    for i in range(5):
        test = LinkedList()
        test_l = []
        for j in range(5):
            num = random.randint(0, 25)
            test.add(num)
            test_l.append(num)
        
        print("max in list: {}\nrecursive max: {}".format(max(test_l), test.largest()))


if __name__ == "__main__":
    main()