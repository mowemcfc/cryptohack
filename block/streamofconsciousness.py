#!/usr/bin/env python3

import requests
import string
from itertools import combinations
BASE_URL = "https://aes.cryptohack.org"
TARGET_URL = "/stream_consciousness/encrypt/"

known = "crypto{"
charset = string.ascii_lowercase + string.digits + string.punctuation
print(charset)

def get():
    resp = requests.get(f"{BASE_URL}{TARGET_URL}")
    return bytes.fromhex(resp.json()["ciphertext"])

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

flag_ct = b''

ciphertexts = [b'\xf2}f\xe0\x1b\xe7h(\xfc\xd1p\xed\x80\xcaA\x19\x82\xd7\xba\xc8^\xd5:\x925r\x1c\xce`\x8bZQL\xb0\t\x91 \xed\xfb\x97\xcb`~\xba\xe8\x1c\x04\xe8R\xbb\xe2`6J{U^\xc4\xa6\xf1\xed\xa1<\x92\xf0\xcb\x08\x02\x06$\xb4\xc5\r\xaeGM\x87\x90\x17(\x19\x12\x0e\xb0\xf3\x7fU\x8d\xce9$\x01#\xeb\x96\x13\x00d\x8d\xcd9\x8e\x8fW\x01BU\x9dX;\xa4w\xfeZ\xdb\xbf\xe0\xb3\xc6', b'\xf2}f\xe0\x1b\xe7h(\xfc\xd1p\xed\x80\xcaA\x19\x82\xd7\xba\xc8^\xd5:\x925r\x1c\xce`\x8bZQL\xb0\t\x91 \xed\xfb\x97\xcb`~\xba\xe8\x1c\x04\xe8R\xbb\xe2`6J{U^\xc4\xa6\xf1\xed\xa1<\x92\xf0\xcb\x08\x02\x06$\xb4\xc5\r\xaeGM\x87\x90\x17(\x19\x12\x0e\xb0\xf3\x7fU\x8d\xce9$\x01#\xeb\x96\x13\x00d\x8d\xcd9\x8e\x8fW\x01BU\x9dX;\xa4w\xfeZ\xdb\xbf\xe0\xb3\xc6', b'\xf1}z\xb3\x1a\xa8 3\xe6\xc7l\xbe\xcb\x85\x15\x1e\x85\x84\xea\xcaV\xc9<\x92:rY\x8f#\xcf\x12\\N\xf9,\xd5%\xec\xfd\xc3\xc2i2\xf7\xe5\x07\x04\xa4@\xf2\xe6k)', b"\xe7f#\xfa\x18\xe7Ig\xe6\xc3q\xbe\xcd\x84LQ\x9c\xcd\xe9\xc3\x1f\xd3'\xdb6pY\x87#\x8bFV^\xb02\xd8+\xea\xee\xc2\x83L~\xb4\xf0\x01F\xf0\x15", b"\xe7f#\xfa\x18\xe7Ig\xe6\xc3q\xbe\xcd\x84LQ\x9c\xcd\xe9\xc3\x1f\xd3'\xdb6pY\x87#\x8bFV^\xb02\xd8+\xea\xee\xc2\x83L~\xb4\xf0\x01F\xf0\x15", b"\xefa#\xf0\x1f\xa9'3\xae\xc0p\xbe\xd8\x85G\x1f\xcb\xcb\xef\xdf\x13\x87*\x8e 5\x10\x9am\xc8SP\x1b\xf2%\x91%\xe5\xf4\x8c\xd1`:\xf9", b'\xef5p\xfb\x1f\xablg\xe2\xcdf\xfb\x8c\x8fC\x14\x99\xdd\xee\xc3V\xc9/\xdb5{\x1d\xce#\xc4F\x1e\\\xf54\x91$\xeb\xf7\xc3\xc1d=\xbc\xbf', b'\xf1zv\xff\x1a\xe7Ig\xe6\xc3c\xfb\x8c\x88P\x1d\x82\xc1\xec\xce[\x87<\x931{Y\x9a%\xcaF\x1er\xb0#\xde9\xee\xfe\xc3\xd1`?\xb4\xf9O\x12\xf1W\xf3\xabjsNgT^\xc4\xaa\xf6\xbf\xbb \x9e\xfe\xc2ANR9\xb3\xceK', b'\xf6pq\xfb\x1f\xb7sg\xe6\xc75\xf6\xcd\x99\x15\x1c\x82\xd7\xe9\xce[\x87<\x9315\r\x9c,\xc2\\\x1eZ\xfe$\x91%\xf1\xba\x81\xc2f5\xf7\xf3\x16A\xea[\xec\xa5.A_}H\r\x89\xaa\xe2\xfa\xf3=\x86\xfa\xc7DFG$\xb5\xcf\x1a\xa8', b'\xef2n\xb3\x0b\xa9h&\xfe\xd2l\xb2\x8c\xa3\x15\x15\x8e\xd7\xff\xd9I\xc2h\x92 9Y\x9a%\xce\x12XZ\xe5,\xc5k\xf1\xba\x8e\xcak;\xfb\xb1\r\x14\xf0\x14\xd2\xacc6K}TL\x94\xb5\xe9\xbf\xb29\x9f\xb7\xda@J\x06#\xbd\xcd\x11\xa5\x15@\xc2\x9d\x0bdT\x1fI', b'\xef2n\xb3\x0b\xa9h&\xfe\xd2l\xb2\x8c\xa3\x15\x15\x8e\xd7\xff\xd9I\xc2h\x92 9Y\x9a%\xce\x12XZ\xe5,\xc5k\xf1\xba\x8e\xcak;\xfb\xb1\r\x14\xf0\x14\xd2\xacc6K}TL\x94\xb5\xe9\xbf\xb29\x9f\xb7\xda@J\x06#\xbd\xcd\x11\xa5\x15@\xc2\x9d\x0bdT\x1fI', b'\xf1}b\xe7^\xa6 )\xef\xd1a\xe7\x8c\x99X\x14\x87\xc8\xba\xdfW\xce;\xdb$t\x10\x809\x8bZ__\xbe', b'\xf1}z\xb3\x1a\xa8 3\xe6\xc7l\xbe\xcb\x85\x15\x1e\x85\x84\xea\xcaV\xc9<\x92:rY\x8f#\xcf\x12\\N\xf9,\xd5%\xec\xfd\xc3\xc2i2\xf7\xe5\x07\x04\xa4@\xf2\xe6k)', b'\xc5gz\xe3\n\xa8{,\xbd\xdb \xa9\xde\xd9\x01\x1c\xb4\xd6\xa9\xde\n\x94\x17\xcaaJ\x1f\xdaz\x9f^C', b"\xf2}q\xf6\x1b\xe7b(\xf7\xd15\xec\xd9\x84[\x18\x85\xc3\xb6\x8bO\xcb)\x82={\x1e\xce,\xdf\x12VT\xe23\xd4?\xae\xba\xb0\xc6w'\xb8\xeb\x07\x00\xa5", b"\xe7f#\xfa\x18\xe7Ig\xe6\xc3q\xbe\xcd\x84LQ\x9c\xcd\xe9\xc3\x1f\xd3'\xdb6pY\x87#\x8bFV^\xb02\xd8+\xea\xee\xc2\x83L~\xb4\xf0\x01F\xf0\x15", b'\xe2gf\xe0\r\xeam&\xe5\xcb{\xf9\x8c\x8b[\x15\xcb\xe9\xf3\xc7S\xce&\x9e&l', b'\xef5p\xfb\x1f\xablg\xe2\xcdf\xfb\x8c\x8fC\x14\x99\xdd\xee\xc3V\xc9/\xdb5{\x1d\xce#\xc4F\x1e\\\xf54\x91$\xeb\xf7\xc3\xc1d=\xbc\xbf', b'\xe4`w\xb37\xe7w.\xe2\xce5\xed\xc4\x85BQ\x83\xcd\xf7\x85', b'\xef5p\xfb\x1f\xablg\xe2\xcdf\xfb\x8c\x8fC\x14\x99\xdd\xee\xc3V\xc9/\xdb5{\x1d\xce#\xc4F\x1e\\\xf54\x91$\xeb\xf7\xc3\xc1d=\xbc\xbf', b'\xf1}z\xb3\x1a\xa8 3\xe6\xc7l\xbe\xcb\x85\x15\x1e\x85\x84\xea\xcaV\xc9<\x92:rY\x8f#\xcf\x12\\N\xf9,\xd5%\xec\xfd\xc3\xc2i2\xf7\xe5\x07\x04\xa4@\xf2\xe6k)', b"\xf2}q\xf6\x1b\xe7b(\xf7\xd15\xec\xd9\x84[\x18\x85\xc3\xb6\x8bO\xcb)\x82={\x1e\xce,\xdf\x12VT\xe23\xd4?\xae\xba\xb0\xc6w'\xb8\xeb\x07\x00\xa5"]


while len(ciphertexts) != 22:
    ciphertexts.append(get())
   

for a,b in combinations(ciphertexts,2):
    pt = byte_xor(byte_xor(a,b), b'crypto{k3y57r34m_r3u53_15_f47')
    if b'Three' in pt:
        key = byte_xor(a, b'crypto{k3y57r34m_r3u53_15_f47')

print(f"partial key: {key.hex()}")

def update_pts():
    plaintexts = []
    for ct in ciphertexts:
        pt = byte_xor(key,ct)
        plaintexts.append(pt)
        if b'crypto{' in pt:
            flag_ct = ct
            print(ct.hex())
    return plaintexts, flag_ct


while len(key) != 32:
    plaintexts, flag_ct = update_pts()
    for i, pt in enumerate(plaintexts):
        print(f" i: {i} | pt: {pt}")
    index = int(input("choose text: "))
    cur_pt = plaintexts[index]
    c = input("guess next char: ")
    key += bytes([ord(c) ^ ciphertexts[index][len(key)]])
    print(f'current key: {key.hex()} | flag = {byte_xor(flag_ct,key)}')