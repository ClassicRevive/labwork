import sys
from LinkedList import LinkedList

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    
    ll = LinkedList()
    problem = False
    if ll.is_present(item)(items[0]):
        print("An empty list should not match anything")
        problem = True
    
    else:
        for item in items:
            if ll.is_present(item)(item):
                print(item + " detected before being added.")
                problem = True
            ll.add(item)
            
        # Now every item in the items should be in the list.
        for item in items:
            if not ll.is_present(item): # item should not be contained
                print(item + " not found in list.")
                problem = True

    if not problem:
        # check that the list still contains all the items
        while not ll.is_empty() and len(items) > 0:
            if ll.remove() != items.pop():
                print("List has been modified")
                problem = true
                break
        
        if not problem:
            if (not ll.is_empty()) or len(items) != 0:
                print("the list size is wrong");
                problem = True
                
    if problem:
        print("More work nned!")
    else:
        print("all ok!")

if __name__ == "__main__":
    main()