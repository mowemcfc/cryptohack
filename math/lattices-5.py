#!/usr/bin/python3

import numpy as np
import math

def size(v):
    return np.linalg.norm(v)

def main(A):
    v = A[0]
    u = A[1]
    while True:
        if size(u) < size(v):
            w = u
            u = v
            v = w

        m = np.inner(v, u)/ np.inner(v, v)
        m = math.floor(m)


        print('m:', m)
        print(v)
        print(u)
        if m == 0:
            return v, u

        u = u - m*v
    
if __name__ == "__main__":

    A = np.array([[846835985, 9834798552], [87502093, 123094980]])
    res = main(A)
    print(np.inner(res[0],res[1]))

