#!/usr/bin/python3
from functools import reduce
def main():
    equations = [(2,5), (3,11), (5,17)]
    M = reduce(lambda x, y: x*y, [t[1] for t in equations]) 
    print(M)
    x = 0
    for a, m in equations: 
        b = M // m
        b_inverse = pow(b, -1, m)

        x += (a * b * b_inverse)

    x = x % M
    print(x)

if __name__ == "__main__":
    main()
