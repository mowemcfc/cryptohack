#!/usr/bin/python3

e = 65537
p = 17
q = 23
N = p * q

c = pow(12,e,N)
print(c)
