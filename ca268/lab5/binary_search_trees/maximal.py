#
# Test whether the BST is maximal
# height and count methods are available
#

from BST import BST

def is_maximal(bst):
    return (2 ** (bst.height()) - 1) == bst.count()

