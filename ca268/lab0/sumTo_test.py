from recursive_sum import sumto

def main():
    # Read two integers from stdin
    a = int(input())
    b = int(input())
    # Call sumto which should recursively sum the integers from a to b-1
    print(sumto(a, b))

if __name__ == "__main__":
    main()