#!/usr/bin/python3
"""
p = 29
target_a2 = 18

for a in range(10000):
    a2 = (a**2) % p
    print(a2)
    if a2 == target_a2:
        print("MATCH FOUND")
        print(a)
        exit()
"""

p = 29
ints = [14, 6, 11]
for i in ints:
    for a in range(10):
        a2 = (a**2) % p
        if a2 == i:
            print('MATCH FOUND')
            print(a)
            
    

