import sys
from recursive import is_palindrome

def main():
   for line in sys.stdin:
      # remove end of line
      word = line.strip()
      if len(word) > 0:
         # call recursive function to check if a palindrome
         no = "" if is_palindrome(word) else "not "
         print(word + " is " + no + "a palindrome.")

if __name__ == "__main__":
   main()
