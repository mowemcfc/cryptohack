#!/usr/bin/python3

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
N = (p-1) * (q-1)
print(N)

# use prev extended euclid with e, totient to find d
