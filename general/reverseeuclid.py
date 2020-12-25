#!/usr/bin/python3

import sys

def gcdExtended(a,b):
    if a == 0:
        return b,0,1

    gcd,x1,y1 = gcdExtended(b % a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd,x,y

def main(a,b):
    gcd,x1,y1 = gcdExtended(a,b)

    print(x1, y1)

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    main(a,b)
