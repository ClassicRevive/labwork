def sumto(a, b):
    if a == b:
        return 0

    # base case
    if a > b - 2:
        return a

    # recursive case
    return a + sumto(a + 1, b)
