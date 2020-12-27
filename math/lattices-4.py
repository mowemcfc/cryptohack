#!/usr/bin/python3

import numpy as np

def det(A):
    return np.linalg.det(A)


def main(A):
    print(det(A))


if __name__ == "__main__":
    A = np.array([[6,2,-3],[5,1,4],[2,7,1]])
    main(A)
