#!/usr/bin/python3

import sys

def xor(pt, key):
    ct = []
    for c in pt:
        ct.append(c ^ key)

    return ct

def main(pt, key):
    pt_ints = [ord(c) for c in pt]

    encrypted_ints = xor(pt_ints, key)
    encrypted_str = "".join([chr(i) for i in encrypted_ints])
    print(encrypted_str)


pt = sys.argv[1]
key = int(sys.argv[2])
main(pt, key)
