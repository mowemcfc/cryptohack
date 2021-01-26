#!/usr/bin/env python3

from requests import get
import textwrap 
from json import loads, dumps
import binascii
import string

known_pt = "crypto{"
flag = [c for c in known_pt]
blockindex = 2
url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
blocksize = 16
charset = string.ascii_lowercase + string.digits + string.punctuation

def hex2string(h):
    text = bytes(h,'ascii')
    pt = str(binascii.hexlify(text),"ascii")
    return pt

while flag[:-1] != "}":
    pt = hex2string("A"*(blocksize*3-len(flag)-1))
    r = get(f"{url}{pt}")
    target = textwrap.wrap(r.json()["ciphertext"],32)[blockindex]
    for c in charset:
        pt = hex2string("A"*(blocksize*3-len(flag)-1) + "".join(flag) + c)
        r = get(f"{url}{pt}").json()["ciphertext"]
        blocks = textwrap.wrap(r,32)
        block = blocks[blockindex]
        print(f"TARGET: {target} | CHAR: {c} | BLOCK: {block} | FLAG: {''.join(flag)}", end="\r")
        if block == target:
            flag.append(c)
            break

