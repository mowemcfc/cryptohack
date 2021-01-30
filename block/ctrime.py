#/usr/bin/env python3

import string
import requests
import binascii

BASE_URL = "https://aes.cryptohack.org"
TARGET_URL = "/ctrime/encrypt/"

def hex2string(h):
    text = bytes(h,'ascii')
    pt = str(binascii.hexlify(text),"ascii")
    return pt


def get_ct_len(b):
    b = hex2string(b)
    resp = requests.get(f"{BASE_URL}{TARGET_URL}{3*b}")
    return len(bytes.fromhex(resp.json()["ciphertext"]))


FLAG = "crypto{CRIME_571ll_"
charset  = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation


while '}' not in FLAG:
    cur_len = get_ct_len(FLAG + "`")
    for char in charset:
        print(f"CHAR: {char} | FLAG: {FLAG}", end="     \r", flush=True)
        b = FLAG + char
        try_len = get_ct_len(b)
        if try_len < cur_len:
            FLAG = FLAG + char
            print(f"CHAR: {char} | FLAG: {FLAG}")
            break
