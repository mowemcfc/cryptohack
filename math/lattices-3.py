#!/usr/bin/python3

import numpy as np

def proj(u, v):
    return np.inner(u,v) / np.inner(u,u) * u

def main(A):
    B = np.array([A[0], [0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0]])
    for i in range(1,len(A)):
        B[i] = A[i]
        for j in range(0,i):
            B[i] -= proj(B[j], A[i]) 

    return B

if __name__ == "__main__":
    A = np.array([[4.0,1.0,3.0,-1.0], [2.0,1.0,-3.0,4.0], [1.0,0.0,-2.0,7.0], [6.0,2.0,9.0,-5.0]])
    print(main(A))
