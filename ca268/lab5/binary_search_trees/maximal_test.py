from maximal import is_maximal
from BST import BST

def test(lst):
    bst = BST()

    # Add each element in the lst to the tree
    for n in lst:
        bst.add(n)

    # Print the list and whether or not the resulting tree is maximal
    print("bst.is_maximal(" + str(lst) + ") is " + str(is_maximal(bst)))

def main():
    test([16, 31, 32])
    test([102, 23, 133, 3, 66, 122, 141, 0, 15, 52, 85, 113, 126, 140, 156])

if __name__ == '__main__':
    main()
