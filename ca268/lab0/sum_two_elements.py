
''' find all pairs in a list that add to k'''

# the j axis must be parsed within the range [i + 1:] 
# to prevent double counting

def sum_to_k(ls, k):
    for i in range(len(ls)):
        for j in range(len(ls[i + 1:])):
            if ls[i] + ls[i + 1:][j] == k:
                print(ls[i], ls[i + 1:][j])

def main():
    sum_to_k([60, 6, 10, 8, 5], 15)

if __name__ == '__main__':
    main()
n