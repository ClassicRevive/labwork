#   Program to check a student's maximum function.
#
import sys
from recursive_max import maximum

# Read in a list from a string of numbers
def get_list(line):
   tokens = line.split()
   # convert the tokens to integers (using a list comprehension)
   return [int(tok) for tok in tokens]

def main():
   line = sys.stdin.readline()
   # remove end of line
   line = line.strip()
   # Convert to a list
   nums = get_list(line)

   # call recursive function to get max of the list.
   print(maximum(nums))

if __name__ == "__main__":
   main()
