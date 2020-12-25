#!/usr/bin/python3
import sys
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)


def main():
    print(gcd(a,b))

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    main()
