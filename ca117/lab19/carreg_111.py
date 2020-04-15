from re import findall
import sys


car = r"\b\d{2}[12]\s(?:C|C[ECNW]|D|D[L]|G|K[EKY]|L|L[DHMS]|M[HNO]|OY|RN|SO|T|W|W[HXW])\s[1-9]\d{0,5}\b"

def main():

    # Verify regular expression is not overly long
    assert(len(car) < 120)

    s = sys.stdin.read()

    carlist = findall(car, s)
    print('Cars: {}'.format(carlist))

if __name__ == '__main__':
    main()
