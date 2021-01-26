#!/usr/bin/env python3

import textwrap
import requests
BASE_URL = "https://aes.cryptohack.org/"
CHALL_URL = "ecbcbcwtf/decrypt/"

flag = "0fb667fdb7ab97718bc4e05b14778a2679c85caefd9fb1829e9ed06a608ef6ecb2a9deab282aab666b23805727112bc0"
flag_blocks = textwrap.wrap(flag,32)[::-1]
print(flag_blocks)


#crypto{3cb_5uck5_4v01d_17_!!!!!}
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

for i in range(len(flag_blocks)-1):
    r = requests.get(f"{BASE_URL}{CHALL_URL}{flag_blocks[i]}")
    decrypted_block = r.json()["plaintext"]
    xord = byte_xor(bytes.fromhex(flag_blocks[i+1]), bytes.fromhex(decrypted_block))
    print(xord)


