import sys

def do_square(n):
 count = 0
 for i in range(n):
    for j in range(n):
        #  Executes n x n times
        count += 1
     # executes n times
 return count

def main(arguments):
    if len(arguments) == 0:
        n = 10
    else:
        inp = arguments[0]
        n = int(inp)

    count = do_square(n)
    print("Count = " + str(count))

if __name__ == '__main__':
    main(sys.argv[1:])
