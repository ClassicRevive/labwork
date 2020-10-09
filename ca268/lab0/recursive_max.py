def maxi(a, b):
   if a >= b:
      return a
   else:
      return b

def maximum(l):
    # base case
    if len(l) == 1:
        return l[0]

    # recursive case:
    return maxi(l[0], maximum(l[1:]))
