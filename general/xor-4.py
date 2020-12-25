#!/usr/bin/python3

from pwn import xor
from Crypto.Util.number import long_to_bytes, bytes_to_long

def main(ct, key_bytes_bytes):
    i = 0
    flag = []
    for c in ct:
        flag.append(chr(c ^ key_bytes[i]))
        i = (i + 1) % len(key)

    print("".join(flag))

ct = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
key = "myXORkey"
key_bytes = bytes(key, "utf-8")
main(ct, key_bytes)
