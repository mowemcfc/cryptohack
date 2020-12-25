#!/usr/bin/python3

from pwn import xor
from Crypto.Util.number import long_to_bytes, bytes_to_long

def main(ct):
    for i in range(1,256):
        key = bytes(chr(i), "utf-8")
        print(xor(ct, key).encode("utf-8")) 
    


ct = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
main(ct)
